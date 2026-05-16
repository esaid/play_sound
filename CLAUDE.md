# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a simple utility designed to play a sound file (`coq.wav`) using the Linux `aplay` utility. It is intended to be used as a hook for Claude Code to notify the user when an operation is complete.

## Development Commands
- Run the sound player: `python3 playsound.py`

## Architecture
- `playsound.py`: Main script that locates `coq.wav` in its own directory and executes `aplay` via `subprocess`.
- `coq.wav`: The audio file to be played.

## Requirements
- Linux OS with `alsa-utils` installed (provides `aplay`).

## Integration as Claude Code Hook
To use this as a hook, configure a `Stop` hook in `settings.json` or `.claude/settings.local.json` to execute:
`python3 /path/to/play_sound/playsound.py`
