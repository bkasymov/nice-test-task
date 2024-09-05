package main

import (
	"log"
	"net/http"
	"nice-test-task/internal/handler"
	"time"
)

func main() {
	http.HandleFunc("/", handler.Handler)
	server := &http.Server{
		Addr:         ":8080",
		Handler:      nil,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		IdleTimeout:  15 * time.Second,
	}
	if err := server.ListenAndServe(); err != nil {
		log.Fatal(err)
	}
}
