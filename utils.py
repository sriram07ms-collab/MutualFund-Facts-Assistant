"""
Utility functions for the Mutual Fund Facts Assistant
"""
import re
from typing import List, Optional

def clean_text(text: str) -> str:
    """Clean and normalize text content"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters that might interfere
    text = text.strip()
    return text

def extract_scheme_name(query: str) -> Optional[str]:
    """Extract scheme name from query if mentioned"""
    schemes = {
        'large cap': 'Nippon India Large Cap Fund',
        'flexi cap': 'Nippon India Flexi Cap Fund',
        'elss': 'Nippon India ELSS Tax Saver Fund',
        'small cap': 'Nippon India Small Cap Fund'
    }
    
    query_lower = query.lower()
    for key, value in schemes.items():
        if key in query_lower:
            return value
    return None

def validate_url(url: str) -> bool:
    """Validate URL format"""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

def format_source_url(url: str) -> str:
    """Format source URL for display"""
    # Remove query parameters for cleaner display
    if '?' in url:
        url = url.split('?')[0]
    return url

