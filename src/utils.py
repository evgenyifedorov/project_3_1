import os
from config import ROOT_DIR
import json


OPERATION_PATH = os.path.join(ROOT_DIR, 'operations.json')

def load_json_operations():
    """читает json файл и выводит пять операций EXECUTED"""

    with open(OPERATION_PATH, encoding='UTF-8') as file:
        operation_files = json.load(file)
        operation_list = []
        for operation in operation_files:
            if operation == {}:
                continue
            if operation['state'] == 'EXECUTED':
                operation_list.append(operation)
        sort_lising = sorted(operation_list, key=lambda x: x['date'], reverse=True)
        five_operations = sort_lising[:5]

        return five_operations


def format_date(date):
    """Получает отформатированную дату
   """
    formatted_date = date.split('T')[0].split('-')
    formatted_date = '{}.{}.{}'.format(formatted_date[2], formatted_date[1], formatted_date[0])
    return formatted_date



def mask_card_number(card_number):
    """Получает замаскированный номер карты
    """
    masked_number = '{} {}** **** {}'.format(card_number[:-12], card_number[-10:-8], card_number[-4:])
    return masked_number


def mask_amount_number(amount_number):
    """Получает замаскированный вид счета
    """
    masked_amount = 'Счет **{}'.format(amount_number[-4:])
    return masked_amount