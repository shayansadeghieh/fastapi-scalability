package main

import (
	"fmt"
	"math/rand"
	"time"

	vegeta "github.com/tsenart/vegeta/lib"
)

func main() {
	rate := vegeta.Rate{Freq: 1, Per: time.Second} // x requests per second
	duration := 1 * time.Second

	targeter := NewCustomTargeter()
	attacker := vegeta.NewAttacker()
	var metrics vegeta.Metrics
	for res := range attacker.Attack(targeter, rate, duration, "Load Test") {
		metrics.Add(res)
	}
	metrics.Close()
	fmt.Printf("%+v  \n", metrics)
}

func NewCustomTargeter() vegeta.Targeter {
	return func(tgt *vegeta.Target) error {
		if tgt == nil {
			return vegeta.ErrNilTarget
		}

		tgt.Method = "POST"
		tgt.URL = "http://127.0.0.1:9000/hungry"

		rand := generateFourDigitRandom()

		payload := fmt.Sprintf(`{ "id": "%04d", "item": "burgers" }`, rand)
		tgt.Body = []byte(payload)
		return nil
	}
}

func generateFourDigitRandom() int {
	return rand.Intn(10000)
}
