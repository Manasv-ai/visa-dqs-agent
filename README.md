GenAI Data Quality Scoring (DQS) Agent for Payments

An AI-powered Data Quality Agent that automatically analyzes large-scale payments datasets, computes Data Quality Scores (DQS) across key dimensions, and explains business impact & remediation steps using Generative AI.

Built for fast evaluation of payment data reliability in fintech, banking, and transaction-heavy systems.

🧠 Problem Statement

In payments and fintech systems, poor data quality leads to:

Failed settlements

Incorrect fraud detection

Revenue leakage

Regulatory compliance risks

Traditional data quality checks are:

Manual

Rule-heavy

Hard to interpret for business users

This project solves that gap by combining:

Automated data quality scoring

Large-scale CSV handling

GenAI-based human-readable insights

✨ Key Features
📊 Automated Data Quality Scoring

The agent evaluates datasets across core dimensions:

Completeness – Missing values detection

Uniqueness – Duplicate transaction analysis

Validity – Type & value sanity checks

Timeliness – Data freshness evaluation

🤖 GenAI-Powered Explanation

Uses a language model to:

Identify key data risks

Explain business impact in payments context

Suggest top corrective actions

🧠 Smart Dimension Detection

Automatically detects applicable quality dimensions based on:

Column names

Data types

Dataset structure

🖥️ Interactive UI (Streamlit)

Upload large CSV files

View detected dimensions

Visualize quality scores

Read AI-generated explanations

⚙️ Scalable Data Simulation

Includes a synthetic 200MB payments dataset generator for stress testing and demos.

🏗️ Project Architecture
visa-dqs-agent/
│
├── app.py                  # Streamlit UI entry point
├── scoring_engine.py       # Core DQS computation logic
├── dimension_detector.py   # Automatic dimension detection
├── llm_agent.py            # GenAI explanation engine
├── genrate_dataset.py      # Large payments dataset generator
├── requirements.txt
├── Dockerfile
└── sample_data/

🧪 Data Quality Dimensions
Dimension	Description
Completeness	Missing values across dataset
Uniqueness	Duplicate transaction detection
Validity	Basic value and type correctness
Timeliness	Freshness of transaction data
🚀 How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/Manasv-ai/visa-dqs-agent.git
cd visa-dqs-agent

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

4️⃣ Upload a CSV

Upload a payments dataset (.csv) and let the agent analyze it.

🧠 Example Output

Detected data quality dimensions

Individual DQS scores (progress bars)

Composite Data Quality Score

AI-generated explanation covering:

Risks

Business impact

Actionable fixes

🧩 Tech Stack

Python

Pandas / NumPy

Streamlit

Hugging Face Transformers

Generative AI (LLM-based explanation)

Docker (optional deployment)

📈 Use Cases

FinTech & Payments companies

Banking data validation

Fraud detection pipelines

Data engineering quality checks

AI-powered analytics platforms

🔮 Future Improvements

Replace GPT-2 with instruction-tuned LLMs (GPT-4 / LLaMA-3 / Mixtral)

Domain-specific validity rules (amount, currency, status)

RAG with regulatory data quality standards

Per-dimension AI agents

Cloud deployment (AWS / GCP)

👨‍💻 Author

Manas Khatri

AI / GenAI Engineer

FinTech & Data Systems Enthusiast
