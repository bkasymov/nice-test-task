package handler

import (
	"fmt"
	"net/http"
)

func Handler(w http.ResponseWriter, _ *http.Request) {
	fmt.Fprintf(w, "Hello from PSPDFKit Engineer!")
}
