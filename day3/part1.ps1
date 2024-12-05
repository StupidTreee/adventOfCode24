$data = Get-Content data.txt

$totalValue = 0

$output = $data | Select-String -Pattern 'mul\((\d{1,3}),(\d{1,3})\)' -AllMatches

foreach ( $match in $output.Matches) {
    $totalValue += [int]$match.Groups[1].Value * [int]$match.Groups[2].Value
}
$totalValue