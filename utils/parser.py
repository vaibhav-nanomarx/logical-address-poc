from bs4 import BeautifulSoup
import json
import os

def parse_html_to_json(element):
    tag_data = {
        "Tag": element.name,
        "Class": " ".join(element.get("class", [])),
        "ID": element.get("id", ""),
        "URL": element.get("href", ""),
        "SRC": element.get("src", ""),
        "ALT": element.get("alt", ""),
        "CHILDREN": []
    }
    for child in element.find_all(recursive=False):
        tag_data["CHILDREN"].append(parse_html_to_json(child))
    return tag_data

def html_to_json(html_input, file_name="parsed_output", output_dir="parsed_HTML"):
    if not html_input.strip():
        raise ValueError("HTML input cannot be empty.")

    # Parse HTML input using BeautifulSoup
    soup = BeautifulSoup(html_input, "html.parser")

    # Convert the parsed HTML to JSON format
    parsed_json = []
    for element in soup.find_all(recursive=False):
        parsed_json.append(parse_html_to_json(element))

    # Save JSON output to a file
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{file_name}.json")
    with open(output_path, "w") as json_file:
        json.dump(parsed_json, json_file, indent=4)

    return output_path, parsed_json