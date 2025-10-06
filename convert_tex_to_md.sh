#!/bin/bash

# Script to convert all .tex files in tex/ directory to .md files in content/ directory
# and fix equation references for MyST compatibility

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed. Please install pandoc first."
    exit 1
fi

# Check if pandoc-crossref is installed
if ! pandoc --list-extensions | grep -q "crossref"; then
    echo "Warning: pandoc-crossref filter may not be available. Continuing anyway..."
fi

# Create content directory if it doesn't exist
mkdir -p content

# Process each .tex file in the tex/ directory
for tex_file in tex/*.tex; do
    # Check if any .tex files exist
    if [ ! -f "$tex_file" ]; then
        echo "No .tex files found in tex/ directory"
        exit 1
    fi
    
    # Extract filename without extension
    filename=$(basename "$tex_file" .tex)
    
    # Define output file path and temporary file
    output_file="content/${filename}.md"
    temp_file="content/${filename}.md.tmp"
    
    echo "Converting $tex_file to $output_file..."
    
    # Remove existing output file if it exists to force overwrite
    if [ -f "$output_file" ]; then
        echo "Removing existing file: $output_file"
        rm -f "$output_file"
    fi
    
    # Convert .tex to .md using pandoc to temporary file first
    pandoc "$tex_file" \
        -f latex \
        -t commonmark_x+tex_math_dollars \
        --wrap=none \
        --citeproc \
        --metadata=link-citations=true \
        --bibliography=references.bib \
        --filter pandoc-crossref \
        -o "$temp_file"
        
    # pandoc "$tex_file" \
    #     -f latex \
    #     -t commonmark_x+tex_math_dollars-attributes-header_attributes \
    #     --wrap=none \
    #     --citeproc \
    #     --metadata=link-citations=true \
    #     --bibliography=references.bib \
    #     -o "$temp_file"
            
    # Check if conversion was successful
    if [ $? -eq 0 ]; then
        echo "Successfully converted $tex_file"
        
        # Apply regex replacement to fix equation references for MyST
        echo "Fixing equation references for MyST compatibility..."
        
        # Use perl for better UTF-8 handling instead of sed
        # Replace complex equation references with simple MyST format
        # Pattern: [\[label\]](#label){reference-type="ref" reference="label"}
        # Replacement: [](#label)
        perl -i -pe 's/\[\\\[([^]]*)\\\]\]\(#\1\)\{reference-type="ref" reference="\1"\}/[](#\1)/g' "$temp_file"
        
        # Also handle cases without the \[ \] wrapper
        perl -i -pe 's/\[([^]]*)\]\(#\1\)\{reference-type="ref" reference="\1"\}/[](#\1)/g' "$temp_file"
        
        # Clean up headers by removing {#id} attributes
        # Pattern: #### Title. {#id}
        # Replacement: #### Title.
        perl -i -pe 's/^(#{1,6}\s+[^{]+)\s*\{#[^}]+\}\s*$/\1/' "$temp_file"
        
        # Force move temporary file to final location (overwrite)
        mv -f "$temp_file" "$output_file"
        
        echo "Fixed equation references and saved to $output_file"
    else
        echo "Error: Failed to convert $tex_file"
        # Clean up temporary file if it exists
        [ -f "$temp_file" ] && rm "$temp_file"
        exit 1
    fi
done

echo "All .tex files have been successfully converted to .md files!"
echo "Output files are in the content/ directory."
