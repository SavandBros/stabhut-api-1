from fabric.operations import local


def manage_local(cmd):
    """Run manage.py on local."""
    local(f"python manage.py {cmd}")


def check_isort():
    """Checking imported module sorting and optimization."""
    local("isort --recursive --check-only --diff .")


def apply_isort():
    """Apply optimizing and sorting on module imports. """
    local("isort --recursive --atomic .")


def code_quality():
    """Runs code quality."""
    local("flake8 -j $(grep processor /proc/cpuinfo | wc -l) --config=flake8.ini")
    local("black . --check --exclude migrations --line-length 120")
    check_isort()


def blackify(path="."):
    """Black is the uncompromising Python code formatter."""
    local(f"black {path} --exclude migrations --line-length 120")


def pre_commit():
    """Runs all required code formatters."""
    apply_isort()
    blackify()
    code_quality()
