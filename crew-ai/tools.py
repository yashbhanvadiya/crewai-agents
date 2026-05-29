from crewai_tools import YoutubeChannelSearchTool
from crewai_tools.rag.data_types import DataType
from crewai_tools.tools.rag.rag_tool import RagTool
import pytube.extract
import re

## --- Patches for library bugs ---

# Patch 1: pytube doesn't support YouTube's /@handle URL format.
# Add the /@handle pattern to pytube's channel_name regex list.
_original_channel_name = pytube.extract.channel_name

def _patched_channel_name(url: str) -> str:
    """Support /@handle URLs in addition to the original patterns."""
    # Try the @handle pattern first
    match = re.search(r"(?:\/(@)([%\d\w_\-]+)(\/.*)?)", url)
    if match:
        return f"/{match.group(1)}{match.group(2)}"
    return _original_channel_name(url)

pytube.extract.channel_name = _patched_channel_name

# Patch 2: crewai_tools' add() method prepends @ to full URLs, corrupting them.
_original_add = YoutubeChannelSearchTool.add

def _patched_add(self, youtube_channel_handle: str) -> None:
    """Fixed add that doesn't corrupt URLs by prepending @."""
    if youtube_channel_handle.startswith(("http://", "https://")):
        RagTool.add(self, youtube_channel_handle, data_type=DataType.YOUTUBE_CHANNEL)
    else:
        _original_add(self, youtube_channel_handle)

YoutubeChannelSearchTool.add = _patched_add

## --- Tool initialization ---

## Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="https://www.youtube.com/@krishnaik06"
)