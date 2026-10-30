# `/usr/bin/nvmefwupdater`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 108,448 bytes.

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
Bad Argument
phy_data
NVMe Updater: %s - Device tree property wasn't found\n
Samsung
<<Warning: Unknown value for k2DLithographyStrings>>
/usr/standalone/firmware/BFH/s3e-bfh-loader.bin
NVMe Updater Error [%s:%d]:PerformBFH: Failed to load any file data.\n
NVMe Updater Error [%s:%d]:IOConnectCallMethod failed\n
3d-v4
Turks
NVMe Updater: msp = %s phyText = %s phyData = %s\n
Production Update Required
NVMe Updater Error [%s:%d]:Failed to read in tunable table tunnel opcode dictionary at %s\n
set_pci_port_state
NVMe Updater: DriveConfig version : drive %d, update %d\n
S1X
slc
NVMe Updater: BFH params: imp-mohm=0x%x\n
NVMe Updater: Successfully updated FW...\n
NVMe Updater Error [%s:%d]:Failed to allocate %llu byte buffer to read stdin\n
NVMe Updater:     FTL Util FMT Min %d\n
thermal-throttling
[--query [<path-to-bfh-update>]] [--queryVendor] [--queryUpdate] [--queryBFHFile] [--validate <path-to-version-plist>] 
YMTC
NVMe Updater Error [%s:%d]:Version number from tunable table tunnel opcode dictionary at %s does not match expected value: %d != %d\n
NVMe Updater: Skipped firmware update successfully\n
NVMe Updater:     NANDDeviceID 0x%04x
NVMe Updater: Skipping FW Finalize\n
%s/%016llX.pak
NVMe Updater Error [%s:%d]:Failed getting storage device. Error=0x%x\n
NVMe Updater Error [%s:%d]:Unknown validation status %d!\n
NVMe Updater: Loaded %llu byte tunable table bundle from stdin\n
NVMe Updater Error [%s:%d]:Failed to read tunnel dictionary from tunable table tunnel opcode dictionary at %s\n
NVMe Updater: FTL_UtilVersion or DM_Version mismatch, skipping config\n
tlc
Invalid Update
NVMe Updater Error [%s:%d]:Value for property \"%s\" is data as expected, received CFTypeID = %lu\n
icc-20us-ma
NVMe Updater:     ECCVersionNANDRevision 0x%04x
PBPM.bin
NVMe Updater Error [%s:%d]:Unknown MSP type: 0x%x\n
t303
NVMe Updater Error [%s:%d]:Mismatch in property length. name=%s, required=%lu, found=%ld\n
NVMe Updater: Finalizing FW...\n
nvme: %s %X %s %s %s %s %d plane %dGB 
<<Warning: Unknown value for kChipIDStrings>>
NVMe Updater Error [%s:%d]:Failed setting BFH params.\n
IODeviceTree:/arm-io
NVMe Updater Error [%s:%d]:Failed to parse filename key at position %lu as a string from tunable table tunnel opcode dictionary at %s\n
set_nvme_state
chip-revision
NVMe Updater: Update config %d: S3%c, Rev %X\n
sendtunabletables
NVMe Updater Error [%s:%d]:%s UpdateMspBfhParams failed. status=0x%x\n
NVMe Updater: BFH params: icc-duration-idx=0x%x\n
NVMe Updater: FW Namepsace Mismatch found...\n
nand-dev-platform
NVMe Updater Error [%s:%d]:Failed getting NAND descriptor. Error=0x%x\n
imp-mohm
/usr/standalone/firmware/storagetunables/file_to_tunnel_dictionary.plist
FileVersion
NVMe Updater: Passthrough command done fNVMeStatus=0x%x fReturn=0x%x \n
queryVendor
msp-phy-fw-path
<<Warning: Unknown value for kVendorStrings>>
NVMe Updater Error [%s:%d]:BFHLoaderFile is NULL\n
NVMe Updater: BFH params: indirection-size=0x%x\n
NVMe Updater: NVMe status detail: %s\n
NVMe Updater: Activating FW...\n
NVMe Updater Error [%s:%d]:Failed to extract version number from tunable table tunnel opcode dictionary at %s\n
DM_Version   : %d\n
BiCS 4
5th Gen Lithography
NVMe Updater Error [%s:%d]:Mismatch in property length. name=%s, expected=%lu, found=%ld\n
IODeviceTree:/chosen
icc-duration-idx
NVMe Updater Error [%s:%d]:Failed to allocate tunnelDictKeys\n
NVMe Updater Error [%s:%d]:Failed to parse tunnel opcode value at position %lu as a number from tunable table tunnel opcode dictionary at %s\n
BDR_AF.bin
help
NVMe Updater Error [%s:%d]:XML Convertion failed !\n
NVMe Updater: %s UpdateMspBfhParams completed with status=0x%x\n
NVMe Updater: BFH params: phy tx eq=0x%x\n
NVMe Updater: BFH params: write-perf-mlc-mbps=0x%x\n
NVMe Updater: Checking for NAND development tunable bundle id property: %s\n
NVMe Updater Error [%s:%d]:Failed to open tunable table tunnel opcode dictionary at %s\n
NVMe Updater Error [%s:%d]:Failed to create string ref.\n
NVMe Updater Error [%s:%d]:%s: Failed allocating OFW BFH buffer.\n
disable-pcie-phy-override
NVMe Updater Error [%s:%d]:Failed to allocate %lu byte buffer to read tunable table bundle file property\n
NVMe Updater Error [%s:%d]:Encountered an error while reading tunable table bundle archive data\n
NVMe Updater Error [%s:%d]:illegal state: %s\n
NVMe Updater: Config version mismatch: drive %d, update %d\n
<<Warning: Unknown value for kDensityStrings>>
bdr-af
/usr/standalone/firmware/Turks/msp_fubfh_loader.bin
NVMe Updater Error [%s:%d]:Error Activating FW!\n
b
[--update <path-to-fw-update>] [--sendtunabletables [<path-to-table-bundle-file>] [--tunabledictionaryfile <path-to_dict-file>]] 
<<Warning: Unknown value for kChipDieStrings>>
FTL Rev      : %d.%d\n
3d-g3
Turks/msp_fubfh_loader.bin
S5E
queryBFHFile
power-budget-platform-modes
M9
perst-deassert
NVMe Updater Error [%s:%d]:PerformBFH failed. status=0x%x\n
tunable-table-bundle
NVMe Updater Error [%s:%d]:FirmwareValidate - Identify controller failed with return status 0x%X nvme status 0x%X.\n
c
NVMe Updater Error [%s:%d]:Failed to open tunable table bundle archive\n
NVMe Updater: Getting file from stdin\n
Only one option processed per invocation
<<Warning: Unknown value for k3DHynixLithographyStrings>>
S4E
icc-5us-ma
Invalid
NVMe Updater:     FTL Util FMT %d\n
NVMe Updater: HW mismatch, skipping config\n
IODeviceTree:/arm-io/apcie/pci-bridge0/s3e
NVMe Updater Error [%s:%d]:Unkown SOC Revision.\n
write-perf-tlc-mbps
FilenameToTunnelOpcode
<<Warning: Unknown value for kDimensionStrings>>
NVMe Updater: fw_length !. New fw_length = %d\n
NVMe Updater Error [%s:%d]:--tunabledictionaryfile option only valid with --sendtunabletables\n
NVMe Updater Error [%s:%d]:Failed getting MSP type. Error=0x%x\n
NVMe Updater Error [%s:%d]:Error opening file %s\n
NVMe Updater: BFH params: icc-5us-ma=0x%x\n
/usr/standalone/firmware/storagetunables/
NVMe Updater Error [%s:%d]:Failed to allocate %llu byte buffer to decompress tunable table\n
NVMe Updater Error [%s:%d]:Failed to create fileURL from path %s\n
NVMe Updater:     FTL Versions: CLog %d.%d, DM %d\n
NVMe Updater Error [%s:%d]:Failed to create stream from fileURL\n
NVMe Updater: Current config: S3%c, Rev %X\n
/usr/standalone/firmware/S4E/msp_fubfh_loader.bin
NVMe Updater Error [%s:%d]:No operation option specified.\n
NVMe Updater Error [%s:%d]:Not in BFH mode\n
NVMe Updater Error [%s:%d]:Both Phy Text and Phy Data files are required !.\n
NVMe Updater: Downloading FW...\n
NVMe Updater Error [%s:%d]:Failed to create CFString ref from path %s\n
[--bfh <path-to-bfh-update>] [--pci <state>] [--nvme <state>] [--identify] [--skip] [--help]
7th Gen Lithography
low-latency-profile
NVMe Updater Error [%s:%d]:perform_bfh failed. status=0x%x\n
NVMe Updater: BFH params: disable-pcie-phy-override=0x%x\n
NVMe Updater Error [%s:%d]:Error Finalizing FW!\n
NVMe Updater Error [%s:%d]:FirmwareValidate - file buffer is NULL. Nothing to validate.\n
NVMe Updater: SW FTL Major mismatch, erase install required\n
3d-v2
%s/%s/%s.text.bin
M9/msp_fubfh_loader.bin
NVMe Updater: BFH params: host soc platform=0x%x\n
vcc-mv
NVMe Updater: Sending %llu byte tunable table file %s to device with opcode %u\n
NVMe Updater Error [%s:%d]:%s\n
enable-skip
NVMe Updater: ECC version mismatch, skipping config\n
%s/%s/%s.data.bin
pci-phy-rx-eq
tunabledictionaryfile
nand_fw
Toshiba
NVMe Updater: NAND not supported, skipping config\n
%02X 
pmlc
nand
Hynix
NVMe Updater: BFH params: write-perf-tlc-mbps=0x%x\n
%s: 
%08X 
1z
t8310
NVMe Updater Error [%s:%d]:Could not stat %s\n
NVMe Updater: Ramdisk tunable table bundle file does not exist at %s\n
NVMe Updater Error [%s:%d]:SendTunableTableLegacyPath failed. status=0x%x\n
NVMe Updater: Blank NAND detected. Will skip Util, DM and FTL version checking\n
%s Die 
NVMe Updater Error [%s:%d]:Only one operation allowed.\n
NVMe Updater Error [%s:%d]:Failed setting S3E BFH params\n
NVMe Updater: %s: Did not find device tree property \"%s\"\n
NVMeUpdateLib.cpp
Sandisk
NVMe Updater: BFH params: icc-1us-ma=0x%x\n
NVMe Updater:     FTL Versions: CLog %d.%d, DM Min %d\n
General Error
NVMe Updater: Downloading Phy FW Data...\n
NVMe Updater Error [%s:%d]:Found a tunable table file of unknown type in the bundle: %s\n
AppleEmbeddedNVMeController
validate
skip
S3E
pci-phy-tx-eq
icc-ma
s4e-bfh-params
NVMe Updater Error [%s:%d]:Tunable table tunnel opcode dictionary at %s does not have expected root dictionary structure\n
NVMe Updater Error [%s:%d]:Failed to reallocate %llu byte buffer to read stdin\n
queryUpdate
NVMe Updater: Override BFH case\n
perform_ofw_bfh
NVMe Updater: Downloading Phy FW Text...\n
NVMe Updater: Loaded %llu byte tunable table bundle from ramdisk file (via EDT bundle property): %s:\n
NVMe Updater Error [%s:%d]:Failed to decompress tunable table from file %s\n
<<Warning: Unknown value for k3DLithographyStrings>>
ECCVersion   : %d\n
Tunable Table File Doesn't Exist
NVMe Updater: Did not find tunable table bundle file property\n
NVMe Updater Error [%s:%d]:Failed to load any data from tunable table bundle\n
t302
set_s5e_bfh_params
NVMe Updater: Checking for standard tunable bundle id property: %s\n
Retry Update
update
Usage: %s 
NVMe Updater Error [%s:%d]:Invalid MSP type %x\n
NVMe Updater Error [%s:%d]:Failed to parse version number from tunable table tunnel opcode dictionary at %s\n
UpdateMspBfhParams
nvmefwupdater.cpp
NVMe Updater: Non-override BFH case. BFH loader path: %s\n
NVMe Updater: Device tree entry not found. (%s)\n
NVMe Updater: returning %s\n
/usr/standalone/firmware/M9/msp_fubfh_loader.bin
NVMe Updater: Validating FW...\n
NVMe Updater: BFH params: icc-20us-ma=0x%x\n
NVMe Updater Error [%s:%d]:Tunnel opcode value at position %lu failed to parse into an integer from tunable table tunnel opcode dictionary at %s\n
1y
NVMe Updater Error [%s:%d]:Phy filename prop missing/empty from EDT on phy capable device !\n
S4E/msp_fubfh_loader.bin
NVMe Updater: Performing BFH OFW stage...\n
NVMe Updater Error [%s:%d]:Error downloading Phy FW! with sectionID = %d\n
Filename arguments can be replaced with '-' to read file in from stdin
bfh
q::fpovut::d:b:c:n:ihkm:r:s:
NVMe Updater: Found entry for tunable table filename %s in opcode dictionary file\n
nvme
NVMe Updater: Loaded %llu byte tunable table bundle from filepath: %s:\n
NVMe Updater Error [%s:%d]:Choices: %s %s %s\n
PTS Version  : %s\n
power-budget-active
IODeviceTree:/arm-io/ans
NVMe Updater Error [%s:%d]:Out of bounds BFH params buffer. type=%d length=%d offset=%d\n
tunable-table-bundle-nand-dev
NVMe Updater Error [%s:%d]:Failed to read tunable table bundle file property\n
NVMe Updater Error [%s:%d]:Choices: %s %s %s %s\n
pci
NVMe Updater Error [%s:%d]:Failed getting BFH status.\n
chip-id
NVMe Updater: FW Revision from update file : %d.%02d.%02d\n
NAND
phy_text
indirection-size
NVMe Updater: Num configurations in update file: %d\n
=======================
query
NVMe Updater Error [%s:%d]:Unrecognized option: %c\n
Invalid-FW-File.pak
NVMe Updater: Didn't find entry for tunable table filename %s in opcode dictionary file, falling back to hardcoded values\n
NVMe Updater: Sending %llu byte tunable table file %s to device\n
6th Gen Lithography
mlc
1D
TT.bin
perst-assert
NVMe Updater: BFH params: host soc revision=0x%x\n
NVMe Updater:     NANDDeviceID 0x%04x\n
NVMe Updater: Update found - erase install required\n
3d-v3
LowQD.bin
BFH/s3e-bfh-loader.bin
write-perf-mlc-mbps
NVMe Updater Error [%s:%d]:SendTunableTable failed. status=0x%x\n
3D
Dumping raw identify data:
NVMe Updater Error [%s:%d]:Error Checking FW!\n
NVMe Updater: %s UpdateMspBfhParams status = %X\n
msp-bfh-params
NVMe Updater: Asked to skip the firmware update \n
NVMe Updater:     ECCVersionNANDRevision 0x%04x\n
NVMe Updater: Update found - regular update\n
Success
Tunable File EDT Value Doesn't Exist
PB.bin
NVMe Updater Error [%s:%d]:Propertry max length exceeded. name=%s, max=%lu, found=%ld\n
NVMe Updater: BFH params: vcc-mv=0x%x\n
icc-1us-ma
NVMe Updater: Clog Mismatch found...\n
NVMe Updater Error [%s:%d]:Failed to parse tunnel dictionary from tunable table tunnel opcode dictionary at %s\n
phy
t8320
enable
disable
NVMe Updater: %s: result=%d\n
3d-g2
identify
3d-g1
NVMe Updater Error [%s:%d]:pread failed!\n
NVMe Updater Error [%s:%d]:Failed to allocate tunnelDictValues\n
NVMe Updater Error [%s:%d]:Failed to reset BFH GPIO.\n
FW Revision  : %s\n
NVMe Updater: Skipping FW activate\n
NVMe Updater Error [%s:%d]:Error downloading PhyFW with SectionID = %d, retry NAND update!\n
NVMe Updater Error [%s:%d]:Failed to read version number from tunable table tunnel opcode dictionary at %s\n
NVMe Updater Error [%s:%d]:PerformBFH: File name is NULL.  Aborting\n
S6E
Regular Update Required
Erase Update Required
Send Tunable Table Failed
NVMe Updater: BFH params: phy rx eq=0x%x\n
NVMe Updater Error [%s:%d]:Error Activating FW, retry NAND update!\n
1x
```
