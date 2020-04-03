"""Fabric config file."""
import os
from typing import List

import environ
from fabric.api import env


env.root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
env.use_ssh_config = True

_env = environ.Env()
_env.read_env(os.path.join(env.root, ".env"))

# Project
env.project_name = "stabhut"
env.django_project_dir = "stabhut"
env.project_path = env.root
env.db_config = _env.db("DATABASE_URL")
env.environ = _env

apps = [
    "ticket",
]

translations: List[str] = [
    "en",
    "fa",
]
