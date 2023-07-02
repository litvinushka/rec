from flask import Flask, render_template, send_file, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)

audio_files = []  # Список аудиозаписей

@app.route('/')
def index():
    return render_template('play.html')

@app.route('/upload', methods=['POST'])
def upload_audio_file():
    audio_file = request.data

    # Сохранение аудиофайла на сервере
    with open('uploaded_audio.wav', 'wb') as file:
        file.write(audio_file)

    # Добавление аудиозаписи в список
    audio_files.append('uploaded_audio.wav')

    # Отправка списка аудиозаписей на клиент
    socketio.emit('audio_list', audio_files, broadcast=True)

    return 'Audio file uploaded successfully.'

@app.route('/audio')
def get_audio_file():
    # Возвращение сохраненного аудиофайла
    return send_file('uploaded_audio.wav', mimetype='audio/wav')

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    # Отправка списка аудиозаписей при подключении клиента
    socketio.emit('audio_list', audio_files)

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('audio_data')
def handle_audio_data(data):
    # Обработка аудио данных
    print("Received audio data:", data)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)