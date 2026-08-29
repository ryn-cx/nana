from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID

class Details(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href: str

class Grid(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')
    tier: str | None = None
    type: str | None = None
    tms_image_type: str | None = Field(None, alias='tmsImageType')
    is_personalized: bool | None = Field(None, alias='isPersonalized')
    parent_id: UUID | None = Field(None, alias='parentId')

class ImageMap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: Grid

class ParentalRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str

class Meta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')

class ViewOption(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    provider_product_id: str | None = Field(None, alias='providerProductId')
    recording_type: str | None = Field(None, alias='recordingType')

class Attribution(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    attribution: Attribution | None = None

class Line2Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_cta: bool | None = Field(None, alias='hasCta')
    text: str
    optional: bool | None = None
    font: str | None = None

class Line1Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_cta: bool | None = Field(None, alias='hasCta')
    text: str
    font: str

class GridItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_map: ImageMap1 = Field(..., alias='imageMap')
    product_provider_ids: list[str] = Field(..., alias='productProviderIds')
    has_media: bool | None = Field(None, alias='hasMedia')
    free: bool | None = None
    line2: list[Line2Item]
    line1: list[Line1Item]

class Bobs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: list[GridItem]

class Meta1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str | None = None
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')
    version: int | None = None

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_server_data: str

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str

class TopRightItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    text_color: str = Field(..., alias='textColor')

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str | None = None
    text_color: str = Field(..., alias='textColor')

class Grid1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    top_right: list[TopRightItem] | None = Field(None, alias='top-right')
    bottom_left: list[BottomLeftItem] | None = Field(None, alias='bottom-left')

class Image2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image2
    title: str

class Image3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image3
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str | None = None
    text_color: str = Field(..., alias='textColor')

class TopRightItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image3
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    text_color: str = Field(..., alias='textColor')

class DetailScreen(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bottom_left: list[BottomLeftItem1] = Field(..., alias='bottom-left')
    top_right: list[TopRightItem1] | None = Field(None, alias='top-right')

class Indicators(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: Grid1 | None = None
    provider_badge: ProviderBadge | None = Field(None, alias='providerBadge')
    detail_screen: DetailScreen | None = Field(None, alias='detailScreen')

class CenterOverlay(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class Layout(BaseModel):
    model_config = ConfigDict(defer_build=True)
    center_overlay: CenterOverlay = Field(..., alias='centerOverlay')

class Image5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    tms_image_type: str = Field(..., alias='tmsImageType')

class ImageUrl(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_still_image: bool = Field(..., alias='isStillImage')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    url: str

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_map: ImageMap = Field(..., alias='imageMap')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    parental_ratings: list[ParentalRating] | None = Field(None, alias='parentalRatings')
    type: str | None = None
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
    indicators: Indicators | None = None
    layout: Layout | None = None
    images: list[Image5] | None = None
    image_urls: list[ImageUrl] | None = Field(None, alias='imageUrls')
    description: str | None = None
    kids_mode: bool | None = Field(None, alias='kidsMode')
    is_private: bool | None = Field(None, alias='isPrivate')

class ViewItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    details: Details | None = None
    content: Content

class Meta2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href: str
    id: str
    version: int

class TrackerOverrides1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection_id: str
    query_params: str
    collection_params: str
    category_ids: str
    row_server_data: str | None = None

class Collection(BaseModel):
    model_config = ConfigDict(defer_build=True)
    playback_context_params: str = Field(..., alias='playbackContextParams')
    collection_type: str = Field(..., alias='collectionType')
    view: list[ViewItem]
    meta: Meta2
    content_type: str = Field(..., alias='content-type')
    type: str
    title: str
    tracker_overrides: TrackerOverrides1 = Field(..., alias='trackerOverrides')
    invalidate_on: list[str] | None = Field(None, alias='invalidateOn')
    actions: list[str] | None = None

class Image6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    relative_height: float = Field(..., alias='relativeHeight')

class BottomLeftItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image6
    alt_text: str = Field(..., alias='altText')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID

class Grid2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bottom_left: list[BottomLeftItem2] = Field(..., alias='bottom-left')

class Indicators1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: Grid2

class Favorite(BaseModel):
    model_config = ConfigDict(defer_build=True)
    indicators: Indicators1

class ActionItems(BaseModel):
    model_config = ConfigDict(defer_build=True)
    favorite: Favorite

class Context(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class TrackerBeacon(BaseModel):
    model_config = ConfigDict(defer_build=True)
    quote_escape: str | None = Field(None, alias='quoteEscape')
    method: str
    body: str | None = None
    url: str
    events: list[str]

class Template(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str

class Colors(BaseModel):
    model_config = ConfigDict(defer_build=True)
    highlight_color: str = Field(..., alias='highlightColor')
    background_color: str = Field(..., alias='backgroundColor')
    progress_color: str = Field(..., alias='progressColor')
    theme: str
    overlay_color: str = Field(..., alias='overlayColor')
    text_color: str = Field(..., alias='textColor')

class Layout1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    overlay_title: bool = Field(..., alias='overlayTitle')
    template: Template
    colors: Colors

class TrackerOverrides2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_server_data: str
    page_id: str

class DynamicCollectionIndex(BaseModel):
    model_config = ConfigDict(defer_build=True)
    savelist: int
    continue_watching: int = Field(..., alias='continueWatching')

class Treacle(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dynamic_collection_index: DynamicCollectionIndex = Field(..., alias='dynamicCollectionIndex')

class PageModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
    layout: Layout1
    meta: Meta2
    auto_play: bool = Field(..., alias='autoPlay')
    tracker_overrides: TrackerOverrides2 = Field(..., alias='trackerOverrides')
    trace_id: UUID = Field(..., alias='traceId')
    treacle: Treacle
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
