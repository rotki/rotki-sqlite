from setuptools import setup, Extension

sqlite_ext = Extension(
    "rsqlite._sqlite3",
    sources=[
        "_sqlite/blob.c",
        "_sqlite/connection.c",
        "_sqlite/cursor.c",
        "_sqlite/microprotocols.c",
        "_sqlite/module.c",
        "_sqlite/prepare_protocol.c",
        "_sqlite/row.c",
        "_sqlite/statement.c",
        "_sqlite/util.c",
        "sqlite3.c"
    ],
    include_dirs=["."],
    define_macros=[
        ("MODULE_NAME", '"rsqlite"'),
        ("PY_SQLITE_ENABLE_LOAD_EXTENSION", "1"),
        ("SQLITE_ENABLE_FTS5", "1"),
        ("SQLITE_ENABLE_JSON1", "1"),
        ("SQLITE_ENABLE_RTREE", "1"),
        ("SQLITE_ENABLE_STAT4", "1"),
        ("SQLITE_ENABLE_COLUMN_METADATA", "1"),
        ("SQLITE_ENABLE_DBSTAT_VTAB", "1")
    ],
    undef_macros=["SQLITE_OMIT_LOAD_EXTENSION"]
)

setup(
    ext_modules=[sqlite_ext]
)