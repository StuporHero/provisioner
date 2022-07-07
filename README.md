# provisioner

A Python-based provisioner for use with packer.

The main motivation behind creating this is to have a lightweight declarative provisioner
for use-cases that would currently be handled by shell scripts. The shell provisioner for
packer gets complicated quickly, so having this should make it easier to do simple things
with a pleasant syntax. The main differentiating attribute of this when compared to other
tools like Ansible, Chef, and Puppet is that this provisioner is specifically designed to
facilitate the creation of immutable infrastructure rather than to manage infrastructure.

## Copyright 2022 Michael Juliano

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
