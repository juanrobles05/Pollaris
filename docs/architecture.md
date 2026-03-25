# Pollaris Architecture

## System Overview

Pollaris is designed as a modular web application composed of multiple components.

## Planned Components

Frontend
- Next.js

Backend
- FastAPI

Database
- PostgreSQL

Infrastructure
- Docker

## Backend Architecture

### main
Responsibility:
- Initialize the application
- Register routers
- Start the server

Should Not:
- Contain business logic
- Handle database operations directly

### routers
Responsibility:
- Define HTTP endpoints
- Receive and return HTTP requests and responses
- Validate request structure
- Call application services

Should Not:
- Access the database directly
- Business logic validation

### schemas
Responsibility:
- Define the structure of request and response data
- Validate data types and required fields
- Serialize and deserialize data between the API and aplication

Should Not:
- Access the database
- Define database tables
- implement business logic

### services
Responsibility:
- Implement business logic
- Apply business logic
- Coordinate between models and others components
- Orchestrate application workflows

Should Not:
- Define HTTP endpoints
- Handle request/response directly
- Define database schema
- Manage low-level database connections

### models
Responsibility:
- Define database tables and their structure
- Represent entities in the database
- Define fields, types and relationships

Should Not:
- Implement business logic
- Handle HTTP requests
- Validate request data

### db
Responsibility:
- Manage database connections
- Provide database sessions
- Initialize database configuration

Should Not:
- Contain business logic
- Define application workflows
- Define database tables

### core
Responsibility:
- Manage application configuration
- Store environment settings
- Configure shared components (logging, security, etc)

Should Not:
- Contain business logic
- Handle HTTP requests
