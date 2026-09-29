package calc

import (
	"math"
	"testing"
)

func TestWaterLitres(t *testing.T) {
	got, err := WaterLitres(2, 3, 3)
	if err != nil || got != 18 {
		t.Fatalf("WaterLitres = %v, %v; want 18, nil", got, err)
	}
}

func TestBatteryWh(t *testing.T) {
	got, err := BatteryWh(12, 10)
	if err != nil || got != 120 {
		t.Fatalf("BatteryWh = %v, %v; want 120, nil", got, err)
	}
}

func TestRuntimeHours(t *testing.T) {
	got, err := RuntimeHours(400, 100)
	if err != nil || got != 4 {
		t.Fatalf("RuntimeHours = %v, %v; want 4, nil", got, err)
	}
}

func TestRejectNonFiniteInputs(t *testing.T) {
	tests := []struct {
		name string
		fn   func() error
	}{
		{"water NaN", func() error { _, err := WaterLitres(1, 1, math.NaN()); return err }},
		{"water Inf", func() error { _, err := WaterLitres(1, 1, math.Inf(1)); return err }},
		{"battery NaN", func() error { _, err := BatteryWh(12, math.NaN()); return err }},
		{"battery Inf", func() error { _, err := BatteryWh(12, math.Inf(1)); return err }},
		{"runtime NaN", func() error { _, err := RuntimeHours(math.NaN(), 10); return err }},
		{"runtime Inf", func() error { _, err := RuntimeHours(100, math.Inf(1)); return err }},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := tt.fn(); err == nil {
				t.Fatal("expected non-finite input to be rejected")
			}
		})
	}
}
