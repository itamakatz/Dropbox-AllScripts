
# enable to run powershell scripts. execute in andmin poershell:
# set-executionpolicy remotesigned

# path to powershell script:
# C:\Users\Itamar\Dropbox\Coding & Tools\3D Printer & Robotics\Printrun Monitor\Printrun Screenshot Monitor.ps1

[Reflection.Assembly]::LoadWithPartialName("System.Drawing")
function screenshot([Drawing.Rectangle]$bounds, $path) {
   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height
   $graphics = [Drawing.Graphics]::FromImage($bmp)

   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)

   $bmp.Save($path)

   $graphics.Dispose()
   $bmp.Dispose()
}

# $shell = New-Object -ComObject "Shell.Application"
# $shell.minimizeall()

$bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1920, 1080)
screenshot $bounds "C:\Users\Itamar\Dropbox\Coding & Tools\3D Printer & Robotics\Printrun Monitor\Printrun Screenshot.png"

start-sleep -Seconds 0.5

# $shell.undominimizeall()