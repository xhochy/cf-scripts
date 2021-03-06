from .migrators import Rebuild
from .auto_tick import initialize_migrators, migrator_status
import os
import json


def main(args=None):
    gx, *_, migrators = initialize_migrators(do_rebuild=True)
    if not os.path.exists('./status'):
        os.mkdir('./status')

    for migrator in migrators:
        if isinstance(migrator, Rebuild):
            migrator_name = migrator.__class__.__name__.lower()
            if migrator_name == 'rebuild':
                migrator_name = migrator.name.lower().replace(" ", "")
            status, build_order = migrator_status(migrator, gx)
            with open(os.path.join(f'./status/{migrator_name}.json'), 'w') as fo:
                json.dump(
                    status,
                    fo,
                    indent=2
                )

if __name__ == '__main__':
    main()
