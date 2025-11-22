# Tiny SQL Expert – SLM  
Natural language to SQL translator using Phi-3 Mini with a self-correction loop.

Tiny SQL Expert is a lightweight natural-language-to-SQL generator powered by **Phi-3 Mini 4K**.  
It converts user questions into **valid SQL queries**, enforces strict schema constraints, performs **JOIN-aware reasoning**, and includes an automated **self-correction mechanism** that regenerates SQL when validation fails.

This project demonstrates efficient SQL generation using a small language model, strong output control, and safe SQL validation.

---

## 🚀 Features

### 🔹 Natural Language → SQL
Transforms user queries into precise SQL statements using a compact 4B-parameter model.

### 🔹 Built-in Self-Correction
If the first attempt produces invalid SQL, the system automatically:

- Validates SQL syntax  
- Detects schema or JOIN errors  
- Re-prompts the model with error feedback  
- Generates a corrected SQL query  

### 🔹 Schema-Aware JOIN Reasoning
Understands and navigates a relational schema composed of:

- **Users**  
- **Orders**  
- **Products**  
- **OrderItems**

### 🔹 Strict Output Discipline
Returns **only SQL** — no explanations, no formatting.

### 🔹 Clean, Modular Architecture
Separate modules for inference, validation, schema rules, and CLI logic.

---

## 📁 Project Structure

<pre>
tiny-sql-expert/
│
├── main.py                 # CLI + self-correction loop
├── model_interface.py      # Model loading & inference
├── schema.py               # Schema & controlled BASE_PROMPT
├── sql_validator.py        # Syntax & schema validator
│
├── requirements.txt
├── sql_expert_demo.ipynb   # Google Colab demo notebook
│
├── INVALIDquery.png
├──  VALIDquery.png
</pre>



## 🏗️ System Architecture

<pre>
User Question
        ↓
Prompt (schema + rules)
        ↓
Phi-3 Mini (HuggingFace Transformers)
        ↓
Generated SQL
        ↓
SQL Validator ── Invalid? ── Yes → Retry with error feedback
                        │
                        No
                        ↓
                Final SQL Output
</pre>


<h2>🧩 Core Components</h2>

<h3><strong>main.py</strong></h3>
<ul>
  <li>Runs the interaction loop</li>
  <li>Implements retry/self-correction</li>
  <li>Extracts SQL-only output</li>
</ul>

<h3><strong>model_interface.py</strong></h3>
<ul>
  <li>Loads Phi-3 Mini</li>
  <li>Handles tokenization & inference</li>
</ul>

<h3><strong>schema.py</strong></h3>
<ul>
  <li>Defines DB schema</li>
  <li>Controls LLM behavior via BASE_PROMPT</li>
</ul>

<h3><strong>sql_validator.py</strong></h3>
<ul>
  <li>Validates SQL syntax</li>
  <li>Ensures schema compliance</li>
  <li>Blocks unsafe queries</li>
  <li>Returns errors for retrying</li>
</ul>

<hr>

<h2>📸 Demonstration</h2>

<h3>❌ Invalid SQL (Attempt 1)</h3>
<p><img src="screenshots/INVALIDquery.png" width="550"></p>
<p>Shows SQL rejected due to hallucinated column or table.</p>

<h3>✔ Corrected SQL (Attempt 2)</h3>
<p><img src="screenshots/VALIDquery.png" width="550"></p>
<p>Shows corrected SQL generated after retry.</p>

<p>These images demonstrate the system’s self-correction capability.</p>

<hr>

<h2>🔧 Installation</h2>

<h3>1. Clone the repository</h3>
<pre>
<code>
git clone https://github.com/jac1na/Tiny-SQL-Expert--SLM.git
cd Tiny-SQL-Expert--SLM
</code>
</pre>

<h3>2. Install dependencies</h3>
<pre>
<code>
pip install -r requirements.txt
</code>
</pre>

<h3>3. Run the application</h3>
<pre>
<code>
python main.py
</code>
</pre>

<hr>

<h2>🖥️ Example Usage</h2>

<p><strong>Input:</strong></p>
<pre>
<code>
List all products bought in the last 7 days.
</code>
</pre>

<p><strong>Output:</strong></p>
<pre>
<code>
SELECT p.name, SUM(oi.quantity) AS total_quantity
FROM Products p
JOIN OrderItems oi ON p.product_id = oi.product_id
JOIN Orders o ON oi.order_id = o.order_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY p.name;
</code>
</pre>

<hr>

<h2>🎒 Google Colab Notebook</h2>
<p>A Colab-friendly version of the project is available here:</p>

<p><a href="https://colab.research.google.com/drive/1zjJ2Lb4kCwrXO9RMfAVnRZXqFmBGhtXe#scrollTo=QFqPPQD5rHz5">
🔗 Colab Notebook
</a></p>

<hr>

<h2>🧾 License</h2>
<p>This project is released under the <strong>MIT License</strong>, allowing reuse, modification, and distribution.</p>

<hr>

<h2>👤 Author</h2>
<p><strong>JASINA</strong><br>
GitHub: <a href="https://github.com/jac1na">https://github.com/jac1na</a><br>
Email: <a href="mailto:jazsina7@gmail.com">jazsina7@gmail.com</a>
</p>


