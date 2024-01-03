import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scan_vulnerabilities(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            vulnerabilities = check_for_vulnerabilities(url, soup)
            
            if vulnerabilities:
                print(f"Vulnerabilities found at {url}: {', '.join(vulnerabilities)}")
            else:
                print(f"No vulnerabilities found at {url}")
        else:
            print(f"Failed to access URL: {url}")
    except requests.RequestException as e:
        print(f"Error occurred while scanning {url}: {e}")

def check_for_vulnerabilities(base_url, soup):
    vulnerabilities_found = []

    # Example: Check for forms without CSRF protection
    forms = soup.find_all('form')
    for form in forms:
        if not form.find('input', {'name': 'csrf_token'}):
            vulnerabilities_found.append("CSRF protection missing in a form")

    # Example: Check for insecure (HTTP) resource references
    insecure_resources = soup.find_all(['script', 'img', 'link'], {'src': True, 'href': True})
    for resource in insecure_resources:
        resource_url = urljoin(base_url, resource.get('src') or resource.get('href'))
        if resource_url.startswith('http://'):
            vulnerabilities_found.append(f"Insecure resource reference found: {resource_url}")

    # Add more checks based on your specific requirements

    return vulnerabilities_found

# Example usage
target_url = "https://example.com"
scan_vulnerabilities(target_url)
