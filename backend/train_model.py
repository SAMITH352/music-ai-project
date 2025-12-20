import os
import glob
import pickle
import numpy as np
from music21 import converter, instrument, note, chord
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.utils import to_categorical

# ---------------- CONFIG ----------------
MIDI_FOLDER = "midi_songs"
SEQUENCE_LENGTH = 50
MODEL_FILE = "model.keras"
NOTES_FILE = "notes.pkl"
# ----------------------------------------


def get_notes():
    notes = []

    print("🎵 Reading MIDI files...")

    midi_files = glob.glob(os.path.join(MIDI_FOLDER, "*.mid"))
    print("📂 MIDI files found:", midi_files)

    if not midi_files:
        raise Exception("❌ No MIDI files found")

    for file in midi_files:
        print(f"➡ Parsing: {file}")
        try:
            midi = converter.parse(file)

            # FLATTEN EVERYTHING (THIS IS THE KEY FIX)
            elements = midi.flatten().notes

            for element in elements:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

        except Exception as e:
            print(f"⚠️ Skipped {file} → {e}")

    print(f"🎼 Notes extracted: {len(notes)}")

    if len(notes) < SEQUENCE_LENGTH:
        raise Exception("❌ Not enough notes extracted to train")

    return notes


def prepare_sequences(notes):
    pitchnames = sorted(set(notes))
    note_to_int = {note: i for i, note in enumerate(pitchnames)}

    network_input = []
    network_output = []

    for i in range(len(notes) - SEQUENCE_LENGTH):
        seq_in = notes[i:i + SEQUENCE_LENGTH]
        seq_out = notes[i + SEQUENCE_LENGTH]

        network_input.append([note_to_int[n] for n in seq_in])
        network_output.append(note_to_int[seq_out])

    network_input = np.reshape(
        network_input, (len(network_input), SEQUENCE_LENGTH, 1)
    )
    network_input = network_input / float(len(pitchnames))
    network_output = to_categorical(network_output)

    return network_input, network_output, pitchnames


def build_model(input_shape, output_size):
    model = Sequential()
    model.add(LSTM(256, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(256))
    model.add(Dropout(0.3))
    model.add(Dense(256, activation="relu"))
    model.add(Dense(output_size, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model


def main():
    notes = get_notes()

    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes, f)

    network_input, network_output, pitchnames = prepare_sequences(notes)

    model = build_model(
        (network_input.shape[1], network_input.shape[2]),
        network_output.shape[1]
    )

    print("🚀 Training model...")
    model.fit(network_input, network_output, epochs=20, batch_size=64)

    model.save(MODEL_FILE)
    print("✅ MODEL TRAINED AND SAVED")


if __name__ == "__main__":
    main()
