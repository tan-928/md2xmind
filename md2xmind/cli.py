#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Command Line Interface for md2xmind

@Author  : Tan_928
@Time    : 2025-06-20
@desc    : CLI tool to convert Markdown files to XMind format
"""

import argparse
import os
from md2xmind import Md2Xmind

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to XMind")
    parser.add_argument('md_file', type=str, help="Path to the input Markdown file")
    parser.add_argument('-o', '--output', type=str, default=None, help="Path to the output XMind file")
    parser.add_argument('-t', '--topic', type=str, default=None, help="Main topic name for the mindmap")
    args = parser.parse_args()

    md_file = args.md_file
    output_file = args.output if args.output else f"{os.path.splitext(md_file)[0]}.xmind"
    topic_name = args.topic if args.topic else os.path.basename(md_file).split('.')[0]

    try:
        Md2Xmind.process_file(md_file, output_file, topic_name)
        print(f"Successfully converted {md_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
