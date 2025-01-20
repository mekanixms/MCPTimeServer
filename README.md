# MCP Time Server

A Model Context Protocol (MCP) server that provides current time from internet time servers with timezone support.

## Features

- Fetches accurate time from NTP servers (pool.ntp.org)
- Supports custom timezone configuration via environment variable
- Graceful error handling for network issues and invalid timezones
- Compatible with Claude Desktop

## Installation

1. Install the required dependencies:
```bash
pip install mcp ntplib pytz
```

2. Install the server in Claude Desktop with your preferred timezone:
```bash
mcp install timeserver.py -e TIMEZONE=America/New_York
```

Locate the claude_desktop_config.json and add (or change as mcp command generates it) to "mcpServers" the "Time Server":
```json
{
  "mcpServers": {
    "Time Server": {
      "command": "/path/to/python",
      "args": [
        "/path/to/timeserver.py"
      ],
      "env": {
        "TIMEZONE": "America/New_York"
      }
    }
  }
}
```

You can set any valid timezone name from the IANA Time Zone Database. Some common examples:
- 'America/New_York'
- 'Europe/London'
- 'Asia/Tokyo'
- 'US/Pacific'
- 'UTC' (default if no timezone is specified)

## Usage

Once installed, you can ask Claude to use the `get_current_time` tool to fetch and display the current time in your configured timezone. The tool will:
- Connect to pool.ntp.org to get the accurate current time
- Convert the time to your specified timezone (or UTC if none specified)
- Return a formatted string with the current date, time, and timezone

## Error Handling

The server handles several types of errors gracefully:
- Network connectivity issues when reaching the NTP server
- Invalid timezone specifications (falls back to UTC)
- General exceptions with informative error messages

## Dependencies

- mcp: Model Context Protocol SDK
- ntplib: NTP client library
- pytz: Timezone database and utilities