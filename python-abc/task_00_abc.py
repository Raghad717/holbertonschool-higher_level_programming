#!/usr/bin/env python3
"""
Abstract Animal class and its subclasses Dog and Cat
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class Animal
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses
        """
        pass


class Dog(Animal):
    """
    Dog class inheriting from Animal
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class inheriting from Animal
    """

    def sound(self):
        return "Meow"
