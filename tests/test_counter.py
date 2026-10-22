"""Tests for the counter service."""
from unittest import TestCase
from service import app, routes


class CounterTest(TestCase):
    """Counter tests"""

    def setUp(self):
        routes.COUNTERS.clear()
        self.client = app.test_client()

    def test_create_counter(self):
        """It should create a counter"""
        result = self.client.post("/counters/foo")
        self.assertEqual(result.status_code, 201)

    def test_duplicate_counter(self):
        """It should not create a duplicate counter"""
        self.client.post("/counters/foo")
        result = self.client.post("/counters/foo")
        self.assertEqual(result.status_code, 409)

    def test_update_counter(self):
        """It should increment a counter"""
        self.client.post("/counters/foo")
        result = self.client.put("/counters/foo")
        self.assertEqual(result.get_json()["foo"], 1)

    def test_read_counter(self):
        """It should read a counter"""
        self.client.post("/counters/foo")
        result = self.client.get("/counters/foo")
        self.assertEqual(result.status_code, 200)

    def test_delete_counter(self):
        """It should delete a counter"""
        self.client.post("/counters/foo")
        result = self.client.delete("/counters/foo")
        self.assertEqual(result.status_code, 204)
