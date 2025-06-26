# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
MD2Xmind: Convert Markdown files to XMind format

@Author  : Tan_928
@Time    : 2019-07-20 05:04
@desc    : Convert Markdown documents to XMind mindmap format
"""

import os
import zipfile
import xmind
from xmind.core.const import ATTR_AUTHOR


class Md2Xmind:
    """
    A class to convert Markdown content to XMind mindmap format.
    """

    @staticmethod
    def process_file(md_file_path, target_file_name, topic_name=''):
        """
        Process a Markdown file and convert it to XMind format.
        
        Args:
            md_file_path (str): Path to the Markdown file
            target_file_name (str): Name or path for the output XMind file
            topic_name (str): Main topic name for the mindmap (optional)
            
        Returns:
            str: Path to the generated XMind file
        """
        if not os.path.exists(md_file_path):
            raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
        
        # Read the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()
        
        # Get topic name from filename if not provided
        if not topic_name:
            topic_name = Md2Xmind.get_file_name(md_file_path)
        
        return Md2Xmind.process_content(md_content, target_file_name, topic_name)

    @staticmethod
    def process_content(md_content, target_file_name, topic_name=''):
        """
        Process Markdown content and convert it to XMind format.
        
        Args:
            md_content (str): Markdown content as string
            target_file_name (str): Name or path for the output XMind file
            topic_name (str): Main topic name for the mindmap (optional)
            
        Returns:
            str: Path to the generated XMind file
        """
        if not md_content:
            raise ValueError("Markdown content cannot be empty")
        
        # Ensure the target file has .xmind extension
        if not target_file_name.endswith('.xmind'):
            target_file_name += '.xmind'
        
        # Convert to absolute path
        target_xmind_file_path = os.path.abspath(target_file_name)
        
        # Use default topic name if not provided
        if not topic_name:
            topic_name = 'Mindmap'
        
        return Md2Xmind.create_xmind_at_path(md_content, target_xmind_file_path, topic_name)

    @staticmethod
    def create_xmind_at_path(md_content, target_xmind_file_path, topic_name):
        """
        Create an XMind file at the specified absolute path.
        
        Args:
            md_content (str): Markdown content
            target_xmind_file_path (str): Absolute path for the output XMind file
            topic_name (str): Main topic name for the mindmap
            
        Returns:
            str: Path to the generated XMind file
        """
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(target_xmind_file_path), exist_ok=True)

        # Remove existing file if it exists
        if os.path.exists(target_xmind_file_path):
            os.remove(target_xmind_file_path)

        # Create a new XMind workbook
        workbook = xmind.load(target_xmind_file_path)

        # Get the primary sheet
        sheet1 = workbook.getPrimarySheet()

        # Generate mind map on the sheet
        Md2Xmind.handle_content(md_content, sheet1, topic_name)

        # Save the workbook
        xmind.save(workbook)

        # Create and add manifest.xml file for better compatibility
        Md2Xmind._add_manifest_to_xmind(target_xmind_file_path)

        return target_xmind_file_path

    @staticmethod
    def handle_content(md_content, sheet1, topic_name):
        """
        Parse Markdown content and build the mindmap structure.
        
        Args:
            md_content (str): Markdown content
            sheet1: XMind sheet object
            topic_name (str): Main topic name
        """
        content_lines = md_content.split('\n')

        # Initialize root topic
        root_topic = sheet1.getRootTopic()
        
        # Dictionary to store topics at each level
        topics = {1: root_topic}
        
        # Flag to track if we've found the first level 1 heading
        found_first_heading = False

        for line_number, line in enumerate(content_lines, 1):
            line = line.strip()

            if line.startswith('#'):
                # Count the number of # to determine the level
                heading_match = line.split()
                if heading_match:
                    level = len(heading_match[0])
                    # Extract title by removing the # symbols and leading/trailing spaces
                    title = line.lstrip('#').strip()
                    
                    if not title:  # Skip empty headings
                        continue
                    
                    # If this is the first level 1 heading, use it as root topic title
                    if level == 1 and not found_first_heading:
                        root_topic.setTitle(title)
                        found_first_heading = True
                        continue
                    
                    # Find the appropriate parent topic
                    parent_level = level - 1
                    if parent_level not in topics:
                        # If parent level doesn't exist, use the closest available parent
                        available_parents = [l for l in topics.keys() if l < level]
                        if not available_parents:
                            # If no parent is available, use root topic
                            parent_level = 1
                        else:
                            parent_level = max(available_parents)
                    
                    parent_topic = topics[parent_level]

                    # Add new topic
                    new_topic = parent_topic.addSubTopic()
                    new_topic.setTitle(title)

                    # Update topics dictionary
                    topics[level] = new_topic
                    # Remove any deeper levels that are no longer valid
                    topics = {k: v for k, v in topics.items() if k <= level}
            elif line and not line.startswith('```'):
                # Handle non-heading content (optional: can be extended to handle lists, etc.)
                # For now, we only process headings to create a clean mindmap structure
                pass
        
        # If no level 1 heading was found, use the provided topic_name
        if not found_first_heading:
            root_topic.setTitle(topic_name)

    @staticmethod
    def get_file_name(file_path):
        """
        Extract filename without extension from a file path.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            str: Filename without extension
        """
        dirname, filename = os.path.split(file_path)
        name_parts = filename.split('.')
        
        # Join all parts except the last one (extension)
        if len(name_parts) > 1:
            return '.'.join(name_parts[:-1])
        else:
            return filename

    @staticmethod
    def _add_manifest_to_xmind(xmind_file_path):
        """
        Add manifest.xml to the XMind file for better compatibility.
        
        Args:
            xmind_file_path (str): Path to the XMind file
        """
        manifest_content = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns="http://www.xmind.net/manifest/2008">
    <file-entry full-path="content.xml" media-type="application/vnd.xmind.workbook+xml"/>
    <file-entry full-path="Thumbnails/thumbnail.png" media-type="image/png"/>
</manifest>'''
        
        # Create temporary manifest file
        manifest_path = 'manifest.xml'
        try:
            with open(manifest_path, 'w', encoding='utf-8') as f:
                f.write(manifest_content)

            # Add manifest.xml to the XMind file
            with zipfile.ZipFile(xmind_file_path, 'a') as zipf:
                zipf.write(manifest_path, 'META-INF/manifest.xml')
        finally:
            # Clean up temporary file
            if os.path.exists(manifest_path):
                os.remove(manifest_path)


# Legacy function names for backward compatibility
def process_file(md_file_path, target_file_name, topic_name=''):
    """Legacy function for backward compatibility."""
    return Md2Xmind.process_file(md_file_path, target_file_name, topic_name)


def process_content(md_content, target_file_name, topic_name=''):
    """Legacy function for backward compatibility."""
    return Md2Xmind.process_content(md_content, target_file_name, topic_name)