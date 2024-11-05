from urllib.parse import urlparse, parse_qs, urlunparse


# Extract the 'id' parameter from the URL
def extract_id(url):
    query_params = parse_qs(urlparse(url).query)
    return query_params.get('id', [None])[0]


# Construct a new URL with a SQL payload attached to the 'id' parameter
def construct_test_url(base_url, id_value, payload):
    parsed_url = urlparse(base_url)
    new_query = f"id={id_value}{payload}"
    return urlunparse(parsed_url._replace(query=new_query))
