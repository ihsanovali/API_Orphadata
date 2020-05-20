# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Product6GeneExternalReference(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, source: str=None, reference: str=None):  # noqa: E501
        """Product6GeneExternalReference - a model defined in Swagger

        :param source: The source of this Product6GeneExternalReference.  # noqa: E501
        :type source: str
        :param reference: The reference of this Product6GeneExternalReference.  # noqa: E501
        :type reference: str
        """
        self.swagger_types = {
            'source': str,
            'reference': str
        }

        self.attribute_map = {
            'source': 'Source',
            'reference': 'Reference'
        }
        self._source = source
        self._reference = reference

    @classmethod
    def from_dict(cls, dikt) -> 'Product6GeneExternalReference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product6_Gene_ExternalReference of this Product6GeneExternalReference.  # noqa: E501
        :rtype: Product6GeneExternalReference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self) -> str:
        """Gets the source of this Product6GeneExternalReference.


        :return: The source of this Product6GeneExternalReference.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this Product6GeneExternalReference.


        :param source: The source of this Product6GeneExternalReference.
        :type source: str
        """

        self._source = source

    @property
    def reference(self) -> str:
        """Gets the reference of this Product6GeneExternalReference.


        :return: The reference of this Product6GeneExternalReference.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Product6GeneExternalReference.


        :param reference: The reference of this Product6GeneExternalReference.
        :type reference: str
        """

        self._reference = reference
