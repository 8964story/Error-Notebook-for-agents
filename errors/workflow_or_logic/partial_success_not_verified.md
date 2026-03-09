---
notebook_id: nb_workflow_002
title: Partial success not verified
category: workflow_or_logic
tags: [partial_success, verification, workflow]
risk: high
version: 1
status: active
---

# Error: Partial Success Not Verified

## Symptoms
- part of the task succeeded
- agent reported success too early
- downstream artifact is missing or incomplete

## Root Cause
The workflow stopped after the first successful step and skipped explicit end-state verification.

## Fix
Define the true completion condition, re-run the missing steps, and verify final artifacts instead of intermediate status.

## Verification
- Confirm all expected final artifacts exist
- Confirm the reported success matches the user's actual task goal
