# Changelog

## [0.2.0] - 2026-05-07
### Added
- 4 endpoints: register, login, transfer, account
- Authentication
- SQLite database
- Data models for users, accounts and transactions

### Notes
- Phase 1 complete
- Introduced vulnerabilities: 
    - IDOR - /accounts/{id} endpoint returns details without ownership check 
    - Broken authentication - Plaintext passwords + unlimited retries
    - No input validation - negative transfers are allowed

## [0.1.0] - 2026-05-06
### Added
- Initial FastAPI project setup
- `/health` endpoint
- Dockerized application with docker-compose

### Notes
- Phase 0 complete: baseline environment established
- No authentication or data models yet