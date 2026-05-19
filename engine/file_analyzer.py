from engine.search_engine import SearchEngine

SUPPORTED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".html",
    ".css",
    ".java",
    ".go",
    ".rs",
    ".cpp",
    ".c",
    ".cs"
]


class FileAnalyzer:
    def __init__(self):
        self.search_engine = SearchEngine()

    def analyze(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()

            findings = self.search_engine.search(content)

            return {
                "file": file_path,
                "findings": findings
            }

        except Exception as error:
            return {
                "file": file_path,
                "error": str(error),
                "findings": []
            }