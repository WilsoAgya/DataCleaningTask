##DOWNLOADS FOLDER ORGANIZER SCRIPT

#Objective: Automatically organize files in the Downloads folder into categorized subfolders

#### High-Level Approach:
- Access and scan downloads folder
- Decide where each file belongs
- Move files into appropriate folders
- Repeat safely without data loss

#Tasks

#### Access Downloads Folder
- Determine the absolute path to the Downloads history
- Read all items in folder
- Ignore directories and only process files

#### Define file Organization Criteria
- Use file extensions as the primary categorization method
- Group files into logical categories based on type

#### File Type Categories
- Documents
  - `.pdf`, `.docx`, `.txt`
- Images
  - `.jpg`, `.png`, `.gif`
- Videos
  - `.mp4`, `.mov`
- Audio
  - `.mp3`, `.wav`
- Archives
  - `.zip`, `.rar`
- Other
  - Any file types that do not match existing categories

### Organize Files
- Iterate through each file in the Downloads folder
- Extract the file extension
- Match the extension to a category
- Move the file into the appropriate folder
- Handle filename conflicts safely

### Keep Downloads Updated
- Manual execution
  - Run the script whenever cleanup is needed
  - 
### Safety and Edge Cases
- Skip files currently in use
- Do not move the organizer script itself
- Prevent overwriting existing files
- Log moved files for debugging and tracking
- Support a dry-run mode for testing

## Minimal Viable Implementation
- Organize files by extension only
- Create folders automatically
- Run the script manually

## Future Improvements
- Add size-based or date-based organization
- Allow user-configurable rules


