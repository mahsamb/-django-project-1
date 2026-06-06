# Run this INSIDE your cloned GitHub repo folder (where django-project-1.zip is).
# Commits as mahsamb, not the PC git user.

$ErrorActionPreference = "Stop"
$zipName = "django-project-1.zip"

if (-not (Test-Path $zipName)) {
    Write-Host "ERROR: $zipName not found in $(Get-Location)" -ForegroundColor Red
    Write-Host "Place this script in the same folder as the uploaded zip."
    exit 1
}

Write-Host "Extracting $zipName ..."
$temp = Join-Path $env:TEMP "django-extract-$(Get-Random)"
New-Item -ItemType Directory -Path $temp | Out-Null
Expand-Archive -Path $zipName -DestinationPath $temp -Force

Get-ChildItem $temp | ForEach-Object {
    $dest = Join-Path (Get-Location) $_.Name
    if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
    Move-Item $_.FullName $dest
}
Remove-Item $temp -Recurse -Force
Remove-Item $zipName -Force

Write-Host "Zip removed. Committing as mahsamb ..."
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
python "$scriptDir\commit_as_mahsamb.py" "Extract project files from django-project-1.zip"

Write-Host ""
Write-Host "Done. Now push with your mahsamb GitHub account:" -ForegroundColor Green
Write-Host "  git push -u origin main"
