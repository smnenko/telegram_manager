from telethon import TelegramClient


class TelegramAccount:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session = f'accounts/{self.api_id}'

        self._setup()

    def _setup(self):
        with TelegramClient(self.session, self.api_id, self.api_hash):
            pass


if __name__ == '__main__':
    with open('welcome.txt') as f:
        for line in f.readlines():
            print(line.strip())
    inp = input(
        'Select option you need:\n'
        '[x] 1. Add account to our system\n'
        '[x] 2. Subscribe to group\n'
        '[x] 3. View all group posts\n'
        'Your choice is => #'
    )

