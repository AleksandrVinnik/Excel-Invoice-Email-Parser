# Fireplace.Life Email Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A specialized Python tool to extract customer email addresses from Fireplace.Life invoice Excel files. Enables creation of high-quality Lookalike Audiences for Facebook Ads campaigns by leveraging Meta's machine learning to target users similar to existing fireplace customers.

---

## Features

- 🔍 Recursive Excel file scanning (`xlsx` and `xls`)
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
    I & J --> K["3–5× better<br>performance"]
    
    %% ====== VS BASIC TARGETING ====== %%
    L[Basic Targeting] --- |"Limited to:<br>• Location<br>• Demographics<br>• Surface interests"| M[Higher Cost]
    F --- |"Enables:<br>• AI similarity matching<br>• Behavioral prediction<br>• Dynamic optimization"| N[Lower Cost]
    
    %% ====== STYLING ====== %%
    classDef main fill:#e3f2fd,stroke:#2196f3,stroke-width:2px;
    classDef feat fill:#bbdefb,stroke:#64b5f6,stroke-width:1px;
    classDef perf fill:#c8e6c9,stroke:#4caf50;
    classDef comp fill:#fff8e1,stroke:#ffc107;

    class A,B,C,D,E,F,G main;
    class B1,C1,F1 feat;
    class H,I,J,K perf;
    class L,M,N comp;

    linkStyle 0,1,2,3,4,5,6 stroke:#1976d2,stroke-width:2px;
    linkStyle 7,8,9 stroke:#64b5f6,stroke-width:1px,stroke-dasharray:3;
    linkStyle 10,11,12 stroke:#4caf50,stroke-width:2px;
    linkStyle 13,14 stroke:#ff9800,stroke-width:2px;


```

---

## ⚡ Why Use Email-Based Lookalike Audiences?

| 🧠 **Aspect**            | 😬 **Basic Targeting**           | 🚀 **Email Lookalike**                        |
|--------------------------|----------------------------------|-----------------------------------------------|
| 📊 **Data Depth**         | ❌ Surface-level interests        | ✅ 1000+ behavioral data points               |
| 🎯 **Precision**          | 🪤 Broad demographic groups       | 🎯 Algorithmic similarity matching            |
| 📉 **Conversion Rate**    | 🔻 1–2% industry average          | 📈 3–5%+ documented results                   |
| 💸 **Cost per Lead**      | 💰 $15–50 industry average        | 💵 $5–15 documented results                   |
| 📈 **ROAS Improvement**   | 🟡 Baseline                      | 🟢 2.8× average increase                      |

Email-based lookalike audiences outperform basic targeting because:

🔍 **Meta's AI analyzes 1000+ data points per user** from your customer emails  
🧠 **Machine learning identifies patterns** in purchase behavior and preferences  
🎯 **Finds "twin audiences"** with similar characteristics to proven customers  
📈 **Boosts conversion rates** by 2–3x compared to interest-based targeting  
💰 **Cuts cost per lead by up to 50%**, according to Meta case studies  

---

## 🚨 Key Differentiators You’re Missing Without Email Lookalikes

- 🔍 **Behavioral Prediction** – Targets users who *act* like your best customers, not just *look* like them  
- 🛒 **Purchase Intent Focus** – Zeroes in on users showing strong buying signals  
- 🤖 **Algorithmic Optimization** – Meta's AI continuously refines targeting based on conversions  
- 🌐 **Cross-Platform Insight** – Leverages the full Meta ecosystem (Instagram, WhatsApp, Facebook, etc.)  
> ⚠️ Sticking with basic targeting? You might be wasting **half your budget** on the wrong people.
