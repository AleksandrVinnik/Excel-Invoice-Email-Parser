# Fireplace.Life Email Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A specialized Python tool to extract customer email addresses from Fireplace.Life invoice Excel files. Enables creation of high-quality Lookalike Audiences for Facebook Ads campaigns by leveraging Meta's machine learning capabilities to target users similar to existing fireplace customers.

## Features

- 🔍 Recursive Excel file scanning (`xlsx` and `xls`)
- ✉️ Advanced email pattern recognition with validation
- 🧹 Automatic exclusion of temporary/backup files
- 📊 Progress tracking with real-time statistics
- ✅ Deduplication of email addresses
- 💾 CSV output with clean email formatting

## Use Case

```mermaid
graph LR
    A[Invoice Excel Files] --> B(Email Extraction)
    B --> C[Unique Customer Emails]
    C --> D[Facebook Lookalike Audience]
    D --> E[Targeted Ad Campaign]
    E --> F[High-Intent Fireplace Leads]
