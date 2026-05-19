Perfeito — vamos criar o Searching Engineering System para o cleanmaxxing.

A ideia: o sistema pesquisa regras de código limpo por categoria, prioridade, linguagem, problema e contexto.

## Searching Engineering System
The cleanmaxxing skill uses a searchable engineering system to retrieve the most relevant clean-code rules, patterns, refactors, and optimizations.
### Search Objectives
The search system must help identify:
- code smells
- architecture violations
- naming problems
- complexity issues
- performance problems
- refactoring opportunities
- language-specific best practices
### Search Inputs
The assistant should search using:
- user request
- programming language
- framework
- file type
- detected code smell
- performance bottleneck
- architecture layer
- priority level
### Searchable Databases
The system uses these CSV databases:
```txt
data/code-smells.csv
data/architecture-rules.csv
data/complexity-thresholds.csv
data/naming-rules.csv
data/performance-rules.csv
data/refactoring-patterns.csv

Search Priority

Results should be ranked by:

1. Direct match to user's problem
2. Programming language relevance
3. Framework relevance
4. Severity
5. Maintainability impact
6. Performance impact
7. Simplicity of implementation

Rule Matching Logic

IF code contains duplication
THEN search refactoring-patterns.csv for "Extract Function", "Extract Class", "Strategy Pattern"
IF function is too long
THEN search complexity-thresholds.csv and refactoring-patterns.csv
IF variable names are unclear
THEN search naming-rules.csv
IF code is slow
THEN search performance-rules.csv
IF structure is messy
THEN search architecture-rules.csv
IF code has hidden bugs or bad practices
THEN search code-smells.csv

Output Format

Every search result should return:

Problem detected:
Rule matched:
Severity:
Why it matters:
Recommended fix:
Example before:
Example after:

Search Behavior

The assistant must not blindly apply every rule.

It should:

* prioritize high-impact fixes
* avoid overengineering
* explain tradeoffs
* challenge weak assumptions
* preserve existing behavior
* prefer simple improvements over clever abstractions

Core Principle

Clean code is not code with more patterns.

Clean code is code that is:

easy to read
easy to change
hard to misuse
efficient enough
simple by default