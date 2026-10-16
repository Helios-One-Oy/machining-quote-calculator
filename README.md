# Machining quote calculator

A small, honest cost model for quoting CNC machined parts at several quantities. One Python file, one JSON job file, no dependencies. There is also a [Google Sheet version](https://docs.google.com/spreadsheets/d/1zp7MDqecXFc0cZSa8qUuJfJZpQ8Yvh0jBvYF8gzSwHo/copy) (File > Make a copy).

```
$ python3 quote.py example-bracket.json
NW-1042 bracket, 6061-T6, black anodize
  qty  material     setup       run   outside      cost     price   job total  fixed %
    1      8.33    274.25     25.27    150.00    457.84    595.19      595.19     93%
   10      8.33     27.43     25.27     15.00     76.02     98.82      988.22     56%
   50      8.33      5.49     25.27      3.00     42.08     54.70     2734.98     20%
```

`fixed %` is the share of the cost that is setup, programming and lot charges. On a one-off it is most of the price, which is why a single part costs what it does.

## The model

For a quantity `q`:

```
cost per part = material
              + (sum of setup minutes x rate) / 60 / q
              + (sum of run minutes per part x rate) / 60
              + outside processing lot charges / q
              + outside processing per part
price per part = cost per part x (1 + markup)
```

Everything is per operation, so you can see which line drives the number.

## Filling in the job file

- **Material.** Price the blank you actually buy, not the finished part: add saw kerf and facing stock, and round up to the bar or plate size your supplier sells. If the job needs a full bar and the rest sits on the rack, decide whether the customer pays for it.
- **Setup minutes** are once per job: fixturing, touch-offs, first article, plus CAM programming as its own line. Most quoting mistakes on small lots are here, not in cycle time.
- **Run minutes** are per part. Until you have your own actuals, take the CAM simulation time and pad it for tool changes, loading and deburr between parts.
- **Outside processing** (anodize, heat treat, plating) usually has a lot minimum. Put that in `lot_charge`, anything priced per piece in `per_part`.
- **Markup** is a fraction (0.30 = 30%).

Quote at least three quantities. It answers the "why is one so expensive" question before it is asked, and sometimes the customer ends up ordering 5 instead of 1.

Write the actual hours next to the quoted ones when the job ships. That gap, reviewed once a month, is what makes the next quote better.

## Usage

```
python3 quote.py example-bracket.json
python3 quote.py my-part.json --qty 1 5 25 100
```

## Doing this from the drawing

This repo is the math. [QuotedPart](https://quotedpart.com/?utm_source=github&utm_medium=social&utm_campaign=organic-launch&utm_content=quote-calculator-readme) does the same thing starting from the RFQ drawing (PDF, with or without STEP): it reads the part, proposes the operations and times, and prices it on your own shop rates with every line editable. Built by Helios One.

## License

MIT
