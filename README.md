# TuneForge Notes Converter Microservice

A sophisticated microservice that converts raw frequency data into professional-grade MIDI files using advanced musical theory algorithms. Part of the TuneForge platform's audio generation pipeline.

## Technical Overview

This microservice specializes in:
1. Frequency to MIDI note conversion
2. Polyphonic chord processing
3. Musical timing and tempo management
4. Professional MIDI file generation

### Musical Processing Architecture

The service implements advanced musical processing:
- Logarithmic frequency to MIDI note conversion
- Multi-track MIDI composition
- Dynamic instrument selection
- Precise tempo and timing control
- Polyphonic chord handling

## Technical Challenges & Solutions

### 1. Musical Accuracy
**Challenge:** Converting raw frequencies to precise MIDI notes
**Solution:** 
- Implemented logarithmic frequency conversion
- Round-to-nearest MIDI note calculation
- Precise mathematical formulas for note conversion

### 2. Polyphonic Processing
**Challenge:** Handling multiple simultaneous notes (chords)
**Solution:**
- Multi-note track management
- Parallel note processing
- Synchronized timing control

### 3. Performance Optimization
**Challenge:** Processing complex musical data efficiently
**Solution:**
- Optimized algorithms for note conversion
- Efficient MIDI file generation
- Streamlined cloud storage integration

## Technology Stack

- **MIDI Processing:** MIDIUtil
- **Mathematical Processing:** Python math library
- **Cloud Storage:** Azure Blob Storage
- **API Framework:** Flask
- **Container:** Docker
- **CI/CD:** GitHub Actions

## Project Structure
```
.
├── README.md
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── storage/                  # Azure storage integration
├── Dockerfile                # Container configuration
└── .github/                  # CI/CD workflows
```

## Setup and Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd TuneForge-NotesConverter-ms
```

2. Set up environment variables:
```bash
export AZURE_STORAGE_CONNECTION_STRING="your-connection-string"
export BLOB_CONTAINER_NAME="your-container-name"
```

3. Local Development Setup:
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the service
python -m flask run
```

4. Docker Deployment:
```bash
docker build -t tuneforge-notesconverter .
docker run -p 5000:5000 tuneforge-notesconverter
```

## Musical Features

1. **Note Processing:**
   - Frequency to MIDI conversion
   - Support for frequencies from 8Hz to 12.5kHz
   - Precise mathematical conversion

2. **Tempo Control:**
   - Dynamic tempo adjustment
   - Speed multiplier support
   - Beat synchronization

3. **Instrument Support:**
   - Multiple instrument selection
   - General MIDI standard compliance
   - Channel volume control

## CI/CD Pipeline

Automated deployment workflow using GitHub Actions:
- Builds Docker image
- Runs tests
- Publishes to container registry
- Deploys to both main and develop environments

## Best Practices

1. **Musical Accuracy:**
   - Precise mathematical conversions
   - Professional-grade MIDI generation
   - Accurate tempo management

2. **Code Quality:**
   - Comprehensive error handling
   - Efficient algorithms
   - Clean code structure

3. **Performance:**
   - Optimized processing
   - Efficient memory usage
   - Fast response times