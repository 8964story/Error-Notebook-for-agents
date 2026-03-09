#!/usr/bin/env python3
"""Simple error classifier for routing to error notebooks."""

def classify(text: str) -> str:
    t = (text or '').lower()
    if any(k in t for k in ['timeout', 'api key', 'auth', 'cron', 'delivery', 'provider']):
        return 'api_call'
    if any(k in t for k in ['models.json', 'openclaw.json', 'file', 'path', 'encoding']):
        return 'file_io'
    if any(k in t for k in ['scrape', 'x.com', 'cloudflare', 'fetch', 'browser']):
        return 'web_scraping'
    return 'logic'

if __name__ == '__main__':
    import sys
    print(classify(' '.join(sys.argv[1:])))
