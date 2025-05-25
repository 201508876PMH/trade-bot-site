import re

# Input file
input_file = "full_backtest_report.txt"

# Define sections and their output filenames
sections = [
    ("BACKTESTING REPORT", "backtest_report.md"),
    ("LEFT OPEN TRADES REPORT", "left_open_trades_report.md"),
    ("ENTER TAG STATS", "enter_tags.md"),
    ("EXIT REASON STATS", "exit_tags.md"),
    ("MIXED TAG STATS", "mixed_tags.md"),
    ("SUMMARY METRICS", "summary_metrics.md"),
    ("STRATEGY SUMMARY", "strategy_summary.md"),
]

# Read full content
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Find each section start index
split_indices = []
for title, _ in sections:
    match = re.search(rf"\n.*{re.escape(title)}.*\n", content)
    if match:
        split_indices.append((title, match.start(), match.end()))

# Add final EOF index
split_indices.append(("EOF", len(content), len(content)))

# Extract and write each section
for i in range(len(sections)):
    section_title, start_idx, end_idx = split_indices[i]
    _, next_start, _ = split_indices[i + 1]

    section_content = content[end_idx:next_start].strip()

    # Remove heading line if it's only the title (e.g., STRATEGY SUMMARY)
    # Also remove any empty lines right before the table
    section_lines = section_content.splitlines()
    cleaned_lines = []
    skip_next_blank = True
    for line in section_lines:
        if skip_next_blank and line.strip() == "":
            continue
        cleaned_lines.append(line)
        skip_next_blank = False

    output_filename = sections[i][1]
    with open(output_filename, "w", encoding="utf-8") as out:
        out.write("\n".join(cleaned_lines).strip() + "\n")

    print(f"✓ Cleaned and wrote: {output_filename}")
