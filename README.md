# logical-address-poc

running the app: `streamlit run app.py`

example:

`<div id="users">`
    `<div class="user" id="user-1">`
       ` <span class="name">John Doe</span>`
       ` <span class="email">john@example.com</span>`
   ` </div>`
    `<div class="user" id="user-2">`
       ` <span class="name">Jane Smith</span>`
        `<span class="email">jane@example.com</span>`
    `</div>`
`</div>`


Address Path: #users > .user > .name

Selector Type: CSS Selector

# CSS Selectors for Extracting Content and Attributes

## 1. Extracting Text Content
Use standard CSS selectors to target the element and extract its text content.

### Examples:
- `.class-name`  
  Extracts the text content of all elements with the class `class-name`.
- `#id > div`  
  Extracts the text content of all `div` elements that are direct children of an element with the ID `id`.

---

## 2. Extracting Attributes
To extract attributes, append `@attribute` to the CSS selector.

### Examples:
- `.class-name@href`  
  Extracts the `href` attribute of all elements with the class `class-name`.
- `img@src`  
  Extracts the `src` attribute of all `img` elements.
- `#id > a@title`  
  Extracts the `title` attribute of all `a` elements that are direct children of an element with the ID `id`.

