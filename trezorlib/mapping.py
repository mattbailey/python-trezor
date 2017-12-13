# This file is part of the TREZOR project.
#
# Copyright (C) 2012-2016 Marek Palatinus <slush@satoshilabs.com>
# Copyright (C) 2012-2016 Pavol Rusnak <stick@satoshilabs.com>
# Copyright (C) 2016      Jochen Hoenicke <hoenicke@gmail.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

from . import messages
from . import protobuf

map_type_to_class = {}
map_class_to_type = {}

def build_map():
    for msg_name in dir(messages.MessageType):
        if msg_name.startswith('__'):
            continue

        try:
            msg_class = getattr(messages, msg_name)
        except AttributeError:
            raise
            raise ValueError("Implementation of protobuf message '%s' is missing" % msg_name)

        wire_type = getattr(messages.MessageType, msg_name)

        map_type_to_class[wire_type] = msg_class
        map_class_to_type[msg_class] = wire_type


def get_type(msg):
    return map_class_to_type[msg.__class__]


def get_class(t):
    return map_type_to_class[t]

build_map()
