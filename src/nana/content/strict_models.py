from datetime import datetime
from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, Field

class DetailPoster(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class DetailBackground(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_poster: DetailPoster = Field(..., alias='detailPoster')
    detail_background: DetailBackground = Field(..., alias='detailBackground')

class Field100(BaseModel):
    model_config = ConfigDict(defer_build=True)
    size: int
    text: str

class Descriptions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_100: Field100 | None = Field(None, alias='100')

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str

class Meta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class StagingWindow(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start_time: int = Field(..., alias='startTime')
    end_time: int = Field(..., alias='endTime')

class ProviderDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    is_available: bool = Field(..., alias='isAvailable')
    index_source: str = Field(..., alias='indexSource')
    images: list[Image]
    description: str
    language: str
    is_private: bool = Field(..., alias='isPrivate')
    type: str
    title: str
    descriptions: dict[str, Any]
    unlocked: bool
    searchable: bool
    tags: list[None]
    use_provider_descriptions: bool = Field(..., alias='useProviderDescriptions')
    index_type: str = Field(..., alias='indexType')
    meta: Meta
    channel_store_code: str = Field(..., alias='channelStoreCode')
    regions_images: list[None] = Field(..., alias='regionsImages')
    default_program_locale: str | None = Field(None, alias='defaultProgramLocale')
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')
    short_description: str | None = Field(None, alias='shortDescription')
    staging_window: StagingWindow | None = Field(None, alias='stagingWindow')

class AudioTrack(BaseModel):
    model_config = ConfigDict(defer_build=True)
    language: str
    iso639_part1: str = Field(..., alias='iso639Part1')
    label: str
    type: str | None = None

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    pid: UUID

class DrmAuthentication(BaseModel):
    model_config = ConfigDict(defer_build=True)
    drm_content_provider: str = Field(..., alias='drmContentProvider')
    data: Data

class Video(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_type: str = Field(..., alias='videoType')
    drm_authentication: DrmAuthentication = Field(..., alias='drmAuthentication')
    url: str
    quality: str

class TrickPlayFile(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    quality: str

class Caption(BaseModel):
    model_config = ConfigDict(defer_build=True)
    language: str
    iso639_part1: str = Field(..., alias='iso639Part1')
    label: str
    caption_type: str = Field(..., alias='captionType')
    url: str

class Media(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: list[AudioTrack] = Field(..., alias='audioTracks')
    duration: int
    ad_breaks: list[time] | None = Field(None, alias='adBreaks')
    original_audio_language: str = Field(..., alias='originalAudioLanguage')
    videos: list[Video]
    trick_play_files: list[TrickPlayFile] = Field(..., alias='trickPlayFiles')
    captions: list[Caption]
    validity_end_time: datetime = Field(None, alias='validityEndTime')
    validity_start_time: datetime = Field(None, alias='validityStartTime')

class ViewOption(BaseModel):
    model_config = ConfigDict(defer_build=True)
    play_id: str = Field(..., alias='playId')
    license: str
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    media: Media
    provider_name: str = Field(..., alias='providerName')
    ads_provider_id: str = Field(..., alias='adsProviderId')
    provider_product_id: str | None = Field(None, alias='providerProductId')
    ads_content_id: str | None = Field(None, alias='adsContentId')

class Credit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    role: str
    name: str

class ClosingCredit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    heading: str
    credits: list[Credit]
    credit_type: str = Field(..., alias='creditType')

class CastAndCrew(BaseModel):
    model_config = ConfigDict(defer_build=True)
    closing_credits: list[ClosingCredit] = Field(..., alias='closingCredits')
    title: str

class ImageMap1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_poster: DetailPoster = Field(..., alias='detailPoster')

class Meta1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Credit1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_map: ImageMap1 | None = Field(None, alias='imageMap')
    role: str
    meta: Meta1
    name: str
    person_id: UUID = Field(..., alias='personId')
    birth_date: date | None = Field(None, alias='birthDate')

class Meta2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID
    wid: UUID

class DrmAuthentication1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    drm_content_provider: str = Field(..., alias='drmContentProvider')
    data: Data

class Video1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_type: str = Field(..., alias='videoType')
    drm_authentication: DrmAuthentication1 = Field(..., alias='drmAuthentication')
    url: str
    quality: str

class Media1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: list[AudioTrack] = Field(..., alias='audioTracks')
    duration: int
    ad_breaks: list[time] | None = Field(None, alias='adBreaks')
    original_audio_language: str = Field(..., alias='originalAudioLanguage')
    videos: list[Video1]
    trick_play_files: list[TrickPlayFile] = Field(..., alias='trickPlayFiles')
    captions: list[Caption]

class PlaybackDetails(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    auto_play_next_url: str | None = Field(None, alias='autoPlayNextURL')

class Meta3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta3

class CreditCuePoint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    start: int
    end: int
    skippable: bool
    type: str
    credit_type: str | None = Field(None, alias='creditType')

class ViewOption1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    business_model: str = Field(..., alias='businessModel')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    has_media: bool = Field(..., alias='hasMedia')
    media: Media1
    date_added: AwareDatetime = Field(..., alias='dateAdded')
    provider_type: str = Field(..., alias='providerType')
    play_id: str = Field(..., alias='playId')
    playback_details: PlaybackDetails = Field(..., alias='playbackDetails')
    price: int
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails1 = Field(..., alias='providerDetails')
    currency: str
    provider_name: str = Field(..., alias='providerName')
    initial_available_time: AwareDatetime = Field(..., alias='initialAvailableTime')
    price_display: str = Field(..., alias='priceDisplay')
    staging_end_time: str | None = Field(None, alias='stagingEndTime')
    in4k: bool
    ads_provider_id: str = Field(..., alias='adsProviderId')
    tags: list[str]
    in_hd: bool = Field(..., alias='inHd')
    license: str
    is_dummy_play_id: bool = Field(..., alias='isDummyPlayId')
    credit_cue_points: list[CreditCuePoint] = Field(..., alias='creditCuePoints')
    staging_start_time: str | None = Field(None, alias='stagingStartTime')

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta2
    season_number: str = Field(..., alias='seasonNumber')
    episode_number: str = Field(..., alias='episodeNumber')
    view_options: list[ViewOption1] = Field(..., alias='viewOptions')

class Zone(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta3

class Image1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    is_primary: bool | None = Field(None, alias='isPrimary')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str

class Meta5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str
    cid: str

class CategoryObject(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kids_appropriate: bool | None = Field(None, alias='kidsAppropriate')
    is_available: bool = Field(..., alias='isAvailable')
    index_source: str = Field(..., alias='indexSource')
    is_featured_row_eligible: bool | None = Field(None, alias='isFeaturedRowEligible')
    language: str
    browsable: bool | None = None
    requires_user_info: bool = Field(..., alias='requiresUserInfo')
    type: str
    title: str
    descriptions: dict[str, Any]
    view_options: list[None] | None = Field(None, alias='viewOptions')
    enabled: bool | None = None
    mvpd_livefeeds: list[None] | None = Field(None, alias='mvpdLivefeeds')
    recent_season_first: bool | None = Field(None, alias='recentSeasonFirst')
    zone: Zone | None = None
    kids_directed: bool | None = Field(None, alias='kidsDirected')
    genres: list[None]
    extra: str | None = None
    zone_id: str | None = Field(None, alias='zoneId')
    channel_store_code: str = Field(..., alias='channelStoreCode')
    release_year: int | None = Field(None, alias='releaseYear')
    savable: bool
    content_rating_class: int | None = Field(None, alias='contentRatingClass')
    images: list[Image1]
    editorially_generated: bool = Field(..., alias='editoriallyGenerated')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    start_year: str | None = Field(None, alias='startYear')
    searchable: bool | None = None
    reverse_chronological: bool | None = Field(None, alias='reverseChronological')
    meta: Meta5
    genre_appropriate: bool = Field(..., alias='genreAppropriate')
    sub_type: str = Field(..., alias='subType')

class ParentalRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    code: str
    rating_source: str = Field(..., alias='ratingSource')
    rating_level: int = Field(..., alias='ratingLevel')

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

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image3
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: datetime = Field(..., alias='validityEndTime')
    validity_start_time: datetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str
    text_color: str = Field(..., alias='textColor')

class Grid(BaseModel):
    model_config = ConfigDict(defer_build=True)
    bottom_left: list[BottomLeftItem] = Field(..., alias='bottom-left')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image3
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: datetime = Field(..., alias='validityEndTime')
    validity_start_time: datetime = Field(..., alias='validityStartTime')
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
    grid: Grid | None = None
    detail_screen: DetailScreen | None = Field(None, alias='detailScreen')

class Meta6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID

class Series(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta6
    title: str

class Meta7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_server_data: str

class Meta8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scope: str | None = None
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID

class Meta9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scope: str | None = None
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Series1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta9
    title: str

class Next(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta8
    series: Series1 | None = None

class ImageMap2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    detail_background: DetailBackground = Field(..., alias='detailBackground')

class Meta10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Credit2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    role: str
    meta: Meta10
    name: str
    person_id: UUID = Field(..., alias='personId')
    birth_date: date | None = Field(None, alias='birthDate')

class Meta11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str
    sid: str
    has_view_options: bool | None = Field(None, alias='hasViewOptions')

class Grid1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: Grid1

class Image5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    is_primary: bool | None = Field(None, alias='isPrimary')
    roku_id: str | None = Field(None, alias='rokuId')

class Meta12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID
    wid: UUID

class Image6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image6
    title: str

class Indicators1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_badge: ProviderBadge1 = Field(..., alias='providerBadge')

class Meta13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta13

class Media2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    duration: int

class ViewOption2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails2 = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    media: Media2

class Episode1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    current_time: AwareDatetime = Field(..., alias='currentTime')
    image_map: ImageMap3 = Field(..., alias='imageMap')
    images: list[Image5]
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    meta: Meta12
    description: str
    season_number: str = Field(..., alias='seasonNumber')
    title: str
    indicators: Indicators1
    episode_number: str = Field(..., alias='episodeNumber')
    view_options: list[ViewOption2] = Field(..., alias='viewOptions')

class Credit3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    role: str
    name: str

class ClosingCredit1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    heading: str
    credits: list[Credit3]
    credit_type: str = Field(..., alias='creditType')

class CastAndCrew1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    closing_credits: list[ClosingCredit1] = Field(..., alias='closingCredits')
    title: str

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_map: ImageMap2 | None = Field(None, alias='imageMap')
    credits: list[Credit2] | None = None
    meta: Meta11
    season_number: str | None = Field(None, alias='seasonNumber')
    title: str | None = None
    descriptions: dict[str, Any] | None = None
    release_year: int | None = Field(None, alias='releaseYear')
    episodes: list[Episode1] | None = None
    cast_and_crew: CastAndCrew1 | None = Field(None, alias='castAndCrew')

class ImageMap4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    grid: Grid1

class Image7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    is_primary: bool | None = Field(None, alias='isPrimary')
    roku_id: str | None = Field(None, alias='rokuId')

class Meta15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Image8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image: Image8
    title: str

class Indicators2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_badge: ProviderBadge2 = Field(..., alias='providerBadge')

class Meta16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta16

class ViewOption3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails3 = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    media: Media2

class Episode2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    current_time: AwareDatetime = Field(..., alias='currentTime')
    image_map: ImageMap4 = Field(..., alias='imageMap')
    images: list[Image7]
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    meta: Meta15
    description: str
    season_number: str = Field(..., alias='seasonNumber')
    title: str
    indicators: Indicators2
    episode_number: str = Field(..., alias='episodeNumber')
    view_options: list[ViewOption3] = Field(..., alias='viewOptions')

class Season1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta13
    episodes: list[Episode2]

class ContentModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_map: ImageMap = Field(..., alias='imageMap')
    type: str
    title: str
    descriptions: Descriptions
    view_options: list[ViewOption] = Field(..., alias='viewOptions')
    language_dialog_body: str = Field(..., alias='languageDialogBody')
    cast_and_crew: CastAndCrew | None = Field(None, alias='castAndCrew')
    credits: list[Credit1]
    kids_directed: bool = Field(..., alias='kidsDirected')
    genres: list[str]
    release_year: int = Field(..., alias='releaseYear')
    savable: bool
    episodes: list[Episode] | None = None
    category_objects: list[CategoryObject] = Field(..., alias='categoryObjects')
    content_rating_class: int = Field(..., alias='contentRatingClass')
    save_list_last_interaction_time: int = Field(..., alias='saveListLastInteractionTime')
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    admin_include: dict[str, Any] = Field(..., alias='adminInclude')
    parental_ratings: list[ParentalRating] = Field(..., alias='parentalRatings')
    season_number: str | None = Field(None, alias='seasonNumber')
    indicators: Indicators
    reverse_chronological: bool = Field(..., alias='reverseChronological')
    current_time: AwareDatetime = Field(..., alias='currentTime')
    series: Series | None = None
    meta: Meta7
    tracker_overrides: TrackerOverrides = Field(..., alias='trackerOverrides')
    trace_id: UUID = Field(..., alias='traceId')
    next: Next | None = None
    description: str | None = None
    seasons: list[Season] | None = None
    run_time_seconds: int | None = Field(None, alias='runTimeSeconds')
    episode_number: str | None = Field(None, alias='episodeNumber')
    season: Season1 | None = None
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
