from pathlib import Path

# * DIRECTORIES
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
LIB_DIR = Path(BASE_DIR, "lib")
LOGO_FILE = Path(BASE_DIR, "ui", "assets", "logo.png")
LOGO_XS_FILE = Path(BASE_DIR, "ui", "assets", "logo-xs.png")

# * STRINGS
# ---------------------------------------------------------------------------
MSG_ABOUT = "This program is distributed under the END USER LICENSE AGREEMENT (EULA). \n\n" \
            "The sale, distribution, reproduction or modification of this program, " \
            "as well as the files associated and/or used by it for any purpose, " \
            "is prohibited without prior written authorization from the licensee.\n\n" \
            "Copyright (c) 2022 LOREM COMPANY. All rights reserved. \n\n" \
            "Contact: contact@loremcompany.com "
