# NTI: Machine Learning for Data Analysis - Lecture 01

This repository contains the practical implementation and coursework for **Lecture 01: Python Syntax Refresh for Data Analysis**, as part of the Machine Learning training program at the National Telecommunication Institute (NTI).

## Course Overview

The program bridges the gap between raw data analysis and intelligent decision-making by covering full data pipelines, machine learning models, thorough evaluations, and production-ready deployments.

## Lecture 01 Objectives & Recap

The core focus of this module was establishing a solid programming foundation before moving into heavily optimized scientific computing packages (NumPy/Pandas). 

Key areas refreshed and verified inside the integrated environment:
- **Dynamic Constructs & Variable Scope:** Pythonic multi-assignments, variable swapping mechanics, global vs. local scoping behaviors.
- **Control Flows & Loop Mechanics:** Writing optimized `for` and `while` execution loops utilizing advanced `break` and `continue` branching statements.
- **Advanced Functional Programming:** Defining modular functions with explicit keyword arguments, packaging multiple dynamic returns, and implementing single-expression `lambda` functions inline.
- **Data Structures & Comprehensions:** Comprehensive manipulation of both mutable and immutable standard native collections (`Lists`, `2D Lists`, `Dictionaries`, `Sets`, `Tuples`), and leveraging high-performance **List Comprehensions**.
- **Exception Profiling:** Differentiating between standard *Syntax Errors*, *Runtime Errors*, and latent *Logical Errors* using defensive programming layouts.

## Dataset & Analytical Practice

The hands-on practice utilizes the standard open-source **RMS Titanic Passenger Dataset**, exploring metadata properties including demographics, boarding classes, socio-economic fare margins, and survival indicators.

### Task Implementations Completed

- **Custom Aggregations:** Engineered a dynamic, reusable function `average_column(df, column_name)` returning high-precision decimal calculations for features like passenger `Age` and boarding `Fare`.
- **High-Performance Class Extraction:** Leveraged native comprehension syntaxes integrated with mathematical `Sets` to dynamically pull distinct categories within the passenger routing parameters (`Pclass`).
- **Conditional Boundary Evaluation:** Multi-branch statistical logic classifying overall target metrics against structured boundary constraints.

### Advanced Optimization Challenge

- **Algorithmic Profiling:** Implemented granular programmatic scanning across target features using core baseline conditional blocks (avoiding higher-level framework shortcuts) to count survival allocations.
- **Feature Filtering:** Structured advanced inline expressions capturing comprehensive target sub-matrices where operational data thresholds scaled past the historical operational mean.

## Installation & Setup

To reproduce the analysis locally, ensure you have Python 3.10+ installed, then follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yousefelgohary/titanic.git
   cd titanic
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment & Tools

- **IDE:** Antigravity IDE (Agent-Assisted Runtime Environments)
- **Core Language:** Python 3.10+
- **Framework Previews:** Pandas (Dataframe parsing engine), NumPy

## Repository Structure

```text
titanic/
├── .venv/                 # Virtual environment (ignored in git)
├── .gitignore             # Git ignore configuration
├── requirements.txt       # Project dependencies
├── README.md              # Comprehensive technical overview
├── Recap.ipynb            # Interactive notebook with syntax and exercises
└── titanic.csv            # Core operational passenger records dataset
```
