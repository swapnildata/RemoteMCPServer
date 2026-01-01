import json
from fastmcp import FastMCP
from typing import Dict, Any

# Initialize MCP server
mcp = FastMCP("HRMS MCP Server")

# Load employee data once at startup
with open("employees.json", "r", encoding="utf-8") as f:
    EMPLOYEE_DATA = json.load(f)["employees"]


def find_employee_by_id(employee_id: str) -> Dict[str, Any]:
    for emp in EMPLOYEE_DATA:
        if emp["employee_id"] == employee_id:
            return emp
    return {}


@mcp.tool()
def get_employee_hrms(employee_id: str) -> Dict[str, Any]:
    """
    Fetch complete HRMS details of an employee using employee_id.
    """
    employee = find_employee_by_id(employee_id)

    if not employee:
        return {
            "error": "Employee not found",
            "employee_id": employee_id
        }

    return employee


if __name__ == "__main__":
    # Start MCP server (stdio / http depending on deployment)
    mcp.run(transport='http',host='0.0.0.0',port=8000)
    #mcp.run()