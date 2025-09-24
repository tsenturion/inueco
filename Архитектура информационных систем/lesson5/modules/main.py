import input_func, process_func, output_func

if __name__ == '__main__':
    data = input_func.input_data()
    data = process_func.process_data(data)
    output_func.output_data(data=data)
