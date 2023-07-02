from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_audio_file():
    audio_file = request.data

    # Сохранение аудиофайла на сервере
    with open('uploaded_audio.wav', 'wb') as file:
        file.write(audio_file)

    return 'Audio file uploaded successfully.'

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('audio_data')
def handle_audio_data(data):
    # Обработка аудио данных
    print("Received audio data:", data)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)
