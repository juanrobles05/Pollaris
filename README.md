# Pollaris

Pollaris is a modern election management platform designed to help organizations conduct secure, transparent, and reliable voting processes.

The platform aims to provide a structured alternative to traditional voting methods such as paper ballots, manual counting, or generic online forms.

Pollaris is being developed both as a functional system and as a technical learning project exploring modern software engineering practices.

---

## Motivation

Many organizations and communities still conduct elections using informal methods such as:

* Paper ballots
* Manual vote counting
* Raising hands during meetings
* Online form tools

These approaches can lead to human errors, limited transparency, and difficulty auditing the voting process.

Pollaris aims to provide a simple but robust platform to manage elections in a controlled and reliable way.

---

## Project Goals

This project aims to explore and implement modern development practices, including:

* Backend API development
* Frontend application architecture
* CI/CD pipelines
* Containerized infrastructure
* High availability systems
* Distributed system design
* Blockchain-based vote verification (experimental)

---

## Core Features (MVP)

The initial version of Pollaris focuses on the essential components required to conduct a digital election.

* Election creation and management
* Candidate registration
* Voter management
* Secure vote submission
* Automatic vote counting
* Election results visualization

---

## Architecture Overview

The system is designed as a modular web application with separate frontend and backend services.

Planned technologies include:

Backend

* FastAPI

Frontend

* Next.js

Database

* PostgreSQL

Infrastructure

* Docker

Future versions may include caching, distributed services, and blockchain-based auditing.

---

## Project Structure

docs/          # Project documentation

```
pollaris/
│
├── docs/          # Project documentation
├── backend/       # Backend API
├── frontend/      # Web application
└── infra/         # Infrastructure configuration
```

---

## Developer instructions

To run the backend locally, see [`backend/README.md`](backend/README.md) for detailed steps on creating the virtual environment, installing dependencies, and running the server.

---

## Documentation

Detailed project documentation is available in the `docs` directory.

* `product.md` — Product definition and goals
* `roadmap.md` — Project development roadmap
* `architecture.md` — System architecture decisions

---

## Development Status

Pollaris is currently in early development.

The project roadmap includes multiple phases covering backend development, frontend implementation, infrastructure setup, and advanced system features.

---

## License

This project is licensed under the MIT License.
