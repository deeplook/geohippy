"""
Workers to be used for multiprocessing.
"""

import subprocess

import redis


def start_redis(*args):
    """Start a vanilla Redis server.
    """
    subprocess.check_call("redis-server")
