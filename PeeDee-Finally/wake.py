import pyttsx3 as tts 
import speech_recognition as sr 
import ttspeak

WAKE_WORD = "xin chào"
GREETING = "pi đi nghe nè"
def listen_for_wake_word():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hệ thống đang chờ từ kích hoạt...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Điều chỉnh cho tiếng ồn xung quanh

        while True:
            try:
                print("Lắng nghe...")
                audio = recognizer.listen(source)

                text1 = recognizer.recognize_google(audio, language="vi-US").lower()
                print(f"Bạn đã nói: {text1}")

                if WAKE_WORD in text1:
                    print("Từ kích hoạt được phát hiện!")
                    ttspeak.text_to_speak(GREETING)
                    break

            except sr.UnknownValueError:
                print("Không hiểu giọng nói, vui lòng thử lại.")
            except sr.RequestError as e:
                print(f"Lỗi kết nối đến dịch vụ nhận diện giọng nói: {e}")
                break