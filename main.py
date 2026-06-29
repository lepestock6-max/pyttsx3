import pyttsx3

welcome = 'привет! Я твой бот для озвучки, напиши что-то в чат и я это озвучу!'
def golos1(golos):
    engine = pyttsx3.init() 

    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 105)

    volume = engine.getProperty('volume')   
    print (volume)                          
    engine.setProperty('volume',1.0) 

    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[0].id)  

    engine.say(golos)
    engine.runAndWait()
    engine.stop()

golos1(welcome)
golos = input("введите что-то:")

golos1(golos)
