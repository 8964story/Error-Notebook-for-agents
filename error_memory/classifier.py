from __future__ import annotations

"""Rule-based error classification for Error Notebook."""

PROVIDER_AUTH_KEYWORDS = {
    "api key",
    "auth",
    "authentication",
    "unauthorized",
    "forbidden",
    "provider",
    "invalid token",
    "model unavailable",
    "unknown model",
}

TRANSIENT_NETWORK_KEYWORDS = {
    "timeout",
    "timed out",
    "connection reset",
    "temporarily unavailable",
    "rate limit",
    "429",
    "network error",
}

FILE_IO_KEYWORDS = {
    "file not found",
    "path",
    "directory",
    "encoding",
    "models.json",
    "config",
    "no such file",
}

WEB_SCRAPING_KEYWORDS = {
    "scrape",
    "browser",
    "cloudflare",
    "page loaded",
    "extracted content is empty",
    "selector",
    "article",
    "snapshot",
}

WORKFLOW_OR_LOGIC_KEYWORDS = {
    "cron",
    "delivery",
    "routing",
    "wrong branch",
    "partial success",
    "workflow",
    "plan",
}


def classify_error(error_text: str) -> str:
    """Classify raw error text into a coarse failure domain."""
    text = (error_text or "").lower()

    if any(keyword in text for keyword in PROVIDER_AUTH_KEYWORDS):
        return "provider_auth"
    if any(keyword in text for keyword in TRANSIENT_NETWORK_KEYWORDS):
        return "transient_network"
    if any(keyword in text for keyword in FILE_IO_KEYWORDS):
        return "file_io"
    if any(keyword in text for keyword in WEB_SCRAPING_KEYWORDS):
        return "web_scraping"
    if any(keyword in text for keyword in WORKFLOW_OR_LOGIC_KEYWORDS):
        return "workflow_or_logic"
    return "workflow_or_logic"
