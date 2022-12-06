from io import StringIO

input_file = 'input_data.txt'

def read_input():
    read_input_file = open(input_file, 'r')
    read_input_file_data = read_input_file.read()
    input_values = read_input_file_data.split("\n")
    return input_values

def input_data_stream(input_data):
    for input_data_line in input_data:
        input_stream = StringIO(input_data_line)
        return input_stream

def read_header_stream(input_stream, index):
    input_stream.seek(index)
    return input_stream.read()[:4], int(index)

def read_message_stream(input_stream, index):
    input_stream.seek(index)
    return input_stream.read()[:14], int(index)

def check_header_protocol_stream(header, index):
    x = list(set(header))
    y = list(header)
    x.sort()
    y.sort()
    if (x == y):
        x = []
        y = []
        return True, index
    else:
        index += 1
        return False, index

def puzzle_1(input_data):
    header_index_correct = False
    input_stream_index = 0
    input_stream_for_protocol = input_data_stream(input_data)
    while not header_index_correct:
        header_protocol_stream, input_stream_index = read_header_stream(input_stream_for_protocol, input_stream_index)
        header_index_correct, input_stream_index = check_header_protocol_stream(header_protocol_stream, input_stream_index)
    print(f"Puzzle 1\nProtocol starts with {header_protocol_stream} at index {input_stream_index} after processing {input_stream_index + 4} characters")

def puzzle_2(input_data):
    header_index_correct = False
    input_stream_index = 0
    input_stream_for_message = input_data_stream(input_data)
    while not header_index_correct:
        header_protocol_stream, input_stream_index = read_message_stream(input_stream_for_message, input_stream_index)
        header_index_correct, input_stream_index = check_header_protocol_stream(header_protocol_stream, input_stream_index)
    print(f"Puzzle 2\nMessage starts with {header_protocol_stream} at index {input_stream_index} after processing {input_stream_index + 14} characters")

def main():
    read_input_data = read_input()
    puzzle_1(read_input_data)
    puzzle_2(read_input_data)


if __name__ == "__main__":
    main()
