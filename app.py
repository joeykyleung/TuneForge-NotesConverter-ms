import math
import logging

from flask import Flask, request
import midiutil
from storage import azureStorage
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


def get_midi_number(frequency: float):
    return round(12*math.log2(frequency/440) + 69)


@app.route('/', methods=['POST'])
def create():
    data = request.get_json()
    chords = data['notes']
    speed = int(data['speed'] * 120)
    instrument = int(data['instrument'])
    output_file = data['midi_filename']
    midis = []
    for chord in chords:
        midis.append([get_midi_number(note) for note in chord])

    try:
        create_midi_file(midis, speed, instrument, output_file)
    except Exception as e:
        app.logger.error(e)
        return "Error", 500
    return output_file, 201


def create_midi_file(chords, tempo, instrument, output_file):
    app.logger.info("Creating midi from chords:" + str(chords))
    # Create a MIDI file
    midi_file = midiutil.MIDIFile(1)

    # Set the tempo and track name
    track = 0
    channel = 0
    track_name = "Music Notes"

    # Add track name and tempo to the MIDI file
    midi_file.addTrackName(track, 0, track_name)
    midi_file.addTempo(track, 0, tempo)

    # Add notes to the MIDI file
    time = 0
    duration = 1

    midi_file.addProgramChange(track, channel, time, instrument)

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

    app.logger.info('Attempting to upload midi file to blob storage as '
                 + output_file)
    azureStorage.upload(temp_file_name, output_file)
    os.remove(temp_file_name)


