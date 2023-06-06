import telebot
from telebot import types

bot = telebot.TeleBot('5866824657:AAF-4w0c7NbacF8knEGPUtWX4gapD-Rq3bM')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nВы можете узнать ответы на интересующие вас вопросы, используя команды, которые указаны в выпадающем меню, слева от строки для ввода сообщений.',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id, '⛓ <a href="https://c-patex.com/"><i>Сайт</i></a> Экосистемы С-Patex\nДля получения более <b>подробной информации</b> просим ознакомиться с <b>F.A.Q</b> по <a href="https://t.me/cpatexcis/332/"><i>ссылке</i></a>  👈',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['withdrawal'])
def withdrawal(message):
    bot.send_message(message.chat.id, '💰 <b>Все выводы</b> обрабатываются до 3х часов, если ваш вывод задерживается, пожалуйста, свяжитесь со службой поддержки (<i>детали по команде</i> <b>/contact</b>)\nДля получения <b>более подробной информации</b> просим ознакомиться с <b>F.A.Q</b> по <a href="https://t.me/cpatexcis/332"><i>ссылке</i></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['fees'])
def fees(message):
    bot.send_message(message.chat.id, '💲 Детальный <b>график комиссий</b> можете найти <a href="https://c-patex.com/fees/">здесь</a>.\n Для получения <b>более подробной информации</b> просим ознакомиться с <b>F.A.Q</b> по <a href="https://t.me/cpatexcis/332"><i>ссылке</i></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['kyc'])
def kyc(message):
    bot.send_message(message.chat.id, '👤 <b>Максимальный регламент</b> на проверку ~24 часа. На практике заявки обрабатываются гораздо быстрее.\nДля получения более подробной информации просим ознакомиться с <b>F.A.Q</b>  по <a href="https://t.me/cpatexcis/332"><i>ссылке</i></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['deposit'])
def deposit(message):  bot.send_message(message.chat.id, '🪙 Если ваш депозит <b>не был зачислен</b>, пожалуйста, предоставьте нам подробные данные о транзакции <b>(СУММА, ВАЛЮТА, ХЕШ)</b> на почту: 📬 support@c-patex.com\nДля получения <b>более подробной информации</b> просим ознакомиться с <b>F.A.Q</b>  по <a href="https://t.me/cpatexcis/332"><i>ссылке</i></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['contact'])
def contact(message):   bot.send_message(message.chat.id, 'Вы можете связаться с нами на почте — 📬 support@c-patex.com\n🌐 Создать тикет в службу поддержки на <a href="https://c-patex.com/support">сайте</a>\n📱 Либо связаться с агентом поддержки в <a href="http://t.me/cpatexsupport">Телеграмме</a>', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['two_factor_auth'])
def  two_factor_auth(message):   bot.send_message(message.chat.id, '👤Для отключения <b>2FA</b> необходимо предоставить <b>обе стороны документа (паспорт или ID-карту или водительское удостоверение), а также 🤳 селфи, на котором вы держите документ, и листок бумаги со следующим рукописным текстом «C-PATEX.COM», текущая дата и ваша подпись".</b>\nПожалуйста, присылайте все фотографии нам по адресу support@c-patex.com.\n<b>Для получения более подробной информации</b> просим ознакомиться с <b>F.A.Q</b>  по <a href="https://t.me/cpatexcis/332"><i>ссылке</i></a> 👈\n', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['docs'])
def docs(message):   bot.send_message(message.chat.id, '📝 Ссылка на <a href="https://c-patex.com/files/en/wp.pdf?v=1.2"><b>whitepaper</b></a>\n🔩 Ссылка на <a href="https://patex.io/docs/Patex%20Tokenomics.pdf"><b>токеномику</b></a>', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['socials'])
def socials(message):   bot.send_message(message.chat.id, '📜 <a href="https://linktr.ee/patex_ecosystem"><b>Linktr.ee</b></a>\n \
— <a href="https://www.facebook.com/patexecosystem"><b>Facebook</b></a>\n \
— <a href="https://www.instagram.com/patex_ecosystem/"><b>Instagram</b></a> \n \
— <a href="https://www.youtube.com/channel/UCLmHyM6kZ5bViyh7my6ZkpA"><b>YouTube</b></a> \n \
— <a href="https://medium.com/@patex_ecosystem"><b>Medium</b></a> \n \
— <a href="https://twitter.com/patex_ecosystem"><b>Twitter</b></a> \n \
       \n \
📝<a href="https://linktr.ee/patex_ecosystem"><b>Patex Chats</b></a>\n \
— <a href="https://t.me/cpatexeng"><b>TG Channel (English)</b></a> \n \
— <a href="https://t.me/cpatexexchange"><b>TG Channel (Español / Portuguese)</b></a> \n \
— <a href="https://t.me/cpatexespanol"><b>TG Chat (Español)</b></a> \n \
— <a href="https://t.me/cpatexportuguese"><b>TG Chat (Portuguese)</b></a> \n \
— <a href="https://t.me/+HmW0DJAYl1YzMjAy"><b>TG Chat (English)</b></a> \n \
— <a href="https://t.me/cpatexcis"><b>TG Chat (CIS)</b></a>', disable_web_page_preview=True, parse_mode='HTML')


bot.polling(none_stop=True, interval=1)