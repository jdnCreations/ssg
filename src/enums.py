from enum import Enum


TextType = Enum(
    'TextType',
    ['TEXT', 'BOLD', 'ITALIC', 'CODE', 'LINK', 'IMAGE']
)
