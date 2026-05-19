import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RULES_DIR = BASE_DIR / "rules"


class SearchEngine:
    def __init__(self):
        self.rules = []

    def load_csv(self, filename):
        path = RULES_DIR / filename

        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.rules.append(row)

    def load_all_rules(self):
        files = [
            "code-smells.csv",
            "architecture-rules.csv",
            "naming-rules.csv",
            "performance-rules.csv",
            "refactoring-patterns.csv",
        ]

        for file in files:
            self.load_csv(file)

    def search(self, query, language=None):
        results = []

        query = query.lower()

        for rule in self.rules:
            text = " ".join(str(v).lower() for v in rule.values())

            if query in text:
                score = 1

                if language and language.lower() in text:
                    score += 2

                results.append({
                    "score": score,
                    "rule": rule
                })

        results.sort(key=lambda x: x["score"], reverse=True)

        return results


if __name__ == "__main__":
    engine = SearchEngine()

    engine.load_all_rules()

    results = engine.search(
        query="long function duplication",
        language="python"
    )

    for result in results[:5]:
        print(result)