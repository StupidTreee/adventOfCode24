$data = Get-Content data.txt

$2dArray = @()
$safeReportCount = 0
$safeReportCountDamped = 0
$part1UnsafeReports

foreach ($line in $data) {
    $2dArray += ,($line -split '\s+' | ForEach-Object { [int]$_ })
}

function Is-SafeReport {
    param([int[]]$levels)

    $initialDiff = $levels[1] - $levels[0]
    if ($initialDiff -eq 0) { return $false }
    $direction = if ($initialDiff -gt 0) { "Increasing" } else { "Decreasing" }

    for ($i = 1; $i -lt $levels.Length; $i++) {
        $diff = $levels[$i] - $levels[$i-1]

        if ([math]::Abs($diff) -lt 1 -or [math]::Abs($diff) -gt 3) { 
            $part1UnsafeReports += $levels
            return $false 
        }
        if (($direction -eq "Increasing" -and $diff -lt 0) -or
            ($direction -eq "Decreasing" -and $diff -gt 0)) { 
            $part1UnsafeReports += $levels    
            return $false 
        }
    }
    return $true
}

function Problem-Damper {
    param([int[]]$levels)
    for ($i = 0; $i -lt $levels.length; $i++) {
        $newLine = $levels[0..($i-1)] + $levels[($i+1)..($levels.Count - 1)]
        if ((Is-SafeReport -levels $newLine) -eq $true) {
            return $true
        }


    }

}

foreach ($line in $2dArray) {
    if (Is-SafeReport -levels $line) {
        $safeReportCount++
    }
}

foreach ($line in $part1UnsafeReports) {
    if (Problem-Damper -levels $line) {
        $safeReportCountDamped++
    }
}

Write-Output "Number of safe reports: $safeReportCount"
Write-Output "Number of safe reports after Problem-Damper: $safeReportCountDamped"
