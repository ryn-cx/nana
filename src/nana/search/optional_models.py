from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | None = None
    id: str | None = None
    media_type: str | None = Field(None, alias='mediaType')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | None = None
    query_params: str | None = None
    collection_params: str | None = None

class Grid(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')

class ImageMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    tier: str | None = None
    provider_id: str | None = Field(None, alias='providerId')
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    type: str | None = None
    roku_id: str | None = Field(None, alias='rokuId')
    is_primary: bool | None = Field(None, alias='isPrimary')

class ParentalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | None = None

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image1 | None = None
    title: str | None = None

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | None = None

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image2 | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    audioguide: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class Grid1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem] | None = Field(None, alias='bottom-left')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image2 | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: AwareDatetime | None = Field(None, alias='validityEndTime')
    validity_start_time: AwareDatetime | None = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    audioguide: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class DetailScreen(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem1] | None = Field(None, alias='bottom-left')

class Indicators(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_badge: ProviderBadge | None = Field(None, alias='providerBadge')
    grid: Grid1 | None = None
    detail_screen: DetailScreen | None = Field(None, alias='detailScreen')

class Field100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: int | None = None
    text: str | None = None

class Descriptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_100: Field100 | None = Field(None, alias='100')

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None

class ProviderDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta1 | None = None
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')

class ViewOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_id: str | None = Field(None, alias='providerId')
    provider_details: ProviderDetails | None = Field(None, alias='providerDetails')
    provider_product_id: str | None = Field(None, alias='providerProductId')

class AmpId(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    id: str | None = None

class Meta2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')
    source: str | None = None
    href: str | None = None
    sid: UUID | str | None = Field(default=None, union_mode='left_to_right')

class TrackerOverrides1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | None = None

class Meta3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    sid: str | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta3 | None = None

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap | None = Field(None, alias='imageMap')
    images: list[Image] | None = None
    run_time_seconds: int | None = Field(None, alias='runTimeSeconds')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    parental_ratings: list[ParentalRating] | None = Field(None, alias='parentalRatings')
    type: str | None = None
    title: str | None = None
    indicators: Indicators | None = None
    descriptions: Descriptions | None = None
    view_options: list[ViewOption] | None = Field(None, alias='viewOptions')
    amp_ids: list[AmpId] | None = Field(None, alias='ampIds')
    current_time: AwareDatetime | None = Field(None, alias='currentTime')
    kids_directed: bool | None = Field(None, alias='kidsDirected')
    genres: list[str] | None = None
    meta: Meta2 | None = None
    release_year: int | None = Field(None, alias='releaseYear')
    savable: bool | None = None
    tracker_overrides: TrackerOverrides1 | None = Field(None, alias='trackerOverrides')
    seasons: list[Season] | None = None
    end_date: AwareDatetime | None = Field(None, alias='endDate')

class Search(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    confidence_score: int | float | None = Field(None, alias='confidenceScore')

class Features(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    search: Search | None = None

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | None = None

class ViewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content | None = None
    features: Features | None = None
    details: Details | None = None

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta | None = None
    type: str | None = None
    content_type: str | None = Field(None, alias='content-type')
    title: str | None = None
    tracker_overrides: TrackerOverrides | None = Field(None, alias='trackerOverrides')
    view: list[ViewItem] | None = None
    trace_id: UUID | None = Field(None, alias='traceId')
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
