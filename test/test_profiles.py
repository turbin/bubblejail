# SPDX-License-Identifier: GPL-3.0-or-later

# Copyright 2019, 2020 igo95862

# This file is part of bubblejail.
# bubblejail is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# bubblejail is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with bubblejail.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

from os import environ
from pathlib import Path
from unittest import TestCase
from unittest import main as unittest_main

from tomli import load as toml_load

from bubblejail.bubblejail_instance import BubblejailProfile


class TestProfiles(TestCase):
    def test_profiles(self) -> None:
        meson_source_root = Path(environ['MESON_SOURCE_ROOT'])
        profiles_str_path = (
            meson_source_root / 'data/usr-share/bubblejail/profiles'
        )

        for profile_path in profiles_str_path.iterdir():
            with self.subTest(profile_path.stem):
                with open(profile_path, mode='rb') as f:
                    BubblejailProfile(**toml_load(f))


if __name__ == '__main__':
    unittest_main()
