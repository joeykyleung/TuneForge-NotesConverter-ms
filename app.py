from flask import Flask
import midiutil

app = Flask(__name__)


@app.route('/')
def create():  # put application's code here
    chords = [[60, 64, 67], [62, 65, 69], [64, 67, 71], [65, 69, 72], [60]]
    output_file = "input.mid"
    create_midi_file(chords, output_file)
    return "Hello World!"


def create_midi_file(chords, output_file):
    # Create a MIDI file
    midi_file = midiutil.MIDIFile(1)

    # Set the tempo and track name
    track = 0
    channel = 0
    tempo = 60
    track_name = "Music Notes"

    # Add track name and tempo to the MIDI file
    midi_file.addTrackName(track, 0, track_name)
    midi_file.addTempo(track, 0, tempo)

    # Add notes to the MIDI file
    time = 0
    duration = 1

    # Set the instrument
    program = 1  # Change this to the desired instrument program number
    midi_file.addProgramChange(track, channel, time, program)

    for chord in chords:
        for note in chord:
            midi_file.addNote(track, channel, note, time, duration, volume=100)
        time += 1
    # for note in notes:
    #     midi_file.addNote(track, channel, note, time, duration, volume=100)
    #     time += 1

    # Save the MIDI file
    with open(output_file, 'wb') as file:
        midi_file.writeFile(file)
