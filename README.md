# Local Audit Ledger Analyzer

A 100% offline, privacy-first analytics tool built for auditors. Easily upload large general ledgers or trial balances (CSVs up to 2 GB), ask questions in plain English, and receive filtered tabular results.

---

## 🔒 Privacy & Compliance
* **Zero Data Leaks:** All data processing and AI queries run entirely on your local machine.
* **No Cloud Calls:** No files, account details, or schemas are ever sent to external servers or third-party APIs.
* **Air-Gapped Ready:** After the initial one-time model setup, the application operates completely offline without an internet connection.

---

## ⚙️ Hardware & Model Selection Guide

Select the appropriate AI model in the sidebar based on your machine's available RAM:

| RAM Available | Recommended Model | Description | Best For |
| :--- | :--- | :--- | :--- |
| **8 GB or less** | `⚡ Fast (llama3.2:3b)` | Lightweight & low-memory footprint (~2 GB RAM usage). | Quick filters, threshold lookups, and basic aggregations without freezing your computer. |
| **16 GB or more** | `🧠 Smart (llama3.1)` | Full-reasoning model (~4.7 GB RAM usage). | Complex multi-step reasoning, cross-table `JOIN`s, and multi-condition audit checks. |

> **Recommendation:** If your laptop has 8 GB of RAM or if you are running heavy applications simultaneously (e.g., Excel workbooks, Teams, enterprise software), stick with the **Fast** model to ensure smooth performance.

---

## 🚀 Quick Start Instructions

### Prerequisites
1. **Python 3.9+**: Installed from [python.org](https://www.python.org/) or Microsoft Store.
2. **Ollama**: Installed from [ollama.com](https://ollama.com/download).

---

### Running the App

1. Download this repository as a `.zip` file and extract it to your preferred folder.
2. Launch the application according to your operating system:

* **Windows Users:**
  * Double-click `Launch_App.bat`.
* **macOS Users:**
  * Double-click `Launch_App.command`.
  *(If prompted about permissions on macOS, open Terminal and run: `chmod +x Launch_App.command`)*

> ⚠️ **Important (First Run Only):** Ensure your laptop is connected to the internet during the very first run so the script can download the local AI model weights. Once downloaded, you can disconnect from the internet entirely.

---

<img width="1440" height="900" alt="Screenshot 2026-08-23 at 10 42 35 PM" src="https://github.com/user-attachments/assets/3d20ba38-b05b-4ad3-9aef-881dd42bec3e" />


## 💡 How to Use
1. **Upload Files:** Upload one or multiple CSV files (General Ledgers, Trial Balances, Subledgers) up to 2 GB each.
2. **Select Model:** Choose your model (`Fast` or `Smart`) in the sidebar.
3. **Ask Questions:** Type your audit queries in plain English into the chat box, for example:
   * *"Show me all transactions where Debit is greater than 10,000."*
   * *"What is the total Credit amount for Account 4010?"*
   * *"List all entries with description containing 'Payroll' sorted by Date."*
4. **Export Results:** Review the resulting data table and click **Download Filtered Data** to export your results back into CSV format.
