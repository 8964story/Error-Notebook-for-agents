---
notebook_id: nb_provider_auth_003
title: Model unavailable
category: provider_auth
tags: [model, unavailable, provider]
risk: medium
version: 1
status: active
---

# Error: Model Unavailable

## Symptoms
- requested model is unavailable
- model alias not found
- provider rejects the selected model

## Root Cause
The requested model is disabled, unavailable for the current account, or mapped incorrectly in configuration.

## Fix
Verify the model name/alias, check provider availability, and switch to an available model if necessary.

## Verification
- Confirm the model appears in the provider's available model list
- Run a minimal request successfully against the corrected model
