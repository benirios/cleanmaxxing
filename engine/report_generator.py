import os


class ReportGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate(self, results):
        report_path = os.path.join(self.output_dir, "report.md")

        with open(report_path, "w", encoding="utf-8") as report:
            report.write("# CleanMaxxing Report\n\n")

            total_files = len(results)
            report.write(f"Analyzed Files: {total_files}\n\n")

            for result in results:
                report.write(f"## {result['file']}\n\n")

                if "error" in result:
                    report.write(f"ERROR: {result['error']}\n\n")
                    continue

                findings = result.get("findings", [])

                if not findings:
                    report.write("No issues found.\n\n")
                    continue

                for finding in findings:
                    report.write(f"- {finding}\n")

                report.write("\n")

        return report_path