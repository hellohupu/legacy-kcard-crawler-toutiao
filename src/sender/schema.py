import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

class Constellation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AQUARIUS', 'PISCES', 'ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO', 'LIBRA', 'SCORPIO', 'SAGITTARIUS', 'CAPRICORN')


Float = sgqlc.types.Float

class Gender(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('MALE', 'FEMALE')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class ItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ARTICLE', 'VIDEO', 'LIVE')


class StatsDomain(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('FOLLOWER', 'FOLLOWING', 'ITEM')


String = sgqlc.types.String

class TimePosition(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NOW', 'LATEST')


class TimeUnit(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('YEAR', 'MONTHS', 'WEEKS', 'DAYS', 'HOURS', 'MINUTES', 'SECONDS', 'MILLISECONDS')


class UserType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('KOL', 'USER')


class _BrandOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('name_asc', 'name_desc', '_id_asc', '_id_desc')


class _CityOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('name_asc', 'name_desc', '_id_asc', '_id_desc')


class _CommentOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('content_asc', 'content_desc', 'like_asc', 'like_desc', 'timeCreated_asc', 'timeCreated_desc', 'timeUpdated_asc', 'timeUpdated_desc', '_id_asc', '_id_desc')


class _ItemOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'title_asc', 'title_desc', 'type_asc', 'type_desc', 'isBusiness_asc', 'isBusiness_desc', 'isAccepted_asc', 'isAccepted_desc', 'isCompleted_asc', 'isCompleted_desc', 'cover_asc', 'cover_desc', 'coverAnimated_asc', 'coverAnimated_desc', 'url_asc', 'url_desc', 'content_asc', 'content_desc', 'exposure_asc', 'exposure_desc', 'view_asc', 'view_desc', 'like_asc', 'like_desc', 'favorite_asc', 'favorite_desc', 'comment_asc', 'comment_desc', 'share_asc', 'share_desc', 'timeCreated_asc', 'timeCreated_desc', 'timeUpdated_asc', 'timeUpdated_desc', 'ctime_asc', 'ctime_desc', 'mtime_asc', 'mtime_desc', '_id_asc', '_id_desc')


class _McnOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('name_asc', 'name_desc', 'fullName_asc', 'fullName_desc', 'logo_asc', 'logo_desc', 'description_asc', 'description_desc', 'kolTotal_asc', 'kolTotal_desc', 'followerTotal_asc', 'followerTotal_desc', '_id_asc', '_id_desc')


class _ProvinceOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('name_asc', 'name_desc', '_id_asc', '_id_desc')


class _RelationDirections(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IN', 'OUT')


class _SourceOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'name_asc', 'name_desc', 'url_asc', 'url_desc', '_id_asc', '_id_desc')


class _StatsOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('domain_asc', 'domain_desc', 'key_asc', 'key_desc', '_id_asc', '_id_desc')


class _TagOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('name_asc', 'name_desc', 'value_asc', 'value_desc', '_id_asc', '_id_desc')


class _TimeDurationOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('length_asc', 'length_desc', 'unit_asc', 'unit_desc', '_id_asc', '_id_desc')


class _UserInfoOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('id_asc', 'id_desc', 'nickname_asc', 'nickname_desc', 'type_asc', 'type_desc', 'isPrimary_asc', 'isPrimary_desc', 'phone_asc', 'phone_desc', 'wechat_asc', 'wechat_desc', 'avatar_asc', 'avatar_desc', 'signature_asc', 'signature_desc', 'gender_asc', 'gender_desc', 'birthdate_asc', 'birthdate_desc', 'constellation_asc', 'constellation_desc', 'mcnId_asc', 'mcnId_desc', 'priceVideo_asc', 'priceVideo_desc', 'priceLongVideo_asc', 'priceLongVideo_desc', 'priceArticle_asc', 'priceArticle_desc', 'timeCreated_asc', 'timeCreated_desc', 'timeUpdated_asc', 'timeUpdated_desc', 'ctime_asc', 'ctime_desc', 'mtime_asc', 'mtime_desc', '_id_asc', '_id_desc')



########################################################################
# Input Objects
########################################################################
class CommentInput(sgqlc.types.Input):
    __schema__ = schema
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    item = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='item')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    author = sgqlc.types.Field(String, graphql_name='author')
    like = sgqlc.types.Field(Int, graphql_name='like')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')


class IntRangeInput(sgqlc.types.Input):
    __schema__ = schema
    start = sgqlc.types.Field(Int, graphql_name='start')
    end = sgqlc.types.Field(Int, graphql_name='end')


class ItemCommentInput(sgqlc.types.Input):
    __schema__ = schema
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    author = sgqlc.types.Field(String, graphql_name='author')
    like = sgqlc.types.Field(Int, graphql_name='like')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')


class ItemInput(sgqlc.types.Input):
    __schema__ = schema
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    author = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='author')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(ItemType, graphql_name='type')
    is_business = sgqlc.types.Field(Boolean, graphql_name='isBusiness')
    is_accepted = sgqlc.types.Field(Boolean, graphql_name='isAccepted')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    cover = sgqlc.types.Field(String, graphql_name='cover')
    cover_animated = sgqlc.types.Field(String, graphql_name='coverAnimated')
    url = sgqlc.types.Field(String, graphql_name='url')
    content = sgqlc.types.Field(String, graphql_name='content')
    brands = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='brands')
    comments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ItemCommentInput)), graphql_name='comments')
    exposure = sgqlc.types.Field(Int, graphql_name='exposure')
    view = sgqlc.types.Field(Int, graphql_name='view')
    like = sgqlc.types.Field(Int, graphql_name='like')
    favorite = sgqlc.types.Field(Int, graphql_name='favorite')
    comment = sgqlc.types.Field(Int, graphql_name='comment')
    share = sgqlc.types.Field(Int, graphql_name='share')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')


class McnInput(sgqlc.types.Input):
    __schema__ = schema
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    full_name = sgqlc.types.Field(String, graphql_name='fullName')
    logo = sgqlc.types.Field(String, graphql_name='logo')
    description = sgqlc.types.Field(String, graphql_name='description')
    kol_total = sgqlc.types.Field(Int, graphql_name='kolTotal')
    follower_total = sgqlc.types.Field(Int, graphql_name='followerTotal')


class SourceInput(sgqlc.types.Input):
    __schema__ = schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')


class StatsDataInput(sgqlc.types.Input):
    __schema__ = schema
    time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='time')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    age = sgqlc.types.Field(IntRangeInput, graphql_name='age')
    interest = sgqlc.types.Field(String, graphql_name='interest')
    province = sgqlc.types.Field(String, graphql_name='province')
    activity = sgqlc.types.Field(String, graphql_name='activity')
    phone_brand = sgqlc.types.Field(String, graphql_name='phoneBrand')
    item_type = sgqlc.types.Field(ItemType, graphql_name='itemType')
    is_business = sgqlc.types.Field(Boolean, graphql_name='isBusiness')
    is_accepted = sgqlc.types.Field(Boolean, graphql_name='isAccepted')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    rolling_window_time = sgqlc.types.Field(Int, graphql_name='rollingWindowTime')
    rolling_window_count = sgqlc.types.Field(Int, graphql_name='rollingWindowCount')
    percent = sgqlc.types.Field(Float, graphql_name='percent')
    count = sgqlc.types.Field(Int, graphql_name='count')
    exposure_total = sgqlc.types.Field(Int, graphql_name='exposureTotal')
    exposure_mean = sgqlc.types.Field(Int, graphql_name='exposureMean')
    view_total = sgqlc.types.Field(Int, graphql_name='viewTotal')
    view_mean = sgqlc.types.Field(Int, graphql_name='viewMean')
    like_total = sgqlc.types.Field(Int, graphql_name='likeTotal')
    like_mean = sgqlc.types.Field(Int, graphql_name='likeMean')
    favorite_total = sgqlc.types.Field(Int, graphql_name='favoriteTotal')
    favorite_mean = sgqlc.types.Field(Int, graphql_name='favoriteMean')
    comment_total = sgqlc.types.Field(Int, graphql_name='commentTotal')
    comment_mean = sgqlc.types.Field(Int, graphql_name='commentMean')
    share_total = sgqlc.types.Field(Int, graphql_name='shareTotal')
    share_mean = sgqlc.types.Field(Int, graphql_name='shareMean')
    merchant_cooperated_total = sgqlc.types.Field(Int, graphql_name='merchantCooperatedTotal')
    item_accept_time_mean = sgqlc.types.Field(Int, graphql_name='itemAcceptTimeMean')
    item_complete_time_mean = sgqlc.types.Field(Int, graphql_name='itemCompleteTimeMean')


class StatsInput(sgqlc.types.Input):
    __schema__ = schema
    domain = sgqlc.types.Field(sgqlc.types.non_null(StatsDomain), graphql_name='domain')
    user = sgqlc.types.Field(String, graphql_name='user')
    item = sgqlc.types.Field(String, graphql_name='item')
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StatsDataInput)), graphql_name='data')


class TimeDurationInput(sgqlc.types.Input):
    __schema__ = schema
    length = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='length')
    unit = sgqlc.types.Field(sgqlc.types.non_null(TimeUnit), graphql_name='unit')


class UserInfoInput(sgqlc.types.Input):
    __schema__ = schema
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    type = sgqlc.types.Field(UserType, graphql_name='type')
    is_primary = sgqlc.types.Field(Boolean, graphql_name='isPrimary')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    wechat = sgqlc.types.Field(String, graphql_name='wechat')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')
    signature = sgqlc.types.Field(String, graphql_name='signature')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    birthdate = sgqlc.types.Field(String, graphql_name='birthdate')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    constellation = sgqlc.types.Field(Constellation, graphql_name='constellation')
    mcn = sgqlc.types.Field(String, graphql_name='mcn')
    mcn_id = sgqlc.types.Field(String, graphql_name='mcnId')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    price_video = sgqlc.types.Field(Int, graphql_name='priceVideo')
    price_long_video = sgqlc.types.Field(Int, graphql_name='priceLongVideo')
    price_article = sgqlc.types.Field(Int, graphql_name='priceArticle')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')


class _BrandFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_BrandFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_BrandFilter')), graphql_name='OR')
    name = sgqlc.types.Field(ID, graphql_name='name')
    name_not = sgqlc.types.Field(ID, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(ID, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(ID, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(ID, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(ID, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(ID, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(ID, graphql_name='name_not_ends_with')


class _CityFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_CityFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_CityFilter')), graphql_name='OR')
    name = sgqlc.types.Field(ID, graphql_name='name')
    name_not = sgqlc.types.Field(ID, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(ID, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(ID, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(ID, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(ID, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(ID, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(ID, graphql_name='name_not_ends_with')
    kols = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols')
    kols_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_not')
    kols_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_in')
    kols_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_not_in')
    kols_some = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_some')
    kols_none = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_none')
    kols_single = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_single')
    kols_every = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_every')


class _CommentFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_CommentFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_CommentFilter')), graphql_name='OR')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_not = sgqlc.types.Field(String, graphql_name='content_not')
    content_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='content_in')
    content_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='content_not_in')
    content_contains = sgqlc.types.Field(String, graphql_name='content_contains')
    content_not_contains = sgqlc.types.Field(String, graphql_name='content_not_contains')
    content_starts_with = sgqlc.types.Field(String, graphql_name='content_starts_with')
    content_not_starts_with = sgqlc.types.Field(String, graphql_name='content_not_starts_with')
    content_ends_with = sgqlc.types.Field(String, graphql_name='content_ends_with')
    content_not_ends_with = sgqlc.types.Field(String, graphql_name='content_not_ends_with')
    item = sgqlc.types.Field('_ItemFilter', graphql_name='item')
    item_not = sgqlc.types.Field('_ItemFilter', graphql_name='item_not')
    item_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ItemFilter')), graphql_name='item_in')
    item_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ItemFilter')), graphql_name='item_not_in')
    author = sgqlc.types.Field('_UserInfoFilter', graphql_name='author')
    author_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='author_not')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='author_in')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='author_not_in')
    like = sgqlc.types.Field(Int, graphql_name='like')
    like_not = sgqlc.types.Field(Int, graphql_name='like_not')
    like_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='like_in')
    like_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='like_not_in')
    like_lt = sgqlc.types.Field(Int, graphql_name='like_lt')
    like_lte = sgqlc.types.Field(Int, graphql_name='like_lte')
    like_gt = sgqlc.types.Field(Int, graphql_name='like_gt')
    like_gte = sgqlc.types.Field(Int, graphql_name='like_gte')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_created_not = sgqlc.types.Field(String, graphql_name='timeCreated_not')
    time_created_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeCreated_in')
    time_created_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeCreated_not_in')
    time_created_contains = sgqlc.types.Field(String, graphql_name='timeCreated_contains')
    time_created_not_contains = sgqlc.types.Field(String, graphql_name='timeCreated_not_contains')
    time_created_starts_with = sgqlc.types.Field(String, graphql_name='timeCreated_starts_with')
    time_created_not_starts_with = sgqlc.types.Field(String, graphql_name='timeCreated_not_starts_with')
    time_created_ends_with = sgqlc.types.Field(String, graphql_name='timeCreated_ends_with')
    time_created_not_ends_with = sgqlc.types.Field(String, graphql_name='timeCreated_not_ends_with')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')
    time_updated_not = sgqlc.types.Field(String, graphql_name='timeUpdated_not')
    time_updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeUpdated_in')
    time_updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeUpdated_not_in')
    time_updated_contains = sgqlc.types.Field(String, graphql_name='timeUpdated_contains')
    time_updated_not_contains = sgqlc.types.Field(String, graphql_name='timeUpdated_not_contains')
    time_updated_starts_with = sgqlc.types.Field(String, graphql_name='timeUpdated_starts_with')
    time_updated_not_starts_with = sgqlc.types.Field(String, graphql_name='timeUpdated_not_starts_with')
    time_updated_ends_with = sgqlc.types.Field(String, graphql_name='timeUpdated_ends_with')
    time_updated_not_ends_with = sgqlc.types.Field(String, graphql_name='timeUpdated_not_ends_with')


class _ItemFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ItemFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ItemFilter')), graphql_name='OR')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    title = sgqlc.types.Field(String, graphql_name='title')
    title_not = sgqlc.types.Field(String, graphql_name='title_not')
    title_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='title_in')
    title_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='title_not_in')
    title_contains = sgqlc.types.Field(String, graphql_name='title_contains')
    title_not_contains = sgqlc.types.Field(String, graphql_name='title_not_contains')
    title_starts_with = sgqlc.types.Field(String, graphql_name='title_starts_with')
    title_not_starts_with = sgqlc.types.Field(String, graphql_name='title_not_starts_with')
    title_ends_with = sgqlc.types.Field(String, graphql_name='title_ends_with')
    title_not_ends_with = sgqlc.types.Field(String, graphql_name='title_not_ends_with')
    author = sgqlc.types.Field('_UserInfoFilter', graphql_name='author')
    author_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='author_not')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='author_in')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='author_not_in')
    type = sgqlc.types.Field(ItemType, graphql_name='type')
    type_not = sgqlc.types.Field(ItemType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ItemType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ItemType)), graphql_name='type_not_in')
    is_business = sgqlc.types.Field(Boolean, graphql_name='isBusiness')
    is_business_not = sgqlc.types.Field(Boolean, graphql_name='isBusiness_not')
    is_accepted = sgqlc.types.Field(Boolean, graphql_name='isAccepted')
    is_accepted_not = sgqlc.types.Field(Boolean, graphql_name='isAccepted_not')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    is_completed_not = sgqlc.types.Field(Boolean, graphql_name='isCompleted_not')
    cover = sgqlc.types.Field(String, graphql_name='cover')
    cover_not = sgqlc.types.Field(String, graphql_name='cover_not')
    cover_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='cover_in')
    cover_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='cover_not_in')
    cover_contains = sgqlc.types.Field(String, graphql_name='cover_contains')
    cover_not_contains = sgqlc.types.Field(String, graphql_name='cover_not_contains')
    cover_starts_with = sgqlc.types.Field(String, graphql_name='cover_starts_with')
    cover_not_starts_with = sgqlc.types.Field(String, graphql_name='cover_not_starts_with')
    cover_ends_with = sgqlc.types.Field(String, graphql_name='cover_ends_with')
    cover_not_ends_with = sgqlc.types.Field(String, graphql_name='cover_not_ends_with')
    cover_animated = sgqlc.types.Field(String, graphql_name='coverAnimated')
    cover_animated_not = sgqlc.types.Field(String, graphql_name='coverAnimated_not')
    cover_animated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='coverAnimated_in')
    cover_animated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='coverAnimated_not_in')
    cover_animated_contains = sgqlc.types.Field(String, graphql_name='coverAnimated_contains')
    cover_animated_not_contains = sgqlc.types.Field(String, graphql_name='coverAnimated_not_contains')
    cover_animated_starts_with = sgqlc.types.Field(String, graphql_name='coverAnimated_starts_with')
    cover_animated_not_starts_with = sgqlc.types.Field(String, graphql_name='coverAnimated_not_starts_with')
    cover_animated_ends_with = sgqlc.types.Field(String, graphql_name='coverAnimated_ends_with')
    cover_animated_not_ends_with = sgqlc.types.Field(String, graphql_name='coverAnimated_not_ends_with')
    url = sgqlc.types.Field(String, graphql_name='url')
    url_not = sgqlc.types.Field(String, graphql_name='url_not')
    url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='url_in')
    url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='url_not_in')
    url_contains = sgqlc.types.Field(String, graphql_name='url_contains')
    url_not_contains = sgqlc.types.Field(String, graphql_name='url_not_contains')
    url_starts_with = sgqlc.types.Field(String, graphql_name='url_starts_with')
    url_not_starts_with = sgqlc.types.Field(String, graphql_name='url_not_starts_with')
    url_ends_with = sgqlc.types.Field(String, graphql_name='url_ends_with')
    url_not_ends_with = sgqlc.types.Field(String, graphql_name='url_not_ends_with')
    content = sgqlc.types.Field(String, graphql_name='content')
    content_not = sgqlc.types.Field(String, graphql_name='content_not')
    content_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='content_in')
    content_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='content_not_in')
    content_contains = sgqlc.types.Field(String, graphql_name='content_contains')
    content_not_contains = sgqlc.types.Field(String, graphql_name='content_not_contains')
    content_starts_with = sgqlc.types.Field(String, graphql_name='content_starts_with')
    content_not_starts_with = sgqlc.types.Field(String, graphql_name='content_not_starts_with')
    content_ends_with = sgqlc.types.Field(String, graphql_name='content_ends_with')
    content_not_ends_with = sgqlc.types.Field(String, graphql_name='content_not_ends_with')
    brands = sgqlc.types.Field(_BrandFilter, graphql_name='brands')
    brands_not = sgqlc.types.Field(_BrandFilter, graphql_name='brands_not')
    brands_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BrandFilter)), graphql_name='brands_in')
    brands_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_BrandFilter)), graphql_name='brands_not_in')
    brands_some = sgqlc.types.Field(_BrandFilter, graphql_name='brands_some')
    brands_none = sgqlc.types.Field(_BrandFilter, graphql_name='brands_none')
    brands_single = sgqlc.types.Field(_BrandFilter, graphql_name='brands_single')
    brands_every = sgqlc.types.Field(_BrandFilter, graphql_name='brands_every')
    comments = sgqlc.types.Field(_CommentFilter, graphql_name='comments')
    comments_not = sgqlc.types.Field(_CommentFilter, graphql_name='comments_not')
    comments_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_CommentFilter)), graphql_name='comments_in')
    comments_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_CommentFilter)), graphql_name='comments_not_in')
    comments_some = sgqlc.types.Field(_CommentFilter, graphql_name='comments_some')
    comments_none = sgqlc.types.Field(_CommentFilter, graphql_name='comments_none')
    comments_single = sgqlc.types.Field(_CommentFilter, graphql_name='comments_single')
    comments_every = sgqlc.types.Field(_CommentFilter, graphql_name='comments_every')
    exposure = sgqlc.types.Field(Int, graphql_name='exposure')
    exposure_not = sgqlc.types.Field(Int, graphql_name='exposure_not')
    exposure_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='exposure_in')
    exposure_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='exposure_not_in')
    exposure_lt = sgqlc.types.Field(Int, graphql_name='exposure_lt')
    exposure_lte = sgqlc.types.Field(Int, graphql_name='exposure_lte')
    exposure_gt = sgqlc.types.Field(Int, graphql_name='exposure_gt')
    exposure_gte = sgqlc.types.Field(Int, graphql_name='exposure_gte')
    view = sgqlc.types.Field(Int, graphql_name='view')
    view_not = sgqlc.types.Field(Int, graphql_name='view_not')
    view_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='view_in')
    view_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='view_not_in')
    view_lt = sgqlc.types.Field(Int, graphql_name='view_lt')
    view_lte = sgqlc.types.Field(Int, graphql_name='view_lte')
    view_gt = sgqlc.types.Field(Int, graphql_name='view_gt')
    view_gte = sgqlc.types.Field(Int, graphql_name='view_gte')
    like = sgqlc.types.Field(Int, graphql_name='like')
    like_not = sgqlc.types.Field(Int, graphql_name='like_not')
    like_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='like_in')
    like_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='like_not_in')
    like_lt = sgqlc.types.Field(Int, graphql_name='like_lt')
    like_lte = sgqlc.types.Field(Int, graphql_name='like_lte')
    like_gt = sgqlc.types.Field(Int, graphql_name='like_gt')
    like_gte = sgqlc.types.Field(Int, graphql_name='like_gte')
    favorite = sgqlc.types.Field(Int, graphql_name='favorite')
    favorite_not = sgqlc.types.Field(Int, graphql_name='favorite_not')
    favorite_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='favorite_in')
    favorite_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='favorite_not_in')
    favorite_lt = sgqlc.types.Field(Int, graphql_name='favorite_lt')
    favorite_lte = sgqlc.types.Field(Int, graphql_name='favorite_lte')
    favorite_gt = sgqlc.types.Field(Int, graphql_name='favorite_gt')
    favorite_gte = sgqlc.types.Field(Int, graphql_name='favorite_gte')
    comment = sgqlc.types.Field(Int, graphql_name='comment')
    comment_not = sgqlc.types.Field(Int, graphql_name='comment_not')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='comment_in')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='comment_not_in')
    comment_lt = sgqlc.types.Field(Int, graphql_name='comment_lt')
    comment_lte = sgqlc.types.Field(Int, graphql_name='comment_lte')
    comment_gt = sgqlc.types.Field(Int, graphql_name='comment_gt')
    comment_gte = sgqlc.types.Field(Int, graphql_name='comment_gte')
    share = sgqlc.types.Field(Int, graphql_name='share')
    share_not = sgqlc.types.Field(Int, graphql_name='share_not')
    share_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='share_in')
    share_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='share_not_in')
    share_lt = sgqlc.types.Field(Int, graphql_name='share_lt')
    share_lte = sgqlc.types.Field(Int, graphql_name='share_lte')
    share_gt = sgqlc.types.Field(Int, graphql_name='share_gt')
    share_gte = sgqlc.types.Field(Int, graphql_name='share_gte')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_created_not = sgqlc.types.Field(String, graphql_name='timeCreated_not')
    time_created_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeCreated_in')
    time_created_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeCreated_not_in')
    time_created_contains = sgqlc.types.Field(String, graphql_name='timeCreated_contains')
    time_created_not_contains = sgqlc.types.Field(String, graphql_name='timeCreated_not_contains')
    time_created_starts_with = sgqlc.types.Field(String, graphql_name='timeCreated_starts_with')
    time_created_not_starts_with = sgqlc.types.Field(String, graphql_name='timeCreated_not_starts_with')
    time_created_ends_with = sgqlc.types.Field(String, graphql_name='timeCreated_ends_with')
    time_created_not_ends_with = sgqlc.types.Field(String, graphql_name='timeCreated_not_ends_with')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')
    time_updated_not = sgqlc.types.Field(String, graphql_name='timeUpdated_not')
    time_updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeUpdated_in')
    time_updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeUpdated_not_in')
    time_updated_contains = sgqlc.types.Field(String, graphql_name='timeUpdated_contains')
    time_updated_not_contains = sgqlc.types.Field(String, graphql_name='timeUpdated_not_contains')
    time_updated_starts_with = sgqlc.types.Field(String, graphql_name='timeUpdated_starts_with')
    time_updated_not_starts_with = sgqlc.types.Field(String, graphql_name='timeUpdated_not_starts_with')
    time_updated_ends_with = sgqlc.types.Field(String, graphql_name='timeUpdated_ends_with')
    time_updated_not_ends_with = sgqlc.types.Field(String, graphql_name='timeUpdated_not_ends_with')
    ctime = sgqlc.types.Field(String, graphql_name='ctime')
    ctime_not = sgqlc.types.Field(String, graphql_name='ctime_not')
    ctime_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ctime_in')
    ctime_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ctime_not_in')
    ctime_contains = sgqlc.types.Field(String, graphql_name='ctime_contains')
    ctime_not_contains = sgqlc.types.Field(String, graphql_name='ctime_not_contains')
    ctime_starts_with = sgqlc.types.Field(String, graphql_name='ctime_starts_with')
    ctime_not_starts_with = sgqlc.types.Field(String, graphql_name='ctime_not_starts_with')
    ctime_ends_with = sgqlc.types.Field(String, graphql_name='ctime_ends_with')
    ctime_not_ends_with = sgqlc.types.Field(String, graphql_name='ctime_not_ends_with')
    mtime = sgqlc.types.Field(String, graphql_name='mtime')
    mtime_not = sgqlc.types.Field(String, graphql_name='mtime_not')
    mtime_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mtime_in')
    mtime_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mtime_not_in')
    mtime_contains = sgqlc.types.Field(String, graphql_name='mtime_contains')
    mtime_not_contains = sgqlc.types.Field(String, graphql_name='mtime_not_contains')
    mtime_starts_with = sgqlc.types.Field(String, graphql_name='mtime_starts_with')
    mtime_not_starts_with = sgqlc.types.Field(String, graphql_name='mtime_not_starts_with')
    mtime_ends_with = sgqlc.types.Field(String, graphql_name='mtime_ends_with')
    mtime_not_ends_with = sgqlc.types.Field(String, graphql_name='mtime_not_ends_with')
    stats = sgqlc.types.Field('_StatsFilter', graphql_name='stats')
    stats_not = sgqlc.types.Field('_StatsFilter', graphql_name='stats_not')
    stats_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_StatsFilter')), graphql_name='stats_in')
    stats_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_StatsFilter')), graphql_name='stats_not_in')


class _McnFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_McnFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_McnFilter')), graphql_name='OR')
    name = sgqlc.types.Field(ID, graphql_name='name')
    name_not = sgqlc.types.Field(ID, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(ID, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(ID, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(ID, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(ID, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(ID, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(ID, graphql_name='name_not_ends_with')
    full_name = sgqlc.types.Field(String, graphql_name='fullName')
    full_name_not = sgqlc.types.Field(String, graphql_name='fullName_not')
    full_name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fullName_in')
    full_name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fullName_not_in')
    full_name_contains = sgqlc.types.Field(String, graphql_name='fullName_contains')
    full_name_not_contains = sgqlc.types.Field(String, graphql_name='fullName_not_contains')
    full_name_starts_with = sgqlc.types.Field(String, graphql_name='fullName_starts_with')
    full_name_not_starts_with = sgqlc.types.Field(String, graphql_name='fullName_not_starts_with')
    full_name_ends_with = sgqlc.types.Field(String, graphql_name='fullName_ends_with')
    full_name_not_ends_with = sgqlc.types.Field(String, graphql_name='fullName_not_ends_with')
    logo = sgqlc.types.Field(String, graphql_name='logo')
    logo_not = sgqlc.types.Field(String, graphql_name='logo_not')
    logo_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='logo_in')
    logo_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='logo_not_in')
    logo_contains = sgqlc.types.Field(String, graphql_name='logo_contains')
    logo_not_contains = sgqlc.types.Field(String, graphql_name='logo_not_contains')
    logo_starts_with = sgqlc.types.Field(String, graphql_name='logo_starts_with')
    logo_not_starts_with = sgqlc.types.Field(String, graphql_name='logo_not_starts_with')
    logo_ends_with = sgqlc.types.Field(String, graphql_name='logo_ends_with')
    logo_not_ends_with = sgqlc.types.Field(String, graphql_name='logo_not_ends_with')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_not = sgqlc.types.Field(String, graphql_name='description_not')
    description_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='description_in')
    description_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='description_not_in')
    description_contains = sgqlc.types.Field(String, graphql_name='description_contains')
    description_not_contains = sgqlc.types.Field(String, graphql_name='description_not_contains')
    description_starts_with = sgqlc.types.Field(String, graphql_name='description_starts_with')
    description_not_starts_with = sgqlc.types.Field(String, graphql_name='description_not_starts_with')
    description_ends_with = sgqlc.types.Field(String, graphql_name='description_ends_with')
    description_not_ends_with = sgqlc.types.Field(String, graphql_name='description_not_ends_with')
    kol_total = sgqlc.types.Field(Int, graphql_name='kolTotal')
    kol_total_not = sgqlc.types.Field(Int, graphql_name='kolTotal_not')
    kol_total_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='kolTotal_in')
    kol_total_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='kolTotal_not_in')
    kol_total_lt = sgqlc.types.Field(Int, graphql_name='kolTotal_lt')
    kol_total_lte = sgqlc.types.Field(Int, graphql_name='kolTotal_lte')
    kol_total_gt = sgqlc.types.Field(Int, graphql_name='kolTotal_gt')
    kol_total_gte = sgqlc.types.Field(Int, graphql_name='kolTotal_gte')
    follower_total = sgqlc.types.Field(Int, graphql_name='followerTotal')
    follower_total_not = sgqlc.types.Field(Int, graphql_name='followerTotal_not')
    follower_total_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='followerTotal_in')
    follower_total_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='followerTotal_not_in')
    follower_total_lt = sgqlc.types.Field(Int, graphql_name='followerTotal_lt')
    follower_total_lte = sgqlc.types.Field(Int, graphql_name='followerTotal_lte')
    follower_total_gt = sgqlc.types.Field(Int, graphql_name='followerTotal_gt')
    follower_total_gte = sgqlc.types.Field(Int, graphql_name='followerTotal_gte')
    kols = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols')
    kols_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_not')
    kols_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_in')
    kols_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_not_in')
    kols_some = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_some')
    kols_none = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_none')
    kols_single = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_single')
    kols_every = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_every')


class _Neo4jDateInput(sgqlc.types.Input):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jDateTimeInput(sgqlc.types.Input):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalDateTimeInput(sgqlc.types.Input):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalTimeInput(sgqlc.types.Input):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jTimeInput(sgqlc.types.Input):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _ProvinceFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ProvinceFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_ProvinceFilter')), graphql_name='OR')
    name = sgqlc.types.Field(ID, graphql_name='name')
    name_not = sgqlc.types.Field(ID, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(ID, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(ID, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(ID, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(ID, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(ID, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(ID, graphql_name='name_not_ends_with')
    kols = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols')
    kols_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_not')
    kols_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_in')
    kols_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_not_in')
    kols_some = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_some')
    kols_none = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_none')
    kols_single = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_single')
    kols_every = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_every')


class _SourceFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SourceFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SourceFilter')), graphql_name='OR')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(ID, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(ID, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(ID, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(ID, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(ID, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(ID, graphql_name='id_not_ends_with')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    url = sgqlc.types.Field(String, graphql_name='url')
    url_not = sgqlc.types.Field(String, graphql_name='url_not')
    url_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='url_in')
    url_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='url_not_in')
    url_contains = sgqlc.types.Field(String, graphql_name='url_contains')
    url_not_contains = sgqlc.types.Field(String, graphql_name='url_not_contains')
    url_starts_with = sgqlc.types.Field(String, graphql_name='url_starts_with')
    url_not_starts_with = sgqlc.types.Field(String, graphql_name='url_not_starts_with')
    url_ends_with = sgqlc.types.Field(String, graphql_name='url_ends_with')
    url_not_ends_with = sgqlc.types.Field(String, graphql_name='url_not_ends_with')
    kols = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols')
    kols_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_not')
    kols_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_in')
    kols_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_not_in')
    kols_some = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_some')
    kols_none = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_none')
    kols_single = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_single')
    kols_every = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_every')


class _StatsFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_StatsFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_StatsFilter')), graphql_name='OR')
    domain = sgqlc.types.Field(StatsDomain, graphql_name='domain')
    domain_not = sgqlc.types.Field(StatsDomain, graphql_name='domain_not')
    domain_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StatsDomain)), graphql_name='domain_in')
    domain_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StatsDomain)), graphql_name='domain_not_in')
    user = sgqlc.types.Field('_UserInfoFilter', graphql_name='user')
    user_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='user_not')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='user_not_in')
    item = sgqlc.types.Field(_ItemFilter, graphql_name='item')
    item_not = sgqlc.types.Field(_ItemFilter, graphql_name='item_not')
    item_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ItemFilter)), graphql_name='item_in')
    item_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ItemFilter)), graphql_name='item_not_in')
    key = sgqlc.types.Field(String, graphql_name='key')
    key_not = sgqlc.types.Field(String, graphql_name='key_not')
    key_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='key_in')
    key_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='key_not_in')
    key_contains = sgqlc.types.Field(String, graphql_name='key_contains')
    key_not_contains = sgqlc.types.Field(String, graphql_name='key_not_contains')
    key_starts_with = sgqlc.types.Field(String, graphql_name='key_starts_with')
    key_not_starts_with = sgqlc.types.Field(String, graphql_name='key_not_starts_with')
    key_ends_with = sgqlc.types.Field(String, graphql_name='key_ends_with')
    key_not_ends_with = sgqlc.types.Field(String, graphql_name='key_not_ends_with')


class _TagFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TagFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TagFilter')), graphql_name='OR')
    name = sgqlc.types.Field(ID, graphql_name='name')
    name_not = sgqlc.types.Field(ID, graphql_name='name_not')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(ID, graphql_name='name_contains')
    name_not_contains = sgqlc.types.Field(ID, graphql_name='name_not_contains')
    name_starts_with = sgqlc.types.Field(ID, graphql_name='name_starts_with')
    name_not_starts_with = sgqlc.types.Field(ID, graphql_name='name_not_starts_with')
    name_ends_with = sgqlc.types.Field(ID, graphql_name='name_ends_with')
    name_not_ends_with = sgqlc.types.Field(ID, graphql_name='name_not_ends_with')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_not = sgqlc.types.Field(String, graphql_name='value_not')
    value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='value_in')
    value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='value_not_in')
    value_contains = sgqlc.types.Field(String, graphql_name='value_contains')
    value_not_contains = sgqlc.types.Field(String, graphql_name='value_not_contains')
    value_starts_with = sgqlc.types.Field(String, graphql_name='value_starts_with')
    value_not_starts_with = sgqlc.types.Field(String, graphql_name='value_not_starts_with')
    value_ends_with = sgqlc.types.Field(String, graphql_name='value_ends_with')
    value_not_ends_with = sgqlc.types.Field(String, graphql_name='value_not_ends_with')
    kols = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols')
    kols_not = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_not')
    kols_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_in')
    kols_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='kols_not_in')
    kols_some = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_some')
    kols_none = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_none')
    kols_single = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_single')
    kols_every = sgqlc.types.Field('_UserInfoFilter', graphql_name='kols_every')


class _TimeDurationFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimeDurationFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_TimeDurationFilter')), graphql_name='OR')
    length = sgqlc.types.Field(Float, graphql_name='length')
    length_not = sgqlc.types.Field(Float, graphql_name='length_not')
    length_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='length_in')
    length_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Float)), graphql_name='length_not_in')
    length_lt = sgqlc.types.Field(Float, graphql_name='length_lt')
    length_lte = sgqlc.types.Field(Float, graphql_name='length_lte')
    length_gt = sgqlc.types.Field(Float, graphql_name='length_gt')
    length_gte = sgqlc.types.Field(Float, graphql_name='length_gte')
    unit = sgqlc.types.Field(TimeUnit, graphql_name='unit')
    unit_not = sgqlc.types.Field(TimeUnit, graphql_name='unit_not')
    unit_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TimeUnit)), graphql_name='unit_in')
    unit_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TimeUnit)), graphql_name='unit_not_in')


class _UserInfoFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_UserInfoFilter')), graphql_name='OR')
    source = sgqlc.types.Field(_SourceFilter, graphql_name='source')
    source_not = sgqlc.types.Field(_SourceFilter, graphql_name='source_not')
    source_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SourceFilter)), graphql_name='source_in')
    source_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SourceFilter)), graphql_name='source_not_in')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    nickname_not = sgqlc.types.Field(String, graphql_name='nickname_not')
    nickname_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nickname_in')
    nickname_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='nickname_not_in')
    nickname_contains = sgqlc.types.Field(String, graphql_name='nickname_contains')
    nickname_not_contains = sgqlc.types.Field(String, graphql_name='nickname_not_contains')
    nickname_starts_with = sgqlc.types.Field(String, graphql_name='nickname_starts_with')
    nickname_not_starts_with = sgqlc.types.Field(String, graphql_name='nickname_not_starts_with')
    nickname_ends_with = sgqlc.types.Field(String, graphql_name='nickname_ends_with')
    nickname_not_ends_with = sgqlc.types.Field(String, graphql_name='nickname_not_ends_with')
    type = sgqlc.types.Field(UserType, graphql_name='type')
    type_not = sgqlc.types.Field(UserType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserType)), graphql_name='type_not_in')
    is_primary = sgqlc.types.Field(Boolean, graphql_name='isPrimary')
    is_primary_not = sgqlc.types.Field(Boolean, graphql_name='isPrimary_not')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    phone_not = sgqlc.types.Field(String, graphql_name='phone_not')
    phone_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='phone_in')
    phone_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='phone_not_in')
    phone_contains = sgqlc.types.Field(String, graphql_name='phone_contains')
    phone_not_contains = sgqlc.types.Field(String, graphql_name='phone_not_contains')
    phone_starts_with = sgqlc.types.Field(String, graphql_name='phone_starts_with')
    phone_not_starts_with = sgqlc.types.Field(String, graphql_name='phone_not_starts_with')
    phone_ends_with = sgqlc.types.Field(String, graphql_name='phone_ends_with')
    phone_not_ends_with = sgqlc.types.Field(String, graphql_name='phone_not_ends_with')
    wechat = sgqlc.types.Field(String, graphql_name='wechat')
    wechat_not = sgqlc.types.Field(String, graphql_name='wechat_not')
    wechat_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='wechat_in')
    wechat_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='wechat_not_in')
    wechat_contains = sgqlc.types.Field(String, graphql_name='wechat_contains')
    wechat_not_contains = sgqlc.types.Field(String, graphql_name='wechat_not_contains')
    wechat_starts_with = sgqlc.types.Field(String, graphql_name='wechat_starts_with')
    wechat_not_starts_with = sgqlc.types.Field(String, graphql_name='wechat_not_starts_with')
    wechat_ends_with = sgqlc.types.Field(String, graphql_name='wechat_ends_with')
    wechat_not_ends_with = sgqlc.types.Field(String, graphql_name='wechat_not_ends_with')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')
    avatar_not = sgqlc.types.Field(String, graphql_name='avatar_not')
    avatar_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='avatar_in')
    avatar_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='avatar_not_in')
    avatar_contains = sgqlc.types.Field(String, graphql_name='avatar_contains')
    avatar_not_contains = sgqlc.types.Field(String, graphql_name='avatar_not_contains')
    avatar_starts_with = sgqlc.types.Field(String, graphql_name='avatar_starts_with')
    avatar_not_starts_with = sgqlc.types.Field(String, graphql_name='avatar_not_starts_with')
    avatar_ends_with = sgqlc.types.Field(String, graphql_name='avatar_ends_with')
    avatar_not_ends_with = sgqlc.types.Field(String, graphql_name='avatar_not_ends_with')
    signature = sgqlc.types.Field(String, graphql_name='signature')
    signature_not = sgqlc.types.Field(String, graphql_name='signature_not')
    signature_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='signature_in')
    signature_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='signature_not_in')
    signature_contains = sgqlc.types.Field(String, graphql_name='signature_contains')
    signature_not_contains = sgqlc.types.Field(String, graphql_name='signature_not_contains')
    signature_starts_with = sgqlc.types.Field(String, graphql_name='signature_starts_with')
    signature_not_starts_with = sgqlc.types.Field(String, graphql_name='signature_not_starts_with')
    signature_ends_with = sgqlc.types.Field(String, graphql_name='signature_ends_with')
    signature_not_ends_with = sgqlc.types.Field(String, graphql_name='signature_not_ends_with')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    gender_not = sgqlc.types.Field(Gender, graphql_name='gender_not')
    gender_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Gender)), graphql_name='gender_in')
    gender_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Gender)), graphql_name='gender_not_in')
    birthdate = sgqlc.types.Field(String, graphql_name='birthdate')
    birthdate_not = sgqlc.types.Field(String, graphql_name='birthdate_not')
    birthdate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='birthdate_in')
    birthdate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='birthdate_not_in')
    birthdate_contains = sgqlc.types.Field(String, graphql_name='birthdate_contains')
    birthdate_not_contains = sgqlc.types.Field(String, graphql_name='birthdate_not_contains')
    birthdate_starts_with = sgqlc.types.Field(String, graphql_name='birthdate_starts_with')
    birthdate_not_starts_with = sgqlc.types.Field(String, graphql_name='birthdate_not_starts_with')
    birthdate_ends_with = sgqlc.types.Field(String, graphql_name='birthdate_ends_with')
    birthdate_not_ends_with = sgqlc.types.Field(String, graphql_name='birthdate_not_ends_with')
    province = sgqlc.types.Field(_ProvinceFilter, graphql_name='province')
    province_not = sgqlc.types.Field(_ProvinceFilter, graphql_name='province_not')
    province_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ProvinceFilter)), graphql_name='province_in')
    province_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ProvinceFilter)), graphql_name='province_not_in')
    city = sgqlc.types.Field(_CityFilter, graphql_name='city')
    city_not = sgqlc.types.Field(_CityFilter, graphql_name='city_not')
    city_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_CityFilter)), graphql_name='city_in')
    city_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_CityFilter)), graphql_name='city_not_in')
    constellation = sgqlc.types.Field(Constellation, graphql_name='constellation')
    constellation_not = sgqlc.types.Field(Constellation, graphql_name='constellation_not')
    constellation_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Constellation)), graphql_name='constellation_in')
    constellation_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Constellation)), graphql_name='constellation_not_in')
    mcn = sgqlc.types.Field(_McnFilter, graphql_name='mcn')
    mcn_not = sgqlc.types.Field(_McnFilter, graphql_name='mcn_not')
    mcn_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_McnFilter)), graphql_name='mcn_in')
    mcn_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_McnFilter)), graphql_name='mcn_not_in')
    items = sgqlc.types.Field(_ItemFilter, graphql_name='items')
    items_not = sgqlc.types.Field(_ItemFilter, graphql_name='items_not')
    items_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ItemFilter)), graphql_name='items_in')
    items_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_ItemFilter)), graphql_name='items_not_in')
    items_some = sgqlc.types.Field(_ItemFilter, graphql_name='items_some')
    items_none = sgqlc.types.Field(_ItemFilter, graphql_name='items_none')
    items_single = sgqlc.types.Field(_ItemFilter, graphql_name='items_single')
    items_every = sgqlc.types.Field(_ItemFilter, graphql_name='items_every')
    price_video = sgqlc.types.Field(Int, graphql_name='priceVideo')
    price_video_not = sgqlc.types.Field(Int, graphql_name='priceVideo_not')
    price_video_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='priceVideo_in')
    price_video_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='priceVideo_not_in')
    price_video_lt = sgqlc.types.Field(Int, graphql_name='priceVideo_lt')
    price_video_lte = sgqlc.types.Field(Int, graphql_name='priceVideo_lte')
    price_video_gt = sgqlc.types.Field(Int, graphql_name='priceVideo_gt')
    price_video_gte = sgqlc.types.Field(Int, graphql_name='priceVideo_gte')
    price_long_video = sgqlc.types.Field(Int, graphql_name='priceLongVideo')
    price_long_video_not = sgqlc.types.Field(Int, graphql_name='priceLongVideo_not')
    price_long_video_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='priceLongVideo_in')
    price_long_video_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='priceLongVideo_not_in')
    price_long_video_lt = sgqlc.types.Field(Int, graphql_name='priceLongVideo_lt')
    price_long_video_lte = sgqlc.types.Field(Int, graphql_name='priceLongVideo_lte')
    price_long_video_gt = sgqlc.types.Field(Int, graphql_name='priceLongVideo_gt')
    price_long_video_gte = sgqlc.types.Field(Int, graphql_name='priceLongVideo_gte')
    price_article = sgqlc.types.Field(Int, graphql_name='priceArticle')
    price_article_not = sgqlc.types.Field(Int, graphql_name='priceArticle_not')
    price_article_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='priceArticle_in')
    price_article_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='priceArticle_not_in')
    price_article_lt = sgqlc.types.Field(Int, graphql_name='priceArticle_lt')
    price_article_lte = sgqlc.types.Field(Int, graphql_name='priceArticle_lte')
    price_article_gt = sgqlc.types.Field(Int, graphql_name='priceArticle_gt')
    price_article_gte = sgqlc.types.Field(Int, graphql_name='priceArticle_gte')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_created_not = sgqlc.types.Field(String, graphql_name='timeCreated_not')
    time_created_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeCreated_in')
    time_created_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeCreated_not_in')
    time_created_contains = sgqlc.types.Field(String, graphql_name='timeCreated_contains')
    time_created_not_contains = sgqlc.types.Field(String, graphql_name='timeCreated_not_contains')
    time_created_starts_with = sgqlc.types.Field(String, graphql_name='timeCreated_starts_with')
    time_created_not_starts_with = sgqlc.types.Field(String, graphql_name='timeCreated_not_starts_with')
    time_created_ends_with = sgqlc.types.Field(String, graphql_name='timeCreated_ends_with')
    time_created_not_ends_with = sgqlc.types.Field(String, graphql_name='timeCreated_not_ends_with')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')
    time_updated_not = sgqlc.types.Field(String, graphql_name='timeUpdated_not')
    time_updated_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeUpdated_in')
    time_updated_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='timeUpdated_not_in')
    time_updated_contains = sgqlc.types.Field(String, graphql_name='timeUpdated_contains')
    time_updated_not_contains = sgqlc.types.Field(String, graphql_name='timeUpdated_not_contains')
    time_updated_starts_with = sgqlc.types.Field(String, graphql_name='timeUpdated_starts_with')
    time_updated_not_starts_with = sgqlc.types.Field(String, graphql_name='timeUpdated_not_starts_with')
    time_updated_ends_with = sgqlc.types.Field(String, graphql_name='timeUpdated_ends_with')
    time_updated_not_ends_with = sgqlc.types.Field(String, graphql_name='timeUpdated_not_ends_with')
    ctime = sgqlc.types.Field(String, graphql_name='ctime')
    ctime_not = sgqlc.types.Field(String, graphql_name='ctime_not')
    ctime_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ctime_in')
    ctime_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ctime_not_in')
    ctime_contains = sgqlc.types.Field(String, graphql_name='ctime_contains')
    ctime_not_contains = sgqlc.types.Field(String, graphql_name='ctime_not_contains')
    ctime_starts_with = sgqlc.types.Field(String, graphql_name='ctime_starts_with')
    ctime_not_starts_with = sgqlc.types.Field(String, graphql_name='ctime_not_starts_with')
    ctime_ends_with = sgqlc.types.Field(String, graphql_name='ctime_ends_with')
    ctime_not_ends_with = sgqlc.types.Field(String, graphql_name='ctime_not_ends_with')
    mtime = sgqlc.types.Field(String, graphql_name='mtime')
    mtime_not = sgqlc.types.Field(String, graphql_name='mtime_not')
    mtime_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mtime_in')
    mtime_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mtime_not_in')
    mtime_contains = sgqlc.types.Field(String, graphql_name='mtime_contains')
    mtime_not_contains = sgqlc.types.Field(String, graphql_name='mtime_not_contains')
    mtime_starts_with = sgqlc.types.Field(String, graphql_name='mtime_starts_with')
    mtime_not_starts_with = sgqlc.types.Field(String, graphql_name='mtime_not_starts_with')
    mtime_ends_with = sgqlc.types.Field(String, graphql_name='mtime_ends_with')
    mtime_not_ends_with = sgqlc.types.Field(String, graphql_name='mtime_not_ends_with')
    stats = sgqlc.types.Field(_StatsFilter, graphql_name='stats')
    stats_not = sgqlc.types.Field(_StatsFilter, graphql_name='stats_not')
    stats_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_StatsFilter)), graphql_name='stats_in')
    stats_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_StatsFilter)), graphql_name='stats_not_in')
    stats_some = sgqlc.types.Field(_StatsFilter, graphql_name='stats_some')
    stats_none = sgqlc.types.Field(_StatsFilter, graphql_name='stats_none')
    stats_single = sgqlc.types.Field(_StatsFilter, graphql_name='stats_single')
    stats_every = sgqlc.types.Field(_StatsFilter, graphql_name='stats_every')



########################################################################
# Output Objects and Interfaces
########################################################################
class Brand(sgqlc.types.Type):
    __schema__ = schema
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class City(sgqlc.types.Type):
    __schema__ = schema
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    kols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInfo'))), graphql_name='kols', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UserInfoOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Comment(sgqlc.types.Type):
    __schema__ = schema
    content = sgqlc.types.Field(String, graphql_name='content')
    item = sgqlc.types.Field('Item', graphql_name='item', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_ItemFilter, graphql_name='filter', default=None)),
))
    )
    author = sgqlc.types.Field('UserInfo', graphql_name='author', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    like = sgqlc.types.Field(Int, graphql_name='like')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class IntRange(sgqlc.types.Type):
    __schema__ = schema
    start = sgqlc.types.Field(Int, graphql_name='start')
    end = sgqlc.types.Field(Int, graphql_name='end')


class Item(sgqlc.types.Type):
    __schema__ = schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    author = sgqlc.types.Field('UserInfo', graphql_name='author', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    type = sgqlc.types.Field(ItemType, graphql_name='type')
    is_business = sgqlc.types.Field(Boolean, graphql_name='isBusiness')
    is_accepted = sgqlc.types.Field(Boolean, graphql_name='isAccepted')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    cover = sgqlc.types.Field(String, graphql_name='cover')
    cover_animated = sgqlc.types.Field(String, graphql_name='coverAnimated')
    url = sgqlc.types.Field(String, graphql_name='url')
    content = sgqlc.types.Field(String, graphql_name='content')
    brands = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Brand))), graphql_name='brands', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BrandOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BrandFilter, graphql_name='filter', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Comment))), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_CommentOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_CommentFilter, graphql_name='filter', default=None)),
))
    )
    exposure = sgqlc.types.Field(Int, graphql_name='exposure')
    view = sgqlc.types.Field(Int, graphql_name='view')
    like = sgqlc.types.Field(Int, graphql_name='like')
    favorite = sgqlc.types.Field(Int, graphql_name='favorite')
    comment = sgqlc.types.Field(Int, graphql_name='comment')
    share = sgqlc.types.Field(Int, graphql_name='share')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')
    ctime = sgqlc.types.Field(String, graphql_name='ctime')
    mtime = sgqlc.types.Field(String, graphql_name='mtime')
    stats = sgqlc.types.Field('Stats', graphql_name='stats', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_StatsFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Mcn(sgqlc.types.Type):
    __schema__ = schema
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    full_name = sgqlc.types.Field(String, graphql_name='fullName')
    logo = sgqlc.types.Field(String, graphql_name='logo')
    description = sgqlc.types.Field(String, graphql_name='description')
    kol_total = sgqlc.types.Field(Int, graphql_name='kolTotal')
    follower_total = sgqlc.types.Field(Int, graphql_name='followerTotal')
    kols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInfo'))), graphql_name='kols', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UserInfoOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    update_user_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateResult'))), graphql_name='UpdateUserInfo', args=sgqlc.types.ArgDict((
        ('inputs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserInfoInput))), graphql_name='inputs', default=None)),
))
    )
    update_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateResult'))), graphql_name='UpdateItem', args=sgqlc.types.ArgDict((
        ('inputs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ItemInput))), graphql_name='inputs', default=None)),
))
    )
    update_comment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateResult'))), graphql_name='UpdateComment', args=sgqlc.types.ArgDict((
        ('inputs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentInput))), graphql_name='inputs', default=None)),
))
    )
    update_source = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateResult'))), graphql_name='UpdateSource', args=sgqlc.types.ArgDict((
        ('inputs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SourceInput))), graphql_name='inputs', default=None)),
))
    )
    update_mcn = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateResult'))), graphql_name='UpdateMcn', args=sgqlc.types.ArgDict((
        ('inputs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(McnInput))), graphql_name='inputs', default=None)),
))
    )
    update_stats = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UpdateResult'))), graphql_name='UpdateStats', args=sgqlc.types.ArgDict((
        ('inputs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StatsInput))), graphql_name='inputs', default=None)),
))
    )


class Province(sgqlc.types.Type):
    __schema__ = schema
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    kols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInfo'))), graphql_name='kols', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UserInfoOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Query(sgqlc.types.Type):
    __schema__ = schema
    user_info = sgqlc.types.Field(sgqlc.types.list_of('UserInfo'), graphql_name='UserInfo', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('nickname', sgqlc.types.Arg(String, graphql_name='nickname', default=None)),
        ('type', sgqlc.types.Arg(UserType, graphql_name='type', default=None)),
        ('is_primary', sgqlc.types.Arg(Boolean, graphql_name='isPrimary', default=None)),
        ('phone', sgqlc.types.Arg(String, graphql_name='phone', default=None)),
        ('wechat', sgqlc.types.Arg(String, graphql_name='wechat', default=None)),
        ('avatar', sgqlc.types.Arg(String, graphql_name='avatar', default=None)),
        ('signature', sgqlc.types.Arg(String, graphql_name='signature', default=None)),
        ('gender', sgqlc.types.Arg(Gender, graphql_name='gender', default=None)),
        ('birthdate', sgqlc.types.Arg(String, graphql_name='birthdate', default=None)),
        ('constellation', sgqlc.types.Arg(Constellation, graphql_name='constellation', default=None)),
        ('mcn_id', sgqlc.types.Arg(String, graphql_name='mcnId', default=None)),
        ('tags', sgqlc.types.Arg(String, graphql_name='tags', default=None)),
        ('price_video', sgqlc.types.Arg(Int, graphql_name='priceVideo', default=None)),
        ('price_long_video', sgqlc.types.Arg(Int, graphql_name='priceLongVideo', default=None)),
        ('price_article', sgqlc.types.Arg(Int, graphql_name='priceArticle', default=None)),
        ('time_created', sgqlc.types.Arg(String, graphql_name='timeCreated', default=None)),
        ('time_updated', sgqlc.types.Arg(String, graphql_name='timeUpdated', default=None)),
        ('ctime', sgqlc.types.Arg(String, graphql_name='ctime', default=None)),
        ('mtime', sgqlc.types.Arg(String, graphql_name='mtime', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UserInfoOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    source = sgqlc.types.Field(sgqlc.types.list_of('Source'), graphql_name='Source', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SourceOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SourceFilter, graphql_name='filter', default=None)),
))
    )
    province = sgqlc.types.Field(sgqlc.types.list_of(Province), graphql_name='Province', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(ID, graphql_name='name', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ProvinceOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ProvinceFilter, graphql_name='filter', default=None)),
))
    )
    city = sgqlc.types.Field(sgqlc.types.list_of(City), graphql_name='City', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(ID, graphql_name='name', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_CityOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_CityFilter, graphql_name='filter', default=None)),
))
    )
    tag = sgqlc.types.Field(sgqlc.types.list_of('Tag'), graphql_name='Tag', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(ID, graphql_name='name', default=None)),
        ('value', sgqlc.types.Arg(String, graphql_name='value', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TagOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TagFilter, graphql_name='filter', default=None)),
))
    )
    mcn = sgqlc.types.Field(sgqlc.types.list_of(Mcn), graphql_name='Mcn', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(ID, graphql_name='name', default=None)),
        ('full_name', sgqlc.types.Arg(String, graphql_name='fullName', default=None)),
        ('logo', sgqlc.types.Arg(String, graphql_name='logo', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('kol_total', sgqlc.types.Arg(Int, graphql_name='kolTotal', default=None)),
        ('follower_total', sgqlc.types.Arg(Int, graphql_name='followerTotal', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_McnOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_McnFilter, graphql_name='filter', default=None)),
))
    )
    item = sgqlc.types.Field(sgqlc.types.list_of(Item), graphql_name='Item', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(String, graphql_name='id', default=None)),
        ('title', sgqlc.types.Arg(String, graphql_name='title', default=None)),
        ('type', sgqlc.types.Arg(ItemType, graphql_name='type', default=None)),
        ('is_business', sgqlc.types.Arg(Boolean, graphql_name='isBusiness', default=None)),
        ('is_accepted', sgqlc.types.Arg(Boolean, graphql_name='isAccepted', default=None)),
        ('is_completed', sgqlc.types.Arg(Boolean, graphql_name='isCompleted', default=None)),
        ('cover', sgqlc.types.Arg(String, graphql_name='cover', default=None)),
        ('cover_animated', sgqlc.types.Arg(String, graphql_name='coverAnimated', default=None)),
        ('url', sgqlc.types.Arg(String, graphql_name='url', default=None)),
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('exposure', sgqlc.types.Arg(Int, graphql_name='exposure', default=None)),
        ('view', sgqlc.types.Arg(Int, graphql_name='view', default=None)),
        ('like', sgqlc.types.Arg(Int, graphql_name='like', default=None)),
        ('favorite', sgqlc.types.Arg(Int, graphql_name='favorite', default=None)),
        ('comment', sgqlc.types.Arg(Int, graphql_name='comment', default=None)),
        ('share', sgqlc.types.Arg(Int, graphql_name='share', default=None)),
        ('time_created', sgqlc.types.Arg(String, graphql_name='timeCreated', default=None)),
        ('time_updated', sgqlc.types.Arg(String, graphql_name='timeUpdated', default=None)),
        ('ctime', sgqlc.types.Arg(String, graphql_name='ctime', default=None)),
        ('mtime', sgqlc.types.Arg(String, graphql_name='mtime', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ItemOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ItemFilter, graphql_name='filter', default=None)),
))
    )
    brand = sgqlc.types.Field(sgqlc.types.list_of(Brand), graphql_name='Brand', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(ID, graphql_name='name', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_BrandOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_BrandFilter, graphql_name='filter', default=None)),
))
    )
    comment = sgqlc.types.Field(sgqlc.types.list_of(Comment), graphql_name='Comment', args=sgqlc.types.ArgDict((
        ('content', sgqlc.types.Arg(String, graphql_name='content', default=None)),
        ('like', sgqlc.types.Arg(Int, graphql_name='like', default=None)),
        ('time_created', sgqlc.types.Arg(String, graphql_name='timeCreated', default=None)),
        ('time_updated', sgqlc.types.Arg(String, graphql_name='timeUpdated', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_CommentOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_CommentFilter, graphql_name='filter', default=None)),
))
    )
    stats = sgqlc.types.Field(sgqlc.types.list_of('Stats'), graphql_name='Stats', args=sgqlc.types.ArgDict((
        ('domain', sgqlc.types.Arg(StatsDomain, graphql_name='domain', default=None)),
        ('key', sgqlc.types.Arg(String, graphql_name='key', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_StatsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_StatsFilter, graphql_name='filter', default=None)),
))
    )
    time_duration = sgqlc.types.Field(sgqlc.types.list_of('TimeDuration'), graphql_name='TimeDuration', args=sgqlc.types.ArgDict((
        ('length', sgqlc.types.Arg(Float, graphql_name='length', default=None)),
        ('unit', sgqlc.types.Arg(TimeUnit, graphql_name='unit', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_TimeDurationOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_TimeDurationFilter, graphql_name='filter', default=None)),
))
    )


class Source(sgqlc.types.Type):
    __schema__ = schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')
    kols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInfo'))), graphql_name='kols', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UserInfoOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Stats(sgqlc.types.Type):
    __schema__ = schema
    domain = sgqlc.types.Field(sgqlc.types.non_null(StatsDomain), graphql_name='domain')
    user = sgqlc.types.Field('UserInfo', graphql_name='user', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    item = sgqlc.types.Field(Item, graphql_name='item', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_ItemFilter, graphql_name='filter', default=None)),
))
    )
    key = sgqlc.types.Field(String, graphql_name='key')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatsData'))), graphql_name='data', args=sgqlc.types.ArgDict((
        ('dimensions', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='dimensions', default=None)),
        ('time', sgqlc.types.Arg(String, graphql_name='time', default=None)),
        ('start', sgqlc.types.Arg(String, graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(String, graphql_name='end', default=None)),
        ('duration', sgqlc.types.Arg(Int, graphql_name='duration', default=None)),
        ('current', sgqlc.types.Arg(TimePosition, graphql_name='current', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class StatsData(sgqlc.types.Type):
    __schema__ = schema
    time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='time')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    age = sgqlc.types.Field(IntRange, graphql_name='age')
    interest = sgqlc.types.Field('Tag', graphql_name='interest')
    province = sgqlc.types.Field(Province, graphql_name='province')
    activity = sgqlc.types.Field(String, graphql_name='activity')
    phone_brand = sgqlc.types.Field(Brand, graphql_name='phoneBrand')
    item_type = sgqlc.types.Field(ItemType, graphql_name='itemType')
    is_business = sgqlc.types.Field(Boolean, graphql_name='isBusiness')
    is_accepted = sgqlc.types.Field(Boolean, graphql_name='isAccepted')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    rolling_window_time = sgqlc.types.Field(Int, graphql_name='rollingWindowTime')
    rolling_window_count = sgqlc.types.Field(Int, graphql_name='rollingWindowCount')
    percent = sgqlc.types.Field(Float, graphql_name='percent')
    count = sgqlc.types.Field(Int, graphql_name='count')
    exposure_total = sgqlc.types.Field(Int, graphql_name='exposureTotal')
    exposure_mean = sgqlc.types.Field(Int, graphql_name='exposureMean')
    view_total = sgqlc.types.Field(Int, graphql_name='viewTotal')
    view_mean = sgqlc.types.Field(Int, graphql_name='viewMean')
    like_total = sgqlc.types.Field(Int, graphql_name='likeTotal')
    like_mean = sgqlc.types.Field(Int, graphql_name='likeMean')
    favorite_total = sgqlc.types.Field(Int, graphql_name='favoriteTotal')
    favorite_mean = sgqlc.types.Field(Int, graphql_name='favoriteMean')
    comment_total = sgqlc.types.Field(Int, graphql_name='commentTotal')
    comment_mean = sgqlc.types.Field(Int, graphql_name='commentMean')
    share_total = sgqlc.types.Field(Int, graphql_name='shareTotal')
    share_mean = sgqlc.types.Field(Int, graphql_name='shareMean')
    merchant_cooperated_total = sgqlc.types.Field(Int, graphql_name='merchantCooperatedTotal')
    item_accept_time_mean = sgqlc.types.Field(Int, graphql_name='itemAcceptTimeMean')
    item_complete_time_mean = sgqlc.types.Field(Int, graphql_name='itemCompleteTimeMean')


class Tag(sgqlc.types.Type):
    __schema__ = schema
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')
    kols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInfo'))), graphql_name='kols', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_UserInfoOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_UserInfoFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class TimeDuration(sgqlc.types.Type):
    __schema__ = schema
    length = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='length')
    unit = sgqlc.types.Field(sgqlc.types.non_null(TimeUnit), graphql_name='unit')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class UpdateResult(sgqlc.types.Type):
    __schema__ = schema
    ctime = sgqlc.types.Field(String, graphql_name='ctime')
    mtime = sgqlc.types.Field(String, graphql_name='mtime')
    message = sgqlc.types.Field(String, graphql_name='message')


class UserInfo(sgqlc.types.Type):
    __schema__ = schema
    source = sgqlc.types.Field(Source, graphql_name='source', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SourceFilter, graphql_name='filter', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    type = sgqlc.types.Field(UserType, graphql_name='type')
    is_primary = sgqlc.types.Field(Boolean, graphql_name='isPrimary')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    wechat = sgqlc.types.Field(String, graphql_name='wechat')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')
    signature = sgqlc.types.Field(String, graphql_name='signature')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    birthdate = sgqlc.types.Field(String, graphql_name='birthdate')
    province = sgqlc.types.Field(Province, graphql_name='province', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_ProvinceFilter, graphql_name='filter', default=None)),
))
    )
    city = sgqlc.types.Field(City, graphql_name='city', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_CityFilter, graphql_name='filter', default=None)),
))
    )
    constellation = sgqlc.types.Field(Constellation, graphql_name='constellation')
    mcn = sgqlc.types.Field(Mcn, graphql_name='mcn', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_McnFilter, graphql_name='filter', default=None)),
))
    )
    mcn_id = sgqlc.types.Field(String, graphql_name='mcnId')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Item)), graphql_name='items', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_ItemOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_ItemFilter, graphql_name='filter', default=None)),
))
    )
    price_video = sgqlc.types.Field(Int, graphql_name='priceVideo')
    price_long_video = sgqlc.types.Field(Int, graphql_name='priceLongVideo')
    price_article = sgqlc.types.Field(Int, graphql_name='priceArticle')
    time_created = sgqlc.types.Field(String, graphql_name='timeCreated')
    time_updated = sgqlc.types.Field(String, graphql_name='timeUpdated')
    ctime = sgqlc.types.Field(String, graphql_name='ctime')
    mtime = sgqlc.types.Field(String, graphql_name='mtime')
    stats = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Stats)), graphql_name='stats', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_StatsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_StatsFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class _Neo4jDate(sgqlc.types.Type):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jDateTime(sgqlc.types.Type):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalDateTime(sgqlc.types.Type):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalTime(sgqlc.types.Type):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jTime(sgqlc.types.Type):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')



########################################################################
# Unions
########################################################################
