from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
from telethon.tl.types import Channel


class TelegramSession:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_file = f'accounts/{self.api_id}_{self.api_hash}'
        self.channel_count = None
        self.session = TelegramClient(
            self.session_file,
            self.api_id,
            self.api_hash
        )

        self._setup()

    def _setup(self):
        self._refresh_channel_count()

    def _refresh_channel_count(self):
        self.channel_count = 0
        with self.session:
            for dialog in self.session.iter_dialogs():
                if isinstance(dialog.entity, Channel):
                    self.channel_count += 1

    def follow_channel(self, channel_id):
        with self.session:
            self.session.loop.run_until_complete(
                self.session(JoinChannelRequest(channel_id))
            )

    def view_posts(self):
        with self.session:
            for dialog in self.session.iter_dialogs():
                if isinstance(dialog.entity, Channel):
                    message_ids = [
                        i.id
                        for i in self.session.iter_messages(entity=dialog.entity, limit=100)
                    ]
                    self.session.loop.run_until_complete(
                        self.session(GetMessagesViewsRequest(
                            peer=dialog,
                            id=message_ids,
                            increment=True
                        ))
                    )
