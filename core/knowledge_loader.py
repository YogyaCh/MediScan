from config.settings import REFERENCE_PATH

def load_knowledge(report_type: str) -> str:
    try:
        with open(f"{REFERENCE_PATH}/{report_type.lower()}_reference.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No domain knowledge available for this report type."
