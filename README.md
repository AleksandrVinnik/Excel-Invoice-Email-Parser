# Fireplace.Life Email Extractor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A specialized Python tool to extract customer email addresses from Fireplace.Life invoice Excel files. Enables creation of high-quality Lookalike Audiences for Facebook Ads campaigns by leveraging Meta's machine learning to target users similar to existing fireplace customers.

## Features

- 🔍 Recursive Excel file scanning (`xlsx` and `xls`)
- ✉️ Advanced email pattern recognition with validation
- 🧹 Automatic exclusion of temporary/backup files
- 📊 Progress tracking with real-time statistics
- ✅ Deduplication of email addresses
- 💾 CSV output with clean email formatting

## ⚡ Why Use Email-Based Lookalike Audiences?

```mermaid
graph TD
    A[Targeting Options] --> B[Basic Facebook Targeting]
    A --> C[Email-Based Lookalike Audiences]
    
    B --> D[Demographics<br>Age, Gender, Location]
    B --> E[Interests<br>Home Improvement, Interior Design]
    B --> F[Behaviors<br>Online Shopping, DIY Projects]
    B --> G[Limited Accuracy]
    B --> H[Higher Cost Per Lead]
    
    C --> I[Meta's Machine Learning Algorithms]
    C --> J[1000+ Data Points Per User]
    C --> K[Purchase Behavior Patterns]
    C --> L[Similarity Matching]
    C --> M[Higher Quality Leads]
    C --> N[Lower Customer Acquisition Cost]
    
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#6f9,stroke:#333,stroke-width:4px
```

Email-based lookalike audiences outperform basic targeting because:

🔍 **Meta's AI analyzes 1000+ data points per user** from your customer emails  
🧠 **Machine learning identifies patterns** in purchase behavior and preferences  
🎯 **Finds "twin audiences"** with similar characteristics to proven customers  
📈 **Boosts conversion rates** by 2–3x compared to interest-based targeting  
💰 **Cuts cost per lead by up to 50%**, according to Meta case studies  

## ⚠️ Strategic Disadvantage of Basic Targeting vs. Email Lookalikes

| 🧠 **Aspect**            | 😬 **Basic Targeting**           | 🚀 **Email Lookalike**                        |
|--------------------------|----------------------------------|-----------------------------------------------|
| 📊 **Data Depth**         | ❌ Surface-level interests        | ✅ 1000+ behavioral data points               |
| 🎯 **Precision**          | 🪤 Broad demographic groups       | 🎯 Algorithmic similarity matching            |
| 📉 **Conversion Rate**    | 🔻 1–2% industry average          | 📈 3–5%+ documented results                   |
| 💸 **Cost per Lead**      | 💰 $15–50 industry average        | 💵 $5–15 documented results                   |
| 📈 **ROAS Improvement**   | 🟡 Baseline                      | 🟢 2.8× average increase                      |


---

## Use Case



```markdown
## 🔄 Value-Driven Workflow

```mermaid
graph TD
    subgraph "Data Preparation"
        A[📥 Invoice Excel Files] --> B[⚙️ Email Extraction]
        B --> C[🧹 Data Cleansing]
        C --> D[✅ Unique Emails]
    end
    
    subgraph "Audience Building"
        D --> E[📤 CSV Export]
        E --> F[👥 Facebook Audience]
    end
    
    subgraph "Performance Results"
        F --> G[🎯 Targeted Campaign]
        G --> H[🔥 High-Intent Leads]
        H --> I[💰 Lower CPA]
        H --> J[📈 Higher ROAS]
    end
    
    style subgraph fill:#f5f5f5,stroke:#bdbdbd,stroke-width:1px,color:#333
    style A fill:#e3f2fd,stroke:#2196f3
    style B fill:#bbdefb,stroke:#2196f3
    style C fill:#90caf9,stroke:#2196f3
    style D fill:#64b5f6,stroke:#2196f3
    style E fill:#42a5f5,stroke:#2196f3
    style F fill:#2196f3,stroke:#0d47a1
    style G fill:#1976d2,stroke:#0d47a1
    style H fill:#4caf50,stroke:#2e7d32
    style I fill:#ff9800,stroke:#ef6c00
    style J fill:#ff9800,stroke:#ef6c00
```

---

## 🚨 Key Differentiators You’re Missing Without Email Lookalikes

- 🔍 **Behavioral Prediction** – Targets users who *act* like your best customers, not just *look* like them  
- 🛒 **Purchase Intent Focus** – Zeroes in on users showing strong buying signals  
- 🤖 **Algorithmic Optimization** – Meta's AI continuously refines targeting based on conversions  
- 🌐 **Cross-Platform Insight** – Leverages the full Meta ecosystem (Instagram, WhatsApp, Facebook, etc.)  
> ⚠️ Sticking with basic targeting? You might be wasting **half your budget** on the wrong people.
