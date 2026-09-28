package calc

import "testing"

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
