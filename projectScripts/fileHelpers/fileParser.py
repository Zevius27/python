from bs4 import BeautifulSoup


def get_truncate_divs(html):
    """
    Extract all truncate divs from HTML content.

    Args:
        html (str): HTML string to parse

    Returns:
        list: List of BeautifulSoup div elements with class 'truncate'
    """
    soup = BeautifulSoup(html, 'html.parser')
    truncate_divs = soup.select('div.truncate')
    return truncate_divs


def get_truncate_text(html):
    """
    Get text content from all truncate divs.

    Args:
        html (str): HTML string to parse

    Returns:
        list: List of strings containing text from each truncate div
    """
    soup = BeautifulSoup(html, 'html.parser')
    truncate_divs = soup.select('div.truncate')
    return [div.get_text(strip=True) for div in truncate_divs]


def get_truncate_links(html):
    """
    Extract all links from truncate divs.

    Args:
        html (str): HTML string to parse

    Returns:
        list: List of dictionaries containing link text and href
    """
    soup = BeautifulSoup(html, 'html.parser')
    truncate_divs = soup.select('div.truncate')
    links = []

    for div in truncate_divs:
        link = div.find('a', class_='item_open')
        if link:
            links.append({
                'text': link.text.strip(),
                'href': link.get('href', '')
            })

    return links


def get_file_items(html):
    """
    Extract all file/folder items with their details.

    Args:
        html (str): HTML string to parse

    Returns:
        list: List of dictionaries containing item details
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = []

    for item_div in soup.select('[data-item-id]'):
        item_id = item_div.get('data-item-id')
        truncate_div = item_div.find('div', class_='truncate')

        if truncate_div:
            link = truncate_div.find('a', class_='item_open')
            date_span = truncate_div.find('span')

            item_data = {
                'id': item_id,
                'name': link.text.strip() if link else '',
                'href': link.get('href', '') if link else '',
                'date': date_span.text.strip() if date_span else '',
                'is_folder': bool(item_div.find('i', class_='fa-folder'))
            }
            items.append(item_data)

    return items
