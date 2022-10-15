import collections


def sort_string(string):
    string = ''.join(sorted(string))
    return string


def string_to_array(string):
    return [char for char in string]


def array_to_string(array):
    return ''.join(array)


def filter_chars_out_from_string(string, filterout_array):
    for char in filterout_array:
        string = string.replace(char, "")
    return string


def count_char_in_string(string):
    frequencies = collections.Counter(string)
    count_dict = {}
    for key, value in frequencies.items():
        if value > 0:
            count_dict[key] = value
    return dict(sorted(count_dict.items(), key=lambda item: item[1]))
