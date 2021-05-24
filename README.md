# PyxelSand 2

> PyxelSand2 is a rewrite of the [PyxelSand](https://github.com/HarryPeach/PyxelSand) project, which is a "falling sand" style game written with the Python game engine: [Pyxel](https://github.com/kitao/pyxel)

![pyxel-210524-184203](https://user-images.githubusercontent.com/4750998/119386676-c7b16800-bcbf-11eb-9221-e9b1b868dfe1.gif)

## How to install
1. Install [Poetry](https://python-poetry.org/)
2. Run `poetry install` in the root directory
3. Run `poetry run python -m sand_game`
4. (Optional) Run `poetry run pytest` to run the unit tests

## How to play
- **Left click** places the currently selected particle
- **Right click** removes particles under the cursor
- **Space** pauses and resumes the simulation

## License

This software is licensed under the GPLv3 license. The full license can be found in the LICENSE file.

```
Copyright (C) 2021  Harry Peach

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```