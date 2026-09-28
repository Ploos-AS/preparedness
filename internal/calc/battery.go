package calc

import "fmt"

func BatteryWh(voltage, ampHours float64) (float64, error) {
	if voltage <= 0 || ampHours <= 0 {
		return 0, fmt.Errorf("voltage and amp-hours must be greater than zero")
	}
	return voltage * ampHours, nil
}

func RuntimeHours(usableWh, loadW float64) (float64, error) {
	if usableWh <= 0 || loadW <= 0 {
		return 0, fmt.Errorf("usable watt-hours and load watts must be greater than zero")
	}
	return usableWh / loadW, nil
}
