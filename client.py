import websocket
server_url = "ws://127.0.0.1/:5000"
def send_audio_file_to_server(server_url, audio_file_path):
    ws = websocket.create_connection(server_url)

    try:
        with open(audio_file_path, 'rb') as file:
            audio_data = file.read()

        ws.send(audio_data)
        print("Audio file sent successfully.")
    except FileNotFoundError:
        print(f"File not found: {audio_file_path}")
    except Exception as e:
        print("An error occurred while sending the audio file.")
        print(e)

    ws.close()
audio_file_path = "audio.wav"
send_audio_file_to_server(server_url, audio_file_path)