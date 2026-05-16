# PlaySound for Claude Code

A simple utility to play a sound notification when Claude Code finishes an operation.

## Installation

### Prerequisites
Ensure you are on a **Linux** system and have the ALSA sound utilities installed:
```bash
sudo apt-get update
sudo apt-get install alsa-utils
```

## Configuration as a Claude Code Hook

To have Claude play a sound (a rooster's crow) whenever it finishes a task, you need to configure a `Stop` hook.

### 1. Get the Absolute Path
Claude Code requires the absolute path to the script. If your project is at `/home/esaid/PycharmProjects/play_sound/`, the command is:
`python3 /home/esaid/PycharmProjects/play_sound/playsound.py`

### 2. Set the Hook
You can choose where to configure this:

**Option A: Project-only (Recommended)**
Edit `.claude/settings.local.json` in your project root:
```json
{
  "hooks": {
    "Stop": "python3 /home/esaid/PycharmProjects/play_sound/playsound.py"
  }
}
```

**Option B: Global (Works in all projects)**
Edit your global settings at `~/.claude/settings.json`:
```json
{
  "hooks": {
    "Stop": "python3 /home/esaid/PycharmProjects/play_sound/playsound.py"
  }
}
```

## Testing
1. Run any command in Claude Code (e.g., `/help`).
2. When Claude finishes its response, you should hear `coq.wav` play.

## Troubleshooting
- **No sound?** Test the script manually:
  `python3 /home/esaid/PycharmProjects/play_sound/playsound.py`
- **Command not found?** Ensure `alsa-utils` is installed.
