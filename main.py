import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

surgery = ["Will my child need more surgery as new technology becomes available?", "need more surgery"]
bye = ["bye", "Thank you", 'Thanks']
name = ["tell me your name", "name", 'what is your name', "your name "]
therapy = ["when is my next therapy session", "therapy session", "session"]
food = ["nutrition", "diet plan", "diet", 'food']
Time = ["time", "what is time now", "time please", "tell me the time"]
day = ["day", "tell me the day", "day please", "date"]
last = ["when is my last therapy session", "last therapy session", "last therapy"]
operation = ["My child’s hearing aid(s) did not help very much. Will a cochlear implant be better?", "hearing aid",
             "cochlear implant be better"]
beginner_list = ["Baa  Baa Black Sheep", "Mary Had a Little Lamb", "Five little monkeys jumping on the bed",
                 "Jack and Jill went up the hill", "Twinkle twinkle little star", "Row Row Row Your Boat",
                 "I am a little teapot Short and stout"]
advanced_list = ["The door slammed down on my hand and I screamed like a little baby",
                 "The chocolate chip cookies smelled so good ", "I found a gold coin on the playground",
                 "The church was white and brown and looked very old",
                 "This dinner is so delicious I can't stop eating"]

def speechtestlist(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]

def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')
        recognizer.adjust_for_ambient_noise(source)
        recognizer.energy_threshold = 0.8
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            print("Recognizing")
            query = recognizer.recognize_google(audio, language='en-in')
            print("the command is printed=", query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(str(date))
    print(day)
    speak(str(month))
    print(month)
    speak(str(year))
    print(year)

def tellTime():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)

def beginner():
    for statementb in beginner_list:
        speech_test(statementb)

def advanced():
    for statementa in advanced_list:
        speech_test(statementa)
        break

def speech_test(test_sentence):
    speak(test_sentence)
    speak('Repeat')
    query = takeCommand().lower()
    p1 = test_sentence
    p1 = p1.lower()
    speech = p1.replace(" ", "")
    p1_list = list(speech)
    p2 = query
    p2 = p2.lower()
    response = p2.replace(" ", "")
    p2_list = list(response)
    proceed = True

    while proceed:
        ret_list = speechtestlist(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]

    count = len(p1_list) + len(p2_list)
    total = len(speech)
    efficiency = (1 - (count / total)) * 100
    print("Speech Efficiency : ", efficiency)

def Hello():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    elif 18 <= hour < 24:
        speak("Good evening!")
    else:
        speak("Good night")
    while hour:
        speak("how can I help you?")
        Take_query()

def Take_query():
    while True:
        query = takeCommand().lower()

        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif query in day:
            tellDay()
            continue

        if query in Time:
            tellTime()
            continue
        elif query in operation:
            speak("It is difficult to predict how each child will do with a cochlear implant,"
                  " because everyone is different. During the cochlear implant evaluation, "
                  "the audiologist and/or cochlear implant surgeon can discuss realistic expectations with you."
                  " Associated disabilities can also be a deterrent to development of Speech & Language. ")

            print("It is difficult to predict how each child will do with a cochlear implant,"
                  " because everyone is different. During the cochlear implant evaluation, "
                  "the audiologist and/or cochlear implant surgeon can discuss realistic expectations with you."
                  " Associated disabilities can also be a deterrent to development of Speech & Language. ")

        elif query == "contact us":
            speak("here is number to contact")
            print("")

        elif query == "food":
            speak("Magnesium can help maintain nerve function"
                  "so avocados, salmon, legumes, kale, spinach, and bananas."
                  "Potassium is believed that a drop in the levels of fluid in the inner ear so mushrooms, "
                  "sweet potatoes, potatoes "
                  "zinc and omega-3s are some of nutrition")

        elif query == "song":
            speak('working on it')
            webbrowser.open('https://youtu.be/SDXHcR5AL6E')
            continue

        elif query == "Can the implant hear immediately after surgery":
            print("After the surgery, one has to wait for the scar to heal. "
                  "This period is approximately 2 to 3 weeks. During this time,"
                  " the implant cannot hear through the implant because the external part is not coupled to it yet."
                  " After this healing period is over,the implant and processor are programmed for the first time. "
                  "This is called the ‘switch on’. ")

        elif query in surgery:
            speak("The implanted unit is designed to last a lifetime.")

        elif query == "Can the sound processor be removed at night":
            speak("Yes. But you should turn it off to save the battery."
                  " Some users wear the sound processor all night so they can hear.")

        elif query == "What sounds can be heard with a cochlear implant":
            speak("Your child will probably hear most sounds of medium-to-high loudness. ")

        if query in bye:
            speak("Bye. I am leaving ")
            exit()
        elif query == "therapy":
            speak("shortly by this week")
        elif query == "last therapy session":
            speak("two days before")
        elif query == "who created you":
            speak("I was created by Creative Seeds.")
        elif query == "speech test":
            beginner()

        elif query in name:
            speak("I am Mex. I am here to help you")
        else:
            speak("sorry  can't understand")

if __name__ == '__main__':
    Hello()

