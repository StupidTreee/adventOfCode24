function checkLine() {
    param(
        [Parameter(Mandatory)]$line
    )
  	Out-Host -InputObject "I'm here"
    $direction = 0
    if ( $line[1] -eq $line[0] ) {
        return -1
    }
    if ( $line[1] -gt $line[0] ) {
        $direction = 1
    }
    else {
        $direction = -1
    }
    for ( $i = 0; $i -lt $line.Count; $i++ ) {
        if ( $i -gt 0 ) {
            if ( $line[$i] -eq $line[$i-1] ) {
                return -1
            }
            if ( ( ( $line[$i] -gt $line[$i-1] ) -and ( $direction -eq -1 ) ) -or `
                 ( ( $line[$i] -lt $line[$i-1] ) -and ( $direction -eq 1 ) ) ) {
                return -1
            }
            if ( ([Math]::Abs($line[$i] - $line[$i-1]) ) -gt 3 ) {
                return -1
            }
        }
    }
    return 0
}
$sum = 0
foreach ( $line in Get-Content -Path ./input2 ) {
    $numbers = [System.Collections.ArrayList]::new($line.Split(" "))
    for ( $i = 0; $i -lt $numbers.Count; $i++ ) {
        $numbers[$i] = [int]$numbers[$i]
    }
    if ( ( checkLine -line $numbers ) -eq -1 ) {
        "Wrong: " + $line
        for ( $i = 0; $i -lt $numbers.Count; $i++ ) {
            $copy = $numbers.Clone()
            $copy.RemoveAt($i)
            if ((checkLine -line $copy) -ne -1) {
                "Good (I made it good): " + $copy
                $sum += 1
                break
            }
        }
    }
    else {
        "Good: " + $line
        $sum += 1
    }
}
$sum