# Helper function to rename the last saved file
def rename_last_saved(folder,new_name):
    # Get list of files
    files = os.listdir(folder)
    # Filter out non-CSV files and sort by modification time
    csv_files = [f for f in files if f.endswith('.csv')]
    csv_files.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))
    # Get the last saved file
    last_saved_file = csv_files[-1]
    # Rename the file
    os.rename(os.path.join(folder, last_saved_file), os.path.join(folder, new_name))
