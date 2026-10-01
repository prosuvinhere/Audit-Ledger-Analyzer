# Private Audit Lakehouse

A 100% offline, air-gapped data lakehouse designed for strict audit environments. Combine the scalable storage of a data lake with the analytical querying power of a warehouse. Process highly sensitive General Ledgers, Trial Balances, and Subledgers (CSVs up to 2 GB) using plain English, with absolute cryptographic certainty that your client data never leaves your machine.

---

## 🔒 Security, Privacy & Compliance

Designed specifically for audit professionals handling restricted financial data under strict NDAs, this tool ensures complete data sovereignty:

* **Zero Data Exfiltration:** All data processing, indexing, and AI inference run strictly on `localhost`.
* **No Telemetry or Tracking:** The application contains zero usage trackers, crash reporters, or silent telemetry pings.
* **Strict Client Confidentiality:** Ensures frictionless compliance with enterprise data handling policies, SOC 2, GDPR, and strict client NDAs.
* **Metadata Protection:** Not only is the raw financial data kept local, but your table schemas, column names, and query history are also never transmitted to any third-party AI provider.
* **Ephemeral Processing:** Query execution happens entirely in local memory. Once you close the application, no residual AI context window or query cache is stored on external servers.
* **Air-Gapped Ready:** After the initial one-time local model download, the application can operate on a completely disconnected machine or within heavily restricted enterprise networks.

---

## ⚙️ Hardware & Model Selection Guide

Select the appropriate AI model in the sidebar based on your machine's available RAM. All models run completely on your local hardware:

| RAM Available | Recommended Model | Description | Best For |
| --- | --- | --- | --- |
| **8 GB or less** | `⚡ Fast (llama3.2:3b)` | Lightweight & low-memory footprint (~2 GB RAM usage). | Quick filters, threshold lookups, and basic aggregations while leaving system resources for enterprise software (e.g., Excel, Teams). |
| **16 GB or more** | `🧠 Smart (llama3.1)` | Full-reasoning model (~4.7 GB RAM usage). | Complex multi-step reasoning, cross-table `JOIN`s, and multi-condition anomaly detection. |

---

## 🚀 Quick Start Instructions

### Prerequisites

1. **Python 3.9+**: Installed from [python.org](https://www.python.org/) or Microsoft Store.
2. **Ollama**: Installed from [ollama.com](https://ollama.com/download) (Provides the localized AI environment).

---

### Running the App

1. Download this repository as a `.zip` file and extract it to a secure local directory.
2. Launch the application according to your operating system:

* **Windows Users:**
* Double-click `Launch_App.bat`. *(Note: If your corporate firewall flags the batch file, you can run `streamlit run app.py` directly from your terminal).*


* **macOS Users:**
* Double-click `Launch_App.command`.
*(If prompted about permissions, open Terminal and run: `chmod +x Launch_App.command`)*



> ⚠️ **Initial Setup Note:** You must be connected to the internet during the very first run to download the open-source AI weights directly to your machine. **Once the download completes, you can disconnect from the network entirely to analyze client data in a true air-gapped state.**

---

## 💡 How to Use

1. **Upload Secure Files:** Upload one or multiple CSV files up to 2 GB each directly into the browser to populate your local lakehouse. Data remains in your local system memory.
2. **Select Local Model:** Choose your isolated model (`Fast` or `Smart`) in the sidebar.
3. **Ask Questions:** Type your audit queries in plain English into the chat box, for example:
* *"Show me all transactions where Debit is greater than 10,000."*
* *"What is the total Credit amount for Account 4010?"*
* *"List all entries with description containing 'Payroll' sorted by Date."*


4. **Export Results:** Review the resulting data table and click **Download Filtered Data** to safely export your results back into a local CSV for your audit workpapers.
