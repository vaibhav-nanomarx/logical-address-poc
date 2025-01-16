import streamlit as st
from bs4 import BeautifulSoup
import json
import os

def parse_html(element):
    tag_data = {
        "Tag": element.name,
        "Class": " ".join(element.get("class", [])),
        "ID": element.get("id", ""),
        "URL": element.get("href", ""),
        "SRC": element.get("src", ""),
        "ALT": element.get("alt", ""),
        "CONTENT": element.text.strip() if element.text else "",
        "CHILDREN": []
    }
    for child in element.find_all(recursive=False):
        tag_data["CHILDREN"].append(parse_html(child))
    return tag_data

def main():
    st.title("HTML to JSON Parser")
    html_input = st.text_area("Paste HTML code here:", height=300)
    file_name = st.text_input("Enter the output JSON file name (without extension):", value="parsed_output")

    if st.button("Parse HTML"):
        if html_input.strip():
            soup = BeautifulSoup(html_input, "html.parser")
            parsed_json = []
            for element in soup.find_all(recursive=False):
                parsed_json.append(parse_html(element))

            output_dir = "parsed_HTML"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{file_name}.json")
            with open(output_path, "w") as json_file:
                json.dump(parsed_json, json_file, indent=4)

            st.subheader("Parsed JSON Output")
            st.json(parsed_json)
            st.success(f"JSON file saved to {output_path}")
        else:
            st.error("Please provide valid HTML input.")

if __name__ == "__main__":
    main()
