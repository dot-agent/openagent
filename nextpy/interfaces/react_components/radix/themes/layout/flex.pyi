# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

"""Stub file for nextpy/components/radix/themes/layout/flex.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from nextpy.backend.vars import Var, BaseVar, ComputedVar
from nextpy.backend.event import EventChain, EventHandler, EventSpec
from nextpy.interfaces.web.style import Style
from typing import Literal
from nextpy import el
from nextpy.backend.vars import Var
from ..base import LiteralAlign, LiteralJustify, LiteralSize
from .base import LayoutComponent

LiteralFlexDirection = Literal["row", "column", "row-reverse", "column-reverse"]
LiteralFlexDisplay = Literal["none", "inline-flex", "flex"]
LiteralFlexWrap = Literal["nowrap", "wrap", "wrap-reverse"]

class Flex(el.Div, LayoutComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color: Optional[Union[Var[str], str]] = None,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
        display: Optional[
            Union[
                Var[Literal["none", "inline-flex", "flex"]],
                Literal["none", "inline-flex", "flex"],
            ]
        ] = None,
        direction: Optional[
            Union[
                Var[Literal["row", "column", "row-reverse", "column-reverse"]],
                Literal["row", "column", "row-reverse", "column-reverse"],
            ]
        ] = None,
        align: Optional[
            Union[
                Var[Literal["start", "center", "end", "baseline", "stretch"]],
                Literal["start", "center", "end", "baseline", "stretch"],
            ]
        ] = None,
        justify: Optional[
            Union[
                Var[Literal["start", "center", "end", "between"]],
                Literal["start", "center", "end", "between"],
            ]
        ] = None,
        wrap: Optional[
            Union[
                Var[Literal["nowrap", "wrap", "wrap-reverse"]],
                Literal["nowrap", "wrap", "wrap-reverse"],
            ]
        ] = None,
        gap: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        access_key: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        auto_capitalize: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        dir: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        draggable: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        enter_key_hint: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        hidden: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        input_mode: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        item_prop: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        lang: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        role: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        slot: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        spell_check: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        tab_index: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        title: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        translate: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        p: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        px: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        py: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        pt: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        pr: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        pb: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        pl: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        shrink: Optional[Union[Var[Literal["0", "1"]], Literal["0", "1"]]] = None,
        grow: Optional[Union[Var[Literal["0", "1"]], Literal["0", "1"]]] = None,
        m: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mx: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        my: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mt: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mr: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mb: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        ml: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Flex":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color: map to CSS default color property.
            color_scheme: map to radix color property.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            display: How to display the element: "none" | "inline-flex" | "flex"
            direction: How child items are layed out: "row" | "column" | "row-reverse" | "column-reverse"
            align: Alignment of children along the main axis: "start" | "center" | "end" | "baseline" | "stretch"
            justify: Alignment of children along the cross axis: "start" | "center" | "end" | "between"
            wrap: Whether children should wrap when they reach the end of their container: "nowrap" | "wrap" | "wrap-reverse"
            gap: Gap between children: "0" - "9"
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            translate: Specifies whether the content of an element should be translated or not.
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            shrink: Whether the element will take up the smallest possible space: "0" | "1"
            grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...
