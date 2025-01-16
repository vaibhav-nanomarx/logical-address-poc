import streamlit as st
import json

def find_content_paths(json_data, search_item, current_path=""):
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

def main():
    st.title("JSON Search Tool")

    json_input = st.text_area("Paste JSON here:", height=300)

    search_query = st.text_input("Enter the text or attribute value to search for:")

    if st.button("Search"):
        if json_input.strip() and search_query.strip():
            try:
                json_data = json.loads(json_input)
                paths = find_content_paths(json_data, search_query)

                st.subheader("Search Results")
                if paths:
                    for path in paths:
                        st.code(path)
                else:
                    st.warning("No matches found for the given search query.")

            except json.JSONDecodeError:
                st.error("Invalid JSON format. Please check your input.")
        else:
            st.error("Please provide both JSON input and a search query.")

if __name__ == "__main__":
    main()
