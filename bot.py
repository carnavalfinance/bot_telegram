import telepot
import time
from telepot.loop import MessageLoop

TOKEN_TELEGRAM = 'TOKEN'

bot = telepot.Bot(TOKEN_TELEGRAM)




def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text'].split('@')[0] if len(msg['text'].split('@')) > 1 else msg['text']
    #print(content_type, chat_type, chat_id, msg['text'])

    if command == '/buy':
        bot.sendMessage(chat_id=chat_id, text='https://pancakeswap.finance/swap?inputCurrency=BNB&outputCurrency=0xf442a55e0b4a50ec98775775676536f0dba26b08', disable_web_page_preview=False)
    elif command == '/price':
        bot.sendMessage(chat_id=chat_id, text='', disable_web_page_preview=False)
    elif command == '/airdrop':
        bot.sendMessage(chat_id=chat_id, text='https://carnaval.finance/airdrop', disable_web_page_preview=False)
    elif command == '/faucet':
        bot.sendMessage(chat_id=chat_id, text='https://carnaval.finance/faucet', disable_web_page_preview=False)
    elif command == '/contract':
        bot.sendMessage(chat_id=chat_id, text='https://bscscan.com/token/0xf442a55e0b4a50ec98775775676536f0dba26b08', disable_web_page_preview=False)
    elif command == '/chart':
        bot.sendMessage(chat_id=chat_id, text='https://charts.bogged.finance/0xf442A55E0b4a50eC98775775676536F0DbA26b08', disable_web_page_preview=False)
    elif command == '/holders':
        bot.sendMessage(chat_id=chat_id, text='https://bscscan.com/token/0xf442a55e0b4a50ec98775775676536f0dba26b08#balances', disable_web_page_preview=False)
    elif command == '/whitepapper':
        txt = f'English: https://carnaval.finance/whitepaper_en.pdf\nPortuguês: https://carnaval.finance/whitepaper_pt.pdf'
        bot.sendMessage(chat_id=chat_id, text=txt, disable_web_page_preview=False)
    elif command == '/site':
        bot.sendMessage(chat_id=chat_id, text='https://carnaval.finance/', disable_web_page_preview=False)
    elif command == '/twitter':
        bot.sendMessage(chat_id=chat_id, text='https://twitter.com/CarnavalFinance', disable_web_page_preview=False)
    elif command == '/github':
        bot.sendMessage(chat_id=chat_id, text='https://github.com/carnavalfinance', disable_web_page_preview=False)
    elif command == '/telegram':
        bot.sendMessage(chat_id=chat_id, text='https://t.me/carnavalfinance', disable_web_page_preview=False)
    elif command == '/discord':
        bot.sendMessage(chat_id=chat_id, text='', disable_web_page_preview=False)
    elif command == '/help':
        txt = """/buy - Buy $CRNL Token
/price - Display $CRNL Current Price
/airdrop - Airdrop
/faucet - Faucet
/contract - Display Carnaval Smart Contract
/chart - Chart Token Price
/holders - Token Holder List
/whitepapper - Carnaval Whitepaper
/site - Official Website
/twitter - Official Twitter 
/github - Project Github
/telegram - Telegram Group
/discord - Discord Group
/help - Show available commands"""
        bot.sendMessage(chat_id, txt)




MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
