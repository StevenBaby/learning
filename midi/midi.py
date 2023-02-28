# coding=utf-8

import mido
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(
    figsize=(18, 9),
)
ax = fig.add_subplot()
plt.pause(0.001)
messages = []

melody_note = 0
chord_note = 0

with mido.open_input("Keystation 61 MK3 2") as inport, \
        mido.open_output("loopMIDI Port 2 2") as out:
    for msg in inport:
        print(f"\r{msg}", end='')
        out.send(msg)
        if not hasattr(msg, 'note'):
            continue

        messages.append(msg)

        x = np.linspace(1, 100, 100)
        chords = np.zeros_like(x)
        melody = np.zeros_like(x)

        for idx, msg in enumerate(messages[-100:]):
            if msg.note >= 60:
                melody_note = msg.note
            else:
                chord_note = msg.note
            melody[idx] = melody_note
            chords[idx] = chord_note

        ax.clear()
        ax.plot(x, melody)
        ax.plot(x, chords)
        ax.scatter(x, melody)
        ax.scatter(x, chords)
        ax.set_ylim(0, 100)

        plt.pause(0.0001)
