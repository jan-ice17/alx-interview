# 📈 Log Parsing Script

This Python script reads logs from standard input line-by-line and computes key metrics. It processes log data according to a specific format and provides real-time metrics every 10 lines or upon keyboard interruption (`CTRL + C`).

## 📋 Input Format

The expected log format for each line is as follows:

- **IP Address**: IP address of the request.
- **Date**: Date and time of the request.
- **Status Code**: HTTP response status code (e.g., `200`, `404`).
- **File Size**: Size of the file or request in bytes.

⚠️ *Lines that do not follow this format are skipped.*

## 🛠️ Features

- **Total File Size**: Continuously updates the total of all `<file size>` values.
- **HTTP Status Code Tracking**: Counts and tracks the number of occurrences for specific HTTP status codes:
  - Supported codes: `200`, `301`, `400`, `401`, `403`, `404`, `405`, and `500`.
  - Only prints the status codes that appear, sorted in ascending order.
- **Real-Time Statistics**: Displays metrics every 10 lines and on keyboard interruption (`CTRL + C`).

## 🚀 Getting Started

### Prerequisites
- **Python 3**: Make sure you have Python 3 installed.

### Installation
1. Clone the repository or download the script.
2. Make the script executable (on Unix-based systems):
   ```bash
   chmod +x script.py
