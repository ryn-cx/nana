from datetime import datetime
from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

class DetailPoster(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class DetailBackground(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ImageMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_poster: DetailPoster | Any = Field(None, alias='detailPoster', union_mode='left_to_right')
    detail_background: DetailBackground | Any = Field(None, alias='detailBackground', union_mode='left_to_right')

class Field100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    size: int | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Descriptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_100: Field100 | Any = Field(None, alias='100', union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    tier: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class StagingWindow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start_time: int | Any = Field(None, alias='startTime', union_mode='left_to_right')
    end_time: int | Any = Field(None, alias='endTime', union_mode='left_to_right')

class ProviderDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    index_source: str | Any = Field(None, alias='indexSource', union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    language: str | Any = Field(default=None, union_mode='left_to_right')
    is_private: bool | Any = Field(None, alias='isPrivate', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    descriptions: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    unlocked: bool | Any = Field(default=None, union_mode='left_to_right')
    searchable: bool | Any = Field(default=None, union_mode='left_to_right')
    tags: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    use_provider_descriptions: bool | Any = Field(None, alias='useProviderDescriptions', union_mode='left_to_right')
    index_type: str | Any = Field(None, alias='indexType', union_mode='left_to_right')
    meta: Meta | Any = Field(default=None, union_mode='left_to_right')
    channel_store_code: str | Any = Field(None, alias='channelStoreCode', union_mode='left_to_right')
    regions_images: list[Any] | Any = Field(None, alias='regionsImages', union_mode='left_to_right')
    default_program_locale: str | Any = Field(None, alias='defaultProgramLocale', union_mode='left_to_right')
    provider_product_ids: list[str] | Any = Field(None, alias='providerProductIds', union_mode='left_to_right')
    short_description: str | Any = Field(None, alias='shortDescription', union_mode='left_to_right')
    staging_window: StagingWindow | Any = Field(None, alias='stagingWindow', union_mode='left_to_right')

class AudioTrack(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    language: str | Any = Field(default=None, union_mode='left_to_right')
    iso639_part1: str | Any = Field(None, alias='iso639Part1', union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    pid: UUID | Any = Field(default=None, union_mode='left_to_right')

class DrmAuthentication(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    drm_content_provider: str | Any = Field(None, alias='drmContentProvider', union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Video(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_type: str | Any = Field(None, alias='videoType', union_mode='left_to_right')
    drm_authentication: DrmAuthentication | Any = Field(None, alias='drmAuthentication', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    quality: str | Any = Field(default=None, union_mode='left_to_right')

class TrickPlayFile(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    quality: str | Any = Field(default=None, union_mode='left_to_right')

class Caption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    language: str | Any = Field(default=None, union_mode='left_to_right')
    iso639_part1: str | Any = Field(None, alias='iso639Part1', union_mode='left_to_right')
    label: str | Any = Field(default=None, union_mode='left_to_right')
    caption_type: str | Any = Field(None, alias='captionType', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')

class Media(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: list[AudioTrack] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    ad_breaks: list[time] | Any = Field(None, alias='adBreaks', union_mode='left_to_right')
    original_audio_language: str | Any = Field(None, alias='originalAudioLanguage', union_mode='left_to_right')
    videos: list[Video] | Any = Field(default=None, union_mode='left_to_right')
    trick_play_files: list[TrickPlayFile] | Any = Field(None, alias='trickPlayFiles', union_mode='left_to_right')
    captions: list[Caption] | Any = Field(default=None, union_mode='left_to_right')
    validity_end_time: datetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: datetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')

class ViewOption(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    play_id: str | Any = Field(None, alias='playId', union_mode='left_to_right')
    license: str | Any = Field(default=None, union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_details: ProviderDetails | Any = Field(None, alias='providerDetails', union_mode='left_to_right')
    is_unlocked: bool | Any = Field(None, alias='isUnlocked', union_mode='left_to_right')
    media: Media | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(None, alias='providerName', union_mode='left_to_right')
    ads_provider_id: str | Any = Field(None, alias='adsProviderId', union_mode='left_to_right')
    provider_product_id: str | Any = Field(None, alias='providerProductId', union_mode='left_to_right')
    ads_content_id: str | Any = Field(None, alias='adsContentId', union_mode='left_to_right')

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    role: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class ClosingCredit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    heading: str | Any = Field(default=None, union_mode='left_to_right')
    credits: list[Credit] | Any = Field(default=None, union_mode='left_to_right')
    credit_type: str | Any = Field(None, alias='creditType', union_mode='left_to_right')

class CastAndCrew(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    closing_credits: list[ClosingCredit] | Any = Field(None, alias='closingCredits', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class ImageMap1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_poster: DetailPoster | Any = Field(None, alias='detailPoster', union_mode='left_to_right')

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class Credit1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap1 | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    role: str | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta1 | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    person_id: UUID | Any = Field(None, alias='personId', union_mode='left_to_right')
    birth_date: date | Any = Field(None, alias='birthDate', union_mode='left_to_right')

class Meta2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | Any = Field(default=None, union_mode='left_to_right')
    wid: UUID | Any = Field(default=None, union_mode='left_to_right')

class DrmAuthentication1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    drm_content_provider: str | Any = Field(None, alias='drmContentProvider', union_mode='left_to_right')
    data: Data | Any = Field(default=None, union_mode='left_to_right')

class Video1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_type: str | Any = Field(None, alias='videoType', union_mode='left_to_right')
    drm_authentication: DrmAuthentication1 | Any = Field(None, alias='drmAuthentication', union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    quality: str | Any = Field(default=None, union_mode='left_to_right')

class Media1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: list[AudioTrack] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    duration: int | Any = Field(default=None, union_mode='left_to_right')
    ad_breaks: list[time] | Any = Field(None, alias='adBreaks', union_mode='left_to_right')
    original_audio_language: str | Any = Field(None, alias='originalAudioLanguage', union_mode='left_to_right')
    videos: list[Video1] | Any = Field(default=None, union_mode='left_to_right')
    trick_play_files: list[TrickPlayFile] | Any = Field(None, alias='trickPlayFiles', union_mode='left_to_right')
    captions: list[Caption] | Any = Field(default=None, union_mode='left_to_right')

class PlaybackDetails(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    auto_play_next_url: str | Any = Field(None, alias='autoPlayNextURL', union_mode='left_to_right')

class Meta3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_view_options: bool | Any = Field(None, alias='hasViewOptions', union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class ProviderDetails1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta3 | Any = Field(default=None, union_mode='left_to_right')

class CreditCuePoint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    start: int | Any = Field(default=None, union_mode='left_to_right')
    end: int | Any = Field(default=None, union_mode='left_to_right')
    skippable: bool | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    credit_type: str | Any = Field(None, alias='creditType', union_mode='left_to_right')

class ViewOption1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    business_model: str | Any = Field(None, alias='businessModel', union_mode='left_to_right')
    is_unlocked: bool | Any = Field(None, alias='isUnlocked', union_mode='left_to_right')
    has_media: bool | Any = Field(None, alias='hasMedia', union_mode='left_to_right')
    media: Media1 | Any = Field(default=None, union_mode='left_to_right')
    date_added: AwareDatetime | Any = Field(None, alias='dateAdded', union_mode='left_to_right')
    provider_type: str | Any = Field(None, alias='providerType', union_mode='left_to_right')
    play_id: str | Any = Field(None, alias='playId', union_mode='left_to_right')
    playback_details: PlaybackDetails | Any = Field(None, alias='playbackDetails', union_mode='left_to_right')
    price: int | Any = Field(default=None, union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_details: ProviderDetails1 | Any = Field(None, alias='providerDetails', union_mode='left_to_right')
    currency: str | Any = Field(default=None, union_mode='left_to_right')
    provider_name: str | Any = Field(None, alias='providerName', union_mode='left_to_right')
    initial_available_time: AwareDatetime | Any = Field(None, alias='initialAvailableTime', union_mode='left_to_right')
    price_display: str | Any = Field(None, alias='priceDisplay', union_mode='left_to_right')
    staging_end_time: str | Any = Field(None, alias='stagingEndTime', union_mode='left_to_right')
    in4k: bool | Any = Field(default=None, union_mode='left_to_right')
    ads_provider_id: str | Any = Field(None, alias='adsProviderId', union_mode='left_to_right')
    tags: list[str] | Any = Field(default=None, union_mode='left_to_right')
    in_hd: bool | Any = Field(None, alias='inHd', union_mode='left_to_right')
    license: str | Any = Field(default=None, union_mode='left_to_right')
    is_dummy_play_id: bool | Any = Field(None, alias='isDummyPlayId', union_mode='left_to_right')
    credit_cue_points: list[CreditCuePoint] | Any = Field(None, alias='creditCuePoints', union_mode='left_to_right')
    staging_start_time: str | Any = Field(None, alias='stagingStartTime', union_mode='left_to_right')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta2 | Any = Field(default=None, union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    view_options: list[ViewOption1] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')

class Zone(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta3 | Any = Field(default=None, union_mode='left_to_right')

class Image1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    is_primary: bool | Any = Field(None, alias='isPrimary', union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class Meta5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_view_options: bool | Any = Field(None, alias='hasViewOptions', union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    cid: str | Any = Field(default=None, union_mode='left_to_right')

class CategoryObject(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    kids_appropriate: bool | Any = Field(None, alias='kidsAppropriate', union_mode='left_to_right')
    is_available: bool | Any = Field(None, alias='isAvailable', union_mode='left_to_right')
    index_source: str | Any = Field(None, alias='indexSource', union_mode='left_to_right')
    is_featured_row_eligible: bool | Any = Field(None, alias='isFeaturedRowEligible', union_mode='left_to_right')
    language: str | Any = Field(default=None, union_mode='left_to_right')
    browsable: bool | Any = Field(default=None, union_mode='left_to_right')
    requires_user_info: bool | Any = Field(None, alias='requiresUserInfo', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    descriptions: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    view_options: list[Any] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')
    enabled: bool | Any = Field(default=None, union_mode='left_to_right')
    mvpd_livefeeds: list[Any] | Any = Field(None, alias='mvpdLivefeeds', union_mode='left_to_right')
    recent_season_first: bool | Any = Field(None, alias='recentSeasonFirst', union_mode='left_to_right')
    zone: Zone | Any = Field(default=None, union_mode='left_to_right')
    kids_directed: bool | Any = Field(None, alias='kidsDirected', union_mode='left_to_right')
    genres: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    extra: str | Any = Field(default=None, union_mode='left_to_right')
    zone_id: str | Any = Field(None, alias='zoneId', union_mode='left_to_right')
    channel_store_code: str | Any = Field(None, alias='channelStoreCode', union_mode='left_to_right')
    release_year: int | Any = Field(None, alias='releaseYear', union_mode='left_to_right')
    savable: bool | Any = Field(default=None, union_mode='left_to_right')
    content_rating_class: int | Any = Field(None, alias='contentRatingClass', union_mode='left_to_right')
    images: list[Image1] | Any = Field(default=None, union_mode='left_to_right')
    editorially_generated: bool | Any = Field(None, alias='editoriallyGenerated', union_mode='left_to_right')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    start_year: str | Any = Field(None, alias='startYear', union_mode='left_to_right')
    searchable: bool | Any = Field(default=None, union_mode='left_to_right')
    reverse_chronological: bool | Any = Field(None, alias='reverseChronological', union_mode='left_to_right')
    meta: Meta5 | Any = Field(default=None, union_mode='left_to_right')
    genre_appropriate: bool | Any = Field(None, alias='genreAppropriate', union_mode='left_to_right')
    sub_type: str | Any = Field(None, alias='subType', union_mode='left_to_right')

class ParentalRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    code: str | Any = Field(default=None, union_mode='left_to_right')
    rating_source: str | Any = Field(None, alias='ratingSource', union_mode='left_to_right')
    rating_level: int | Any = Field(None, alias='ratingLevel', union_mode='left_to_right')

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

class BottomLeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image3 | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: datetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: datetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    audioguide: str | Any = Field(default=None, union_mode='left_to_right')
    text_color: str | Any = Field(None, alias='textColor', union_mode='left_to_right')

class Grid(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bottom_left: list[BottomLeftItem] | Any = Field(None, alias='bottom-left', union_mode='left_to_right')

class BottomLeftItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_color: list[str] | Any = Field(None, alias='badgeColor', union_mode='left_to_right')
    image: Image3 | Any = Field(default=None, union_mode='left_to_right')
    badge_type: str | Any = Field(None, alias='badgeType', union_mode='left_to_right')
    validity_end_time: datetime | Any = Field(None, alias='validityEndTime', union_mode='left_to_right')
    validity_start_time: datetime | Any = Field(None, alias='validityStartTime', union_mode='left_to_right')
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
    grid: Grid | Any = Field(default=None, union_mode='left_to_right')
    detail_screen: DetailScreen | Any = Field(None, alias='detailScreen', union_mode='left_to_right')

class Meta6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | Any = Field(default=None, union_mode='left_to_right')

class Series(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta6 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Meta7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | str | Any = Field(default=None, union_mode='left_to_right')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | Any = Field(default=None, union_mode='left_to_right')

class Meta8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scope: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | Any = Field(default=None, union_mode='left_to_right')

class Meta9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scope: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class Series1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta9 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Next(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta8 | Any = Field(default=None, union_mode='left_to_right')
    series: Series1 | Any = Field(default=None, union_mode='left_to_right')

class ImageMap2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    detail_background: DetailBackground | Any = Field(None, alias='detailBackground', union_mode='left_to_right')

class Meta10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    has_view_options: bool | Any = Field(None, alias='hasViewOptions', union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class Credit2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    role: str | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta10 | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    person_id: UUID | Any = Field(None, alias='personId', union_mode='left_to_right')
    birth_date: date | Any = Field(None, alias='birthDate', union_mode='left_to_right')

class Meta11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: str | Any = Field(default=None, union_mode='left_to_right')
    has_view_options: bool | Any = Field(None, alias='hasViewOptions', union_mode='left_to_right')

class Grid1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ImageMap3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid1 | Any = Field(default=None, union_mode='left_to_right')

class Image5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    tier: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    is_primary: bool | Any = Field(None, alias='isPrimary', union_mode='left_to_right')
    roku_id: str | Any = Field(None, alias='rokuId', union_mode='left_to_right')

class Meta12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')
    sid: UUID | Any = Field(default=None, union_mode='left_to_right')
    wid: UUID | Any = Field(default=None, union_mode='left_to_right')

class Image6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ProviderBadge1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image6 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Indicators1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_badge: ProviderBadge1 | Any = Field(None, alias='providerBadge', union_mode='left_to_right')

class Meta13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class ProviderDetails2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta13 | Any = Field(default=None, union_mode='left_to_right')

class Media2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    duration: int | Any = Field(default=None, union_mode='left_to_right')

class ViewOption2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_details: ProviderDetails2 | Any = Field(None, alias='providerDetails', union_mode='left_to_right')
    is_unlocked: bool | Any = Field(None, alias='isUnlocked', union_mode='left_to_right')
    media: Media2 | Any = Field(default=None, union_mode='left_to_right')

class Episode1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_time: AwareDatetime | Any = Field(None, alias='currentTime', union_mode='left_to_right')
    image_map: ImageMap3 | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    images: list[Image5] | Any = Field(default=None, union_mode='left_to_right')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    meta: Meta12 | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    indicators: Indicators1 | Any = Field(default=None, union_mode='left_to_right')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    view_options: list[ViewOption2] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')

class Credit3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    role: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class ClosingCredit1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    heading: str | Any = Field(default=None, union_mode='left_to_right')
    credits: list[Credit3] | Any = Field(default=None, union_mode='left_to_right')
    credit_type: str | Any = Field(None, alias='creditType', union_mode='left_to_right')

class CastAndCrew1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    closing_credits: list[ClosingCredit1] | Any = Field(None, alias='closingCredits', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap2 | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    credits: list[Credit2] | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta11 | Any = Field(default=None, union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    descriptions: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(None, alias='releaseYear', union_mode='left_to_right')
    episodes: list[Episode1] | Any = Field(default=None, union_mode='left_to_right')
    cast_and_crew: CastAndCrew1 | Any = Field(None, alias='castAndCrew', union_mode='left_to_right')

class ImageMap4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    grid: Grid1 | Any = Field(default=None, union_mode='left_to_right')

class Image7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    tier: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    is_primary: bool | Any = Field(None, alias='isPrimary', union_mode='left_to_right')
    roku_id: str | Any = Field(None, alias='rokuId', union_mode='left_to_right')

class Meta15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class Image8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    path: str | Any = Field(default=None, union_mode='left_to_right')
    aspect_ratio: str | Any = Field(None, alias='aspectRatio', union_mode='left_to_right')

class ProviderBadge2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image: Image8 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class Indicators2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_badge: ProviderBadge2 | Any = Field(None, alias='providerBadge', union_mode='left_to_right')

class Meta16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    href_v2: str | Any = Field(None, alias='hrefV2', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')
    href: str | Any = Field(default=None, union_mode='left_to_right')

class ProviderDetails3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta16 | Any = Field(default=None, union_mode='left_to_right')

class ViewOption3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_details: ProviderDetails3 | Any = Field(None, alias='providerDetails', union_mode='left_to_right')
    is_unlocked: bool | Any = Field(None, alias='isUnlocked', union_mode='left_to_right')
    media: Media2 | Any = Field(default=None, union_mode='left_to_right')

class Episode2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_time: AwareDatetime | Any = Field(None, alias='currentTime', union_mode='left_to_right')
    image_map: ImageMap4 | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    images: list[Image7] | Any = Field(default=None, union_mode='left_to_right')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    meta: Meta15 | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    indicators: Indicators2 | Any = Field(default=None, union_mode='left_to_right')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    view_options: list[ViewOption3] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')

class Season1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta13 | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Episode2] | Any = Field(default=None, union_mode='left_to_right')

class ContentModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_map: ImageMap | Any = Field(None, alias='imageMap', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    descriptions: Descriptions | Any = Field(default=None, union_mode='left_to_right')
    view_options: list[ViewOption] | Any = Field(None, alias='viewOptions', union_mode='left_to_right')
    language_dialog_body: str | Any = Field(None, alias='languageDialogBody', union_mode='left_to_right')
    cast_and_crew: CastAndCrew | Any = Field(None, alias='castAndCrew', union_mode='left_to_right')
    credits: list[Credit1] | Any = Field(default=None, union_mode='left_to_right')
    kids_directed: bool | Any = Field(None, alias='kidsDirected', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(None, alias='releaseYear', union_mode='left_to_right')
    savable: bool | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Episode] | Any = Field(default=None, union_mode='left_to_right')
    category_objects: list[CategoryObject] | Any = Field(None, alias='categoryObjects', union_mode='left_to_right')
    content_rating_class: int | Any = Field(None, alias='contentRatingClass', union_mode='left_to_right')
    save_list_last_interaction_time: int | Any = Field(None, alias='saveListLastInteractionTime', union_mode='left_to_right')
    release_date: AwareDatetime | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    admin_include: dict[str, Any] | Any = Field(None, alias='adminInclude', union_mode='left_to_right')
    parental_ratings: list[ParentalRating] | Any = Field(None, alias='parentalRatings', union_mode='left_to_right')
    season_number: str | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    indicators: Indicators | Any = Field(default=None, union_mode='left_to_right')
    reverse_chronological: bool | Any = Field(None, alias='reverseChronological', union_mode='left_to_right')
    current_time: AwareDatetime | Any = Field(None, alias='currentTime', union_mode='left_to_right')
    series: Series | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta7 | Any = Field(default=None, union_mode='left_to_right')
    tracker_overrides: TrackerOverrides | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
    trace_id: UUID | Any = Field(None, alias='traceId', union_mode='left_to_right')
    next: Next | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
    run_time_seconds: int | Any = Field(None, alias='runTimeSeconds', union_mode='left_to_right')
    episode_number: str | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    season: Season1 | Any = Field(default=None, union_mode='left_to_right')
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
