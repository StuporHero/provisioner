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
from context.local import LocalPosixContext
from resources import file, File
from tempfile import TemporaryDirectory


def test_should_not_say_a_file_exists_if_it_does_not():
    target = File('/path/does/not/exist')
    assert not target.exists


def test_should_say_a_file_exists_if_it_does():
    target = File(__file__)
    assert target.exists


def test_should_copy_local_file_to_the_destination():
    with TemporaryDirectory() as dir:
        context = LocalPosixContext()
        result = file(
            context=context,
            source=f'file://{__file__}',
            destination=os.path.join(dir, 'test_file')
        )
        assert result.exists
