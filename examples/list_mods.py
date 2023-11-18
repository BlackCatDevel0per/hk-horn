from __future__ import annotations

from pprint import pprint
from typing import TYPE_CHECKING

from hk_horn import HornAPI

if TYPE_CHECKING:
	...


if __name__ == '__main__':
	horn = HornAPI()
	mods_lst = list(
			horn.parser.iter_mods(),
		)
	pprint(
		mods_lst,
	)

	print()
	print(f'Mods count: {len(mods_lst)}')
