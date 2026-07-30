from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field

class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    href: str
    id: str
    media_type: str = Field(..., alias='mediaType')

class TrackerOverrides(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    collection_id: str
    query_params: str
    collection_params: str

class Grid(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')

class ImageMap(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: Grid

class Image(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    tier: str
    provider_id: str | None = Field(None, alias='providerId')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    is_primary: bool | None = Field(None, alias='isPrimary')
    roku_id: str | None = Field(None, alias='rokuId')

class ParentalRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str

class Image1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image: Image1
    title: str

class Image2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str

class BottomLeftItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image2
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str
    text_color: str = Field(..., alias='textColor')

class Grid1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bottom_left: list[BottomLeftItem] = Field(..., alias='bottom-left')

class BottomLeftItem1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image2
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str
    text_color: str = Field(..., alias='textColor')

class DetailScreen(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bottom_left: list[BottomLeftItem1] = Field(..., alias='bottom-left')

class Indicators(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    provider_badge: ProviderBadge | None = Field(None, alias='providerBadge')
    grid: Grid1
    detail_screen: DetailScreen = Field(..., alias='detailScreen')

class Field100(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    size: int
    text: str

class Descriptions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_100: Field100 | None = Field(None, alias='100')

class Meta1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta1
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')

class ViewOption(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails = Field(..., alias='providerDetails')
    provider_product_id: str | None = Field(None, alias='providerProductId')

class AmpId(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    id: str

class Meta2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str | None = None
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')

class TrackerOverrides1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_server_data: str

class Meta3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    sid: str

class Season(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta3

class Content(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_map: ImageMap = Field(..., alias='imageMap')
    images: list[Image]
    run_time_seconds: int | None = Field(None, alias='runTimeSeconds')
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    parental_ratings: list[ParentalRating] | None = Field(None, alias='parentalRatings')
    type: str
    title: str
    indicators: Indicators | None = None
    descriptions: Descriptions
    view_options: list[ViewOption] | None = Field(None, alias='viewOptions')
    amp_ids: list[AmpId] | None = Field(None, alias='ampIds')
    current_time: AwareDatetime = Field(..., alias='currentTime')
    kids_directed: bool = Field(..., alias='kidsDirected')
    genres: list[str]
    meta: Meta2
    release_year: int = Field(..., alias='releaseYear')
    savable: bool
    tracker_overrides: TrackerOverrides1 = Field(..., alias='trackerOverrides')
    seasons: list[Season] | None = None
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class Search(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    confidence_score: int | float = Field(..., alias='confidenceScore')

class Features(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    search: Search

class Details(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    href: str

class ViewItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    content: Content
    features: Features
    details: Details

class SearchModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta
    type: str
    content_type: str = Field(..., alias='content-type')
    title: str
    tracker_overrides: TrackerOverrides = Field(..., alias='trackerOverrides')
    view: list[ViewItem]
    trace_id: UUID = Field(..., alias='traceId')
