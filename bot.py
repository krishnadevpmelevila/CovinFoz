from enum import Flag
from dotenv import load_dotenv
import os
from telegram import *
from telegram.ext import *
import requests
import json
from datetime import date
from datetime import timedelta
load_dotenv()
new = os.environ.get("CODE")
api = os.environ.get("API")
api2 = os.environ.get("API2")
dateto=date.today()
dateis2=str(dateto)
dateis=str(dateto.strftime("%d-%m-%Y")) #Current date in string
yesterday = dateto - timedelta(days = 1)
dateYes1=str(yesterday.strftime("%d-%m-%Y")) #Current date in string

dateyes = str(yesterday)


def checkKey(dict, key):
      
    if key in dict.keys():
        return True
    else:
        return False
def vCheck(dict, key):
      
    if key in dict.keys():
        return True
    else:
        return False
def tCheck(dict, key):
      
    if key in dict.keys():
        return True
    else:
        return False
            
print('ok1')
url = api
url2=api2


print(dateis)
response = requests.request("GET", url)
response2 = requests.request("GET", url2)
todos = json.loads(response.text)
todos2 = json.loads(response2.text)

checking=todos2['KL']['dates']

checked=checkKey(checking, dateis2) #Check for current date is available

if(checked):
    testData=todos2['KL']['dates'][dateis2]
    done=checkKey(testData, 'delta') #Check for current data is available
else:
    done=False
    
# Total Datas
tcs=todos['reports']

for data in tcs:
    
    if data["date"] == dateis:
        rc=data['today_positive']
        flag=False
    elif data["date"] == dateYes1:
        rc=data['today_positive']
        flag=True
        
    else:
        rc="Program Error please contact @krishnadev"
if(checked):
    tc=todos2['KL']['dates'][dateis2]['total']['confirmed']        
    td=todos2['KL']['dates'][dateis2]['total']['deceased']
    tr=todos2['KL']['dates'][dateis2]['total']['recovered']
    tt=todos2['KL']['dates'][dateis2]['total']['tested']
    tv=todos2['KL']['dates'][dateis2]['total']['vaccinated']
else:
    tc=todos2['KL']['dates'][dateyes]['total']['confirmed']        
    td=todos2['KL']['dates'][dateyes]['total']['deceased']
    tr=todos2['KL']['dates'][dateyes]['total']['recovered']
    tt=todos2['KL']['dates'][dateyes]['total']['tested']
    tv=todos2['KL']['dates'][dateyes]['total']['vaccinated']
# Recent Data

if(done):
    vData=todos2['KL']['dates'][dateis2]['delta']
    
    tDone=tCheck(vData,'tested')
    vDone=vCheck(vData,'vaccinated')
    rd=todos2['KL']['dates'][dateis2]['delta']['deceased']
    rr=todos2['KL']['dates'][dateis2]['delta']['recovered']
    if(tDone):
        rt=todos2['KL']['dates'][dateis2]['delta']['tested']
    else:
        rt=todos2['KL']['dates'][dateyes]['delta']['tested']
    if(vDone):
        rv=todos2['KL']['dates'][dateis2]['delta']['vaccinated']
    else:
        rv=todos2['KL']['dates'][dateyes]['delta']['vaccinated']

else:
    vData=todos2['KL']['dates'][dateyes]['delta']
    
    vDone=vCheck(vData,'vaccinated')
    rd=todos2['KL']['dates'][dateyes]['delta']['deceased']
    rr=todos2['KL']['dates'][dateyes]['delta']['recovered']
    rt=todos2['KL']['dates'][dateyes]['delta']['tested']
    if(vDone):
        rv=todos2['KL']['dates'][dateyes]['delta']['vaccinated']
    else:
        rv="Data not available"




print('ok2')


# ncs=todos['total_values']['newlyConfirmedCases']
# dth=todos['stats']['totalDeaths']

# Bot Auth
bot = Bot(new)

# Bot initialise
updater=Updater(new,use_context=True)
dispatcher=updater.dispatcher
# START
def Start(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Welcome to CovinFoz 🥰 | Stay 🏚️ Stay Safe \n Type the commands to get started 🖋️:\n 1. /tc - Total confirmed cases in Kerala \n 2. /td - Total death in Kerala\n 3. /tr - Total recovered in Kerala\n 4. /tt - Total tested in Kerala \n 5. /tv - Total vacinated in Kerala \n \n\n 6. /rc - Today's confirmed cases in Kerala \n 7. /rd - Today's deaths in Kerala \n 8. /rr - Today's recovered cases in Kerala \n 9. /rt - Today's tested cases in Kerala \n 10. /rv - Today's vaccinated cases in Kerala"
	)
start_value=CommandHandler('start',Start)
dispatcher.add_handler(start_value)
updater.start_polling()

# Total confirmed cases
def totalConfirm(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Total confirmed cases in Kerala is: "+str(tc)
	)
tc_value=CommandHandler('tc',totalConfirm)
dispatcher.add_handler(tc_value)
updater.start_polling()

# Total Deaths
def totalDeath(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Total death in Kerala is: "+str(td)
	)
td_value=CommandHandler('td',totalDeath)
dispatcher.add_handler(td_value)
updater.start_polling()

# Total Recovery

def totalRecovery(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Total recovery cases in Kerala is: "+str(tr)
	)
tr_value=CommandHandler('tr',totalRecovery)
dispatcher.add_handler(tr_value)
updater.start_polling()

# Total Tested
def totalTested(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Total tests in Kerala is: "+str(tt)
	)
tt_value=CommandHandler('tt',totalTested)
dispatcher.add_handler(tt_value)
updater.start_polling()

# Total Vaccinated
def totalVaccinated(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Total vaccination in Kerala is: "+str(tv)
	)
tv_value=CommandHandler('tv',totalVaccinated)
dispatcher.add_handler(tv_value)
updater.start_polling()
if(flag):
    def recentConfirm(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Yesterday's confirmed cases in Kerala is: "+str(rc)+"\n Today's datas will be updated soon!"
    	)
    rc_value=CommandHandler('rc',recentConfirm)
    dispatcher.add_handler(rc_value)
    updater.start_polling()

# Recent confirmed cases
def recentConfirm(update:Update,context:CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="Today's confirmed cases in Kerala is: "+str(rc)
	)
rc_value=CommandHandler('rc',recentConfirm)
dispatcher.add_handler(rc_value)
updater.start_polling()
if(done):
    # Recent Deaths
    def recentDeath(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Today's death in Kerala is: "+str(rd)
    	)
    rd_value=CommandHandler('rd',recentDeath)
    dispatcher.add_handler(rd_value)
    updater.start_polling()
    
    # Recent Recovery
    
    def recentRecovery(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Today's recovery cases in Kerala is: "+str(rr)
    	)
    rr_value=CommandHandler('rr',recentRecovery)
    dispatcher.add_handler(rr_value)
    updater.start_polling()
    
    # Recent Tested
    def recentTested(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Today's tests in Kerala is: "+str(rt)
    	)
    rt_value=CommandHandler('rt',recentTested)
    dispatcher.add_handler(rt_value)
    updater.start_polling()
    
    # Recent Vaccinated
    def recentVaccinated(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Today's vaccination in Kerala is: "+str(rv)
    	)
    rv_value=CommandHandler('rv',recentVaccinated)
    dispatcher.add_handler(rv_value)
    updater.start_polling()
else:
    
    # # Recent confirmed cases
    def recentConfirm(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Yesterday's confirmed cases in Kerala is: "+str(rc)+"\n Today's datas will be updated soon!"
    	)
    rc_value=CommandHandler('rc',recentConfirm)
    dispatcher.add_handler(rc_value)
    updater.start_polling()
    
    # Recent Deaths
    def recentDeath(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Yesterday's death in Kerala is: "+str(rd)+"\n Today's datas will be updated soon!"
    	)
    rd_value=CommandHandler('rd',recentDeath)
    dispatcher.add_handler(rd_value)
    updater.start_polling()
    
    # Recent Recovery
    
    def recentRecovery(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Yesterday's recovery cases in Kerala is: "+str(rr)+"\n Today's datas will be updated soon!"
    	)
    rr_value=CommandHandler('rr',recentRecovery)
    dispatcher.add_handler(rr_value)
    updater.start_polling()
    
    # Recent Tested
    def recentTested(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Yesterday's tests in Kerala is: "+str(rt)+"\n Today's datas will be updated soon!"
    	)
    rt_value=CommandHandler('rt',recentTested)
    dispatcher.add_handler(rt_value)
    updater.start_polling()
    
    # Recent Vaccinated
    def recentVaccinated(update:Update,context:CallbackContext):
    	bot.send_message(
    		chat_id=update.effective_chat.id,
    		text="Yesterday's vaccination in Kerala is: "+str(rv)+"\n Today's datas will be updated soon!"
    	)
    rv_value=CommandHandler('rv',recentVaccinated)
    dispatcher.add_handler(rv_value)
    updater.start_polling()
    
    
print("working...")