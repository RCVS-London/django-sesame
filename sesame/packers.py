from __future__ import unicode_literals

import struct
import uuid


class BasePacker(object):
    """
    Abstract base class for packers.

    """

    def pack_pk(self, user_pk):
        """
        Create a short representation of the primary key of a user.

        Return bytes.

        """

    def unpack_pk(self, data):
        """
        Extract the primary key of a user from a signed token.

        Return the primary key and the remaining bytes.

        """


class IntPacker(object):
    @staticmethod
    def pack_pk(user_pk):
        return struct.pack(str("!i"), user_pk)

    @staticmethod
    def unpack_pk(data):
        return struct.unpack(str("!i"), data[:4])[0], data[4:]


class UUIDPacker(object):
    @staticmethod
    def pack_pk(user_pk):
        return user_pk.bytes

    @staticmethod
    def unpack_pk(data):
        return uuid.UUID(bytes=data[:16]), data[16:]


class CharPacker:
    @staticmethod
    def encode(data: str) -> int:
        b = data.encode("utf-8")
        return int.from_bytes(b, byteorder='big')

    @staticmethod
    def decode(data: int) -> bytes:
        return data.to_bytes(((i.bit_length() + 7) // 8), byteorder='big'), data


PACKERS = {"AutoField": IntPacker, "IntegerField": IntPacker, "UUIDField": UUIDPacker, "CharField": CharPacker}
