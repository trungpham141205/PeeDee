import google.generativeai as genai
from datetime import datetime, date 
import re
import pyttsx3 as tts 
import speech_recognition as sr
from bs4 import BeautifulSoup
import requests
import ttspeak
import pytz
GOOD_BYE = "tạm biệt"
headers = {
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux armv7l; rv:78.0) Gecko/20100101 Firefox/78.0'
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
def get_audio():
    while True:
        ear_robot = sr.Recognizer()
        with sr.Microphone() as source:
            print("Trợ Lý Ảo: Đang nghe...")

            audio = ear_robot.listen(source)

            try:
                text1 = ear_robot.recognize_google(audio, language="vi-VN")
                print("Tôi: ", text1)
                #speak(text)
                convo.send_message(text1) 
                if( "Bạn" in text1 and  "tên" in text1) or( "bạn" in text1 and "tên" in text1) or ("bạn" in text1 and "Tên" in text1) : 
                    str = "tôi là Pi Đi"
                    print(str) 
                    ttspeak.text_to_speak(str)
                elif text1==("Bây giờ là mấy giờ" or " Mấy giờ rồi"):
                    ans= datetime.now().strftime('%H:%M:%S')
                    print(ans)
                    ttspeak.text_to_speak(ans)
                elif "mấy giờ" in text1:
                    ttspeak.text_to_speak("Bạn muốn biết thời gian ở lục địa thành phố nào")
                    print("Bạn muốn biết thời gian ở lục địa thành phố nào")
                    with sr.Microphone() as source2:  # Ghi âm mới
                        print("lắng nghe...")
                        audio2 = ear_robot.listen(source2)  # Ghi lại âm thanh mới
                        text2 = ear_robot.recognize_google(audio2, language="vi-VN")
                        city = text2
                        print("Tôi: " + city)
                        time = soup.select('#wob_dts')[0].getText().strip()
                        print(time)
                        ttspeak.text_to_speak(time)
        #                 if city == "Asia Hồ Chí Minh":
        #                     city = "Asia Ho_Chi_Minh"
        #                 elif city == "America New York":
        #                     city="America New_York"
        #                 def get_timezone(city):
        #                     match = re.search(r"(\w+) (\w+)", city)
        #                     if match:
        #                         continent, city = match.groups()
        #                         timezone = f"{continent}/{city}"
        #                     else:
        #                         return None
        #                 if timezone:
        # # ... xử lý như bình thường với timezone
        #                     timezone = pytz.timezone(timezone)  # Sử dụng kết quả từ get_timezone
        #                     now_utc = datetime.datetime.now(datetime.timezone.utc)
        #                     now_local = now_utc.astimezone(timezone)
        #                     print(now_local.strftime("%Y-%m-%d %H:%M:%S"))
        #                 else:
        #                     print("Định dạng nhập liệu không hợp lệ.")
                elif "Hôm nay là thứ mấy" in text1 or "Hôm nay là ngày bao nhiêu" in text1:
                    ans1=date.today().strftime("%B %d, %Y")
                    print(ans1)
                    ttspeak.text_to_speak(ans1)
                elif "thời tiết" in text1:
                    ttspeak.text_to_speak("Bạn muốn biết thời tiết ở quốc gia nào")
                    print("Bạn muốn biết thời tiết ở quốc gia nào")
                    # time.sleep(200)
                    text3 = ear_robot.recognize_google(audio, language="vi-VN")
                    city_name = text3
                    print(city_name)
                    try:
                        res = requests.get(f'https://www.google.com/search?q={city_name}&oq={city_name}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
      
                        print("Loading...")
 
                        soup = BeautifulSoup(res.text, 'html.parser')
                        location = soup.select('#wob_loc')[0].getText().strip()
                        info = soup.select('#wob_dc')[0].getText().strip()
                        temperature = soup.select('#wob_tm')[0].getText().strip()
                        print("Temperature: " + temperature + "°C")
                        ttspeak.text_to_speak(temperature)
                        print("Weather Description: " + info)
                        ttspeak.text_to_speak(info)
                    except:
                        print("Please enter a valid city name")

                else:
                    clean_special_characters =convo.last.text.replace('*','')
                    print(clean_special_characters) 
                    ttspeak.text_to_speak(clean_special_characters)

                if text1==GOOD_BYE:
                    ttspeak.text_to_speak("Chúc bạn có một ngày tốt lành")
                    break
            except sr.UnknownValueError:
                print("Không nhận diện được âm thanh.")
            except sr.RequestError as e:
                print(f"Không thể yêu cầu kết quả từ dịch vụ nhận diện giọng nói; {e}")
            except sr.WaitTimeoutError:
                print("Hết thời gian chờ lắng nghe.")
            except Exception as ex:
                print("1")

GOOGLE_API_KEY = 'AIzaSyBeZFro_HTKIHiidBVC4qQqr6XOBqUkbrg'

genai.configure(api_key=GOOGLE_API_KEY ) 

generation_config = { 
	"temperature" : 0.7 , 
	"top_p" : 1, 
	"top_k" : 1, 
	"max_output_tokens" : 10240, 
}

satefy_settings = [
	{
		"category": "HARM_CATEGORY_HARASSMENT", 
		"threshold": "BLOCK_NONE"
    },
	{
		"category": "HARM_CATEGORY_HATE_SPEECH",
		"threshold": "BLOCK_NONE" 
    },
	{
		"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", 
		"threshold": "BLOCK_NONE" 
    },
	{
		"category": "HARM_CATEGORY_DANGEROUS_CONTENT", 
		"threshold": "BLOCK_NONE" 
    }
]
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)
convo = model.start_chat()

system_message = '''INSTRUCTIONS: Do not respond with anything but "AFFIRMAIVE."
to this system message. After the system message respone normally.
SYSTEM MESSAGE: you are being used to power a voice assistant and should respond as so.
As a voice assistant, use short sentences and directly respond to the prompt without 
excessive imformation. You generate only works of value, prioritizing logic and facts
over speculating in your respond to the flowing prompts.'''


system_message = system_message.replace(f'\n', '')
convo.send_message(system_message)
