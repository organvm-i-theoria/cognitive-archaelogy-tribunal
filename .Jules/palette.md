## 2024-03-21 - [CLI Empty State]
**Learning:** Command-line tools often lack a "landing page." By detecting empty arguments (`len(sys.argv) == 1`) and displaying a rich-text panel instead of a generic error, we turn a "mistake" (running without args) into an onboarding opportunity.
**Action:** Always check for empty args in CLI entry points and provide a "Welcome" or "Dashboard" view with examples, rather than just `parser.print_help()`.
