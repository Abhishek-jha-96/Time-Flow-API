# Time-Flow-API
Backend Repository 

## Prerequisites
1. Docker
2. Docker Compose

## Server Setup Instructions

### Local Environment
- Copy the `.envs/api.env`, `.envs/db.env` and `.envs/services.env` file to `.envs/local`:
   ```bash
   cp .envs/ .envs/local
   ```
### Development Environment
- Copy the `.envs/api.env`, `.envs/db.env` and `.envs/services.env` file to `.envs/dev`:
   ```bash
   cp .envs/ .envs/dev
   ```
### Production Environment
- Copy the `.envs/api.env`, `.envs/db.env` and `.envs/services.env` file to `.envs/prod`:
   ```bash
   cp .envs/ .envs/prod
   ```

### Generate Encryption Keys
1. **Generate SSL Certificate and Private Key**:
   - Use [mkcert](https://github.com/FiloSottile/mkcert#installation) for localhost:
     ```bash
     cd .ssl/ && mkcert localhost && mkcert -install
     ```

2. **Generate Keys for Signing and Verifying JWT Tokens**:
   ```bash
   cd .encryption_keys/
   openssl genrsa -out jwtRS256.key 4096 && openssl rsa -in jwtRS256.key -pubout > jwtRS256.pub
   ```

### Build Server
- To build and run the docker containers use:
```commandline
sh script/build_and_run_server.sh {environment}
```
- To restart or run the docker containers without building again, use:
```commandline
sh script/run_server.sh {environment}
```

### Example Usage
```bash
# Run in development environment
sh script/run_server.sh dev

# Run in production environment
sh script/run_server.sh prod
```

**Access the application at** http://localhost:8000
**Access the Swagger docs at** http://localhost:8000/api/v1/docs/