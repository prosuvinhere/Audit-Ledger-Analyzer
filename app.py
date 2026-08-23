import streamlit as st
import duckdb
import platform
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import re 

# 1. OS Detection & Sidebar
current_os = platform.system()
os_message = "Windows environment detected." if current_os == "Windows" else f"{current_os} environment detected."

with st.sidebar:
    st.caption(f"System Check: {os_message}")
    st.markdown("### AI Engine Selection")
    model_choice = st.radio(
        "Choose your model based on your machine's RAM:",
        [
            "⚡ Fast (llama3.2:3b) - Best for 8GB RAM", 
            "🧠 Smart (llama3.1) - Needs 16GB+ RAM"
        ]
    )

st.title("Local Audit Ledger Analyzer")

# Determine which model string to pass to Ollama based on user selection
active_model = "llama3.2:3b" if "Fast" in model_choice else "llama3.1"

# 2 & 3. Multiple File Upload (2GB limit enabled via config.toml)
uploaded_files = st.file_uploader(
    "Upload Audit Files (CSVs up to 2GB)", 
    type="csv", 
    accept_multiple_files=True
)

if uploaded_files:
    table_schemas = []
    
    for file in uploaded_files:
        file_path = f"temp_{file.name}"
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        
        # Strip out illegal SQL characters and format the table name
        raw_name = file.name.split('.')[0]
        table_name = re.sub(r'\W+', '_', raw_name)
        
        if table_name[0].isdigit():
            table_name = f"tbl_{table_name}"
            
        # Safely wrap table name in double quotes for DuckDB views
        duckdb.query(f'CREATE OR REPLACE VIEW "{table_name}" AS SELECT * FROM read_csv_auto(\'{file_path}\')')
        
        schema_df = duckdb.query(f'DESCRIBE "{table_name}"').df()
        columns = ", ".join(schema_df['column_name'].tolist())
        table_schemas.append(f"Table '{table_name}' has columns: {columns}")
        
    st.success(f"{len(uploaded_files)} file(s) loaded successfully.")
    
    schema_context = "\n".join(table_schemas)
    user_question = st.text_input("Ask a question across your data (e.g., 'What are the top 5 highest debits?')")

    if user_question:
        llm = Ollama(model=active_model)
        
        # ADVANCED AUDIT PROMPT WITH FEW-SHOT EXAMPLES
        prompt = PromptTemplate.from_template("""
        You are an expert SQL assistant for financial auditors.
        Your task is to write a strictly valid DuckDB SQL query to answer the user's question based on the provided table schemas.
        
        Available Tables:
        {schema_context}
        
        CRITICAL RULES:
        1. Return ONLY the raw SQL query.
        2. Do NOT include markdown formatting like ``` or ```sql.
        3. Do NOT include any explanations, greetings, or conversational text.
        4. Always wrap column names in double quotes (e.g., "Debit") to prevent syntax errors.
        5. Use ILIKE for case-insensitive string matching.
        
        EXAMPLES:
        User Request: What is the total Debit for Payroll?
        SQL: SELECT SUM("Debit") FROM "mock_general_ledger" WHERE "Description" ILIKE '%Payroll%';
        
        User Request: Show me top 5 highest credit transactions.
        SQL: SELECT * FROM "mock_general_ledger" ORDER BY "Credit" DESC LIMIT 5;
        
        User Request: {question}
        SQL:
        """)
        
        formatted_prompt = prompt.format(schema_context=schema_context, question=user_question)
        
        try:
            st.write(f"Executing analytical query using {active_model}...")
            
            # The LLM invocation
            raw_response = llm.invoke(formatted_prompt)
            
            # Final safety net: Strip out any rogue markdown the model might still try to output
            sql_query = raw_response.replace("```sql", "").replace("```", "").strip()
            
            result_df = duckdb.query(sql_query).df()
            
            st.dataframe(result_df)
            st.download_button("Download Filtered Data", result_df.to_csv(index=False), "filtered_audit_data.csv")
            
        except Exception as e:
            st.error(f"Could not parse the request. Please rephrase. (Error: {e})")
            # Optional: Print the failed SQL to the terminal so you can debug what the LLM got wrong
            print(f"FAILED SQL ATTEMPT: {raw_response}")