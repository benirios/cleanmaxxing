import ast


class CodeDetector:
    def __init__(self, code: str):
        self.code = code
        self.tree = ast.parse(code)

    def detect_long_functions(self, max_lines=40):
        issues = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                start = node.lineno
                end = getattr(node, "end_lineno", start)
                length = end - start + 1

                if length > max_lines:
                    issues.append({
                        "type": "long_function",
                        "name": node.name,
                        "lines": length,
                        "message": f"Function '{node.name}' has {length} lines."
                    })

        return issues

    def detect_deep_nesting(self, max_depth=4):
        issues = []

        def get_depth(node, depth=0):
            max_found = depth

            for child in ast.iter_child_nodes(node):
                if isinstance(child, (ast.If, ast.For, ast.While, ast.Try, ast.With)):
                    max_found = max(max_found, get_depth(child, depth + 1))
                else:
                    max_found = max(max_found, get_depth(child, depth))

            return max_found

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                depth = get_depth(node)

                if depth > max_depth:
                    issues.append({
                        "type": "deep_nesting",
                        "name": node.name,
                        "depth": depth,
                        "message": f"Function '{node.name}' has nesting depth {depth}."
                    })

        return issues

    def detect_magic_numbers(self):
        issues = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if node.value not in [0, 1, -1]:
                    issues.append({
                        "type": "magic_number",
                        "value": node.value,
                        "line": node.lineno,
                        "message": f"Magic number '{node.value}' found on line {node.lineno}."
                    })

        return issues

    def run_all(self):
        return (
            self.detect_long_functions()
            + self.detect_deep_nesting()
            + self.detect_magic_numbers()
        )