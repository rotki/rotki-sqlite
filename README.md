# rsqlite3

A Python 3.13 SQLite3 extension module with static SQLite build support.

The release workflow builds wheels for both standard (`cp313`) and
free-threaded (`cp313t`) Python 3.13 interpreters.

## Building

This project supports building with a statically linked SQLite library. The sqlite3.c and sqlite3.h amalgamation files are included in the repository.

### Build with uv

To build the wheel with static SQLite using uv:

```bash
uv build --wheel
```

### Build with setuptools directly

To build with the static SQLite amalgamation:

```bash
python setup.py build_static bdist_wheel
```

This will create a wheel file in the `dist/` directory with SQLite statically compiled into the extension.

## Features

The static build includes the following SQLite features:
- FTS3/FTS4/FTS5 (Full Text Search)
- JSON1 extension
- RTREE (R-Tree index)
- Math functions
- Load extension support
- And more...
