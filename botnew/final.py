import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import pickle
import time

#massive=[[]]
# ниже счетчики для перекрута обьявлений
k=0
i=0
mm=0
oof=0
uuu=0
schetch=0
godg=0
sychetch=0
pepgodg=0
sychetchr=0
pepgodga=0
# конец счетчиков
us=0 # Для id совместника
sn_komnat=0 # Для id снять комнату
sdam_komn=0 # Для id сдать комнату
snat1kom=0 # для id снять однокомнатную
sdam_odnok=0 #Для id сдать однокомнатную
snimu2k=0 #Для Id снять 2 двухкомнатную
sdatka2k=0 # для id сдать двушку 2 комнатную
s_snat3=0 # для Id снять 3 комнатную
sdat3sdat=0 # ДЛя id сдать 3 комнатную

token ='029b2ced70358ef3263fc79c588f0734b999ee5df2ec50991894caaf5cd537875c85cc1e5e38c0d4e55d0'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def create_keyboard(response):
    '''Создание клавиатуры'''
    keyboard = VkKeyboard(one_time=False)   #параметр в скобках отвечает за закрытие при нажатии или нет

    if response == 'начать':

        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY) # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'найти человека, для аренды жилья':  # закрытие клавиатуры
        #print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'смотреть анкеты или следующая':
        keyboard.add_button('Смотреть анкеты или следующая', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить свою анкету из объявлений', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'удалить свою анкету из объявлений':
        keyboard.add_button('Подтвердить удаление объявления', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'подтвердить удаление объявления':#переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'перейти в главное меню':#переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'я хочу снять жилье':#ЧЕЛОВЕК ХОЧЕТ СНЯТЬ ЖИЛЬЕ
        keyboard.add_button('Снять комнату', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Снять 1-комнатную квартиру', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Снять 2-комнатную квартиру', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Снять 3-комнатную квартиру', color=VkKeyboardColor.PRIMARY)

    elif response == "я хочу сдать жилье":             #ЧЕЛОВЕК ХОЧЕТ СДАТЬ ЖИЛЬЕ
        keyboard.add_button('Сдать комнату', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Сдать 1-комнатную квартиру', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Сдать 2-комнатную квартиру', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Сдать 3-комнатную квартиру', color=VkKeyboardColor.PRIMARY)

    elif response == 'снять комнату':  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ ЖИЛЬЕ
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'сдать комнату':  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ ЖИЛЬЕ
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'смотреть комнаты или следующая': # показать обьявление ТЕМ КТО ХОЧЕТ СНЯТЬ КОМНАТУ
        keyboard.add_button('Смотреть комнаты или следующая', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить своe объявление', color=VkKeyboardColor.PRIMARY) #надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'удалить своe объявление': # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ АРЕНДАТОРАМ
        keyboard.add_button('Подтвердить удаление', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'подтвердить удаление':#переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'смотреть объявления или следующее': # показать обьявление ТЕМ КТО ХОЧЕТ СДАТЬ КОМНАТУ
        keyboard.add_button('Смотреть объявления или следующее', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о сдаче', color=VkKeyboardColor.PRIMARY) #надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'удалить объявление о сдаче': # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ АРЕНДОДАТЕЛЯМ
        keyboard.add_button('Подтвердить удаление о сдаче', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'подтвердить удаление о сдаче':#переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'снять 1-комнатную квартиру':  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ 1 КОМНАТНУЮ КВАРТИРУ СНЯТИЕ СНЯТИЕ
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'сдать 1-комнатную квартиру':  # ЧЕЛОВЕК ХОЧЕТ СДАТЬ 1 КОМНАТНУЮ КВАРТИРУ СДАЧА СДАЧА
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'смотреть 1к.кв. или следующая': # показать обьявление ТЕМ КТО ХОЧЕТ СНЯТЬ 1 комн. КВАРТИРУ
        keyboard.add_button('Смотреть 1к.кв. или следующая', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о снятии 1к.кв.', color=VkKeyboardColor.PRIMARY) #надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'смотреть арендаторов или следующий': # показать обьявление ТЕМ КТО ХОЧЕТ сдать 1 комн. КВАРТИРУ
        keyboard.add_button('Смотреть арендаторов или следующий', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о сдаче 1к.кв.', color=VkKeyboardColor.PRIMARY) #надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'удалить объявление о снятии 1к.кв.':  # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ АРЕНДАТОРАМ
        keyboard.add_button('❗Подтвердить удаление', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == '❗подтвердить удаление':  # переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'удалить объявление о сдаче 1к.кв.':  # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ АРЕНДОДАТЕЛЯМ
        keyboard.add_button('‼Подтвердить удаление‼', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == '‼подтвердить удаление‼':  # переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'снять 2-комнатную квартиру':  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ 2 КОМНАТНУЮ КВАРТИРУ СНЯТИЕ СНЯТИЕ
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'сдать 2-комнатную квартиру':  # ЧЕЛОВЕК ХОЧЕТ СДАТЬ 2 КОМНАТНУЮ КВАРТИРУ СДАЧА СДАЧА
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'смотреть 2к.кв. или следующая': # показать обьявление ТЕМ КТО ХОЧЕТ СНЯТЬ 2 комн. КВАРТИРУ
        keyboard.add_button('Смотреть 2к.кв. или следующая', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о снятии 2к.кв.', color=VkKeyboardColor.PRIMARY) #надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'смотреть арендаторов или следующий👥':  # показать обьявление ТЕМ КТО ХОЧЕТ сдать 2 комн. КВАРТИРУ
        keyboard.add_button('Смотреть арендаторов или следующий👥', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о сдаче 2к.кв.', color=VkKeyboardColor.PRIMARY)  # надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'удалить объявление о снятии 2к.кв.':  # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ Арендаторам 2 к кв
        keyboard.add_button('Подтвердить удаление👥', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'подтвердить удаление👥':  # переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'удалить объявление о сдаче 2к.кв.':  # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ АРЕНДОДАТЕЛЯМ
        keyboard.add_button('👥Подтвердить удаление', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == '👥подтвердить удаление':  # переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'снять 3-комнатную квартиру':  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ 2 КОМНАТНУЮ КВАРТИРУ СНЯТИЕ СНЯТИЕ
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'сдать 3-комнатную квартиру':  # ЧЕЛОВЕК ХОЧЕТ СДАТЬ 3 КОМНАТНУЮ КВАРТИРУ СДАЧА СДАЧА
        # print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    elif response == 'смотреть 3к.кв. или следующая': # показать обьявление ТЕМ КТО ХОЧЕТ СНЯТЬ 3 комн. КВАРТИРУ
        keyboard.add_button('Смотреть 3к.кв. или следующая', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о снятии 3к.кв.', color=VkKeyboardColor.PRIMARY) #надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'смотреть арендаторов или следующий✅':  # показать обьявление ТЕМ КТО ХОЧЕТ сдать 3 комн. КВАРТИРУ
        keyboard.add_button('Смотреть арендаторов или следующий✅', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Удалить объявление о сдаче 3к.кв.', color=VkKeyboardColor.PRIMARY)  # надо сделать удаление
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'удалить объявление о снятии 3к.кв.':  # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ Арендаторам 3 к кв
        keyboard.add_button('Подтвердить удаление✅✅', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'подтвердить удаление✅✅':  # переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    elif response == 'удалить объявление о сдаче 3к.кв.':  # ПЕРЕЙТИ НА СТРАНИЦУ ПОДТВЕРЖДЕНИЯ АРЕНДОДАТЕЛЯМ
        keyboard.add_button('Подтвердить удаление⚠', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на другую строку
        keyboard.add_button('Перейти в главное меню', color=VkKeyboardColor.PRIMARY)  # создание кнопки

    elif response == 'подтвердить удаление⚠':  # переход на главную страницу
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)


    else:
        keyboard.add_button('Я хочу снять жилье', color=VkKeyboardColor.PRIMARY)  # создание кнопки
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Я хочу сдать жилье', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()  # Переход на третью строку
        keyboard.add_button('Найти человека, для аренды жилья', color=VkKeyboardColor.PRIMARY)

    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            keyboard = create_keyboard(response)

            if event.from_user and not event.from_me and sdat3sdat==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                pisisdam=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                zilka = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                ffail1 = 'ssdam3k.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(ffail1, 'rb')  # 1 открытие
                da1 = pickle.load(f)  # 2 открытие
                tus2 = da1[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                tus2.insert(0, [pisisdam, zilka])  # ДОБАВЛЯЕМ В МАССИВ
                del pisisdam
                del zilka

                print('_' * 40)
                print('В базе: ' + (str(len(tus2)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(ffail1, 'wb')  # Ооткрыли wb
                pickle.dump(tus2, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(tus2)
                print(('-') * 40)
                del tus2  # удалили оба массива
                del da1


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть арендаторов или следующий✅', color=VkKeyboardColor.POSITIVE) #КЛАВА СОЗДАТЬ
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажмите кнопку.'
                                 ,keyboard=keyboard)
                    sdat3sdat=0


            if event.from_user and not event.from_me and s_snat3==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                kabibi=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                bisisi = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                silifs = 'sn3kvart.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(silifs, 'rb')  # 1 открытие
                sis3kv = pickle.load(f)  # 2 открытие
                vivir3 = sis3kv[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                vivir3.insert(0, [kabibi, bisisi])  # ДОБАВЛЯЕМ В МАССИВ
                del kabibi
                del bisisi

                print('_' * 40)
                print('В базе: ' + (str(len(vivir3)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(silifs, 'wb')  # Ооткрыли wb
                pickle.dump(vivir3, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(vivir3)
                print(('-') * 40)
                del vivir3  # удалили оба массива
                del sis3kv


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть 3к.кв. или следующая', color=VkKeyboardColor.POSITIVE) #КЛАВА
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажмите кнопку.'
                                 ,keyboard=keyboard)
                    s_snat3=0

                    #return keyboard  #КЛАВА

            if event.from_user and not event.from_me and sdatka2k==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                sisdam=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                sisbilka = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                sifail1 = 'sdam2k.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(sifail1, 'rb')  # 1 открытие
                sisda1 = pickle.load(f)  # 2 открытие
                virtus2 = sisda1[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                virtus2.insert(0, [sisdam, sisbilka])  # ДОБАВЛЯЕМ В МАССИВ
                del sisdam
                del sisbilka

                print('_' * 40)
                print('В базе: ' + (str(len(virtus2)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(sifail1, 'wb')  # Ооткрыли wb
                pickle.dump(virtus2, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(virtus2)
                print(('-') * 40)
                del virtus2  # удалили оба массива
                del sisda1


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть арендаторов или следующий👥', color=VkKeyboardColor.POSITIVE) #КЛАВА СОЗДАТЬ
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажмите кнопку.'
                                 ,keyboard=keyboard)
                    sdatka2k=0

                    #return keyboard  #КЛАВА

            if event.from_user and not event.from_me and snimu2k==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                bibi=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                sisi = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                lifs = 'kvart2sn.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(lifs, 'rb')  # 1 открытие
                sis1kv = pickle.load(f)  # 2 открытие
                vivir1 = sis1kv[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                vivir1.insert(0, [bibi, sisi])  # ДОБАВЛЯЕМ В МАССИВ
                del bibi
                del sisi

                print('_' * 40)
                print('В базе: ' + (str(len(vivir1)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(lifs, 'wb')  # Ооткрыли wb
                pickle.dump(vivir1, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(vivir1)
                print(('-') * 40)
                del vivir1  # удалили оба массива
                del sis1kv


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть 2к.кв. или следующая', color=VkKeyboardColor.POSITIVE) #КЛАВА
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажмите кнопку.'
                                 ,keyboard=keyboard)
                    snimu2k=0


            if event.from_user and not event.from_me and sdam_odnok==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                sdam=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                sbilka = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                fail1 = 'sdam1kkv.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(fail1, 'rb')  # 1 открытие
                sda1 = pickle.load(f)  # 2 открытие
                virtu = sda1[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                virtu.insert(0, [sdam, sbilka])  # ДОБАВЛЯЕМ В МАССИВ
                del sdam
                del sbilka

                print('_' * 40)
                print('В базе: ' + (str(len(virtu)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(fail1, 'wb')  # Ооткрыли wb
                pickle.dump(virtu, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(virtu)
                print(('-') * 40)
                del virtu  # удалили оба массива
                del sda1


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть арендаторов или следующий', color=VkKeyboardColor.POSITIVE) #КЛАВА СОЗДАТЬ
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажмите кнопку.'
                                 ,keyboard=keyboard)
                    sdam_odnok=0


            if event.from_user and not event.from_me and snat1kom==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                abi=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                silka = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                fill = 'kvartira1sn.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(fill, 'rb')  # 1 открытие
                s1kv = pickle.load(f)  # 2 открытие
                vir1 = s1kv[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                vir1.insert(0, [abi, silka])  # ДОБАВЛЯЕМ В МАССИВ
                del abi
                del silka

                print('_' * 40)
                print('В базе: ' + (str(len(vir1)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(fill, 'wb')  # Ооткрыли wb
                pickle.dump(vir1, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(vir1)
                print(('-') * 40)
                del vir1  # удалили оба массива
                del s1kv


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть 1к.кв. или следующая', color=VkKeyboardColor.POSITIVE) #КЛАВА
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажмите кнопку.'
                                 ,keyboard=keyboard)
                    snat1kom=0 # конец заполнения обьявления о снятии 1 к кв


            if event.from_user and not event.from_me and sdam_komn==event.user_id:

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                comnsd=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                sisilsd = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                shopcomsd = 'combocomnatsd.data' # shopcomsd ссылка на имя файла, 'combocomnatsd.data' - название файла
                f = open(shopcomsd, 'rb')  # 1 открытие
                scomsd = pickle.load(f)  # 2 открытие
                peremsd = scomsd[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                peremsd.insert(0, [comnsd, sisilsd])  # ДОБАВЛЯЕМ В МАССИВ
                del comnsd
                del sisilsd

                print('_' * 40)
                print('В базе: ' + (str(len(peremsd)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(shopcomsd, 'wb')  # Ооткрыли wb
                pickle.dump(peremsd, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(peremsd)
                print(('-') * 40)
                del peremsd  # удалили оба массива
                del scomsd


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть объявления или следующее', color=VkKeyboardColor.POSITIVE) #КЛАВА
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажми кнопку.'
                                 ,keyboard=keyboard)
                    sdam_komn=0

            if event.from_user and not event.from_me and sn_komnat==event.user_id: # усовое дело для снятия комнат

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                comn=str(event.text)  #ТЕКСТ СООБЩЕНИЯ
                sisil = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                shopcom = 'combocomnat.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(shopcom, 'rb')  # 1 открытие
                scom = pickle.load(f)  # 2 открытие
                perem = scom[:]  # perem наш массив, полученный полной вырезкой
                f.close()  # закрыли

                perem.insert(0, [comn, sisil])  # ДОБАВЛЯЕМ В МАССИВ
                del comn
                del sisil

                print('_' * 40)
                print('В базе: ' + (str(len(perem)-1)) + ' человек(а)')
                print('_' * 40)

                f = open(shopcom, 'wb')  # Ооткрыли wb
                pickle.dump(perem, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(perem)
                print(('-') * 40)
                del perem  # удалили оба массива
                del scom


                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)           #КЛАВА
                    keyboard.add_button('Смотреть комнаты или следующая', color=VkKeyboardColor.POSITIVE) #КЛАВА
                    keyboard = keyboard.get_keyboard()  #КЛАВА


                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажми кнопку.'
                                 ,keyboard=keyboard)
                    sn_komnat=0
                    #конец усового дела для снятия комнаты

            if event.from_user and not event.from_me and us==event.user_id: # усовое дело для совместников

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print(event.user_id)
                response = event.text.lower()
                keyboard = create_keyboard(response)

                textx1 = str(event.text)  # ТЕКСТ СООБЩЕНИЯ
                ssilx = 'https://vk.com/id' + str(event.user_id)  # ССЫЛЬ НА СТРАНИЦУ

                shoplistfile = 'shoplist.data'
                f = open(shoplistfile, 'rb')  # 1 открытие
                stored = pickle.load(f)  # 2 открытие
                spis = stored[:]  # spis наш массив, полученный полной вырезкой
                f.close()  # закрыли

                spis.insert(0, [textx1, ssilx])  # ДОБАВЛЯЕМ В МАССИВ
                del textx1
                del ssilx

                print('_' * 40)
                print('В базе: ' + (str(len(spis) - 1)) + ' человек(а)')
                print('_' * 40)

                f = open(shoplistfile, 'wb')  # Ооткрыли wb
                pickle.dump(spis, f)  # поместили
                f.close()  # закрыли
                print(('-') * 40)
                print(spis)
                print(('-') * 40)
                del spis  # удалили оба массива
                del stored

                if event.from_user and not event.from_me:
                    send_message(vk_session, 'user_id', event.user_id, message='Ваше объявление добавлено.')
                    # НАДО ДОБАВИТЬ КЛАВИАТУРУ
                    keyboard = VkKeyboard(one_time=False)  # КЛАВА
                    keyboard.add_button('Смотреть анкеты или следующая', color=VkKeyboardColor.POSITIVE)  # КЛАВА
                    keyboard = keyboard.get_keyboard()  # КЛАВА

                    send_message(vk_session, 'user_id', event.user_id, message='Предлагаем к просмотру  объявления. \n'
                                                                               'Для просмотра нажми кнопку.'
                                 , keyboard=keyboard)
                    us=0
                    #конец усового дела

            if event.from_user and not event.from_me:

                if response == "начать":
                    '''начало работы бота'''
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Здравствуйте, я Аренда Бот, бот для подбора квартир и комнат в аренду. Хотите снять или сдать квартиру? Я Аренда Бот и моя миссия помочь вам в этом! Забудьте про доски объявлений и пустую трату времени на поиск подходящей для вас квартиры ….. ведь теперь есть я. \n'
                                         'p.s Аренда Бот.', keyboard=keyboard)

                    send_message(vk_session, 'user_id', event.user_id, message= 'Нажмите нужную кнопку для продолжения.\n'
                                                                                'Для того чтобы найти человека, для совместной \n'
                                                                                'аренды жилья, нажмите "Найти человека, для '
                                                                                'аренды жилья".',keyboard=keyboard)

                elif response == "найти человека, для аренды жилья": #создание анкеты
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о совместной аренде в одном сообщении. '
                                 ,keyboard=keyboard)
                    us=event.user_id # назначение id  переменной us

                elif response == "смотреть анкеты или следующая": #ПРОСМОТР АНКЕТ
                    '''ПРОСМОТР АНКЕТ'''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',keyboard=keyboard)

                    shoplistfile = 'shoplist.data'
                    f = open(shoplistfile, 'rb')  # 1 открытие
                    stored = pickle.load(f)  # 2 открытие
                    spis = stored[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if k == (len(spis)-1):
                        send_message(vk_session, 'user_id', event.user_id, message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                                                                   'Рекомендуем добавить ваше объявление на стену группы.\n'
                                                                                   'https://vk.com/club185937820',keyboard=keyboard)
                        k=0
                    try :
                        for element in spis[k]: # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element, keyboard=keyboard)
                        #print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        k = 0
                    finally:
                        k += 1

                elif response == "удалить свою анкету из объявлений": #страница подтверждения удаления
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "подтвердить удаление объявления": #страница  удаления
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    shoplistfile = 'shoplist.data'
                    f = open(shoplistfile, 'rb')
                    stored = pickle.load(f)  # 2 открытие
                    spis = stored[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for i in range(0, len(spis), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        ssil1 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if ssil1 in spis[i]:
                            print(i)
                            del spis[i]
                            del i
                            del ssil1
                            break

                    print('_' * 40)
                    print(spis)
                    print('_' * 40)
                    print('В базе: ' + (str(len(spis) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(shoplistfile, 'wb')  # Открыли wb
                    pickle.dump(spis, f)           # поместили
                    f.close()                      # закрыли

                    del spis     #удалили оба массива
                    del stored   #удалили оба массива

                elif response == "перейти в главное меню": #начало
                    '''ГЛАВНОЕ МЕНЮ'''
                    send_message(vk_session, 'user_id', event.user_id, message='Нажмите нужную кнопку для продолжения.\n'
                                                                                'Для того чтобы найти соседа, для совместной \n'
                                                                                'аренды жилья, нажмите "Найти соседа, для '
                                                                                'аренды жилья".',keyboard=keyboard)

                elif response == "я хочу снять жилье":  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ ЖИЛЬЕ
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Нажмите нужную кнопку для продолжения.\n'
                                         'Выберите какую недвижимость Вы хотите арендовать.', keyboard=keyboard)

                elif response == 'снять комнату': #создание ОБЪЯВЛЕНИЯ О СНЯТИИ КОМНАТЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о снятии комнаты в одном сообщении. '
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    sn_komnat=event.user_id # переход на страницу заполнения объявления сниму комнату

                elif response == "я хочу сдать жилье":  # ЧЕЛОВЕК ХОЧЕТ СНЯТЬ ЖИЛЬЕ
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Нажмите нужную кнопку для продолжения.\n'
                                         'Выберите какую недвижимость Вы хотите сдавать в аренду.', keyboard=keyboard)

                elif response == 'сдать комнату': #создание ОБЪЯВЛЕНИЯ О СНЯТИИ КОМНАТЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о сдаче комнаты в одном сообщении.'
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    sdam_komn=event.user_id

                elif response == 'смотреть комнаты или следующая': #ПРОСМОТР КОМНАТ
                    '''ПРОСМОТР комнат в аренду'''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',keyboard=keyboard)

                    shop = 'combocomnatsd.data'
                    f = open(shop, 'rb')  # 1 открытие
                    sto = pickle.load(f)  # 2 открытие
                    iss = sto[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if mm == (len(iss)-1):
                        send_message(vk_session, 'user_id', event.user_id, message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                                                                   'Рекомендуем добавить ваше объявление на стену группы.\n'
                                                                                   'https://vk.com/club185937820',keyboard=keyboard)
                        mm=0
                    try :
                        for element1 in iss[mm]: # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element1, keyboard=keyboard)
                        #print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        mm = 0
                    finally:
                        mm += 1

                elif response == "удалить своe объявление": #страница подтверждения удаления АРЕНДАТОРАМ!!!
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',keyboard=keyboard)


                elif response == "подтвердить удаление": #страница  удаления АРЕНДАТОРАМ
                    '''переход на страницу удаления обьявления АРЕНДАТОРАМ'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    sho = 'combocomnat.data'
                    f = open(sho, 'rb')
                    ttt = pickle.load(f)  # 2 открытие
                    sss = ttt[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for oof in range(0, len(sss), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        s1 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if s1 in sss[oof]:
                            print(oof)
                            del sss[oof]
                            del oof
                            del s1
                            break

                    print('_' * 40)
                    print(sss)
                    print('_' * 40)
                    print('В базе: ' + (str(len(sss) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(sho, 'wb')  # Открыли wb
                    pickle.dump(sss, f)           # поместили
                    f.close()                      # закрыли

                    del sss     #удалили оба массива
                    del ttt   #удалили оба массива

                elif response == 'смотреть объявления или следующее': #ПРОСМОТР ОБЪЯВЛЕНИЙ О СНЯТИИ КОМНАТ
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СНЯТИИ КОМНАТ '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',keyboard=keyboard)

                    ppp = 'combocomnat.data'
                    f = open(ppp, 'rb')  # 1 открытие
                    toy = pickle.load(f)  # 2 открытие
                    kent = toy[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if uuu == (len(kent)-1):
                        send_message(vk_session, 'user_id', event.user_id, message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                                                                   'Рекомендуем добавить ваше объявление на стену группы.\n'
                                                                                   'https://vk.com/club185937820',keyboard=keyboard)
                        uuu=0
                    try :
                        for element2 in kent[uuu]: # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element2, keyboard=keyboard)
                        #print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        uuu = 0
                    finally:
                        uuu += 1

                elif response == "удалить объявление о сдаче": #страница подтверждения удаления АРЕНДОДАТЕЛЯМ!!!
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "подтвердить удаление о сдаче": #страница  удаления АРЕНДОДАТЕЛЯМ!!!
                    '''переход на страницу удаления обьявления АРЕНДОДАТЕЛЯМ'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    shod = 'combocomnatsd.data'
                    f = open(shod, 'rb')
                    ttt1 = pickle.load(f)  # 2 открытие
                    sss12 = ttt1[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for oof11 in range(0, len(sss12), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        s12 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if s12 in sss12[oof11]:
                            print(oof11)
                            del sss12[oof11]
                            del oof11
                            del s12
                            break

                    print('_' * 40)
                    print(sss12)
                    print('_' * 40)
                    print('В базе: ' + (str(len(sss12) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(shod, 'wb')  # Открыли wb
                    pickle.dump(sss12, f)           # поместили
                    f.close()                      # закрыли

                    del sss12     #удалили оба массива
                    del ttt1   #удалили оба массива

                elif response == 'снять 1-комнатную квартиру': #создание ОБЪЯВЛЕНИЯ О СНЯТИИ 1 КОМНАТНОЙ КВАРТИРЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о снятии 1 к.кв. в одном сообщении.'
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    snat1kom=event.user_id


                elif response == 'сдать 1-комнатную квартиру': #создание ОБЪЯВЛЕНИЯ О СДАЧЕ 1 КОМНАТНОЙ КВАРТИРЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о сдаче 1 к.кв. в одном сообщении.'
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    sdam_odnok=event.user_id

                elif response == 'смотреть 1к.кв. или следующая': #ПРОСМОТР ОБЪЯВЛЕНИЙ О СДАЧЕ КВАРТИР
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СДАЧЕ КВАРТИР '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',keyboard=keyboard)

                    qqq = 'sdam1kkv.data'
                    f = open(qqq, 'rb')  # 1 открытие
                    toys = pickle.load(f)  # 2 открытие
                    kents = toys[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if schetch == (len(kents)-1):
                        send_message(vk_session, 'user_id', event.user_id, message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                                                                   'Рекомендуем добавить ваше объявление на стену группы.\n'
                                                                                   'https://vk.com/club185937820',keyboard=keyboard)
                        schetch=0
                    try :
                        for element3 in kents[schetch]: # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element3, keyboard=keyboard)
                        #print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        schetch = 0
                    finally:
                        schetch += 1

                elif response == 'смотреть арендаторов или следующий':  # ПРОСМОТР ОБЪЯВЛЕНИЙ О  СНЯТИИ КВАРТИР
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СНЯТИИ КВАРТИР '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',
                                 keyboard=keyboard)

                    qqq1 = 'kvartira1sn.data'
                    f = open(qqq1, 'rb')  # 1 открытие
                    toys1 = pickle.load(f)  # 2 открытие
                    kents2 = toys1[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if godg == (len(kents2) - 1):
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        godg = 0
                    try:
                        for element233 in kents2[godg]:  # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element233, keyboard=keyboard)
                        # print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        godg = 0
                    finally:
                        godg += 1

                elif response == "удалить объявление о снятии 1к.кв.": #страница подтверждения удаления О СНЯТИИ
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "❗подтвердить удаление": #страница  удаления АРЕНДАТОРАМ 1 комнатные!!!
                    '''переход на страницу удаления обьявления АРЕНДаторам'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    shod1 = 'kvartira1sn.data'
                    f = open(shod1, 'rb')
                    ttt99 = pickle.load(f)  # 2 открытие
                    sss99 = ttt99[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for oof99 in range(0, len(sss99), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        s99 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if s99 in sss99[oof99]:
                            print(oof99)
                            del sss99[oof99]
                            del oof99
                            del s99
                            break

                    print('_' * 40)
                    print(sss99)
                    print('_' * 40)
                    print('В базе: ' + (str(len(sss99) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(shod1, 'wb')  # Открыли wb
                    pickle.dump(sss99, f)           # поместили
                    f.close()                      # закрыли

                    del sss99     #удалили оба массива
                    del ttt99   #удалили оба массива

                elif response == "удалить объявление о сдаче 1к.кв.": #страница подтверждения удаления О СНЯТИИ
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "‼подтвердить удаление‼": #страница  удаления АРЕНДОДАТЕЛЕЙ 1 комнатные!!!
                    '''переход на страницу удаления обьявления АРЕНДОДАТЕЛЕЙ 1 комнатных'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    shod33 = 'sdam1kkv.data'
                    f = open(shod33, 'rb')
                    ttt33 = pickle.load(f)  # 2 открытие
                    sss33 = ttt33[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for oof33 in range(0, len(sss33), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        s33 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if s33 in sss33[oof33]:
                            print(oof33)
                            del sss33[oof33]
                            del oof33
                            del s33
                            break

                    print('_' * 40)
                    print(sss33)
                    print('_' * 40)
                    print('В базе: ' + (str(len(sss33) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(shod33, 'wb')  # Открыли wb
                    pickle.dump(sss33, f)           # поместили
                    f.close()                      # закрыли

                    del sss33     #удалили оба массива
                    del ttt33   #удалили оба массива

                elif response == 'снять 2-комнатную квартиру': #создание ОБЪЯВЛЕНИЯ О СНЯТИИ 2 КОМНАТНОЙ КВАРТИРЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о снятии 2 к.кв. в одном сообщении.'
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    snimu2k=event.user_id #функция для добавления объявления о снятии

                elif response == 'сдать 2-комнатную квартиру': #создание ОБЪЯВЛЕНИЯ О СДАЧЕ 2 КОМНАТНОЙ КВАРТИРЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о сдаче 2 к.кв. в одном сообщении.'
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    sdatka2k=event.user_id  #ОБРАБОТКА И ЗАПОЛНЕНИЕ ОБЪЯВЛЕНИЯ О СДАЧЕ 2 К КВ

                elif response == 'смотреть 2к.кв. или следующая': #ПРОСМОТР ОБЪЯВЛЕНИЙ О СДАЧЕ 2 комнатных КВАРТИР
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СДАЧЕ КВАРТИР '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',keyboard=keyboard)

                    sysqqq = 'sdam2k.data'
                    f = open(sysqqq, 'rb')  # 1 открытие
                    sytoys = pickle.load(f)  # 2 открытие
                    sykents = sytoys[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if sychetch == (len(sykents)-1):
                        send_message(vk_session, 'user_id', event.user_id, message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                                                                   'Рекомендуем добавить ваше объявление на стену группы.\n'
                                                                                   'https://vk.com/club185937820',keyboard=keyboard)
                        sychetch=0
                    try :
                        for element3s in sykents[sychetch]: # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element3s, keyboard=keyboard)
                        #print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        sychetch = 0
                    finally:
                        sychetch += 1

                elif response == 'смотреть арендаторов или следующий👥':  # ПРОСМОТР ОБЪЯВЛЕНИЙ О  СНЯТИИ 2комн КВАРТИР
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СНЯТИИ КВАРТИР ДВУШЕК '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',
                                 keyboard=keyboard)

                    pepqqq1 = 'kvart2sn.data'
                    f = open(pepqqq1, 'rb')  # 1 открытие
                    peptoys1 = pickle.load(f)  # 2 открытие
                    pepkents2 = peptoys1[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if pepgodg == (len(pepkents2) - 1):
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        pepgodg = 0
                    try:
                        for element2334 in pepkents2[pepgodg]:  # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element2334, keyboard=keyboard)
                        # print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        pepgodg = 0
                    finally:
                        pepgodg += 1

                elif response == "удалить объявление о снятии 2к.кв.":  # страница подтверждения удаления О СНЯТИИ
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "подтвердить удаление👥": #страница  удаления О СНЯТИИ 2  комнатные!!!
                    '''переход на страницу удаления обьявления АРЕНДаторам'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    shod1111 = 'kvart2sn.data'
                    f = open(shod1111, 'rb')
                    ttt00 = pickle.load(f)  # 2 открытие
                    sss00 = ttt00[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for oof00 in range(0, len(sss00), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        s00 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if s00 in sss00[oof00]:
                            print(oof00)
                            del sss00[oof00]
                            del oof00
                            del s00
                            break

                    print('_' * 40)
                    print(sss00)
                    print('_' * 40)
                    print('В базе: ' + (str(len(sss00) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(shod1111, 'wb')  # Открыли wb
                    pickle.dump(sss00, f)           # поместили
                    f.close()                      # закрыли

                    del sss00     #удалили оба массива
                    del ttt00   #удалили оба массива

                elif response == "удалить объявление о сдаче 2к.кв.": #страница подтверждения удаления О СНЯТИИ
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "👥подтвердить удаление": #страница  удаления О Сдаче  2  комнатные!!!
                    '''переход на страницу удаления обьявления СДАТЧИКАМ'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    shod0009 = 'sdam2k.data'
                    f = open(shod0009, 'rb')
                    ttt01 = pickle.load(f)  # 2 открытие
                    sss01 = ttt01[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for oof01 in range(0, len(sss01), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        s01 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if s01 in sss01[oof01]:
                            print(oof01)
                            del sss01[oof01]
                            del oof01
                            del s01
                            break

                    print('_' * 40)
                    print(sss01)
                    print('_' * 40)
                    print('В базе: ' + (str(len(sss01) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(shod0009, 'wb')  # Открыли wb
                    pickle.dump(sss01, f)           # поместили
                    f.close()                      # закрыли

                    del sss01     #удалили оба массива
                    del ttt01   #удалили оба массива

                elif response == 'снять 3-комнатную квартиру': #создание ОБЪЯВЛЕНИЯ О СНЯТИИ 3 КОМНАТНОЙ КВАРТИРЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о снятии 3 к.кв. в одном сообщении. '
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    s_snat3=event.user_id #функция для добавления объявления о снятии 3 КОМНАТНЫХ

                elif response == 'сдать 3-комнатную квартиру': #создание ОБЪЯВЛЕНИЯ О СДАЧЕ 3 КОМНАТНОЙ КВАРТИРЫ
                    '''переход на страницу заполнения обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Напишите текст объявления о сдаче 3 к.кв. в одном сообщении.'
                                 ,keyboard=keyboard)
                    #ниже будет функция для заполнения текста объявления.
                    sdat3sdat=event.user_id #ОБРАБОТКА И ЗАПОЛНЕНИЕ ОБЪЯВЛЕНИЯ О СДАЧЕ 2 К КВ

                elif response == 'смотреть 3к.кв. или следующая': #ПРОСМОТР ОБЪЯВЛЕНИЙ О СДАЧЕ 3 комнатных КВАРТИР
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СДАЧЕ КВАРТИР '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',keyboard=keyboard)

                    sysqqqr = 'ssdam3k.data'
                    f = open(sysqqqr, 'rb')  # 1 открытие
                    sytoysr = pickle.load(f)  # 2 открытие
                    sykentsr = sytoysr[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if sychetchr == (len(sykentsr)-1):
                        send_message(vk_session, 'user_id', event.user_id, message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                                                                   'Рекомендуем добавить ваше объявление на стену группы.\n'
                                                                                   'https://vk.com/club185937820',keyboard=keyboard)
                        sychetchr=0
                    try :
                        for element3sr in sykentsr[sychetchr]: # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element3sr, keyboard=keyboard)
                        #print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        sychetchr = 0
                    finally:
                        sychetchr += 1

                elif response == 'смотреть арендаторов или следующий✅':  # ПРОСМОТР ОБЪЯВЛЕНИЙ О  СНЯТИИ 3комн КВАРТИР
                    '''ПРОСМОТР ОБЪЯВЛЕНИЙ О СНЯТИИ КВАРТИР ТРЕШЕК '''
                    send_message(vk_session, 'user_id', event.user_id, message='Объявление пользователя: ',
                                 keyboard=keyboard)

                    pepqqq1a = 'sn3kvart.data'
                    f = open(pepqqq1a, 'rb')  # 1 открытие
                    peptoys1a = pickle.load(f)  # 2 открытие
                    pepkents2a = peptoys1a[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    if pepgodga == (len(pepkents2a) - 1):
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот"\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        pepgodga = 0
                    try:
                        for element2334a in pepkents2a[pepgodga]:  # ПЕРЕБОР АНКЕТ С ИНДЕКСОМ k
                            send_message(vk_session, 'user_id', event.user_id, message=element2334a, keyboard=keyboard)
                        # print(massive[k][i])
                    except:
                        send_message(vk_session, 'user_id', event.user_id,
                                     message='Подписывайтесь на наше сообщество "Аренда Бот".\n'
                                             'Рекомендуем добавить ваше объявление на стену группы.\n'
                                             'https://vk.com/club185937820', keyboard=keyboard)
                        pepgodga = 0
                    finally:
                        pepgodga += 1

                elif response == "удалить объявление о снятии 3к.кв.":  # страница подтверждения удаления О СНЯТИИ 3 к кв
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "подтвердить удаление✅✅":  # страница  удаления О СНЯТИИ 3  комнатные!!!
                    '''переход на страницу удаления обьявления АРЕНДаторам 3 комнатных'''
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Спасибо, что воспользовались услугами нашего \n'
                                         'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                         'https://vk.com/club185937820', keyboard=keyboard)
                    qwshod1111 = 'sn3kvart.data'
                    f = open(qwshod1111, 'rb')
                    qwttt00 = pickle.load(f)  # 2 открытие
                    qwsss00 = qwttt00[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for qwoof00 in range(0, len(qwsss00), 1):  # ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        qws00 = 'https://vk.com/id' + str(event.user_id)  # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if qws00 in qwsss00[qwoof00]:
                            print(qwoof00)
                            del qwsss00[qwoof00]
                            del qwoof00
                            del qws00
                            break

                    print('_' * 40)
                    print(qwsss00)
                    print('_' * 40)
                    print('В базе: ' + (str(len(qwsss00) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(qwshod1111, 'wb')  # Открыли wb
                    pickle.dump(qwsss00, f)  # поместили
                    f.close()  # закрыли

                    del qwsss00  # удалили оба массива
                    del qwttt00  # удалили оба массива

                elif response == "удалить объявление о сдаче 3к.кв.": #страница подтверждения удаления О СДАЧЕ
                    '''переход на страницу удаления обьявления'''
                    send_message(vk_session, 'user_id', event.user_id, message='Подтвердите удаление нажав на кнопку.',
                                 keyboard=keyboard)

                elif response == "подтвердить удаление⚠": #страница  удаления О Сдаче  3  комнатные!!!
                    '''переход на страницу удаления обьявления СДАТЧИКАМ'''
                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо, что воспользовались услугами нашего \n'
                                                                               'чат бота. Подписывайтесь на наше сообщество "Аренда Бот" \n'
                                                                               'https://vk.com/club185937820',keyboard=keyboard)
                    ddshod0009 = 'ssdam3k.data'
                    f = open(ddshod0009, 'rb')
                    ddttt01 = pickle.load(f)  # 2 открытие
                    ddsss01 = ddttt01[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for ddoof01 in range(0, len(ddsss01), 1):#ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        dds01 = 'https://vk.com/id' + str(event.user_id) # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if dds01 in ddsss01[ddoof01]:
                            print(ddoof01)
                            del ddsss01[ddoof01]
                            del ddoof01
                            del dds01
                            break

                    print('_' * 40)
                    print(ddsss01)
                    print('_' * 40)
                    print('В базе: ' + (str(len(ddsss01) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(ddshod0009, 'wb')  # Открыли wb
                    pickle.dump(ddsss01, f)           # поместили
                    f.close()                      # закрыли

                    del ddsss01     #удалили оба массива
                    del ddttt01   #удалили оба массива

                else :

                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Для вашего удобства мы создали кнопки команд. \n'
                                         'Если нет кнопок на экране, нажмите на квадрат \n '
                                         'с четыремя точками.', keyboard=keyboard)



