from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    collection_id: str | Any = Field(default=None, union_mode='left_to_right')
    query_params: str | Any = Field(default=None, union_mode='left_to_right')
    collection_params: str | Any = Field(default=None, union_mode='left_to_right')

class Grid(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    roku_id: str | Any = Field(None, alias='rokuId', union_mode='left_to_right')

class ImageMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    tier: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    roku_id: str | Any = Field(None, alias='rokuId', union_mode='left_to_right')
    is_primary: bool | Any = Field(None, alias='isPrimary', union_mode='left_to_right')

class ParentalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image1 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image2 | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    audioguide: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class Grid1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem] | Any = Field(None, alias='bottom-left', union_mode='left_to_right')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image2 | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: AwareDatetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: AwareDatetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    audioguide: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class DetailScreen(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem1] | Any = Field(None, alias='bottom-left', union_mode='left_to_right')

class Indicators(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_badge: ProviderBadge | Any = Field(None, alias='providerBadge', union_mode='left_to_right')
    grid: Grid1 | Any = Field(default=None, union_mode='left_to_right')
    detail_screen: DetailScreen | Any = Field(None, alias='detailScreen', union_mode='left_to_right')

class Field100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: int | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Descriptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_100: Field100 | Any = Field(None, alias='100', union_mode='left_to_right')

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class ProviderDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta1 | Any = Field(default=None, union_mode='left_to_right')
    provider_product_ids: list[str] | Any = Field(None, alias='providerProductIds', union_mode='left_to_right')

class ViewOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_details: ProviderDetails | Any = Field(None, alias='providerDetails', union_mode='left_to_right')
    provider_product_id: str | Any = Field(None, alias='providerProductId', union_mode='left_to_right')

class AmpId(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')

class Meta2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | str | Any = Field(default=None, union_mode='left_to_right')

class TrackerOverrides1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | Any = Field(default=None, union_mode='left_to_right')

class Meta3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    sid: str | Any = Field(default=None, union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta3 | Any = Field(default=None, union_mode='left_to_right')

class Content(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    run_time_seconds: int | Any = Field(None, alias='runTimeSeconds', union_mode='left_to_right')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    parental_ratings: list[ParentalRating] | Any = Field(None, alias='parentalRatings', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    indicators: Indicators | Any = Field(default=None, union_mode='left_to_right')
    descriptions: Descriptions | Any = Field(default=None, union_mode='left_to_right')
    view_options: list[ViewOption] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')
    amp_ids: list[AmpId] | Any = Field(None, alias='ampIds', union_mode='left_to_right')
    current_time: AwareDatetime | Any = Field(None, alias='currentTime', union_mode='left_to_right')
    kids_directed: bool | Any = Field(None, alias='kidsDirected', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta2 | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(None, alias='releaseYear', union_mode='left_to_right')
    savable: bool | Any = Field(default=None, union_mode='left_to_right')
    tracker_overrides: TrackerOverrides1 | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
    end_date: AwareDatetime | Any = Field(None, alias='endDate', union_mode='left_to_right')

class Search(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    confidence_score: int | float | Any = Field(None, alias='confidenceScore', union_mode='left_to_right')

class Features(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    search: Search | Any = Field(default=None, union_mode='left_to_right')

class Details(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    href: str | Any = Field(default=None, union_mode='left_to_right')

class ViewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content: Content | Any = Field(default=None, union_mode='left_to_right')
    features: Features | Any = Field(default=None, union_mode='left_to_right')
    details: Details | Any = Field(default=None, union_mode='left_to_right')

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    content_type: str | Any = Field(None, alias='content-type', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    tracker_overrides: TrackerOverrides | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
    view: list[ViewItem] | Any = Field(default=None, union_mode='left_to_right')
    trace_id: UUID | Any = Field(None, alias='traceId', union_mode='left_to_right')
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
