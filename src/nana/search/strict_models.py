from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, Field

class Meta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href: str
    id: str
    media_type: str = Field(..., alias='mediaType')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(defer_build=True)
    collection_id: str
    query_params: str
    collection_params: str

class Grid(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')

class ImageMap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: Grid

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    tier: str
    provider_id: str | None = Field(None, alias='providerId')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    roku_id: str | None = Field(None, alias='rokuId')
    is_primary: bool | None = Field(None, alias='isPrimary')

class ParentalRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str

class Image1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image1
    title: str

class Image2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image2
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str
    text_color: str = Field(..., alias='textColor')

class Grid1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bottom_left: list[BottomLeftItem] = Field(..., alias='bottom-left')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image2
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str
    text_color: str = Field(..., alias='textColor')

class DetailScreen(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bottom_left: list[BottomLeftItem1] = Field(..., alias='bottom-left')

class Indicators(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_badge: ProviderBadge = Field(..., alias='providerBadge')
    grid: Grid1
    detail_screen: DetailScreen = Field(..., alias='detailScreen')

class Field100(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size: int
    text: str

class Descriptions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_100: Field100 | None = Field(None, alias='100')

class Meta1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta1
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')

class ViewOption(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails = Field(..., alias='providerDetails')
    provider_product_id: str | None = Field(None, alias='providerProductId')

class AmpId(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    id: str

class Meta2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str | None = None
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')

class TrackerOverrides1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_server_data: str

class Meta3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    sid: str

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta3

class Content(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class Search(BaseModel):
    model_config = ConfigDict(defer_build=True)
    confidence_score: int | float = Field(..., alias='confidenceScore')

class Features(BaseModel):
    model_config = ConfigDict(defer_build=True)
    search: Search

class Details(BaseModel):
    model_config = ConfigDict(defer_build=True)
    href: str

class ViewItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content: Content
    features: Features
    details: Details

class SearchModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta
    type: str
    content_type: str = Field(..., alias='content-type')
    title: str
    tracker_overrides: TrackerOverrides = Field(..., alias='trackerOverrides')
    view: list[ViewItem]
    trace_id: UUID = Field(..., alias='traceId')
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
