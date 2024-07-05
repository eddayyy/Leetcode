# Save this as git_commands.ps1

# Run the Python script
Write-Output "Executing update.py..."
python update.py

# Check if the Python script executed successfully
if ($LASTEXITCODE -ne 0) {
    Write-Output "No Updates"
    exit $LASTEXITCODE
}

# Run the git add command
Write-Output "Executing git add..."
git add .

# Run the git commit command
Write-Output "Executing git commit..."
git commit -m "Updating solutions"

# Run the git push command
Write-Output "Executing git push..."
git push
