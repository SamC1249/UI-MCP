### EXA AI USE ###

from exa_py import Exa
import os
from dotenv import load_dotenv

load_dotenv()

EXA_API_KEY = os.getenv("EXA_API_KEY")

if EXA_API_KEY:
    exa = Exa(api_key=EXA_API_KEY)
    results = exa.search_and_contents(
        "Latest research in LLMs", 
        text=True
    )
    print(results)
else:
    print("NO API KEY")

@mcp.tool()
def agent_web_search(query: str) -> str:
    """ Searches the web """
    return exa.search_and_contents(
        f"${query}",
        text=True
    )



