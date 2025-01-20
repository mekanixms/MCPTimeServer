from mcp.server.fastmcp import FastMCP
import ntplib
import os
from datetime import datetime
import pytz

# Create an MCP server
mcp = FastMCP(
    "Time Server",
    dependencies=["ntplib", "pytz"],  # Specify required dependencies
    description="A server that provides current time from internet time servers"
)

@mcp.tool()
def get_current_time() -> str:
    """
    Get the current time from an NTP server and format it according to the configured timezone.
    Returns a string with the current date and time.
    """
    try:
        # Create NTP client
        client = ntplib.NTPClient()
        
        # Query NTP server (using pool.ntp.org)
        response = client.request('pool.ntp.org')
        
        # Get timestamp from response
        timestamp = response.tx_time
        
        # Convert to datetime
        utc_time = datetime.fromtimestamp(timestamp, pytz.UTC)
        
        # Get timezone from environment variable, default to UTC
        timezone_str = os.getenv('TIMEZONE', 'UTC')
        try:
            timezone = pytz.timezone(timezone_str)
            local_time = utc_time.astimezone(timezone)
            return f"Current time ({timezone_str}): {local_time.strftime('%Y-%m-%d %H:%M:%S %Z')}"
        except pytz.exceptions.UnknownTimeZoneError:
            return f"Error: Unknown timezone '{timezone_str}'. Using UTC instead.\nCurrent time (UTC): {utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')}"
            
    except Exception as e:
        return f"Error fetching time: {str(e)}"

if __name__ == "__main__":
    mcp.run()