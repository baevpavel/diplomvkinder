import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import token_vkinder

from datetime import datetime

vk = vk_api.VkApi(token=token_vkinder)


def message_send(user_id, message, attachment=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'attachment': attachment,
               'random_id': get_random_id()
               }
              )


longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message_send(event.user_id, event.text.lower())
