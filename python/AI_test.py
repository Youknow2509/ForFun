#noi chuyen thanh chu
import speech_recognition as sr  
import pyttsx3
from datetime import date, datetime

robot_ear = sr.Recognizer()  # khoi tao tai nghe
robot_brain =""  #khoi tao bo nho
robot_mouth = pyttsx3.init()  # khoi tao phan noi

print("Welcome to AI by V")

while True:
    with sr.Microphone() as source: 
        robot_ear.adjust_for_ambient_noise(source,duration=0.9)
        print("Robot: I'm listening - Tôi đang lắng nghe bạn nói")
        print("Robot: ....")
        audio = robot_ear.listen(source)  # chuyển âm nói thành chữ

    try:
        you_speak =robot_ear.recognize_google(audio)
    except:
        you_speak =""  # truong hop am noi khong nghe duoc hay on hay khong thanh tieng 
    print("You: " + you_speak)
    
    #xu li lenh bo nao cua may tinh 
    if  you_speak == "":
        robot_brain = " I don't thing it, can you speak again or you can written to here - Tôi không nghe được những điều bạn nói, bạn có thể nói lại được không "  # đang cần fix vừa nói vừa viết đc nhưng chưa đc
       # you_written = input('You can written here:')    # lỗi nhập input không nhân vào biến , cho vào if không chạy 
        
    elif  "hello" in you_speak :
        robot_brain = "Helo V - Chào V"
    elif  "today" in you_speak:
        today = date.today()    
        robot_brain = today.strftime("%B %d, %Y")
    elif  "time"in you_speak:
        now=datetime.now()   
        robot_brain =now.strftime(" %H hours %M minutes %S seconds - %Hh %Mph %Ss ")
    elif "thinh" in you_speak:
        robot_brain = " He is immaturity - Thằng Thịnh Hậu Đậu "
    elif "bye" in you_speak:          #ket thuc vong lap
        robot_brain = " Bye V - Chào tạm biệt V "
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    
    print("Robot: " + robot_brain)
    #chu thanh am noi

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
