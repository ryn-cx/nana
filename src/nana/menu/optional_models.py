from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    path: str | Any = Field(default=None, union_mode='left_to_right')

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class ViewItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta1 | Any = Field(default=None, union_mode='left_to_right')
    icon: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class ViewItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    view: list[ViewItem2] | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta1 | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class ViewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta | Any = Field(default=None, union_mode='left_to_right')
    hideable: bool | Any = Field(default=None, union_mode='left_to_right')
    title_loc_key: str | Any = Field(None, alias='titleLocKey', union_mode='left_to_right')
    do_not_personalize: bool | Any = Field(None, alias='doNotPersonalize', union_mode='left_to_right')
    field_uuid: str | Any = Field(None, alias='_UUID', union_mode='left_to_right')
    custom_icon_text: str | Any = Field(None, alias='customIconText', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    view: list[ViewItem1] | Any = Field(default=None, union_mode='left_to_right')

class Meta3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    version: int | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | Any = Field(default=None, union_mode='left_to_right')

class MenuModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    view: list[ViewItem] | Any = Field(default=None, union_mode='left_to_right')
    meta: Meta3 | Any = Field(default=None, union_mode='left_to_right')
    deletable: bool | Any = Field(default=None, union_mode='left_to_right')
    channel_store: str | Any = Field(None, alias='channelStore', union_mode='left_to_right')
    iln_enabled: bool | Any = Field(None, alias='ilnEnabled', union_mode='left_to_right')
    active_index: int | Any = Field(None, alias='activeIndex', union_mode='left_to_right')
    collapse: bool | Any = Field(default=None, union_mode='left_to_right')
    tracker_overrides: TrackerOverrides | Any = Field(None, alias='trackerOverrides', union_mode='left_to_right')
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
