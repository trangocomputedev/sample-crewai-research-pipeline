import re
from crewai.tools import BaseTool
from pydantic import Field


class CustomScraperTool(BaseTool):
    name: str = "Custom Web Scraper"
    description: str = (
        "Scrape and clean the text content of a web page, stripping HTML tags "
        "and returning only readable prose. Use when ScrapeWebsiteTool returns too much noise."
    )
    max_chars: int = Field(default=8000, description="Maximum characters to return")

    def _run(self, url: str) -> str:
        try:
            import urllib.request
            with urllib.request.urlopen(url, timeout=10) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text).strip()
            return text[: self.max_chars]
        except Exception as exc:
            return f"Error scraping {url}: {exc}"
