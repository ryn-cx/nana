# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import SearchModel as OptionalModel
from .strict_models import SearchModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        AmpId,
        BottomLeftItem,
        BottomLeftItem1,
        Content,
        Descriptions,
        DetailScreen,
        Details,
        Features,
        Field100,
        Grid,
        Grid1,
        Image,
        Image1,
        Image2,
        ImageMap,
        Indicators,
        Meta,
        Meta1,
        Meta2,
        Meta3,
        ParentalRating,
        ProviderBadge,
        ProviderDetails,
        Search,
        SearchModel,
        Season,
        TrackerOverrides,
        TrackerOverrides1,
        ViewItem,
        ViewOption,
    )
else:
    from .optional_models import (
        AmpId,
        BottomLeftItem,
        BottomLeftItem1,
        Content,
        Descriptions,
        DetailScreen,
        Details,
        Features,
        Field100,
        Grid,
        Grid1,
        Image,
        Image1,
        Image2,
        ImageMap,
        Indicators,
        Meta,
        Meta1,
        Meta2,
        Meta3,
        ParentalRating,
        ProviderBadge,
        ProviderDetails,
        Search,
        SearchModel,
        Season,
        TrackerOverrides,
        TrackerOverrides1,
        ViewItem,
        ViewOption,
    )

__all__ = [
    "AmpId",
    "BottomLeftItem",
    "BottomLeftItem1",
    "Content",
    "Descriptions",
    "DetailScreen",
    "Details",
    "Features",
    "Field100",
    "Grid",
    "Grid1",
    "Image",
    "Image1",
    "Image2",
    "ImageMap",
    "Indicators",
    "Meta",
    "Meta1",
    "Meta2",
    "Meta3",
    "ParentalRating",
    "ProviderBadge",
    "ProviderDetails",
    "Search",
    "SearchModel",
    "Season",
    "TrackerOverrides",
    "TrackerOverrides1",
    "ViewItem",
    "ViewOption",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> SearchModel:
    """Read a downloaded file into SearchModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
