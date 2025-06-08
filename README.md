# Fireplace.Life Email Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A specialized Python tool to extract customer email addresses from Fireplace.Life invoice Excel files. Enables creation of high-quality Lookalike Audiences for Facebook Ads campaigns by leveraging Meta's machine learning to target users similar to existing fireplace customers.

![Facebook Lookalike Audience](Images/Facebook-Lookalike-Audience.gif)

---

## Features

- 🔍 Recursive Excel file scanning (`.xlsx` and `.xls`)
- ✉️ Advanced email pattern recognition with validation
- 🧹 Automatic exclusion of temporary/backup files
- 📊 Progress tracking with real-time statistics
- ✅ Deduplication of email addresses
- 💾 CSV output with clean email formatting

---

## Use Case

```mermaid
graph TD

    %% ====== CORE WORKFLOW ====== %%
    A[📥 Invoice Excel Files] --> B[⚙️ Email Extraction]
    B --> C[🧹 Data Cleansing]
    C --> D[✅ Unique Emails]
    D --> E[📤 CSV Export]
    E --> F[👥 Facebook Lookalike]
    F --> G[🎯 Targeted Ads]
    G --> H[🔥 High-Intent Leads]
    
    %% ====== KEY FEATURES ====== %%
    B -.-> B1["• Scans all subfolders<br>• Reads XLSX/XLS formats<br>• Skips temp files"]
    C -.-> C1["• Smart email validation<br>• Case normalization<br>• Deduplication"]
    F -.-> F1["• Meta's AI analyzes 1000+ data points<br>• Finds similar purchase patterns<br>• Cross-platform behavior tracking"]
    
    %% ====== PERFORMANCE BENEFITS ====== %%
    H --> I[💰 Lower CPA]
    H --> J[📈 Higher ROAS]
    I & J --> K["🚀 3×+ better<br>performance"]
    
    %% ====== VS BASIC TARGETING ====== %%
    L[Basic Targeting] --- |"Limited to:<br>• Location<br>• Demographics<br>• Surface interests"| M[👎 Higher Cost]
    F --- |"Enables:<br>• AI similarity matching<br>• Behavioral prediction<br>• Dynamic optimization"| N[👍 Lower Cost]
```


## ⚡ Why Email-Based Lookalike Audiences?

| 🧠 **Aspect**             | 😬 **Basic Targeting**             | 🚀 **Email Lookalike**                          |
|---------------------------|------------------------------------|--------------------------------------------------|
| 📊 **Data Depth**         | ❌ Surface-level interests          | ✅ 1,000+ behavioral data points               |
| 🎯 **Precision**          | 🪤 Broad demographic groups         | 🎯 Algorithmic similarity matching             |
| 📉 **Conversion Rate**    | 🔻 ~9.2% average across industries | 📈 ~18–27% (2–3× lift; up to 32× in studies)    |
| 💸 **Cost per Lead**      | 💰 $15-22 industry average         | 💵 $3.75–6.36 (AdEspresso verified)             |
| 📈 **ROAS Improvement**   | 🟡 Baseline                        | 🟢 ~3× average ROAS; case example reached ~9.7× |

*Sources: AdEspresso, Meta Business, HubSpot*

Email-based lookalike audiences outperform basic targeting because:

- 🔍 **Meta's AI analyzes 1000+ data points per user** from your customer emails  
- 🧠 **Machine learning identifies patterns** in purchase behavior and preferences  
- 🎯 **Finds "twin audiences"** with similar characteristics to proven customers  
- 📈 **Boosts conversion rates by 2–3×** compared to interest-based targeting  
- 💰 **Cuts cost per lead by 50–80%**, based on Meta and AdEspresso benchmarks  

---

## 🚨 Key Differentiators You’re Missing Without Email Lookalikes

- 🔍 **Behavioral Prediction** – Targets users who *act* like your best customers, not just *look* like them  
- 🛒 **Purchase Intent Focus** – Zeroes in on users showing strong buying signals  
- 🤖 **Algorithmic Optimization** – Meta's AI continuously refines targeting based on conversions  
- 🌐 **Cross-Platform Insight** – Leverages the full Meta ecosystem (Instagram, WhatsApp, Facebook, etc.)
