import asyncio
import websockets
import speech_recognition as sr

# def recognize_speech(audio_data):
#     recognizer = sr.Recognizer()
#     with sr.AudioData(audio_data, offset=0, duration=None) as source:
#         audio = recognizer.record(source, duration=60)  # Thu âm tối đa 5 giây
#         try:
#             text = recognizer.recognize_google(audio, language="vi-VN")
#             print(f"Recognized speech: {text}")
#             return text
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")

async def receive_audio_data(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(f"Received audio data from ESP32: {message}\n")
        except websockets.ConnectionClosed:
            print("Connection to ESP32 closed")
            break

async def main():
    uri = "ws://192.168.4.1:81"
    try:
        async with websockets.connect(uri, timeout=30) as websocket:
            await receive_audio_data(websocket)
    except TimeoutError:
        print(f"Failed to connect to {uri}: Timeout")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
