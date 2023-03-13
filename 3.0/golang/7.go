package main

import (
	"fmt"
	"math"
)

func main() {
	var ah, am, as int
	var bh, bm, bs int
	var ch, cm, cs int

	fmt.Scanf("%d:%d:%d\n", &ah, &am, &as)
	fmt.Scanf("%d:%d:%d\n", &bh, &bm, &bs)
	fmt.Scanf("%d:%d:%d\n", &ch, &cm, &cs)

	Asec := float64(as + am*60 + ah*60*60)
	Bsec := bs + bm*60 + bh*60*60
	Csec := float64(cs + cm*60 + ch*60*60)

	var resptime float64
	if Csec < Asec {
		resptime = (24*60*60 + Csec - Asec) / 2
	} else {
		resptime = (Csec - Asec) / 2
	}

	resptimeint := int(math.Round(resptime))
	Bsec += resptimeint

	hours := Bsec / 3600
	minuts := (Bsec - 3600*(Bsec/3600)) / 60
	seconds := (Bsec - 3600*(Bsec/3600)) - 60*minuts
	if hours >= 24 {
		hours -= 24
	}

	fmt.Printf("%02d:%02d:%02d\n", hours, minuts, seconds)
}
