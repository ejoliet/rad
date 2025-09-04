#!/usr/bin/env python3
"""
ASDF Schema Visualization Generator
Analyzes Roman Space Telescope WFI Spectroscopy ASDF schemas and creates visualizations
"""

import yaml
import os
import json
from pathlib import Path
from collections import defaultdict

class ASSDFSchemaAnalyzer:
    def __init__(self, schema_dir):
        self.schema_dir = Path(schema_dir)
        self.schemas = {}
        self.relationships = defaultdict(list)
        self.keyword_schemas = {}
        
    def load_schemas(self):
        """Load all YAML schema files"""
        # Load main schemas
        for yaml_file in self.schema_dir.glob("*.yaml"):
            with open(yaml_file, 'r') as f:
                try:
                    content = yaml.safe_load(f)
                    self.schemas[yaml_file.stem] = content
                except yaml.YAMLError as e:
                    print(f"Error loading {yaml_file}: {e}")
        
        # Load keyword schemas
        keywords_dir = self.schema_dir / "keywords"
        if keywords_dir.exists():
            for yaml_file in keywords_dir.glob("*.yaml"):
                with open(yaml_file, 'r') as f:
                    try:
                        content = yaml.safe_load(f)
                        self.keyword_schemas[yaml_file.stem] = content
                    except yaml.YAMLError as e:
                        print(f"Error loading {yaml_file}: {e}")
    
    def analyze_relationships(self):
        """Analyze schema relationships and references"""
        for schema_name, schema_content in self.schemas.items():
            if 'properties' in schema_content and 'meta' in schema_content['properties']:
                meta = schema_content['properties']['meta']
                if 'allOf' in meta:
                    for ref in meta['allOf']:
                        if '$ref' in ref:
                            ref_path = ref['$ref']
                            # Extract the referenced schema name
                            if 'keywords/' in ref_path:
                                keyword_name = ref_path.split('/')[-1].split('-')[0]
                                self.relationships[schema_name].append(('keyword', keyword_name))
                            elif 'ssc_basic' in ref_path:
                                self.relationships[schema_name].append(('base', 'ssc_basic'))
    
    def generate_markdown_mindmap(self):
        """Generate a markdown file suitable for mindmap tools"""
        md_content = []
        md_content.append("# Roman WFI Spectroscopy ASDF Schema Structure")
        md_content.append("")
        md_content.append("## Overview")
        md_content.append("This mindmap represents the hierarchical structure of ASDF schemas for the Roman Space Telescope Wide Field Instrument (WFI) spectroscopy data products.")
        md_content.append("")
        
        # Main schema hierarchy
        md_content.append("## WFI Spectroscopy Level 4 Data Products")
        
        for schema_name, schema_content in self.schemas.items():
            title = schema_content.get('title', schema_name)
            md_content.append(f"### {title}")
            md_content.append(f"- **Schema ID**: `{schema_name}`")
            
            if 'archive_meta' in schema_content:
                md_content.append(f"- **Archive Type**: {schema_content['archive_meta']}")
            
            # Add referenced keywords
            if schema_name in self.relationships:
                md_content.append("- **Metadata Components**:")
                for ref_type, ref_name in self.relationships[schema_name]:
                    if ref_type == 'keyword':
                        if ref_name in self.keyword_schemas:
                            keyword_schema = self.keyword_schemas[ref_name]
                            keyword_title = keyword_schema.get('title', ref_name)
                            md_content.append(f"  - {keyword_title}")
                            
                            # Add properties of keyword schema
                            if 'properties' in keyword_schema:
                                for prop_name, prop_info in keyword_schema['properties'].items():
                                    prop_title = prop_info.get('title', prop_name)
                                    prop_desc = prop_info.get('description', '')
                                    md_content.append(f"    - `{prop_name}`: {prop_title}")
                                    if prop_desc and 'Placeholder' not in prop_desc:
                                        md_content.append(f"      - {prop_desc}")
                    elif ref_type == 'base':
                        md_content.append(f"  - SSC Basic Schema")
            md_content.append("")
        
        # Keyword schemas detail
        md_content.append("## Keyword Schema Details")
        
        for keyword_name, keyword_schema in self.keyword_schemas.items():
            title = keyword_schema.get('title', keyword_name)
            md_content.append(f"### {title}")
            
            if 'properties' in keyword_schema:
                md_content.append("#### Properties:")
                for prop_name, prop_info in keyword_schema['properties'].items():
                    prop_title = prop_info.get('title', prop_name)
                    prop_type = prop_info.get('type', 'unknown')
                    prop_desc = prop_info.get('description', '')
                    
                    md_content.append(f"- **{prop_name}** (`{prop_type}`): {prop_title}")
                    if prop_desc and 'Placeholder' not in prop_desc:
                        md_content.append(f"  - Description: {prop_desc}")
                    
                    # Add archive catalog info if available
                    if 'archive_catalog' in prop_info:
                        archive_info = prop_info['archive_catalog']
                        md_content.append(f"  - Archive: {archive_info.get('datatype', 'unknown')} → {archive_info.get('destination', ['unknown'])[0]}")
            
            if 'required' in keyword_schema:
                md_content.append(f"#### Required Fields: {', '.join(keyword_schema['required'])}")
            
            md_content.append("")
        
        return '\n'.join(md_content)
    
    def generate_mermaid_diagram(self):
        """Generate a Mermaid diagram representation"""
        mermaid_content = []
        mermaid_content.append("```mermaid")
        mermaid_content.append("graph TD")
        mermaid_content.append("    %% Roman WFI Spectroscopy ASDF Schema Structure")
        mermaid_content.append("")
        
        # Root node
        mermaid_content.append("    ROOT[\"WFI Spectroscopy<br/>ASDF Schemas\"]")
        mermaid_content.append("")
        
        # Main schemas
        for schema_name, schema_content in self.schemas.items():
            title = schema_content.get('title', schema_name).replace(' ', '<br/>')
            node_id = schema_name.upper().replace('_', '')
            mermaid_content.append(f"    {node_id}[\"{title}\"]")
            mermaid_content.append(f"    ROOT --> {node_id}")
        
        mermaid_content.append("")
        
        # Keyword relationships
        for schema_name, refs in self.relationships.items():
            schema_node_id = schema_name.upper().replace('_', '')
            for ref_type, ref_name in refs:
                if ref_type == 'keyword':
                    keyword_node_id = ref_name.upper().replace('_', '')
                    keyword_title = self.keyword_schemas.get(ref_name, {}).get('title', ref_name)
                    keyword_title = keyword_title.replace(' ', '<br/>')
                    mermaid_content.append(f"    {keyword_node_id}[\"{keyword_title}\"]")
                    mermaid_content.append(f"    {schema_node_id} --> {keyword_node_id}")
        
        mermaid_content.append("")
        mermaid_content.append("    %% Styling")
        mermaid_content.append("    classDef mainSchema fill:#e1f5fe,stroke:#01579b,stroke-width:2px")
        mermaid_content.append("    classDef keywordSchema fill:#f3e5f5,stroke:#4a148c,stroke-width:2px")
        mermaid_content.append("    classDef rootNode fill:#e8f5e8,stroke:#1b5e20,stroke-width:3px")
        mermaid_content.append("")
        
        # Apply classes
        mermaid_content.append("    class ROOT rootNode")
        for schema_name in self.schemas.keys():
            node_id = schema_name.upper().replace('_', '')
            mermaid_content.append(f"    class {node_id} mainSchema")
        
        for keyword_name in self.keyword_schemas.keys():
            node_id = keyword_name.upper().replace('_', '')
            mermaid_content.append(f"    class {node_id} keywordSchema")
        
        mermaid_content.append("```")
        return '\n'.join(mermaid_content)
    
    def generate_json_structure(self):
        """Generate JSON structure for other visualization tools"""
        structure = {
            "name": "WFI Spectroscopy ASDF Schemas",
            "type": "root",
            "children": []
        }
        
        for schema_name, schema_content in self.schemas.items():
            schema_node = {
                "name": schema_content.get('title', schema_name),
                "type": "main_schema",
                "id": schema_name,
                "children": []
            }
            
            # Add metadata components
            if schema_name in self.relationships:
                for ref_type, ref_name in self.relationships[schema_name]:
                    if ref_type == 'keyword' and ref_name in self.keyword_schemas:
                        keyword_schema = self.keyword_schemas[ref_name]
                        keyword_node = {
                            "name": keyword_schema.get('title', ref_name),
                            "type": "keyword_schema",
                            "id": ref_name,
                            "children": []
                        }
                        
                        # Add properties
                        if 'properties' in keyword_schema:
                            for prop_name, prop_info in keyword_schema['properties'].items():
                                prop_node = {
                                    "name": f"{prop_name}: {prop_info.get('title', prop_name)}",
                                    "type": "property",
                                    "datatype": prop_info.get('type', 'unknown'),
                                    "description": prop_info.get('description', '')
                                }
                                keyword_node["children"].append(prop_node)
                        
                        schema_node["children"].append(keyword_node)
            
            structure["children"].append(schema_node)
        
        return json.dumps(structure, indent=2)

def main():
    analyzer = ASSDFSchemaAnalyzer("/workspace/asdf_schemas")
    analyzer.load_schemas()
    analyzer.analyze_relationships()
    
    # Generate markdown mindmap
    markdown_content = analyzer.generate_markdown_mindmap()
    with open("/workspace/wfi_schemas_mindmap.md", "w") as f:
        f.write(markdown_content)
    
    # Generate Mermaid diagram
    mermaid_content = analyzer.generate_mermaid_diagram()
    with open("/workspace/wfi_schemas_mermaid.md", "w") as f:
        f.write("# WFI Spectroscopy ASDF Schemas - Mermaid Diagram\n\n")
        f.write(mermaid_content)
    
    # Generate JSON structure
    json_content = analyzer.generate_json_structure()
    with open("/workspace/wfi_schemas_structure.json", "w") as f:
        f.write(json_content)
    
    print("✅ Generated visualization files:")
    print("   📄 wfi_schemas_mindmap.md - Detailed markdown mindmap")
    print("   🔄 wfi_schemas_mermaid.md - Mermaid diagram")
    print("   📊 wfi_schemas_structure.json - JSON structure for visualization tools")

if __name__ == "__main__":
    main()