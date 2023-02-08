def get_format(file_path):
    index = len(file_path) - 1
    while index >= 0:
        if file_path[index] == '.':
            break
        index = index - 1
    return (file_path[:index], file_path[index:])
