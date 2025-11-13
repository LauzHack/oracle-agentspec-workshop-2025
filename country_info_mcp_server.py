#!/usr/bin/env python3
"""
A minimal MCP (Model Context Protocol) server that exposes a single tool:
- get_country_info(country: str = "Switzerland"): calls the REST Countries API.

Usage:
------
$ python country_info_mcp_server.py
"""

import requests
from fastmcp import FastMCP

mcp = FastMCP("Country Info MCP Server")


@mcp.tool
def get_country_info(country: str = "Switzerland") -> str:
    """
    Fetch basic country information using REST Countries.

    Parameters:
    - country: Country name
    """
    url = f"https://restcountries.com/v3.1/name/{country}"
    params = {"fields": "languages,capital,currencies,region,population,capitalInfo,name"}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raises an error for bad status codes
    return str(response.json())


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)
