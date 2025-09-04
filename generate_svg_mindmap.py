#!/usr/bin/env python3
"""
Generate an SVG mindmap visualization of the ASDF schemas
"""

import xml.etree.ElementTree as ET
import math
import json

def create_svg_mindmap():
    # SVG dimensions
    width, height = 1400, 1000
    center_x, center_y = width // 2, height // 2
    
    # Create SVG root
    svg = ET.Element("svg", {
        "width": str(width),
        "height": str(height),
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": f"0 0 {width} {height}"
    })
    
    # Add styles
    style = ET.SubElement(svg, "style")
    style.text = """
        .root-node { fill: #28a745; stroke: #1e7e34; stroke-width: 3px; }
        .main-schema { fill: #007bff; stroke: #0056b3; stroke-width: 2px; }
        .keyword-schema { fill: #6f42c1; stroke: #5a32a3; stroke-width: 2px; }
        .property { fill: #fd7e14; stroke: #e8590c; stroke-width: 1px; }
        .link { stroke: #6c757d; stroke-width: 2px; fill: none; }
        .text { font-family: Arial, sans-serif; text-anchor: middle; dominant-baseline: central; fill: white; font-weight: bold; }
        .text-small { font-size: 10px; }
        .text-medium { font-size: 12px; }
        .text-large { font-size: 14px; }
        .background { fill: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); }
    """
    
    # Add background
    bg = ET.SubElement(svg, "rect", {
        "width": str(width),
        "height": str(height),
        "fill": "#f8f9fa"
    })
    
    # Schema data (simplified for SVG generation)
    schemas = [
        {"name": "Catalog", "type": "main", "keywords": ["observation", "instrument", "catalog"]},
        {"name": "Combined 1D", "type": "main", "keywords": ["observation", "instrument", "calibration", "wavelength", "pointing", "g2dp_common"]},
        {"name": "Individual 1D", "type": "main", "keywords": ["observation", "instrument", "calibration", "wavelength", "pointing", "g2dp_common"]},
        {"name": "Decontaminated 2D", "type": "main", "keywords": ["observation", "instrument", "calibration", "wavelength", "pointing", "g2dp_common"]},
        {"name": "Data Quality", "type": "main", "keywords": ["observation", "instrument", "catalog"]},
        {"name": "Location Table", "type": "main", "keywords": ["observation", "instrument", "location_table"]}
    ]
    
    keyword_details = {
        "observation": ["ID_OBS", "FILESET_ID", "PROGNUM", "SEGMENT", "VISNUM"],
        "instrument": ["optical_element"],
        "catalog": ["id_catalog"],
        "calibration": ["version_cdp_cal_file"],
        "wavelength": ["wl_contamination_range", "wl_reference", "unit_flux", "unit_wl"],
        "pointing": ["pos_wcs_field_center_ra", "pos_wcs_field_center_dec"],
        "g2dp_common": ["version_g2dp_software", "id_g2dp_run"],
        "location_table": ["dither", "nsrc", "optical_model", "v3yangle"]
    }
    
    # Draw central node
    root_circle = ET.SubElement(svg, "circle", {
        "cx": str(center_x),
        "cy": str(center_y),
        "r": "50",
        "class": "root-node"
    })
    
    root_text = ET.SubElement(svg, "text", {
        "x": str(center_x),
        "y": str(center_y),
        "class": "text text-large"
    })
    root_text.text = "WFI Spectroscopy"
    
    # Position main schemas in a circle around center
    num_schemas = len(schemas)
    main_radius = 200
    
    for i, schema in enumerate(schemas):
        angle = 2 * math.pi * i / num_schemas
        schema_x = center_x + main_radius * math.cos(angle)
        schema_y = center_y + main_radius * math.sin(angle)
        
        # Draw connection line
        line = ET.SubElement(svg, "line", {
            "x1": str(center_x),
            "y1": str(center_y),
            "x2": str(schema_x),
            "y2": str(schema_y),
            "class": "link"
        })
        
        # Draw schema node
        schema_circle = ET.SubElement(svg, "circle", {
            "cx": str(schema_x),
            "cy": str(schema_y),
            "r": "35",
            "class": "main-schema"
        })
        
        # Schema text
        schema_text = ET.SubElement(svg, "text", {
            "x": str(schema_x),
            "y": str(schema_y),
            "class": "text text-medium"
        })
        schema_text.text = schema["name"]
        
        # Position keywords around each schema
        keyword_radius = 120
        num_keywords = len(schema["keywords"])
        
        for j, keyword in enumerate(schema["keywords"]):
            if num_keywords == 1:
                keyword_angle = angle
            else:
                keyword_angle = angle + (j - (num_keywords-1)/2) * 0.6 / num_keywords
            
            keyword_x = schema_x + keyword_radius * math.cos(keyword_angle)
            keyword_y = schema_y + keyword_radius * math.sin(keyword_angle)
            
            # Keep within bounds
            keyword_x = max(60, min(width-60, keyword_x))
            keyword_y = max(60, min(height-60, keyword_y))
            
            # Draw connection line
            keyword_line = ET.SubElement(svg, "line", {
                "x1": str(schema_x),
                "y1": str(schema_y),
                "x2": str(keyword_x),
                "y2": str(keyword_y),
                "class": "link",
                "stroke-width": "1"
            })
            
            # Draw keyword node
            keyword_circle = ET.SubElement(svg, "circle", {
                "cx": str(keyword_x),
                "cy": str(keyword_y),
                "r": "25",
                "class": "keyword-schema"
            })
            
            # Keyword text
            keyword_text = ET.SubElement(svg, "text", {
                "x": str(keyword_x),
                "y": str(keyword_y),
                "class": "text text-small"
            })
            keyword_text.text = keyword.replace("_", " ").title()
    
    # Add legend
    legend_x = 50
    legend_y = height - 200
    
    legend_items = [
        ("Root Schema", "root-node", 15),
        ("Main Schemas", "main-schema", 12),
        ("Keyword Schemas", "keyword-schema", 10),
        ("Properties", "property", 8)
    ]
    
    legend_bg = ET.SubElement(svg, "rect", {
        "x": str(legend_x - 10),
        "y": str(legend_y - 20),
        "width": "200",
        "height": str(len(legend_items) * 25 + 30),
        "fill": "rgba(255,255,255,0.9)",
        "stroke": "#ccc",
        "rx": "5"
    })
    
    legend_title = ET.SubElement(svg, "text", {
        "x": str(legend_x + 90),
        "y": str(legend_y),
        "class": "text text-medium",
        "fill": "#333"
    })
    legend_title.text = "Legend"
    
    for i, (label, class_name, radius) in enumerate(legend_items):
        item_y = legend_y + 25 + i * 25
        
        # Legend circle
        legend_circle = ET.SubElement(svg, "circle", {
            "cx": str(legend_x + 15),
            "cy": str(item_y),
            "r": str(radius),
            "class": class_name
        })
        
        # Legend text
        legend_text = ET.SubElement(svg, "text", {
            "x": str(legend_x + 40),
            "y": str(item_y),
            "class": "text text-small",
            "fill": "#333",
            "text-anchor": "start"
        })
        legend_text.text = label
    
    # Add title
    title = ET.SubElement(svg, "text", {
        "x": str(center_x),
        "y": "30",
        "class": "text text-large",
        "fill": "#333",
        "font-size": "20px"
    })
    title.text = "Roman WFI Spectroscopy ASDF Schema Structure"
    
    return svg

def save_svg():
    svg = create_svg_mindmap()
    
    # Convert to string and save
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    tree = ET.ElementTree(svg)
    tree.write("/workspace/wfi_schemas_mindmap.svg", encoding="utf-8", xml_declaration=True)
    print("✅ Generated SVG mindmap: wfi_schemas_mindmap.svg")

if __name__ == "__main__":
    save_svg()