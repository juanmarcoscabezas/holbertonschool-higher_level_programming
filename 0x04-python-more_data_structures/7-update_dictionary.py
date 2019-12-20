def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        new_dict = {key: value}
        a_dictionary.update(new_dict)
    return a_dictionary
