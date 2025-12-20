import pickle
import random
import numpy as np
from music21 import instrument, note, chord, stream
from keras.models import load_model

SEQUENCE_LENGTH = 50
MODEL_FILE = "model.keras"
NOTES_FILE = "notes.pkl"


def generate_music():
    model = load_model(MODEL_FILE)

    with open(NOTES_FILE, "rb") as f:
        notes = pickle.load(f)

    pitchnames = sorted(set(notes))
    note_to_int = {note: i for i, note in enumerate(pitchnames)}
    int_to_note = {i: note for i, note in enumerate(pitchnames)}

    if len(notes) <= SEQUENCE_LENGTH:
        raise Exception("Not enough notes to generate music")

    start = random.randint(0, len(notes) - SEQUENCE_LENGTH - 1)
    pattern = notes[start:start + SEQUENCE_LENGTH]
    prediction_output = []

    for _ in range(200):
        input_seq = np.reshape(
            [note_to_int[n] for n in pattern],
            (1, SEQUENCE_LENGTH, 1)
        )
        input_seq = input_seq / float(len(pitchnames))

        prediction = model.predict(input_seq, verbose=0)
        index = np.argmax(prediction)
        result = int_to_note[index]

        prediction_output.append(result)
        pattern.append(result)
        pattern = pattern[1:]

    # Create MIDI
    offset = 0
    output_notes = []

    for pattern in prediction_output:
        if '.' in pattern:
            notes_in_chord = pattern.split('.')
            notes_objs = [note.Note(int(n)) for n in notes_in_chord]
            new_chord = chord.Chord(notes_objs)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    output_file = "generated_music.mid"
    midi_stream.write("midi", fp=output_file)

    return output_file
