from sys import getsizeof
from os.path import getsize
from helper import Helper


class Buffer:

    def __init__(self):
        self.__buffer = ""
        self.current_file_name = Helper.get_new_file_name()

    @property
    def buffer(self):
        return self.__buffer

    @buffer.setter
    def buffer(self, value):
        self.__buffer = value

    def __str__(self):
        return self.buffer

    def clear(self):
        """
        This function clears the buffer.
        """

        self.buffer = ""

    def __write_to_file(self, data):
        """
        This function writes the given data directly to the file on disk without checking if the size of the file exceed
        twenty KB.

        :param data: Data to be written to the file
        """

        path = "logs\\" + self.current_file_name
        with open(path, "a", encoding="UTF-8") as file:
            file.write(data)

    def write_to_file(self):
        """
        This function writes the buffer to the file on disk, but before that it checks if the file size is not exceed
        twenty KB. If exceeded then a new file name is created and the buffer is written to that file.
        """

        twenty_kb = 20480
        file = self.current_file_name

        try:
            if getsize(file) >= twenty_kb:
                self.current_file_name = Helper.get_new_file_name()
                self.__write_to_file(self.buffer)
                self.clear()
            else:
                self.__write_to_file(self.buffer)
                self.clear()

        except FileNotFoundError:
            self.__write_to_file(self.buffer)
            self.clear()

    def write(self, text):
        """
        This function writes the given text to the buffer. If the size of the buffer will exceed one KB, then
        the buffer will be written to the file on disk.

        :param text: Text to be written to the buffer
        """

        one_kb = 1024

        if getsizeof(self.buffer) >= one_kb:
            self.write_to_file()
            self.buffer += text
        else:
            self.buffer += text

    def check_memory_usage(self):
        """
        This function prints the size of the buffer in bytes.
        """

        print(getsizeof(self.buffer))
