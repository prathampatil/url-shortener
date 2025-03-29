"""
URL Shortener Utility
A simple utility to create shortened URLs.

This module provides functionality to:
1. Generate short URL codes
2. Save and retrieve URL mappings
"""

import hashlib
import json
import time
from datetime import datetime
from pathlib import Path
import numpy as np

class URLShortener:
    def __init__(self, storage_path="url_data.json"):
        """Initialize the URL shortener with the given storage path."""
        self.storage_path = Path(storage_path)
        self.url_data = self._load_data()
    
    def _load_data(self):
        """Load URL data from storage or return an empty dictionary if no data exists."""
        if self.storage_path.exists():
            with open(self.storage_path, "r") as f:
                return json.load(f)
        return {"urls": {}}
    
    def _save_data(self):
        """Save the URL data to storage."""
        with open(self.storage_path, "w") as f:
            json.dump(self.url_data, f, indent=2)
    
    def create_short_url(self, original_url, custom_code=None):
        """
        Create a shortened URL code for the given original URL.
        
        Args:
            original_url: The original URL to shorten
            custom_code: Optional custom code to use
            
        Returns:
            The short code for the URL
        """
        if custom_code:
            code = custom_code
        else:
            # Generate a short code based on the URL and current time
            i_hash_input = f"{original_url}_{time.time()}"
            code = hashlib.md5(hash_input.encode()).hexdigest()[:6]
        
        # Store the mapping
        self.url_data["urls"][code] = {
            "original_url": original_url,
            "created_at": datetime.now().isoformat()
        }
        
        self._save_data()
        return code
    
    def get_original_url(self, code):
        """
        Get the original URL for a given short code.
        
        Args:
            code: The short code to look up
            
        Returns:
            The original URL or None if not found
        """
        if code not in self.url_data["urls"]:
            return None
        
        return self.url_data["urls"][code]["original_url"]


if __name__ == "__main__":
    # example
    shortener = URLShortener()
    code = shortener.create_short_url("https://tuwien.ac.at/very/long/url/that/needs/shortening")
    print(f"Shortened URL code: {code}")
    
    original = shortener.get_original_url(code)
    print(f"Original URL: {original}")
