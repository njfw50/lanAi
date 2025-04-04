[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Clear-Host
Write-Host "===============================" -ForegroundColor Cyan
Write-Host "       🤖 LANAI CONSOLE         " -ForegroundColor Yellow
Write-Host "===============================" -ForegroundColor Cyan

while ($true) {
    $inputText = Read-Host "`nType your question (or type 'exit' to quit)"

    if ($inputText -eq "exit") {
        Write-Host "`n🛑 Shutting down LanAI..."
        break
    }

    Write-Host "       🤖 LANAI CONSOLE         " -ForegroundColor Yellow
    Write-Host "🧠 LanAI is thinking..." -ForegroundColor Green

    # Chama o script Python e passa a pergunta
    python lanai_core.py $inputText

    Write-Host "`n-----------------------------------"
}

