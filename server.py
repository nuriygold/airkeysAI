# server.py — AirKeys AI WebSocket Server
# This file will contain the Python asyncio WebSocket server that:
#   - Serves the iPad PWA frontend via aiohttp static file handler
#   - Handles real-time keystrokes from iPad to Mac via pyautogui
#   - Integrates Claude API for inline AI completions and suggestions
#   - Routes slash commands to n8n webhooks for workflow automation
#   - Bridges CREAO agent app commands for text transformation
#   - Generates QR code for easy iPad pairing on local network
#
# Code coming in next phase — see docs/architecture.md for design details.
