# Cleanmaxxing

AI-powered code quality auditing and refactoring engine focused on clean architecture, maintainability, performance, and scalable engineering practices.

---

# Installation

## NPX (Recommended)

Run instantly without installing globally:

```bash
npx cleanmaxxing ./your-project
```

---

## Global Installation

```bash
npm install -g cleanmaxxing
```

Then run:

```bash
cleanmaxxing ./your-project
```

---

## Local Development Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd cleanmaxxing
```

Install dependencies:

```bash
npm install
```

Run locally:

```bash
node cli.js ./your-project
```

---

# Usage

## Analyze a Project

```bash
npx cleanmaxxing ./src
```

or

```bash
cleanmaxxing ./src
```

---

# Example Output

```txt
[✓] Scanning project...
[✓] Running detectors...
[✓] Applying engineering rules...
[✓] Generating report...

Report generated:
reports/report.md
```

---

# Features

- Code smell detection
- Architecture auditing
- Performance analysis
- Complexity detection
- Naming consistency validation
- Refactor suggestions
- Rule-based scoring system
- Search-engine-powered rule matching
- AI-friendly markdown reports

---

# What Cleanmaxxing Detects

## Code Smells

- Long functions
- Deep nesting
- Duplicate logic
- God classes
- Large files
- Dead code

## Architecture Issues

- Tight coupling
- Circular dependencies
- Layer violations
- Poor modularization

## Performance Problems

- Expensive loops
- Repeated computations
- Inefficient patterns
- Heavy rendering logic

## Maintainability Risks

- High complexity
- Poor naming
- Low cohesion
- Large responsibilities

---

# Project Structure

```txt
cleanmaxxing/
│
├── cleanmaxxing.py
├── cli.py
├── cli.js
├── install.js
│
├── engine/
│   ├── detectors.py
│   ├── file_analyzer.py
│   ├── project_analyzer.py
│   ├── report_generator.py
│   └── search_engine.py
│
├── prompts/
│   └── rule-engine.md
│
├── rules/
│   ├── architecture-rules.csv
│   ├── code-smells.csv
│   ├── complexity-thresholds.csv
│   ├── naming-rules.csv
│   └── performance-rules.csv
│
└── reports/
    └── report.md
```

---

# Report System

Cleanmaxxing generates structured markdown reports including:

- Architecture analysis
- Complexity warnings
- Naming violations
- Performance risks
- Refactor opportunities
- Engineering scores

Output:

```txt
reports/report.md
```

---

# Rule Engine

Rules are CSV-driven for speed and extensibility.

Example:

```csv
pattern,severity,recommendation
long_function,high,Extract smaller methods
deep_nesting,medium,Reduce conditional complexity
```

This allows:

- Easy customization
- Community rule packs
- AI-generated rules
- Fast pattern matching

---

# Search Engineering System

The internal search engine powers:

- Rule lookup
- Pattern prioritization
- Semantic matching
- Detector routing

Core file:

```txt
engine/search_engine.py
```

---

# Vision

Cleanmaxxing aims to become:

- An AI-native code quality standard
- A universal engineering auditing layer
- A scalable refactoring intelligence engine

The goal is not just clean code.

The goal is scalable systems, maintainable engineering, and efficient architecture.

---

# Future Roadmap

- AST-based analysis
- Multi-language support
- GitHub Actions integration
- VSCode extension
- Auto-refactors
- Technical debt scoring
- Complexity heatmaps
- Architecture visualization
- CI/CD enforcement
- Security auditing

---

# Contributing

Contributions are welcome.

Ideas:

- New detectors
- Better rules
- Language parsers
- Performance optimizations
- AI integrations

---

# License

MIT License
