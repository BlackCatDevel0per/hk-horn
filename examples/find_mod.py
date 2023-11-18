from __future__ import annotations

from pprint import pprint
from typing import TYPE_CHECKING

from hk_horn import HornAPI
from hk_horn.enums import ModAttrs

if TYPE_CHECKING:
	from hk_horn.models import Mod


if __name__ == '__main__':
	horn = HornAPI()
	result: list[Mod] = horn.find_mod_by(
		fields=ModAttrs.name,
		# fields='name',

		ptrn='HK',

		# stop=2,
	)

	pprint(result)


	result_names = [mod.name for mod in result]

	pprint(result_names)
