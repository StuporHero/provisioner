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
from context.local import LocalPosixContext
from pytest import raises


def test_should_turn_a_plain_path_into_a_file_uri():
    target = LocalPosixContext()
    assert target.normalize_destination(__file__) == f'file://{__file__}'


def test_should_fail_when_given_a_uri_to_normalize():
    with raises(Exception) as e:
        target = LocalPosixContext()
        target.normalize_destination('file://bad')
    assert 'Destination should not be a URI: file://bad' in str(e.value)
