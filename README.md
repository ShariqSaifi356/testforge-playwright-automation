# testforge-playwright-automation
TestForge — Enterprise E-Commerce Test Automation Framework

## Playwright MCP with GitHub Copilot

This workspace includes a project-scoped Playwright MCP configuration in `.vscode/mcp.json`. It allows GitHub Copilot Chat to open and inspect web pages through Playwright while you develop or investigate tests.

### Prerequisites

- Node.js and `npx` available on `PATH`
- GitHub Copilot Chat in VS Code with MCP support enabled

### Start the MCP server

1. Open this repository as the VS Code workspace root.
2. Open Copilot Chat and use the tools menu to start the `playwright` MCP server if VS Code has not started it automatically.
3. Ask Copilot to navigate to a page, inspect its accessible structure, or exercise a flow in a browser.

The server is launched on demand with `npx @playwright/mcp@latest`; no npm dependency is added to the Python test framework. MCP browser sessions are exploratory and separate from the pytest `page` fixture used by the automated tests.

### Example prompts

- `Use Playwright MCP to open https://automationexercise.com/ and inspect the Signup / Login link.`
- `Use Playwright MCP to verify the signup flow and suggest stable locators for pages/signup_page.py.`
- `Use Playwright MCP to reproduce this failing browser step and report the visible error.`

Keep secrets and production credentials out of prompts and browser sessions. Review any generated locator or test change before applying it.
