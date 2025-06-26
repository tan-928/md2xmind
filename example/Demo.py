#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
MD2Xmind Demo Script

@Author  : Tan_928
@Time    : 2019-07-20 05:09
@desc    : Demonstration of how to use md2xmind package
"""

import os
import md2xmind


def demo_file_conversion():
	"""Demonstrate converting a Markdown file to XMind format."""
	print("=== File Conversion Demo ===")
	
	# Get the path to the test markdown file
	current_dir = os.path.dirname(os.path.abspath(__file__))
	md_file_path = os.path.join(current_dir, 'test2.md')
	
	if not os.path.exists(md_file_path):
		print(f"Warning: Test file {md_file_path} not found.")
		return
	
	# Convert file using the simple API
	try:
		output_path = md2xmind.start_trans_file(
			md_file_path, 
			'demo_output_file.xmind', 
			'Demo Mindmap from File'
		)
		print(f"✓ File conversion successful: {output_path}")
	except Exception as e:
		print(f"✗ File conversion failed: {e}")


def demo_content_conversion():
	"""Demonstrate converting Markdown content string to XMind format."""
	print("\n=== Content Conversion Demo ===")
	
	# Sample Markdown content
	md_content = """# Main Topic
	
## Subtopic 1
### Sub-subtopic 1.1
### Sub-subtopic 1.2

## Subtopic 2
### Sub-subtopic 2.1
#### Deep subtopic 2.1.1
#### Deep subtopic 2.1.2

## Subtopic 3
### Sub-subtopic 3.1
"""
	
	# Convert content using the API
	try:
		output_path = md2xmind.start_trans_content(
			md_content, 
			'demo_output_content.xmind', 
			'Demo Mindmap from Content'
		)
		print(f"✓ Content conversion successful: {output_path}")
	except Exception as e:
		print(f"✗ Content conversion failed: {e}")


def demo_class_usage():
	"""Demonstrate using the Md2Xmind class directly."""
	print("\n=== Class Usage Demo ===")
	
	# Sample Markdown content
	md_content = """# Python Programming
	
## Basics
### Variables
### Data Types
### Control Structures

## Advanced Topics
### Object-Oriented Programming
#### Classes
#### Inheritance
#### Polymorphism

### Functional Programming
#### Lambda Functions
#### Map, Filter, Reduce

## Libraries
### Standard Library
### Third-party Packages
"""
	
	# Use the class directly
	try:
		output_path = md2xmind.Md2Xmind.process_content(
			md_content, 
			'demo_class_usage.xmind', 
			'Python Programming Guide'
		)
		print(f"✓ Class usage successful: {output_path}")
	except Exception as e:
		print(f"✗ Class usage failed: {e}")


def main():
	"""Main function to run all demos."""
	print("MD2Xmind Package Demo")
	print("====================")
	
	demo_file_conversion()
	demo_content_conversion()
	demo_class_usage()
	
	print("\n=== Demo Complete ===")
	print("Check the generated .xmind files in the current directory!")


if __name__ == '__main__':
	main()
