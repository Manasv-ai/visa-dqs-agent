from transformers import pipeline

llm = pipeline("text-generation", model="gpt2")

def generate_insight(scores, composite):
    prompt = f"""
    You are a payments data quality analyst.

    Scores:
    {scores}

    Composite DQS: {composite}

    Explain:
    1. Key data quality risks
    2. Business impact in payments context
    3. Top 2 fixes in simple language
    """

    output = llm(prompt, max_length=200, do_sample=True)
    return output[0]["generated_text"]
