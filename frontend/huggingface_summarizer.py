from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_tokens=1300):
    max_input = 1024  # tokens (around 1500 words)
    input_text = text[:4000]  # roughly fit in 1024 tokens

    summary = summarizer(input_text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def simplify_text(text):
    prompt = (
        "Simplify the following text for easy understanding:\n\n"
        f"{text}"
    )
    result = summarizer(prompt, max_length=200, min_length=50, do_sample=False)
    return result[0]['summary_text']
