# Wiring diagrams
A handly little reference for making cables. 

It is intended to make it simpler and more reusable by abstracting
away some of the connector details into reusable components, so that
an improvement to a connector description improves all generated cable
descriptions.

## How to use/build

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
make
```

(If you're on windows or not a developer, send your changes or details
in any case - I can take care any fancy stuff and make sure it all works!)

## How to edit/add

New connectors or documentation for same - everything goes under `devices/`.
If you're adding something from a manufacturer that isn't
listed already, generally try to follow the existing
`manufacturer/device/connectorname.{yaml,png,md}` pattern.

New cables - should go under `cables/`. Add new connectors as necessary.

Note: If you can't easily run the build scripts to check output, send
your changes anyway! 

## Gotchas

Image references in `devices/` yaml all assume they are being referenced
from one sub-layer into cables, so pictures (and rendering) will break
as soon as cables are separated into subfolders or anything else.

This will require intervention, but it's not yet a problem. Maybe we
can rewrite the image src in python, since we're already reading and
writing yaml in main.py.

## Style guidelines

Prefer the OEM manual pin descriptions where possible.
Use underscores instead of spaces in pin descriptions ('_').
Prefer OEM manual capitalization/casing where it makes sense.
Where it doesn't make sense, all lowercase is acceptable.
In general, just keep in mind that connector detail will be reused.
And finally:
It's better to have vague documentation that can be improved than
wrong documentation. And it's generally better to have something rather
than nothing.

Where possible please include connector pictures. Numbering, naming,
schematics, all are welcome. All the better if you include a note
somewhere, ideally a text file next to any pictures or documentation,
identifying the provenance of your information.

## Quality concerns

Known-good connectors and cable designs that you have personally
verified against an extant cable and/or used with devices can be marked
'knowngood:True' in the yaml.

Before marking a cable accurate, please check it over for the following issues:

* Is the pin numbering clear?
* Is the purpose of each pin clear?
* Are the pictures mirrored, or labeled the wrong gender without a
description saying so?

If any part of a diagram is confusing or any other issue, even if you
don't have the fix, please open a ticket. This is intended to be a
one-stop-shop for making cables and that means noting any confusion for
remedy is important.



## sidenote:
Self: Also look into https://github.com/daq-tools/wireviz-web

