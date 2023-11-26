# IntegrityWatcher

**File Integrity Monitoring Project with Email Alerts**

IntegrityWatcher is a Python-based solution designed for robust file integrity monitoring within a specified directory. This project empowers users to establish a secure baseline of file hashes, enabling continuous vigilance for unauthorized changes or new file creations. Notably, it includes features for SMTP email alerts and the ability to run as an executable on different systems.

## Project Overview

### Key Features

- **Baseline Creation**: Compute SHA-512 hashes for files in the "Files" directory to establish a secure foundation.
- **Continuous Monitoring**: Vigilantly observe files for changes, new additions, or deletions.
- **Security Breach Detection**: Swiftly identify potential security breaches or unauthorized file modifications.
- **SMTP Email Alerts**: Receive notifications via email for any unauthorized changes or new file additions.
- **Executable Usage**: Convert the script to an executable for seamless deployment on various systems.

### Key Components

1. **`calculate_file_hash(filepath)`**: Compute the SHA-512 hash of a file.
2. **`erase_baseline_if_already_exists()`**: Safeguard to erase an existing baseline for a fresh start.
3. **`log_change(action, file_path, username)`**: Log changes made to files, including action type, file path, and the user responsible.
4. **`notify_server_mailtrap(action, file_path, username)`**: Send email alerts using the Mailtrap SMTP server to notify about file changes.
5. **`get_username()`**: Retrieve the system user's username running the script.

## Usage

1. Choose 'A' to create a new baseline or 'B' to begin monitoring with an existing one.
2. Configure SMTP settings in `config.py` for email alerts.
3. Run the script in your preferred environment:

   ```bash
   python fileintegerity.py
## Enhancing Cybersecurity

IntegrityWatcher serves as a crucial component of cybersecurity, providing:

- **Unauthorized Changes Detection:** Identify unauthorized adjustments to system files.
- **Early Intrusion Detection:** Swiftly detect security breaches or unauthorized alterations.
- **Compliance Assurance:** Align with security standards by preserving file integrity.
- **Data Exfiltration Prevention:** Thwart unauthorized data access or exfiltration attempts.
- **Logging and Alerting:** Generate logs and receive alerts about potential security incidents.
- **Forensic Analysis:** Leverage baseline data and change history for comprehensive forensic analysis.

## Quick Start

Getting started with IntegrityWatcher is simple:

1. Run the Python script in your preferred environment:

   ```bash
   python fileintegerity.py
