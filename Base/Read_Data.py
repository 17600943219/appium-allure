import os
import yaml


def read_test_data(file_name):
    file_path = os.getcwd() + os.sep + 'Data' + os.sep + file_name + '.yaml'
    # file_path = os.path.abspath('..') + os.sep + 'Data' + os.sep + file_name + '.yaml'
    with open(file_path, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    print(read_test_data('test'))
