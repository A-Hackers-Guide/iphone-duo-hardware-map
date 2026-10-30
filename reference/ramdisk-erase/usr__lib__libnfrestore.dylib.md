# `/usr/lib/libnfrestore.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 183,728 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2136)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libnfrestore.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libPN548_API.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libnfshared.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (636)

```
DevicePath
_NFRestoreConfigureSPMIIRQ
%s:%i Error %d at %s
%s:%i Failed to create property matching dictionary
%s:%i Failed to load stack after re-restore.
PN800V A0/A1
Error 0x%04x at %s:%d: %llx %s
%s:%i Dumping EEPROM after failure
_NFRestoreNfcFirmwareStep
%s:%i Selected file %s
Mismatched protected firmware hash
_NFRestoreReadPlatformInfoFromFactoryPage
NfRestoreCopyUniqueFDRKey
yes
nfcWithRadio
%s:%i Command failed: status=0x%04x
%s
%s:%i se object is not valid
IONameMatch
%s:%i Found property %s : %s
NfRestoreSEOpen_Internal
%s:%i No FDR Key !
JcopForceJCOPPostflightScript
NFRestoreNfc
SN300V_FW_B0_02_01_C9_rev170948.bin
SE310S_FW_A0_01_01_D3_rev165460.bin
/usr/standalone/firmware/nfrestore/firmware/fw-hashes/SN450V-hashes.plist
NfSecureElementScriptRun
%s:%i Feature not supported
1
FirmwareBundleData
%s:%i EEPROM User Area Start:0x%08X End:0x%08X
%s:%i Failed to update customer factory page.
_NFRestoreBootMeasurements
%s:%i Failed to decode plist
*
%s:%i Context already exists
SE310S_FW_A0_01_01_41_rev172736.bin
%s:%i Failed to get factory page.
RestoreHammerfest
%s:%i Failed to update OS info
NfSecureElementSetPower
ExportFinished
%s:%i Failed to create iterator
SN100V B0 / B1
HammerfestOnly
%s:%i Factory page E0 clear not supported on this hardware.
SN300V_FW_B0_02_01_88_rev172757.bin
SN450V_FW_A1_01_01_80A_rev14497923.bin
_NFRestoreValidateBootMeasurements
_NFRestoreReadATETrimVersion
%s:%i Bundle is missing RF settings - NFCC might fail RF operation
%s:%i Failed to update FW: %s
SN450V_FW_B0_02_01_015_rev48936220.bin
apply
%s:%i Failed to get controller info..
> %s\n
%s:%i Failed to get OS info
NFHardwareSkipSpmiReconfig
AppleStockholmControl
%s:%i Address Start:0x%08X End:0x%08X
stockholm-spmi
%s:%i Transceive failed
FirmwareBundlePath
StockholmOnly
Hammerfest
%s:%i Failed to configure EDT settings : 0x%x
%s:%i Executed %d lines successfully
%s:%i Failed to scan directory %u : %s
%s:%i \"%s\" errno=%d failed to stat parent: %s
SN100V_FW_A3_01_01_B6_rev157827.bin
SN200V_FW_B1_02_01_FA_rev124452.bin
%s:%i Failed to get info.
%s:%i Failed to find matching file for %02x_%02x_%02x (%@)
%s:%i Customer factory page is locked
%s:%i This is a SIP, NED or Dev, skipping antenna test
%s:%i Failed to delete existing file: %s
%s:%i \"%s\" errno=%d Failed to open %s
hammerfest-spmi
 
_NFRestore
%s\n
_NfRestoreBundleGetFileHandle
AppleHammerfestSPMI
IOClass
se-spmi-irq
SN300V B1
PN552_FW_02_01_6A_rev125914.bin
%s:%i Failed to restore after load failure.
%s:%i Running customer factory page update with %s
_NFRestoreDebugNFCCError
%s:%i Error : Invalid TLV: 0x%x
%s:%i Wrote to file: %s
%s:%i \"%s\" errno=%d parent is not directory: %s
fury-fw
SN200V_FURY_FW_B1_02_01_AE_rev170322.bin
%s:%i Failed to query Boot measurements
%s:%i Failed to parse index file as dictionary
%s:%i Failed to check antenna : 0x%x
NfSecureElementScriptRunLine
%s:%i \"%s\" errno=%d stat failed
NfSecureElementOpen
LogAPDU
com.apple.nfstack
kNfUpdateParamQueryFDRKey
%s:%i Failed to load stack after RF settings. Bailing
%s:%i Error : Unexpected TLV: 0x%x
%02X_%02X_%02X
NfRestoreBundleScan
.
nfrestore-loop
kNfUpdateParamIntegrity
JcopPostflightScript
%s:%i Found exact plist match: %s
_NFHardwareWalkTree
NfRestoreInvalidateProhibitTimer
NFRestoreParseParams
%s:%i No RF for this device.
%s:%i Failed to read index file
absent
com.apple.nfjcop
Idle
%s:%i migration=%s pkgs=%d inst=%d
%s:%i No matching files
/%s
%s:%i %s has property %s : %s
_NFHardwareLookInTree
RootFilePath
%s:%i Ignoring file of type %d: %s
AppleStockholmControlUserClient
Customer factory page
%s:%i Skipping SPMIIRQ
%s:%i Radio %s.
/dev/
NFHardwareInterfaceIsSupported
%s:%i Failed to load driver
_NFRestorePushError
%s:%i Iteration %d of %d
%s:%i Failed %d
NfcUpdateFile
%s:%i Failed to clear E0 tag : %d
PN800V_FW_A0_01_01_A8_rev164283.bin
\r\n
%s:%i FDR Key : %s
CLIRestore
%s:%i %s
%s:%i Customer factory page is already locked with production content. Nothing to do.
NfSecureElementClose
IOUserClientClass
Unknown
InvokedFromCommandLine
SN100V_FW_A3_01_01_C3_rev78599.bin
_NfRestoreCustomerFactoryPageUpdate
%s:%i Unexpected NULL parameter
%s:%i Encoding error: %s
%s:%i Failed to enter wired mode
%s:%i id=%s dev=0x%02x hw=0x%08x fw=0x%04x cfw=0x%04x restricted=%s OSUpdate=%s
mobile
NfcMaxFwDlRetries
_NfRestoreStripHeaderFromPlatformInfoTLV
SN100V_FW_A3_
AuxiliaryDevicePath
NFHardwareSerialIsSupported
%s:%i Failed to create matching dictionary
%s:%i Failed to get valid service
SN300V B0
Stockholm
PN800V_FW_A1_01_01_B4_rev47094117.bin
%02X.%02X.%03X
%02X.%02X.%02X
ignore
fixup
%s:%i Failed to write factory page : %d
PN80v ES2.1
SN300V B20
SN200V_FURY_FW_B1_02_01_FA_rev149466.bin
value
%s:%i Unexpected length mismatch : %zu vs %zu
%s:%i Factory page already has production content. Nothing to do.
Error 0x%04x at %s:%d
%s:%i Failed to write to path: %s
PN600V
index.plist
SN450V_FW_A1_
%s:%i Failed to get OS mode
ImportInProgress
_NFHardwareDumpIOKit
_NFHardwareIsEntryMatching
com.apple.nfrestore
%s:%i Skipping Stockholm restore
%s:%i Error: Failed to validate boot measurements
%s:%i Erasing firmware flags.
SN200V_FURY_FW_B1_
%s:%i calloc failure...
NfSecureElementUpdateOSInfo
ExportPreparation
%s:%i No data found for %s
%s:%i ROM version %02x.%02x
%s:%i Failed to load plist
w
%s:%i ----------------------- IOService plane --------------------------
PN800V_FW_A1_01_01_14_rev46806918.bin
%s:%i Chip version %02x.%02x.%02x
SN450V_FW_B1_03_01_815_rev49087064.bin
rf
%s:%i Failed find IOKit service
%s:%i Failed to shut down Stockholm
%s:%i Validating boot measurements
Mismatched protected lifecycle hash
%s:%i ATE Trim version is %x (%d)
NO
%s:%i Failed to open SE
%s:%i Firmware: %x.%x rev %d
true
NFRestoreParseBootArgs
RestoreSystemPartition
ClearE0Tag
%s:%i Failed to open driver
%s:%i RF not supported
UNKNOWN
%s:%i Matched name %s, returned 0x%04x
???
JcopTerminateApplets
_NFRestoreClearE0Tag
NFRestoreNfcFirmwareNameForController
%s:%i Unexpected ROM version %02x.%02x
/usr/standalone/firmware/nfrestore/firmware/fury-fw-hashes/PN800V-hashes.plist
%s:%i Failed to get file name %s
SN210V B1
SE310S A0
%s:%i Failed to load stack - retrying FW download
%s:%i Failed to allocate NfSecureElement_t
%s:%i Failed to parse bundle data
NFRestoreRFSettingsForController
%s:%i Customer factory page is locked without production content ! Skipping for older devices
%s:%i Retry...
%s:%i Failed to write data to %s
%s:%i mode=%s counter=%d reference=%d osid=0x%02x othervalid=0x%02x
%s:%i %s found
IOMatchCategory
InvalidBStateSettingsPolicy
Mismatched info hash
%s:%i Failed to open %s
Update
%s:%i Failed find IOKit service %s
LogNCI
DisableBootMeasurementEnforcement
PN552_FW_02_01_AF_59162.bin
SN450V_FW_A1_01_01_00A_rev14059249.bin
%s:%i Using custom hashes
%s:%i Failed to configure HW Settings: %d
_NFRestoreRunPostFlight
StockholmOptions
%s:%i Provided buffer too small for result: %zu
kern.bootargs
kNfUpdateAntennaSelfTest
%s:%i Failed to read file: %s
%s:%i snprintf error
%s/%s
StockholmRestore.plist
ExportInProgress
%s:%i Middleware: %x.%x.%x.%x
NfcRFSettingsFile
fw
%s:%i Failed to validate Boot measurements
%s:%i Warning : more than 1 TLV : %d
_NFRestoreConfigureHWSettings
%s:%i 
NfRestoreBundleCreate
FactoryInstall
NFRestoreNfcForController
%s:%i Failed to install %s
PN800V_FW_A0_01_01_08_rev163891.bin
Mismatched scratch firmware hash
%s:%i Error : unexpected length %d
%s:%i Error : more than 1 TLV : %d
IOService
%s:%i Warning: failed to validate boot measurements, skipping
fw-unlock
_NfRestoreCustomerFactoryPageMatches
_NFRestoreNfcRFStep
%02X_%02X_%03X
NULL
%s:%i Will %s spmi for %s
nfc,primary,gpio
%s:%i Failed to load stack
SN200V B0
SN450V B0/B1/B2
com.apple.spmi.nfc.hammerfest
NFCBootHashOverride
Dump: 
%s:%i Incorrect bundle
Current platform info from customer factory page is 
%s:%i Failed to create errorValue CFString
com.apple.stockholm
%s:%i Failed to scan %s
%s:%i Unexpected Si version %02x.%02x
%s:%i Bundle is missing folder: rf
%s:%i Customer factory page is already locked with debug content. Nothing to do.
skip
%s:%i Running postflight: %s
NfRestoreSEDumpControllerInfo
%s:%i **************** Restoring Hammerfest ****************
HammerfestFirmwareType
%s:%i Failed at line %d: %s
nfrestore: %s\n
_NFHardwarePrintNode
%s:%i %s has matching {%s / %s}
%s:%i Failed to shut down Hammerfest
NfcForceFwDl
mask
%s:%i \"%s\" errno=%d Failed to stat at %s
%s:%i Failed to build target path: %s
hammerfest
%s:%i Failed to create context
Unknown PN80v
SN100V B2
NfRestoreRunIntegrityCheck
_NfRestoreCopyCustomerPageUpdateFirmware
not reconfigure
%s:%i Failed to lookup service : 0x%x
%s:%i %s has no child
LockFactoryPage
%s:%i Configuring NFCC to use GPIO %d as data IRQ
%s:%i Customer factory page is locked without production content !
%s:%i se=%d, enabled=%d
JCOP
%s:%i Failed to create CF property string
=
%s:%i Update LPCD settings failed; continue
%s:%i Failed to disable boost
fw-mfg
%s:%i Retrieving boot measurements
%s:%i Failed to update customer factory page
.plist
present
%s:%i Failed to create NfRestoreSE object
SN300V B21
%s:%i ==== CONTROLLER ====
%s:%i Invalid hashes length
%s:%i Invalid hex string
AppleStockholmSPMI
%s:%i %s has child %s
%s:%i **************** Restoring Stockholm ****************
SN200V_FW_B1_
_NFRestoreWriteFactoryPage
%s:%i Writing factory page (E0:%s F0:%s 02:%s 03:%s 04:%s 05:%s 06:%s)
AppleHammerfestControl
com.apple.
NfRestoreSETransceiveToOS
%s:%i Failed to reconfigure I/O : 0x%x
debug
%s:%i Unknown encoding error
%s:%i Invalid iterator
%s:%i Unmatched interface %s
SN300V_FW_B0_
prod
ReadyForImport
IONameMatched
SN450V A0/A1
NfRestoreReturnError
FDR Key : %s\n
NFRestoreDictionaryCopyDataForKey
%s:%i Invalid format
%s:%i Failed to update RF settings.
%s:%i Received: %s
_NfRestoreBundleWrite
%s:%i Assuming HW not present
Error at %s:%d
%s:%i Failed to install FW
%s:%i Currently running version 0x%04X, rev %d
??
SN200V B1
LogMW
No FDR Key !\n
%s:%i Bundle is missing folder: %s
SN450V_FW_B0_
_NfRestoreHasRadio
skip-spmi-reconfig
reconfigure
%s:%i Failed to get driver info
%s:%i Invalid boot-arg length: %zu
_NFRestoreShutdownNFCC
_NFRestoreGenericHardwareError
SN450V_FW_B1_03_01_015_rev48923467.bin
stockholm
IOPropertyMatch
%s:%i Failed to get iterator for service
%s:%i Driver already open. This is bad
fury-fw-mfg
%s:%i Stack loaded after re-restore.
%s:%i Malformed Customer page !
%s:%i Failed to find file %s
PN800V_FW_A0_
%s:%i R-APDU does not match expected prefix!
%s:%i Expected: %s
%s:%i Failed to parse params
YES
Mismatched scratch lifecycle hash
_NFRestoreLoadStackAndRestoreOnFailure
%s:%i Failed to configure NFCC to use GPIO %d as data IRQ : %d
%s:%i Failed to run script
_NfRestoreBundleValidateTargetPath
nfc,secondary,gpio
SimulateRestoreOS
%s:%i Found boot-arg \"%s\" = \"%s\"
fury-rf
%s:%i Bundle is missing folder: fury-rf
%s:%i TX LDO current is %d
%s:%i R-APDU does not match expected suffix!
_NFHardwareFindMatchingService
%s:%i Nothing to do
SN450V_FW_B0_02_01_814_rev46829584.bin
%s:%i More than 1 file matching %02x_%02x_%02x
%s:%i Failed to get factory page : %d
%s:%i No radio key, skipping RF settings.
_NFRestoreJcop
%s:%i Could not find service with: %s, retrying slow path
%s:%i Unexpected state.
ForceVenReset
%s:%i Failed to read boot-args: %d
SN200V_FW_B1_02_01_BA_rev170350.bin
%s:%i Error : invalid length %d
%s:%i Locking factory page (%s)
Manufacturing
NFHardwareInterfaceHasExternalSPMIIRQ
%s:%i %s driver already open - can't interrupt
%s:%i Found matching unlock firmware: %s
%s:%i Using data from %s
%s:%i No external SPMIIRQ
_NfRestoreRunAntennaSelfCheck
%s:%i %s NOT found
%s:%i Failed to get controller info
%s:%i Hardware: %x.%x (%s)
%s:%i Skipping Hammerfest restore.
[Hex dump: length=%lu bytes] (%s:%i %s)
EEPROM User Area: 
PN800V_FW_A1_
SN450V_FW_B1_
_NfRestoreBundleReadDir
NfRestoreSEEnumerate
%s:%i Failed at iteration %d
%{public}s:%i Skipping SPMIIRQ
%{public}s:%i Feature not supported
%{public}s:%i Hardware: %x.%x (%s)
%{public}s:%i %s driver already open - can't interrupt
%{public}s:%i Incorrect bundle
%{public}s:%i Failed to read index file
%{public}s:%i Failed to parse index file as dictionary
%{public}s:%i Failed to update customer factory page.
%{public}s:%i Failed to install FW
%{public}s:%i Selected file %s
%{public}s:%i Bundle is missing RF settings - NFCC might fail RF operation
%{public}s:%i R-APDU does not match expected prefix!
%{public}s:%i Nothing to do
%{public}s:%i Failed to update FW: %s
%{public}s:%i Iteration %d of %d
%{public}s:%i Failed at iteration %d
%{public}s:%i No matching files
%{public}s:%i Found exact plist match: %s
%{public}s:%i Customer factory page is locked without production content ! Skipping for older devices
%{public}s:%i Failed to scan directory %u : %s
%{public}s:%i Failed to write data to %s
%{public}s:%i ==== CONTROLLER ====
%{public}s:%i Failed to configure EDT settings : 0x%x
%{public}s:%i More than 1 file matching %02x_%02x_%02x
%{public}s:%i Failed to update OS info
%{public}s:%i Failed to create matching dictionary
%{public}s:%i Matched name %s, returned 0x%04x
%{public}s:%i Unexpected state.
%{public}s:%i Dumping EEPROM after failure
%{public}s:%i Failed to decode plist
%{public}s:%i Failed to get factory page.
%{public}s:%i Running postflight: %s
%{public}s:%i id=%s dev=0x%02x hw=0x%08x fw=0x%04x cfw=0x%04x restricted=%s OSUpdate=%s
%{public}s:%i Invalid iterator
%{public}s:%i Failed to get driver info
%{public}s:%i **************** Restoring Stockholm ****************
%{public}s:%i %s
%{public}s:%i Warning : more than 1 TLV : %d
%{public}s:%i Unexpected length mismatch : %zu vs %zu
%{public}s:%i Writing factory page (E0:%s F0:%s 02:%s 03:%s 04:%s 05:%s 06:%s)
%{public}s:%i Failed to check antenna : 0x%x
%{public}s:%i Failed at line %d: %s
%{public}s:%i Skipping Stockholm restore
%{public}s:%i Unexpected Si version %02x.%02x
%{public}s:%i Error : Invalid TLV: 0x%x
%{public}s:%i Factory page already has production content. Nothing to do.
%{public}s:%i Failed to open %s
%{public}s:%i Failed to get OS mode
%{public}s:%i Failed to get OS info
%{public}s:%i Failed find IOKit service %s
%{public}s:%i Failed to get controller info
%{public}s:%i FDR Key : %s
%{public}s:%i Using custom hashes
%{public}s:%i Error : invalid length %d
%{public}s:%i TX LDO current is %d
%{public}s:%i \"%s\" errno=%d Failed to stat at %s
%{public}s:%i Failed to enter wired mode
%{public}s:%i Erasing firmware flags.
%{public}s:%i Failed to clear E0 tag : %d
%{public}s:%i Failed to find matching file for %02x_%02x_%02x (%@)
%{public}s:%i Received: %s
%{public}s:%i Executed %d lines successfully
%{public}s:%i Will %s spmi for %s
%{public}s:%i Firmware: %x.%x rev %d
%{public}s:%i Failed to shut down Stockholm
%{public}s:%i Update LPCD settings failed; continue
%{public}s:%i Bundle is missing folder: %s
%{public}s:%i %s has property %s : %s
%{public}s:%i Failed to shut down Hammerfest
%{public}s:%i Failed to configure HW Settings: %d
%{public}s:%i Failed to write factory page : %d
%{public}s:%i %s found
%{public}s:%i Provided buffer too small for result: %zu
%{public}s:%i Address Start:0x%08X End:0x%08X
%{public}s:%i Invalid format
%{public}s:%i Locking factory page (%s)
%{public}s:%i snprintf error
%{public}s:%i Failed to build target path: %s
%{public}s:%i Failed to write to path: %s
%{public}s:%i \"%s\" errno=%d stat failed
%{public}s:%i Failed to create context
%{public}s:%i Failed to scan %s
%{public}s:%i Failed to load stack after RF settings. Bailing
%{public}s:%i \"%s\" errno=%d Failed to open %s
%{public}s:%i se=%d, enabled=%d
%{public}s:%i Failed to load stack
%{public}s:%i Assuming HW not present
%{public}s:%i **************** Restoring Hammerfest ****************
%{public}s:%i Failed to get controller info..
%{public}s:%i se object is not valid
%{public}s:%i Failed to open SE
%{public}s:%i Chip version %02x.%02x.%02x
%{public}s:%i Failed to load plist
%{public}s:%i Customer factory page is locked without production content !
%{public}s:%i Expected: %s
%{public}s:%i Encoding error: %s
%{public}s:%i Skipping Hammerfest restore.
%{public}s:%i Transceive failed
%{public}s:%i No FDR Key !
%{public}s:%i Failed to reconfigure I/O : 0x%x
%{public}s:%i This is a SIP, NED or Dev, skipping antenna test
%{public}s:%i %s has child %s
%{public}s:%i Found property %s : %s
%{public}s:%i Unmatched interface %s
%{public}s:%i Failed %d
%{public}s:%i Failed to install %s
%{public}s:%i Unexpected NULL parameter
%{public}s:%i 
%{public}s:%i Failed to lookup service : 0x%x
%{public}s:%i Failed to load driver
%{public}s:%i Middleware: %x.%x.%x.%x
%{public}s:%i Failed to read file: %s
%{public}s:%i Failed to find file %s
%{public}s:%i Failed to allocate NfSecureElement_t
%{public}s:%i Failed to create property matching dictionary
%{public}s:%i Failed to create iterator
[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)
%{public}s:%i ROM version %02x.%02x
%{public}s:%i Customer factory page is locked
%{public}s:%i R-APDU does not match expected suffix!
%{public}s:%i %s has no child
%{public}s:%i Failed to disable boost
%{public}s:%i No data found for %s
%{public}s:%i Failed to query Boot measurements
%{public}s:%i Error : Unexpected TLV: 0x%x
%{public}s:%i Error : unexpected length %d
%{public}s:%i Radio %s.
%{public}s:%i Ignoring file of type %d: %s
%{public}s:%i Warning: failed to validate boot measurements, skipping
%{public}s:%i Error: Failed to validate boot measurements
%{public}s:%i No RF for this device.
%{public}s:%i Currently running version 0x%04X, rev %d
%{public}s:%i Bundle is missing folder: fury-rf
%{public}s:%i RF not supported
%{public}s:%i Configuring NFCC to use GPIO %d as data IRQ
%{public}s:%i Wrote to file: %s
%{public}s:%i Failed to create NfRestoreSE object
%{public}s:%i Failed to load stack - retrying FW download
%{public}s:%i Failed to load stack after re-restore.
%{public}s:%i Using data from %s
%{public}s:%i \"%s\" errno=%d failed to stat parent: %s
%{public}s:%i Unknown encoding error
%{public}s:%i ----------------------- IOService plane --------------------------
%{public}s:%i Invalid boot-arg length: %zu
%{public}s:%i Unexpected ROM version %02x.%02x
%{public}s:%i Validating boot measurements
%{public}s:%i Failed to validate Boot measurements
%{public}s:%i Failed to get file name %s
%{public}s:%i Customer factory page is already locked with production content. Nothing to do.
%{public}s:%i Retry...
%{public}s:%i Failed to create CF property string
%{public}s:%i Failed to parse params
%{public}s:%i Failed to open driver
%{public}s:%i Driver already open. This is bad
%{public}s:%i Stack loaded after re-restore.
%{public}s:%i \"%s\" errno=%d parent is not directory: %s
%{public}s:%i Failed to delete existing file: %s
%{public}s:%i migration=%s pkgs=%d inst=%d
%{public}s:%i No external SPMIIRQ
%{public}s:%i Customer factory page is already locked with debug content. Nothing to do.
%{public}s:%i Failed find IOKit service
%{public}s:%i Failed to run script
%{public}s:%i Command failed: status=0x%04x
%{public}s:%i calloc failure...
%{public}s:%i %s has matching {%s / %s}
%{public}s:%i Failed to read boot-args: %d
%{public}s:%i Failed to parse bundle data
%{public}s:%i mode=%s counter=%d reference=%d osid=0x%02x othervalid=0x%02x
%{public}s:%i Failed to get iterator for service
%{public}s:%i Context already exists
%{public}s:%i Invalid hashes length
%{public}s:%i Running customer factory page update with %s
%{public}s:%i ATE Trim version is %x (%d)
%{public}s:%i Bundle is missing folder: rf
%{public}s:%i Failed to update RF settings.
%{public}s:%i Failed to configure NFCC to use GPIO %d as data IRQ : %d
%{public}s:%i Invalid hex string
%{public}s:%i Failed to create errorValue CFString
%{public}s:%i Found boot-arg \"%s\" = \"%s\"
%{public}s:%i Retrieving boot measurements
%{public}s:%i Failed to restore after load failure.
%{public}s:%i Malformed Customer page !
%{public}s:%i Failed to update customer factory page
%{public}s:%i Found matching unlock firmware: %s
%{public}s:%i Failed to get factory page : %d
%{public}s:%i Failed to get info.
%{public}s:%i Error : more than 1 TLV : %d
%{public}s:%i No radio key, skipping RF settings.
%{public}s:%i Error %d at %s
%{public}s:%i Could not find service with: %s, retrying slow path
%{public}s:%i Failed to get valid service
%{public}s:%i %s NOT found
%{public}s:%i EEPROM User Area Start:0x%08X End:0x%08X
%{public}s:%i Factory page E0 clear not supported on this hardware.
```
