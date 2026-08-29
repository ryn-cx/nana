from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel, Field
from uuid import UUID

class Meta(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    type: str
    path: str | None = None

class Meta1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    type: str

class ViewItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta1
    icon: str | None = None
    title: str

class ViewItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    view: list[ViewItem2]
    meta: Meta1
    title: str

class ViewItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    meta: Meta
    hideable: bool
    title_loc_key: str = Field(..., alias='titleLocKey')
    do_not_personalize: bool = Field(..., alias='doNotPersonalize')
    field_uuid: str = Field(..., alias='_UUID')
    custom_icon_text: str = Field(..., alias='customIconText')
    id: str
    title: str
    view: list[ViewItem1] | None = None

class Meta3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    version: int
    media_type: str = Field(..., alias='mediaType')
    id: str

class TrackerOverrides(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_server_data: str

class MenuModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
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
