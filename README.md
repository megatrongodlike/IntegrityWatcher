# IntegrityWatcher

**File Integrity Monitoring Project**

IntegrityWatcher is a Python-based solution that empowers you to vigilantly monitor the integrity of files within a specified directory. By creating a baseline of file hashes, it continuously observes for unauthorized changes or new file creations.

## Project Overview

File integrity monitoring is a cornerstone of cybersecurity. The IntegrityWatcher project offers the following capabilities:

- **Baseline Creation**: Establish a secure foundation by computing SHA-512 hashes for files in the "Files" directory.
- **Continuous Monitoring**: Vigilantly oversee files for changes, new file additions, or deletions.
- **Security Breach Detection**: Swiftly identify potential security breaches or unauthorized file modifications.

## Key Features

- **calculate_file_hash**: A robust function for meticulously computing the SHA-512 hash of a file.
- **erase_baseline_if_already_exists**: A safeguard for erasing an existing baseline, ensuring a fresh start if needed.
- **User Interaction**: A user-friendly interface offering options to create a new baseline or monitor files using an existing one.

## Usage

Experience the power of IntegrityWatcher with these straightforward steps:

1. Choose 'A' to initiate the creation of a new baseline. This process computes file hashes and records them in `baseline.txt`.

2. Opt for 'B' to begin monitoring. The script retrieves the baseline data from `baseline.txt` and promptly informs you of any file alterations or new additions in the "Files" directory.

## Enhancing Cybersecurity

IntegrityWatcher serves as a critical component of cybersecurity:

- **Unauthorized Changes Detection**: Remain vigilant about system files to identify any unauthorized adjustments.
- **Early Intrusion Detection**: Swiftly detect security breaches or unauthorized alterations.
- **Compliance Assurance**: Align with security standards and regulations by preserving file integrity.
- **Data Exfiltration Prevention**: Thwart unauthorized data access or exfiltration attempts.
- **Logging and Alerting**: Generate logs and receive alerts about potential security incidents effortlessly.
- **Forensic Analysis**: In the event of a security breach, leverage the baseline data and change history for comprehensive forensic analysis.

## Quick Start

Run the Python script in your preferred environment. Ensure that you customize file paths as needed to suit your specific setup:

```python
fileintegerity.py
