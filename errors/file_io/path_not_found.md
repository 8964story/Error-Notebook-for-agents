# Error: Path Not Found

## Symptoms
- File not found
- no such file or directory
- config path invalid

## Root Cause
Wrong working directory, wrong relative path, or stale path reference.

## Fix
Inspect the current working directory, validate the intended file path, and update the command/config to the correct path.

## Verification
- Confirm the corrected path exists
- Confirm the file is the intended artifact, not just any existing file

## Tags
file_io
path
config
