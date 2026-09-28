package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"

	"github.com/Ploos-AS/preparedness/internal/calc"
)

type output struct {
	SchemaVersion int            `json:"schema_version"`
	Tool          string         `json:"tool"`
	Inputs        map[string]any `json:"inputs"`
	Result        map[string]any `json:"result"`
	Units         string         `json:"units"`
	Jurisdiction  *string        `json:"jurisdiction"`
	Notes         []string       `json:"notes"`
}

func usage() {
	fmt.Fprintln(os.Stderr, "Ploos Preparedness Toolkit")
	fmt.Fprintln(os.Stderr, "usage: ploos-prep <water|battery|power> [options]")
	fmt.Fprintln(os.Stderr, "All calculations are offline and use SI units.")
}

func emit(tool string, inputs, result map[string]any, asJSON bool) {
	if asJSON {
		v := output{1, tool, inputs, result, "SI", nil, []string{}}
		b, _ := json.MarshalIndent(v, "", "  ")
		fmt.Println(string(b))
		return
	}
	for k, v := range result {
		fmt.Printf("%s: %v\n", k, v)
	}
}

func water(args []string) error {
	f := flag.NewFlagSet("water", flag.ContinueOnError)
	people := f.Int("people", 0, "number of people")
	days := f.Int("days", 0, "number of days")
	rate := f.Float64("litres-per-person-day", 3, "planning litres per person per day")
	j := f.Bool("json", false, "machine-readable JSON output")
	if err := f.Parse(args); err != nil { return err }
	v, err := calc.WaterLitres(*people, *days, *rate); if err != nil { return err }
	emit("water", map[string]any{"people":*people,"days":*days,"litres_per_person_day":*rate}, map[string]any{"litres":v}, *j)
	return nil
}

func battery(args []string) error {
	f := flag.NewFlagSet("battery", flag.ContinueOnError)
	voltage := f.Float64("voltage", 0, "battery voltage")
	ah := f.Float64("ah", 0, "capacity in amp-hours")
	j := f.Bool("json", false, "machine-readable JSON output")
	if err := f.Parse(args); err != nil { return err }
	v, err := calc.BatteryWh(*voltage, *ah); if err != nil { return err }
	emit("battery", map[string]any{"voltage_v":*voltage,"capacity_ah":*ah}, map[string]any{"nominal_wh":v}, *j)
	return nil
}

func power(args []string) error {
	f := flag.NewFlagSet("power", flag.ContinueOnError)
	wh := f.Float64("usable-wh", 0, "usable energy in watt-hours")
	w := f.Float64("load-w", 0, "load in watts")
	j := f.Bool("json", false, "machine-readable JSON output")
	if err := f.Parse(args); err != nil { return err }
	v, err := calc.RuntimeHours(*wh, *w); if err != nil { return err }
	emit("power", map[string]any{"usable_wh":*wh,"load_w":*w}, map[string]any{"runtime_hours":v}, *j)
	return nil
}

func main() {
	if len(os.Args) < 2 { usage(); os.Exit(2) }
	var err error
	switch os.Args[1] {
	case "water": err = water(os.Args[2:])
	case "battery": err = battery(os.Args[2:])
	case "power": err = power(os.Args[2:])
	case "help", "-h", "--help": usage(); return
	default: usage(); err = fmt.Errorf("unknown command %q", os.Args[1])
	}
	if err != nil { fmt.Fprintln(os.Stderr, "error:", err); os.Exit(2) }
}
