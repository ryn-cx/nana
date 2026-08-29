from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class Meta(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    type: str | None = None
    path: str | None = None

class Meta1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    type: str | None = None

class ViewItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta1 | None = None
    icon: str | None = None
    title: str | None = None

class ViewItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    view: list[ViewItem2] | None = None
    meta: Meta1 | None = None
    title: str | None = None

class ViewItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    meta: Meta | None = None
    hideable: bool | None = None
    title_loc_key: str | None = Field(None, alias='titleLocKey')
    do_not_personalize: bool | None = Field(None, alias='doNotPersonalize')
    field_uuid: str | None = Field(None, alias='_UUID')
    custom_icon_text: str | None = Field(None, alias='customIconText')
    id: str | None = None
    title: str | None = None
    view: list[ViewItem1] | None = None

class Meta3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    version: int | None = None
    media_type: str | None = Field(None, alias='mediaType')
    id: str | None = None

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_server_data: str | None = None

class MenuModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    type: str | None = None
    view: list[ViewItem] | None = None
    meta: Meta3 | None = None
    deletable: bool | None = None
    channel_store: str | None = Field(None, alias='channelStore')
    iln_enabled: bool | None = Field(None, alias='ilnEnabled')
    active_index: int | None = Field(None, alias='activeIndex')
    collapse: bool | None = None
    tracker_overrides: TrackerOverrides | None = Field(None, alias='trackerOverrides')
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
