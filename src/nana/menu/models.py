from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict, Field

class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str
    path: str | None = None

class Meta1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str

class ViewItem2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta1
    icon: str | None = None
    title: str

class ViewItem1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    view: list[ViewItem2]
    meta: Meta1
    title: str

class ViewItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    meta: Meta
    hideable: bool
    title_loc_key: str = Field(..., alias='titleLocKey')
    do_not_personalize: bool = Field(..., alias='doNotPersonalize')
    field_uuid: str = Field(..., alias='_UUID')
    custom_icon_text: str = Field(..., alias='customIconText')
    id: str
    title: str
    view: list[ViewItem1] | None = None

class Meta3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    version: int
    media_type: str = Field(..., alias='mediaType')
    id: str

class TrackerOverrides(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_server_data: str

class MenuModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    type: str
    view: list[ViewItem]
    meta: Meta3
    deletable: bool
    channel_store: str = Field(..., alias='channelStore')
    iln_enabled: bool = Field(..., alias='ilnEnabled')
    active_index: int = Field(..., alias='activeIndex')
    collapse: bool
    tracker_overrides: TrackerOverrides = Field(..., alias='trackerOverrides')
    trace_id: UUID = Field(..., alias='traceId')
