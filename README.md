# Run AI Agents Anywhere with Open Agent Specification

This repository contains material presented during the LauzHack workshop on 
Thursday 13th November 2025 ([event page](https://luma.com/estildp0)). The
workshop presentation was prepared and given by Oracle about the Open Source
project [Open Agent Specs](https://github.com/oracle/agent-spec).

## Installation

(1) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

(2) Install `pyagentspec` from source

The 

```bash
git clone git@github.com:oracle/agent-spec.git
cd agent-spec/pyagentspec
pip install -e .
```

(3) Install `wayflowcore` from PyPI

```bash
pip install "wayflowcore[oci]"
```

(4) Install `fastmcp` for running the local MCP server

```bash
pip install fastmcp
```

You are now ready to open and run the `AgentSpec_Workshop.ipynb` notebook.
