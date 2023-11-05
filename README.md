# IntegrityWatcher
File Integrity Monitoring Project
# File Integrity Monitoring Project

This Python project allows you to monitor the integrity of files in a specified directory by creating a baseline of file hashes and continuously checking for changes or unauthorized file creations.

## Overview

File integrity monitoring is a crucial aspect of cybersecurity. This project helps you:

- Create a baseline of file hashes for files in the "Files" directory.
- Continuously monitor files for changes, new file creations, or deletions.
- Detect potential security breaches and unauthorized modifications to critical files.

## Project Details

- **calculate_file_hash**: A function to calculate the SHA-512 hash of a file.
- **erase_baseline_if_already_exists**: A function to delete the baseline file if it already exists.
- **User Interaction**: The script prompts the user to choose between creating a new baseline or monitoring files with an existing baseline.

## Usage

1. Choose 'A' to create a new baseline. This calculates the hashes of files and writes them to `baseline.txt`.
2. Choose 'B' to start monitoring. The script reads the baseline data from `baseline.txt` and notifies you of any changes or new file creations in the "Files" directory.

## Cybersecurity Implications

File integrity monitoring can be used for:

- Detecting unauthorized changes to system files.
- Early intrusion detection.
- Maintaining compliance with security standards and regulations.
- Preventing data exfiltration.
- Providing a log and alerting system for security incidents.
- Facilitating forensic analysis in the event of a security breach.

## Usage

You can run the Python script in your preferred environment. Make sure to adapt the file paths as needed for your specific setup.

```python
fileintegerity.py
