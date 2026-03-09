# Error: API Key Missing

## Symptoms
- OpenAI API key missing
- auth not configured for provider
- request fails before model invocation

## Root Cause
Environment variable or provider auth profile is missing.

## Fix
Set the required API key or switch to a provider/model that already has valid auth configured.

## Verification
- Check the required API key/profile is present
- Run a minimal request and confirm a real response is returned

## Tags
api_call
auth
provider
