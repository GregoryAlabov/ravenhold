#!/usr/bin/env python3
import vk_api.vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import random
import time
import config

vk_session = vk_api.VkApi(token=config.token_server2)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Сообщение от :' + str(event.user_id))
            print('Текст сообщения: ' + str(event.text))
            message_text = event.text.lower()

            greeting_message = 'Приветствую!\nДля подробной информации по работе бота введите \"помощь\"'
            error_message = 'Для подробной информации по работе бота введите \"помощь\"'
            help_message = 'Ниже приведен список команд данного чатбота:\n ' \
                           '\"Время\", чтобы узнать текущее время \n' \
                           '\"упс\" для забавного ролика \n' \
                           '\"кот\" чтобы получить фотографию замечательного котейки \n' \
                           '\"кусь\" если хотите чтобы вас укусили\n' \
                           'После не забудьте поблагодарить бота'
            now_time = 'Текущее время ' + str(datetime.strftime(datetime.now(), "%H:%M:%S"))

            if event.from_user and not event.from_me:
                if message_text == 'привет':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': greeting_message,
                                       'random_id': 0})
                elif message_text == 'помощь':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': help_message,
                                       'random_id': 0})
                elif message_text == 'время':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': now_time,
                                       'random_id': 0})
                elif message_text == 'спасибо':
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'sticker_id': "13824",
                                       'random_id': 0})
                elif message_text == "василий" or message_text == "вася" or message_text == "васян" \
                        or message_text == "васятка" or message_text == "кот":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': "Не желаете ли немного Василия в ленту? =)",
                                       'attachment': 'photo-183611279_457239023',
                                       'random_id': 0})
                elif message_text == "упс":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'attachment': 'video117268894_456239490',
                                       'random_id': 0})
                elif message_text == "кусь":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'sticker_id': "14214",
                                       'random_id': 0})
                else:
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id,
                                       'message': error_message,
                                       'random_id': 0})
