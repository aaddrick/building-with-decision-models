# Installing building-with-decision-models for OpenCode

This repository ships one skill. OpenCode finds skills on its own in
`~/.config/opencode/skills/<name>/SKILL.md`, so no plugin or config entry is needed.

## Install

Clone the repository and link the skill folder into OpenCode's global skills directory:

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git ~/.local/share/building-with-decision-models
mkdir -p ~/.config/opencode/skills
ln -s ~/.local/share/building-with-decision-models/skills/building-with-decision-models ~/.config/opencode/skills/building-with-decision-models
```

On Windows, or anywhere symlinks are awkward, copy the folder instead of linking it:

```bash
cp -r ~/.local/share/building-with-decision-models/skills/building-with-decision-models ~/.config/opencode/skills/
```

To install for one project only, put the folder in that project's `.opencode/skills/` instead.

## Check it installed

```bash
opencode debug skill | grep '"name": "building-with-decision-models"'
```

Restart OpenCode. It loads the skill when the task matches. To load it by hand, ask:

```
use the skill tool to load building-with-decision-models
```

The skill links to files beside it (`patterns.md`, `providers/jev.md`, and so on). OpenCode tells the
agent the skill's base directory when it loads, so the agent reads them from there.

## Update

```bash
git -C ~/.local/share/building-with-decision-models pull
```

If you copied the folder, copy it again after pulling.

## Uninstall

Delete the `building-with-decision-models` link (or copied folder) from `~/.config/opencode/skills/`,
then delete the clone at `~/.local/share/building-with-decision-models`.
