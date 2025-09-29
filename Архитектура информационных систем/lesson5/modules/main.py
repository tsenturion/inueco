from input_func import *
from process_func import *
from output_func import *

if __name__ == '__main__':
    data = input_data()
    data = process_data(data)
    output_data(data=data)
