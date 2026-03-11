# YAML Processor

A lightweight **YAML-based task runner** designed to simplify operational scripts and replace complex Bash automation with structured, readable configuration.

This tool allows you to define automation workflows in YAML and execute them as CLI commands. It is especially useful for **DevOps workflows, deployment pipelines, infrastructure tasks, and local automation**.

Instead of maintaining large `deploy.sh` or `setup.sh` scripts, you can define the same logic in YAML with support for **template variables, services configuration, and reusable steps**.

---

# Why YAML Processor?

Bash scripts often grow into large, hard-to-maintain files.

Example problem:

```
deploy.sh
```

```bash
git clone https://repo
cd service
npm install
npm run build
sudo systemctl restart api
ansible-playbook deploy.yml
```

Problems:

* Hard to maintain
* Hard to parameterize
* Hard to reuse
* Difficult to document

YAML Processor solves this by introducing **structured automation**.

Example YAML:

```yaml
name: deploy-blog
version: 1

gitUrl: https://github.com/AyushAher/blog

services:
  - name: api
    port:
      - 3000

steps:
  - echo Cloning repository
  - git clone {{gitUrl}}
  - echo Restarting {{services.$0.name}}
```

---

# Features

* YAML-based task automation
* Template variable support
* Service definitions
* Sequential step execution
* CLI-based execution
* Safe YAML parsing
* Modular architecture
* Works with existing tools (Ansible, Docker, Git, etc.)

---

# Use Cases

YAML Processor is designed to help with:

### DevOps automation

```
build
test
deploy
cleanup
```

### Deployment pipelines

Instead of large deployment scripts:

```
deploy.sh
```

Use:

```
deploy.yaml
```

### Infrastructure tasks

Examples:

* Docker deployments
* Ansible orchestration
* Terraform operations
* Server maintenance

Example:

```yaml
steps:
  - docker compose pull
  - docker compose up -d
```

### Homelab automation

Useful for managing local infrastructure.

Example:

```yaml
steps:
  - git pull
  - docker build -t api .
  - docker compose restart
```

---

# Installation

Clone the repository:

```
git clone https://github.com/AyushAher/Yaml_Processor.git
cd Yaml_Processor
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Usage

Run a YAML workflow:

```
python cli.py sample.yaml
```

The processor will:

1. Load the YAML configuration
2. Resolve template variables
3. Parse execution steps
4. Execute commands sequentially

---

# YAML Structure

A YAML file can contain the following sections.

## Basic Structure

```yaml
name: sampleYaml
version: 1

gitUrl: https://github.com/example/repo

services:
  - name: api
    port:
      - 3000

steps:
  - echo Starting deployment
  - git clone {{gitUrl}}
```

---

# Template Variables

You can reference values defined in the YAML file.

Example:

```yaml
steps:
  - echo Deploying {{services.$0.name}}
```

Access rules:

```
{{object.field}}
{{list.$index.field}}
```

Example:

```
{{services.$1.name}}
```

---

# Example Configuration

```yaml
name: deploy-service
version: 1

gitUrl: https://github.com/company/service

services:
  - name: Node-Api
    port:
      - 3000
      - 3001

  - name: dotnet-api
    port:
      - 71009

steps:
  - echo Cloning repository
  - git clone {{gitUrl}}
  - echo Starting {{services.$0.name}}
```

---

# How It Works

Execution flow:

```
YAML File
   ↓
Load YAML
   ↓
Resolve Template Variables
   ↓
Parse Steps
   ↓
Execute Commands
```

Commands are executed using Python's `subprocess` module.

---

# Security Notes

* YAML files are parsed using `yaml.safe_load`
* Shell commands are executed without `shell=True`
* Template variables are validated during parsing

Only run YAML configurations from **trusted sources**.

---

# Project Structure

```
Yaml_Processor/
│
├── cli.py
├── sample.yaml
├── requirements.txt
│
├── Services/
│   ├── ProcessYaml.py
│   ├── Yaml_Runner.py
│   └── SaveFile.py
```

---

# Future Improvements

Planned enhancements include:

* `.env` support for environment variables
* Task-based execution
* Parallel task execution
* Dependency graph for tasks
* Logging system
* Dry-run mode
* Workspace isolation

---

# Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# License

This project is licensed under the MIT License.
