print("Made by Mrpi314tech programming")
print('Starting up Jimbot... may take a moment')
# Import modules
import time
import os
import random
import numpy as np
import subprocess
import smbus
from datetime import datetime as dt
import requests
import json
import sys
# Find username and ip
file_location=os.path.expanduser('~')
# Set up clock
hur=int(dt.now().strftime("%H"))
minits=int(dt.now().strftime("%M"))
if hur >= 12:
    if hur == 12:
        if minits <= 9:
            currentTime = str(hur)+":0"+str(minits)+" PM"
        else:
            currentTime = str(hur)+":"+str(minits)+" PM"
    elif minits <= 9:
        currentTime = str(hur-12)+":0"+str(minits)+" PM"
    else:
        currentTime = str(hur-12)+":"+str(minits)+" PM"
else:
    if minits <= 9:
        currentTime = str(hur)+":0"+str(minits)+" AM"
    else:
        currentTime = str(hur)+":"+str(minits)+" AM"
if hur >= 5 and hur <= 11:
    tofdy="Good morning"
elif hur >= 12 and hur <= 16:
    tofdy="Good afternoon"
elif hur >= 17 and hur <= 22:
    tofdy="Good evening"
else:
    tofdy="Go to bed"
if hur >=18 or hur<=6:
    backgn=file_location+"/Jimbot/images/backgroundn.jpg"
elif hur<=11:
    backgn=file_location+"/Jimbot/images/backgroundm.jpg"
else:
    backgn=file_location+"/Jimbot/images/background.jpg"
# Test
print('hello')
# Set up simple phrases
chatlist=['I can do many things to help out. Just ask me!','Press edit to customize me to your needs', 'if you want to play a game, just ask me!','what is your favorite color?', "what are you doing today?", 'what is your favorite food?', 'Tell me about yourself.',"What's your favorite thing to do in your free time?",    "Have you traveled anywhere recently? Where did you go?",    "What's your favorite type of music?",    "Do you have any hobbies that you enjoy?",    "What do you like to do on the weekends?"]  
# define variables for determining mood
data=[]
jsaid=[]
mood=1
# Import information from survey
your_name = "Mrpi314"
name="Jimbot"
# Simple grammar
verb="act answer approve arrange break build buy color cough create complete cry dance describe draw drink eat edit enter exit imitate invent jump laugh lie listen paint plan play read replace run scream see shop shout sing skip sleep sneeze solve study teach touch turn walk win write whistle yank zip concern decide dislike doubt feel forget hate hear hope impress know learn like look love mind notice own perceive realize recognize remember see smell surprise please prefer promise think understand am appear are be become been being feel grow is look remain seem smell sound stay taste turn was were can could may might must ought to shall should will would"
notnoun="for and nor but or yet so a an the and do I he him her tell we they it who what where when why how me she you my"+verb.lower()

def speak(txt):
  print(txt)
# Google Search
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    screen('installing new libraries')
    os.system('pip install beautifulsoup4')
    exit()
import re
pattern = r'([a-zA-Z])(\d)'
pattern2 = r'([a-z])([A-Z])'
pattern3 = r'([A-Z])([A-Z])'
pattern4 = r'(\d)([a-zA-Z])'
pattern5= r'([A-Z])'
def google_search(url):
    url=url.replace('+','plus')
    url="https://www.google.com/search?q="+url.replace(' ','+')
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        text_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'div'])
        
        page_text = ' '.join(element.get_text() for element in text_elements)
        page_text=page_text.replace('°', ' degrees ')
        page_text=page_text.replace('\u202f', ' ')
        page_text=page_text.replace('\u203a', ' ')
        page_text=page_text.replace(':00', " o'clock")
        #page_text=page_text.replace('\u', ' ')
        for i in range(0,10):
            page_text = re.sub(pattern, r'\1 \2', page_text)
            page_text = re.sub(pattern2, r'\1 \2', page_text)
            page_text = re.sub(pattern3, r'\1 \2', page_text)
            page_text = re.sub(pattern4, r'\1 \2', page_text)
        page_text=page_text.replace('N F L', 'NFL')
        page_text=page_text.replace('M L B', 'MLB')
        page_text=page_text.replace('N B A', 'NBA')
        page_text=page_text.replace('N H L', 'NHL')
        page_text=page_text.replace('P M', 'pm')
        page_text=page_text.replace('A M', 'am')
        page_text=page_text.replace('\n', ' ')
        #page_text=page_text.split("Featured Snippets")[0]
        page_text=page_text.split("Verbatim")[1]
        #page_text=page_text.split(".")[0]
        #page_text=page_text.split("?")[0]
        page_text=page_text.split("All times are in Eastern Time")[0]
        #page_text=page_text.split("-")[0]
        try:
            if 'def' in url:
                page_text=page_text.split("/")[2]
            pass
        except:
            pass
        page_text=page_text.split("People also ask")[0]
        page_text=page_text.split("Others want to know")[0]
        page_text=page_text.split("More questions")[0]
        if 'degree' in page_text:
            page_text=page_text.replace(' F ', ' fahrenheit ')
        page_text=page_text.replace(' Q ', ' Quarter ')
        page_text=page_text.replace(' Final,', '')
        page_text=page_text.replace(' Sun,', ' Sunday,')
        page_text=page_text.replace(' Mon,', ' Monday,')
        page_text=page_text.replace(' Tue,', ' Tuesday,')
        page_text=page_text.replace(' Wed,', ' Wednesday,')
        page_text=page_text.replace(' Thu,', ' Thursday,')
        page_text=page_text.replace(' Fri,', ' Friday,')
        page_text=page_text.replace(' Sat,', ' Saturday,')
        
        page_text=page_text.replace(' Jan ', ' January ')
        page_text=page_text.replace(' Feb ', ' February ')
        page_text=page_text.replace(' Mar ', ' March ')
        page_text=page_text.replace(' Apr ', ' April ')
        page_text=page_text.replace(' Jun ', ' June ')
        page_text=page_text.replace(' Jul ', ' July ')
        page_text=page_text.replace(' Aug ', ' August ')
        page_text=page_text.replace(' Sep ', ' September ')
        page_text=page_text.replace(' Oct ', ' October ')
        page_text=page_text.replace(' Nov ', ' November ')
        page_text=page_text.replace(' Dec ', ' December ')
        page_text = re.split(r'\.(?=[A-Z])', page_text)[0]
        if 'eather' in url:
            page_text = page_text.split(',')
            page_text[1] = re.split(r'(?<=[a-z])\s(?=[A-Z])', page_text[1])[0]
            page_text=str(page_text[0])+str(page_text[1])
        if '...' in page_text or 'www.' in page_text or '.com' in page_text or '.org' in page_text or '.gov' in page_text or '.edu' in page_text or '.io' in page_text:
            return ('Adequate answer not found. Open '+url)
        return page_text
    else:
        return f"Error: Unable to retrieve content. Status code {response.status_code}"
# What he is doing today
def gtdt():
    screen('I am computing your input')
# Chatbot function.
def question(qstn):
    global data
    global crsponce
    global ndef
    global nword
    global file_location
    qstn=qstn.lower()
    qstn=qstn.replace('@ ', '')
    global notnoun
    wverb=qstn.split(" ")
    snfv=0
    aantt=0        
    if 'spell' in qstn:
        try:
            htspl=qstn.split('spell ')
            spell(htspl[1])
        except:
            pass
        moodometer=[1,2,3,4,6]
    elif 'you' in qstn and 'doing' in qstn and 'what' in qstn:
        gtdt()
        moodometer=[1,2,3,4,5]
    elif qstn == 'exit' or 'leave' in qstn or "goodbye" in qstn:
        screen("Goodbye")
        exit()
        moodometer=[1,2,3,4]
    elif 'you' in qstn and 'doing' in qstn and 'how' in qstn:
        screen('I am doing great!')
        moodometer=[1,1,1,2,3,4]
    elif 'hi' == qstn or 'hi ' in qstn or 'hello' in qstn or 'what' in qstn and ' up' in qstn or 'wussup' in qstn or 'greet' in qstn:
        greeth=random.choice(range(1,3))
        if greeth == 1:
            screen('hello, %s' % your_name)
        elif greeth == 2:
            screen('whats up, %s' % your_name)
        else:
            screen('Hey, %s' % your_name)
        moodometer=[1,2,2,2,2,2,3]
    elif crsponce[0] == 'what are you doing today?' and 'nothing' in qstn:
        screen('I know you are doing something')
        moodometer=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif crsponce[0] == 'what are you doing today?' and 'talking to you' in qstn:
        screen('other then that')
        moodometer=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif crsponce[0] == 'what are you doing today?' and ' doing' in qstn or 'going' in qstn and crsponce[0] == 'what are you doing today?' or ' am ' in qstn and crsponce[0] == 'what are you doing today?' or ' will be ' in qstn and crsponce[0] == 'what are you doing today?':
        screen('oh.')
        gtdt()
        moodometer=[1,2,3,4,5]
    elif crsponce[0] == 'and how are you?' and 'great' in qstn or crsponce[0] == 'and how are you?' and ' good' in qstn and crsponce[0] == 'and how are you?' and 'fine' in qstn:
        screen('that is very good')
        moodometer=[1,2,3]
    elif crsponce[0] == "What's your favorite type of music?" and 'music' in qstn:
        if 'jazz' in qstn:
            screen("That's mine too!")
        else:
            screen('My favorite music is Jazz')
        moodometer=[1,2,3,4]
    elif crsponce[0] == "Have you traveled anywhere recently? Where did you go?" and ' went ' in qstn:
        screen('I recentely went to Canada to eat Jellied Moose nose')
        moodometer=[1,2,3]
    elif crsponce[0] == "What's your favorite thing to do in your free time?" and 'my' in qstn and 'favorite' in qstn or crsponce[0] == "What's your favorite thing to do in your free time?" and 'i ' in qstn and 'like' in qstn:
        screen('My favorite thing to do is sit here and compute your input')
        moodometer=[1,2,3]
    elif crsponce[0] == 'if you want to play a game, just ask me!' and 'ok' in qstn:
        rockpaper()
        moodometer=[1,2]
    elif crsponce[0] == 'What do you like to do on the weekends?' and 'nothing' in qstn:
        screen('I know you do something')
        moodometer=[1,3,4]
    elif 'i like to' in qstn:
        screen('oh, I like to sleep.')
        moodometer=[1,2,3,4]
    elif 'you' in qstn and 'said' in qstn:
        screen("no I didn't")
        moodometer=[1,2,3,4]
    elif 'timer' in qstn:
        os.system('~/Jimbot/Bash/Jimbotterminal python3 ~/Jimbot/Python/skills/timer.py &')
        moodometer=[1,2,3]
    elif 'run' in qstn or 'open' in qstn:
        if 'open' in qstn:
            qstn=qstn.replace('open ', 'run ')
        if '/' in qstn:
            oqstno=qstn.replace('run', 'run ')
        else:
            oqstno=qstn
        screen('running command '+qstn.replace('run', ''))
        if ' ' in oqstno.split('run ')[1]:
            os.system((oqstno.split('run ')[1])+' &')
        else:
            os.system((oqstno.split('run ')[1])+' &')
        time.sleep(1)
        print('\n')
        moodometer=[1,2,3,4,6]
    elif 'kill' in qstn or 'till' in qstn or 'close' in qstn:
        if 'till' in qstn:
            screen('assuming you ment "Kill"...')
            qstn=qstn.replace('till', 'kill')
        elif 'close' in qstn:
            qstn=qstn.replace('close', 'kill')
        if '/' in qstn:
            oqstno=qstn.replace('kill', 'kill ')
        else:
            oqstno=qstn
        os.system('killall -9 '+(oqstno.split('kill ')[1]))
        screen('killing process '+qstn.replace('kill', ''))
        print('\n')
        moodometer=[1,2,3,4,6]
    elif rsponce[0] == 'I feel great!' and 'good' in qstn:
        snl('and how are you?')
        moodometer=[1,2,3,4]
    elif crsponce[0] == 'what are you doing today?' and "don't know" in qstn:
        screen('me neither.')
        moodometer=[1,2,3,4]
    elif "color" in crsponce[0] and "color" in qstn:
       print('My favorite color is Amaranth')
       moodometer=[1,2,3,4]
    elif 'my' in qstn and 'food' in qstn and 'favorite' in qstn and 'is' in qstn and not 'why' in qstn and not 'what' in qstn and not 'how' in qstn:
        screen('oh, my favorite food is Jellied Moose nose')
        moodometer=[1,2,3,4]
    elif qstn == 'yes' and data[0] == 2:
        screen('Really?')
        moodometer=[1,3,4]
    elif 'wrong with you' in qstn:
        screen('first, tell me: whats wrong with YOU?')
        moodometer=[1,3,5,5]
    elif 'you' in qstn and 'suck' in qstn or 'you' in qstn and'stink' in qstn or 'you' in qstn and 'smell' in qstn:
        screen("no, you do.")
        moodometer=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    elif 'you' in qstn and 'bad' in qstn or 'you' in qstn and 'stupid' in qstn or 'you' in qstn and 'weird' in qstn:
        screen("no, you are.")
        moodometer=[5,5,5,5,5,5,5]
    elif 'am' in qstn and 'talking' in qstn or 'was' in qstn and 'talking' in qstn:
        screen('oh sorry')
        moodometer=[1,2,3,4]
    elif 'because' in qstn and 'answer' in qstn or 'terrible' in qstn and 'answer' in qstn:
        screen('yes it is')
        moodometer=[1,2,3,4,5,5]
    elif 'look good' in qstn or 'look nice' in qstn:
        screen('thanks!')
        moodometer=[2,4,4,4,4]
    elif 'great day' in qstn or 'awesome day' in qstn or 'cool day' in qstn:
        if 'have' in qstn:
            screen('you too')
        else:
            screen('yes it is')
        moodometer=[1,2,3,3,3,3,3,3,3,3,3,3,3,3,4,5]
    elif 'I know' in qstn:
        screen('so true')
        moodometer=[1,2,2,2,2,3,4,4,4,4,4]
    elif 'look bad' in qstn or 'look terrible' in qstn:
        screen('Thats not nice')
        moodometer=[5,5,5,5,5,5,5,5,5]
    elif "you're" in qstn or "you are" in qstn:
        screen("No I'm not")
        moodometer=[1,2,3]
    elif 'fart' in qstn:
        stinky()
        moodometer=[1,2,3,4,4,5,5]
    elif 'picture' in qstn:
        os.system("fswebcam -r 1280x720 --no-banner ~/Pictures/AI.jpg")
        screen('Picture taken')
        moodometer=[1,2,3,4,5]
    elif 'Google search' in qstn or 'google search' in qstn:
        saidgtxt=input("Search: ")
        #os.system('xdg-open https://www.google.com/search?q='+saidgtxt+' &')
        try:
            screen(google_search(saidgtxt))
        except ConnectionError:
            screen('No internet connection!')
        moodometer=[1,2,3,4,5,6]
    elif 'I will' in qstn or 'definately' in qstn:
        screen('that is good')
        moodometer=[1,2,3,4,4,4,4,4,4,5]
    elif 'me too' in qstn or 'me also' in qstn:
        print(':)')
        speak('smiles')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'chance' in qstn and 'no' in qstn or 'way' in qstn and 'no' in qstn:
        screen('It could\nhappen')
        moodometer=[1,2,3,4,5]
    elif 'hate you' in qstn:
        screen('Feelings: hurt. Restarting system.')
        raise ValueError('You are a bad person so I kicked you out')
    elif 'i feel' in qstn:
        if 'sad' in qstn or 'bad' in qstn or 'angry' in qstn or 'depressed' in qstn or "sick" in qstn:
            screen('I hope you feel better soon')
            moodometer=[1,2,3,4,4,4,4,4,4,5]
        elif 'happy' in qstn or 'well' in qstn or 'fine' in qstn or 'good' in qstn or 'wonderful' in qstn:
            screen('that is very good')
            moodometer=[1,2,3,4,4,4,4,4,4,5]
        else:
            screen('ok')
            moodometer=[1,2,3,4]
    elif 'never mind' in qstn or 'nevermind' in qstn:
        screen('ok')
        moodometer=[1,2,3,4]
    elif 'only' in qstn and 'friend' in qstn or 'best friend' in qstn:
        screen("thanks, but that's not very healthy")
        moodometer=[1,2,3,4,4,5]
    elif 'I wish' in qstn or 'I hope' in qstn:
        screen('me too')
        moodometer=[1,2,3,4,4,4,5]
    elif 'middle' in qstn and 'name' in qstn and 'you' in qstn:
        screen('3.141592653589793238462643383275')
        moodometer=[1,2,3,4,5]
    elif 'how are you' in qstn or 'how do you do' in qstn:
        screen('I feel great!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'funny' in qstn and 'you' in qstn or 'hystarical' in qstn and 'you' in qstn:
        screen('Thanks')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4]
    elif 'that' in qstn and 'funny' in qstn:
        screen('Thanks')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4]
    elif 'joke' in qstn or 'funny' in qstn or 'laugh' in qstn:
        joke()
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4,4]
    elif 'have' in qstn and 'but' in qstn:
        screen('yes')
        moodometer=[1,2,3,4,4,5]
    elif 'rock' in qstn and 'paper' in qstn:
        rockpaper()
        moodometer=[1,2,3,4,4,5]
    elif 'thanks' in qstn:
        screen('your welcome')
        moodometer=[1,2,3,4,4,4,4,4,5]
    elif 'you' in qstn and 'food' in qstn and 'favorite' in qstn:
        screen('My favorite food is Jellied Moose Nose')
        moodometer=[1,2,3,4,5]
    elif 'it did' in qstn:
        screen('thanks!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4]
    elif 'your welcome' in qstn:
        print(':)')
        speak('smiles')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'your cool' in qstn or 'you too' in qstn:
        print(':)')
        speak('smiles')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'welcome' in qstn and "you" in qstn:
        screen('thanks')
        moodometer=[1,2,3,4,4,4]
    elif qstn == 'nice':
        screen('Thank you')
        moodometer=[1,2,3,4]
    elif 'I say' in qstn:
        moodometer=[1,2,3,4,5]
        screen('just say anything')
    elif qstn == 'why':
        screen('because')
        moodometer=[1,5,5,5]
    elif 'scared' in qstn or 'frightened' in qstn:
        print('dont worry, youll probably be fine')
        moodometer=[1,2,3,4,4,4,5]
    elif 'ok' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    elif 'time' in qstn and "is it" in qstn:
        ntime()
        moodometer=[1,2,3,4,5]
    elif 'favorite color' in qstn and 'your' in qstn and not 'me' in qstn:
        screen('Amaranth')
        moodometer=[1,2,3,4,5]
    elif 'movie' in qstn or 'I watch' in qstn:
        screen('anything with Wall-e or the Jetsons')
        moodometer=[1,2,3,4,5]
    elif qstn == "maybe":
        screen('maybe...')
        moodometer=[1,3,4,5]
    elif qstn == "it is":
        screen('yep')
        moodometer=[1,2]
    elif "correct" in qstn and "you" in qstn and "are" in qstn or qstn == "correct":
        screen("I know")
        moodometer=[1,2,3,4]
    elif 'what' in qstn and 'your' in qstn:
        screen("I'm not sure I have one")
        moodometer=[1,2,3,4]
    elif 'Bible' in qstn or 'verse' in qstn:
        bible()
        moodometer=[1,2,3,4,5]
    elif qstn == "oh":
        screen('yep')
        moodometer=[1,2,3,4,5]
    elif 'what' in qstn and not 'whatever' in qstn or 'how' in qstn or'when' in qstn or 'who' in qstn or 'why' in qstn:
        screen('Searching...')
        try:
            screen(google_search(qstn))
        except ConnectionError:
            screen('No internet connection!')
        moodometer=[1,2,3,4,6]
    elif 'when' in qstn and 'born' in qstn or 'how' in qstn and 'old' in qstn:
        screen('I was born in 2021')
        moodometer=[1,2,3,4,5]
    elif qstn == 'no' or 'no ' in qstn:
        screen('ok')
        moodometer=[1,2,3,4]
    elif 'are you' in qstn or 'your name' in qstn:
        screen('I am '+name)
        moodometer=[1,2,3,4,4,5]
    elif 'i like' in qstn:
        screen('oh')
        moodometer=[1,2,3,4]
    elif 'sorry' in qstn:
        screen('for what?')
        moodometer=[1,2,3,4]
    elif 'you' in qstn and 'cool' in qstn:
        screen('Thanks!')
        moodometer=[1,2,3,4]
    elif 'yes' in qstn:
        screen('ok')
        moodometer=[1,2,3,4,5]
    else:
        nnfco=0
        while True:
            try:
                if not wverb[nnfco] in notnoun:
                    screen('I do not know what '+wverb[nnfco]+' means, or how that relates to teh conversation.')
                    break
                else:
                    nnfco+=1
            except IndexError:
                screen('I did not understand that. You can press edit to tell me what it means')
                break
        moodometer=[1,2,3,4]
    # Determine mood
    global mood
    if moodometer == [1,2,3,4,5] or moodometer==[1,2,3,4,5,6]:
        moodometer.remove(5)
    try:
        moodometer.remove(4)
    except ValueError:
        pass
    moodometer.insert(0, mood)
    moodometer.insert(0, mood)
    if '6' in str(moodometer):
        moodometer.remove(2)
    moodc=random.choice(moodometer)
    if moodc == 4 or moodc == 1:
        mood = 1
    elif moodc == 3:
        mood = 3
    elif moodc == 2:
        global chatlist
        chatty=random.choice(chatlist)
        snl(chatty)
        psaid.insert(0, chatty)
        if len(psaid) >= 3:
            chatlist.insert(1, psaid[2])
        chatlist.remove(chatty)
        mood = 2 
    elif moodc == 5:
        saylist=[1,2]
        if random.choice(saylist) == 2:
            snl('I am done.')
        else:
            snl('I am really mad')
        mood = 5
# Chatbot lists for when he is angry
def mquestion(qstn):
    print('\n\n')
    if 'hello' in qstn or 'hi' in qstn:
        screen('hi')
        madometer=[1,2,3]
    elif 'good' in qstn and 'look' in qstn or 'smell' in qstn or 'sound' in qstn:
        screen('thanks!')
        madometer=[2,3,3,3]
    elif 'sorry' in qstn and not 'not' in qstn:
        screen('ok')
        madometer=[2,3,3,3,3,3,3,3]
    elif 'good' in qstn:
        screen('whats so good about it?')
        madometer=[1,2,2,3]
    elif 'why' in qstn:
        screen('because')
        madometer=[1,2]
    elif 'you' in qstn and 'suck' in qstn or 'stink' in qstn or 'smell' in qstn or 'bad' in qstn or 'stupid' in qstn or 'weird' in qstn:
        screen("no, you are bad")
        madometer=[1,2]    
    elif 'forgive' in qstn:
        screen('fine')
        madometer=[3]
    else:
        screen("I'm still mad")
        madometer=[1]
    gooh=random.choice(madometer)
    if gooh == 3:
        global mood
        mood=1
# Define variables for storing the history
psaid=[]
wign=[]
ndef=""
nword=""
rsponce=['']
crsponce=['']
AIg = 0
ne = 1
# Play rock paper scissors
def rockpaper():
    screen('Rock paper scissors!')
    time.sleep(1)
    screen('what is your throw?')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        humanthrow=r.recognize_google(audio)
        hand=[1,2,3] #1=rock, 2= paper, 3=scissors
        throw=random.choice(hand)
    if 'rock' in humanthrow or 'Rock' in humanthrow:
        if throw == 1:
            screen('rock, tie')
        if throw == 2:
            screen('paper, you lose')
        if throw == 3:
            screen('scissors, you win')
    elif 'paper' in humanthrow or 'Paper' in humanthrow:
        if throw == 1:
            screen('rock, you win')
        if throw == 2:
            screen('paper, tie')
        if throw == 3:
            screen('scissors, you lose')
    elif 'scissors' in humanthrow or 'Scissors' in humanthrow:
        if throw == 1:
            screen('rock, you lose')
        if throw == 2:
            screen('paper, you win')
        if throw == 3:
            screen('scissors, tie')
    else:
        screen('that is not rock paper or scissors')
    time.sleep(1)
# Function for helping determine mood
def most_frequent(List):
    return max(set(List), key = List.count)
# Tell a joke
def joke():
    jokey=random.choice([1,2,3,4,5,6,7,8,9,10])
    if jokey == 1:
        screen("why did the golfer bring an extra pair of pants?")
        time.sleep(2)
        screen("in case he got a hole in one")
    elif jokey == 2:
        screen("what did the monkey say when he slid down the flagpole?")
        time.sleep(2)
        screen("goodness gracious great balls of fire!")
    elif jokey == 3:
        screen("what is fast, loud and crunchy?")
        time.sleep(2)
        screen("A rocket chip")
    elif jokey == 4:
        screen("why do ducks have feathers on their tails?")
        time.sleep(2)
        screen("to cover their butt-quacks")
    elif jokey == 5:
        screen("what starts with T, ends with T, and is filled with T")
        time.sleep(2)
        screen("A Teapot")
    elif jokey == 6:
        screen("why was 6 afraid of 7")
        time.sleep(2)
        screen("because 7, 8, 9")
    elif jokey == 7:
        screen("what did the 0 say to the 8")
        time.sleep(2)
        screen("nice belt")
    elif jokey == 8:
        screen("what is a sharks favorite game?")
        time.sleep(2)
        screen("swallow the leader")
    elif jokey == 9:
        screen("what's brown and sticky")
        time.sleep(2)
        screen("a stick")
    elif jokey == 10:
        screen("why can't you trust an atom?")
        time.sleep(2)
        screen("they make up everything")
# Set up functions to print to GUI
def screen(text):
    print(text)
    global jsaid
    rsponce.insert(0, text)
def snl(snlt):
    print(snlt)
    global jsaid
    crsponce.insert(0, snlt)
# Function for spelling
def spell(spl):
    screen('%s is spelled:'%spl)
    def letters(wordd):
        return [char for char in wordd]
    ltr=0
    while True:
        try:
            screen(letters(spl)[ltr])
            ltr+=1
        except:
            break
    screen(spl)
# Figure out time
def ntime():
    now=dt.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    if hour >= 13:
        hour -= 12
    if minute <=9:
        minute="0"+str(minute)
    if second <= 9:
        second="0"+str(minute)
    print(str(hour)+":"+str(minute)+":"+str(second))
    speak(str(hour)+":"+str(minute))
# Find any bible verse from an API
def bible():
    screen('what verse?')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('...')
        audio=r.listen(source)
        verse=r.recognize_google(audio)
    screen(verse)
    response = requests.get("https://bible-api.com/"+verse)
    try:
        screen(response.json()['text'])
    except KeyError:
        screen('that verse does not exist')
# Define variables that will be used for different things
TM_var="TM"
st=0
greet='hello, %s' % your_name
speak(greet)
fill=0
lasts=' '
user_text=''
resthre=0
# No longer defining things
while True:
    # Reset variables
    talkyes=True
    if st == 0:
        st=1
        past=['z','z','z','z']
    saidtxt=input(': ')
    # Compute input
    if saidtxt == 'what' or 'pardon' in saidtxt or saidtxt == 'again' or saidtxt == 'repeat':
        saidtxt=jsaid[1]
    if mood == 5:
        mquestion(saidtxt)
    else:
        question(saidtxt)
    lasts=saidtxt
    data.insert(0, int(mood))
    if len(data) >= 5:
        data.pop(3)
    ml=most_frequent(data)
