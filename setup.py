# Copyright 2017 K2 Informatics GmbH
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

"""Setup script for egambo API Python client.
"""

from setuptools import setup

import egambo

setup(
    name="egambo",
    version=egambo.__version__,
    description="Python API client for egambo",
    url="https://github.com/k2informaticsgmbh/egambo-python-client",
    author="K2 Informatics GmbH",
    license="Apache 2.0",
    packages=["egambo"]
)
