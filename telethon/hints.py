import datetime
import io
import typing

from . import helpers
from .tl import types, custom

Phone = str
Username = str
PeerID = int
Entity = typing.Union[types.User, types.Chat, types.Channel]
FullEntity = typing.Union[types.UserFull, types.messages.ChatFull, types.ChatFull, types.ChannelFull]

EntityLike = typing.Union[
    Phone,
    Username,
    PeerID,
    types.TypePeer,
    types.TypeInputPeer,
    Entity,
    FullEntity
]
EntitiesLike = typing.Union[EntityLike, typing.Sequence[EntityLike]]

ButtonLike = typing.Union[types.TypeKeyboardButton, custom.Button]
MarkupLike = typing.Union[
    types.TypeReplyMarkup,
    ButtonLike,
    typing.Sequence[ButtonLike],
    typing.Sequence[typing.Sequence[ButtonLike]]
]

TotalList = helpers.TotalList

DateLike = typing.Optional[typing.Union[float, datetime.datetime, datetime.date, datetime.timedelta]]


LocalPath = str
ExternalUrl = str
BotFileID = str
FileLike = typing.Union[
    LocalPath,
    ExternalUrl,
    BotFileID,
    bytes,
    io.IOBase,
    types.TypeMessageMedia,
    types.TypeInputFile,
    types.TypeInputFileLocation
]

OutFileLike = typing.Union[
    str,
    typing.Type[bytes],
    io.IOBase
]

MessageLike = typing.Union[str, types.Message]
MessageIDLike = typing.Union[int, types.Message, types.TypeInputMessage]

ProgressCallback = typing.Callable[[int, int], None]
