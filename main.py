import telebot

with open("api.key") as fapikey:
    apikey = fapikey.readline()

bot = telebot.TeleBot(apikey)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = str(message.text).lower()
    if len(msg) > 10:
        bot.send_message(message.from_user.id, "многабукоффф! давай что-нибудь попроще...")
    elif msg in ["привет", "здравствуй", "здравствуйте"]:
        bot.send_message(message.from_user.id, "привет!")
    else:
        lst = str(msg).replace("-", " - ").replace("+", " + ").replace("  ", " ").split()

        if len(lst) == 1:
            bot.send_message(message.from_user.id, lst[0])
        elif len(lst) == 3:
            oper = lst[1]
            op1 = lst[0]
            op2 = lst[2]

            try:
                if oper == "+":
                    res = str(int(op1) + int(op2))
                    bot.send_message(message.from_user.id, res)

                elif oper == "-":
                    res = str(int(op1) - int(op2))
                    bot.send_message(message.from_user.id, res)

                else:
                    bot.send_message(message.from_user.id, "пока только плюс или минус могу")

            except Exception as ex:
                bot.send_message(message.from_user.id, f"ха! думал я зависну? нее, эту ошибку я "
                                                       f"обрабатываю (класс ошибки {ex.__class__})")

        elif len(lst) > 3:
            bot.send_message(message.from_user.id, "пока я умею работать только с двумя операндами! не грузи :)")
        else:
            bot.send_message(message.from_user.id, "я не понимаю :( пока я умею только складывать два числа!")


bot.polling(none_stop=True, interval=0)
