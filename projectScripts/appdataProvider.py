from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

# from pprint import pprint

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://gofile.io/d/pLp39s")
sleep(5)

# Get appdata as Python dict
appdata = driver.execute_script("return appdata;")

# Using pprint (works well for Python dicts)
# pprint(appdata, indent=2, width=10)

# Extract all file names in a single pass without recursion
file_names = []
folder_names = []
file_links = []
content_data = appdata.get('fileManager', {}).get(
    'mainContent', {}).get('data', {})
children = content_data.get('children', {})

for child_id, child in children.items():
    if child.get('type') == 'file':
        file_names.append(child.get('name'))
        file_links.append(child.get('link'))
    elif child.get('type') == 'folder':
        # Direct access to folder's children
        folder_names.append(child.get('name'))


print("File names:")
for name in file_names:
    print(f"  - {name}")


print("Folder names:")
for name in folder_names:
    print(f"  - {name}")

print("Links:")
for name in file_links:
    print(f"  - {name}")

driver.quit()
