import math

from flask import Flask, request
import midiutil
from storage import azureStorage
import os

app = Flask(__name__)


def get_midi_number(frequency: float):
    return round(12*math.log2(frequency/440) + 69)

@app.route('/', methods=['POST'])
def create():  # put application's code here
    data = request.get_json()
    chords = data['notes']
    speed = data['speed']
    midis = []
    for chord in chords:
        midis.append([get_midi_number(note) for note in chord])
    print(midis)
    output_file = "output.mid"
    try:
        create_midi_file(midis, output_file)
    except Exception as e:
        print(e)
        return "Error", 500
    return "Success", 201


def create_midi_file(chords, output_file):
    print("Creating midi from chords:" + str(chords))
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
    temp_file_name = 'temp_out.mid'
    with open(temp_file_name, 'wb') as file:
        midi_file.writeFile(file)

    azureStorage.upload('temp_out.mid', output_file)
    os.remove(temp_file_name)


