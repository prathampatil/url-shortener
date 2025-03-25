# URL Shortener Utility

A simple utility to create shortened URLs. This is a lightweight implementation inspired by URL shortening services like Bitly and TinyURL.

## Features

- Generate short URL codes from long URLs
- Support for custom URL codes
- Persistent storage of URL mappings

## Installation

```bash
git clone https://github.com/JFKane/url-shortener.git
cd url-shortener
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from url_shortener import URLShortener

# Initialize the shortener
shortener = URLShortener()

# Create a short URL
code = shortener.create_short_url("https://example.com/very/long/url/that/needs/shortening")
print(f"Short URL code: {code}")  # e.g., "a1b2c3"

# Retrieve the original URL
original_url = shortener.get_original_url(code)
print(f"Original URL: {original_url}")
```

### Custom URL Codes

```python
# Create a URL with a custom code
custom_code = shortener.create_short_url(
    "https://example.com/my-important-page", 
    custom_code="my-page"
)
```

## Data Storage

URL mappings are stored in a JSON file. See `test_data.json` for an example of the data structure.

## Development

### Running Tests

```bash
pytest
```

### Code Quality

This project uses [ruff](https://github.com/astral-sh/ruff) for linting:

```bash
ruff check .
```

## License

MIT License - See LICENSE file for details.