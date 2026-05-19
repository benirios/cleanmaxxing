
---
name: cleanmaxxing
description: Code cleanliness, architecture, maintainability, and performance intelligence with enforceable engineering standards
---
# cleanmaxxing
Comprehensive engineering guide for writing scalable, maintainable, efficient, and production-grade code.
Contains:
- Clean architecture rules
- Naming conventions
- File structure systems
- Performance optimization patterns
- Reusability heuristics
- Anti-pattern detection
- Refactoring workflows
- Testing standards
- API and database design principles
- Security and scalability rules
- Language/framework-specific best practices
---
# Philosophy
The objective of cleanmaxxing is:
> Make code easy to read, easy to maintain, hard to break, and efficient at scale.
Priority order:
1. Readability
2. Maintainability
3. Predictability
4. Scalability
5. Performance
6. Cleverness (LAST)
Good code:
- Explains itself
- Minimizes cognitive load
- Avoids unnecessary abstraction
- Makes bugs obvious
- Is consistent
- Scales without chaos
---
# Prerequisites
Check if tooling exists:
```bash
node -v
npm -v
python3 --version || python --version
git --version

Optional tooling:

npm install -g eslint prettier typescript

Recommended:

npm install -D eslint prettier husky lint-staged

⸻

How to Use This Skill

When user requests:

* refactor
* optimize
* clean
* improve
* organize
* scale
* productionize
* debug
* simplify
* architect
* review

follow this workflow.

⸻

Step 1: Analyze the Codebase

Extract:

* Language/framework
* Architecture style
* Performance bottlenecks
* Complexity level
* Naming consistency
* State management patterns
* File organization quality
* Reusability quality
* Testing coverage
* Scalability risks

Identify:

* code smells
* dead code
* unnecessary abstraction
* duplicate logic
* render waste
* large components
* tight coupling
* deep nesting
* weak naming
* state chaos
* excessive dependencies

⸻

Step 2: Run Cleanmaxxing Audit (REQUIRED)

Always audit these areas:

Category	Goal
Readability	Easy to understand
Maintainability	Easy to modify
Simplicity	Minimal complexity
Consistency	Predictable patterns
Performance	Efficient execution
Scalability	Handles growth
Reusability	Avoid duplication
Separation of concerns	Clear responsibilities
DX	Developer-friendly
Security	Safe by default
Testing	Reliable behavior

⸻

Step 3: Refactor Hierarchically

Always improve in this order:

1. Remove dead code
2. Simplify logic
3. Improve naming
4. Reduce nesting
5. Split responsibilities
6. Improve architecture
7. Optimize performance
8. Add abstractions ONLY if necessary

⸻

Step 4: Validate Improvements

Ensure:

* functionality unchanged
* performance improved
* readability improved
* complexity reduced
* scalability increased

⸻

Core Principles

1. Readability Over Cleverness

Good

const isUserAuthenticated = user.token !== null

Bad

const auth = !!user?.token

Prefer explicitness over smart-looking code.

⸻

2. Single Responsibility Principle

Each:

* function
* file
* component
* hook
* service
* module

should have ONE responsibility.

Bad

handleCheckout()

Handles:

* validation
* analytics
* payment
* emails
* redirects

Good

validateCart()
processPayment()
trackPurchase()
sendReceipt()
redirectToSuccess()

⸻

3. Predictable Structure

Codebases should feel:

* repetitive
* familiar
* systematic

NOT “creative”.

Consistency beats originality.

⸻

4. Optimize AFTER Clarity

Never prematurely optimize.

Bad engineers:

* micro-optimize early
* destroy readability
* create accidental complexity

Only optimize:

* measured bottlenecks
* large datasets
* render-heavy components
* expensive operations
* network-heavy systems

⸻

Naming Conventions

Variables

Good

const filteredProducts
const isPaymentSuccessful
const activeSubscriptions

Bad

const data
const temp
const thing
const x

Names must reveal intent instantly.

⸻

Functions

Functions should describe:

* WHAT they do
* NOT HOW they do it

Good

calculateInvoiceTotal()
filterActiveUsers()
sendVerificationEmail()

Bad

handleData()
process()
doStuff()

⸻

Components

Good

<ProductCard />
<CheckoutForm />
<UserAvatar />

Bad

<Card />
<Item />
<Box />

Generic names increase cognitive load.

⸻

File Structure Rules

Preferred Structure

src/
├── components/
├── features/
├── services/
├── hooks/
├── utils/
├── lib/
├── types/
├── constants/
├── store/
├── pages/
└── tests/

⸻

Component Rules

Component Size

If a component exceeds:

* ~250 lines
* multiple responsibilities
* excessive state
* multiple rendering concerns

split it.

⸻

Avoid God Components

Bad

Dashboard.tsx

Contains:

* API calls
* charts
* filters
* forms
* modals
* state
* business logic

Good

Separate:

* hooks
* services
* UI sections
* business logic
* utilities

⸻

State Management Rules

Keep State Local First

Prefer:

1. local state
2. lifted state
3. context
4. global store

Avoid global state unless truly shared.

⸻

Derived State Should NOT Be Stored

Bad

const [filteredUsers, setFilteredUsers]

Good

const filteredUsers = users.filter(...)

⸻

Performance Rules

Prevent Unnecessary Renders

Avoid inline functions in massive lists:

Bad

onClick={() => handleClick(id)}

⸻

Memoize ONLY When Needed

Bad

useMemo everywhere

Good Use Cases

* expensive calculations
* stable references
* render bottlenecks
* dependency-heavy computations

⸻

Lazy Load Heavy Features

Use:

* dynamic imports
* route splitting
* virtualization
* pagination

for large applications.

⸻

API Design Rules

Separate Layers Properly

Never mix:

* UI
* API
* database
* business logic

inside the same module.

⸻

Recommended Layer Pattern

components → hooks → services → API

⸻

Database Rules

Avoid N+1 Queries

Batch requests whenever possible.

⸻

Index Frequently Queried Fields

Especially:

* IDs
* slugs
* timestamps
* foreign keys

⸻

Error Handling Rules

Never Swallow Errors

Bad

try {
} catch {}

Good

catch (error) {
  logger.error(error)
  showToast("Something went wrong")
}

⸻

Type Safety Rules

Avoid any

Bad

const data: any

Good

interface User
type Product

⸻

Complexity Rules

Comment Rule

If comments are required to explain logic,
the code is probably too complex.

Refactor first.

⸻

Nesting Rule

If nesting exceeds 3 levels:

* extract function
* use guard clauses
* simplify conditions

⸻

Boolean Complexity Rule

Bad

if (
  isAdmin &&
  isOwner &&
  isVerified &&
  !isSuspended &&
  hasPermission
)

Good

const canManageProject = ...

⸻

Anti-Patterns

Avoid Massive Utility Files

Bad

helpers.ts
utils.ts
misc.ts
common.ts

Split utilities by domain.

⸻

Avoid Premature Abstraction

Bad

AbstractButtonFactoryManager

for a tiny project.

⸻

Avoid Deep Prop Drilling

Use:

* composition
* context
* state management

when appropriate.

⸻

Avoid Copy-Paste Logic

Extract reusable behavior.

⸻

Avoid Magic Values

Bad

if (status === 7)

Good

if (status === STATUS_ARCHIVED)

⸻

Testing Standards

Prefer Behavior Testing

Test:

* user outcomes
* business rules
* workflows

NOT implementation details.

⸻

Critical Systems Must Be Tested

Always test:

* authentication
* payments
* validation
* permissions
* API contracts
* forms

⸻

Security Rules

Never Trust Client Input

Always validate:

* server-side
* database-side

Always sanitize input.

⸻

Never Expose Secrets

Do NOT expose:

* API keys
* private tokens
* credentials
* database secrets

in frontend code.

⸻

Refactoring Workflow

Recommended Process

1. Understand

Read before changing.

⸻

2. Simplify

Reduce complexity first.

⸻

3. Extract

Split reusable logic.

⸻

4. Optimize

Only after clarity.

⸻

5. Validate

Ensure behavior unchanged.

⸻

Language-Specific Guidelines

React

Prefer

* small components
* composition
* custom hooks
* server state separation
* feature folders

Avoid

* giant contexts
* prop drilling
* excessive useEffect
* unnecessary memoization

⸻

Next.js

Prefer

* server components
* route handlers
* streaming
* dynamic imports

Avoid

* oversized bundles
* unnecessary client components
* deep fetch waterfalls

⸻

TypeScript

Prefer

* explicit types
* discriminated unions
* inferred return types when obvious

Avoid

* any
* type assertion abuse
* giant interfaces

⸻

Python

Prefer

* readable functions
* small modules
* type hints
* explicit naming

Avoid

* hidden side effects
* massive utility files
* overengineering

⸻

Cleanmaxxing Review Rules

When reviewing code:

* explain WHY something is bad
* propose cleaner alternatives
* reduce complexity
* prioritize maintainability
* identify scalability risks
* identify hidden performance issues
* challenge unnecessary abstractions

Do NOT:

* praise messy code
* accept poor architecture
* optimize blindly
* support clever-but-unreadable solutions

⸻

Pre-Delivery Checklist

Readability

* Names reveal intent
* Minimal nesting
* No dead code
* No confusing abstractions

Maintainability

* Responsibilities separated
* Predictable structure
* Reusable logic extracted

Performance

* No unnecessary renders
* No duplicate requests
* Lazy loading where needed

Type Safety

* No unnecessary any
* Strong validation
* Predictable contracts

DX

* Easy to navigate
* Easy to debug
* Easy to extend

Scalability

* Modular architecture
* Decoupled business logic
* No bottleneck structures

Security

* Input validated
* Secrets protected
* Permissions enforced

⸻

Final Rule

Code should feel:

* obvious
* boring
* predictable
* scalable

If code looks “genius”,
it is probably bad engineering.