from mcp.server.fastmcp import FastMCP
from functions/search.py import agent_web_search

# Create an MCP server
mcp = FastMCP("Knowledge", json_response=True)


### TOOLING ###
@mcp.tool()


### RESOURCES ####
@mcp.resource()



### PROMPT ### 
@mcp.prompt()

# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")