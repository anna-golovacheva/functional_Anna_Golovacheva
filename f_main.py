def filter_data(val: str, list_to_filter: list) -> list:
    filtered_data = list(filter(lambda line: val in line, list_to_filter))
    return filtered_data


def map_data(num: str, list_to_map: list) -> list:

    mapped_data = list(map(lambda element: element.split(" ")[int(num)], list_to_map))
    return mapped_data


def unique_data(_, list_to_make_unique: list) -> list:
    unique_list = list(set(list_to_make_unique))
    return unique_list


def sort_data(turn: str, list_to_sort: list) -> list:
    if turn == 'desc':
        reversed = True
    elif turn == 'asc':
        reversed = False
    sorted_list = sorted(list_to_sort, reverse=reversed)
    return sorted_list


def limit_data(num: str, list_to_limit: list) -> list:
    int_num = int(num)
    return list_to_limit[:int_num]


def file_work(file) -> list:
    with open(file, encoding='utf-8') as file_data:
        lines_list = [lines.replace(' - - ', ' ').rstrip() for lines in file_data]
        return lines_list


def execute(list_of_command_items: list, list_of_data: list) -> list:
    command_dict = {
        "filter": filter_data,
        "limit": limit_data,
        "map": map_data,
        "sort": sort_data,
        "unique": unique_data
    }

    for command in list_of_command_items:
        list_of_data = command_dict[command[0]](command[1], list_of_data)

    return list_of_data

def main():
    while True:
        data_list = file_work('apache_logs.txt')

        user_input = input('Введите команду: ')
        if user_input == 'stop':
            break
        else:
            user_input_list = user_input.split(' | ')
            command_items = list(map(lambda items: items.split(' '), user_input_list))

            print(execute(command_items, data_list))


if __name__ == '__main__':
    main()
