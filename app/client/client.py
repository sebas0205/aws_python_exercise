from typing import Union, Any

import boto3


class Services:
    def __init__(self, service: str):
        self.service = service
        self.client = self._get_client()
        self.resource= self._get_resource()

    def _get_client(self):
        """Create a client to the service"""
        return boto3.client(self.service)

    def _get_resource(self):
        "Ccreate a resource"
        return boto3.resource(self.service)
