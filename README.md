INSTRUCTIONS:
============

Place your text files (.txt) in this folder before running the Invite_formatter.py script.

The formatter can handle invitation lists with formats like:
- John, Doe <john@example.com>; Jane, Smith <jane@example.com>
- FirstName, LastName <email1@domain.com>; FirstName2, LastName2 <email2@domain.com>

Formatting options:
1. Remove email addresses (keep names only)
2. Remove names (keep email addresses only)  
3. Sort alphabetically (must be combined with option 1 or 2)
4. Reverse order (must be combined with option 1 or 2)
5. Combinations (e.g., "1 + 3" for remove emails + alphabetical, "2 + 4" for emails only + reverse)

Note: Options 3 and 4 cannot be selected alone - they must be combined with option 1 or 2.

After formatting, you can choose to revert to the original content if needed.
