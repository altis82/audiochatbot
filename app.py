from flask import Flask, request, jsonify, render_template  # Add render_template here
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from chat import chatgpt
app = Flask(__name__)
recognizer = sr.Recognizer()
@app.route('/')
def home():
    # This will render the `index.html` file from the `templates` directory
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files['audio']
    audio_data = BytesIO(audio_file.read())
    
    # Convert audio file to WAV format if necessary
    audio_segment = AudioSegment.from_file(audio_data)
    audio_segment.export("temp.wav", format="wav")
    
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)
        
    try:
        transcription = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        transcription = "Could not understand audio"
    except sr.RequestError:
        transcription = "API unavailable"
    
    output = chatgpt(transcription)
    print(transcription)
    return jsonify({"transcription": transcription, "output":output})

if __name__ == '__main__':
    app.run(debug=True)
