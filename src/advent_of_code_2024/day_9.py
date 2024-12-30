from dataclasses import dataclass
from importlib.resources import files
from typing import List

from advent_of_code_2024.utils import AbstractDataclass


def example_input() -> str:
    return "2333133121414131402"


def problem_input() -> str:
    return files("resources").joinpath("day-9-input.txt").read_text()


@dataclass()
class FilesystemEntry(AbstractDataclass):
    size: int


@dataclass
class FreeSpace(FilesystemEntry):
    pass


@dataclass
class File(FilesystemEntry):
    id: int


Filesystem = List[FilesystemEntry]


def _swap(fs: Filesystem, free_idx: int, file_idx: int) -> Filesystem:
    file = fs[file_idx]
    free = fs[free_idx]
    new_file_slice = [file] + ([FreeSpace(free.size - file.size)] if free.size > file.size else [])
    new_free_slice = [FreeSpace(file.size)]
    return fs[:free_idx] + new_file_slice + fs[free_idx + 1 : file_idx] + new_free_slice + fs[file_idx + 1 :]


def _find_space(fs: Filesystem, min_size: int, start_idx: int) -> int:
    idx = start_idx
    while idx < len(fs):
        if isinstance(fs[idx], FreeSpace) and fs[idx].size >= min_size:
            return idx
        idx += 1
    return -1


def convert_to_blocks(e: FilesystemEntry) -> List[FilesystemEntry]:
    match e:
        case File() as f:
            return [File(1, f.id)] * f.size
        case FreeSpace() as s:
            return [FreeSpace(1)] * s.size


def solution_part_one(s: str) -> int:
    fs = [block for e in _parse_input(s) for block in convert_to_blocks(e)]

    def next_file_idx(idx: int) -> int:
        while idx > 0 and not isinstance(fs[idx], File):
            idx -= 1
        return idx

    free_idx = 0
    file_idx = len(fs) - 1

    while True:
        file_idx = next_file_idx(file_idx)
        free_idx = _find_space(fs, fs[file_idx].size, free_idx)

        if free_idx > file_idx:
            break

        fs = _swap(fs, free_idx, file_idx)

    return sum(idx * x.id for idx, x in enumerate(fs) if isinstance(x, File))


# Part two


def solution_part_two(s: str) -> int:
    fs = _parse_input(s)

    def next_file_idx(id: int) -> int:
        idx = len(fs) - 1
        while idx >= 0:
            if isinstance(fs[idx], File) and fs[idx].id == id:
                return idx
            idx -= 1
        return idx

    file_id = fs[-1].id

    while file_id >= 0:
        file_idx = next_file_idx(file_id)
        free_idx = _find_space(fs, fs[file_idx].size, 0)

        if free_idx != -1 and free_idx < file_idx:
            fs = _swap(fs, free_idx, file_idx)

        file_id -= 1

    fs_blocks = [block for e in fs for block in convert_to_blocks(e)]

    return sum(idx * x.id for idx, x in enumerate(fs_blocks) if isinstance(x, File))


def main() -> None:
    s = problem_input()
    print(solution_part_one(s))
    print(solution_part_two(s))


def _parse_input(s: str) -> List[FilesystemEntry]:
    def parse_chunk(id: int, s: str) -> List[FilesystemEntry]:
        if len(s) == 2:
            return [File(int(s[0]), id), FreeSpace(int(s[1]))]
        else:
            return [File(int(s[0]), id)]

    chunks = [s[i : i + 2] for i in range(0, len(s), 2)]

    return [entry for idx, s in enumerate(chunks) for entry in parse_chunk(idx, s)]


if __name__ == "__main__":
    main()
