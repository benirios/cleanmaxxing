import sys

from engine.project_analyzer import ProjectAnalyzer
from engine.report_generator import ReportGenerator


def generate_project_report(root_path):
    analyzer = ProjectAnalyzer(root_path)
    project_report = analyzer.analyze()

    generator = ReportGenerator()
    report_path = generator.generate(project_report)

    print(f"CleanMaxxing report generated: {report_path}")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    generate_project_report(target)