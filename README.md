# Journalgranskaren Core

**Journalgranskaren Core** är en öppen källkodsmotor som analyserar svenska journaltexter
för att upptäcka saknade negationer, förbättringsformuleringar utan motivering och oklara åtgärder.

Detta repo innehåller:
* **app/** – logik för semantisk och regelbaserad analys
* **webapp/** – Flask-baserat gränssnitt för lokal demo
* **examples/** – testdata

> För API, batchanalys, exportfunktioner och journalsystem-integration finns `journalgranskaren-pro` (kommersiell modul).

## Installation

```bash
git clone https://github.com/ditt-konto/journalgranskaren-core.git
cd journalgranskaren-core
pip install -r requirements.txt
python webapp/flask_app.py
```

## Licens

MIT – fri att använda och modifiera.
