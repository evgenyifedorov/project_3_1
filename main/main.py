from src.utils import *

operations = load_json_operations()

for operation in operations:
    print(f'{format_date(operation["date"])} {operation["description"]}')
    if operation['description'] == 'Открытие вклада':
        print(mask_amount_number(operation["to"]))
        print(f'{operation["operationAmount"]["amount"]} '
              f'{operation["operationAmount"]["currency"]["name"]}\n')
    elif operation['description'] == 'Перевод со счета на счет':
        print (f'{mask_amount_number(operation["from"])} -> '
               f'{mask_amount_number(operation["to"])}')
        print (f'{operation["operationAmount"]["amount"]} '
               f'{operation["operationAmount"]["currency"]["name"]}\n')
    else:
        print(f'{mask_card_number(operation["from"])} -> '
              f'{mask_amount_number(operation["to"])}')
        print(f'{operation["operationAmount"]["amount"]} '
              f'{operation["operationAmount"]["currency"]["name"]}\n')