# Error: Page Loaded But No Data

## Symptoms
- Browser page loads successfully
- extraction returns empty or irrelevant text
- agent reports success without target content

## Root Cause
Page shell loaded, but target content was not rendered, selected, or verified.

## Fix
Re-check the target selector/content region, wait for target-specific content, and verify the extracted output is semantically relevant.

## Verification
- Confirm extracted content is non-empty
- Confirm the extracted content contains the requested target data rather than page chrome/placeholders

## Tags
web_scraping
browser
silent_failure
