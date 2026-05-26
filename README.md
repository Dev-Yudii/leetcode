# LeetCode Analytics & Automation Pipeline
This repository contains my LeetCode solutions and tracks my long-term problem-solving progress through an external automation and analytics pipeline.

The goal is not only to practice algorithms and data structures, but also to build a real dataset from my own learning behavior over time.


## Problem Solving Focus
This repository focuses on:

- Data structures and algorithms
- Pattern recognition
- Complexity analysis
- Clean and maintainable Python solutions
- Continuous learning and progress tracking


## Powered by Automation
This repository is powered by an external automation pipeline responsible for generating templates, parsing examples, and tracking metadata.

Whenever a new LeetCode Daily Challenge is fetched, the pipeline automatically:

1. Creates a structured Python workspace based on the problem category.
2. Generates a Python template containing:
   - Problem metadata
   - Starter boilerplate
   - Local test execution block
3. Extracts example test cases directly from the problem description.
4. Registers the problem inside a local SQLite database for historical tracking.

Interested? Check it on: https://github.com/Dev-Yudii/leetcode-analytics-automation


## Solution Workflow
Each solution follows a consistent workflow:

### 1. Local Test Execution
Every generated file includes a local `__main__` execution block with pre-mapped examples from LeetCode for quick testing before submission.

### 2. Review & Retrospective
At the bottom of each solution file, I document:

- Initial approaches
- Roadblocks encountered
- Final solution decisions
- Complexity analysis
- Performance observations

### 3. Continuous Learning
I also document new Python features, data structures, and algorithmic concepts learned during the solving process.

Examples:
- Set intersections
- Hash table behavior
- Constant-space scenarios
- Complexity trade-offs


## Analytics & BI Roadmap
Every problem solved is logged into a local SQLite database (`leetcode_history.db`) containing metadata such as:

- ID
- Title
- Slug
- Difficulty
- Category
- Timestamp


### Current & Planned Features
- [x] Automated file generation
- [x] Local SQLite tracking
- [x] Dynamic category organization
- [ ] CLI status management (`PENDING`, `SOLVED`, `FAILED`)
- [ ] Duration and attempt tracking
- [ ] Missing-day synchronization
- [ ] Dockerized execution environment
- [ ] GitHub Actions scheduled automation
- [ ] Power BI dashboard integration

### Long-Term Goal
The long-term objective is to transform daily problem-solving activity into a personal analytics platform capable of measuring:

- Solving consistency
- Topic proficiency
- Difficulty distribution
- Learning progression over time
- Performance trends


## Running Tests Locally
```bash
1. Clone the repository
    git clone https://github.com/Dev-Yudii/leetcode
2. Enter the repository
3. Run a specific problem
    python hash_table/3120_count-the-number-of-special-characters-i.py