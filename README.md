# Zeinloop

Zeinloop is the company Nirmeet Rao founded to build AI native products. One product built under Zeinloop is a real estate compliance SaaS focused on New York City decarbonization data, taken from concept to a minimum viable product.

## The problem

A building owner who needs to understand decarbonization compliance starts with scattered data. Energy usage lives in one place, building size lives in another, and emissions figures arrive in formats that do not line up. Before anyone can judge where a building stands, someone has to gather the pieces, check that nothing essential is missing, and put them into a form that can be compared across buildings.

## The product idea

Zeinloop treats a building as a structured record. Intake captures the building, its size, and its energy and emissions data in one place. Validation checks that record before any summary is produced. A summary then shows emissions per square foot for each validated building, and flags anything incomplete or above an illustrative threshold for human review.

1. Intake. Capture the building identifier, the square footage, and the energy and emissions data in one structured record.
2. Validate. Check required fields and simple rules before any summary is produced.
3. Summarize. Produce a comparable figure, emissions per square foot, for each validated building.
4. Review. Flag anything incomplete or above threshold for human review instead of letting it pass quietly.
5. Complete. Record the outcome so the team can see where data is missing and where buildings cluster above threshold.

## Why the structured record matters

Compliance work fails quietly when a missing field is treated as zero, or when two buildings are compared on figures that were measured differently. Zeinloop puts the check before the summary, so a gap is visible at intake instead of surfacing later as a wrong comparison. That split is the product decision: the system prepares a comparable summary, and a person reviews anything the checks cannot confirm.

## Relation to his other work

The pattern here matches his other healthcare and workflow products. PharmFlows, the LLM workflows he shipped at Concordia Pharma, reported serving time errors down 86 percent and cycle time down 30 percent on his resume. Paxei, his prior authorization preparation workflow, reported preparation time cut from 45 minutes to 10 minutes. All three use the same shape: structured intake, validation, a draft or summary, and human review. His ephe platform work adds the matching tooling idea, that tool contracts are a product surface and context is a budget.

## The demo in this repository

The demo folder contains a minimal reference implementation of this pattern in plain Python with no external packages. It runs three synthetic sample buildings, validates each one, computes emissions per square foot for validated buildings, flags incomplete buildings for review, and prints a short summary. The sample data is invented for illustration only. It is not building data, not utility data, and not employer data. The threshold used in the demo is illustrative only. It is not a legal limit and it is not a New York City rule.

## What this is not

This is not a shipped product. This is not an employer system. This is not a measured result from any job. It is a reference demo and a written case study, built to illustrate a way of working that his verified projects already reflect.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
