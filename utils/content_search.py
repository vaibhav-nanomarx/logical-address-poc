import json

def find_content_paths(json_data, search_item, current_path=""):
    """
    Recursively search JSON data for the specified content or attribute value.

    Args:
        json_data (dict or list): The JSON data to search.
        search_item (str): The text or attribute value to search for.
        current_path (str): The current CSS selector path.

    Returns:
        list: A list of CSS selector paths matching the search item.
    """
    paths = []

    if isinstance(json_data, dict):
        tag = json_data.get("Tag", "")
        css_selector = f"{current_path}{tag}" if current_path else tag

        if search_item in json_data.get("CONTENT", ""):
            paths.append(css_selector)

        for attr in ["Class", "ID", "URL", "SRC", "ALT"]:
            if search_item in json_data.get(attr, ""):
                attribute_selector = f"{css_selector}@{attr.lower()}"
                paths.append(attribute_selector)

        # Traverse children
        for child in json_data.get("CHILDREN", []):
            child_selector = f"{css_selector} > " if css_selector else ""
            paths.extend(find_content_paths(child, search_item, child_selector))

    elif isinstance(json_data, list):
        for element in json_data:
            paths.extend(find_content_paths(element, search_item, current_path))

    return paths

def search_in_json(json_input, search_query):
    """
    Search for a specific query in JSON input and return matching paths.

    Args:
        json_input (str): JSON string to search.
        search_query (str): The query to search for.

    Returns:
        list: Matching paths in the JSON structure.
    """
    try:
        json_data = json.loads(json_input)
        return find_content_paths(json_data, search_query)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format.")
