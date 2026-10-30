# `/usr/bin/nvmefwupdater`

From the upgrade restore ramdisk (141-29011-104.dmg). 108,448 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 1976)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE
```

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libarchive.2.dylib (compatibility version 9.0.0, current version 9.2.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.nvmefwupdate.allow</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleNVMeUpdateUC</string>
</dict>
</plist>
```

## Strings (312)

```
ECCVersion   : %d\n
Tunable File EDT Value Doesn't Exist
NVMe Updater Error [%s:%d]:Unrecognized option: %c\n
NVMe Updater Error [%s:%d]:Failed getting NAND descriptor. Error=0x%x\n
NVMe Updater Error [%s:%d]:Could not stat %s\n
NVMe Updater: BFH params: indirection-size=0x%x\n
NVMe Updater Error [%s:%d]:Error Activating FW!\n
AppleEmbeddedNVMeController
NVMe Updater: SW FTL Major mismatch, erase install required\n
Tunable Table File Doesn't Exist
NVMe Updater: BFH params: phy tx eq=0x%x\n
%08X 
nand-dev-platform
NVMe Updater Error [%s:%d]:Failed to allocate %lu byte buffer to read tunable table bundle file property\n
NVMe Updater:     FTL Versions: CLog %d.%d, DM %d\n
tunable-table-bundle
NVMe Updater Error [%s:%d]:PerformBFH: Failed to load any file data.\n
%s Die 
Erase Update Required
thermal-throttling
NVMe Updater: BFH params: icc-duration-idx=0x%x\n
NVMe Updater Error [%s:%d]:Unknown validation status %d!\n
NVMe Updater: %s UpdateMspBfhParams completed with status=0x%x\n
NVMe Updater Error [%s:%d]:Invalid MSP type %x\n
NVMe Updater Error [%s:%d]:Failed to read tunable table bundle file property\n
NVMe Updater Error [%s:%d]:Tunable table tunnel opcode dictionary at %s does not have expected root dictionary structure\n
NVMeUpdateLib.cpp
5th Gen Lithography
mlc
help
[--update <path-to-fw-update>] [--sendtunabletables [<path-to-table-bundle-file>] [--tunabledictionaryfile <path-to_dict-file>]] 
chip-revision
NVMe Updater Error [%s:%d]:Unkown SOC Revision.\n
NVMe Updater: BFH params: icc-5us-ma=0x%x\n
%02X 
bdr-af
NVMe Updater: BFH params: vcc-mv=0x%x\n
S1X
enable
NVMe Updater: BFH params: write-perf-tlc-mbps=0x%x\n
NVMe Updater Error [%s:%d]:Version number from tunable table tunnel opcode dictionary at %s does not match expected value: %d != %d\n
NVMe Updater Error [%s:%d]:FirmwareValidate - Identify controller failed with return status 0x%X nvme status 0x%X.\n
NVMe Updater: Blank NAND detected. Will skip Util, DM and FTL version checking\n
Success
NVMe Updater: Device tree entry not found. (%s)\n
NVMe Updater Error [%s:%d]:Error downloading Phy FW! with sectionID = %d\n
NVMe Updater:     ECCVersionNANDRevision 0x%04x
<<Warning: Unknown value for k2DLithographyStrings>>
validate
msp-phy-fw-path
NVMe Updater: BFH params: host soc platform=0x%x\n
1D
power-budget-platform-modes
NVMe Updater Error [%s:%d]:%s: Failed allocating OFW BFH buffer.\n
FileVersion
NVMe Updater Error [%s:%d]:Failed to allocate %llu byte buffer to read stdin\n
NVMe Updater: Passthrough command done fNVMeStatus=0x%x fReturn=0x%x \n
7th Gen Lithography
power-budget-active
PB.bin
NVMe Updater Error [%s:%d]:Error Checking FW!\n
NVMe Updater Error [%s:%d]:Choices: %s %s %s\n
NVMe Updater:     FTL Versions: CLog %d.%d, DM Min %d\n
6th Gen Lithography
NVMe Updater: Getting file from stdin\n
NVMe Updater: Update config %d: S3%c, Rev %X\n
S5E
Hynix
NVMe Updater: Didn't find entry for tunable table filename %s in opcode dictionary file, falling back to hardcoded values\n
NVMe Updater Error [%s:%d]:Failed to allocate tunnelDictKeys\n
disable
NVMe Updater Error [%s:%d]:Choices: %s %s %s %s\n
PBPM.bin
icc-1us-ma
NVMe Updater: Found entry for tunable table filename %s in opcode dictionary file\n
set_nvme_state
3D
<<Warning: Unknown value for kVendorStrings>>
NVMe Updater Error [%s:%d]:Failed getting storage device. Error=0x%x\n
BFH/s3e-bfh-loader.bin
Turks/msp_fubfh_loader.bin
NVMe Updater: Successfully updated FW...\n
NVMe Updater Error [%s:%d]:Failed to read version number from tunable table tunnel opcode dictionary at %s\n
NVMe Updater:     NANDDeviceID 0x%04x\n
NVMe Updater: FTL_UtilVersion or DM_Version mismatch, skipping config\n
S4E
NVMe Updater Error [%s:%d]:SendTunableTableLegacyPath failed. status=0x%x\n
<<Warning: Unknown value for kDensityStrings>>
1y
NVMe Updater: BFH params: icc-1us-ma=0x%x\n
NVMe Updater: Ramdisk tunable table bundle file does not exist at %s\n
NVMe Updater Error [%s:%d]:Failed setting BFH params.\n
NVMe Updater: NVMe status detail: %s\n
NVMe Updater Error [%s:%d]:Tunnel opcode value at position %lu failed to parse into an integer from tunable table tunnel opcode dictionary at %s\n
/usr/standalone/firmware/BFH/s3e-bfh-loader.bin
NVMe Updater Error [%s:%d]:Value for property \"%s\" is data as expected, received CFTypeID = %lu\n
NVMe Updater: Loaded %llu byte tunable table bundle from stdin\n
NVMe Updater Error [%s:%d]:IOConnectCallMethod failed\n
General Error
S3E
vcc-mv
/usr/standalone/firmware/storagetunables/file_to_tunnel_dictionary.plist
NVMe Updater Error [%s:%d]:Failed to open tunable table tunnel opcode dictionary at %s\n
NVMe Updater: %s: result=%d\n
3d-v3
%s/%s/%s.text.bin
NVMe Updater Error [%s:%d]:BFHLoaderFile is NULL\n
NVMe Updater: Loaded %llu byte tunable table bundle from ramdisk file (via EDT bundle property): %s:\n
NVMe Updater:     NANDDeviceID 0x%04x
NVMe Updater:     FTL Util FMT Min %d\n
<<Warning: Unknown value for k3DLithographyStrings>>
Dumping raw identify data:
NVMe Updater Error [%s:%d]:Not in BFH mode\n
NVMe Updater Error [%s:%d]:illegal state: %s\n
NVMe Updater: NAND not supported, skipping config\n
<<Warning: Unknown value for kChipIDStrings>>
NVMe Updater: Skipping FW Finalize\n
pmlc
t302
pci-phy-rx-eq
/usr/standalone/firmware/storagetunables/
NVMe Updater Error [%s:%d]:PerformBFH: File name is NULL.  Aborting\n
NVMe Updater Error [%s:%d]:--tunabledictionaryfile option only valid with --sendtunabletables\n
NVMe Updater Error [%s:%d]:Failed to create CFString ref from path %s\n
Filename arguments can be replaced with '-' to read file in from stdin
NVMe Updater: DriveConfig version : drive %d, update %d\n
Bad Argument
/usr/standalone/firmware/M9/msp_fubfh_loader.bin
Turks
icc-duration-idx
NVMe Updater Error [%s:%d]:Encountered an error while reading tunable table bundle archive data\n
NVMe Updater: Non-override BFH case. BFH loader path: %s\n
NVMe Updater: Asked to skip the firmware update \n
NVMe Updater Error [%s:%d]:Failed getting MSP type. Error=0x%x\n
t8320
icc-5us-ma
Send Tunable Table Failed
nand
UpdateMspBfhParams
S6E
NVMe Updater Error [%s:%d]:Failed to reset BFH GPIO.\n
NVMe Updater Error [%s:%d]:Mismatch in property length. name=%s, required=%lu, found=%ld\n
perst-assert
IODeviceTree:/arm-io
tunable-table-bundle-nand-dev
NVMe Updater Error [%s:%d]:Found a tunable table file of unknown type in the bundle: %s\n
NVMe Updater Error [%s:%d]:Failed to extract version number from tunable table tunnel opcode dictionary at %s\n
NVMe Updater Error [%s:%d]:Failed to allocate tunnelDictValues\n
NAND
NVMe Updater Error [%s:%d]:XML Convertion failed !\n
NVMe Updater: returning %s\n
NVMe Updater: FW Revision from update file : %d.%02d.%02d\n
queryBFHFile
1z
3d-g2
/usr/standalone/firmware/Turks/msp_fubfh_loader.bin
Toshiba
NVMe Updater Error [%s:%d]:Both Phy Text and Phy Data files are required !.\n
NVMe Updater Error [%s:%d]:Failed to decompress tunable table from file %s\n
NVMe Updater Error [%s:%d]:Only one operation allowed.\n
NVMe Updater: ECC version mismatch, skipping config\n
nvme: %s %X %s %s %s %s %d plane %dGB 
=======================
/usr/standalone/firmware/S4E/msp_fubfh_loader.bin
Regular Update Required
tunabledictionaryfile
q::fpovut::d:b:c:n:ihkm:r:s:
%s/%016llX.pak
NVMe Updater Error [%s:%d]:Failed to open tunable table bundle archive\n
FW Revision  : %s\n
low-latency-profile
BDR_AF.bin
sendtunabletables
NVMe Updater Error [%s:%d]:%s UpdateMspBfhParams failed. status=0x%x\n
NVMe Updater Error [%s:%d]:%s\n
FilenameToTunnelOpcode
NVMe Updater Error [%s:%d]:FirmwareValidate - file buffer is NULL. Nothing to validate.\n
bfh
t303
S4E/msp_fubfh_loader.bin
NVMe Updater Error [%s:%d]:Failed setting S3E BFH params\n
NVMe Updater: Update found - regular update\n
3d-v2
Retry Update
query
NVMe Updater Error [%s:%d]:Out of bounds BFH params buffer. type=%d length=%d offset=%d\n
NVMe Updater: %s: Did not find device tree property \"%s\"\n
NVMe Updater Error [%s:%d]:Error downloading PhyFW with SectionID = %d, retry NAND update!\n
NVMe Updater Error [%s:%d]:Failed to parse tunnel dictionary from tunable table tunnel opcode dictionary at %s\n
NVMe Updater:     ECCVersionNANDRevision 0x%04x\n
BiCS 4
pci-phy-tx-eq
NVMe Updater: BFH params: host soc revision=0x%x\n
NVMe Updater: BFH params: disable-pcie-phy-override=0x%x\n
set_pci_port_state
NVMe Updater Error [%s:%d]:Failed getting BFH status.\n
NVMe Updater: BFH params: imp-mohm=0x%x\n
NVMe Updater Error [%s:%d]:Mismatch in property length. name=%s, expected=%lu, found=%ld\n
NVMe Updater: Config version mismatch: drive %d, update %d\n
Usage: %s 
NVMe Updater: msp = %s phyText = %s phyData = %s\n
NVMe Updater: Checking for NAND development tunable bundle id property: %s\n
NVMe Updater Error [%s:%d]:Error opening file %s\n
indirection-size
%s: 
NVMe Updater: FW Namepsace Mismatch found...\n
b
[--query [<path-to-bfh-update>]] [--queryVendor] [--queryUpdate] [--queryBFHFile] [--validate <path-to-version-plist>] 
NVMe Updater Error [%s:%d]:Failed to parse filename key at position %lu as a string from tunable table tunnel opcode dictionary at %s\n
1x
tlc
NVMe Updater: Performing BFH OFW stage...\n
NVMe Updater: Downloading Phy FW Data...\n
NVMe Updater Error [%s:%d]:Failed to allocate %llu byte buffer to decompress tunable table\n
NVMe Updater Error [%s:%d]:Failed to parse version number from tunable table tunnel opcode dictionary at %s\n
NVMe Updater:     FTL Util FMT %d\n
NVMe Updater: HW mismatch, skipping config\n
FTL Rev      : %d.%d\n
DM_Version   : %d\n
phy_data
t8310
NVMe Updater Error [%s:%d]:Error Finalizing FW!\n
NVMe Updater: Loaded %llu byte tunable table bundle from filepath: %s:\n
update
LowQD.bin
nvmefwupdater.cpp
%s/%s/%s.data.bin
NVMe Updater: Override BFH case\n
NVMe Updater Error [%s:%d]:pread failed!\n
disable-pcie-phy-override
NVMe Updater: Did not find tunable table bundle file property\n
NVMe Updater: Num configurations in update file: %d\n
NVMe Updater: Skipping FW activate\n
3d-g3
IODeviceTree:/arm-io/ans
NVMe Updater: Validating FW...\n
NVMe Updater: Checking for standard tunable bundle id property: %s\n
NVMe Updater Error [%s:%d]:Failed to create fileURL from path %s\n
PTS Version  : %s\n
NVMe Updater: fw_length !. New fw_length = %d\n
3d-v4
skip
phy_text
phy
icc-ma
msp-bfh-params
NVMe Updater: Finalizing FW...\n
NVMe Updater Error [%s:%d]:Error Activating FW, retry NAND update!\n
NVMe Updater Error [%s:%d]:perform_bfh failed. status=0x%x\n
Invalid
NVMe Updater Error [%s:%d]:Failed to load any data from tunable table bundle\n
NVMe Updater Error [%s:%d]:Failed to create stream from fileURL\n
NVMe Updater Error [%s:%d]:Failed to read in tunable table tunnel opcode dictionary at %s\n
NVMe Updater Error [%s:%d]:Failed to read tunnel dictionary from tunable table tunnel opcode dictionary at %s\n
queryUpdate
nand_fw
NVMe Updater Error [%s:%d]:PerformBFH failed. status=0x%x\n
NVMe Updater: BFH params: write-perf-mlc-mbps=0x%x\n
[--bfh <path-to-bfh-update>] [--pci <state>] [--nvme <state>] [--identify] [--skip] [--help]
NVMe Updater: Update found - erase install required\n
TT.bin
nvme
NVMe Updater: BFH params: phy rx eq=0x%x\n
Samsung
NVMe Updater: BFH params: icc-20us-ma=0x%x\n
NVMe Updater: Clog Mismatch found...\n
<<Warning: Unknown value for k3DHynixLithographyStrings>>
Invalid Update
Sandisk
IODeviceTree:/arm-io/apcie/pci-bridge0/s3e
c
NVMe Updater Error [%s:%d]:No operation option specified.\n
NVMe Updater Error [%s:%d]:Failed to create string ref.\n
perst-deassert
chip-id
s4e-bfh-params
NVMe Updater: Sending %llu byte tunable table file %s to device\n
NVMe Updater: Skipped firmware update successfully\n
identify
NVMe Updater Error [%s:%d]:Phy filename prop missing/empty from EDT on phy capable device !\n
YMTC
enable-skip
queryVendor
pci
Invalid-FW-File.pak
NVMe Updater Error [%s:%d]:Propertry max length exceeded. name=%s, max=%lu, found=%ld\n
imp-mohm
<<Warning: Unknown value for kDimensionStrings>>
NVMe Updater: %s UpdateMspBfhParams status = %X\n
IODeviceTree:/chosen
NVMe Updater: Activating FW...\n
NVMe Updater Error [%s:%d]:SendTunableTable failed. status=0x%x\n
Only one option processed per invocation
slc
M9
NVMe Updater: %s - Device tree property wasn't found\n
write-perf-mlc-mbps
write-perf-tlc-mbps
NVMe Updater: Downloading Phy FW Text...\n
NVMe Updater Error [%s:%d]:Failed to parse tunnel opcode value at position %lu as a number from tunable table tunnel opcode dictionary at %s\n
NVMe Updater Error [%s:%d]:Failed to reallocate %llu byte buffer to read stdin\n
<<Warning: Unknown value for kChipDieStrings>>
perform_ofw_bfh
icc-20us-ma
set_s5e_bfh_params
NVMe Updater: Sending %llu byte tunable table file %s to device with opcode %u\n
3d-g1
Production Update Required
NVMe Updater Error [%s:%d]:Unknown MSP type: 0x%x\n
M9/msp_fubfh_loader.bin
NVMe Updater: Downloading FW...\n
NVMe Updater: Current config: S3%c, Rev %X\n
```
