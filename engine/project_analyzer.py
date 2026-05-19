import os

from engine.file_analyzer import FileAnalyzer, SUPPORTED_EXTENSIONS


class ProjectAnalyzer:
    def __init__(self, target_path):
        self.target_path = target_path
        self.file_analyzer = FileAnalyzer()

    def analyze(self):
        reports = []

        if os.path.isfile(self.target_path):
            if self._is_supported_file(self.target_path):
                reports.append(self.file_analyzer.analyze(self.target_path))
            return reports

        for root, dirs, files in os.walk(self.target_path):
            dirs[:] = [d for d in dirs if d not in ["node_modules", ".git", "__pycache__", "venv", ".venv"]]

            for file_name in files:
                file_path = os.path.join(root, file_name)

                if self._is_supported_file(file_path):
                    reports.append(self.file_analyzer.analyze(file_path))

        return reports

    def _is_supported_file(self, file_path):
        return any(file_path.endswith(ext) for ext in SUPPORTED_EXTENSIONS)