[project]
name = "learning-path-evaluator"
version = "0.1.0"
description = "AI environment for evaluating student learning paths"
authors = [{ name = "Prabhav" }]
readme = "README.md"
requires-python = ">=3.9"

dependencies = [
    "fastapi",
    "uvicorn",
    "openai",
    "openenv-core>=0.2.0"
]

[project.scripts]
server = "server.app:app"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
py-modules = ["environment", "inference"]
