# Scraper pre letáky

Tento projekt je web scraper v Pythone, ktorý sťahuje informácie o propagačných letákoch z webovej stránky `prospektmaschine.de`.

## Popis

Skript automaticky prechádza kategóriu "hypermarkety", identifikuje všetky dostupné obchody a pre každý z nich extrahuje detaily o aktuálnych letákoch. Zozbierané údaje zahŕňajú názov letáku, URL náhľadu, názov obchodu a obdobie platnosti. Tieto informácie sa následne ukladajú do súboru `hyperia_letaky.json`.

## Inštalácia

1.  Uistite sa, že máte nainštalovaný Python 3.
2.  Klonujte tento repozitár.
3.  Vytvorte virtuálne prostredie a nainštalujte závislosti. Môžete to urobiť manuálne alebo pomocou `make`.

    **S `make` (odporúčané):**
    ```bash
    make install
    ```
    Tento príkaz vytvorí virtuálne prostredie v priečinku `venv` (ak neexistuje) a nainštaluje všetky potrebné závislosti.

    **Manuálne:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Použitie

Pred spustením sa uistite, že máte aktivované virtuálne prostredie, ak ste ho vytvorili manuálne.

```bash
source venv/bin/activate
```

### Priamo cez Python

Pre spustenie scrapera jednoducho spustite hlavný skript z aktivovaného prostredia:

```bash
python main.py
```

### Pomocou Makefile

`Makefile` automaticky použije virtuálne prostredie, takže ho nemusíte aktivovať ručne.

*   **Spustenie scrapera:**
    ```bash
    make run
    ```

*   **Vytvorenie prostredia a inštalácia závislostí:**
    ```bash
    make install
    ```

*   **Vyčistenie projektu:** (odstráni `hyperia_letaky.json`, dočasné súbory a `venv`)
    ```bash
    make clean
    ```

Po úspešnom spustení scrapera sa v hlavnom adresári projektu vytvorí súbor `hyperia_letaky.json` s extrahovanými dátami.

## Závislosti

Projekt využíva nasledujúce knižnice:

*   `beautifulsoup4`
*   `requests`

Úplný zoznam závislostí nájdete v súbore `requirements.txt`.