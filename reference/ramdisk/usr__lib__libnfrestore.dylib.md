# `/usr/lib/libnfrestore.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 183,728 bytes.

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
No FDR Key !\n
RestoreSystemPartition
%s:%i No data found for %s
%s:%i Running postflight: %s
%s/%s
%s:%i \"%s\" errno=%d failed to stat parent: %s
stockholm-spmi
SN200V B1
%s:%i Failed to create context
com.apple.nfrestore
FDR Key : %s\n
RootFilePath
InvokedFromCommandLine
SN300V_FW_B0_02_01_88_rev172757.bin
RestoreHammerfest
Unknown
%s:%i Incorrect bundle
%s:%i calloc failure...
%s:%i Failed at line %d: %s
%s
ReadyForImport
NFHardwareSkipSpmiReconfig
/dev/
hammerfest-spmi
%s:%i Failed to scan directory %u : %s
%s:%i mode=%s counter=%d reference=%d osid=0x%02x othervalid=0x%02x
IOPropertyMatch
_NFHardwarePrintNode
%s:%i Failed to create iterator
NfRestoreSEOpen_Internal
%s:%i **************** Restoring Hammerfest ****************
ClearE0Tag
_NFRestoreBootMeasurements
%s:%i Failed to get controller info..
%s:%i Locking factory page (%s)
_NfRestoreHasRadio
%s:%i se=%d, enabled=%d
SN100V B2
NFRestoreParseBootArgs
PN552_FW_02_01_6A_rev125914.bin
%s:%i ATE Trim version is %x (%d)
%s:%i Command failed: status=0x%04x
ExportFinished
IOService
NFHardwareInterfaceHasExternalSPMIIRQ
NfRestoreCopyUniqueFDRKey
%s:%i Failed to open driver
_NFRestore
%s:%i Failed to load stack - retrying FW download
SN450V_FW_A1_01_01_00A_rev14059249.bin
_NfRestoreCustomerFactoryPageMatches
%s:%i Failed to run script
%s:%i Unmatched interface %s
LockFactoryPage
NFRestoreNfcForController
%s:%i Failed to get info.
%02X_%02X_%02X
%s:%i Customer factory page is already locked with production content. Nothing to do.
> %s\n
%s:%i \"%s\" errno=%d parent is not directory: %s
skip-spmi-reconfig
%s:%i Assuming HW not present
PN800V_FW_A0_01_01_A8_rev164283.bin
%s:%i Failed to read index file
mask
%s:%i More than 1 file matching %02x_%02x_%02x
_NFRestoreJcop
_NfRestoreBundleGetFileHandle
%s:%i Failed to create CF property string
%s:%i Skipping Stockholm restore
NfcForceFwDl
%s:%i Nothing to do
%s:%i Erasing firmware flags.
nfcWithRadio
%s:%i \"%s\" errno=%d Failed to open %s
NfSecureElementSetPower
UNKNOWN
%s:%i No RF for this device.
SN200V_FURY_FW_B1_02_01_FA_rev149466.bin
%s:%i Retrieving boot measurements
%s:%i Bundle is missing folder: rf
debug
Idle
%s:%i Failed to lookup service : 0x%x
AppleStockholmControlUserClient
NfRestoreSETransceiveToOS
SN100V B0 / B1
rf
fixup
SN450V_FW_B0_
present
Update
%s:%i Failed to create property matching dictionary
NFRestoreNfcFirmwareNameForController
SN450V_FW_B1_03_01_015_rev48923467.bin
%s:%i No FDR Key !
com.apple.nfstack
kNfUpdateParamQueryFDRKey
NfRestoreRunIntegrityCheck
%s:%i Ignoring file of type %d: %s
%s:%i Invalid iterator
[Hex dump: length=%lu bytes] (%s:%i %s)
%s:%i Failed to read file: %s
SN450V_FW_B0_02_01_015_rev48936220.bin
Mismatched info hash
%s:%i Failed to parse index file as dictionary
%s:%i Failed to find file %s
_NFRestoreReadPlatformInfoFromFactoryPage
%s:%i Failed to allocate NfSecureElement_t
%s:%i Failed to shut down Hammerfest
=
NfcRFSettingsFile
fw
SN100V_FW_A3_01_01_C3_rev78599.bin
%s:%i Failed to query Boot measurements
%s:%i R-APDU does not match expected suffix!
AppleStockholmControl
%s:%i Provided buffer too small for result: %zu
%s:%i Failed to parse bundle data
%s:%i Failed to configure EDT settings : 0x%x
Mismatched scratch firmware hash
Customer factory page
SN100V_FW_A3_
stockholm
%s:%i 
%s:%i Middleware: %x.%x.%x.%x
%s:%i %s
SN100V_FW_A3_01_01_B6_rev157827.bin
_NFRestoreValidateBootMeasurements
%s:%i Writing factory page (E0:%s F0:%s 02:%s 03:%s 04:%s 05:%s 06:%s)
%s:%i Wrote to file: %s
%s:%i Failed find IOKit service %s
_NFHardwareIsEntryMatching
LogMW
%s:%i Failed %d
mobile
%s:%i Address Start:0x%08X End:0x%08X
PN552_FW_02_01_AF_59162.bin
%s:%i Malformed Customer page !
SN450V_FW_B1_
%s:%i Failed to create matching dictionary
%s:%i Failed to decode plist
absent
%s:%i Failed to update OS info
ImportInProgress
nfc,primary,gpio
com.apple.
NFHardwareInterfaceIsSupported
HammerfestOnly
%s:%i Failed to update customer factory page.
%s:%i Update LPCD settings failed; continue
%s:%i Currently running version 0x%04X, rev %d
%s:%i Failed to load plist
NFRestoreRFSettingsForController
_NFRestoreConfigureSPMIIRQ
%s:%i Factory page already has production content. Nothing to do.
%s:%i Failed to create NfRestoreSE object
StockholmOnly
CLIRestore
%s:%i Factory page E0 clear not supported on this hardware.
Mismatched scratch lifecycle hash
skip
StockholmOptions
w
JcopForceJCOPPostflightScript
%s:%i Bundle is missing RF settings - NFCC might fail RF operation
%s:%i Failed to update RF settings.
%s:%i Selected file %s
%s:%i ROM version %02x.%02x
%s:%i Unexpected ROM version %02x.%02x
%s:%i Running customer factory page update with %s
%s:%i Received: %s
AppleHammerfestControl
AppleStockholmSPMI
AppleHammerfestSPMI
%s:%i Failed to open SE
SN450V A0/A1
JcopPostflightScript
Mismatched protected firmware hash
%s:%i Failed to get factory page.
%s:%i Retry...
%s:%i Failed to enter wired mode
%s:%i Failed to parse params
%s:%i Failed to read boot-args: %d
value
%s:%i Failed to get factory page : %d
.
%s:%i Unknown encoding error
NfSecureElementClose
NfSecureElementUpdateOSInfo
%s:%i Failed to load driver
%s:%i Feature not supported
%s:%i Found boot-arg \"%s\" = \"%s\"
%s:%i Error: Failed to validate boot measurements
%s:%i Failed to reconfigure I/O : 0x%x
%s:%i Validating boot measurements
%02X.%02X.%02X
_NfRestoreCopyCustomerPageUpdateFirmware
LogNCI
LogAPDU
kern.bootargs
%s:%i Invalid boot-arg length: %zu
ignore
PN800V_FW_A1_
%02X_%02X_%03X
_NFRestoreDebugNFCCError
%s:%i Failed to shut down Stockholm
%s:%i Invalid format
%s:%i Failed to load stack after re-restore.
%s:%i Unexpected length mismatch : %zu vs %zu
%s:%i se object is not valid
%s:%i Failed to get OS info
%s:%i Failed to get iterator for service
%s:%i %s NOT found
 
_NFRestoreNfcFirmwareStep
%s:%i Found matching unlock firmware: %s
HammerfestFirmwareType
%s:%i Failed to write data to %s
JCOP
IOClass
%s:%i Transceive failed
%s:%i ==== CONTROLLER ====
Error at %s:%d
%s:%i FDR Key : %s
%s:%i No external SPMIIRQ
nfc,secondary,gpio
%s:%i %s has child %s
%s:%i %s has property %s : %s
%s:%i Failed to load stack
SN300V B21
%s:%i EEPROM User Area Start:0x%08X End:0x%08X
SN450V_FW_B0_02_01_814_rev46829584.bin
%02X.%02X.%03X
Current platform info from customer factory page is 
%s:%i Customer factory page is already locked with debug content. Nothing to do.
IONameMatched
SN300V B20
NfRestoreSEDumpControllerInfo
%s:%i Skipping Hammerfest restore.
SN300V_FW_B0_02_01_C9_rev170948.bin
%s:%i Unexpected Si version %02x.%02x
_NfRestoreStripHeaderFromPlatformInfoTLV
%s:%i Failed to find matching file for %02x_%02x_%02x (%@)
%s:%i Customer factory page is locked without production content !
%s:%i Context already exists
com.apple.nfjcop
se-spmi-irq
%s:%i Failed to load stack after RF settings. Bailing
_NFRestoreConfigureHWSettings
_NfRestoreRunAntennaSelfCheck
*
NfSecureElementOpen
%s:%i %s found
JcopTerminateApplets
SN200V_FW_B1_02_01_FA_rev124452.bin
PN800V_FW_A1_01_01_14_rev46806918.bin
%s:%i Failed to get file name %s
NfSecureElementScriptRun
%s:%i Error %d at %s
kNfUpdateAntennaSelfTest
NfcMaxFwDlRetries
DisableBootMeasurementEnforcement
SN200V_FW_B1_02_01_BA_rev170350.bin
_NfRestoreCustomerFactoryPageUpdate
%s:%i Encoding error: %s
%s:%i Failed to get valid service
NfRestoreSEEnumerate
%s:%i Failed at iteration %d
NFRestoreDictionaryCopyDataForKey
/usr/standalone/firmware/nfrestore/firmware/fury-fw-hashes/PN800V-hashes.plist
%s:%i Failed to check antenna : 0x%x
%s:%i Failed find IOKit service
_NfRestoreBundleReadDir
%s:%i Failed to delete existing file: %s
NFRestoreParseParams
%s:%i Failed to install %s
%s:%i Failed to update customer factory page
index.plist
.plist
NfSecureElementScriptRunLine
%s:%i ----------------------- IOService plane --------------------------
%s:%i Driver already open. This is bad
%s:%i Error : Invalid TLV: 0x%x
%s:%i migration=%s pkgs=%d inst=%d
SN450V B0/B1/B2
Stockholm
_NFHardwareFindMatchingService
IOMatchCategory
%s:%i Failed to get driver info
SE310S_FW_A0_01_01_41_rev172736.bin
%s:%i Skipping SPMIIRQ
%s:%i Failed to build target path: %s
/%s
reconfigure
FirmwareBundlePath
Dump: 
_NfRestoreBundleWrite
%s:%i Could not find service with: %s, retrying slow path
com.apple.spmi.nfc.hammerfest
%s:%i Iteration %d of %d
%s:%i Configuring NFCC to use GPIO %d as data IRQ
%s:%i Failed to write factory page : %d
%s:%i This is a SIP, NED or Dev, skipping antenna test
%s:%i \"%s\" errno=%d stat failed
PN800V_FW_A0_01_01_08_rev163891.bin
SimulateRestoreOS
_NFRestoreClearE0Tag
%s:%i Dumping EEPROM after failure
%s:%i Bundle is missing folder: %s
%s:%i Radio %s.
StockholmRestore.plist
%s:%i Unexpected state.
Hammerfest
%s:%i Failed to update FW: %s
%s:%i Customer factory page is locked without production content ! Skipping for older devices
IOUserClientClass
PN800V_FW_A1_01_01_B4_rev47094117.bin
%s:%i Failed to validate Boot measurements
_NFRestoreNfcRFStep
%s:%i Found exact plist match: %s
%s:%i R-APDU does not match expected prefix!
\r\n
ExportInProgress
%s:%i Failed to create errorValue CFString
nfrestore-loop
%s:%i Failed to install FW
SE310S_FW_A0_01_01_D3_rev165460.bin
_NFRestoreLoadStackAndRestoreOnFailure
prod
%s:%i Failed to get controller info
%s:%i Firmware: %x.%x rev %d
%s:%i Warning: failed to validate boot measurements, skipping
fury-fw-mfg
SN450V_FW_A1_01_01_80A_rev14497923.bin
SN200V_FW_B1_
SN300V_FW_B0_
AuxiliaryDevicePath
FactoryInstall
Mismatched protected lifecycle hash
_NFRestoreReadATETrimVersion
yes
Error 0x%04x at %s:%d
%s:%i \"%s\" errno=%d Failed to stat at %s
hammerfest
%s:%i Matched name %s, returned 0x%04x
_NFRestorePushError
%s:%i Chip version %02x.%02x.%02x
apply
%s:%i No matching files
%s:%i Executed %d lines successfully
NfRestoreBundleCreate
not reconfigure
com.apple.stockholm
DevicePath
kNfUpdateParamIntegrity
%s:%i %s driver already open - can't interrupt
%s:%i Failed to clear E0 tag : %d
SN200V_FURY_FW_B1_02_01_AE_rev170322.bin
%s:%i Unexpected NULL parameter
_NFRestoreRunPostFlight
NfRestoreReturnError
SN200V B0
PN600V
PN800V A0/A1
InvalidBStateSettingsPolicy
%s:%i TX LDO current is %d
%s:%i Invalid hex string
%s:%i Expected: %s
SN210V B1
%s:%i Failed to scan %s
Error 0x%04x at %s:%d: %llx %s
fury-fw
SN450V_FW_B1_03_01_815_rev49087064.bin
%s:%i Invalid hashes length
%s:%i Error : unexpected length %d
NULL
%s:%i **************** Restoring Stockholm ****************
true
1
%s:%i Failed to configure HW Settings: %d
%s\n
NfRestoreBundleScan
%s:%i snprintf error
_NfRestoreBundleValidateTargetPath
ForceVenReset
_NFRestoreShutdownNFCC
fw-mfg
%s:%i Failed to restore after load failure.
%s:%i Stack loaded after re-restore.
%s:%i Failed to configure NFCC to use GPIO %d as data IRQ : %d
%s:%i Customer factory page is locked
nfrestore: %s\n
SN300V B0
SN300V B1
NfRestoreInvalidateProhibitTimer
%s:%i Hardware: %x.%x (%s)
NO
???
%s:%i Error : Unexpected TLV: 0x%x
fw-unlock
%s:%i Using data from %s
%s:%i Error : more than 1 TLV : %d
ExportPreparation
NFHardwareSerialIsSupported
IONameMatch
PN80v ES2.1
NFCBootHashOverride
_NFRestoreGenericHardwareError
%s:%i Bundle is missing folder: fury-rf
%s:%i RF not supported
%s:%i id=%s dev=0x%02x hw=0x%08x fw=0x%04x cfw=0x%04x restricted=%s OSUpdate=%s
??
%s:%i Failed to disable boost
fury-rf
SN200V_FURY_FW_B1_
PN800V_FW_A0_
%s:%i Error : invalid length %d
%s:%i Failed to write to path: %s
%s:%i %s has no child
SE310S A0
NFRestoreNfc
%s:%i Warning : more than 1 TLV : %d
SN450V_FW_A1_
%s:%i No radio key, skipping RF settings.
%s:%i Failed to open %s
Manufacturing
%s:%i Will %s spmi for %s
YES
EEPROM User Area: 
%s:%i Using custom hashes
_NFRestoreWriteFactoryPage
_NFHardwareDumpIOKit
_NFHardwareLookInTree
%s:%i Found property %s : %s
Unknown PN80v
FirmwareBundleData
NfcUpdateFile
/usr/standalone/firmware/nfrestore/firmware/fw-hashes/SN450V-hashes.plist
%s:%i Failed to get OS mode
_NFHardwareWalkTree
%s:%i %s has matching {%s / %s}
%{public}s:%i **************** Restoring Hammerfest ****************
%{public}s:%i Failed to load stack after RF settings. Bailing
%{public}s:%i Failed to query Boot measurements
%{public}s:%i Failed to validate Boot measurements
%{public}s:%i Failed to get file name %s
%{public}s:%i Failed to write factory page : %d
%{public}s:%i Failed to reconfigure I/O : 0x%x
%{public}s:%i Invalid hashes length
%{public}s:%i Skipping SPMIIRQ
%{public}s:%i %s has matching {%s / %s}
%{public}s:%i Unmatched interface %s
%{public}s:%i Assuming HW not present
%{public}s:%i Failed to disable boost
%{public}s:%i Erasing firmware flags.
%{public}s:%i Failed to load stack - retrying FW download
%{public}s:%i Failed to get info.
%{public}s:%i Failed to get factory page.
%{public}s:%i Warning : more than 1 TLV : %d
%{public}s:%i Failed to configure HW Settings: %d
%{public}s:%i Transceive failed
%{public}s:%i Feature not supported
%{public}s:%i ROM version %02x.%02x
%{public}s:%i Validating boot measurements
%{public}s:%i Invalid hex string
%{public}s:%i R-APDU does not match expected suffix!
%{public}s:%i Command failed: status=0x%04x
%{public}s:%i se=%d, enabled=%d
%{public}s:%i Context already exists
%{public}s:%i Skipping Hammerfest restore.
%{public}s:%i Failed to restore after load failure.
%{public}s:%i Bundle is missing folder: rf
%{public}s:%i No external SPMIIRQ
%{public}s:%i Error : Invalid TLV: 0x%x
%{public}s:%i This is a SIP, NED or Dev, skipping antenna test
%{public}s:%i Failed to enter wired mode
%{public}s:%i Failed to create errorValue CFString
%{public}s:%i FDR Key : %s
%{public}s:%i Failed %d
%{public}s:%i Using custom hashes
%{public}s:%i Unexpected NULL parameter
%{public}s:%i Executed %d lines successfully
%{public}s:%i Wrote to file: %s
%{public}s:%i Failed to get OS mode
%{public}s:%i Failed to clear E0 tag : %d
%{public}s:%i Stack loaded after re-restore.
%{public}s:%i ATE Trim version is %x (%d)
%{public}s:%i Error : more than 1 TLV : %d
%{public}s:%i Failed to check antenna : 0x%x
%{public}s:%i Will %s spmi for %s
%{public}s:%i Found property %s : %s
%{public}s:%i Failed to parse params
%{public}s:%i Found boot-arg \"%s\" = \"%s\"
%{public}s:%i %s driver already open - can't interrupt
%{public}s:%i Factory page E0 clear not supported on this hardware.
%{public}s:%i Unexpected length mismatch : %zu vs %zu
%{public}s:%i \"%s\" errno=%d Failed to stat at %s
%{public}s:%i Unexpected Si version %02x.%02x
%{public}s:%i Retrieving boot measurements
%{public}s:%i Failed to load stack after re-restore.
%{public}s:%i Error : Unexpected TLV: 0x%x
%{public}s:%i Error : invalid length %d
%{public}s:%i Failed to create property matching dictionary
%{public}s:%i Failed to get controller info
%{public}s:%i Dumping EEPROM after failure
%{public}s:%i Failed to write to path: %s
%{public}s:%i Failed to create iterator
%{public}s:%i Configuring NFCC to use GPIO %d as data IRQ
%{public}s:%i Failed to create context
%{public}s:%i Currently running version 0x%04X, rev %d
%{public}s:%i Error : unexpected length %d
%{public}s:%i RF not supported
%{public}s:%i Failed to get factory page : %d
%{public}s:%i Locking factory page (%s)
%{public}s:%i Matched name %s, returned 0x%04x
%{public}s:%i Firmware: %x.%x rev %d
%{public}s:%i EEPROM User Area Start:0x%08X End:0x%08X
%{public}s:%i Found matching unlock firmware: %s
%{public}s:%i Failed to find matching file for %02x_%02x_%02x (%@)
%{public}s:%i calloc failure...
%{public}s:%i Failed to install FW
%{public}s:%i Bundle is missing RF settings - NFCC might fail RF operation
%{public}s:%i TX LDO current is %d
%{public}s:%i Failed to scan directory %u : %s
%{public}s:%i Failed to delete existing file: %s
%{public}s:%i Failed to shut down Stockholm
%{public}s:%i Failed to configure NFCC to use GPIO %d as data IRQ : %d
%{public}s:%i Customer factory page is already locked with production content. Nothing to do.
%{public}s:%i Customer factory page is locked without production content !
%{public}s:%i Radio %s.
%{public}s:%i Encoding error: %s
%{public}s:%i Failed to write data to %s
%{public}s:%i Failed to load driver
%{public}s:%i Failed to open SE
%{public}s:%i Failed at iteration %d
%{public}s:%i Failed to read boot-args: %d
%{public}s:%i Failed to open driver
%{public}s:%i Failed to load plist
%{public}s:%i Failed to shut down Hammerfest
%{public}s:%i Failed to install %s
%{public}s:%i Error %d at %s
%{public}s:%i \"%s\" errno=%d Failed to open %s
%{public}s:%i mode=%s counter=%d reference=%d osid=0x%02x othervalid=0x%02x
%{public}s:%i Middleware: %x.%x.%x.%x
%{public}s:%i Failed to scan %s
%{public}s:%i Chip version %02x.%02x.%02x
%{public}s:%i Running customer factory page update with %s
%{public}s:%i Using data from %s
%{public}s:%i Customer factory page is locked
%{public}s:%i Factory page already has production content. Nothing to do.
%{public}s:%i Writing factory page (E0:%s F0:%s 02:%s 03:%s 04:%s 05:%s 06:%s)
%{public}s:%i ==== CONTROLLER ====
%{public}s:%i Invalid boot-arg length: %zu
%{public}s:%i Failed to find file %s
%{public}s:%i Expected: %s
%{public}s:%i Received: %s
%{public}s:%i Failed at line %d: %s
%{public}s:%i se object is not valid
%{public}s:%i %s has property %s : %s
%{public}s:%i No FDR Key !
%{public}s:%i Customer factory page is locked without production content ! Skipping for older devices
%{public}s:%i Driver already open. This is bad
%{public}s:%i Incorrect bundle
%{public}s:%i Bundle is missing folder: fury-rf
%{public}s:%i No radio key, skipping RF settings.
%{public}s:%i 
%{public}s:%i Running postflight: %s
%{public}s:%i Ignoring file of type %d: %s
%{public}s:%i Failed to get iterator for service
%{public}s:%i Failed to read file: %s
%{public}s:%i No matching files
%{public}s:%i Failed to build target path: %s
%{public}s:%i Invalid iterator
%{public}s:%i No RF for this device.
%{public}s:%i Failed to parse index file as dictionary
[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)
%{public}s:%i Update LPCD settings failed; continue
%{public}s:%i Unexpected state.
%{public}s:%i Nothing to do
%{public}s:%i Malformed Customer page !
%{public}s:%i Failed to update customer factory page
%{public}s:%i \"%s\" errno=%d parent is not directory: %s
%{public}s:%i Unknown encoding error
%{public}s:%i Failed to get OS info
%{public}s:%i Iteration %d of %d
%{public}s:%i More than 1 file matching %02x_%02x_%02x
%{public}s:%i Failed to open %s
%{public}s:%i %s found
%{public}s:%i Hardware: %x.%x (%s)
%{public}s:%i **************** Restoring Stockholm ****************
%{public}s:%i Bundle is missing folder: %s
%{public}s:%i Unexpected ROM version %02x.%02x
%{public}s:%i Found exact plist match: %s
%{public}s:%i Failed to get controller info..
%{public}s:%i Customer factory page is already locked with debug content. Nothing to do.
%{public}s:%i Failed find IOKit service
%{public}s:%i %s
%{public}s:%i Address Start:0x%08X End:0x%08X
%{public}s:%i Failed to configure EDT settings : 0x%x
%{public}s:%i Invalid format
%{public}s:%i Retry...
%{public}s:%i Failed find IOKit service %s
%{public}s:%i Failed to get valid service
%{public}s:%i %s has no child
%{public}s:%i Failed to load stack
%{public}s:%i Failed to parse bundle data
%{public}s:%i Failed to update FW: %s
%{public}s:%i No data found for %s
%{public}s:%i Failed to create matching dictionary
%{public}s:%i %s NOT found
%{public}s:%i Failed to read index file
%{public}s:%i snprintf error
%{public}s:%i \"%s\" errno=%d failed to stat parent: %s
%{public}s:%i Failed to allocate NfSecureElement_t
%{public}s:%i Failed to update OS info
%{public}s:%i Could not find service with: %s, retrying slow path
%{public}s:%i ----------------------- IOService plane --------------------------
%{public}s:%i Provided buffer too small for result: %zu
%{public}s:%i Selected file %s
%{public}s:%i Failed to create CF property string
%{public}s:%i Failed to get driver info
%{public}s:%i Warning: failed to validate boot measurements, skipping
%{public}s:%i Failed to decode plist
%{public}s:%i Failed to update RF settings.
%{public}s:%i \"%s\" errno=%d stat failed
%{public}s:%i id=%s dev=0x%02x hw=0x%08x fw=0x%04x cfw=0x%04x restricted=%s OSUpdate=%s
%{public}s:%i Failed to lookup service : 0x%x
%{public}s:%i Failed to create NfRestoreSE object
%{public}s:%i Skipping Stockholm restore
%{public}s:%i Error: Failed to validate boot measurements
%{public}s:%i Failed to update customer factory page.
%{public}s:%i Failed to run script
%{public}s:%i R-APDU does not match expected prefix!
%{public}s:%i migration=%s pkgs=%d inst=%d
%{public}s:%i %s has child %s
```
