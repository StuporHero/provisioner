# Copyright 2022 Michael Juliano
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import shutil
from context import Context
from urllib.parse import urlparse


class File:
    def __init__(self, path: str):
        self.__path = path

    @property
    def exists(self) -> bool:
        return os.path.exists(self.__path)


def file(context: Context, source: str, destination: str) -> File:
    return File(shutil.copy(urlparse(source).path, destination))
