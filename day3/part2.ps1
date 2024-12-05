$data = Get-Content data.txt

$totalValue = 0

$output = $data | Select-String -Pattern "(?:mul\((\d{1,3}),(\d{1,3})\)|(?:do\(\)|don\'t\(\)))" -AllMatches

$sortOut = $false
foreach($match in $output.Matches) {
    if ($match -match "do\(\)") {
        $sortOut = $false
    } elseif ($match -match "don't\(\)") {
        $sortOut = $true
    }   
    if ((-not $sortOut) -and -not ($match -match "do\(\)")) {
        $totalValue += [int]$match.Groups[1].Value * [int]$match.Groups[2].Value
    }
}

Write-Output "The total Value is: $totalValue"

