
import datetime
from vk_function import VkInfo
from vkinder_db import Vkinderdb


def find_candidate(token, user_id, sex, city, year):
    """Ищем кандидата по заданным параметрам. Затем идем по  списку ID кандидатов и если такого пользователя нет в
       базе данных то возвращаем список с id кандидата и названием фотографий"""
    candidate = VkInfo(token)
    vkdb = Vkinderdb()
    vkdb.create_table()
    candidate_list = candidate.search_users(sex, city, year)
    photo_list = []
    for item in candidate_list:
        if item not in vkdb.get_users(user_id):
            vkdb.insert_user(user_id, item)
            photo_list.append(item)
            photo_list.append(candidate.get_photos(item))
            return photo_list
        else:
            continue


def get_age():
    age = str(datetime.date.today())[:4]
    return int(age)


def get_list_parametrs(token, user_id):
    user_param = VkInfo(token)
    parametrs_list = user_param.get_user_info(user_id)
    return parametrs_list