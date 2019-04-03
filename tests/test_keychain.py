#!/usr/bin/env python3

"""Tests for the package."""

# pylint: disable=line-too-long

import os
import sys
import unittest

#pylint: disable=duplicate-code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import keyper
#pylint: enable=duplicate-code


class KeyperKeychainTests(unittest.TestCase):
    """Test keychain creation."""

    TEST_CERT_PATH = os.path.join(os.path.dirname(__file__), "TestCert_CodeSign.p12")
    TEST_CERT_PASSWORD = "testcertificatepassword"

    def test_temporary_keychain(self):
        """Test that a temporary keychain can be created, read and destroyed."""

        keychain = keyper.Keychain.create_temporary()

        self.assertIsNotNone(keychain.path)
        self.assertIsNotNone(keychain.password)
        self.assertTrue(os.path.exists(keychain.path))
        self.assertTrue(keychain.is_temporary)

        keychain.delete_temporary()

        self.assertFalse(os.path.exists(keychain.path))

    def test_temporary_keychain_context(self):
        """Test that a temporary keychain can be created, read and destroyed via the context manager."""

        with keyper.TemporaryKeychain() as keychain:
            self.assertIsNotNone(keychain.path)
            self.assertIsNotNone(keychain.password)
            self.assertTrue(os.path.exists(keychain.path))
            self.assertTrue(keychain.is_temporary)

        self.assertFalse(os.path.exists(keychain.path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
