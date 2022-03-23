from manager import TelegramManager


if __name__ == '__main__':
    with open('welcome.txt') as f:
        for line in f.readlines():
            print(line.strip())

    running = True
    manager = TelegramManager()
    while running:
        inp = input(
            '[x] 1. Add account to our system\n'
            '[x] 2. Subscribe to channel\n'
            '[x] 3. View all group posts\n'
            'Your choice is => '
        )

        if inp.upper() == 'Q' or inp.upper() == 'QUIT':
            running = False
        elif inp == '1':
            api_id = input('Enter API_ID: ')
            api_hash = input('Enter API_HASH: ')
            manager.add_session(api_id, api_hash)
        elif inp == '2':
            channel = input('Enter channel username or invite id: ')
            count = int(input('Enter required subscribes count: '))
            manager.follow_channel(channel, count)
        elif inp == '3':
            manager.view_posts()
