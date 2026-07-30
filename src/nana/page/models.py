from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field

class Details(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    href: str

class Grid(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')
    tier: str | None = None
    type: str | None = None
    tms_image_type: str | None = Field(None, alias='tmsImageType')
    is_personalized: bool | None = Field(None, alias='isPersonalized')
    parent_id: UUID | None = Field(None, alias='parentId')

class ImageMap(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: Grid

class ParentalRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str

class Image(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image: Image
    title: str

class Image1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str

class BottomLeftItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image1
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str | None = None
    text_color: str = Field(..., alias='textColor')

class TopRightItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image1
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    text_color: str = Field(..., alias='textColor')

class Grid1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bottom_left: list[BottomLeftItem] | None = Field(None, alias='bottom-left')
    top_right: list[TopRightItem] | None = Field(None, alias='top-right')

class BottomLeftItem1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image1
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str | None = None
    text_color: str = Field(..., alias='textColor')

class TopRightItem1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image1
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    text_color: str = Field(..., alias='textColor')

class DetailScreen(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bottom_left: list[BottomLeftItem1] | None = Field(None, alias='bottom-left')
    top_right: list[TopRightItem1] | None = Field(None, alias='top-right')

class Indicators(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    provider_badge: ProviderBadge | None = Field(None, alias='providerBadge')
    grid: Grid1 | None = None
    detail_screen: DetailScreen | None = Field(None, alias='detailScreen')

class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str
    scope: str | None = None

class ProviderDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')

class ViewOption(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    provider_product_id: str | None = Field(None, alias='providerProductId')
    mvpd_livefeed_id: UUID | None = Field(None, alias='mvpdLivefeedId')

class Attribution(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    attribution: Attribution | None = None

class Line2Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_cta: bool | None = Field(None, alias='hasCta')
    text: str
    optional: bool | None = None
    font: str | None = None

class Line1Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_cta: bool | None = Field(None, alias='hasCta')
    text: str
    font: str

class GridItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_map: ImageMap1 = Field(..., alias='imageMap')
    product_provider_ids: list[str] = Field(..., alias='productProviderIds')
    has_media: bool | None = Field(None, alias='hasMedia')
    free: bool | None = None
    line2: list[Line2Item]
    line1: list[Line1Item]

class Bobs(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: list[GridItem]

class Meta1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str | None = None
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')
    version: int | None = None
    scope: str | None = None

class TrackerOverrides(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_server_data: str

class CenterOverlay(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str

class Layout(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    center_overlay: CenterOverlay = Field(..., alias='centerOverlay')

class Image5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    tms_image_type: str = Field(..., alias='tmsImageType')

class ImageUrl(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    is_still_image: bool = Field(..., alias='isStillImage')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    url: str

class Content(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_map: ImageMap = Field(..., alias='imageMap')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    parental_ratings: list[ParentalRating] | None = Field(None, alias='parentalRatings')
    type: str | None = None
    indicators: Indicators | None = None
    title: str
    view_options: list[ViewOption] | None = Field(None, alias='viewOptions')
    bobs: Bobs
    current_time: AwareDatetime | None = Field(None, alias='currentTime')
    seasons_count: int | None = Field(None, alias='seasonsCount')
    kids_directed: bool | None = Field(None, alias='kidsDirected')
    meta: Meta1
    release_year: int | None = Field(None, alias='releaseYear')
    savable: bool | None = None
    tracker_overrides: TrackerOverrides = Field(..., alias='trackerOverrides')
    layout: Layout | None = None
    images: list[Image5] | None = None
    image_urls: list[ImageUrl] | None = Field(None, alias='imageUrls')
    description: str | None = None
    kids_mode: bool | None = Field(None, alias='kidsMode')
    is_private: bool | None = Field(None, alias='isPrivate')

class ViewItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    details: Details | None = None
    content: Content

class Meta2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href: str
    id: str
    version: int

class TrackerOverrides1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    collection_id: str
    query_params: str
    collection_params: str
    category_ids: str
    row_server_data: str | None = None

class Fhd(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo: str

class Original(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo: str

class Hd(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    logo: str

class Assets(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    fhd: Fhd
    original: Original
    hd: Hd

class Layout1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    indicator_id: UUID = Field(..., alias='indicatorId')
    assets: Assets
    alt_text: str = Field(..., alias='altText')
    audioguide: str

class Image6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str

class Meta3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class TrackerOverrides2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_server_data: str

class Providerattributes(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    images: list[Image6]
    provider_product_ids: list[str] = Field(..., alias='providerProductIds')
    meta: Meta3
    channel_store_code: str = Field(..., alias='channelStoreCode')
    is_private: bool = Field(..., alias='isPrivate')
    type: str
    title: str
    tracker_overrides: TrackerOverrides2 = Field(..., alias='trackerOverrides')

class Features(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    providerattributes: Providerattributes

class Collection(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    playback_context_params: str = Field(..., alias='playbackContextParams')
    collection_type: str = Field(..., alias='collectionType')
    view: list[ViewItem]
    meta: Meta2
    content_type: str = Field(..., alias='content-type')
    type: str
    title: str
    tracker_overrides: TrackerOverrides1 = Field(..., alias='trackerOverrides')
    layout: Layout1 | None = None
    features: Features | None = None
    invalidate_on: list[str] | None = Field(None, alias='invalidateOn')
    actions: list[str] | None = None

class Image7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    relative_height: float = Field(..., alias='relativeHeight')

class BottomLeftItem2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image: Image7
    alt_text: str = Field(..., alias='altText')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID

class Grid2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bottom_left: list[BottomLeftItem2] = Field(..., alias='bottom-left')

class Indicators1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: Grid2

class Favorite(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    indicators: Indicators1

class ActionItems(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    favorite: Favorite

class Context(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    more_like_this_svc_url: str = Field(..., alias='moreLikeThisSvcUrl')
    action_items: ActionItems = Field(..., alias='actionItems')
    postman_url: str = Field(..., alias='postmanUrl')
    epg_browse_url: str = Field(..., alias='epgBrowseUrl')
    image_svc_host: str = Field(..., alias='imageSvcHost')
    epg_schedule_patch_url: str = Field(..., alias='epgSchedulePatchUrl')
    watchlist_collection_url: str = Field(..., alias='watchlistCollectionUrl')
    watchlist_remote_collection_url: str = Field(..., alias='watchlistRemoteCollectionUrl')
    epg_row_url: str = Field(..., alias='epgRowUrl')
    epg_splash_uri: str = Field(..., alias='epgSplashUri')
    rights_manager_host: str = Field(..., alias='rightsManagerHost')
    drm: str
    in_app_search_svc_url: str = Field(..., alias='inAppSearchSvcUrl')
    epg_page_url: str = Field(..., alias='epgPageUrl')
    text_vsr_one_stage_search_page_url: str = Field(..., alias='textVsrOneStageSearchPageUrl')
    in_app_search_svc_preview_url: str = Field(..., alias='inAppSearchSvcPreviewUrl')
    search_session_url: str = Field(..., alias='searchSessionUrl')
    trace_relay_svc_url: str = Field(..., alias='traceRelaySvcUrl')
    kids_profile_settings_url: str = Field(..., alias='kidsProfileSettingsUrl')
    continue_watching_collection_url: str = Field(..., alias='continueWatchingCollectionUrl')

class TrackerBeacon(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    quote_escape: str | None = Field(None, alias='quoteEscape')
    method: str
    body: str | None = None
    url: str
    events: list[str]

class Template(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str

class Colors(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    highlight_color: str = Field(..., alias='highlightColor')
    background_color: str = Field(..., alias='backgroundColor')
    progress_color: str = Field(..., alias='progressColor')
    theme: str
    overlay_color: str = Field(..., alias='overlayColor')
    text_color: str = Field(..., alias='textColor')

class Layout2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    overlay_title: bool = Field(..., alias='overlayTitle')
    template: Template
    colors: Colors

class Meta4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href: str
    id: str
    version: int

class TrackerOverrides3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    page_server_data: str
    page_id: str

class DynamicCollectionIndex(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    savelist: int
    continue_watching: int = Field(..., alias='continueWatching')

class Treacle(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    dynamic_collection_index: DynamicCollectionIndex = Field(..., alias='dynamicCollectionIndex')

class PageModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    no_utility_row: bool = Field(..., alias='noUtilityRow')
    is_private: bool = Field(..., alias='isPrivate')
    type: str
    title: str
    collections: list[Collection]
    context: Context
    kids_mode: bool = Field(..., alias='kidsMode')
    content_type: str = Field(..., alias='content-type')
    tracker_beacons: list[TrackerBeacon] = Field(..., alias='trackerBeacons')
    playback_context_params: str = Field(..., alias='playbackContextParams')
    layout: Layout2
    meta: Meta4
    auto_play: bool = Field(..., alias='autoPlay')
    tracker_overrides: TrackerOverrides3 = Field(..., alias='trackerOverrides')
    trace_id: UUID = Field(..., alias='traceId')
    treacle: Treacle
