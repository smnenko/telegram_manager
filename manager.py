import os
import logging

from session import TelegramSession


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
fmt = logging.Formatter('MANAGER | %(levelname)s | %(asctime)s | %(message)s', '%Y-%m-%d %H:%M:%S')
sh.setFormatter(fmt)
logger.addHandler(sh)


class TelegramManager(list):
    def __init__(self):
        super().__init__()
        self.path = 'accounts'
        self._setup()

    def _setup(self):
        if os.path.exists(self.path) and os.path.isdir(self.path):
            logger.info('Sessions folder exists')
            logger.info('Sessions loading started')

            session_files = os.scandir('accounts')
            for session_file in session_files:
                logger.info(f'Session {session_file.name} was found')
                api_id, api_hash = session_file.name.replace('.txt', '').split('_')
                session = TelegramSession(api_id, api_hash)
                self.append(session)
        else:
            logger.info('Sessions folder is not exists')
            os.mkdir(self.path)
            logger.info('Sessions folder was created')

    def add_session(self, api_id: str, api_hash: str):
        session = TelegramSession(api_id, api_hash)
        self.append(session)
        logger.info('Session was added')

    def follow_channel(self, channel: str, count: int):
        subscribed = 0
        for account in sorted(self, key=lambda x: x.channel_count):
            account.follow_channel(channel)
            subscribed += 1
        logger.info(f'Subscriptions to the channel {channel} in count {subscribed} of required {count} were added')

    def view_posts(self):
        for account in self:
            account.view_posts()
        logger.info('Posts were viewed')
