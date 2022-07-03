from threading import Timer


class RepeatedTimer:
    """
    This class creates an object (Timer), that infinitely calls the given function in a new thread
    every given time interval.
    """

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.__timer = None
        self.is_running = False

        self.start()

    def __run(self):
        self.is_running = False
        self.function(*self.args, **self.kwargs)
        self.start()

    def start(self):
        """
        This function runs the RepeatedTimer. It will infinitely call the given function in a new thread
        every given time interval.
        """

        if not self.is_running:
            self.is_running = True
            self.__timer = Timer(self.interval, self.__run)
            self.__timer.start()

    def stop(self):
        """
        This function stops the RepeatedTimer.
        """

        self.is_running = False
        self.__timer.cancel()
