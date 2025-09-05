# This import is from src\mcpserver, call the mcp object/server
from mcpserver.deployment import mcp

def main():
    mcp.run()

if __name__ == "__main__":
    main()