[![ORGAN-I: Theory](https://img.shields.io/badge/ORGAN--I-Theory-1a237e?style=flat-square)](https://github.com/organvm-i-theoria)

# Cognitive Archaeology Tribunal

**Comprehensive archaeological dig tool for auditing, inventorying, and triaging a multi-layer cognitive ecosystem.**

## Purpose

Before a system can be organised, its full extent must be known. The Cognitive Archaeology Tribunal exists to answer a deceptively difficult question: *what do we actually have?* It scans every layer of a creator's digital footprint -- local archives (iCloud, Dropbox, network drives), AI conversation exports (ChatGPT and generic JSON), personal GitHub repositories, organisation repositories, and web bookmark collections -- and produces a unified inventory, a knowledge graph of relationships, and a prioritised triage report with migration recommendations.

This is the foundational audit tool for the eight-organ creative-institutional system. The ORGAN model assumes that ~44 repositories across 8 GitHub organisations can be coherently governed, but that assumption is only valid if the inventory is accurate. The Tribunal generates that inventory. It was originally built to transform scattered creative history -- years of disparate archives, abandoned repos, half-finished AI conversations, and unlabelled bookmark folders -- into a structured foundation from which the organ system could be designed.

Within ORGAN-I (Theoria), this repo embodies *applied epistemology*: the practice of knowing what you know. Its five modules collectively answer the archaeological question, and its outputs feed directly into the planning documents in the [ingesting-organ-document-structure](https://github.com/organvm-i-theoria) corpus.

## Modules

| Module | Scope | Key Outputs |
|--------|-------|-------------|
| **Archive Scanner** | iCloud, Dropbox, local/network drives | File classification, deduplication, space-savings estimates |
| **AI Context Aggregator** | ChatGPT exports, generic JSON conversations | Topic extraction, timeline analysis, search/filter |
| **Personal Repo Analyzer** | Personal GitHub repos | Fork vs. original classification, modification tracking, health metrics |
| **Org Repo Analyzer** | Organisation GitHub repos | Status tracking, dependency detection, migration planning |
| **Web Bookmark Analyzer** | Netscape-format bookmark exports | URL/title/date extraction, collection statistics |

## Outputs

1. **Unified Inventory** (`inventory.json`) -- complete catalog of all discovered assets
2. **Knowledge Graph** (`knowledge_graph.json` + Cytoscape format) -- relationship map across sources
3. **Triage Report** (`triage_report.json` / `.txt`) -- prioritised action items and recommendations
4. **Migration Plans** -- strategic guidance for reorganisation and cleanup

## Quick Start

```bash
git clone https://github.com/organvm-i-theoria/cognitive-archaelogy-tribunal.git
cd cognitive-archaelogy-tribunal
pip install -r requirements.txt
export GITHUB_TOKEN="your_token_here"

# Run all modules
python main.py \
  --scan-archives /path/to/archives \
  --ai-conversations /path/to/chatgpt/export \
  --personal-repos your-username \
  --org-repos your-org \
  --output-dir ./output
```

Individual modules can be run independently (e.g., `--personal-repos` only, `--scan-archives` only). See the full documentation in `docs/` for per-module usage, integration guides, and governance policies.

## Status

**Stub / Active Development** -- Core modules are implemented in Python. The repository contains 184 files including documentation, configuration history (via SpecStory), Trunk-based linting configuration, and integration planning materials. The focus is shifting from personal archaeological use toward generalised audit tooling that other ORGAN repos can invoke.

## Relationship to the Eight-Organ System

One of 18 repositories in [ORGAN-I: Theoria](https://github.com/organvm-i-theoria). The Tribunal's inventory outputs were the empirical basis for the organ-system design itself -- the repo audit in `00-d-organ-system-audit.md` and the `registry-v2.json` source of truth both trace their lineage to data this tool produced. It sits upstream of everything.

## Author

**[@4444J99](https://github.com/4444J99)** / Part of [ORGAN-I: Theoria](https://github.com/organvm-i-theoria)
