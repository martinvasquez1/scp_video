#!/bin/bash

set -e

echo "Rendering..."

uv run manim -qh intro.py Intro
uv run manim -qh context.py Context
uv run manim -qh pseudocode.py Pseudocode
uv run manim -qh code_solution.py CodeSolution
uv run manim -qh tn.py TN
uv run manim -qh tn_sol.py TNSolution
uv run manim -qh table_results.py TableResults
uv run manim -qh plot.py Plot
uv run manim -qh end.py End

echo "Concatenating videos..."

cat > concat.txt <<EOF
file 'media/videos/intro/1080p60/Intro.mp4'
file 'media/videos/context/1080p60/Context.mp4'
file 'media/videos/pseudocode/1080p60/Pseudocode.mp4'
file 'media/videos/code_solution/1080p60/CodeSolution.mp4'
file 'media/videos/tn/1080p60/TN.mp4'
file 'media/videos/tn_sol/1080p60/TNSolution.mp4'
file 'media/videos/table_results/1080p60/TableResults.mp4'
file 'media/videos/plot/1080p60/Plot.mp4'
file 'media/videos/end/1080p60/End.mp4'
EOF

ffmpeg -y \
    -f concat \
    -safe 0 \
    -i concat.txt \
    -c copy \
    video.mp4

rm concat.txt

echo "Done: video.mp4"

