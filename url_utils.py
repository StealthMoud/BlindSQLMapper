from urllib.parse import urlparse, urlunparse, parse_qs

# Function to extract the id value from the URL
def extract_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('id', [None])[0]

# Function to construct a URL with a payload
def construct_test_url(base_url, id_value, payload):
    parsed_url = urlparse(base_url)
    new_query = f"id={id_value}{payload}"
    return urlunparse(parsed_url._replace(query=new_query))
