"""
Web scraper for collecting data from official AMC, SEBI, and AMFI sources
"""
import requests
from bs4 import BeautifulSoup
import time
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
import logging
from typing import Dict, List, Optional
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCollector:
    """Collects data from official mutual fund sources"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.scraped_data_dir = config.SCRAPED_DATA_DIR
        
    def fetch_page(self, url: str, timeout: int = 30) -> Optional[Dict]:
        """Fetch a single page and extract content"""
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=timeout, allow_redirects=True)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()
            
            # Extract text content
            text = soup.get_text(separator=' ', strip=True)
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text(strip=True) if title else url
            
            # Extract meta description if available
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ''
            
            return {
                'url': url,
                'title': title_text,
                'description': description,
                'content': text,
                'timestamp': time.time()
            }
            
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error processing {url}: {e}")
            return None
    
    def collect_all_sources(self) -> List[Dict]:
        """Collect data from all configured sources"""
        all_data = []
        
        for source_name, url in config.SOURCE_URLS.items():
            data = self.fetch_page(url)
            if data:
                # Save individual file
                output_file = self.scraped_data_dir / f"{source_name}.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                all_data.append(data)
                logger.info(f"Successfully collected: {source_name}")
            
            # Be respectful with rate limiting
            time.sleep(2)
        
        # Save combined data
        combined_file = self.scraped_data_dir / "all_sources.json"
        with open(combined_file, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Collected {len(all_data)} sources")
        return all_data
    
    def load_scraped_data(self) -> List[Dict]:
        """Load previously scraped data"""
        combined_file = self.scraped_data_dir / "all_sources.json"
        if combined_file.exists():
            with open(combined_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

if __name__ == "__main__":
    collector = DataCollector()
    collector.collect_all_sources()

