![PR Workflow](https://github.com/BioEcoOcean/metadata-tracking-dev/actions/workflows/gha_generate_pr.yml/badge.svg)

# BioEco Metadata Generator

This repo is a test for generating metadata JSON-LD files for BioEco EOVs within the [BioEcoOcean](https://bioecoocean.org/) project. It is still in development and because it was forked from the NOAA CEFI info hub repo there may still be unrelated info in this repo. Big thank you to the contributors who developed the original metadata generators this repo this is based on, their developments there are invaluable for this project!

## How it (will) work

The idea is to submit a new GitHub issue with the "Contribute BioEco Metadata" issue template, fill in the fields, submit, and then a JSON-LD file will be generated for you. The link to that JSON-LD file can then be used to link the metadata to ODIS through the [ODIS Catalgoue of Sources](https://catalogue.odis.org/). Metadata entered in this template will focus more on project metadata rather than dataset specific metadata, which will be associated with datasets published to [OBIS](https://obis.org/).

### Metadata required
- Project details: title, description, links
- License
- Point of contact(s)
- EOV(s) targeted
- Methods used
- Taxonomic scope
- Temporal scope
- ...

## Things to do:
- ensure issue template includes required metadata and aligns with [ODIS EOV example](https://book.odis.org/thematics/variables/index.html)
- confirm JSON-LD files can be easily updated and doesn't create duplicates (so the link is stable)
- look into generating sitemap.xml
- update the resource link check badge
- investigate EML exports for the JSON files for people to upload to OBIS(?)

_This repo is being developed by Elizabeth Lawrence, OBIS BioEcoOcean Project Officer. Contributions and suggestions are welcome._
