from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from platformdirs import user_cache_dir

if TYPE_CHECKING:
	from typing import Final

__all__ = (
	'ROOT_REPO',
	'SCHEMAS_DIRNAME',
	'API_FILENAME',
	'MOD_FILENAME',
	'MOD_NSMAP',

	'PACKAGES_CACHE',

	'SCHEMAS_DIR',
	'SCHEMA_API_LINKS',
	'SCHEMA_MOD_LINKS',
	'API_LINKS',
	'MOD_LINKS',
)


ROOT_REPO: Final[str] = 'modlinks'
SCHEMAS_DIRNAME: Final[str] = 'Schemas'

API_FILENAME: Final[str] = 'ApiLinks.xml'
MOD_FILENAME: Final[str] = 'ModLinks.xml'

# TODO: ...
MOD_NSMAP: Final[str] = 'https://github.com/HollowKnight-Modding/HollowKnight.ModLinks/HollowKnight.ModManager'


# TODO: ...
PACKAGES_CACHE: Final[Path] = Path(user_cache_dir('horn'))


SCHEMAS_DIR: Final[Path] = Path(ROOT_REPO, SCHEMAS_DIRNAME)

SCHEMA_API_LINKS: Final[Path] = Path(SCHEMAS_DIR, API_FILENAME)
SCHEMA_MOD_LINKS: Final[Path] = Path(SCHEMAS_DIR, MOD_FILENAME)

API_LINKS: Final[Path] = Path(ROOT_REPO, API_FILENAME)
MOD_LINKS: Final[Path] = Path(ROOT_REPO, MOD_FILENAME)
