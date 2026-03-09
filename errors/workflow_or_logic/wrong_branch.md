---
notebook_id: nb_workflow_001
title: Wrong logic branch
category: workflow_or_logic
tags: [logic, planning, intent]
risk: medium
version: 1
status: active
---

# Error: Wrong Logic Branch

## Symptoms
- workflow took the wrong branch
- agent solved a different problem than the user asked
- output is coherent but misaligned

## Root Cause
Intent was misread or an early assumption was not validated against the actual task goal.

## Fix
Restate the task goal, identify the wrong assumption, and re-run from the smallest decision point.

## Verification
- Confirm the new output answers the original task directly
- Confirm no stale assumption remains in the plan
