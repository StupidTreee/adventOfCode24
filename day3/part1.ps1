$data = Get-Content data.txt

$totalValue = 0

$output = $data | Select-String -Pattern 'mul\((\d{1,3}),(\d{1,3})\)' -AllMatches

#$totalValue += $output.Matches.Value | ForEach-Object { $output.Matches.Groups[1].Value * $output.Matches.Groups[2].Value}

foreach ( $match in $output.Matches) {
    $totalValue += [int]$match.Groups[1].Value * [int]$match.Groups[2].Value
}
$totalValue