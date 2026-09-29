package vectors

import (
	"math"
	"os"
	"testing"

	"github.com/Ploos-AS/preparedness/internal/calc"
	"gopkg.in/yaml.v3"
)

type file struct {
	Vectors []struct {
		ID       string             `yaml:"id"`
		Tool     string             `yaml:"tool"`
		Inputs   map[string]float64 `yaml:"inputs"`
		Expected map[string]float64 `yaml:"expected"`
	} `yaml:"vectors"`
}

func closeEnough(got, want float64) bool {
	const epsilon = 1e-9
	return math.Abs(got-want) <= epsilon*math.Max(1, math.Abs(want))
}

func TestContractVectors(t *testing.T) {
	b, err := os.ReadFile("../../data/common/toolkit-test-vectors.yaml")
	if err != nil {
		t.Fatal(err)
	}
	var f file
	if err := yaml.Unmarshal(b, &f); err != nil {
		t.Fatal(err)
	}
	for _, v := range f.Vectors {
		t.Run(v.ID, func(t *testing.T) {
			var got float64
			var err error
			switch v.Tool {
			case "water":
				got, err = calc.WaterLitres(int(v.Inputs["people"]), int(v.Inputs["days"]), v.Inputs["litres_per_person_day"])
				if err == nil && !closeEnough(got, v.Expected["litres"]) {
					t.Fatalf("got %v want %v", got, v.Expected["litres"])
				}
			case "battery":
				got, err = calc.BatteryWh(v.Inputs["voltage_v"], v.Inputs["capacity_ah"])
				if err == nil && !closeEnough(got, v.Expected["nominal_wh"]) {
					t.Fatalf("got %v want %v", got, v.Expected["nominal_wh"])
				}
			case "power":
				got, err = calc.RuntimeHours(v.Inputs["usable_wh"], v.Inputs["load_w"])
				if err == nil && !closeEnough(got, v.Expected["runtime_hours"]) {
					t.Fatalf("got %v want %v", got, v.Expected["runtime_hours"])
				}
			default:
				t.Fatalf("unsupported vector tool %q", v.Tool)
			}
			if err != nil {
				t.Fatal(err)
			}
		})
	}
}
