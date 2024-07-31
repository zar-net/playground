param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("-c", "-nt")]
    [string]$Option,

    [Parameter(Mandatory=$true)]
    [string]$InputFile
)

if (-Not (Test-Path $InputFile)) {
    Write-Host "Input file not found!"
    exit 1
}

$data = Get-Content $InputFile

if ($Option -eq "-c") {
    $output = "Username,RID,LM Hash,NT Hash" | Out-File -FilePath output.csv -Encoding utf8
    foreach ($line in $data) {
        $parts = $line -split ":"
        $csvLine = "$($parts[0]),$($parts[1]),$($parts[2]),$($parts[3])"
        $csvLine | Out-File -FilePath output.csv -Append -Encoding utf8
    }
    Write-Host "CSV file created: output.csv"
} elseif ($Option -eq "-nt") {
    foreach ($line in $data) {
        $parts = $line -split ":"
        "$($parts[0]),$($parts[3])"
    }
} else {
    Write-Host "Usage: .\parse_ntds.ps1 -Option -c|-nt -InputFile <inputfile>"
}
