from datetime import datetime
from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID
from datetime import date, time

class DetailPoster(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class DetailBackground(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ImageMap(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_poster: DetailPoster | None = Field(None, alias='detailPoster')
    detail_background: DetailBackground | None = Field(None, alias='detailBackground')

class Field100(BaseModel):
    model_config = ConfigDict(extra='ignore')
    size: int | None = None
    text: str | None = None

class Descriptions(BaseModel):
    model_config = ConfigDict(extra='ignore')
    field_100: Field100 | None = Field(None, alias='100')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    tier: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    type: str | None = None

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None

class StagingWindow(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start_time: int | None = Field(None, alias='startTime')
    end_time: int | None = Field(None, alias='endTime')

class ProviderDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    is_available: bool | None = Field(None, alias='isAvailable')
    index_source: str | None = Field(None, alias='indexSource')
    images: list[Image] | None = None
    description: str | None = None
    language: str | None = None
    is_private: bool | None = Field(None, alias='isPrivate')
    type: str | None = None
    title: str | None = None
    descriptions: dict[str, Any] | None = None
    unlocked: bool | None = None
    searchable: bool | None = None
    tags: list[Any] | None = None
    use_provider_descriptions: bool | None = Field(None, alias='useProviderDescriptions')
    index_type: str | None = Field(None, alias='indexType')
    meta: Meta | None = None
    channel_store_code: str | None = Field(None, alias='channelStoreCode')
    regions_images: list[Any] | None = Field(None, alias='regionsImages')
    default_program_locale: str | None = Field(None, alias='defaultProgramLocale')
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')
    short_description: str | None = Field(None, alias='shortDescription')
    staging_window: StagingWindow | None = Field(None, alias='stagingWindow')

class AudioTrack(BaseModel):
    model_config = ConfigDict(extra='ignore')
    language: str | None = None
    iso639_part1: str | None = Field(None, alias='iso639Part1')
    label: str | None = None
    type: str | None = None

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore')
    pid: UUID | None = None

class DrmAuthentication(BaseModel):
    model_config = ConfigDict(extra='ignore')
    drm_content_provider: str | None = Field(None, alias='drmContentProvider')
    data: Data | None = None

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_type: str | None = Field(None, alias='videoType')
    drm_authentication: DrmAuthentication | None = Field(None, alias='drmAuthentication')
    url: str | None = None
    quality: str | None = None

class TrickPlayFile(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    quality: str | None = None

class Caption(BaseModel):
    model_config = ConfigDict(extra='ignore')
    language: str | None = None
    iso639_part1: str | None = Field(None, alias='iso639Part1')
    label: str | None = None
    caption_type: str | None = Field(None, alias='captionType')
    url: str | None = None

class Media(BaseModel):
    model_config = ConfigDict(extra='ignore')
    audio_tracks: list[AudioTrack] | None = Field(None, alias='audioTracks')
    duration: int | None = None
    ad_breaks: list[time] | None = Field(None, alias='adBreaks')
    original_audio_language: str | None = Field(None, alias='originalAudioLanguage')
    videos: list[Video] | None = None
    trick_play_files: list[TrickPlayFile] | None = Field(None, alias='trickPlayFiles')
    captions: list[Caption] | None = None
    validity_end_time: datetime = Field(None, alias='validityEndTime')
    validity_start_time: datetime = Field(None, alias='validityStartTime')

class ViewOption(BaseModel):
    model_config = ConfigDict(extra='ignore')
    play_id: str | None = Field(None, alias='playId')
    license: str | None = None
    provider_id: str | None = Field(None, alias='providerId')
    provider_details: ProviderDetails | None = Field(None, alias='providerDetails')
    is_unlocked: bool | None = Field(None, alias='isUnlocked')
    media: Media | None = None
    provider_name: str | None = Field(None, alias='providerName')
    ads_provider_id: str | None = Field(None, alias='adsProviderId')
    provider_product_id: str | None = Field(None, alias='providerProductId')
    ads_content_id: str | None = Field(None, alias='adsContentId')

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore')
    role: str | None = None
    name: str | None = None

class ClosingCredit(BaseModel):
    model_config = ConfigDict(extra='ignore')
    heading: str | None = None
    credits: list[Credit] | None = None
    credit_type: str | None = Field(None, alias='creditType')

class CastAndCrew(BaseModel):
    model_config = ConfigDict(extra='ignore')
    closing_credits: list[ClosingCredit] | None = Field(None, alias='closingCredits')
    title: str | None = None

class ImageMap1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_poster: DetailPoster | None = Field(None, alias='detailPoster')

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None

class Credit1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_map: ImageMap1 | None = Field(None, alias='imageMap')
    role: str | None = None
    meta: Meta1 | None = None
    name: str | None = None
    person_id: UUID | None = Field(None, alias='personId')
    birth_date: date | None = Field(None, alias='birthDate')

class Meta2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None
    sid: UUID | None = None
    wid: UUID | None = None

class DrmAuthentication1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    drm_content_provider: str | None = Field(None, alias='drmContentProvider')
    data: Data | None = None

class Video1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    video_type: str | None = Field(None, alias='videoType')
    drm_authentication: DrmAuthentication1 | None = Field(None, alias='drmAuthentication')
    url: str | None = None
    quality: str | None = None

class Media1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    audio_tracks: list[AudioTrack] | None = Field(None, alias='audioTracks')
    duration: int | None = None
    ad_breaks: list[time] | None = Field(None, alias='adBreaks')
    original_audio_language: str | None = Field(None, alias='originalAudioLanguage')
    videos: list[Video1] | None = None
    trick_play_files: list[TrickPlayFile] | None = Field(None, alias='trickPlayFiles')
    captions: list[Caption] | None = None

class PlaybackDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')
    url: str | None = None
    auto_play_next_url: str | None = Field(None, alias='autoPlayNextURL')

class Meta3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    has_view_options: bool | None = Field(None, alias='hasViewOptions')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None

class ProviderDetails1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta3 | None = None

class CreditCuePoint(BaseModel):
    model_config = ConfigDict(extra='ignore')
    start: int | None = None
    end: int | None = None
    skippable: bool | None = None
    type: str | None = None
    credit_type: str | None = Field(None, alias='creditType')

class ViewOption1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    business_model: str | None = Field(None, alias='businessModel')
    is_unlocked: bool | None = Field(None, alias='isUnlocked')
    has_media: bool | None = Field(None, alias='hasMedia')
    media: Media1 | None = None
    date_added: AwareDatetime | None = Field(None, alias='dateAdded')
    provider_type: str | None = Field(None, alias='providerType')
    play_id: str | None = Field(None, alias='playId')
    playback_details: PlaybackDetails | None = Field(None, alias='playbackDetails')
    price: int | None = None
    provider_id: str | None = Field(None, alias='providerId')
    provider_details: ProviderDetails1 | None = Field(None, alias='providerDetails')
    currency: str | None = None
    provider_name: str | None = Field(None, alias='providerName')
    initial_available_time: AwareDatetime | None = Field(None, alias='initialAvailableTime')
    price_display: str | None = Field(None, alias='priceDisplay')
    staging_end_time: str | None = Field(None, alias='stagingEndTime')
    in4k: bool | None = None
    ads_provider_id: str | None = Field(None, alias='adsProviderId')
    tags: list[str] | None = None
    in_hd: bool | None = Field(None, alias='inHd')
    license: str | None = None
    is_dummy_play_id: bool | None = Field(None, alias='isDummyPlayId')
    credit_cue_points: list[CreditCuePoint] | None = Field(None, alias='creditCuePoints')
    staging_start_time: str | None = Field(None, alias='stagingStartTime')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta2 | None = None
    season_number: str | None = Field(None, alias='seasonNumber')
    episode_number: str | None = Field(None, alias='episodeNumber')
    view_options: list[ViewOption1] | None = Field(None, alias='viewOptions')

class Zone(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta3 | None = None

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    is_primary: bool | None = Field(None, alias='isPrimary')
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    type: str | None = None

class Meta5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    has_view_options: bool | None = Field(None, alias='hasViewOptions')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None
    cid: str | None = None

class CategoryObject(BaseModel):
    model_config = ConfigDict(extra='ignore')
    kids_appropriate: bool | None = Field(None, alias='kidsAppropriate')
    is_available: bool | None = Field(None, alias='isAvailable')
    index_source: str | None = Field(None, alias='indexSource')
    is_featured_row_eligible: bool | None = Field(None, alias='isFeaturedRowEligible')
    language: str | None = None
    browsable: bool | None = None
    requires_user_info: bool | None = Field(None, alias='requiresUserInfo')
    type: str | None = None
    title: str | None = None
    descriptions: dict[str, Any] | None = None
    view_options: list[Any] | None = Field(None, alias='viewOptions')
    enabled: bool | None = None
    mvpd_livefeeds: list[Any] | None = Field(None, alias='mvpdLivefeeds')
    recent_season_first: bool | None = Field(None, alias='recentSeasonFirst')
    zone: Zone | None = None
    kids_directed: bool | None = Field(None, alias='kidsDirected')
    genres: list[Any] | None = None
    extra: str | None = None
    zone_id: str | None = Field(None, alias='zoneId')
    channel_store_code: str | None = Field(None, alias='channelStoreCode')
    release_year: int | None = Field(None, alias='releaseYear')
    savable: bool | None = None
    content_rating_class: int | None = Field(None, alias='contentRatingClass')
    images: list[Image1] | None = None
    editorially_generated: bool | None = Field(None, alias='editoriallyGenerated')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    start_year: str | None = Field(None, alias='startYear')
    searchable: bool | None = None
    reverse_chronological: bool | None = Field(None, alias='reverseChronological')
    meta: Meta5 | None = None
    genre_appropriate: bool | None = Field(None, alias='genreAppropriate')
    sub_type: str | None = Field(None, alias='subType')

class ParentalRating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    code: str | None = None
    rating_source: str | None = Field(None, alias='ratingSource')
    rating_level: int | None = Field(None, alias='ratingLevel')

class Image2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ProviderBadge(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image2 | None = None
    title: str | None = None

class Image3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image3 | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: datetime = Field(None, alias='validityEndTime')
    validity_start_time: datetime = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    audioguide: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class Grid(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bottom_left: list[BottomLeftItem] | None = Field(None, alias='bottom-left')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    badge_color: list[str] | None = Field(None, alias='badgeColor')
    image: Image3 | None = None
    badge_type: str | None = Field(None, alias='badgeType')
    validity_end_time: datetime = Field(None, alias='validityEndTime')
    validity_start_time: datetime = Field(None, alias='validityStartTime')
    id: UUID | None = None
    text: str | None = None
    audioguide: str | None = None
    text_color: str | None = Field(None, alias='textColor')

class DetailScreen(BaseModel):
    model_config = ConfigDict(extra='ignore')
    bottom_left: list[BottomLeftItem1] | None = Field(None, alias='bottom-left')

class Indicators(BaseModel):
    model_config = ConfigDict(extra='ignore')
    provider_badge: ProviderBadge | None = Field(None, alias='providerBadge')
    grid: Grid | None = None
    detail_screen: DetailScreen | None = Field(None, alias='detailScreen')

class Meta6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None
    sid: UUID | None = None

class Series(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta6 | None = None
    title: str | None = None

class Meta7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | str | None = Field(default=None, union_mode='left_to_right')
    source: str | None = None
    href: str | None = None
    sid: UUID | str | None = Field(default=None, union_mode='left_to_right')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore')
    item_server_data: str | None = None

class Meta8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    scope: str | None = None
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None
    sid: UUID | None = None

class Meta9(BaseModel):
    model_config = ConfigDict(extra='ignore')
    scope: str | None = None
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None

class Series1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta9 | None = None
    title: str | None = None

class Next(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta8 | None = None
    series: Series1 | None = None

class ImageMap2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    detail_background: DetailBackground | None = Field(None, alias='detailBackground')

class Meta10(BaseModel):
    model_config = ConfigDict(extra='ignore')
    has_view_options: bool | None = Field(None, alias='hasViewOptions')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None

class Credit2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    role: str | None = None
    meta: Meta10 | None = None
    name: str | None = None
    person_id: UUID | None = Field(None, alias='personId')
    birth_date: date | None = Field(None, alias='birthDate')

class Meta11(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None
    sid: str | None = None
    has_view_options: bool | None = Field(None, alias='hasViewOptions')

class Grid1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ImageMap3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    grid: Grid1 | None = None

class Image5(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    tier: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    type: str | None = None
    is_primary: bool | None = Field(None, alias='isPrimary')
    roku_id: str | None = Field(None, alias='rokuId')

class Meta12(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None
    sid: UUID | None = None
    wid: UUID | None = None

class Image6(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ProviderBadge1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image6 | None = None
    title: str | None = None

class Indicators1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    provider_badge: ProviderBadge1 | None = Field(None, alias='providerBadge')

class Meta13(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None

class ProviderDetails2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta13 | None = None

class Media2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    duration: int | None = None

class ViewOption2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    provider_id: str | None = Field(None, alias='providerId')
    provider_details: ProviderDetails2 | None = Field(None, alias='providerDetails')
    is_unlocked: bool | None = Field(None, alias='isUnlocked')
    media: Media2 | None = None

class Episode1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    current_time: AwareDatetime | None = Field(None, alias='currentTime')
    image_map: ImageMap3 | None = Field(None, alias='imageMap')
    images: list[Image5] | None = None
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    meta: Meta12 | None = None
    description: str | None = None
    season_number: str | None = Field(None, alias='seasonNumber')
    title: str | None = None
    indicators: Indicators1 | None = None
    episode_number: str | None = Field(None, alias='episodeNumber')
    view_options: list[ViewOption2] | None = Field(None, alias='viewOptions')

class Credit3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    role: str | None = None
    name: str | None = None

class ClosingCredit1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    heading: str | None = None
    credits: list[Credit3] | None = None
    credit_type: str | None = Field(None, alias='creditType')

class CastAndCrew1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    closing_credits: list[ClosingCredit1] | None = Field(None, alias='closingCredits')
    title: str | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_map: ImageMap2 | None = Field(None, alias='imageMap')
    credits: list[Credit2] | None = None
    meta: Meta11 | None = None
    season_number: str | None = Field(None, alias='seasonNumber')
    title: str | None = None
    descriptions: dict[str, Any] | None = None
    release_year: int | None = Field(None, alias='releaseYear')
    episodes: list[Episode1] | None = None
    cast_and_crew: CastAndCrew1 | None = Field(None, alias='castAndCrew')

class ImageMap4(BaseModel):
    model_config = ConfigDict(extra='ignore')
    grid: Grid1 | None = None

class Image7(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    tier: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')
    type: str | None = None
    is_primary: bool | None = Field(None, alias='isPrimary')
    roku_id: str | None = Field(None, alias='rokuId')

class Meta15(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: UUID | None = None
    source: str | None = None
    href: str | None = None

class Image8(BaseModel):
    model_config = ConfigDict(extra='ignore')
    path: str | None = None
    aspect_ratio: str | None = Field(None, alias='aspectRatio')

class ProviderBadge2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image: Image8 | None = None
    title: str | None = None

class Indicators2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    provider_badge: ProviderBadge2 | None = Field(None, alias='providerBadge')

class Meta16(BaseModel):
    model_config = ConfigDict(extra='ignore')
    media_type: str | None = Field(None, alias='mediaType')
    href_v2: str | None = Field(None, alias='hrefV2')
    id: str | None = None
    source: str | None = None
    href: str | None = None

class ProviderDetails3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta16 | None = None

class ViewOption3(BaseModel):
    model_config = ConfigDict(extra='ignore')
    provider_id: str | None = Field(None, alias='providerId')
    provider_details: ProviderDetails3 | None = Field(None, alias='providerDetails')
    is_unlocked: bool | None = Field(None, alias='isUnlocked')
    media: Media2 | None = None

class Episode2(BaseModel):
    model_config = ConfigDict(extra='ignore')
    current_time: AwareDatetime | None = Field(None, alias='currentTime')
    image_map: ImageMap4 | None = Field(None, alias='imageMap')
    images: list[Image7] | None = None
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    meta: Meta15 | None = None
    description: str | None = None
    season_number: str | None = Field(None, alias='seasonNumber')
    title: str | None = None
    indicators: Indicators2 | None = None
    episode_number: str | None = Field(None, alias='episodeNumber')
    view_options: list[ViewOption3] | None = Field(None, alias='viewOptions')

class Season1(BaseModel):
    model_config = ConfigDict(extra='ignore')
    meta: Meta13 | None = None
    episodes: list[Episode2] | None = None

class ContentModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
    image_map: ImageMap | None = Field(None, alias='imageMap')
    type: str | None = None
    title: str | None = None
    descriptions: Descriptions | None = None
    view_options: list[ViewOption] | None = Field(None, alias='viewOptions')
    language_dialog_body: str | None = Field(None, alias='languageDialogBody')
    cast_and_crew: CastAndCrew | None = Field(None, alias='castAndCrew')
    credits: list[Credit1] | None = None
    kids_directed: bool | None = Field(None, alias='kidsDirected')
    genres: list[str] | None = None
    release_year: int | None = Field(None, alias='releaseYear')
    savable: bool | None = None
    episodes: list[Episode] | None = None
    category_objects: list[CategoryObject] | None = Field(None, alias='categoryObjects')
    content_rating_class: int | None = Field(None, alias='contentRatingClass')
    save_list_last_interaction_time: int | None = Field(None, alias='saveListLastInteractionTime')
    release_date: AwareDatetime | None = Field(None, alias='releaseDate')
    admin_include: dict[str, Any] | None = Field(None, alias='adminInclude')
    parental_ratings: list[ParentalRating] | None = Field(None, alias='parentalRatings')
    season_number: str | None = Field(None, alias='seasonNumber')
    indicators: Indicators | None = None
    reverse_chronological: bool | None = Field(None, alias='reverseChronological')
    current_time: AwareDatetime | None = Field(None, alias='currentTime')
    series: Series | None = None
    meta: Meta7 | None = None
    tracker_overrides: TrackerOverrides | None = Field(None, alias='trackerOverrides')
    trace_id: UUID | None = Field(None, alias='traceId')
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
