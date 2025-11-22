from model_interface import run_model
from sql_validator import validate
from schema import BASE_PROMPT

def extract_sql(text):
    idx = text.lower().find("select")
    if idx == -1:
        idx = text.lower().find("with")
    if idx == -1:
        return text
    return text[idx:].strip()

def generate_sql(question):
    prompt = BASE_PROMPT + f"\nQuestion: {question}"

    for attempt in range(3):
        raw_output = run_model(prompt).strip()

       
        sql = extract_sql(raw_output)

        valid, error = validate(sql)

        if valid:
            print("\nGenerated SQL:\n")
            return sql
        print(f"[Attempt {attempt+1}] SQL INVALID. \nRetrying")
       

        # retry
        prompt = (
            BASE_PROMPT
            + f"\nThe previous SQL was invalid: {sql}"
            + f"\nError: {error}"
            + f"\nFix the SQL. Output ONLY SQL.\n"
            + f"Question: {question}"
        )

    return "ERROR: Could not generate valid SQL in 3 attempt ."

if __name__ == "__main__":
    q = input("Enter your question: ")
    
    print(generate_sql(q))