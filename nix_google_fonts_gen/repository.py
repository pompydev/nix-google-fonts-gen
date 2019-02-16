import hashlib
import subprocess
import google.protobuf.text_format as text_format

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Iterator

from nix_google_fonts_gen.fonts_public_pb2 import FamilyProto, FontProto


@dataclass
class Font:
    path: Path
    meta: FontProto
    commit: str
    changed: datetime


@dataclass
class Family:
    path: Path
    meta: FamilyProto
    commit: str
    changed: datetime
    fonts: List[Font]

    @property
    def latest_change(self) -> datetime:
        """Return datetime of the latest change affecting this family."""
        return max(
            self.changed,
            *(font.changed for font in self.fonts),
            key=lambda d: d.timestamp()
        )


def families(repository: Path) -> Iterator[Family]:
    """Return iterator over all the font families in repository"""

    def get_font(dir: Path, meta: FontProto):
        font_path = dir / meta.filename
        hash = most_recent_commit(repository, font_path)
        time = commit_time(repository, hash)
        return Font(font_path, meta, hash, time)

    for path in repository.rglob("METADATA.pb"):
        with open(path, "rb") as handle:
            meta = text_format.Parse(handle.read(), FamilyProto())
        dir_path = path.parent
        hash = most_recent_commit(repository, path)
        time = commit_time(repository, hash)
        fonts = [get_font(dir_path, font_meta) for font_meta in meta.fonts]
        yield Family(path, meta, hash, time, fonts)


def most_recent_commit(repo_root: Path, path: Path) -> str:
    """Return commit hash of the most recent commit that affected path."""
    process = subprocess.run(
        ["git", "-C", str(repo_root), "rev-list", "-1", "HEAD", str(path)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return process.stdout.decode("utf-8").strip()


def commit_time(repo_root: Path, hash: str) -> datetime:
    """Return datetime for commit"""
    process = subprocess.run(
        ["git", "-C", str(repo_root), "show", "--quiet", "--format=%ct", hash],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    timestamp = int(process.stdout.decode("utf-8").strip(), 10)
    return datetime.utcfromtimestamp(timestamp)
