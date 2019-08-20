# some query ID or hash code can change, use with care

BASE_URL = "https://www.facebook.com"
LOGIN_URL = "https://www.facebook.com/accounts/login/ajax/"
ACCOUNT_PAGE = "https://www.facebook.com/{username}"
MEDIA_LINK = "https://www.facebook.com/p/{code}"
ACCOUNT_MEDIAS = "https://www.facebook.com/graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={variables}"
ACCOUNT_JSON_INFO = "https://www.facebook.com/{username}/?__a=1"
MEDIA_JSON_INFO = "https://www.facebook.com/p/{code}/?__a=1"
MEDIA_JSON_BY_LOCATION_ID = "https://www.facebook.com/explore/locations/{{facebookLocationId}}/?__a=1&max_id={{maxId}}"
MEDIA_JSON_BY_TAG = "https://www.facebook.com/explore/tags/{tag}/?__a=1&max_id={max_id}"
GENERAL_SEARCH = "https://www.facebook.com/web/search/topsearch/?query={query}"
ACCOUNT_JSON_INFO_BY_ID = "ig_user({userId}){id,username,external_url,full_name,profile_pic_url,biography,followed_by{count},follows{count},media{count},is_private,is_verified}"
COMMENTS_BEFORE_COMMENT_ID_BY_CODE = "https://www.facebook.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={variables}"
LAST_LIKES_BY_CODE = "ig_shortcode({{code}}){likes{nodes{id,user{id,profile_pic_url,username,follows{count},followed_by{count},biography,full_name,media{count},is_private,external_url,is_verified}},page_info}}"
LIKES_BY_SHORTCODE = 'https://www.facebook.com/graphql/query/?query_id=17864450716183058&variables={"shortcode":"{{shortcode}}","first":{{count}},"after":"{{likeId}}"}'
FOLLOWING_URL = "https://www.facebook.com/graphql/query/?query_id=17874545323001329&id={{accountId}}&first={{count}}&after={{after}}"
FOLLOWERS_URL = "https://www.facebook.com/graphql/query/?query_id=17851374694183129&id={{accountId}}&first={{count}}&after={{after}}"
FOLLOW_URL = "https://www.facebook.com/web/friendships/{{accountId}}/follow/"
UNFOLLOW_URL = "https://www.facebook.com/web/friendships/{{accountId}}/unfollow/"
USER_FEED = "https://www.facebook.com/graphql/query/?query_id=17861995474116400&fetch_media_item_count=12&fetch_media_item_cursor=&fetch_comment_count=4&fetch_like=10"
USER_FEED2 = "https://www.facebook.com/?__a=1"
FACEBOOK_QUERY_URL = "https://www.facebook.com/query/"
FACEBOOK_CDN_URL = "https://scontent.cdnfacebook.com/"
ACCOUNT_JSON_PRIVATE_INFO_BY_ID = "https://i.facebook.com/api/v1/users/{userId}/info/"
ACCOUNT_MEDIAS2 = "https://www.facebook.com/graphql/query/?query_id=17880160963012870&id={{accountId}}&first=10&after="

# look alike?
URL_SIMILAR = (
    "https://www.facebook.com/graphql/query/?query_id=17845312237175864&id=4663052"
)
GRAPH_QL_QUERY_URL = "https://www.facebook.com/graphql/query/?query_id={{queryId}}"
