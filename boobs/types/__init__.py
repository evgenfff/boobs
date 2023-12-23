from .methods import APIMethods as APIMethods
from .objects import (
    Update as Update,
    WebhookInfo as WebhookInfo,
    User as User,
    Chat as Chat,
    Message as Message,
    MessageId as MessageId,
    MessageEntity as MessageEntity,
    PhotoSize as PhotoSize,
    Animation as Animation,
    Audio as Audio,
    Document as Document,
    Story as Story,
    Video as Video,
    VideoNote as VideoNote,
    Voice as Voice,
    Contact as Contact,
    Dice as Dice,
    PollOption as PollOption,
    PollAnswer as PollAnswer,
    Poll as Poll,
    Location as Location,
    Venue as Venue,
    WebAppData as WebAppData,
    ProximityAlertTriggered as ProximityAlertTriggered,
    MessageAutoDeleteTimerChanged as MessageAutoDeleteTimerChanged,
    ForumTopicCreated as ForumTopicCreated,
    ForumTopicClosed as ForumTopicClosed,
    ForumTopicEdited as ForumTopicEdited,
    ForumTopicReopened as ForumTopicReopened,
    GeneralForumTopicHidden as GeneralForumTopicHidden,
    GeneralForumTopicUnhidden as GeneralForumTopicUnhidden,
    UserShared as UserShared,
    ChatShared as ChatShared,
    WriteAccessAllowed as WriteAccessAllowed,
    VideoChatScheduled as VideoChatScheduled,
    VideoChatStarted as VideoChatStarted,
    VideoChatEnded as VideoChatEnded,
    VideoChatParticipantsInvited as VideoChatParticipantsInvited,
    UserProfilePhotos as UserProfilePhotos,
    File as File,
    WebAppInfo as WebAppInfo,
    ReplyKeyboardMarkup as ReplyKeyboardMarkup,
    KeyboardButton as KeyboardButton,
    KeyboardButtonRequestUser as KeyboardButtonRequestUser,
    KeyboardButtonRequestChat as KeyboardButtonRequestChat,
    KeyboardButtonPollType as KeyboardButtonPollType,
    ReplyKeyboardRemove as ReplyKeyboardRemove,
    InlineKeyboardMarkup as InlineKeyboardMarkup,
    InlineKeyboardButton as InlineKeyboardButton,
    LoginUrl as LoginUrl,
    SwitchInlineQueryChosenChat as SwitchInlineQueryChosenChat,
    CallbackQuery as CallbackQuery,
    ForceReply as ForceReply,
    ChatPhoto as ChatPhoto,
    ChatInviteLink as ChatInviteLink,
    ChatAdministratorRights as ChatAdministratorRights,
    ChatMember as ChatMember,
    ChatMemberOwner as ChatMemberOwner,
    ChatMemberAdministrator as ChatMemberAdministrator,
    ChatMemberMember as ChatMemberMember,
    ChatMemberRestricted as ChatMemberRestricted,
    ChatMemberLeft as ChatMemberLeft,
    ChatMemberBanned as ChatMemberBanned,
    ChatMemberUpdated as ChatMemberUpdated,
    ChatJoinRequest as ChatJoinRequest,
    ChatPermissions as ChatPermissions,
    ChatLocation as ChatLocation,
    ForumTopic as ForumTopic,
    BotCommand as BotCommand,
    BotCommandScope as BotCommandScope,
    BotCommandScopeDefault as BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats as BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats as BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators as BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat as BotCommandScopeChat,
    BotCommandScopeChatAdministrators as BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember as BotCommandScopeChatMember,
    BotName as BotName,
    BotDescription as BotDescription,
    BotShortDescription as BotShortDescription,
    MenuButton as MenuButton,
    MenuButtonCommands as MenuButtonCommands,
    MenuButtonWebApp as MenuButtonWebApp,
    MenuButtonDefault as MenuButtonDefault,
    ResponseParameters as ResponseParameters,
    InputMedia as InputMedia,
    InputMediaPhoto as InputMediaPhoto,
    InputMediaVideo as InputMediaVideo,
    InputMediaAnimation as InputMediaAnimation,
    InputMediaAudio as InputMediaAudio,
    InputMediaDocument as InputMediaDocument,
    InputFile as InputFile,
    Sticker as Sticker,
    StickerSet as StickerSet,
    MaskPosition as MaskPosition,
    InputSticker as InputSticker,
    InlineQuery as InlineQuery,
    InlineQueryResultsButton as InlineQueryResultsButton,
    InlineQueryResult as InlineQueryResult,
    InlineQueryResultArticle as InlineQueryResultArticle,
    InlineQueryResultPhoto as InlineQueryResultPhoto,
    InlineQueryResultGif as InlineQueryResultGif,
    InlineQueryResultMpeg4Gif as InlineQueryResultMpeg4Gif,
    InlineQueryResultVideo as InlineQueryResultVideo,
    InlineQueryResultAudio as InlineQueryResultAudio,
    InlineQueryResultVoice as InlineQueryResultVoice,
    InlineQueryResultDocument as InlineQueryResultDocument,
    InlineQueryResultLocation as InlineQueryResultLocation,
    InlineQueryResultVenue as InlineQueryResultVenue,
    InlineQueryResultContact as InlineQueryResultContact,
    InlineQueryResultGame as InlineQueryResultGame,
    InlineQueryResultCachedPhoto as InlineQueryResultCachedPhoto,
    InlineQueryResultCachedGif as InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif as InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedSticker as InlineQueryResultCachedSticker,
    InlineQueryResultCachedDocument as InlineQueryResultCachedDocument,
    InlineQueryResultCachedVideo as InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice as InlineQueryResultCachedVoice,
    InlineQueryResultCachedAudio as InlineQueryResultCachedAudio,
    InputMessageContent as InputMessageContent,
    InputTextMessageContent as InputTextMessageContent,
    InputLocationMessageContent as InputLocationMessageContent,
    InputVenueMessageContent as InputVenueMessageContent,
    InputContactMessageContent as InputContactMessageContent,
    InputInvoiceMessageContent as InputInvoiceMessageContent,
    ChosenInlineResult as ChosenInlineResult,
    SentWebAppMessage as SentWebAppMessage,
    LabeledPrice as LabeledPrice,
    Invoice as Invoice,
    ShippingAddress as ShippingAddress,
    OrderInfo as OrderInfo,
    ShippingOption as ShippingOption,
    SuccessfulPayment as SuccessfulPayment,
    ShippingQuery as ShippingQuery,
    PreCheckoutQuery as PreCheckoutQuery,
    PassportData as PassportData,
    PassportFile as PassportFile,
    EncryptedPassportElement as EncryptedPassportElement,
    EncryptedCredentials as EncryptedCredentials,
    PassportElementError as PassportElementError,
    PassportElementErrorDataField as PassportElementErrorDataField,
    PassportElementErrorFrontSide as PassportElementErrorFrontSide,
    PassportElementErrorReverseSide as PassportElementErrorReverseSide,
    PassportElementErrorSelfie as PassportElementErrorSelfie,
    PassportElementErrorFile as PassportElementErrorFile,
    PassportElementErrorFiles as PassportElementErrorFiles,
    PassportElementErrorTranslationFile as PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles as PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified as PassportElementErrorUnspecified,
    Game as Game,
    CallbackGame as CallbackGame,
    GameHighScore as GameHighScore,
)