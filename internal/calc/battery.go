package calc

import (
	"fmt"
	"math"
)

func positiveFinite(values ...float64) bool {
	for _, value := range values {
		if value <= 0 || math.IsNaN(value) || math.IsInf(value, 0) {
			return false
		}
	}
	return true
}

func BatteryWh(voltage, ampHours float64) (float64, error) {
	if !positiveFinite(voltage, ampHours) {
		return 0, fmt.Errorf("voltage and amp-hours must be finite and greater than zero")
	}
	return voltage * ampHours, nil
}

func RuntimeHours(usableWh, loadW float64) (float64, error) {
	if !positiveFinite(usableWh, loadW) {
		return 0, fmt.Errorf("usable watt-hours and load watts must be finite and greater than zero")
	}
	return usableWh / loadW, nil
}
