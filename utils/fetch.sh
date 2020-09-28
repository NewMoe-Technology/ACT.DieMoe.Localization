#!/bin/bash
git clone --depth 1 https://github.com/EQAditu/AdvancedCombatTracker.git
mkdir -p locales/en-US
mkdir -p locales/zh-CN
python3 utils/convert_xml.py
