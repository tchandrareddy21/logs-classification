from pipeline.regex_classifier import classify_with_regex
from pipeline.ml_classifier import  classify_with_ml
from pipeline.llm_classifier import classify_with_llm
import pandas as pd

def classify_log(source, log_message):
    print(f"Log message: {log_message}")
    if source == "LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if not label:
            label = classify_with_ml(log_message)
    return label

def classify(logs):
    return [classify_log(source, log_message) for source, log_message in logs]

