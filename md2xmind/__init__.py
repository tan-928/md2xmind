# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
MD2Xmind: Convert Markdown files to XMind format

@Author  : Tan_928
@Time    : 2019-07-20 05:05
@desc    : A Python package to convert Markdown documents to XMind mindmap format
"""

from md2xmind.Md2Xmind import Md2Xmind, process_file, process_content


def start_trans_file(md_file, target_file_name, topic_name=''):
    """
    Convert a Markdown file to XMind format.
    
    Args:
        md_file (str): Path to the Markdown file to be converted
        target_file_name (str): Name or path for the output XMind file
                               Note: If file exists, it will be deleted and recreated
        topic_name (str): Main topic name for the mindmap (optional)
        
    Returns:
        str: Path to the generated XMind file
    """
    return Md2Xmind.process_file(md_file, target_file_name, topic_name)


def start_trans_content(md_content, target_file_name, topic_name=''):
    """
    Convert Markdown content string to XMind format.
    
    Args:
        md_content (str): Markdown content as a string
        target_file_name (str): Name or path for the output XMind file
                               Note: If file exists, it will be deleted and recreated
        topic_name (str): Main topic name for the mindmap (optional)
        
    Returns:
        str: Path to the generated XMind file
    """
    return Md2Xmind.process_content(md_content, target_file_name, topic_name)


# Backward compatibility - legacy function name
def start_trans(md_file, target_file_name, topic_name=''):
    """
    Legacy function name for backward compatibility.
    Converts a Markdown file to XMind format.
    
    Args:
        md_file (str): Path to the Markdown file to be converted
        target_file_name (str): Name or path for the output XMind file
        topic_name (str): Main topic name for the mindmap (optional)
        
    Returns:
        str: Path to the generated XMind file
    """
    return start_trans_file(md_file, target_file_name, topic_name)


# Export the main class and functions
__all__ = [
    'Md2Xmind',
    'start_trans_file', 
    'start_trans_content',
    'start_trans'  # for backward compatibility
]
