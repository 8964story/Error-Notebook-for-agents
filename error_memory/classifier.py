from __future__ import annotations


def classify_error(error_text: str) -> str:
    text = (error_text or "").lower()

    if any(k in text for k in ["timeout", "api key", "auth", "provider", "cron", "delivery"]):
        return "api_call"
    if any(k in text for k in ["file not found", "path", "directory", "encoding", "models.json", "config"]):
        return "file_io"
    if any(k in text for k in ["scrape", "browser", "cloudflare", "page loaded", "extracted content is empty", "selector"]):
        return "web_scraping"
    return "logic"
