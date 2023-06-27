# Oddslingers Gaming [![Codecov](https://codecov.io/gh/React-Guru-Org/poker-game/branch/dev/graph/badge.svg?token=FUrKdNe6wp)](https://codecov.io/gh/React-Guru-Org/poker-game) [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

## Project Quickstart

```bash
# make sure you've installed docker: https://docs.docker.com/engine/install/
# and docker-compose: https://docs.docker.com/compose/install/
# you may also have to add your user to the docker group: https://docs.docker.com/engine/install/linux-postinstall/

git clone https://github.com/React-Guru-Org/poker-gamegit
cd oddslingers.poker

# Add to /etc/hosts  ->   127.0.0.1    oddslingers.l

docker-compose run django ./manage.py migrate
docker-compose run django ./manage.py createsuperuser
docker-compose up

# Open http://oddslingers.l
```

## Commands

From here, you could begin to do changes in the codebase and to run these commands for developing tasks:

```bash
# For installing yarn packages
docker-compose run --rm django oddslingers yarn_install
# For testing
docker-compose run --rm django oddslingers testpy
docker-compose run --rm django oddslingers testjs
# For linting
docker-compose run --rm django oddslingers lintpy
docker-compose run --rm django oddslingers lintjs
# For rebuilding docker images and update the python packages
docker-compose build
```

Some useful docker-compose commands:
```bash
# Start the stack
docker-compose start
# Stop the stack
docker-compose stop
# List the services
docker-compose ps
# Init the stack
docker-compose up
# Destroy the stack (This delete the docker containers)
docker-compose down
# Build the docker images
```

## Documentation
 
 - [Setup: Dev](https://github.com/React-Guru-Org/poker-game/wiki/Setup:-Dev) or [Setup: Prod](https://github.com/React-Guru-Org/poker-game/wiki/Setup:-Prod)
 - [Layers of the Stack](https://github.com/React-Guru-Org/poker-game/wiki/Layers-of-the-Stack)
 - [Quickstart & Common Tasks](https://github.com/React-Guru-Org/poker-game/wiki/Common-Tasks)
 - [Project Directory Structure](https://github.com/React-Guru-Org/poker-game/wiki/Folder-Locations)
 - [Configuration](https://github.com/React-Guru-Org/poker-game/wiki/Configuration)
 - [Running Tests & Linters](https://github.com/React-Guru-Org/poker-game/wiki/Running-Tests-&-Linters)
 - [Dependency Documentation](https://github.com/React-Guru-Org/poker-game/wiki/Dependency-Documentation)
 - [Game Engine Documentation](https://github.com/React-Guru-Org/poker-game/wiki/Game-Engine)
 - [Style Guide](https://github.com/React-Guru-Org/poker-game/wiki/Style-Guide)
 - [Debugging & Profiling Tools](https://github.com/React-Guru-Org/poker-game/wiki/Debugging-&-Profiling-Tools)
 - [Git Flow & Making Pull Requests](https://github.com/React-Guru-Org/poker-game/wiki/Git-Flow)

We use the Github [Wiki](https://github.com/React-Guru-Org/poker-game/wiki) for documentation, head over there for more info...