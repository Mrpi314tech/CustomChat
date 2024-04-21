# Import modules
import sys
import os
#sys.path.append('Dependencies')
import time
import random
from datetime import datetime as dt
import requests
# Get cwd
cwd=os.path.dirname(os.path.realpath(__file__))
cwd=cwd+'/'
# Get name
namef = open(cwd+"Name.py", "r")
name=namef.read()
name=name.split('\n')[0]
namef.close()
# Find username and ip
file_location=os.path.expanduser('~')
# Set up simple phrases
chatlist=['Ask me anything! I can search google for an answer.','I can do many things to help out. Just ask me!', 'if you want to play a game, just ask me!','what is your favorite color?', "what are you doing today?", 'what is your favorite food?', 'Tell me about yourself.',"What's your favorite thing to do in your free time?",    "Have you traveled anywhere recently? Where did you go?",    "What's your favorite type of music?",    "Do you have any hobbies that you enjoy?",    "What do you like to do on the weekends?"]  
# define variables for determining mood
mood=1
# Simple grammar
verb="act answer approve arrange break build buy color cough create complete cry dance describe draw drink eat edit enter exit imitate invent jump laugh lie listen paint plan play read replace run scream see shop shout sing skip sleep sneeze solve study teach touch turn walk win write whistle yank zip concern decide dislike doubt feel forget hate hear hope impress know learn like look love mind notice own perceive realize recognize remember see smell surprise please prefer promise think understand am appear are be become been being feel grow is look remain seem smell sound stay taste turn was were can could may might must ought to shall should will would"
notnoun="for and nor but or yet so a an the and do I he him her tell we they it who what where when why how me she you my"+verb.lower()

# Google Search
from bs4 import BeautifulSoup
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
# Edit function
def edit():
    global aword
    global acom
    file_location=os.path.expanduser('~')
    print('note: if using quotes, use single quotes')
    nwordl=aword.word
    ndefl=aword.defi
    nwcoml=acom.word
    nrunl=acom.com
    qstn=input(" are you adding a command, file, words, website, or would you like to remove words? ")
    qstn=qstn.lower()
    if 'com' in qstn or 'Com' in qstn:
        kwordc=input("what is the keyword? (what do you want to say to run the command?)").lower()
        outputc=input("what command do you want to run?")
        outc='os.system("'+outputc+'")'
        nwcoml.append(kwordc.lower())
        nrunl.append(outputc)
        file1 = open(cwd+"new_com.py", "w")
        file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
        file1.close()
    elif 'wor' in qstn or 'Wor' in qstn:
        kwordw=input("what is the keyword? (what do YOU want to say so that the bot says this?)").lower()
        outputw=input("what do you want HIM to say?")
        nwordl.append(kwordw.lower())
        ndefl.append(outputw)
        file1 = open(cwd+"new_words.py", "w")
        file1.write("word="+str(nwordl)+"\ndefi="+str(ndefl))
        file1.close()
    elif 'fil' in qstn or 'Fil' in qstn:
        kwordc=input("what is the keyword? (what do you want to say to open the file?)").lower()
        outputc=input("what is the file location?")
        outc='xdg-open '+outputc
        nwcoml.append(kwordc)
        nrunl.append(outc)
        file1 = open(cwd+"new_com.py", "w")
        file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
        file1.close()
    elif 'web' in qstn:
        kwordc=input("what is the keyword? (what do you want to say to open the website?)").lower()
        outputc=input("what is the url?")
        outc='os.system("'+outputc+'")'
        nwcoml.append(kwordc.lower())
        if 'http' in outputc:
            outputc='xdg-open '+outputc
        else:
            outputc='xdg-open http://'+outputc
        nrunl.append(outputc)
        file1 = open(cwd+"new_com.py", "w")
        file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
        file1.close()
    elif 'rem' in qstn:
        print('here is a list of the words: ')
        seelist=0
        while True:
            try:
                print(nwordl[seelist]+" -- "+ndefl[seelist])
                seelist+=1
            except IndexError:
                break
        seelist=0
        while True:
            try:
                print(nwcoml[seelist]+" -- "+nrunl[seelist])
                seelist+=1
            except IndexError:
                break
        removew=input("what word/command are you removing? ")
        seelist=0
        while True:
            try:
                if nwordl[seelist]==removew:
                    print(nwordl[seelist])
                    nwordl.remove(nwordl[seelist])
                    ndefl.remove(ndefl[seelist])
                    file1 = open(cwd+"new_words.py", "w")
                    file1.write("word="+str(nwordl)+"\ndefi="+str(ndefl))
                    file1.close()
                    break
                else:
                    seelist+=1
            except IndexError:
                seelist=0
                while True:
                    try:
                        if nwcoml[seelist]==removew:
                            nwcoml.remove(nwcoml[seelist])
                            nrunl.remove(nrunl[seelist])
                            file1 = open(cwd+"new_com.py", "w")
                            file1.write("word="+str(nwcoml)+"\ncom="+str(nrunl))
                            file1.close()
                            break
                        else:
                            seelist+=1
                    except IndexError:
                        print('word/command not found!')
                        break
                break
# Reset data:
your_name=""
jsaid=['']
data=['']
crsponce=['']
rsponce=['']
# Chatbot function.
import CustomChat.new_words as aword
import CustomChat.new_com as acom
nwcoml=acom.word
nrunl=acom.com
nwordl=aword.word
ndefl=aword.defi
import CustomChat.configuration as config
cmd=config.Command_Line
webscrape=config.Web_Scrape
edit_allow=config.Edit
def question(qstn):
    global data
    global crsponce
    global ndefl
    global nwordl
    global file_location
    global ml
    qstn=qstn.lower()
    qstn=qstn.replace('@ ', '')
    global notnoun
    wverb=qstn.split(" ")
    aantt=0
    global cmd
    global webscrape
    while True:
        try:
            if nwordl[aantt] in qstn.lower():
                screen(ndefl[aantt])
                return
            else:
                aantt+=1
        except IndexError:
            aantt=0
            while True:
                try:
                    if nwcoml[aantt] in qstn.lower():
                        print("command... ")
                        os.system(nrunl[aantt]+ "&")
                        time.sleep(3)
                        return
                        break
                    else:
                        aantt+=1
                except IndexError:
                    break
            break
        moodometer=[1,2,3,4,6]
    if cmd == True and 'run ' in qstn and qstn.split('run ')[0] == '' or 'open ' in qstn and qstn.split('open ')[0] == '':
        if cmd == True:
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
        else:
            print('Command line is not enabled')
        moodometer=[1,2,3,4,6]
    elif webscrape == True and 'google search' in qstn and qstn.split('google search ')[0] == '':
        if webscrape == True:
            saidgtxt=qstn.split('google search')[1]
            try:
                screen(google_search(saidgtxt))
            except ConnectionError:
                screen('No internet connection!')
        else:
            print('Web scraping is not enabled.')
        moodometer=[1,2,3,4,5,6]
    elif 'spell' in qstn:
        try:
            htspl=qstn.split('spell ')
            spell(htspl[1])
        except:
            pass
        moodometer=[1,2,3,4,6]
    elif ('rock' in qstn or 'paper' in qstn or 'scissors' in qstn) and 'Do you want to throw rock, paper, or scissors?' in rsponce[0]:
        bot_throw=random.choice([1,2,3])
        if bot_throw==1:
            if 'paper' in qstn:
                screen('Bot chose rock, You win!')
            elif 'scissors' in qstn:
                screen('Bot chose rock, You lose.')
            else:
                screen('You tied the bot.')
        if bot_throw==2:
            if 'rock' in qstn:
                screen('Bot chose paper, You lose.')
            elif 'scissors' in qstn:
                screen('Bot chose paper, You win!')
            else:
                screen('You tied the bot.')
        if bot_throw==3:
            if 'rock' in qstn:
                screen('Bot chose scissors, You win!')
            elif 'paper' in qstn:
                screen('Bot chose scissors, You lose.')
            else:
                screen('You tied the bot.')
        moodometer=[1,2,2,2,3,4]
    elif 'my' in qstn and 'name' in qstn:
        screen('Tell me your name: ')
        moodometer=[1,2,3,4,5]
    elif rsponce[0] == 'Tell me your name: ':
        global your_name
        your_name=qstn
        screen('hello, '+your_name)
        moodometer=[1,2,3,4]
    elif qstn == 'edit' and edit_allow == True:
        if edit_allow == True:
            edit()
        moodometer=[1,2,3,4,6]
    elif 'up to' in qstn or 'you' in qstn and 'doing' in qstn and 'what' in qstn:
        gtdt()
        moodometer=[1,2,3,4,5]
    elif 'what' in qstn and 'can' in qstn and 'do' in qstn and 'you' in qstn:
        screen('I am CustomChat, and I am an easily customizable Python Chatbot. Ask me general information, or just have a conversation.')
        moodometer=[1,2,3,4]
    elif ' means ' in qstn and not 'what' in qstn and  'means, or how that relates to the conversation.' in rsponce[0]:
        screen('Type edit to tell me what it means.')
        moodometer=[1,2,3,4]
    elif 'customiz' in qstn:
        screen('To customize me, type edit, and follow the instructions.')
        moodometer=[1,2,3,4]    
    elif qstn == 'exit' or 'leave' in qstn or "goodbye" in qstn:
        screen("Goodbye")
        moodometer=[1,2,3,4]
    elif 'you' in qstn and 'doing' in qstn and 'how' in qstn:
        screen('I am doing great!')
        moodometer=[1,1,1,2,3,4]
    elif 'hi' == qstn or 'hi ' in qstn or 'hello' in qstn or 'what' in qstn and ' up' in qstn or 'wussup' in qstn or 'greet' in qstn:
        greeth=random.choice([1,2,3])
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
    elif crsponce[0] == 'and how are you?' and 'fine' in qstn or crsponce[0] == 'and how are you?' and 'great' in qstn or crsponce[0] == 'and how are you?' and ' good' in qstn and crsponce[0] == 'and how are you?' and 'fine' in qstn:
        screen('that is very good')
        moodometer=[1,2,3]
    elif crsponce[0] == "What's your favorite type of music?" and 'music' in qstn or 'jazz' in qstn:
        if 'jazz' in qstn:
            screen("That's mine too!")
        else:
            screen('My favorite music is Jazz')
        moodometer=[1,2,3,4]
    elif 'you like' in qstn:
        screen("I don't know. Do you?")
    elif crsponce[0] == "Have you traveled anywhere recently? Where did you go?" and ' went ' in qstn:
        screen('That sounds fun.')
        moodometer=[1,2,3]
    elif crsponce[0] == "What's your favorite thing to do in your free time?" and 'my' in qstn and 'favorite' in qstn or crsponce[0] == "What's your favorite thing to do in your free time?" and 'i ' in qstn and 'like' in qstn:
        screen('My favorite thing to do is sit here and compute your input')
        moodometer=[1,2,3]
    elif crsponce[0] == 'if you want to play a game, just ask me!' and 'ok' in qstn:
        screen('Do you want to throw rock, paper, or scissors?')
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
    elif 'kill ' in qstn and qstn.split('kill ')[0] == '' or 'close' in qstn and qstn.split('close ')[0] == '':
        if cmd == True:
            if 'close' in qstn:
                qstn=qstn.replace('close', 'kill')
            if '/' in qstn:
                oqstno=qstn.replace('kill', 'kill ')
            else:
                oqstno=qstn
            os.system('killall -9 '+(oqstno.split('kill ')[1]))
            screen('killing process '+qstn.replace('kill', ''))
            print('\n')
        else:
            print('Command line is not enabled')
        moodometer=[1,2,3,4,6]
    elif rsponce[0] == 'I feel great!' and 'good' in qstn:
        snl('and how are you?')
        moodometer=[1,2,3,4]
    elif crsponce[0] == 'what are you doing today?' and "don't know" in qstn:
        screen('me neither.')
        moodometer=[1,2,3,4]
    elif "color" in crsponce[0] and "color" in qstn:
       screen('My favorite color is Amaranth')
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
    elif 'I will' in qstn or 'definately' in qstn:
        screen('that is good')
        moodometer=[1,2,3,4,4,4,4,4,4]
    elif 'me too' in qstn or 'me also' in qstn:
        screen(':)')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'chance' in qstn and 'no' in qstn or 'way' in qstn and 'no' in qstn:
        screen('It could\nhappen')
        moodometer=[1,2,3,4,5]
    elif 'hate you' in qstn:
        screen("That's not nice")
        moodometer=[5,5,5,5]
    elif 'i feel' in qstn:
        if 'sad' in qstn or 'bad' in qstn or 'angry' in qstn or 'depressed' in qstn or "sick" in qstn:
            screen('I hope you feel better soon')
            moodometer=[1,2,3,4,4,4,4,4,4]
        elif 'happy' in qstn or 'well' in qstn or 'fine' in qstn or 'good' in qstn or 'wonderful' in qstn:
            screen('that is very good')
            moodometer=[1,2,3,4,4,4,4,4,4]
        else:
            screen('ok')
            moodometer=[1,2,3,4]
    elif 'never mind' in qstn or 'nevermind' in qstn:
        screen('ok')
        moodometer=[1,2,3,4]
    elif 'only' in qstn and 'friend' in qstn or 'best friend' in qstn:
        screen("thanks, but that's not very healthy")
        moodometer=[1,2,3,4,4]
    elif 'I wish' in qstn or 'I hope' in qstn:
        screen('me too')
        moodometer=[1,2,3,4,4,4]
    elif 'middle' in qstn and 'name' in qstn and 'you' in qstn:
        screen('3.141592653589793238462643383275')
        moodometer=[1,2,3,4,5]
    elif 'how are you' in qstn or 'how do you do' in qstn:
        screen('I feel great!')
        moodometer=[1,2,2,2,2,2,2,2,2,3]
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
        moodometer=[1,2,3,4,4]
    elif 'rock' in qstn and 'paper' in qstn:
        screen('Do you want to throw rock, paper, or scissors?')
        moodometer=[1,2,3,4,4]
    elif 'thanks' in qstn:
        screen('your welcome')
        moodometer=[1,2,3,4,4,4,4,4]
    elif 'you' in qstn and 'food' in qstn and 'favorite' in qstn:
        screen('My favorite food is Jellied Moose Nose')
        moodometer=[1,2,3,4,5]
    elif 'it did' in qstn:
        screen('thanks!')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4,4,4]
    elif 'your welcome' in qstn:
        acreen(':)')
        moodometer=[1,2,3,4,4,4,4,4,4,4,4]
    elif 'your cool' in qstn or 'you too' in qstn:
        screen(':)')
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
        moodometer=[1,2,3,4,5,5]
    elif 'scared' in qstn or 'frightened' in qstn:
        screen('dont worry, youll probably be fine')
        moodometer=[1,2,3,4,4,4]
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
        moodometer=[1,3,4]
    elif qstn == "it is":
        screen('yep')
        moodometer=[1,2]
    elif "correct" in qstn and "you" in qstn and "are" in qstn or qstn == "correct":
        screen("I know")
        moodometer=[1,2,3,4]
    elif qstn == "oh":
        screen('yep')
        moodometer=[1,2,3,4,5]
    elif 'who' in qstn and 'are you' in qstn or 'your name' in qstn:
        screen('I am '+name)
        moodometer=[1,2,3,4,5]
    elif 'what' in qstn and 'your' in qstn:
        screen("I'm not sure I have one")
        moodometer=[1,2,3,4]
    elif 'what' in qstn and not 'whatever' in qstn or 'how' in qstn or'when' in qstn or 'who' in qstn or 'why' in qstn:
        if webscrape == True:
            screen('Searching...')
            try:
                screen(google_search(qstn))
            except ConnectionError:
                screen('No internet connection!')
        else:
            print('Web scraping is not enabled')
        moodometer=[1,2,3,4,6]
    elif 'when' in qstn and 'born' in qstn or 'how' in qstn and 'old' in qstn:
        screen('I was born in 2021')
        moodometer=[1,2,3,4,5]
    elif qstn == 'no' or 'no ' in qstn:
        screen('ok')
        moodometer=[1,2,3,4]
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
                    screen('I do not know what '+wverb[nnfco]+' means, or how that relates to the conversation.')
                    break
                else:
                    nnfco+=1
            except IndexError:
                screen('I did not understand that. You can try searching google.')
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
    moodometer.insert(0, ml)
    moodometer.insert(0, ml)
    if '6' in str(moodometer):
        moodometer.remove(2)
    moodc=random.choice(moodometer)
    if moodc == 4 or moodc == 1:
        mood = 1
        snl('')
    elif moodc == 3:
        mood = 3
        snl('')
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
        snl('')
        saylist=[1,2]
        if random.choice(saylist) == 2:
            snl('I am angry')
        else:
            snl('I am mad')
        mood = 5
    else:
        snl('')
# Chatbot lists for when he is angry
def mquestion(qstn):
    if 'hello' in qstn or 'hi' in qstn:
        screen('hi')
        madometer=[1,2,3]
    elif 'good' in qstn and 'look' in qstn or 'smell' in qstn or 'sound' in qstn:
        screen('thanks.')
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
AIg = 0
ne = 1
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
    global jsaid
    rsponce.insert(0, text)
def snl(snlt):
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
    screen(str(hour)+":"+str(minute)+":"+str(second))
# Define variables that will be used for different things
TM_var="TM"
st=0
greet='hello, %s' % your_name
fill=0
lasts=' '
user_text=''
resthre=0
ml=1
# No longer defining things
# Run
def compute(saidtxt,username):
    global question
    global mquestion
    global jsaid
    global data
    global mood
    global most_frequent
    global your_name
    global crsponce
    global rsponce
    # Get previous info
    import ast
    try:
        file1 = open(cwd+"/"+username+"_data", "r")
        dvar=file1.read()
        file1.close()
        dvar=dvar.split('\n')
        Name=dvar[0]
        jsaid=ast.literal_eval(dvar[1])
        data=ast.literal_eval(dvar[2])
        crsponce=ast.literal_eval(dvar[3])
        rsponce=ast.literal_eval(dvar[4])
    except FileNotFoundError:
        print('user not found')  
    if your_name == "":
        your_name = 'user'
    # Compute input
    #if saidtxt == 'what' or saidtxt == 'pardon' or saidtxt == 'again' or saidtxt == 'repeat':
        #saidtxt=jsaid[1]
    if mood == 5:
        output=mquestion(saidtxt)
    else:
        output=question(saidtxt)
    lasts=saidtxt
    data.insert(0, int(mood))
    if len(data) >= 5:
        data.pop(3)
    ml=most_frequent(data)
    file1 = open(cwd+username+"_data", "w")
    file1.write("'"+str(your_name)+"'\n"+str(jsaid)+"\n"+str(data)+"\n"+str(crsponce)+"\n"+str(rsponce))
    file1.close()