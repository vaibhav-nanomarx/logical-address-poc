import streamlit as st
from bs4 import BeautifulSoup
import lxml.html
from lxml import etree


def extract_with_css(html_content, selector):
    """
    Extract content or attributes from HTML using an enhanced CSS selector.
    If the selector includes '@attribute', extract the specified attribute.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    if '@' in selector:
        base_selector, attribute = selector.split('@')
        base_selector = base_selector.strip()
        attribute = attribute.strip()
        
        elements = soup.select(base_selector)

        return [
            element.get(attribute)
            for element in elements
            if element.get(attribute) is not None
        ]
    else:
        elements = soup.select(selector)
        return [element.get_text(strip=True) for element in elements]

def extract_with_xpath(html_content, xpath_expr):
    try:
        tree = lxml.html.fromstring(html_content)
        elements = tree.xpath(xpath_expr)
        # Convert elements to string if they are elements, else keep as is
        results = []
        for elem in elements:
            if isinstance(elem, etree._Element):
                results.append(etree.tostring(elem, pretty_print=True, method="html").decode())
            else:
                results.append(str(elem))
        return results
    except etree.XPathError as e:
        st.error(f"Invalid XPath expression: {e}")
        return []

def main():
    st.set_page_config(page_title="Pddressing POC", layout="wide")

    # Sidebar for Inputs
    st.sidebar.header("Input Parameters")

    # HTML Input
    html_input = st.sidebar.text_area(
        "Enter HTML Content",
        height=300,
    )

    # Address Path Input
    address_path = st.sidebar.text_input(
        "Enter Address Path",
        help="Provide the CSS Selector or XPath to locate the desired elements."
    )

    # Selector Type Selection
    selector_type = st.sidebar.selectbox(
        "Select Selector Type",
        options=["CSS Selector"],
    )

    # Extract Button
    if st.sidebar.button("Extract Data"):
        if not html_input:
            st.error("Please enter the HTML content.")
        elif not address_path:
            st.error("Please enter the address path.")
        else:
            with st.spinner("Extracting data..."):
                if selector_type == "CSS Selector":
                    try:
                        results = extract_with_css(html_input, address_path)
                        if results:
                            st.success(f"Found {len(results)} element(s).")
                            for idx, item in enumerate(results, 1):
                                st.markdown(f"**Element {idx}:** {item}")
                        else:
                            st.warning("No elements found with the given CSS Selector.")
                    except Exception as e:
                        st.error(f"An error occurred while extracting with CSS Selector: {e}")
                # else:
                #     results = extract_with_xpath(html_input, address_path)
                #     if results:
                #         st.success(f"Found {len(results)} element(s).")
                #         for idx, item in enumerate(results, 1):
                #             st.markdown(f"**Element {idx}:**")
                #             st.code(item, language='html')
                #     else:
                #         st.warning("No elements found with the given XPath.")


if __name__ == "__main__":
    main()
