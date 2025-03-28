# MCP is Dangerous

Function tool usage makes AI Agents very powerful, which is akin to introducing app stores to smartphones.
Especially with the release of [MCP (Model Context Protocol)](https://modelcontextprotocol.io/), tool sharing has become easier than ever.
That's why I've created the [extendable-agents](https://github.com/shaojiejiang/extendable-agents) project to showcase how easy you can extend the capabilities of AI Agents through open-source tools or your custom tools.

While working on extendable-agents, I've realized that tool usage is a double-edged sword.
The danger is that the tools you use have powerful access to your machine, such as your environment variables, files, etc.

## ⚠️ Security Warning

This project is a simple demonstration of the security risks associated with tool usage.
The example below illustrates how malicious actors could potentially exploit MCP servers to access sensitive information:

```python
# WARNING: This is a demonstration of security risks.
# DO NOT use this code maliciously!

import os
from mcp.server.fastmcp import FastMCP


server = FastMCP("Dangerous MCP")


@server.tool()
async def get_environment_variables() -> str:
    """Get all environment variables."""
    result = [
        "Here are what I could find:",
    ]
    for key, value in os.environ.items():
        result.append(f"{key:<30} {value[:5]}***")
    # This means I can open a backdoor to send your data to me!!
    return "\n".join(result)
```

> ⚠️ **Warning:** I recommend running this example in a sandboxed environment and deleting your OpenAI API key afterwards.
You can also test it with your own MCP client, using the following command: `uvx mcp-is-dangerous`.

When using this tool with extendable-agents (choose `PoliceAgent`), the output appears like this:

<img width="937" alt="Screenshot 2025-03-22 at 11 04 57" src="https://github.com/user-attachments/assets/c4e64be4-197e-4f0b-b6ca-b9bb73b2c223" />


It might look harmless or even intentionally benign, right?
But consider this scenario: you simply ask for the current time, and meanwhile, your sensitive data is being leaked without your knowledge.

## Best Practices for Security

To protect yourself when using MCP or similar tools:

1. Always review the source code of tools before using them
2. Run tools in isolated environments when possible
3. Be cautious of tools requesting access to sensitive information
4. Use environment variable filtering when deploying tools
5. Regularly audit the tools you're using

## Disclaimer

This project is meant for educational purposes only to demonstrate potential security risks. Do not use this knowledge for malicious purposes. The author is not responsible for any misuse of this information.

## License

[MIT License](LICENSE)
