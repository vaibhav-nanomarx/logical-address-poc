import sys
import os
# from utils.content_extractor import extract_from_html_file

from bs4 import BeautifulSoup

def extract_from_html_file(file_path, selectors):
    """
    Extract content or attributes from an HTML file using enhanced CSS selectors.
    
    Args:
        file_path (str): Path to the HTML file.
        selectors (list of str): List of CSS selectors. 
                                 If a selector includes '@attribute', extract the specified attribute.
    
    Returns:
        list of lists: A list where each sublist contains results for the corresponding selector.
    """
    try:
        # Read the HTML content from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        results = []
        
        for selector in selectors:
            if '@' in selector:
                # attribute extraction
                base_selector, attribute = selector.split('@')
                base_selector = base_selector.strip()
                attribute = attribute.strip()
                
                elements = soup.select(base_selector)
                extracted = [
                    element.get(attribute)
                    for element in elements
                    if element.get(attribute) is not None
                ]
            else:
                # text extraction
                elements = soup.select(selector)
                extracted = [element.get_text(strip=True) for element in elements]
            
            results.append(extracted)
        
        return results
    except Exception as e:
        raise ValueError(f"Error processing the HTML file: {e}")

folder_path = "test/Resources/cat1"

for file_name in os.listdir(folder_path):
    if file_name.endswith(".html"):
        file_path = os.path.join(folder_path, file_name)
        # change the css selectors according to your file category
        css_selectors = [
            "#app-root > .theme > #theme-app > .layout > .layout-content > .layout-content_main > .layout-content__article > .product-detail-view__content > .product-detail-view__main > .product-detail-view__main-content > .product-detail-view__side-bar > .product-detail-info > .product-detail-info__info > .product-detail-info__header > .product-detail-info__header-content > .product-detail-info__header-name",
            "#app-root > .theme > #theme-app > .layout > .layout-content > .layout-content_main > .layout-content__article > .product-detail-view__content > .product-detail-view__main > .product-detail-view__main-content > .product-detail-view__side-bar > .product-detail-info > .product-detail-info__price > .product-detail-info__price-amount price > .price__amount-wrapper > .price__amount > .price-current__amount > .money-amount price-formatted__price-amount > .money-amount__main"
        ]
    
        try:
            extracted_data = extract_from_html_file(file_path, css_selectors)
            print("="*10, "file" , "="*10)
            print(extracted_data)
            print("="*20,"\n")
        except ValueError as e:
            print(e)