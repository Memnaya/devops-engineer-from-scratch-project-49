install:
	@uv sync

build:
	@uv build

package-reinstall:
	@uv tool install --force dist/*.whl

package-install:
	@uv tool install dist/*.whl

brain-games:
	@uv run brain-games