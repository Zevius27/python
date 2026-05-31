from fileParser import *
from fileHelper import fileHelperHtml


html = fileHelperHtml("tpoNxk")
# print(html)
# Get truncate divs
truncate_divs = get_truncate_divs(html)
print(f"Found {len(truncate_divs)} truncate divs")

# Get links with their details
links = get_truncate_links(html)
for link in links:
    print(f"Link: {link['text']} -> {link['href']}")


# ////////////////////////////////////////////////////////////////////////////////////////////
# Future use
# ////////////////////////////////////////////////////////////////////////////////////////


# # Get just the text
# texts = get_truncate_text(html)
# for text in texts:
#     print(f"Text: {text}")

# # Get complete file items
# items = get_file_items(html)
# for item in items:
#     print(f"Item: {item['name']} (ID: {item['id']}) - Date: {item['date']}")
