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
from .base import Context
from re import compile


URI_PATTERN = compile(r'\w+:(\/?\/?)[^\s]+')


class LocalPosixContext(Context):
    def normalize_destination(self, destination: str) -> str:
        if URI_PATTERN.match(destination) is not None:
            raise Exception(f'Destination should not be a URI: {destination}')
        return f'file://{destination}'
