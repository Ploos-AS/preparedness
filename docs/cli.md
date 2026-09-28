# ploos-prep CLI

`ploos-prep` is the offline command-line interface for Ploos Preparedness Toolkit.

## Water

```sh
ploos-prep water --people 2 --days 3
# litres: 18
```

The default planning rate is 3 litres per person per day. This is a calculator default, not a universal preparedness recommendation; books and jurisdiction-specific guidance must explain their assumptions and sources.

## Battery energy

```sh
ploos-prep battery --voltage 12 --ah 10
# nominal_wh: 120
```

This computes nominal energy only. Real usable energy depends on battery chemistry, discharge limits, temperature, conversion losses and equipment.

## Runtime

```sh
ploos-prep power --usable-wh 400 --load-w 100
# runtime_hours: 4
```

This is the ideal arithmetic runtime from already-usable energy. It does not silently assume inverter efficiency or reserve margins.

## JSON

Add `--json` to any command. Output follows `schemas/tool-output.schema.json`.

The CLI performs no network requests.
