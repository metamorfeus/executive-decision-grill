param([string]$Dir,[string]$Title,[string]$Model="opus")
# Opens a visible PowerShell window running one headless Claude Code helper in $Dir (outside any repo).
git -C $Dir rev-parse 2>$null
if ($LASTEXITCODE -eq 0) { throw "Folder is inside a git repo: $Dir" }
$cmd = "`$Host.UI.RawUI.WindowTitle = '$Title'; Set-Location '$Dir'; claude -p 'Read task_prompt.md in this folder and do exactly what it says.' --model $Model --output-format json --permission-mode acceptEdits --allowedTools 'Bash(python:*)' | Out-File -Encoding utf8 result.json; Write-Host 'FINISHED - see result.json'"
Start-Process powershell.exe -WorkingDirectory $Dir -ArgumentList "-NoExit","-ExecutionPolicy","Bypass","-Command",$cmd
