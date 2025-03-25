"""
Tests for the URL Shortener utility
"""

import pytest
import os
from url_shortener import URLShortener


@pytest.fixture
def shortener():
    """Create a test shortener instance with a temporary data file."""
    test_file = "test_url_data.json"
    # ensure clean start
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # create shortener
    s = URLShortener(storage_path=test_file)
    yield s
    
    # cleanup
    if os.path.exists(test_file):
        os.remove(test_file)


def test_create_short_url(shortener):
    """Test creating a short URL with auto-generated code."""
    original_url = "https://example.com/test"
    code = shortener.create_short_url(original_url)
    
    # check that the code is the right length
    assert len(code) == 6
    
    # check that the URL was stored
    retrieved_url = shortener.get_original_url(code)
    assert retrieved_url == original_url


def test_create_custom_url(shortener):
    """Test creating a short URL with a custom code."""
    original_url = "https://example.com/custom"
    custom_code = "custom"
    code = shortener.create_short_url(original_url, custom_code=custom_code)
    
    # check that our custom code was used
    assert code == custom_code
    
    # check that the URL was stored
    retrieved_url = shortener.get_original_url(code)
    assert retrieved_url == original_url


def test_nonexistent_url(shortener):
    """Test retrieving a URL that doesn't exist."""
    # attempt to retrieve a non-existent URL
    retrieved_url = shortener.get_original_url("nonexistent")
    assert retrieved_url is None