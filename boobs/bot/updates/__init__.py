from .base import BaseUpdate
from .types import *

Cock = Message = MessageUpdate
CallbackQuery = CallbackQueryUpdate
InlineQuery = InlineQueryUpdate
ChatJoinRequest = ChatJoinRequestUpdate
ChatMember = ChatMemberUpdate
ChosenInlineResult = ChosenInlineResultUpdate
PreCheckoutQuery = PreCheckoutQueryUpdate
ShippingQuery = ShippingQueryUpdate
PollAnswer = PollAnswerUpdate
Poll = PollUpdate

__all__ = (
    "BaseUpdate",
    "BotUpdateType",
    "Cock",
    "Message",
    "CallbackQuery",
    "InlineQuery",
    "ChatJoinRequest",
    "ChatMember",
    "ChosenInlineResult",
    "PreCheckoutQuery",
    "ShippingQuery",
    "PollAnswer",
    "Poll",
)
