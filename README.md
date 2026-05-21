![alt text](https://github.com/benirios/cleanmaxxing/blob/main/cmaxxing.png "Logo Title Text 1")
# Cleanmaxxing

English · Português · 简体中文 · 日本語 · 한국어

A light-weight code quality, architecture auditing, and automated refactoring system for Claude Code, Codex, Cursor, Windsurf, OpenCode, Gemini CLI, Copilot, and more.

Solves code entropy — the gradual degradation of readability, maintainability, and performance as AI-generated codebases scale.

npm version npm downloads GitHub stars License

```bash
npx cleanmaxxing@latest
```

Works on Mac, Windows, and Linux.

---

# Cleanmaxxing Install

“If your codebase became a mess after 3 weeks of vibe coding, this fixes it.”

“Finally a tool that audits architecture instead of just formatting code.”

“Feels like having a senior engineer constantly reviewing the entire repo.”

---

Trusted by developers building AI products, SaaS apps, internal tools, automation systems, and startup MVPs.

---

# Important

Returning to Cleanmaxxing?

Run:

```bash
/cleanmaxxing-map-codebase
```

to rebuild architecture awareness and refresh the audit index before running deeper analysis commands.

Your code is fine — Cleanmaxxing just needs updated structural context.

---

# Why I Built This

Most AI-generated codebases decay extremely fast.

The first few days feel productive — then suddenly:

- duplicated logic everywhere
- 900-line components
- broken abstractions
- inconsistent naming
- dead code
- impossible-to-debug architecture
- performance regressions
- “temporary” hacks everywhere

Traditional linters don’t solve this.

They detect syntax problems.

They don’t reason about architecture quality, maintainability, scalability, or long-term entropy.

So I built Cleanmaxxing.

The complexity lives inside the system:
- architecture analysis
- pattern detection
- code smell indexing
- context-aware refactoring
- structural scoring
- rule engines
- dependency analysis
- modularity auditing

What you see:
a few commands that continuously clean and stabilize your codebase.

---

# How It Works

The loop is simple.

## 1. Map the Codebase

```bash
/cleanmaxxing-map-codebase
```

Indexes:
- architecture
- frameworks
- conventions
- folder structure
- dependency graph
- component hierarchy
- code smells
- complexity hotspots

Builds the structural context used by all other commands.

---

## 2. Run a Full Audit

```bash
/cleanmaxxing-audit
```

Performs:
- architecture analysis
- complexity scoring
- duplicate detection
- performance inspection
- naming consistency checks
- modularity analysis
- maintainability scoring
- anti-pattern detection

Outputs a detailed `REPORT.md`.

---

## 3. Detect Structural Problems

```bash
/cleanmaxxing-detect
```

Finds:
- god objects
- fat components
- circular dependencies
- dead code
- over-engineering
- deeply nested logic
- bad abstractions
- repeated patterns
- broken separation of concerns

---

## 4. Refactor

```bash
/cleanmaxxing-refactor
```

Generates:
- cleaner abstractions
- modular architecture
- naming improvements
- folder restructuring
- extracted utilities
- simplified logic
- performance improvements

Without rewriting the entire codebase.

---

## 5. Verify

```bash
/cleanmaxxing-verify
```

Checks whether:
- refactors introduced regressions
- architecture improved
- complexity decreased
- maintainability score increased
- patterns became more consistent

---

## 6. Repeat

```bash
audit → detect → refactor → verify
```

Until the codebase becomes:
- maintainable
- scalable
- readable
- performant
- production-ready

---

# Getting Started

```bash
npx cleanmaxxing@latest
```

The installer prompts for:
- runtime
- global/local install
- rule profiles
- architecture strictness
- framework presets

Supported runtimes:
- Claude Code
- Codex
- Cursor
- Windsurf
- OpenCode
- Gemini CLI
- Copilot
- Kilo
- and more

---

# Core Commands

| Command | What it does |
|---|---|
| `/cleanmaxxing-map-codebase` | Index architecture and conventions |
| `/cleanmaxxing-audit` | Full code quality and architecture audit |
| `/cleanmaxxing-detect` | Detect structural and architectural issues |
| `/cleanmaxxing-refactor` | Generate cleaner implementations |
| `/cleanmaxxing-verify` | Verify improvements and regression safety |
| `/cleanmaxxing-report` | Generate maintainability report |
| `/cleanmaxxing-performance` | Analyze performance bottlenecks |
| `/cleanmaxxing-architecture` | Deep architecture analysis |
| `/cleanmaxxing-complexity` | Detect complexity hotspots |
| `/cleanmaxxing-dependencies` | Analyze dependency graph |
| `/cleanmaxxing-dead-code` | Find unused code and files |

---

# Why It Works

Most AI coding workflows fail for 3 reasons:

## 1. Context Rot

As context windows grow:
- quality drops
- duplication increases
- abstractions drift
- architecture collapses

Cleanmaxxing continuously rebuilds structural awareness.

---

## 2. No Architecture Awareness

Most tools:
- lint syntax
- format code
- maybe typecheck

They do not understand:
- system structure
- modularity
- maintainability
- dependency health
- scalability

Cleanmaxxing does.

---

## 3. No Long-Term Refactoring Loop

Most developers:
- keep shipping
- never restructure
- accumulate entropy

Cleanmaxxing creates a continuous cleanup pipeline.

---

# Features

## Architecture Analysis
- Layer validation
- Domain separation
- Dependency health
- Circular import detection
- Monolith detection

## Code Quality
- Naming consistency
- Complexity scoring
- Duplicate logic detection
- Dead code analysis
- Readability scoring

## Performance
- Render bottlenecks
- Unnecessary rerenders
- Heavy queries
- Expensive loops
- Memory waste

## Refactoring Engine
- Utility extraction
- Component splitting
- Service isolation
- Folder restructuring
- Hook decomposition
- Abstraction cleanup

---

# Configuration

Settings live in:

```bash
.cleanmaxxing/config.json
```

Example:

```json
{
  "mode": "strict",
  "architecture": true,
  "performance": true,
  "maxComplexity": 10,
  "detectDeadCode": true,
  "framework": "react"
}
```

---

# Report System

Cleanmaxxing generates:
- `REPORT.md`
- `ARCHITECTURE.md`
- `PERFORMANCE.md`
- `REFACTOR_PLAN.md`

Each report contains:
- severity scoring
- file references
- detected issues
- recommended fixes
- maintainability insights

---

# Example Workflow

```bash
/cleanmaxxing-map-codebase

/cleanmaxxing-audit

/cleanmaxxing-detect

/cleanmaxxing-refactor

/cleanmaxxing-verify
```

---

# Philosophy

AI-generated code should not become:
- unreadable
- bloated
- over-engineered
- fragile

Cleanmaxxing exists to continuously compress entropy and keep AI-built systems production-grade.

---

# Troubleshooting

Commands not showing up?

Restart your runtime after installation.

Typical install locations:
- `~/.claude/skills/`
- `~/.codex/skills/`
- runtime-specific skill directories

---

Something broken?

Re-run the installer:

```bash
npx cleanmaxxing@latest
```

The installer is idempotent.

---

# Community

| Project | Platform |
|---|---|
| Cleanmaxxing | GitHub |
| Discussions | Discord |
| Updates | X (Twitter) |

---

# License

MIT License. See `LICENSE` for details.
