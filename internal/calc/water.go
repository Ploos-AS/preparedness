package calc

import (
	"fmt"
	"math"
)

func WaterLitres(people int, days int, litresPerPersonDay float64) (float64, error) {
	if people <= 0 || days <= 0 || litresPerPersonDay <= 0 || math.IsNaN(litresPerPersonDay) || math.IsInf(litresPerPersonDay, 0) {
		return 0, fmt.Errorf("people, days and litres-per-person-day must be finite and greater than zero")
	}
	return float64(people) * float64(days) * litresPerPersonDay, nil
}
