package handler

import (
	"fmt"
	"net/http"
)

// Handler responds with a greeting message.
// It writes "Hello from PSPDFKit Engineer!" to the response writer.
func Handler(w http.ResponseWriter, _ *http.Request) {
	fmt.Fprintf(w, "Hello from PSPDFKit Engineer!")
}
