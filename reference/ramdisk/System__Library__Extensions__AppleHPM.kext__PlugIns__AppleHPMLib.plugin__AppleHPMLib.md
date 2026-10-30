# `/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib`

From the upgrade restore ramdisk (141-29011-104.dmg). 92,336 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = BUNDLE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1872)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak
```

## Linked libraries (4)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (53)

```
AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - exit status=0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - first VOUT failed, check if HPM is in DFUf [0x%X], taskRetCode=0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - second VOUT failed, status = [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n
AppleHPMLibRTUpdaterInterface - Check for in ADFU failed\n
-restore
AppleHPMLibRTInterface::%s@0x%llx RID%u - AppleHPMLibRTUpdater - panic debug enabled:%u\n\n
triggerSystemPanic
AppleHPM
AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry. value = 0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - cancelling DFUf failed [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - Forcing CIO + USB2 failed\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - trying VOUT after cancelling DFUf, value = 0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - Read mode failed [0x%X]\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - check for in ADFU failed [0x%X]\n\n
hpmrtdebug
AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry. enable = 0x%X\n\n
forceATCRTUpdateModeCIO
forceATCRTPower
forceATCRTUpdateMode
execVOUT
AppleHPMLibRTUpdaterInterface - Not in DFUf but still failed VOUT\n
AppleHPMLibRTUpdaterInterface - Second VOUT failed\n
AppleHPMLibRTUpdaterInterface - First VOUT failed and cancelling DFUf failed\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - Not in DFUf but still failed VOUT, modeData=0x%x\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - HPM in ADFU\n\n
inADFU
hpmrtlog
AppleHPMLibRTInterface::%s@0x%llx RID%u - Failed to trigger system panic: %u\n
IOService
AppleHPMLibRTUpdaterInterface - forcing CIO + USB2 failed\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - pulling HPM out of DFUf...\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - HPM is NOT in ADFU, modeData=0x%x\n\n
rid
AppleHPMLibRTUpdaterInterface - Read mode failed\n
AppleHPMLibRTInterface
AppleHPMLibRT13Interface::%s@0x%llx RID%u - check for in ADFU failed [0x%X]\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry. enable = 0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - Forcing CIO + USB2 failed\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - exit status=0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - pulling HPM out of DFUf...\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - Not in DFUf but still failed VOUT, modeData=0x%x\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - HPM is NOT in ADFU, modeData=0x%x\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - Read mode failed [0x%X]\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - HPM in ADFU\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - trying VOUT after cancelling DFUf, value = 0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - cancelling DFUf failed [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n
AppleHPMLibRTInterface::%s@0x%llx RID%u - AppleHPMLibRTUpdater - panic debug enabled:%u\n\n
AppleHPMLibRTInterface::%s@0x%llx RID%u - Failed to trigger system panic: %u\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry. value = 0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - first VOUT failed, check if HPM is in DFUf [0x%X], taskRetCode=0x%X\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - second VOUT failed, status = [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n
AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry\n\n
```
