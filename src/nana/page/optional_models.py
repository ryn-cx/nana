from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | None = None

class Grid(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')
    tier: str | None = None
    type: str | None = None
    tms_image_type: str | None = Field(None, alias='tmsImageType')
    is_personalized: bool | None = Field(None, alias='isPersonalized')
    parent_id: UUID | None = Field(None, alias='parentId')

class ImageMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid | None = None

class ParentalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None

class ProviderDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta | None = None
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')

class ViewOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_id: str | None = Field(None, alias='providerId')
    provider_details: ProviderDetails | None = Field(None, alias='providerDetails')
    is_unlocked: bool | None = Field(None, alias='isUnlocked')
    provider_product_id: str | None = Field(None, alias='providerProductId')
    recording_type: str | None = Field(None, alias='recordingType')

class Attribution(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ImageMap1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    attribution: Attribution | None = None

class Line2Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_cta: bool | None = Field(None, alias='hasCta')
    text: str | None = None
    optional: bool | None = None
    font: str | None = None

class Line1Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_cta: bool | None = Field(None, alias='hasCta')
    text: str | None = None
    font: str | None = None

class GridItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap1 | None = Field(None, alias='imageMap')
    product_provider_ids: list[str] | None = Field(None, alias='productProviderIds')
    has_media: bool | None = Field(None, alias='hasMedia')
    free: bool | None = None
    line2: list[Line2Item] | None = None
    line1: list[Line1Item] | None = None

class Bobs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: list[GridItem] | None = None

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')
    source: str | None = None
    href: str | None = None
    sid: UUID | str | None = Field(default=None, union_mode='left_to_right')
    version: int | None = None

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None

class TopRightItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    audioguide: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class Grid1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    top_right: list[TopRightItem] | None = Field(None, alias='top-right')
    bottom_left: list[BottomLeftItem] | None = Field(None, alias='bottom-left')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image2 | None = None
    title: str | None = None

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image3 | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    audioguide: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class TopRightItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image3 | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class DetailScreen(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem1] | None = Field(None, alias='bottom-left')
    top_right: list[TopRightItem1] | None = Field(None, alias='top-right')

class Indicators(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid1 | None = None
    provider_badge: ProviderBadge | None = Field(None, alias='providerBadge')
    detail_screen: DetailScreen | None = Field(None, alias='detailScreen')

class CenterOverlay(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None

class Layout(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    center_overlay: CenterOverlay | None = Field(None, alias='centerOverlay')

class Image5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    tier: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    type: str | None = None
    tms_image_type: str | None = Field(None, alias='tmsImageType')

class ImageUrl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_still_image: bool | None = Field(None, alias='isStillImage')
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    url: str | None = None

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap | None = Field(None, alias='imageMap')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    parental_ratings: list[ParentalRating] | None = Field(None, alias='parentalRatings')
    type: str | None = None
    title: str | None = None
    view_options: list[ViewOption] | None = Field(None, alias='viewOptions')
    bobs: Bobs | None = None
    current_time: AwareDatetime | None = Field(None, alias='currentTime')
    seasons_count: int | None = Field(None, alias='seasonsCount')
    kids_directed: bool | None = Field(None, alias='kidsDirected')
    meta: Meta1 | None = None
    release_year: int | None = Field(None, alias='releaseYear')
    savable: bool | None = None
    tracker_overrides: TrackerOverrides | None = Field(None, alias='trackerOverrides')
    indicators: Indicators | None = None
    layout: Layout | None = None
    images: list[Image5] | None = None
    image_urls: list[ImageUrl] | None = Field(None, alias='imageUrls')
    description: str | None = None
    kids_mode: bool | None = Field(None, alias='kidsMode')
    is_private: bool | None = Field(None, alias='isPrivate')

class ViewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    details: Details | None = None
    content: Content | None = None

class Meta2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | None = Field(None, alias='mediaType')
    href: str | None = None
    id: str | None = None
    version: int | None = None

class TrackerOverrides1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | None = None
    query_params: str | None = None
    collection_params: str | None = None
    category_ids: str | None = None
    row_server_data: str | None = None

class Collection(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    playback_context_params: str | None = Field(None, alias='playbackContextParams')
    collection_type: str | None = Field(None, alias='collectionType')
    view: list[ViewItem] | None = None
    meta: Meta2 | None = None
    content_type: str | None = Field(None, alias='content-type')
    type: str | None = None
    title: str | None = None
    tracker_overrides: TrackerOverrides1 | None = Field(None, alias='trackerOverrides')
    invalidate_on: list[str] | None = Field(None, alias='invalidateOn')
    actions: list[str] | None = None

class Image6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    relative_height: float | None = Field(None, alias='relativeHeight')

class BottomLeftItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image6 | None = None
    alt_text: str | None = Field(None, alias='altText')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None

class Grid2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem2] | None = Field(None, alias='bottom-left')

class Indicators1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid2 | None = None

class Favorite(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    indicators: Indicators1 | None = None

class ActionItems(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    favorite: Favorite | None = None

class Context(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    more_like_this_svc_url: str | None = Field(None, alias='moreLikeThisSvcUrl')
    action_items: ActionItems | None = Field(None, alias='actionItems')
    postman_url: str | None = Field(None, alias='postmanUrl')
    epg_browse_url: str | None = Field(None, alias='epgBrowseUrl')
    image_svc_host: str | None = Field(None, alias='imageSvcHost')
    epg_schedule_patch_url: str | None = Field(None, alias='epgSchedulePatchUrl')
    watchlist_collection_url: str | None = Field(None, alias='watchlistCollectionUrl')
    watchlist_remote_collection_url: str | None = Field(None, alias='watchlistRemoteCollectionUrl')
    epg_row_url: str | None = Field(None, alias='epgRowUrl')
    epg_splash_uri: str | None = Field(None, alias='epgSplashUri')
    rights_manager_host: str | None = Field(None, alias='rightsManagerHost')
    drm: str | None = None
    in_app_search_svc_url: str | None = Field(None, alias='inAppSearchSvcUrl')
    epg_page_url: str | None = Field(None, alias='epgPageUrl')
    text_vsr_one_stage_search_page_url: str | None = Field(None, alias='textVsrOneStageSearchPageUrl')
    in_app_search_svc_preview_url: str | None = Field(None, alias='inAppSearchSvcPreviewUrl')
    search_session_url: str | None = Field(None, alias='searchSessionUrl')
    trace_relay_svc_url: str | None = Field(None, alias='traceRelaySvcUrl')
    kids_profile_settings_url: str | None = Field(None, alias='kidsProfileSettingsUrl')
    continue_watching_collection_url: str | None = Field(None, alias='continueWatchingCollectionUrl')

class TrackerBeacon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    quote_escape: str | None = Field(None, alias='quoteEscape')
    method: str | None = None
    body: str | None = None
    url: str | None = None
    events: list[str] | None = None

class Template(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None

class Colors(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    highlight_color: str | None = Field(None, alias='highlightColor')
    background_color: str | None = Field(None, alias='backgroundColor')
    progress_color: str | None = Field(None, alias='progressColor')
    theme: str | None = None
    overlay_color: str | None = Field(None, alias='overlayColor')
    text_color: str | None = Field(None, alias='textColor')

class Layout1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    overlay_title: bool | None = Field(None, alias='overlayTitle')
    template: Template | None = None
    colors: Colors | None = None

class TrackerOverrides2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_server_data: str | None = None
    page_id: str | None = None

class DynamicCollectionIndex(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    savelist: int | None = None
    continue_watching: int | None = Field(None, alias='continueWatching')

class Treacle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dynamic_collection_index: DynamicCollectionIndex | None = Field(None, alias='dynamicCollectionIndex')

class PageModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    no_utility_row: bool | None = Field(None, alias='noUtilityRow')
    is_private: bool | None = Field(None, alias='isPrivate')
    type: str | None = None
    title: str | None = None
    collections: list[Collection] | None = None
    context: Context | None = None
    kids_mode: bool | None = Field(None, alias='kidsMode')
    content_type: str | None = Field(None, alias='content-type')
    tracker_beacons: list[TrackerBeacon] | None = Field(None, alias='trackerBeacons')
    playback_context_params: str | None = Field(None, alias='playbackContextParams')
    layout: Layout1 | None = None
    meta: Meta2 | None = None
    auto_play: bool | None = Field(None, alias='autoPlay')
    tracker_overrides: TrackerOverrides2 | None = Field(None, alias='trackerOverrides')
    trace_id: UUID | None = Field(None, alias='traceId')
    treacle: Treacle | None = None
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
