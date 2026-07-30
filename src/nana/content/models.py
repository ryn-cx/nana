from datetime import date, time
from typing import Any
from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field

class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    scope: str | None = None
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')

class Meta1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    scope: str | None = None
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Series(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta1
    title: str

class Next(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta
    series: Series | None = None

class DetailPoster(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')

class DetailBackground(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    roku_id: str | None = Field(None, alias='rokuId')

class ImageMap(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_poster: DetailPoster = Field(..., alias='detailPoster')
    detail_background: DetailBackground = Field(..., alias='detailBackground')

class Field100(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    size: int
    text: str

class Descriptions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_100: Field100 = Field(..., alias='100')

class Image(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    tier: str
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str

class Meta2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class StagingWindow(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    start_time: int = Field(..., alias='startTime')
    end_time: int = Field(..., alias='endTime')

class ProviderDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    is_available: bool = Field(..., alias='isAvailable')
    index_source: str = Field(..., alias='indexSource')
    images: list[Image]
    default_program_locale: str | None = Field(None, alias='defaultProgramLocale')
    provider_product_ids: list[str] | None = Field(None, alias='providerProductIds')
    description: str
    language: str
    short_description: str | None = Field(None, alias='shortDescription')
    is_private: bool = Field(..., alias='isPrivate')
    type: str
    title: str
    descriptions: dict[str, Any]
    unlocked: bool
    searchable: bool
    tags: list[None]
    use_provider_descriptions: bool = Field(..., alias='useProviderDescriptions')
    index_type: str = Field(..., alias='indexType')
    meta: Meta2
    channel_store_code: str = Field(..., alias='channelStoreCode')
    regions_images: list[None] = Field(..., alias='regionsImages')
    staging_window: StagingWindow | None = Field(None, alias='stagingWindow')

class AudioTrack(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    language: str
    iso639_part1: str = Field(..., alias='iso639Part1')
    label: str
    type: str | None = None

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    pid: UUID

class DrmAuthentication(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    drm_content_provider: str = Field(..., alias='drmContentProvider')
    data: Data

class Video(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_type: str = Field(..., alias='videoType')
    drm_authentication: DrmAuthentication = Field(..., alias='drmAuthentication')
    url: str
    quality: str

class TrickPlayFile(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    quality: str

class Caption(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    language: str
    iso639_part1: str = Field(..., alias='iso639Part1')
    label: str
    caption_type: str = Field(..., alias='captionType')
    url: str

class Media(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_tracks: list[AudioTrack] = Field(..., alias='audioTracks')
    duration: int
    ad_breaks: list[time] = Field(..., alias='adBreaks')
    original_audio_language: str | None = Field(None, alias='originalAudioLanguage')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    videos: list[Video]
    trick_play_files: list[TrickPlayFile] = Field(..., alias='trickPlayFiles')
    captions: list[Caption]

class ViewOption(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    play_id: str = Field(..., alias='playId')
    license: str
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    media: Media
    provider_product_id: str | None = Field(None, alias='providerProductId')
    provider_name: str = Field(..., alias='providerName')
    ads_provider_id: str = Field(..., alias='adsProviderId')

class DetailPoster1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_poster: DetailPoster1 = Field(..., alias='detailPoster')

class Meta3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Credit(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_map: ImageMap1 | None = Field(None, alias='imageMap')
    role: str
    meta: Meta3
    name: str
    person_id: UUID = Field(..., alias='personId')
    birth_date: date | None = Field(None, alias='birthDate')

class Meta4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class Zone(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta4

class Image1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    is_primary: bool | None = Field(None, alias='isPrimary')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str

class Meta5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str
    cid: str

class CategoryObject(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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

class ParentalRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    code: str
    rating_source: str = Field(..., alias='ratingSource')
    rating_level: int = Field(..., alias='ratingLevel')

class Image2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ProviderBadge(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image: Image2
    title: str

class Image3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str

class BottomLeftItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image3
    badge_type: str = Field(..., alias='badgeType')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    id: UUID
    text: str
    audioguide: str
    text_color: str = Field(..., alias='textColor')

class Grid(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    bottom_left: list[BottomLeftItem] = Field(..., alias='bottom-left')

class BottomLeftItem1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    badge_color: list[str] = Field(..., alias='badgeColor')
    image: Image3
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
    provider_badge: ProviderBadge = Field(..., alias='providerBadge')
    grid: Grid
    detail_screen: DetailScreen = Field(..., alias='detailScreen')

class Meta6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID | str = Field(union_mode='left_to_right')
    source: str
    href: str
    sid: UUID | str = Field(union_mode='left_to_right')

class TrackerOverrides(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_server_data: str

class Meta7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID
    wid: UUID

class AudioTrack1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    language: str
    iso639_part1: str = Field(..., alias='iso639Part1')
    label: str

class DrmAuthentication1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    drm_content_provider: str = Field(..., alias='drmContentProvider')
    data: Data

class Video1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    video_type: str = Field(..., alias='videoType')
    drm_authentication: DrmAuthentication1 = Field(..., alias='drmAuthentication')
    url: str
    quality: str

class Media1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_tracks: list[AudioTrack1] = Field(..., alias='audioTracks')
    duration: int
    ad_breaks: list[time] = Field(..., alias='adBreaks')
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    videos: list[Video1]
    trick_play_files: list[TrickPlayFile] = Field(..., alias='trickPlayFiles')
    captions: list[Caption]

class PlaybackDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    url: str
    auto_play_next_url: str | None = Field(None, alias='autoPlayNextURL')

class Meta8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta8

class CreditCuePoint(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    start: int
    end: int
    skippable: bool
    type: str
    credit_type: str | None = Field(None, alias='creditType')

class ViewOption1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
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
    validity_end_time: AwareDatetime = Field(..., alias='validityEndTime')
    provider_details: ProviderDetails1 = Field(..., alias='providerDetails')
    currency: str
    provider_name: str = Field(..., alias='providerName')
    initial_available_time: AwareDatetime = Field(..., alias='initialAvailableTime')
    price_display: str = Field(..., alias='priceDisplay')
    in4k: bool
    ads_provider_id: str = Field(..., alias='adsProviderId')
    tags: list[str]
    in_hd: bool = Field(..., alias='inHd')
    license: str
    validity_start_time: AwareDatetime = Field(..., alias='validityStartTime')
    is_dummy_play_id: bool = Field(..., alias='isDummyPlayId')
    credit_cue_points: list[CreditCuePoint] = Field(..., alias='creditCuePoints')

class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta7
    season_number: str = Field(..., alias='seasonNumber')
    episode_number: str = Field(..., alias='episodeNumber')
    view_options: list[ViewOption1] = Field(..., alias='viewOptions')

class DetailBackground1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    roku_id: str = Field(..., alias='rokuId')
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_background: DetailBackground1 = Field(..., alias='detailBackground')

class Meta9(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    has_view_options: bool = Field(..., alias='hasViewOptions')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Credit1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    role: str
    meta: Meta9
    name: str
    person_id: UUID = Field(..., alias='personId')
    birth_date: date | None = Field(None, alias='birthDate')

class Meta10(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str
    sid: str
    has_view_options: bool | None = Field(None, alias='hasViewOptions')

class Grid1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    aspect_ratio: str = Field(..., alias='aspectRatio')

class ImageMap3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: Grid1

class Image5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    path: str
    tier: str
    is_primary: bool = Field(..., alias='isPrimary')
    aspect_ratio: str = Field(..., alias='aspectRatio')
    type: str
    roku_id: str | None = Field(None, alias='rokuId')

class Meta11(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID
    wid: UUID

class Meta12(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta12

class Media2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    duration: int

class ViewOption2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails2 = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    media: Media2

class Episode1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    current_time: AwareDatetime = Field(..., alias='currentTime')
    image_map: ImageMap3 = Field(..., alias='imageMap')
    images: list[Image5]
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    meta: Meta11
    description: str
    season_number: str = Field(..., alias='seasonNumber')
    title: str
    episode_number: str = Field(..., alias='episodeNumber')
    view_options: list[ViewOption2] = Field(..., alias='viewOptions')

class Season(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    image_map: ImageMap2 | None = Field(None, alias='imageMap')
    credits: list[Credit1] | None = None
    meta: Meta10
    season_number: str | None = Field(None, alias='seasonNumber')
    title: str | None = None
    descriptions: dict[str, Any] | None = None
    release_year: int | None = Field(None, alias='releaseYear')
    episodes: list[Episode1] | None = None

class Meta13(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str
    sid: UUID

class Series1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta13
    title: str

class Meta14(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ImageMap4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    grid: Grid1

class Meta15(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: UUID
    source: str
    href: str

class Meta16(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    media_type: str = Field(..., alias='mediaType')
    href_v2: str = Field(..., alias='hrefV2')
    id: str
    source: str
    href: str

class ProviderDetails3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta16

class ViewOption3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    provider_id: str = Field(..., alias='providerId')
    provider_details: ProviderDetails3 = Field(..., alias='providerDetails')
    is_unlocked: bool = Field(..., alias='isUnlocked')
    media: Media2

class Episode2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    current_time: AwareDatetime = Field(..., alias='currentTime')
    image_map: ImageMap4 = Field(..., alias='imageMap')
    images: list[Image5]
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    meta: Meta15
    description: str
    season_number: str = Field(..., alias='seasonNumber')
    title: str
    episode_number: str = Field(..., alias='episodeNumber')
    view_options: list[ViewOption3] = Field(..., alias='viewOptions')

class Season1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta14
    episodes: list[Episode2]

class ContentModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    next: Next
    image_map: ImageMap = Field(..., alias='imageMap')
    description: str | None = None
    type: str
    title: str
    descriptions: Descriptions
    view_options: list[ViewOption] = Field(..., alias='viewOptions')
    language_dialog_body: str = Field(..., alias='languageDialogBody')
    credits: list[Credit]
    kids_directed: bool = Field(..., alias='kidsDirected')
    genres: list[str]
    release_year: int = Field(..., alias='releaseYear')
    savable: bool
    category_objects: list[CategoryObject] = Field(..., alias='categoryObjects')
    content_rating_class: int = Field(..., alias='contentRatingClass')
    save_list_last_interaction_time: int = Field(..., alias='saveListLastInteractionTime')
    run_time_seconds: int | None = Field(None, alias='runTimeSeconds')
    release_date: AwareDatetime = Field(..., alias='releaseDate')
    admin_include: dict[str, Any] = Field(..., alias='adminInclude')
    parental_ratings: list[ParentalRating] = Field(..., alias='parentalRatings')
    indicators: Indicators | None = None
    reverse_chronological: bool = Field(..., alias='reverseChronological')
    current_time: AwareDatetime = Field(..., alias='currentTime')
    meta: Meta6
    tracker_overrides: TrackerOverrides = Field(..., alias='trackerOverrides')
    trace_id: UUID = Field(..., alias='traceId')
    episodes: list[Episode] | None = None
    seasons: list[Season] | None = None
    season_number: str | None = Field(None, alias='seasonNumber')
    series: Series1 | None = None
    episode_number: str | None = Field(None, alias='episodeNumber')
    season: Season1 | None = None
