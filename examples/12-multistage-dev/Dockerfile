# Multi-stage Dockerfile for Post 12: Multi-stage builds + dev workflows
#
# Stage 1 (dev): includes Delve debugger, used for local development
# Stage 2 (prod): minimal binary-only image, no debug tools

# ---- dev stage ----
FROM golang:1.24-alpine AS dev

WORKDIR /app

# Install Delve debugger
RUN go install github.com/go-delve/delve/cmd/dlv@latest

COPY . .

# Disable optimizations and inlining so dlv can set breakpoints accurately
RUN go build -gcflags="all=-N -l" -o app .

# dlv exec runs the binary under the debugger, listening on port 2345
# --headless: no interactive terminal needed
# --accept-multiclient: allow reconnects
# --continue: start the program immediately (don't wait for debugger attach)
CMD ["dlv", "exec", "./app", "--headless", "--listen=:2345", "--api-version=2", "--accept-multiclient", "--continue"]

# ---- prod stage ----
# Intermediate stage: compile the binary (not referenced in compose — its output is copied into 'prod')
FROM golang:1.24-alpine AS builder
WORKDIR /app
COPY . .
# Optimized build for production
RUN go build -o app .

FROM alpine:3.19 AS prod
WORKDIR /app
COPY --from=builder /app/app .
EXPOSE 8080
CMD ["./app"]
