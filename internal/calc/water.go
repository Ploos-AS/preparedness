package calc

import "fmt"

func WaterLitres(people int, days int, litresPerPersonDay float64) (float64, error) {
	if people <= 0 || days <= 0 || litresPerPersonDay <= 0 {
		return 0, fmt.Errorf("people, days and litres-per-person-day must be greater than zero")
	}
	return float64(people) * float64(days) * litresPerPersonDay, nil
}
