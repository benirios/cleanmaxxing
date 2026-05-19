import argparse
from engine.project_analyzer import ProjectAnalyzer
from engine.report_generator import ReportGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Cleanmaxxing code quality analyzer"
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Project or file path to analyze"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="cleanmaxxing-report.md",
        help="Output markdown report path"
    )

    args = parser.parse_args()

    analyzer = ProjectAnalyzer(args.path)
    project_report = analyzer.analyze()

    generator = ReportGenerator(project_report)
    report_path = generator.save(args.output)

    print(f"Cleanmaxxing report generated: {report_path}")


if __name__ == "__main__":
    main()