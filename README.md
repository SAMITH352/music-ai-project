# Music AI Generator

A machine learning-powered music generation application that creates original MIDI music using Long Short-Term Memory (LSTM) neural networks trained on classical piano compositions.

## Features

- **AI-Powered Music Generation**: Uses deep learning to generate new musical compositions
- **MIDI Output**: Generates music in standard MIDI format playable by any MIDI-compatible software
- **Web Interface**: Simple web-based interface for easy music generation
- **REST API**: Backend API for programmatic access to music generation

## Technologies Used

### Backend
- **Python**: Core programming language
- **TensorFlow/Keras**: Deep learning framework for LSTM model
- **Flask**: Web framework for API
- **Music21**: Music theory and MIDI processing library
- **NumPy**: Numerical computing

### Frontend
- **HTML/CSS/JavaScript**: Simple web interface
- **Fetch API**: For communicating with the backend

## Project Structure

```
music_ai_project/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── generate_music.py      # Music generation logic
│   ├── train_model.py         # Model training script
│   ├── requirements.txt       # Python dependencies
│   ├── model.keras           # Trained neural network model
│   ├── notes.pkl             # Serialized training data
│   ├── generated_music.mid   # Sample generated music
│   └── midi_songs/           # Training MIDI files
│       ├── piano_sonata_310_1_(c)oguri.mid
│       ├── piano_sonata_310_2_(c)oguri.mid
│       └── piano_sonata_310_3_(c)oguri.mid
├── frontend/
│   ├── index.html            # Web interface
│   ├── script.js             # Frontend JavaScript
│   └── style.css             # Styling
└── run.txt                   # Setup and run instructions
```

## Installation & Setup

### Prerequisites
- Python 3.7+
- Virtual environment support

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install flask flask-cors tensorflow music21 numpy
   ```

4. Train the model (if needed):
   ```bash
   python train_model.py
   ```

5. Start the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Start a simple HTTP server:
   ```bash
   python -m http.server 5500
   ```

3. Open your browser and go to `http://localhost:5500`

## Usage

1. Ensure both backend (Flask) and frontend (HTTP server) are running
2. Open the web interface in your browser
3. Click the "Generate Music" button
4. The generated MIDI file will automatically download
5. Play the MIDI file using any MIDI-compatible player or software

### API Usage

You can also generate music programmatically by calling the backend API:

```bash
curl -X GET http://127.0.0.1:5000/generate -o generated_music.mid
```

## How It Works

1. **Training Phase**:
   - MIDI files are parsed to extract musical notes and chords
   - Sequences of 50 notes are created as training data
   - An LSTM neural network is trained to predict the next note in a sequence

2. **Generation Phase**:
   - The trained model predicts a sequence of 200 notes
   - Predictions are converted back to musical notes and chords
   - A new MIDI file is created with the generated sequence

3. **MIDI Creation**:
   - Notes are assigned to piano instrument
   - Each note/chord has a duration of 0.5 beats
   - The complete sequence forms a musical composition

## Model Details

- **Architecture**: Two LSTM layers (256 units each) with dropout
- **Sequence Length**: 50 notes for input
- **Output**: 200 notes generated per composition
- **Training Data**: Classical piano sonatas (Beethoven's Piano Sonata No. 14)

## Troubleshooting

- **No MIDI files found**: Ensure MIDI files are placed in `backend/midi_songs/`
- **Model training fails**: Check that you have sufficient MIDI data (at least 51 notes)
- **Generation errors**: Verify the model.keras and notes.pkl files exist
- **CORS issues**: Ensure Flask-CORS is installed and configured



## License

This project is for educational and personal use. Please respect copyright laws when using MIDI files for training.

## Author

Samith</content>
<parameter name="filePath">c:\Users\samit\Downloads\Code_Alpha projects\music_ai_project\README.md
