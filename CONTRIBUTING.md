# Contributing

Corrections and new prior art are welcome.

## Fix a fact

Decision models change fast, and new providers arrive every week. If a fact in the skill is wrong, open an issue or a pull request with a link to the source: a provider's docs page, an SDK changelog, a model card, or a live API response. Do not paste an API key into an issue.

## Add prior art

Add the project to the shape that matches how it works, not what domain it serves. `skills/building-with-decision-models/prior-art/INDEX.md` lists the shapes. New entries go in `skills/building-with-decision-models/prior-art/projects/<shape>.md`, under the sub-type that fits. The shape file itself (`prior-art/<shape>.md`) holds only two or three flagship examples, so leave it alone unless the new project should replace one. Projects that compare, benchmark, or switch models go in `skills/building-with-decision-models/prior-art/projects/choosing-and-switching-models.md`. That list has no shape file: its procedure and lessons are in `skills/building-with-decision-models/choosing-and-switching-models.md`, next to `SKILL.md`. Each entry needs:

- one line on how the project uses a decision model (which primitives, which loop),
- the model it runs on, in parentheses (Jev, Clef, Nimble, ...),
- a link to the code or write-up,
- any number the author reports, marked as reported.

A project that tried a decision model and found it a bad fit is just as useful. Name the model: a bad fit on one model may work on another. If it failed for any decision model, add it to `skills/building-with-decision-models/prior-art/bad-fits.md` under "Any decision model". If it failed on one model, add it to that model's file under "Where it fails" (see the next section). A general (any-model) bad fit also needs a one-line headline under "Known bad fits (headlines)" in `prior-art/INDEX.md`: the bolded lead phrase plus a short "instead" if there is one, with no numbers and no links.

## Add a model-specific finding

A field lesson that holds only for one model (a latency, a context or option limit, a calibration number, a failure) goes in `skills/building-with-decision-models/models/<name>.md`, not in a shape file. Shape files keep lessons that hold for any model, plus Jev notes, since Jev is the default. Put the finding under the right topic (Limits, Calibration, Where it does well, Where it fails, By shape) and link its source. A model with only a note or two goes in `models/others.md`. A new model file needs a row in `models/INDEX.md`, and a mention in the "Not on Jev?" line of each shape file it has notes for. Wire-format facts (endpoint, fields, errors, price) belong in `providers/` instead. A head-to-head result between models, where the comparison itself is the lesson, goes in `choosing-and-switching-models.md`; each model's own number stays in its file.

## Add a provider

Add a file to `skills/building-with-decision-models/providers/` and a row to "Pick the provider" in `SKILL.md`. List only how the provider differs from `providers/jev.md`: endpoint, key variable, model IDs, envelope and field-name differences, limits, price, and any evidence about its accuracy and calibration. Link a source for every fact and put a snapshot date at the top.

## Before you open a pull request

```bash
python3 scripts/check_configs.py
python3 -m unittest discover -s tests -v
```

If you change an install command in `README.md`, change it in every file under `.github/readme/` too. The tests check that the commands match.

If you change the hero text, regenerate the card with `python3 scripts/make_card.py` (needs Pillow and NumPy) and commit the PNG.

## Screenshots

The README walkthroughs use images from `scripts/annotate_screens.py`, which blurs account details and draws the step highlights. The raw captures show account details, and the API key ones a live key, so they never go in the repo. Keep them outside the repo and check every output image for anything unmasked before you commit.

- **API key flow** (`.github/assets/api-key/`): capture the four console screens at 1512x807, run `python3 scripts/annotate_screens.py api-key /path/to/raw-dir`, then revoke the key you created for the capture.
- **Plugin marketplace flow** (`.github/assets/plugin-marketplace/`): capture the five claude.ai screens at 1510x812 in the dark theme, starting with no marketplace added (remove it under **Customize > Plugins > Add > Manage marketplaces**), then run `python3 scripts/annotate_screens.py plugin-marketplace /path/to/raw-dir`.

The script's docstring lists the file names each flow expects.
