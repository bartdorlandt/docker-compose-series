You've got three containers to run. So you open a terminal and start typing.

`docker run -d --name redis redis:alpine` — fine. `docker run -d --name web -p 8080:80 --network app-net nginx:alpine` — okay. Now add a database, a background worker, and a metrics exporter. Suddenly you have a 200-line shell script that breaks every time someone joins the team and forgets to run it in the right order.

There's a better way.

---

**What is Docker Compose?**

Docker Compose is a tool for defining and running multi-container applications using a single YAML file. Instead of juggling `docker run` commands, you describe your entire stack — services, networks, volumes — in one place, and then bring everything up with a single command.

It ships with Docker Desktop on Mac and Windows. On Linux, install it as a plugin:

```bash
# As the Docker CLI plugin (recommended)
apt install docker-compose-plugin

# Or grab the standalone binary from GitHub releases
```

Once installed, `docker compose up` starts everything. `docker compose down` tears it all down. That's the whole mental model.

---

**From `docker run` to `docker-compose.yml`**

Here's the equivalent of two `docker run` commands written as a compose file (from [`examples/01-intro/`](https://github.com/bartdorlandt/docker-compose-series/tree/main/examples/01-intro/)):

```yaml
services:
  web:
    image: nginx:alpine
    # Expose nginx on port 8080 on your host
    ports:
      - "8080:80"

  cache:
    image: redis:alpine
    # Redis is only reachable by other services in this compose project — not exposed to the host
```

Compare that to the raw Docker commands you'd otherwise need:

```bash
docker network create my-app
docker run -d --name web --network my-app -p 8080:80 nginx:alpine
docker run -d --name cache --network my-app redis:alpine
```

The Compose file is shorter, but the real advantage is what it implies for free: both services land on the same internal network automatically, so `web` can reach `cache` by name. No `--link` flags. No manual network creation. No documentation to keep in sync with a bash script.

And when a teammate clones your repo, they don't need to know any of this. They just run `docker compose up`.

---

**Why this matters beyond convenience**

The Compose file is checked into version control. That means your entire local development environment is code. It evolves with your project, it gets reviewed in pull requests, and it's consistent across every developer's machine.

It also maps directly to what you'll use in production if you move to Docker Swarm, and it gives you a mental model that scales to Kubernetes (where a "pod" is just a group of containers, exactly like a Compose service).

---

**Key takeaways**

- Docker Compose replaces ad-hoc `docker run` chains with a single declarative YAML file
- `docker compose up` starts all services; `docker compose down` removes them cleanly
- Services are automatically placed on a shared internal network — no manual wiring required
- The Compose file lives in version control, making your dev environment reproducible for the whole team
- Docker Desktop bundles Compose; Linux users install the `docker-compose-plugin` package

---

**Try it yourself**

The full example is at [`examples/01-intro/`](https://github.com/bartdorlandt/docker-compose-series/tree/main/examples/01-intro/) in the repo. Clone it and run `docker compose up` — nginx will be live at `http://localhost:8080` in seconds.

How do you currently manage multi-container apps locally? Shell scripts, a Makefile, something else? I'm curious what pain points you've hit — drop a comment below.
