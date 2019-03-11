import pickle

def request_plaintext():
    print("Select plaintext source:")
    print("1. File")
    print("2. Typed Message")
    input_mode = int(input("Select a number: "))

    if input_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'rb')
        message = input_file.read().decode()
    elif input_mode == 2:
        message = input("Please enter the plaintext: ")

    return message


def request_ciphertext():
    print("Select ciphertext source:")
    print("1. File")
    print("2. Typed Message")
    input_mode = int(input("Select a number: "))

    if input_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'rb')
        message = input_file.read().decode()
    elif input_mode == 2:
        message = input("Please enter the ciphertext: ")

    return message


def output_ciphertext(ciphertext):
    print("Select where to output ciphertext:")
    print("1. File")
    print("2. Terminal")
    output_mode = int(input("Select a number: "))

    if output_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'wb')
        input_file.write(ciphertext.encode('utf-8'))
    elif output_mode == 2:
        print(ciphertext)


def output_plaintext(plaintext):
    print("Select where to output plaintext:")
    print("1. File")
    print("2. Terminal")
    output_mode = int(input("Select a number: "))

    if output_mode == 1:
        filename = input("Please enter the filename: ")
        input_file = open(filename, 'wb')
        input_file.write(plaintext.encode('utf-8'))
    elif output_mode == 2:
        print(plaintext)

def request_seed():
    seed = input("Enter the seed to initialize the block cipher: ")

    seed = sum(map(ord, seed))

    return seed


def save_table(table):
    with open('table.pkl', 'wb') as table_file:
        pickle.dump(table, table_file, protocol=pickle.HIGHEST_PROTOCOL)


def load_table():
    with open('table.pkl', 'rb') as table_file:
        return pickle.load(table_file)