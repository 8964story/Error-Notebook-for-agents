---
notebook_id: nb_provider_auth_002
title: Provider mismatch
category: provider_auth
tags: [provider, config, mismatch]
risk: medium
version: 1
status: active
---

# Error: Provider Mismatch

## Symptoms
- selected provider does not match configured model
- request routed to the wrong provider
- model alias resolves to an unsupported backend

## Root Cause
Model/provider configuration drift or a stale routing config caused the request to hit the wrong provider.

## Fix
Check the configured provider, verify the selected model alias, and align routing so the request targets the intended backend.

## Verification
- Confirm the active provider matches the intended model/backend
- Run a minimal request and verify the response comes from the expected provider
