# `/usr/lib/libauthinstall.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,912,368 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 37 (Size: 5408)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe
```

## Linked libraries (19)

- `/usr/lib/libauthinstall.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/updaters/libAppleTconUARPUpdater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/updaters/libT200Updater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (69 classes, 5 protocols)

Classes: `AMAuthInstallOSSsoAuthenticator`, `Ace3RestoreInfoFirmwareCopierOS`, `Ace3SoCRestoreInfoFirmwareCopierOS`, `Ace3SoCRestoreInfoHelperOS`, `AppleTypeCRetimerFirmwareAggregateRequestCreatorOS`, `AppleTypeCRetimerFirmwareCopierOS`, `AppleTypeCRetimerFirmwareRequestCreatorOS`, `AppleTypeCRetimerRestoreInfoHelperOS`, `FTABFileOS`, `FTABSubfileOS`, `MRUHardwareInfo`, `MRULogHelper`, `MRUPersonalizationInfo`, `MRUPersonalizedFirmware`, `MantaFTABFile`, `MantaFTABSubfile`, `NSData`, `NSError`, `NSFileHandle`, `NSMutableData`, `UARPAssetTagOS`, `UARPAssetVersionOS`, `UARPMetaDataTLV16OS`, `UARPMetaDataTLV32OS`, `UARPMetaDataTLV64OS`, `UARPMetaDataTLV8OS`, `UARPMetaDataTLVDataOS`, `UARPMetaDataTLVOS`, `UARPMetaDataTLVStringOS`, `UARPSuperBinaryOS`, `UARPSuperBinaryPayloadOS`, `UARPTLVHostPersonalizationRequiredOS`, `UARPTLVPersonalizationBoardIDOS`, `UARPTLVPersonalizationChipEpochOS`, `UARPTLVPersonalizationChipIDOS`, `UARPTLVPersonalizationChipRevisionOS`, `UARPTLVPersonalizationECIDDataOS`, `UARPTLVPersonalizationECIDOS`, `UARPTLVPersonalizationEnableMixMatchOS`, `UARPTLVPersonalizationFTABPayloadOS`, `UARPTLVPersonalizationFTABSubfileDigestFilenameOS`, `UARPTLVPersonalizationFTABSubfileDigestOS`, `UARPTLVPersonalizationFTABSubfileEPROOS`, `UARPTLVPersonalizationFTABSubfileESECOS`, `UARPTLVPersonalizationFTABSubfileHashAlgorithmOS`, `UARPTLVPersonalizationFTABSubfileLongnameOS`, `UARPTLVPersonalizationFTABSubfileTagOS`, `UARPTLVPersonalizationFTABSubfileTrustedOS`, `UARPTLVPersonalizationLifeOS`, `UARPTLVPersonalizationLogicalUnitNumberOS`, `UARPTLVPersonalizationManifestEpochOS`, `UARPTLVPersonalizationManifestPrefixOS`, `UARPTLVPersonalizationManifestSuffixOS`, `UARPTLVPersonalizationNonceHashOS`, `UARPTLVPersonalizationNonceOS`, `UARPTLVPersonalizationPayloadTagOS`, `UARPTLVPersonalizationPrefixNeedsLogicalUnitNumberOS`, `UARPTLVPersonalizationProductionModeOS`, `UARPTLVPersonalizationProvisioningOS`, `UARPTLVPersonalizationRequiredOS`, `UARPTLVPersonalizationSecurityDomainOS`, `UARPTLVPersonalizationSecurityModeOS`, `UARPTLVPersonalizationSoCLiveNonceOS`, `UARPTLVPersonalizationSuffixNeedsLogicalUnitNumberOS`, `UARPTLVPersonalizationSuperBinaryAssetIDOS`, `UARPTLVPersonalizationSuperBinaryPayloadIndexOS`, `UARPTLVPersonalizationTicketNeedsLogicalUnitNumberOS`, `UARPTLVPersonalizedManifestOS`, `UARPTLVRequiredPersonalizationOptionOS`

Protocols: `ASAuthorizationControllerDelegate`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`

## Strings (6,129)

First 2,500 of 6,129.
```
%s::%s: failed to copy options\n
%s::%s: failed to create request dict\n
%s::%s: failed to remove rooted fw personalized bits\n
%s::%s: failed to create path url\n
%s::%s: Looks like there is no error present; Nothing to be done here.\n
%s::%s: failed to init logging\n
%s::%s: failed to acquire firmware data from file path\n
%s::%s: Missing = for key: %s\n
%s::%s: failed to init firmware\n
%s::%s: unable to allocate data\n
%s::%s: destination path does not exist after creation attempt (status: %d)\n
%s::%s: failed to convert from string to number\n
%s::%s: failed to update file\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: failed to init data container object\n
%s::%s: padding %ld byte(s) at the end of ftab\n
%s::%s: failed to create ftab file path\n
%s::%s: Failed to build vinyl info.plist dictionary\n
%s::%s: no firmware override specified\n
%s::%s: copyFirmware: failed to create personalized FW URL (status: %d)\n
%s::%s: Failed to parse debugArgs\n
%s::%s: failed to acquire cf data byte pointer\n
%s::%s: cannot save data using optimized flow\n
%s::%s: certPlusLdrVer memory alloc failed\n
%s::%s: AMSupportDigestSha256 failed:\n
%s::%s: file i/o error (code: %d)\n
%s::%s: no device info\n
%s::%s: mainInfoPlistData not present in the input\n
%s::%s: invalid length value\n
%s::%s: firmware data container is invalid\n
UARP: Failed personalization response, error = %u
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: Missing firmwareMac in info.plist -- firmware too old\n
%s::%s: tag '%s' not found in build identity, skipping validation\n
%s::%s: header is bigger than the file\n
%s::%s: no boot nonce in device info or firmware\n
%s::%s: goldInfoPlistData not present in the input\n
%s::%s: failed to add certId\n
%s::%s: failed to acquire file path string\n
%s::%s: Chip major revision seems unreasonable: %d\n
%s::%s: file is empty (file size: %zu)\n
%s::%s: failed to init bundle firmware\n
%s::%s: failed to create options cp\n
%s::%s: running host invoked restore info -- using bundleURL\n
%s::%s: function is not supported in memory optimized flow. Memory optimized files are read only\n
%s::%s: file name not specified\n
%s::%s: failed to allocate space for file object\n
%s::%s: failed to allocate internal data structure\n
%s::%s: failed to convert from number to data\n
%s::%s: failed to create fullURL\n
%s::%s: reducing requested length %zu -> %zu\n
%s::%s: failed to aquire ftab file header\n
%s::%s: failed to create directory to save firmware (status: %d)\n
UARP: TSS Request to server %{public}@ with options %{public}@
Failed to write FTAB header
Failed to write manifest
%s::%s: failed to obtain file stats: (%s)\n
%s::%s: updater failed to find firmware data with bundleData\n
%s::%s: failed to create destination path URL (status: %d)\n
%s::%s: failed to open bbfw archive for reading\n
%s::%s: invalid type for %s\n
%s::%s: Regular bbticket flow\n
%s::%s: failed to get device info list\n
%s::%s: failed to build parameters out of device identity\n
%s::%s: startOfManifestUnaligned: %ld, startOfManifestAligned: %ld, paddingBeforeManifestStart: %u\n
%s::%s: file is smaller than the ftab header size\n
%s::%s: failed to get measurements\n
%s::%s: allowing unsealed FDR data\n
%s::%s: no manifest input provided\n
%s::%s: file data provided is not valid\n
%s::%s: =========== FTAB Header ===========\n
%s::%s: wrong chip rev size\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: failed to get deviceInfoDict\n
%s::%s: attempting copyFirmwareUpdater again with source bundle file map\n
%s::%s: copying preflighted bundle firmware into the dst bundle...\n
%s::%s: failed to get byte pointer\n
%s::%s: failed to acquire ftab file header\n
%s::%s: no firmware file provided\n
%s::%s: Get FW Data from Zip failed\n
%s::%s: error getting properlylist\n
%s::%s: Failed to alloc memory for filename\n
%s::%s: invalid type for rtkitos\n
%s::%s: failed to initialize cache\n
%s::%s: manifest at the end - startOfManifest: %u, endOfFiles: %u, padding: %u\n
%s::%s: Invalid token: %s\n
%s::%s: Count of certID != hashVad \n
%s::%s: unmaping new length for page alignment (alignedLength: %zu. originalLength: %zu)\n
%s::%s: failed to allocate data for personalized path\n
%s::%s: Using FDR trust object hash in updater options override\n
%s::%s: destination bundle was not specified, so we are skipping the copy step...\n
%s::%s: CFData to CFBoolean conversion failure\n
%s::%s: tag is either larger or smaller than limit %u (size: %lu)\n
%s::%s: missing required file %s\n
%s::%s: firmwareFileDictionary is null\n
%s::%s: no read or write permissions to file: (%s)\n
%s::%s: rkos digest is of an unexpected type\n
%s::%s: context passed is null\n
%s::%s: cowardly retreating because tag '%s' exists in runtime MMIO File Data. I refuse to overwrite existing files!\n
%s::%s: failed to get dict entry rkos digest\n
%s::%s: setting gid3En for rtkitos\n
%s::%s: cannot aquire reference for a memory optimized data container. Please use copyData() instead\n
%s::%s: failed to create manifest\n
%s::%s: No manifest provided with firmware. Manifest is required!\n
%s::%s: failed to get firmware data\n
%s::%s: setting gid3En for iboot\n
%s::%s: failed to acquire file path c string\n
%s::%s: failed to get build identity dict from options\n
%s::%s: manifestOffset: %u, manifestSize: %u\n
%s::%s: endOfManifestUnaligned: %ld, endOfManifestAligned: %ld, paddingAfterManifestEnd: %u\n
%s::%s: skipping device identity validation against build identity\n
%s::%s: failed to create build ID key path\n
UARP: Failed to initialize sso
%s::%s: Failed to alloc create fwFilePath CFString\n
%s::%s: failed to add top-level sequence\n
%s::%s: failed to create manifest data output\n
%s::%s: cannot update tag '%s' because it does not exist\n
%s::%s: Bad parameter\n
UARP: Failed to create authinstall reference
Unable to open file for writing at %@ (%@)
%s::%s: getting tags\n
%s::%s: failed to read zip file\n
%s::%s: Baseband Firmware override has wrong type %lu\n
%s::%s: converting from data to number\n
%s::%s: BasebandUpdater Version: %s\n
%s::%s: initialization failure due to incomplete parameters\n
%s::%s: failed to find FW (%s) in build ID in personalized path\n
%s::%s: removing any personalized bits of bundle firmware\n
%s::%s: tag '%s' not found in tss-request map, skipping validation\n
%s::%s: manifest data has no bytes\n
%s::%s: Generation: %u, Valid: %u, BootNonce: 0x%08llx\n
%s::%s: Chip minor revision seems unreasonable: %d\n
UARP: TSS request to signing server %{public}@
%s::%s: read less bytes than required (read: %zu, required: %zu)\n
%s::%s: vinylgetFwData srcPath %s:\n
%s::%s: file data was invalid\n
%s::%s: cache is invalid\n
%s: File too short
%s::%s: no chip rev\n
%s::%s: cannot update a file if no files exist\n
%s::%s: VinylUpdater Version: %s\n
%s::%s: invalid error parameter passed\n
%s::%s: Failed to allocate output dictionary\n
%s::%s: Invalid FDR trust object hash in updater options override\n
Failed to open file handle for writing to '%@'
%s::%s: firmware already has a boot nonce\n
%s::%s: failed to create CFString\n
%s::%s: Failed to get Vinyl Firmware Data\n
%s::%s: cache does not hold correct offset for file %s. Cache offset: %d. FTAB offset: %d. Cache is invalid\n
%s::%s: paging in new length for page alignment (Requested: %zu. Aligned: %zu)\n
%s::%s: Requesting FDR trust object hash\n
%s::%s: attempting to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: Identified chip as R1\n
%s::%s: failed to create dirPath\n
%s::%s: ftab cache had entries before ftab container was initialized. Clearing cache before moving on.\n
%s::%s: No manifest present\n
%s::%s: failed to get fwData\n
%s::%s: object does not hold any data\n
%s::%s: production mode not present in device info. This is fatal!\n
%s::%s: Manifest is not available\n
%s::%s: Identified chip as R2\n
%s::%s: fwMacData is wrong type\n
%s::%s: Let's check if we need to take the regular bbticket vs prov flow\n
%s::%s: copyFirmware: failed to create src rooted FW URL\n
%s::%s: could not create URL to file\n
UARP: TSS Request failed customer path / auth listed
%s::%s: firmware file dictionary not provided\n
%s::%s: failed to update file data\n
%s::%s: too many files specified or there are no files. Limit is %d. Num Files: %d\n
%s::%s: Token: %s\n
%s::%s: Failed to find firmware in restore options\n
%s::%s: Failed to write some or all of data\n
Unable to locate subfile with tag '%@'
%s::%s: fwFileName %s\n
%s::%s: manifest existing in FTAB is being deleted\n
%s::%s: =========== FTAB Payloads ===========\n
%s::%s: Wrote %zu of %zu bytes to %s\n
%s::%s: RoseUpdater Version: %s\n
%s
%s::%s: failed to create Baseband Firmware override key path (read)\n
%s::%s: invalid file descriptor\n
%s::%s: copyFirmware: failed to create default FW URL, (status: %d)\n
%s::%s: failed to retain file data\n
%s::%s: failed to initialize file cache\n
%s::%s: Empty options dict\n
%s::%s: Fw data dictionary not present in the input\n
%s::%s: failed to allocate output dictionary\n
%s::%s: boardID is not 2 bytes in length. Assuming Rose-SE pairing is not supported.\n
%s::%s: failed to encode img4/vad sequence\n
%s::%s: failed to create output request dictionary\n
%s::%s: updater failed to find firmware data with bundleURL\n
%s::%s: Manifest Offset: %u, Manifest Length: %u, Magic: %s\n
%s::%s: failed obtain file size\n
%s::%s: Empty DebugArgs\n
%s::%s: removing file from FTAB cache. File: %s\n
%s::%s: boot nonce has wrong type\n
%s::%s: failed to get manifest, error: %d\n
%s::%s: failed to save file (%d)\n
%s::%s: failed to get file system reprensetation\n
UARP: Failed to set signing server
%s::%s: savePath for FW not specified. This needs to be specified.\n
%s::%s: rooted override data unavailable\n
%s::%s: esec data to boolean conversion failure\n
%s::%s: failed to create directory @ dstPathURL (status: %d)\n
%s::%s: bad device info parameters\n
%s::%s: Tag %s doesn't exist -- continue...\n
%s::%s: incorrect device info type\n
%s::%s: failed to create CFError object\n
%s::%s: Boot nonce set for FTAB. Boot nonce value: %llu\n
%s::%s: SHA384 failed\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: Extracting the Zip payload\n
%s::%s: failed to create file data\n
%s::%s: Failed to set ftab validity\n
%s: Unexpected header magic (%02x %02x %02x %02x %02x %02x %02x %02x)
%s::%s: using global signing with no firmware data available\n
%s::%s: SM::Recovery -- normal? %d macMatchRequired %d\n
%s::%s: failed to add certId-VAD sequence\n
%s::%s: desired type %s, received type %s\n
%s::%s: firmware file failed to initialize\n
Failed to write '%@'
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: sbd1 digest is of an unexpected type\n
%s::%s: Could not obtain deviceInfo dictionary. Sharing all digest information.\n
%s::%s: firmwareLoaderVersion is not a CFData type\n
%s::%s: Possibly OTA flow, fwData is already unziped and extracted, copy directly\n
%{public}s
%s::%s: no file data?!\n
%s::%s: specified tag name is invalid! Tag name: %s\n
%s::%s: No device info\n
%s::%s: copyFirmware: failed to find FW (%s) in build ID\n
%s::%s: function does not support memory optimization flow\n
%s::%s: firmware data is invalid and does not meet ftab standards\n
%s::%s: failed to initialize base class\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: failed to encode DER buffer\n
%s::%s: bad parameters\n
%s::%s: failed to copy firmware\n
%s::%s: creating request\n
%s::%s: invalid params passed\n
%s::%s: failed to get ldrVer\n
%s::%s: Failed to get DebugArgs buffer\n
%s::%s: CentauriUpdater Version: %s\n
%s::%s: Rose-SE pairing is supported for this device\n
%s::%s: failed to build parameters out of build identity\n
%s::%s: Populating underlying error\n
%s::%s: failed to copy ftab file header\n
%s::%s: no manifest preset in dataref\n
%s::%s: failed to obtain reference of data from data container\n
%s::%s: failed to get file stats\n
%s::%s: chipID is empty or isn't data type\n
%s::%s: failed to get mainNonce\n
%s::%s: failed to create personalized rooted FW URL (status: %d)\n
%s::%s: tag '%s' not found in device info, skipping validation\n
%s::%s: no dataref\n
%s::%s: no firmware in restore options\n
%s::%s: ldrVers count is zero\n
%s::%s: failed to allocate bundle firmware path dictionary (type: %hhu)\n
%s::%s: file data has no bytes\n
%s::%s: wrong chip rev type\n
%s::%s: Failed conversion: %s\n
%s::%s: no conversion necessary\n
%s::%s: Failed to measure firmware\n
%s::%s: failed to create number\n
%s::%s: invalid offset value\n
%s::%s: Manifest digest\n
%s::%s: rrko bundle data unavailable\n
%s::%s: =========== FTAB Header ===========\n\n
%s::%s: failed to validate device identity tags\n
%s::%s: Recovery Fw is not available\n
%s::%s: digestRef memory alloc failed\n
%s::%s: invalid type for buildidentity\n
%s::%s: failed to create data container\n
%s::%s: leaving: VinylRestoreInfo: %s\n
%s::%s: file path has not been initialized\n
%s::%s: failed to create copy of file path\n
%s::%s: optional tag %s missing from build identity, skipping\n
%s::%s: boot nonce has wrong size\n
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: security mode demotion disallowed for Baseband\n
%s::%s: failed to un-map file: (%s)\n
%s::%s: header only validation unsupported with optimized data\n
%s::%s: VinylUpdaterCreateRequest  ACFUInitLog returning %d\n
%s::%s: fullPath is null\n
%s::%s: path has wrong type %lu\n
UARP: Failed to enable sso
%s::%s: performing Rose pairing operation -- sharing digest dictionary\n
%s::%s: data is of an unsupported type\n
%s::%s: something went wrong, extra bytes in file\n
%s::%s: Invalid or no firmware file present in restore options\n
%s::%s: Num Files: %u\n
%s::%s: Missing required firmware measurements\n
%s::%s: cannot setData for a memory optimized data container.\n
%s::%s: failed to open file (%s)\n
Unable to delete file at %@
%s::%s: No chip ID\n
%s::%s: failed to extract bbfw item fileData is NULL\n
%s::%s: Create FwData copy failed\n
%s::%s: null device info\n
%s::%s: failed to obtain copy of manifest\n
UARP: TSS Request to server %{public}@ with SSO and options %{public}@
%s::%s: failed to get goldNonce\n
%s::%s: failed to create response tag list\n
%s::%s: Failed to create CF number from int value\n
%s::%s: invalid FTAB file\n
%s::%s: Get FW source path failed\n
%s::%s: rtkitos bundle data unavailable\n
%s::%s: Key: %s not found while parsing debugArgs, but this is not error\n
%s::%s: file indicated is within header space\n
%s::%s: Failed to set manifest\n
%s::%s: failed to create build ID key path for sdb1\n
%s::%s: failed to open bbfw archive for reading eUICCFwReaderOpen\n
%s::%s: %s\n%@
%s::%s: paddingAfterManifestEnd %u bytes\n
%s::%s: Payload is out of valid range\n
%s::%s: file not open\n
%s::%s: SHA256 failed\n
%s::%s: no file name specified\n
%s::%s: Invalid Type of Updater Options dict\n
%s::%s: failed to create mutable data in unoptimized path\n
%s::%s: could not allocate data\n
%s::%s: failed to init certification firmware\n
%s::%s: boardID is empty or isn't data type\n
%s::%s: running device invoked restore info -- using bundleData\n
%s::%s: failed to copy data to dstPathURL (status: %d)\n
%s::%s: Object initialized!\n
%s: Unable to open file at %@ (%@)
%s::%s: failed to create Baseband Firmware override key path (write)\n
%s::%s: ACFU Version: %s\n
%s::%s: failed to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
%s::%s: manifest present in space allocated for header\n
%s::%s: failed to create mutable data\n
%s::%s: Bad chip ID size\n
%s::%s: Failed to allocate shared info dictionary\n
%s::%s: certIdentifier is not a CFData type\n
%s::%s: reset epro to false for all firmware file tags\n
%s::%s: failed to update manifest\n
%s::%s: Bad options\n
%s::%s: failed to get create firmwareInfoDict\n
%s::%s: failed stiching img4 and vad\n
%s::%s: failed to create tag list from vector\n
UARP: %{public}@
%s::%s: copying firmware\n
%s::%s: offset out of range\n
%s::%s: failed due to incompatible bundle data dictionary\n
%s::%s: fFirmwareFile has not been initialized.\n
%s::%s: setFwInfo failed delete vinylFirmware object\n
%s::%s: Didn't find a matching embedded ftab\n
%s::%s: failed to create url from string\n
%s::%s: failed to copy file data\n
%s::%s: file does not exist\n
%s::%s: failed to obtain file data\n
%s: Error parsing file offset list (offset=%u, length=%lu)
%s::%s: failed to create domain\n
%s::%s: nonce is of unexpected size\n
%s::%s: failed to initialize object\n
%s::%s: Modifying request for non-persistent demotion\n
%s::%s: Found updater options in dictionary\n
%s::%s: cowardly retreating because tag '%s' exists. I refuse to overwrite existing files!\n
%s::%s: goldFwData not present in the input\n
%s::%s: failed to extract bbfw item status %d\n
%s::%s: failed to open file error: (%s)\n
%s::%s: Tag: %s :: Offset: 0x%04x Raw address: 0x%lx, size: %u\n
Unable to create file at %@
%s::%s: failed to create capabilities object\n
%s::%s: failed to unmap file: (%s)\n
%s::%s: payload is out of valid range\n
%s::%s: failed to create full description for type ID %lu\n
%s::%s: failed to remove file (%u)\n
%s::%s: Applying FDR trust object hash override\n
%s::%s: failed to get string\n
%s::%s: failed to create firmware\n
%s::%s: rkos bundle data unavailable\n
%s::%s: could not create output data\n
%s::%s: Unexpected value: %u for Key: %s\n
%s::%s: goldFwMac is not a CFData type\n
%s::%s: ldrVerComponents count is not expected\n
%s::%s: Found PairedWithNewerGenBaseband key in options: %{bool}d\n
%s::%s: failed to determine file size for path '%s' (%s)\n
%s::%s: failed to open file\n
%s::%s: failed to obtain data ref\n
%s::%s: entering: %s\n
%s::%s: failed to create im4p\n
%s::%s: Assuming updater options dictionary is being passed\n
UARP: TSS Request passed customer path / auth listed
%s::%s: unexpected device info parameters\n
%s::%s: fwldrver is null\n
%s::%s: enable gid3En for iboot\n
%s::%s: failed to perform destination bundle copy of rooted firmware\n
%s::%s: unsupported conversion: desired type %s, received type %s\n
%s::%s: no data to log\n
%s: Manifest parameters are invalid
%s::%s: mainFwMac is not a CFData type\n
%s::%s: ldrVersStrArray count is zero\n
%s::%s: no digest in build ID (%s)\n
%s::%s: failed to initialize base object\n
%s: Subfile offset error (offset=%u, length=%u)
%s::%s: Get InfoPlist Data from Zip failed\n
%s::%s: Invalid plistDict\n
%s::%s: could not find FW (%s) in build ID\n
%s::%s: failed to convert from data to boolean\n
%s::%s: leaving: VinylRestoreHost: %s\n
%s::%s: failed to get backing length\n
%s::%s: failed to create mutable copy of source device firmware data dictionary (type: %hhu)\n
%s::%s: tag %s missing from firmware, skipping\n
%s::%s: converting from data to boolean\n
%s::%s: function cannot directly manipulate file data with optimized flow\n
%s::%s: could not obtain file data\n
%s::%s: attempting to add new file to cache, but not both size and offset are provided. File: %s\n
%s::%s: cache does not hold correct size for file %s. Cache size: %d. FTAB size: %d. Cache is invalid\n
%s::%s: number of files in cache is invalid\n
%s::%s: Invalid arguments to parseDebugArgs\n
Failed to write '%@' header
%s::%s: VinylRestoreHost: destructor\n
%s::%s: Failed getting FW MAC\n
%s::%s: failed to get byte ptr of fwldrver\n
%s::%s: Using FDR trust object hash in client updater override\n
%s::%s: File indicated is within header space\n
%s::%s: failed to find bbfw item status %d\n
%s::%s: Memory alloc failed certIds/VadDigest\n
%s::%s: failed obtain new file data\n
%s::%s: failed to copy file header\n
%s::%s: firmware data has wrong type\n
%s::%s: successfully created request\n
%s::%s: Failed to open firmware\n
%s::%s: Unable to allocate memory for fullPath:\n
%s::%s: Invalid FDR trust object hash in client updater override\n
%s::%s: failed to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: failed to create host object\n
%s::%s: epro data to boolean conversion failure\n
%s::%s: failed to allocate data\n
%s::%s: Failed to open firmware in restore options\n
%s::%s: updater options has wrong type\n
%s::%s: leaving: %s\n
%s::%s: bundle firmware specified is invalid\n
%s::%s: Prov flow\n
%s::%s: failed to allocate source bundle firmware path dictionary (type: %hhu)\n
%s::%s: failed to remove bundle fw personalized bits\n
%s::%s: Failed to allocate measurements dict\n
%s::%s: no file path provided\n
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: entering: VinylRestoreInfo: %s\n
%s::%s: enable gid3En for rtkitos\n
%s::%s: removing any personalized bits of rooted firmware\n
%s::%s: cache does not have entry for file %s. Cache is invalid\n
%s::%s: successfully got tags\n
%s::%s: failed to parse debug arguments\n
%s::%s: Restore boot nonce present!\n
%s::%s: failed to get create request Dictionary\n
%s::%s: invalid type for iboot\n
%s::%s: Invalid firmware file\n
%s::%s: no fw for tag '%s'\n
%s::%s: data exceeds local buffer size\n
%s::%s: failed to initialize logging\n
%s::%s: input data has no bytes\n
%s::%s: VinylRestoreHost::createRequestDict\n
%s::%s: mainProfileData not present in the input\n
%s::%s: failed to find and/or copy data\n
%s::%s: =========== FTAB Payloads ===========\n\n
%s::%s: failed to create error\n
%s::%s: found rooted firmware\n
%s::%s: mainFwData not present in the input\n
%s::%s: failed to get dict entry\n
%s::%s: manifest present beyond the bounds of the file data\n
%s::%s: empty file\n
%s: File tag parse error (%02x %02x %02x %02x)
%s::%s: failed to create description\n
%s::%s: successfully copied firmware\n
%s::%s: failed to get tags\n
%s::%s: copying preflighted rooted firmware into the dst bundle...\n
%s::%s: bad parameter: options %p, domain %p\n
%s::%s: key value not provided\n
%s::%s: paddingBeforeManifestStart %u bytes\n
%s::%s: attempting to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
%s::%s: Manifest is not present in expected data type\n
UARP: TSS Response %{public}@%{public}@ is 
%s::%s: failed to create empty data\n
%s::%s: chipID is not 2 bytes in length. Assuming Rose-SE pairing is not supported.\n
%s::%s: Deviceinfo is not a dictionary\n
%s::%s: srcPath memory alloc failed\n
%s::%s: wrong digest type (%s)\n
%s::%s: Failed to save packaged firmware file\n
%s::%s: Returning empty sharing digest dictionary -- Rose-SE pairing not supported for this device.\n
%s::%s: Unable to unzip the fwdata:\n
%s::%s: null error parameter\n
%s::%s: bad parameter!\n
%s::%s: could not update ftab cache\n
%s::%s: %s\n
%s::%s: failed to measure fw\n
%s::%s: failed to get dict entry for sbd1 digest\n
%s::%s: incorrect baseband prov info type\n
%s::%s: tag '%s' not found in identity dictionary, ignoring\n
UARP: TSS request is using SSO
%s::%s: failed to create capabilities\n
%s::%s: mainIm4p not present in the input\n
%s::%s: failed to compute digest\n
%s::%s: failed to get src bundle URL\n
%s::%s: failed to add new file\n
%s::%s: Adding new file to FTAB cache. File: %s, offset: %u, size: %u\n
%s::%s: Digest of manifest failed\n
%s::%s: failed to determine if url exists (%u)\n
%s::%s: Failed fo retain firmwareDict\n
%s::%s: Using embedded ftab '%s'\n
%s::%s: attempting to delete file from cache that does not exist. File: %s\n
%s::%s: Unrecognized CF object!\n
%s::%s: file name does not exist\n
%s::%s: failed to get firmware object\n
%s::%s: failed to create mutable data in optimized path\n
%s::%s: invalid optimization mask\n
%s::%s: failed to update cache\n
%s::%s: failed to copy type description for type ID %lu\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: failed to add VAD\n
%s::%s: Unable to copy the firmware:\n
%s::%s: converting from string to number\n
%s::%s: failed to overwrite file (%d)\n
%s::%s: specified tag name is invalid!\n
%s::%s: Failed to create empty trust object hash\n
%s::%s: file '%s' does not exist\n
%s::%s: ftab cache entry updated. File: %s, offset: %u, size: %u\n
%s::%s: VinylRestoreHost: constructor\n
%s::%s: failed to get im4p values\n
%s::%s: tag '%s' has different values in device info and build identity\n
%s::%s: forcing pairing with build ID: %u\n
%s::%s: goldIm4p not present in the input\n
%s::%s: Failed to get value for: %s, exception: %s\n
%s::%s: plistFileName %s\n
%s::%s: failed to create dirURL\n
%s::%s: rooted firmware was personalized already so we should use that to update\n
%s::%s: no manifest found in ftab\n
%s::%s: no write permissions to file... attempting to open file as read-only\n
%s::%s: data length %ld is not within range\n
%s::%s: setAuthPayload failed delete vinylFirmware object\n
%s::%s: VinylFirmware destructor called\n
%s::%s: Get Profile Data from Zip failed\n
%s::%s: fwSrcPath memory alloc failed\n
%s::%s: failed to map file: (%s)\n
%s::%s: failed to create CFString for error object\n
%s::%s: Failed to find firmware\n
UARP: Personalization Message >> %{public}s
%s::%s: No sources found \n
%s::%s: manifest is at top - endOfManifest: %u, startOfFiles: %u, paddingAfterManifestEnd: %u\n
%s::%s: bad input file parameters\n
%s::%s: entering: VinylRestoreHost: %s\n
%s::%s: Failed to alloc create plistFilePath CFString\n
%s::%s: file data must be valid or firmware data must be provided\n
%s::%s: failed to copy ftab header\n
%s::%s: This function has not been implemented\n
%s::%s: SHA512 failed\n
%s::%s: Invalid Type of DebugArgs\n
UARP: TSS Request to default server
UARP: TSS Request failed sso modes
%s::%s: failed to create request\n
%s::%s: security mode not present in device info. This is fatal!\n
%s::%s: tag '%s' not found in tss-request map, ignoring\n
%s::%s: firmware file is invalid\n
%s::%s: Firmware Version: %s\n
UARP: TSS Request %{public}@%{public}@ is 
%s::%s: global signing has wrong type\n
%s::%s: failed to init ftab file object\n
%s::%s: failed to create build ID key path for rkos\n
%s::%s: failed to create build identity tag list\n
%s::%s: failed due to unexpected data type\n
%s::%s: firmware is invalid\n
UARPTLVPersonalizationLifeOS
UARPTLVPersonalizationChipRevisionOS
UARPTLVPersonalizationManifestEpochOS
UARPTLVPersonalizationFTABSubfileHashAlgorithmOS
UARPTLVPersonalizationFTABSubfileDigestOS
UARPTLVPersonalizationFTABSubfileTagOS
NSCopying
MRUPersonalizedFirmware
UARPTLVPersonalizationEnableMixMatchOS
UARPTLVPersonalizationNonceOS
NSSecureCoding
RTKit
UARPTLVPersonalizationBoardIDOS
UARPTLVPersonalizationSoCLiveNonceOS
UARPMetaDataTLVOS
UARPAssetVersionOS
UARPTLVPersonalizationPayloadTagOS
ASAuthorizationControllerDelegate
UARPTLVPersonalizationProvisioningOS
UARPTLVPersonalizationRequiredOS
UARPTLVPersonalizedManifestOS
UARPTLVPersonalizationSuffixNeedsLogicalUnitNumberOS
NSCoding
AppleTypeCRetimerFirmwareCopierOS
AMAuthInstallOSSsoAuthenticator
UARPTLVPersonalizationSuperBinaryPayloadIndexOS
UARPTLVPersonalizationFTABSubfileTrustedOS
AppleTypeCRetimerRestoreInfoHelperOS
UARPSuperBinaryPayloadOS
UARPSuperBinaryOS
FTABSubfileOS
Utils
Ace3SoCRestoreInfoHelperOS
UARPTLVPersonalizationFTABSubfileLongnameOS
FTABFileOS
Dump
MRUPersonalizationInfo
UARPMetaDataTLVDataOS
UARPTLVHostPersonalizationRequiredOS
UARPTLVPersonalizationFTABSubfileESECOS
UARPTLVPersonalizationFTABSubfileDigestFilenameOS
MantaFTABFile
UARPMetaDataTLV8OS
AppleTypeCRetimerFirmwareAggregateRequestCreatorOS
UARPTLVRequiredPersonalizationOptionOS
UARPTLVPersonalizationSecurityModeOS
UARPTLVPersonalizationECIDOS
UARPTLVPersonalizationECIDDataOS
UARPTLVPersonalizationManifestSuffixOS
MantaFTABSubfile
UARPTLVPersonalizationChipEpochOS
UARPTLVPersonalizationFTABPayloadOS
UARPAssetTagOS
MRUHardwareInfo
Ace3SoCRestoreInfoFirmwareCopierOS
UARPTLVPersonalizationTicketNeedsLogicalUnitNumberOS
UARPTLVPersonalizationSuperBinaryAssetIDOS
FTABWrite
UARPMetaDataTLVStringOS
AppleTypeCRetimerFirmwareRequestCreatorOS
NSObject
FileExistsCheck
UARPTLVPersonalizationChipIDOS
UARPMetaDataTLV64OS
Ace3RestoreInfoFirmwareCopierOS
UARPTLVPersonalizationManifestPrefixOS
UARPMetaDataTLV16OS
Availability
UARPTLVPersonalizationPrefixNeedsLogicalUnitNumberOS
UARPTLVPersonalizationSecurityDomainOS
UARPTLVPersonalizationProductionModeOS
UARPTLVPersonalizationNonceHashOS
MRULogHelper
UARPTLVPersonalizationLogicalUnitNumberOS
UARPTLVPersonalizationFTABSubfileEPROOS
UARPMetaDataTLV32OS
_dataLength
T^v,V_layer2Context
_dataPointer
_subfiles
hash
initWithType:length:value:
logicalUnitNumber
_tlvLength
createFileHandleForWritingToURL:
initWithOptions:logFunction:logContext:
payload
_hardwareInfo
ticketPrefix
T@\"NSData\",R
_logContext
caseInsensitiveCompare:
_manifestSuffix
generatePersonalizedSuperBinary
T@\"NSString\",R,V_manifestSuffix
_demote
TI,R,V_payloadIndex
compare:
containsValueForKey:
removeItemAtPath:error:
TB,N,V_stealthMode
Tr*,R,V_dataPointer
appendLittleInt16:
dataLength
decodeObjectForKey:
longTagName:
setAssetID:
setProductionMode:
getTlvs
componentsSeparatedByString:
superbinary:logString:
zone
boardID
generateHashForSubfile:
getDataBlock:offset:
TI,R,V_tag
_url
bytes
TB,R
TQ,V_ecID
length
setTssOption:
setUseLegacyAuthURL:
TC,R,V_provisioning
TC,V_securityMode
TI,R,V_chipID
_digest
version
_prefixNeedsUnitNumber
firstObject
generateHashSHA256
TI,R,V_valid
URLByDeletingLastPathComponent
_componentName
_ecid
_fileHandleWriteDestination
fileHandleForWritingToURL:error:
initWithBytes:length:encoding:
performSelector:
_destBundlePathURL
retain
_dataWriteDestination
_ecidData
setDelegate:
setPrefixNeedsLogicalUnitNumber:
tlvFromPropertyListValue:
writeData:error:
fileExistsAtPath:
payloadsWithout4ccTag:
release
TC,R,V_prefixNeedsLogicalUnitNumber
_char4
_formatVersion
_stealthMode
_tssOption
_metaData
T@\"NSData\",R,V_nonceHash
TI,R,V_securityMode
flags
TI,R,V_tlvLength
TS,R,V_epro
URLWithString:
_nonce
_trustedOverride
isRequired
mutableCopy
numberFromString:
T@\"NSString\",R,V_longname
TI,R,V_chipRev
TQ,R,V_releaseVersion
copyWithZone:
enableMixMatch
esec
writeToData
.cxx_destruct
expandMetaData:
copy
copyItemAtPath:toPath:error:
dataWithContentsOfFile:options:error:
filePointer
initWithFormat:arguments:
isGreaterThan:
_generation
addSubfiles:
requestDictionary
securityDomain
TI,R,V_chipEpoch
TS,R,V_esec
_bootNonce
digest
hashAlgorithm
objectForKeyedSubscript:
setChipEpoch:
versionString
T#,R
T@\"NSData\",R,V_magic
TQ,R,V_ecID
_filename
_ftab
_isRequired
initWithTag:dataPointer:dataLength:
name
T@\"NSString\",R,V_filename
setLiveNonce:
setSsoEnv:
authorizationController:didCompleteWithError:
setValue:forHTTPHeaderField:
stringWithUTF8String:
T@\"NSString\",R,C
T@\"ASAuthorizationController\",&,N,V_authenticationController
TQ,R,V_ecid
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
noncePropertyName
T@\"NSDictionary\",R,V_tssRequest
seekToEndReturningOffset:error:
enumerateObjectsUsingBlock:
needsHostPersonalization
setTicketNeedsLogicalUnitNumber:
T@\"NSNumber\",C,V_trustedOverride
T@\"NSString\",R
TC,R,V_enableMixMatch
TS,R,V_hashAlgorithm
ecidData
prefixNeedsLogicalUnitNumber
readDataUpToLength:error:
setUserInterfaceEnabled:
TC,V_life
authorizationController:didCompleteWithAuthorization:
generateTatsuMeasurementsPerPayload:
metaDataTable
queryItems
_ecID
_tatsuMeasurements
authorizationController:didCompleteWithCustomMethod:
ftabWriteData:error:
writeToDestination
writeBytes:length:
arrayWithArray:
_flags
_securityMode
generateHashForData:
setDemote:
setObject:forKeyedSubscript:
createDestinationBundleFirmwareDirectoryFor:error:
processTLVsForPersonalization
T@\"NSData\",C,V_nonce
T@\"NSDictionary\",R
_totalLength
_nonceHash
completionHandler
stringWithValidatedFormat:validFormatSpecifiers:error:
Tc,R,V_char4
_firmwareBundleURL
_objectName
conformsToProtocol:
objectAtIndex:
productionModePropertyName
setTrusted:
stringWithString:
initWithChipID:chipRev:boardID:securityEpoch:productionStatus:securityMode:securityDomain:ecid:
queryItemWithName:value:
removeAllObjects
trusted
_payloadIndex
code
intValue
majorVersion
tatsuMeasurements:
TI,R,V_generation
addObject:
array
expandSuperBinary
initWithVersionString:
setChipRevision:
setLogicalUnitNumber:
setLongname:
url
T@\"NSString\",&,N,V_ssoRealm
TS,R,V_trusted
_measurements
numberWithUnsignedLong:
setSsoHost:
subfiles
totalLength
allHeaderFields
addSubfileWithTagName:subfileData:
asDictionary
description
integerValue
uarpReadDataToEndOfFileAndReturnError:
_liveNonce
_logFunction
char3
generateRequestDictionary
longLongValue
chipRevision
generatePersonalizedSuperBinaryWithoutRRKO
init
setQueryItems:
_firmwareOverrideData
_suffixNeedsLogicalUnitNumber
hardwareInfo
setSecurityDomain:
tlvType
_asset
_componentNameSuffix
_life
_trusted
appendString:
initWithTag:data:
TQ,R
_fileLength
copyFirmwareToDestinationBundleWithError:
data
decodeObjectOfClass:forKey:
generateTLV:tlvValue:
initWithHardwareInfo:componentName:objectName:nonce:tagNumber:
_ssoEnv
HTTPMethod
_service
logInternal:arguments:
securityMode
securityModePropertyName
setEcidData:
stringWithCapacity:
_char3
_ticketSuffix
_version
string
tssRequestAsString
_minorVersion
_cphyData
_prefixNeedsLogicalUnitNumber
_tlvType
numberWithUnsignedInt:
value
TC,V_securityDomain
manifest
setEsec:
tlvs
T@\"NSData\",R,V_metaData
Tr*,R,V_filePointer
_boardID
TC,V_productionMode
_apParameters
_epro
_rrko
requiredTSSOptions
ticketNeedsLogicalUnitNumber
_provisioning
errorWithDomain:code:userInfo:
setEpro:
totalBytesRequested
_productionStatus
createRequest
isEqual:
path
securityDomainPropertyName
tlvFromKey:value:
T@\"NSDictionary\",R,V_requestDictionary
T@\"NSData\",R,V_nonce
isProxy
setTag:
_buildVersion
boolValue
isEqualToString:
payloads
initWithString:
authorizationProviderWithIdentityProviderURL:
initWithChar1:char2:char3:char4:
suffixNeedsLogicalUnitNumber
TQ,R,V_fileLength
personalizeSuperBinary:signingServer:ssoOnly:
releaseVersion
setTicketPrefix:
_chipRevision
authenticationController
getPayloads
tlvValue
currentHandler
fileValidForOffset:length:
initWithData:encoding:
setManifestEpoch:
ssoRealm
setStealthMode:
dataWithContentsOfFile:
setAuthorizationOptions:
subfileWithTag:
_deviceInfoArray
_subFileArray
layer2Context
_chipID
_chipRev
_requestDictionary
doesNotRecognizeSelector:
_firmwarePathSuffix
_trimmedTlvs
count
defaultManager
setAuthenticationController:
stealthMode
stringByExpandingTildeInPath
TS,R,V_assetID
_payloads
_valid
addEntriesFromDictionary:
authenticate
boardIDPropertyName
credential
productionStatus
URLByAppendingPathComponent:
dumpString
magic
setDigest:
setIsRequired:
stringByAppendingString:
tlvLength
addObjectsFromArray:
dataWithContentsOfURL:options:error:
domain
hasPrefix:
unsignedLongValue
_layer2Context
_longname
_payloadData
generateHashSHA384
generateTatsuMeasurements:
isFileExistsError
payloadIndex
subdataWithRange:
URL
_hashAlgorithm
char4
chipEpoch
demote
metaData
numberWithUnsignedLongLong:
queryItemsWithParameters:
TB,R,V_needsHostPersonalization
T@\"NSArray\",R,V_tlvs
T@\"NSString\",&,N,V_ssoHost
T@\"NSString\",?,R,C
expandTLVs
setTrustedOverride:
_logicalUnitNumber
_ssoRealm
firmwareKeyFromBuildIdentityDict:deviceInfo:
initWithData:metaData:tag:version:
uarpReadDataUpToLength:error:
ssoHost
TI,R,V_dataLength
TI,R,V_securityEpoch
allHTTPHeaderFields
initWithCoder:
metaDataTableEntry
TB,N,V_useLegacyAuthURL
_completionHandler
dataWithBytes:length:
handleFailureInFunction:file:lineNumber:description:
personalizedMetaData
setBoardID:
decodeCharForKey:key:
parseOptions:
setSuffixNeedsLogicalUnitNumber:
T@\"NSData\",C,V_manifest
TQ,R,V_buildVersion
_rkos
_tssRequest
initWithBVERString:
isMemberOfClass:
queryTatsuSigningServer:ssoOnly:error:
respondsToSelector:
percentEncodedQuery
readDataToEndOfFileAndReturnError:
tlvWithLength:value:
generation
processMeasurementsForTSSOptions:unitNumber:asMeasurement:
tssRequest
writeToURL:atomically:
T@\"NSData\",R,V_payload
_char2
_ticketNeedsUnitNumber
authorizationController:shouldRetryAfterError:
generateHashSHA512
longname
setService:
getBytes:range:
_rkosData
ssoEnv
_uinitNumber
appendData:
ecID
setNonceHash:
addSubfile:tag:
_propertyNameSuffix
appendBytes:length:
setEcID:
unsignedCharValue
T@\"NSArray\",R,V_measurements
T@\"NSArray\",R
TB,R,V_productionStatus
TQ,R,V_totalLength
_chipEpoch
keyWithPrefix:
removeSubfile:tag:
setSsoRealm:
Tc,R,V_char1
chipID
dataWithData:
initFile
life
numberWithUnsignedInteger:
setTLVs:
unsignedLongLongValue
T@\"NSData\",R,V_digest
TC,R,V_isRequired
TI,R,V_securityDomain
Tr^{?=IIQQ^{__CFString}^{__CFString}},N,V_service
_authenticationController
tlvTypeName:
unsignedIntValue
writeToURL:error:
T@\"NSNumber\",C,V_demote
service
_verbose
appendFormat:
dataPointer
debugDescription
initWithFilePath:delegate:delegateQueue:
parseFileData
T@\"NSData\",R,V_payloadData
_firmwareInBundleDataDict
supportsSecureCoding
uarpWriteData:error:
_manifestEpoch
removeObject:
Tc,R,V_char2
char2
initWithMajorVersion:minorVersion:releaseVersion:buildVersion:
retainCount
seekToOffset:error:
setLayer2Context:
unsignedShortValue
T@\"NSData\",R,V_bootNonce
_tlvValue
canPerformAuthorization
fileURLWithPath:
nonce
payloadWith4ccTag:
TB,V_provisioning
TC,R,V_suffixNeedsLogicalUnitNumber
TI,V_boardID
nonceHash
setManifest:
TI,V_chipID
_rrkoData
performSelector:withObject:
tssKeyName:unitNumber:
uarpSeekToOffset:error:
useLegacyAuthURL
TQ,R,V_totalBytesRequested
_ticketNeedsLogicalUnitNumber
initWithBytes:length:
performSelector:withObject:withObject:
T@\"NSData\",R,V_manifest
T@\"NSString\",&,N,V_ssoEnv
_ticketPrefix
configureDataWriteDestination
ticketName
tssOption
T@\"MantaFTABSubfile\",R,V_manifest
TC,R,V_life
_totalBytesRequested
arrayWithObjects:count:
fileLength
bootNonce
char1
class
rtKitKeyFromBuildIdentityDict:
writeToURL:
_suffixNeedsUnitNumber
T@\"FTABSubfileOS\",R,V_manifest
preparePayload:
log:
numberWithUnsignedShort:
T@\"NSURL\",R,V_url
Tc,R,V_char3
_keyManifest
_useLegacyAuthURL
absoluteString
ecidPropertyName
removeSubfileWithTag:
setBootNonce:
TI,R,V_isRequired
TI,R,V_tssOption
_securityEpoch
epro
initWithData:delegate:delegateQueue:
initWithPayload:manifest:
bverString
generateTatsuMeasurements:relativeURL:
uarpCloseAndReturnError:
tag
_enableMixMatch
T@\"UARPAssetVersionOS\",R,V_version
getManifest
removeItemAtURL:error:
setProvisioning:
numberWithBool:
T@\"NSString\",R,V_tag
_majorVersion
securityEpoch
setPayloadIndex:
setQuery:
_delegateQueue
countByEnumeratingWithState:objects:count:
productionMode
assetID
appendByte:
filename
setHashAlgorithm:
verboseLog:
_productionMode
TI,R,V_chipRevision
_payload
enumerateKeysAndObjectsUsingBlock:
numberWithUnsignedChar:
stringWithFormat:
_releaseVersion
T@\"NSData\",C,V_ecidData
trustedOverride
tlvFromType:length:value:
unsignedIntegerValue
valueForKeyPath:
TC,V_manifestEpoch
TQ,N,V_flags
_delegate
_needsHostPersonalization
chipIDPropertyName
TI,R,V_productionMode
UTF8String
configureFileHandleWriteDestinationForURL:
createFileAtPath:contents:attributes:
generatePersonalizedSuperBinaryInternal:
valid
T@\"NSArray\",R,V_payloads
decodeBytesForKey:returnedLength:
self
setFilename:
setFlags:
setObject:forKey:
initWithOptions:error:
TQ,R,V_majorVersion
_ssoHost
autorelease
composeTSSRequest:asMeasurement:
getNeedsHostPersonalization
initWithAuthorizationRequests:
initWithHardwareInfo:componentName:objectName:nonce:
_tlvs
byteString
initWithURL:delegate:delegateQueue:
setChipID:
setSecurityMode:
tlvValue:
T@\"UARPAssetTagOS\",R,V_tag
_securityDomain
authenticationURL
ecid
fileURLWithPath:isDirectory:relativeToURL:
minorVersion
_assetID
_char1
composeTSSRequest:
dictionaryWithObjects:forKeys:count:
initWithContentsOfURL:
initWithData:
manifestEpoch
TI,R,V_logicalUnitNumber
copyItemAtURL:toURL:error:
encodeWithCoder:
liveNonce
objectName
writeBytes:length:handle:
writeSubfileToURL:tag:
_tag
authenticatedResponse
measurements
personalizedData
provisioning
setEnableMixMatch:
TB,R,V_securityMode
isKindOfClass:
superclass
TI,R,V_tlvType
_esec
dictionaryWithDictionary:
_fileData
buildVersion
lastPathComponent
payloadData
TI,R,V_boardID
T@?,C,N,V_completionHandler
setNonce:
TC,R,V_manifestEpoch
HTTPBody
_data
_filePointer
_tagNumber
closeAndReturnError:
TC,R,V_ticketNeedsLogicalUnitNumber
isValid
getTssRequest
objectAtIndexedSubscript:
setLife:
uarpSeekToEndReturningOffset:error:
_manifest
generateTLV
manifestSuffix
getMeasurements
dictionary
readFirmwareFileDataWithError:
setManifestSuffix:
T@\"NSString\",R,V_ticketPrefix
appendLittleInt32:
setCompletionHandler:
T@\"MRUHardwareInfo\",R,V_hardwareInfo
T@\"NSData\",R,V_ecID
performRequests
TC,R,V_liveNonce
_magic
encodeBytes:length:forKey:
encodeObject:forKey:
chipRev
TQ,R,V_minorVersion
addSubfileWithTagName:contentsOfURL:
dataWithContentsOfURL:
v24@0:8@?16
@20@0:8I16
@24@0:8I16S20
@24@0:8@16
@32@0:8@16@24
@24@0:8I16C20
v36@0:8@16Q24B32
@\"NSObject<OS_dispatch_queue>\"
B16@0:8
v32@0:8@\"ASAuthorizationController\"16@\"ASAuthorization\"24
Q
Q16@0:8
B24@0:8@\"Protocol\"16
@?16@0:8
v24@0:8@16
@\"NSDictionary\"
r^{?=IIQQ^{__CFString}^{__CFString}}16@0:8
@\"UARPAssetTagOS\"
@\"NSURL\"
S
@32@0:8I16I20^v24
@24@0:8o^@16
B24@0:8:16
@\"NSArray\"
B40@0:8r^v16Q24@32
@24@0:8Q16
B24@0:8^{UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}16
v16@0:8
@\"NSMutableArray\"
r*32@0:8@16@24
@28@0:8I16Q20
v20@0:8I16
@24@0:8I16I20
@\"NSString\"16@0:8
v32@0:8@\"ASAuthorizationController\"16@\"NSString\"24
^?
@\"NSNumber\"
B32@0:8@16o^@24
B36@0:8@16B24^@28
@\"NSString\"
#16@0:8
B24@0:8#16
B24@0:8^@16
@\"NSData\"
B32@0:8r^v16Q24
I16@0:8
C
@32@0:8:16@24
v20@0:8C16
B32@0:8o^Q16o^@24
@56@0:8@16@24@32@40@48
@20@0:8C16
c
r*
@\"NSMutableString\"
@40@0:8@16@24@32
B32@0:8Q16@24
C16@0:8
@40@0:8:16@24@32
@?
@\"NSMutableData\"
@48@0:8Q16Q24Q32Q40
@\"MantaFTABSubfile\"
@32@0:8Q16^v24
r*16@0:8
@28@0:8Q16B24
@\"UARPAssetVersionOS\"
^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHe
@52@0:8I16I20I24I28B32B36I40Q44
@\"FTABFileOS\"
@\"FTABSubfileOS\"
q24@0:8@16
B32@0:8Q16o^@24
@\"NSFileHandle\"
@36@0:8Q16@24B32
@\"<UARPSuperBinaryDelegate>\"
@32@0:8@16^@24
B32@0:8@16@24
Vv16@0:8
@32@0:8c16c20c24c28
v32@0:8@16@24
c16@0:8
v24@0:8Q16
@\"ASAuthorizationController\"
B32@0:8@16^@24
@48@0:8@16@24@32@40
B
@24@0:8^@16
@28@0:8I16@20
B24@0:8^{UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}16
@32@0:8Q16Q24
@32@0:8Q16o^@24
@\"MRUHardwareInfo\"
@32@0:8@16Q24
@\"NSMutableDictionary\"
v20@0:8B16
B24@0:8@16
@40@0:8@16^?24^v32
@24@0:8^{_NSZone=}16
v24@0:8@\"NSCoder\"16
B24@0:8I16I20
@24@0:8:16
v24@0:8r^{?=IIQQ^{__CFString}^{__CFString}}16
v20@0:8S16
@16@0:8
^v
@36@0:8@16r^v24I32
r^{?=IIQQ^{__CFString}^{__CFString}}
^{_NSZone=}16@0:8
I
^v16@0:8
v24@0:8^v16
v32@0:8@\"ASAuthorizationController\"16@\"NSError\"24
v32@0:8@16*24
S16@0:8
@24@0:8@\"NSCoder\"16
@20@0:8S16
B24@0:8o^@16
BbVendorData
failed to compute NSIH for %@: %@
getTags: failed to create build identity tag list
Baseband provisioning failed
Cryptex1,MobileAssetBrainTrustCache
AMAuthInstallMonetMeasureElf
rdcp
Ap,Scorpius
RamPSI-Version
ACFURestoreHost
Failed to locate rkos file in super binary ftab
%s::%s: updater options has wrong type\n
%s::%s: failed to find bbfw item status %d\n
Ap,ANE2
ypilkyibsrqvlyazp6iuq6tu4i2ume
AMAuthInstallSsoCopyCredentialsFromKeychain
failed to create CFUserNotification
Cryptex1,NonceDomain
%s::%s: Failed to find firmware\n
%s::%s: firmware file is invalid\n
%s::%s: failed to get manifest, error: %d\n
toEncoder cannot be NULL
x-intnt-keyalg-certformat
fakeTicket is NULL
%s::%s: failed to create mutable data\n
Personalization FTAB Payload Trusted
Updated Request Dictionary:
unrelated failure; will reclaim fusing program
createArrayFromList
BootUUID
AMAuthInstallBasebandFinalize
Error HttpOpenRequest
%s::%s: failed to allocate data for personalized path\n
OS
No blob in response
Cellular1,CdpHost
Cellular2,Nonce
%@:\n
AMAuthInstallSetFusingServerURL
oauthClientID
2
Error creating data of response
%s::%s: failed to init data container object\n
fwReaderCallback
SHA1Result failed=%d
SinopeUpdaterCreateRequest: failed to open firmware
copyFirmware: failed to remove rooted fw personalized bits
legacy_rat_fw.elf
Path
@ServerVersion
@EUICCTicket
Error key->string
%s::%s: invalid type for iboot\n
%s::%s: data length %ld is not within range\n
No cphy data found
%s::%s: firmware file failed to initialize\n
Details: 
plist_filename : 
BbNonce
PERTOS
Ap,VolumeUUID
AVISP1,RTKitOS
Ap,SDKPlatform
_updater_named
Unsupported chip ID
Existing provisioning manifest found. Not attempting to provision.
getFileSize
AVISP1,PERTOS
%s::%s: cannot aquire reference for a memory optimized data container. Please use copyData() instead\n
copyDataFromFileDictionary
Timer,RestoreRTKitOS,%u
Ap,ExclaveOSTrustCache
aubt
failed to create output file
%s::%s: could not get 'rrko' object from ftab\n
TBMDigests
%s: failed to encode data
com.apple.EmbeddedSoftwareRestore.Baseband.ChipId
IMEI2
BasebandProvInfo
AMAuthInstallApServerRequestAddRequiredTagsWithRecoveryOS
failed to copy data from %@
WARNING: Could not retrieve image properties from devicemap.
msys
%5F
AMSS-DownloadDigest
%s::%s: incorrect device info type\n
%s::%s: No sources found \n
DGST
custpack.elf
APPLECONNECT.APPLE.COM
OK to skip recovery OS - continuing.
%s::%s: converting from string to number\n
%s::%s: global signing has wrong type\n
ginf
AMAuthInstallBundleCopyPublishedVariantsArray
%s::%s: failed to get byte pointer\n
%@,Ticket
failed to add ESEC property for '%@'
mistyped meid
%s: input options: %@
%s::%s: Didn't find a matching embedded ftab\n
Timer,RTKitOS,%u
Wireless1,ProductionMode
updateMeasurementDict
AMAuthInstallBundleCopyPublishedVariantsArray returned NULL
using baseband firmware override: %@ = %@
AllowNeRDBoot
Cellular2,BbFATPCalibrationEnable
%s::%s: invalid FTAB file\n
isCacheValid
0000  
%s::%s: boardID is not 2 bytes in length. Assuming Rose-SE pairing is not supported.\n
%@-TBM
Cellular1,Recipe
initLog
16435966288656694
%s::%s: copyFirmware: failed to create default FW URL, (status: %d)\n
build identity value converted: 
Failed to create hardwareInfo, options: %@
%s::%s: failed to init bundle firmware\n
AMAuthInstallApImg3CopyBuildString
CFHTTPMessageCreateRequest failed
provisioningDict is NULL
psi_ram.fls
%s::%s: failed to build parameters out of build identity\n
%s::%s: manifest present beyond the bounds of the file data\n
%s::%s: failed to create error\n
Payload %2d: [%.4s], %7u bytes.
AMAuthInstallMonetCreateMEIDFromString
Info
%s::%s: failed to create output request dictionary\n
%s::%s: rkos bundle data unavailable\n
LoadableTrustCache
kmpi
UID value of %ld exceeds maximum array bound of %d\n
IsEarlyAccessFirmware
Error empty response create data
Wireless1,CCPUApplicationFirmware
%s::%s: No device info\n
%s failed to encode tag
ApRawSecurityMode
%s: _AMAuthInstallSsoSUSSOCopyToken failed
_AMAuthInstallSsoACMobileInit
tss_submit_job_with_retry
%s::%s: Could not obtain deviceInfo dictionary. Sharing all digest information.\n
Ap,AppleTypeCPhyFirmware
eUICC Param %d unchanged
BuildManifest.plist
AMAuthInstallFusingCreateProfileName
----Begin request
failed to convert ECID %@
rxcl
AMAuthInstallApImg4FindProperty
mistyped encrypted session key
Personalized
AMAuthInstallBundlePersonalizePartialRecoveryOS
%lu
TICKET_VERSION
custom.bbfw
%s: variant is NULL
DFUFileType
AMAuthInstallSupportCreateURLFromString
%s::%s: Adding new file to FTAB cache. File: %s, offset: %u, size: %u\n
InternalBuild
%s::%s: successfully created request\n
fwMacData: 
UpdaterRequestEntries
lpw0
ApDemotionPolicyOverride
getVersion
%s: failed to create local manifest
%s::%s: data is of an unsupported type\n
copyFirmwareUpdater: unexpected device info parameters
Wrong DeviceInfo
fwData and buildIdentity are nullptr
%s::%s: failed to open bbfw archive for reading eUICCFwReaderOpen\n
failed boardKey allocation
%s: failed to get info dict
RestoreHost
rfts
auac
failed to measure: GNSS_FW.elf
*   failed to ack fusing program; continuing anyway   *
Restore.plist
AMAuthInstallMonetSetVersionAndPartialDigest
%s: _AMAuthInstallSsoCopyTicketWithCredentials failed %ld
true
AppleTconUARP
Server not reachable
%s::%s: =========== FTAB Header ===========\n
_AMAuthInstallApImg4CreateDefaultRestoreInfo
provisioning
BSN: 
AMAuthInstallBasebandN41StitchFirmware
restorexbl_sc.elf
----End request
failed to copy payload properties to measurement dictionary.
UniqueBuildID
invalid provisioningInfoValuesBuffer array
Ap,Target
DBL-PartialDigest
Error tssversion->string
%s::%s: tag '%s' not found in build identity, skipping validation\n
%s::%s: Failed to parse debugArgs\n
Cryptex1
siof
bundle personalization requires AP parameters (even with AP personalization disabled)
SocksProxySettings
SE,RapRTKitOS
encodedValue == NULL: '%@'
RestoreRamPSI-Blob
%s::%s: =========== FTAB Payloads ===========\n
CFDictionaryRef  _Nullable SoCUpdaterExecCommandDynamic(NSString *__strong _Nullable, SoCUpdaterLogSinkFunction _Nonnull, void * _Nonnull, CFStringRef _Nonnull, CFDictionaryRef _Nonnull, CFErrorRef * _Nullable)
NO
AMAuthInstallMonetStitchMav25EBootLoader
%s: invalid string
BbfwWriterCreate
copyFirmware: bundle firmware specified is invalid
basic_string
Wireless1,Wifi2GLPhyManuf
Existing provisioning manifest found. Force provisioning is enabled; provisioning anyway.
BbServerNonce
%s::%s: attempting to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: File indicated is within header space\n
ronh
Failed allocation
Personalizing %@
%s: amai is NULL
kern.bootsessionuuid
setting B64_BB_CHIPID failed
libAmSupportErrorDomain
message is NULL
DSP1-DownloadDigest
setFTABValidity
AMAuthInstallApImg4DecodeRestoreInfo
PartialDigest = %@
response missing \"%@\"
\tGeneration: 0x%08x\n
RestoreSBL1-HashTableBody
%s::%s: key value not provided\n
%s::%s: failed to init ftab file object\n
entry.data && entry.length
sm3f
RELEASE
unsupported URL scheme
createMutableFileDatafromFilePath
rtpf
Ap,RestoreCIO
DSP3-HashTableDigest
SE
failed to strip img3 header
, sepNonce=0x%@
zero length euicc main nonce
* unacknowledged fusing program *
AMAuthInstallBasebandLocalSigningEnabled
CDMA2KFW-HashTableDigest
failed to cache server error text: (%d) %@
KeyID 0x%X, overwriting with dev %d
wdt.mbn
restoredbl.mbn
failed to format log message
device info value: 
<%@: %@>
@SE2,Ticket
DMC,USBPDThunderboltFirmware
%s: Failed to fetch SSO token
'%@' not found in buildIdentity
BBTicket
Request Tags:
Failed to locate FTAB in super binary
filename : 
Alamo
rdc2
BbSkeyId
%s::%s: Tag %s doesn't exist -- continue...\n
getFileDataFromZip filePath: 
DMC,BaobabTCONTrinityCabalLUTs
outData
AMAuthInstallApCopyImageTag
AVISP1,ISP
ProductVersion
statusString is NULL
SBL1-HashTableBody
%s::%s: Using embedded ftab '%s'\n
Provisioning never started by BBUpdater, skipping for BB
~
%s::%s: setFwInfo failed delete vinylFirmware object\n
%s::%s: Unable to unzip the fwdata:\n
TagPrefix
boot.bbfw
fwData: 
excl
ap.ticket.8960.dev.cert
amai/LocalPolicy.recoveryOS.img4
%23
ERROR: Can't authenticate with provider URL: %@.
failed to finalize image3 override
AMAuthInstallSupportCopyFile
RestoreSBL1-PartialDigest
queryTags
_CFDictionarySetData
iBSS
provisioning ack failed, enabling force provisioning.
update/main/profile.bin
Personalization Security Mode
Missing kSEOptionSourceBundlePath
RecoveryOSAp,BaseSystemTrustCache
File not found
FactoryPostflight revision: 
failed to measure: restoredbl.mbn
tss_stitch_img3
Cellular1,BbActivationManifestKeyHash
%s::%s: failed to build parameters out of device identity\n
%s::%s: path has wrong type %lu\n
AMAuthInstallUpdaterCryptex1MobileAssetSetInfo
inputData is not of type CFDataRef
object is not a valid img4/im4p type
rampsi-stitch
%s: failed to create directory for %@: %d
%s::%s: Bad chip ID size\n
copyFirmware: failed to create personalized rooted FW URL
eUICCFwReaderOpen
failed to convert securityDomain
Failed to convert password
failed to extract bbfw item \"%@\": %@
Keep-Alive
SE,OSUPubKeyID
sha1
otherParameters
Cellular2,BbActivationBypassEnable
Size of UpdateTable.entries is zero
AMAuthInstallBasebandSetNonce
%s: failed to copy build variant
Cryptex1,PreauthorizationVersion
copyFirmware: rtkitos bundle data unavailable
createRequest: Failed to build parameters out of build identity
TssOverrides
%d
EUICCSignedProfileGold
Unknown
<%@: %u>
AMAuthInstallApImg4PersonalizeFile
failed to create debug output directory
failed secdomKey allocation
AMAuthInstallApImg4GetPayloadPropertiesData
Manifest.OS.Digest
failed to check %@ alignment
Cryptex1,DataOnly
componentName
%s: %@ in deviceInfo is invalid
entry \"%@\" has been previously personalized; skipping it
AP: already fully provisioned, sending ACK
Cryptex1,ExclaveLiveNonceDomain
%s: failed to set updater response tags, result=%d
%s::%s: initialization failure due to incomplete parameters\n
%s::%s: failed to get firmware object\n
%s::%s: Failed to alloc create plistFilePath CFString\n
Wireless1,Wifi2GLMACManuf
%s::%s: failed to find and/or copy data\n
inputData is NULL
baseband updater output: %@
mistyped vendorid
Action
Cellular1,ECID
SOCKS proxy port is NULL
euim
Not copying firmware to destination bundle
Could not find RTKitOS path
ERR
AMAuthInstallSsoCreateToken() OIDC token requested, status=%d.
build manifest lacks info for \"%@\"
RestorePSI-PartialDigest
Request not a dictionary
%s::%s: failed to add certId-VAD sequence\n
failed to convert TagPrefix %@
_AddToArchive
SourceURL
hw.machine
SBL1-HashTableDigest
Vinyl server signing is enabled...
SoftwareBinaryDsp1
BatteryCharging1
MBN qti_certificate_chain_size overflows file
value is NULL
Cellular2,LLB
AMAuthInstallBundleCopyFullPathForBuildIdentityKey
invalid img3
enable-transport-logs
ACIBT
SBL1-HashTableDigest-Blob
AMAuthInstallSupportWriteDataToFileURL
cncx
failed to add %@ image to the ticket body
failed to set calibration key hash
15531444804973541
Ap,
failed to open bbfw archive for writing
Firmware/%@/Rooted/ftab.bin
%s::%s: file data must be valid or firmware data must be provided\n
SepNonceSlotID
dstEncoder cannot be NULL
fuseAttemptSucceeded
mistyped has manifest boolean
%s::%s: savePath for FW not specified. This needs to be specified.\n
%s::%s: failed to copy file data\n
Provisioning
Cannot read CFNumber 
failed to add %@ data
AMAuthInstallApImg4LocalCreateEncodedCertificateChain
AMAuthInstallBasebandCreateServerRequestDictionary
RequestHeaderTags
Ap,AppleVideoEncoder0
_AMAuthInstallBundlePopulatePersonalizedBundle
kExpectedOEMCertChainSize == kOEMCertChainSize || 0 == kOEMCertChainSize
IMEI:%@
ACFUFile
%@,BoardID%@
setAuthPayload
failed to create ap ticket for recovery OS
NOT 64-BYTE MULTIPLE
Baseband not reporting manifest status, not attempting to provision yet.
_localsigning_named
CFURLCreateCopyAppendingPathComponent() failed
Ap,ApplePMCFirmware
tprd
CSEC
%@/manifest
Personalization Enable Mix Match
%s::%s: VinylUpdater Version: %s\n
, nonce=0x%@
replaced NULL response dictionary with cumulative response
reservationLength=0x%x, codeBytesHashed=0x%x (%s), downloadBytesHashed=0x%x (%s)
PermitNeRDPivot
Failed to create personalizationInfo with options: %@\n
WARNING: Note: This default behavior may change in the future into a hard error.
%s: failed to create url for %@-%@: %d
_FlsParserFinalize
DeviceInfo
Failed to parse ftab
expected outputDict as a dictionary
failed to copy personalized URL
ENANDPRG-Version
-[FTABFileOS initWithContentsOfURL:]
%@.plist
RestoreLogo
Ap,RestoreSecureM3Firmware
getPathFromBuildID
personalizing baseband only
postData allocation failed
%s::%s: tag is either larger or smaller than limit %u (size: %lu)\n
-[MantaFTABFile initWithContentsOfURL:]
} 
provisioning info: %@
invalid response
Unable to locate production status for tag %u
failed to create file from %@
could not get tbmr property, status:%d\n
Stashing %@ ticket(s) in bundle (LoopInstance=%@)
RoseUpdaterGetSharedInfo: failed to get dict entry for sbd1 digest
%s::%s: leaving: %s\n
IsX86
bat1
IsFTAB
dev
%s: amai->updaters is NULL
_AMAuthInstallVinylPersonalizeLegacyFirmwareInternal
I
%s: %@ in deviceInfo isn't data
AMAuthInstallApImg4AddBooleanProperty
customBbfwURL CFURLCreateWithFileSystemPath failed
User-Agent
Removing file at URL: 
IM4R
%s: failed to open file %@, error=%s
%s: %@
ap local signing keys available
world.fls
RestorePSI-Blob
%s::%s: failed to get dict entry\n
LeapBinsDigestsArray
entry \"%@\" has been previously personalized as part of \"%@\"; skipping it
encodedLength == 0: '%@'
PhyBlueTooth
%s::%s: Identified chip as R2\n
trbb
getData
Wireless1,PhyBlueToothLPM
Deserialized plist data is not a dictionary firmwarePlist: 
failed to set Bb entitlements
SE,ID
RoseUpdaterCopyFirmware
failed to stitch restore info to %@
defaultTag->copyValue != NULL
AMAuthInstallBasebandMAV20MeasureFirmware
failed to encode DER buffer
%s::%s: Failed to set manifest\n
postflight
rcio
ave4
RecoveryOSDiags
failed to stitch ticket data to file
%3F
AMAuthInstallSsoEnable
BbAntennaType
FlsParser.cpp
AMAuthInstallApImg4LocalAddImages
xbl_support.elf
BuildString
TPCU-DownloadDigest
%s::%s: failed to acquire ftab file header\n
%s::%s: Invalid Type of Updater Options dict\n
Wireless1,PhyBluetooth5GTrim
securityDomain
Failed copying %@ %d
chipID failed to convert to data
Bad partial digest length
Fail to allocate imageProps
Failed to parse as per DeliveryObjectItemSpec
%s::%s: fwSrcPath memory alloc failed\n
RelativeDestPath
_AMAuthInstallBundleSetBasebandFactoryDebugEnable
MBN segment components != size of ELF segment.
_FlsParserCopyInjectedItem
build identity value: 
setManifestOnData
%s::%s: cannot update tag '%s' because it does not exist\n
Unable to locate security mode for tag %u
Ap,ExclaveOS
attemptedToFuse
%@,ECID%@
Baobab,Trinity
failed to create key substring
IRXCoefficient-DownloadDigest
%s: failed to write %@ manifest
libDERErrorDomain
com.apple.EmbeddedSoftwareRestore.eUICC.firmwareMac
setting B64_SKEY_HASH failed
%s::%s: failed to allocate output dictionary\n
%s::%s: failed to create url from string\n
RestoreKernelCache
no response data (httpStatus=%u)
x86,SecurityMode
copyFirmwareContainer
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
_AMAuthInstallCryptex1GetDeviceInfoValue
AOP2
AMAuthInstallApFtabCreateMeasurementsWithTag
BNCH
%5D
://
FlsParserCopyRamPsi
pert
mistyped snum
RestoreBehavior
Found cached (dictionary) ticket at %@
AMAuthInstallBasebandWriteFilesToBbfw
%s::%s: failed to read zip file\n
%s::%s: failed to encode DER buffer\n
failed to set FDR entry in Ap request
update/main/info.plist
/update/main/ticket.der
CFStringGetCString failed.
RTP
this certid specifies local signing
overriding entry: %@
AMAuthInstallLog
failed to measure: RPCU.elf
%s: failed to get recoveryOS image file name
decoder != NULL
Error ReadStreamOpen
-[Ace3RestoreInfoFirmwareCopierOS firmwareKeyFromBuildIdentityDict:deviceInfo:]
Payload - 4cc <%@> - Version <%@> - TLVs - %@
AMAuthInstallBasebandGetRFSelfTestTicket
flashpsi-stitch
RestoreSBL1-HashTableDigest-Blob
RestoreSBL1-HashTableHeaderDefault
%s::%s: file is smaller than the ftab header size\n
Failed to create destination bundle firmware directory at '%@' (%@)
securityMode
AMAuthInstallGetLocalizedStatusString
could not remove info dicts from request
Ap,RestoreDCP2
failed to stitch manifest to file: %s
Personalize
MBN image_size overflows file
%s::%s: failed to initialize base class\n
Cannot found any matched delivery object
AppleConnect bad credentials
%s: unexpected restore property type
dfw1
ap parameters are not set
%s::%s: failed to get create firmwareInfoDict\n
%s::%s: Get Profile Data from Zip failed\n
DebugFW-HashTableDigest
Rose-SE Shared Info: 
%s: dict is NULL
Ap,NextStageIM4MHash
copyFWDataByName
Loaded credentials from keychain with status %d
SecItemUpdate ret=%d
Ap,ProductType
LocalSigningID
Out of memory
BoardID
response missing partial digest for \"%@\"
invalid img3 (tatsublob_len %d <= mastered_reservation_len %d
%s::%s: enable gid3En for rtkitos\n
eUICCFwReaderFindAndCopyFileData
getFileDataFromZip fwSrcPath: 
%s::%s: Unable to allocate memory for fullPath:\n
AMAuthInstallApImg3CopyPersonalizedData
%s: Found variant: %@
copyFirmware: failed to remove bundle fw personalized bits
%s::%s: failed to remove bundle fw personalized bits\n
AMAuthInstallSetFusingRootCA
_AMAuthInstallCopyFormattingDescription
%s failed to create DER file
AntCFG-HashTableDigest
Error IP address->string
eUICC,InfoPlistDataMain
krnl
value == NULL
failed to get username and password values
ssodata
Misc-DownloadDigest
server
%s::%s: failed to create host object\n
%s::%s: unmaping new length for page alignment (alignedLength: %zu. originalLength: %zu)\n
ant_cfg_data.elf
ping-attempts
\tSubfiles:\n
Wireless1,ScanBTLPEM
Cannot allocate for tmpData
failed to add payload type to DER file
%s::%s: failed to update file\n
Fail to parse MQR.data
SN300V3 (Eos v3)
calibration key hash not found
Options.plist
x-intnt-approductionmode
\trequestTags = %@\n
%s::%s: no write permissions to file... attempting to open file as read-only\n
ProductionUpdatePayloadHash
ApInRomDFU
%s::%s: failed to create mutable copy of source device firmware data dictionary (type: %hhu)\n
%s::%s: could not update ftab cache\n
%s::%s: firmware data has wrong type\n
setFwInfo
getTags
\tValid: %u\n
Wireless1,WiFiTxManuf
RestoreRamDisk
_AMAuthInstallGeneratePersonalizationEntries
-----------------------------------------------
ACFUFirmware
TrustObjectDigest
AMAuthInstallSupportCopyDataFromHexString
AMAuthInstallApApplyRequestRules
could not find im4p top level sequence
This is an install/stitch-only request.
%s: entry is NULL
Bbfw url: %@
%s::%s: failed to get file stats\n
AVISP1,Display
\\
copyFirmware: failed to init bundle firmware
,
AVISP1,LLB
Personalization SuperBinary AssetID
-[FTABFileOS addSubfileWithTagName:contentsOfURL:]
copyFirmware: rkos bundle data unavailable
%s: failed to finalize image
failed to copy build variant %d
%s: not match found for request tag %@
chipid: 0x%08X unsupported for img4 local signing
DBL-Version
%s::%s: unable to allocate data\n
wrong chip rev size
SystemLocker
BbFactoryActivationManifestKeyHash
ebl.bin
TestFirmware
openFileForRead
%s::%s: failed to add top-level sequence\n
failed to add payload to sequence
http://%@:%u
failed to stitch \"%@\": %@; continuing anyway
dsp1.mbn
DestURL
failed to find any usable references to \"%@\" in build manifest
AckFusingProgram
BT_MAC:%@
B64_SKEY_HASH
AMAuthInstallApImg4AddDataProperty
AMAuthInstallProvisioningProvisionIfNecessary failed
-[AMAuthInstallOSSsoAuthenticator authenticate]
Username not found
setManifestToTopOnData
gf1f
AMAuthInstallBasebandSetFusings
failed to convert statusNum
AMAuthInstallBundleAppendRecoveryOSiBootFirmwareEntriesToAssetArray
%s: failed to get AMAuthInstallUpdaterRef
\n------ Internal buffer is too small, truncating bytes! ------\n
outKeyHash is NULL
failed to measure: dbl.mbn
dstFtabUrl is NULL
createMainFw
ap
aop_devcfg.mbn
ObjectPayloadPropertyDigest
Misc-PartialDigest
%s::%s: invalid type for %s\n
requestDict after digest: 
Wireless1,ScanBTManuf
MantaMRI
Cryptex1,GenericVolume
%
eUICC,MainRecoveryFw
REQUEST_STRING
DeviceIdentityCreateClientCertificateRequest is not available
rsep
_WriteStreamIntoFile
CentauriRestoreHost
RecoveryOSAp,SystemVolumeCanonicalMetadata
RecoveryOSBaseSystemVolume
x-intnt-keyalg-hashmethod
%s::%s: file name does not exist\n
supportsRoseSEPairing
%s::%s: failed to add certId\n
AMAuthInstallUpdaterCryptex1LocalPolicyCopyFirmware
Failed to create option Dictionary for SSL connection!
received tss response (server version: %@)
Failed to read devicemap from %@
BBCFG-DownloadDigest
No boardID in options dict
AMAuthInstallApFtabIsValid
AMAuthInstallApImg3CopyRequestTag
PMP
NULL amai passed to AMAuthInstallBasebandApplyTssOverrides
%s: Mismatched Host Tools.  %@ Host support not found.  Please make sure you are running tools from an iOS train or one that matches your device.
%s::%s: no digest in build ID (%s)\n
%s::%s: cache is invalid\n
failed to merge build identities
Ap,UseGlobalSigning
%s: tagType is not supported
DERDecoderGetDataWithTag
/usr/lib/updaters/libAce3Updater.dylib
PSI2-Blob
Error InternetOpen
Wireless1,ECID
Failed to copy %@ to %@: %@
%s: failed to get username and password values
BundlePath
fileData is NULL
No nonce in options dict
\ttagName: %s\n
eUICC,BypassSEPPairing
AMAuthInstallBasebandGetKeyHash
g54xhr7fct39kf7ahbkys1sjhoymlz
AlternateUpdateBrainService
stitchData is NULL
AMAuthInstallSupportApplyDictionaryOverrides
\n%@\n
HelsinkiRestore-58.1.4
Failed to create propertylist from data, error: 
SDOM
RamPSI-PartialDigest
Test updater requested fake/empty ticket(s)
TSS/controller?action=2
AppleConnect user canceled
AOP
calibration key status not found
SBUserNotificationDontDismissOnUnlock
Personalization FTAB Payload Security Mode
Timer,ECID,%u
Fail to do AMSupportPlatformCopyURLWithAppendedComponent
RestoreAOP
failed to measure: osbl.mbn
%s: failed to copy build identity
preflash.bbfw
%s::%s: failed to add new file\n
copyFirmwareUpdater: bad device info parameters
failed to encode IMG4 string
bb.rembrandt.ticket.root
Cellular2,ChipID
%s::%s: setAuthPayload failed delete vinylFirmware object\n
checkVinylFwLdrVerLegacy
hashSectionTag argument is NULL
personalization area=0x%x
demote-prod-non-persistent
%s::%s: failed obtain file size\n
Ap,AppleVideoEncoder2
AMAuthInstallSupportCopySetValueForKeyPathInDict
%s::%s: Object initialized!\n
Unable to locate firmware data
Fail to parse Apdu]
eUICC,Im4pGold
You must authorize with the signing server before making this request
Manifest.%@
failed to measure: AudioFW.elf
%@%c%@
Cellular1,CdpAscDl
%s::%s: failed to init certification firmware\n
Ap,EngineeringUseOnlyUnit
fusing program type mismatch
%s: _AMAuthInstallSsoSUSSOCopyToken returned without ssodata
Missing element in updateTableEnry
AMAuthInstallApCopyDeviceEntryFromDeviceMap
diag
RecoveryMode
Ap,GFX1Firmware
Timer,RTKitOS,1
AMAuthInstallApImg4.c
BbfwWriterAddFile failed to add file: %@. Error code: %d
_AMAuthInstallBundleCreateAbridgedEntries
signing done
postString=%@
AMAuthInstallSupportGetValueForKeyPathInDict
Misc-HashTableHeaderDefault
psi_ram2.bin
Ap,CurrentOSSecurityVersion
%s::%s: ACFU Version: %s\n
ManifestPrefix
Ap,RecoveryOSPolicyNonceHash
AMAuthInstallBundleShouldPersonalizeOSImage
Failed creating dictionary for the version data.
Base64Encode failed
AMAuthInstallMonetMeasureEBootLoader
outEscapedValue == NULL
createNum32FromString
nonce
%s::%s: failed to get deviceInfoDict\n
failed chipKey allocation
Ap,RestorecL4
copyFirmware: updater failed to find firmware data with bundleURL
@Wireless1,Ticket
tagNumber
entry \"%@\" does not require personalization; skipping it
AMAuthInstallSupportCreateDataFromFileURL failed.
PL
%s::%s: VinylUpdaterCreateRequest  ACFUInitLog returning %d\n
/usr/lib/libauthinstall.dylib
TDSFW-HashTableDigest
Count of certID != hashVad
SinopeUpdaterCreateRequest
fDeviceInfo
Status
%s: user canceled AppleConnect login
failed to copy EBL
%s::%s: file is empty (file size: %zu)\n
missing amai
BpApBindingDigest
eUICC,Ticket
error from server=%d (%s)
ibdt
provisioning/manifest.bin
Could not find RTKitOS key in build identity dictionary
%s: could not create measurements: %d
failed to decode img4 payload, error:%d
rkof
setting (from PR2 document/Override): %@ = %@
%s::%s: manifestOffset: %u, manifestSize: %u\n
chipRev
%s::%s: Digest of manifest failed\n
boot nonce has wrong type
Bad response
DMC,HarmonyDB
Error gethostbyname
%@: options = %@
environmentIdentifier
CumulativeResponse
%s: unable to prepend entry name to path
RestoreSBL1-HashTableDigest
No data in partial digest
Wireless1,WiFiRx
%@,ChipID%@
%s::%s: failed to open bbfw archive for reading\n
_AMAuthInstallApCopyDeviceEntryFromProvidedDeviceMap
gtcd
RPM-HashTableDigest
%s::%s: failed to create file data\n
%s::%s: tag '%s' not found in device info, skipping validation\n
FTAB:\n
@Timer%u,Ticket
getFileDataFromZip fullPath: 
%s: measurementDict is NULL
%s: Requested ANY type, but UseSpecifiedTypesOnly is set.
IsLoadedByiBootStage1
skipping optional file...
com.apple.accessoryupdater.ftab
%s::%s: failed to create number\n
nsrv
could not measure %@
AMAuthInstallUpdaterCreateResponse
Failed to read file %@: error=%d
#
version=0x%x, personalizationOffset=0x%x
No path in request
Failed to parse firmware data
%s::%s: failed to get mainNonce\n
Firmware/device_map.txt
RestorePSI-DownloadDigest
%s: invalid %@ response tag %@
unknown chipID
%s::%s: failed due to incompatible bundle data dictionary\n
%s::%s: failed to open file (%s)\n
SE FW DEV Version
%s::%s: ldrVersStrArray count is zero\n
fileURL is NULL
acfw
CDMA2KFW-DownloadDigest
BatteryCharging0
RecoveryOSStaticTrustCache
Read error or stream too big
Unable to locate nonce for tag %u
_AMAuthInstallFinalize
ApEffectiveSecurityMode
Buttons1,ButtonsFirmware
CarrierID
InstanceB
%s::%s: failed to create request dict\n
Rap,SoftwareBinaryDsp1
missing build identity
lpbt
%7C
PAICHUSUO:%@
copyDirectData
csys
Img4PayloadType
no baseband chipid found in identity, but baseband returned snum. Can't preflight baseband personalization.
AMAuthInstallApEnableLocalPolicyHactivation
$s: failed to get tag buffer length
failed to measure: ENPRG.mbn
%s::%s: no chip rev\n
EuiccMainTicket
AVISP1,AudioLeft
Debug_info.elf
%@ (from build manifest) is not true. Not setting it
%s::%s: failed to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: failed to create manifest\n
applicationIdentifier
userAgentStringOverride
failed to create DER encoded buffer: sequenceEncoder
Ap,HapticAssets
AMAuthInstallBasebandSupportsLocalSigning
AMAuthInstallBasebandICE3MeasureModemStack
%s: failed to get tags
infoArray: %@\n
Unknown chipID in BLOB
%s: server request failed
%s::%s: file indicated is within header space\n
%s::%s: sbd1 digest is of an unexpected type\n
getRecoveryFwData
!
false
AppleConnect
EUICC,Ticket:
%s::%s: fwFileName %s\n
fwReaderInfoPlistCallback
SSO function returned NULL and no SSO token was provided, SSO disabled.
%s::%s: Restore boot nonce present!\n
gtgv
amai->apParameters->sepNonce is required for BAA request.
personalization
failed to set recovery entitlements
EUICCTicketVersion
%s: bbfwURL is NULL
interactivity
x-intnt-keyalg-keyscheme
Added bbfw file : %@
%s::%s: failed to obtain file data\n
Cannot parse SEFirmware.version.
FlashPSI PartialDigest: %@
ASAuthorizationErrorDomain
com.apple.libauthinstall
1.0
%s::%s: Manifest is not present in expected data type\n
%s::%s: failed to create data container\n
No chipID in options dict
VinylRestoreInfo
%s::%s: running host invoked restore info -- using bundleURL\n
AVISP1,TMU
syab
vinyl/update/gold/signedprofile.der
%@.%@.%@
%s::%s: copying preflighted rooted firmware into the dst bundle...\n
%s::%s: =========== FTAB Payloads ===========\n\n
Failed to get filePathSuffix
Error getaddrinfo
Ap,MinimumOSSecurityVersion
%s::%s: attempting to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
AMAuthInstallBundleCopyReceiptCreateIfNecessary
BbFieldDiagsEnable
No component name in options dict
AVISP1,DiagRTKitOS
%s: failed to allocate path
Cellular2,BbProvisioningEnable
RoseUpdaterGetSharedInfo: rkos digest is of an unexpected type
%s: request is NULL
ftap
AuthUserId
Path URL: 
SepStage1
setting (from build manifest): %@ = %@
AMAuthInstallHttpUriEscapeString
file lacks a hash section
Inserting %@ to Manifest to personalize later
Attempting to add additional entries to HTTP header
Personalization Suffix Needs Logical Unit Number
failed to encode manifest header
failed to create receipt directory: %@
buildIdentity is NULL
Data
Failed to create jmetMetadataSegmentData
Credentials not found
addNewFileToFTABOnData
File error
15439634935985085
entryName != NULL
%s::%s: failed to remove rooted fw personalized bits\n
FTAB contains no payloads
failed to set FDR entitlements
ih_buffer_len(%d) + 8 is not a multiple of %d
%s::%s: input data has no bytes\n
_AMAuthInstallApCreatePersonalizedResponseInternal
LLB
batF
chipID: 0x%x is not supported
0x%08x
100
_AMAuthInstallSupportCreateDataFromCopiedOrMappedFileURL
copyFirmware: failed to init certification firmware
cncn
Ap,InternalUseOnlySW
ApChipID
Ap,DebugCPUFirmware
mistyped manifestProvisioningKeyHash
failed to create key(%@) or value (%@)
LEGACY Server based provisioning enabled. Reading provisioning key from settings.
\tbuildIdentityTags = %@\n
Cellular2,BbFactoryDebugEnable
%s: %s\n %@\n
%60
failed to convert fusing program to xml %@
%s: failed to allocate updaterDict
Updater %@ requested %s signing.
   
devcfg.mbn
AP: provisioning server failed to respond, cannot provision.
AMAuthInstallRembrandtMeasureElf
stitchData is %lld, expected size is %d
Failed to close file in zip %s with error: %d %d
IsiBootNonEssentialFirmware
SBUserNotificationDisplayActionButtonOnLockScreen
Requested tag %@ not found in manifest, ignoring.
<FlsParser %p>
%s::%s: tag '%s' not found in identity dictionary, ignoring\n
imageProps is nullptr
%7E
lpda
AMAuthInstallBasebandJ2StitchFirmware
irx_coefficient.elf
AMAuthInstallSsoCreateToken() ACM token requested, status=%d.
httpStatus is %d
using SSO.
ANS
ap.ticket.localpolicy.hacktivation.key.private
Ap,EnableGroundhog
prettyLog
no fusing profile specified
%s::%s: reset epro to false for all firmware file tags\n
copyFirmware
<Type = 0x%08x, Length = 0x%08x>
v32@?0@\"NSMutableArray\"8@\"NSString\"16@\"NSString\"24
uefi.elf
Ap,OSLongVersion
server error: %d
eUICC,Main
failed to check conditions
```
