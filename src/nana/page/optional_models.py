from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | Any = Field(default=None, union_mode='left_to_right')

class Grid(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    roku_id: str | Any = Field(None, alias='rokuId', union_mode='left_to_right')
    tier: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    tms_image_type: str | Any = Field(None, alias='tmsImageType', union_mode='left_to_right')
    is_personalized: bool | Any = Field(None, alias='isPersonalized', union_mode='left_to_right')
    parent_id: UUID | Any = Field(None, alias='parentId', union_mode='left_to_right')

class ImageMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid | Any = Field(default=None, union_mode='left_to_right')

class ParentalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class ProviderDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta | Any = Field(default=None, union_mode='left_to_right')
    provider_product_ids: list[str] | Any = Field(None, alias='providerProductIds', union_mode='left_to_right')

class ViewOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_details: ProviderDetails | Any = Field(None, alias='providerDetails', union_mode='left_to_right')
    is_unlocked: bool | Any = Field(None, alias='isUnlocked', union_mode='left_to_right')
    provider_product_id: str | Any = Field(None, alias='providerProductId', union_mode='left_to_right')
    recording_type: str | Any = Field(None, alias='recordingType', union_mode='left_to_right')

class Attribution(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ImageMap1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attribution: Attribution | Any = Field(default=None, union_mode='left_to_right')

class Line2Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_cta: bool | Any = Field(None, alias='hasCta', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    optional: bool | Any = Field(default=None, union_mode='left_to_right')
    font: str | Any = Field(default=None, union_mode='left_to_right')

class Line1Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_cta: bool | Any = Field(None, alias='hasCta', union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    font: str | Any = Field(default=None, union_mode='left_to_right')

class GridItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap1 | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    product_provider_ids: list[str] | Any = Field(None, alias='productProviderIds', union_mode='left_to_right')
    has_media: bool | Any = Field(None, alias='hasMedia', union_mode='left_to_right')
    free: bool | Any = Field(default=None, union_mode='left_to_right')
    line2: list[Line2Item] | Any = Field(default=None, union_mode='left_to_right')
    line1: list[Line1Item] | Any = Field(default=None, union_mode='left_to_right')

class Bobs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: list[GridItem] | Any = Field(default=None, union_mode='left_to_right')

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    version: int | Any = Field(default=None, union_mode='left_to_right')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')

class TopRightItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    audioguide: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class Grid1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    top_right: list[TopRightItem] | Any = Field(None, alias='top-right', union_mode='left_to_right')
    bottom_left: list[BottomLeftItem] | Any = Field(None, alias='bottom-left', union_mode='left_to_right')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image2 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image3 | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    audioguide: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class TopRightItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image3 | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class DetailScreen(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem1] | Any = Field(None, alias='bottom-left', union_mode='left_to_right')
    top_right: list[TopRightItem1] | Any = Field(None, alias='top-right', union_mode='left_to_right')

class Indicators(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid1 | Any = Field(default=None, union_mode='left_to_right')
    provider_badge: ProviderBadge | Any = Field(None, alias='providerBadge', union_mode='left_to_right')
    detail_screen: DetailScreen | Any = Field(None, alias='detailScreen', union_mode='left_to_right')

class CenterOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Layout(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    center_overlay: CenterOverlay | Any = Field(None, alias='centerOverlay', union_mode='left_to_right')

class Image5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    tier: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    tms_image_type: str | Any = Field(None, alias='tmsImageType', union_mode='left_to_right')

class ImageUrl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_still_image: bool | Any = Field(None, alias='isStillImage', union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    parental_ratings: list[ParentalRating] | Any = Field(None, alias='parentalRatings', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    view_options: list[ViewOption] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')
    bobs: Bobs | Any = Field(default=None, union_mode='left_to_right')
    current_time: AwareDatetime | Any = Field(None, alias='currentTime', union_mode='left_to_right')
    seasons_count: int | Any = Field(None, alias='seasonsCount', union_mode='left_to_right')
    kids_directed: bool | Any = Field(None, alias='kidsDirected', union_mode='left_to_right')
    meta: Meta1 | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(None, alias='releaseYear', union_mode='left_to_right')
    savable: bool | Any = Field(default=None, union_mode='left_to_right')
    tracker_overrides: TrackerOverrides | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
    indicators: Indicators | Any = Field(default=None, union_mode='left_to_right')
    layout: Layout | Any = Field(default=None, union_mode='left_to_right')
    images: list[Image5] | Any = Field(default=None, union_mode='left_to_right')
    image_urls: list[ImageUrl] | Any = Field(None, alias='imageUrls', union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    kids_mode: bool | Any = Field(None, alias='kidsMode', union_mode='left_to_right')
    is_private: bool | Any = Field(None, alias='isPrivate', union_mode='left_to_right')

class ViewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    details: Details | Any = Field(default=None, union_mode='left_to_right')
    content: Content | Any = Field(default=None, union_mode='left_to_right')

class Meta2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    version: int | Any = Field(default=None, union_mode='left_to_right')

class TrackerOverrides1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | Any = Field(default=None, union_mode='left_to_right')
    query_params: str | Any = Field(default=None, union_mode='left_to_right')
    collection_params: str | Any = Field(default=None, union_mode='left_to_right')
    category_ids: str | Any = Field(default=None, union_mode='left_to_right')
    row_server_data: str | Any = Field(default=None, union_mode='left_to_right')

class Collection(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playback_context_params: str | Any = Field(None, alias='playbackContextParams', union_mode='left_to_right')
    collection_type: str | Any = Field(None, alias='collectionType', union_mode='left_to_right')
    view: list[ViewItem] | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta2 | Any = Field(default=None, union_mode='left_to_right')
    content_type: str | Any = Field(None, alias='content-type', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    tracker_overrides: TrackerOverrides1 | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
    invalidate_on: list[str] | Any = Field(None, alias='invalidateOn', union_mode='left_to_right')
    actions: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Image6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    relative_height: float | Any = Field(None, alias='relativeHeight', union_mode='left_to_right')

class BottomLeftItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image6 | Any = Field(default=None, union_mode='left_to_right')
    alt_text: str | Any = Field(None, alias='altText', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')

class Grid2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem2] | Any = Field(None, alias='bottom-left', union_mode='left_to_right')

class Indicators1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid2 | Any = Field(default=None, union_mode='left_to_right')

class Favorite(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    indicators: Indicators1 | Any = Field(default=None, union_mode='left_to_right')

class ActionItems(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    favorite: Favorite | Any = Field(default=None, union_mode='left_to_right')

class Context(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    more_like_this_svc_url: str | Any = Field(None, alias='moreLikeThisSvcUrl', union_mode='left_to_right')
    action_items: ActionItems | Any = Field(None, alias='actionItems', union_mode='left_to_right')
    postman_url: str | Any = Field(None, alias='postmanUrl', union_mode='left_to_right')
    epg_browse_url: str | Any = Field(None, alias='epgBrowseUrl', union_mode='left_to_right')
    image_svc_host: str | Any = Field(None, alias='imageSvcHost', union_mode='left_to_right')
    epg_schedule_patch_url: str | Any = Field(None, alias='epgSchedulePatchUrl', union_mode='left_to_right')
    watchlist_collection_url: str | Any = Field(None, alias='watchlistCollectionUrl', union_mode='left_to_right')
    watchlist_remote_collection_url: str | Any = Field(None, alias='watchlistRemoteCollectionUrl', union_mode='left_to_right')
    epg_row_url: str | Any = Field(None, alias='epgRowUrl', union_mode='left_to_right')
    epg_splash_uri: str | Any = Field(None, alias='epgSplashUri', union_mode='left_to_right')
    rights_manager_host: str | Any = Field(None, alias='rightsManagerHost', union_mode='left_to_right')
    drm: str | Any = Field(default=None, union_mode='left_to_right')
    in_app_search_svc_url: str | Any = Field(None, alias='inAppSearchSvcUrl', union_mode='left_to_right')
    epg_page_url: str | Any = Field(None, alias='epgPageUrl', union_mode='left_to_right')
    text_vsr_one_stage_search_page_url: str | Any = Field(None, alias='textVsrOneStageSearchPageUrl', union_mode='left_to_right')
    in_app_search_svc_preview_url: str | Any = Field(None, alias='inAppSearchSvcPreviewUrl', union_mode='left_to_right')
    search_session_url: str | Any = Field(None, alias='searchSessionUrl', union_mode='left_to_right')
    trace_relay_svc_url: str | Any = Field(None, alias='traceRelaySvcUrl', union_mode='left_to_right')
    kids_profile_settings_url: str | Any = Field(None, alias='kidsProfileSettingsUrl', union_mode='left_to_right')
    continue_watching_collection_url: str | Any = Field(None, alias='continueWatchingCollectionUrl', union_mode='left_to_right')

class TrackerBeacon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    quote_escape: str | Any = Field(None, alias='quoteEscape', union_mode='left_to_right')
    method: str | Any = Field(default=None, union_mode='left_to_right')
    body: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    events: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Template(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Colors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    highlight_color: str | Any = Field(None, alias='highlightColor', union_mode='left_to_right')
    background_color: str | Any = Field(None, alias='backgroundColor', union_mode='left_to_right')
    progress_color: str | Any = Field(None, alias='progressColor', union_mode='left_to_right')
    theme: str | Any = Field(default=None, union_mode='left_to_right')
    overlay_color: str | Any = Field(None, alias='overlayColor', union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class Layout1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    overlay_title: bool | Any = Field(None, alias='overlayTitle', union_mode='left_to_right')
    template: Template | Any = Field(default=None, union_mode='left_to_right')
    colors: Colors | Any = Field(default=None, union_mode='left_to_right')

class TrackerOverrides2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_server_data: str | Any = Field(default=None, union_mode='left_to_right')
    page_id: str | Any = Field(default=None, union_mode='left_to_right')

class DynamicCollectionIndex(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    savelist: int | Any = Field(default=None, union_mode='left_to_right')
    continue_watching: int | Any = Field(None, alias='continueWatching', union_mode='left_to_right')

class Treacle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dynamic_collection_index: DynamicCollectionIndex | Any = Field(None, alias='dynamicCollectionIndex', union_mode='left_to_right')

class PageModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    no_utility_row: bool | Any = Field(None, alias='noUtilityRow', union_mode='left_to_right')
    is_private: bool | Any = Field(None, alias='isPrivate', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    collections: list[Collection] | Any = Field(default=None, union_mode='left_to_right')
    context: Context | Any = Field(default=None, union_mode='left_to_right')
    kids_mode: bool | Any = Field(None, alias='kidsMode', union_mode='left_to_right')
    content_type: str | Any = Field(None, alias='content-type', union_mode='left_to_right')
    tracker_beacons: list[TrackerBeacon] | Any = Field(None, alias='trackerBeacons', union_mode='left_to_right')
    playback_context_params: str | Any = Field(None, alias='playbackContextParams', union_mode='left_to_right')
    layout: Layout1 | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta2 | Any = Field(default=None, union_mode='left_to_right')
    auto_play: bool | Any = Field(None, alias='autoPlay', union_mode='left_to_right')
    tracker_overrides: TrackerOverrides2 | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
    trace_id: UUID | Any = Field(None, alias='traceId', union_mode='left_to_right')
    treacle: Treacle | Any = Field(default=None, union_mode='left_to_right')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
