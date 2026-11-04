# Zeinloop case study

## What Zeinloop is

Zeinloop is the company Nirmeet Rao founded to build AI native products. One product built under Zeinloop is a real estate compliance SaaS focused on New York City decarbonization data, taken from concept to a minimum viable product. This case study describes that product and the workflow pattern behind it. It gives no dates for Zeinloop work, in line with his standing instruction for that venture.

## The problem in plain terms

Decarbonization compliance starts with data that does not arrive together. A building owner may have energy bills, a floor area figure, and an emissions estimate, each from a different source and in a different format. A person preparing a compliance view has to gather them, check that nothing essential is missing, and produce a summary that can be compared across buildings. Done by hand, that gathering and checking is where the time goes, and where gaps hide. A missing field treated as zero, or two buildings compared on unlike figures, produces a summary that looks precise and is wrong.

## The workflow

1. Intake. One structured record holds the building identifier, the square footage, and the energy and emissions data. If a field is missing, the record says so plainly.
2. Validation. Before any summary is produced, simple rules check the record. A building with missing square footage, missing energy data, or a nonpositive size cannot move to summarization. It goes to review instead.
3. Summarization. From a validated record, the system produces a comparable figure: total emissions divided by square footage. The figure is simple on purpose, so a reviewer can check it rather than trusting a black box score.
4. Human review. Anything incomplete, uncertain, or above an illustrative threshold goes to a person. The reviewer sees exactly what failed and why, so review is focused rather than a full reread.
5. Completion. The outcome is recorded: summarized, or flagged for review, with the reason. Over many buildings, those outcomes show where data is missing and where buildings cluster above threshold, which is where the product improves next.

## Design principles

1. Structure before summarizing. A summary built on an incomplete record only moves the error later.
2. Validate with rules, not hope. Simple checks catch the gaps a fast summary would miss.
3. Explain the flag. A review item should carry its reason, so a person can act on it quickly.
4. Keep judgment with people. The system prepares. A person decides.
5. Make figures comparable. One figure, computed the same way for every building, beats a clever score that cannot be checked.

## What the demo shows, and what it does not show

The demo shows intake, validation, summarization, review flagging, and a summary, on three synthetic buildings. It does not show a real building portfolio, real utility data, real emissions reporting, or a real employer workflow. All sample data is invented for illustration only. The threshold in the demo is illustrative only and is not a legal limit. The value of the demo is the pattern, not the sample data.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
