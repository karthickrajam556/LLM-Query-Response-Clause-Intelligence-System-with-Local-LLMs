import subprocess

def run_ollama_model(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'gemma:2b'],
        input=prompt.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode('utf-8').strip()

def answer_query(query, clauses):
    prompt = f"""You are an AI assistant. Based on the clauses below, answer the user's question and reference relevant clause(s).

Query: {query}

Clauses:
{chr(10).join([f"Clause {i+1}: {c}" for i, c in enumerate(clauses)])}

Answer:"""
    return run_ollama_model(prompt)
