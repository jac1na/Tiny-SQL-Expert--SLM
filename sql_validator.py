import re
import sqlparse
from schema import ALLOWED_TABLES

FORBIDDEN = ["DROP", "DELETE", "ALTER"]

def has_forbidden_words(sql):
    return any(word in sql.upper() for word in FORBIDDEN)

def extract_identifiers(sql):
    tokens = sqlparse.parse(sql)[0].tokens
    identifiers = []
    for token in tokens:
        if token.ttype is None and hasattr(token, "tokens"):
            for sub in token.tokens:
                if sub.ttype is None:
                    identifiers.append(sub.value.lower())
    return identifiers

def validate_schema(sql):
    sql_lower = sql.lower()

    for table, cols in ALLOWED_TABLES.items():
        if table in sql_lower:
            # get all columns used in the SQL for this table
            for col in re.findall(rf"{table}\.\s*(\w+)", sql_lower):
                if col not in cols:
                    return False, f"Column '{col}' does not exist in table '{table}'."

    # Detect any tables used that aren’t in the schema
    for match in re.findall(r"from\s+(\w+)", sql_lower) + re.findall(r"join\s+(\w+)", sql_lower):
        if match not in ALLOWED_TABLES:
            return False, f"Table '{match}' does not exist in schema."

    return True, None

def validate(sql):
    if has_forbidden_words(sql):
        return False, "Forbidden keyword detected."

    try:
        parsed = sqlparse.parse(sql)
        if len(parsed) == 0:
            return False, "Unparsable SQL."
    except Exception:
        return False, "SQL parsing failed."

    # Schema validation
    ok, err = validate_schema(sql)
    if not ok:
        return False, err

    return True, None