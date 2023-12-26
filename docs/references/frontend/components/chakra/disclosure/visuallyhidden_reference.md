##  Reference for nextpy/frontend/components/chakra/disclosure/visuallyhidden(Generated by a LLM. Pending Review)

# Nextpy Documentation: VisuallyHidden Component

## VisuallyHidden

The `VisuallyHidden` component is a utility component used to hide elements on the screen from sighted users but keep them readable to screen readers. This is useful for accessibility purposes, allowing developers to include content that should be announced by assistive technologies without affecting the visual UI design, such as skip links, form labels for screen readers, and other similar use cases.

### Anatomy

The `VisuallyHidden` component can be easily implemented in your project by importing it from the Nextpy library and adding it to your layout. Below are basic and advanced examples of how to use `VisuallyHidden`:

#### Basic Example

```python
from nextpy.components.chakra.disclosure.visuallyhidden import VisuallyHidden

hidden_content = VisuallyHidden.create(
    "This is visually hidden text but accessible by screen readers."
)
```

#### Advanced Example

```python
from nextpy.components.chakra.disclosure.visuallyhidden import VisuallyHidden

hidden_content_advanced = VisuallyHidden.create(
    "Advanced hidden content",
    style=Style(display="none"),
    on_focus=lambda event: print("Focused on hidden content")
)
```

### Components

`VisuallyHidden` does not contain sub-components, but it supports all standard events and custom attributes.

#### Properties

| Prop Name      | Type    | Description                                                           |
|----------------|---------|-----------------------------------------------------------------------|
| style          | Style   | An optional style object to apply custom styles to the component.     |
| key            | Any     | A unique key for the component, useful for list rendering.            |
| id             | Any     | The id for the component.                                             |
| class_name     | Any     | The class name for the component.                                     |
| autofocus      | bool    | If `True`, the component will be auto-focused once the page loads.    |
| custom_attrs   | Dict    | Custom HTML attributes to be added to the component.                  |
| on_[event]     | Various | Event handlers for standard events such as `on_click`, `on_focus`, etc. |

### Notes

- `VisuallyHidden` should only be used for content that is meant to be invisible visually but still accessible to assistive technologies.
- Avoid using `VisuallyHidden` to hide interactive content, as this may cause confusion for keyboard and screen reader users.

### Best Practices

- Use `VisuallyHidden` for content that is solely for screen readers, like descriptive text for form inputs or additional context for links.
- When using `VisuallyHidden`, ensure that the hidden content is not interactive, as this can lead to a confusing experience for users who rely on assistive technology.
- Remember to test your application with screen readers to ensure that `VisuallyHidden` content is appropriately announced.