# `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 834,288 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 3376)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe
```

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,659)

```
sharedDataAccessor
copyPathForPersonalizedData:error:
localizedDescription
copyFirmware: failed to remove bundle fw personalized bits
%s::%s: failed to remove existing symlink: %d\n
%s::%s: startTimer - failed to create timer.\n
%s::%s: Failed to create empty trust object hash\n
validateDeviceId
%s::%s: failed to allocate http header dictionary\n
%s::%s: failed due to unexpected data type\n
%s::%s: %s: file incomplete: expected %u bytes, but received %u\n
%s::%s: failed to allocate string\n
%s::%s: failed to get stats for path: %d\n
%s::%s: event wait timeout\n
processOpenForWriteCommand
%s::%s: Failed to create CF number from int value\n
getVersion
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: failed to obtain reference of data from data container\n
getTagSizeFromHeader
%s::%s: function is not supported in memory optimized flow. Memory optimized files are read only\n
addNewFileToFTABOnData
initFromHeader
%s::%s: failed to create build ID key path\n
%s::%s: missing data classes in request\n
UseSOCKSPort
ACFUFirmware
%s: %s\n %@\n
getData
%s::%s: failed to determine if url exists (%u)\n
%s::%s: failed to modify firmware file\n
Certify
%s::%s: Invalid Type of Updater Options dict\n
%s::%s: CFType to be printed is NULL\n
FDR Trust Object Digest: 
%s::%s: Coredump region size is too large: %d\n
%s::%s: file does not have write permissions\n
createPeronalizedContentPath
%s::%s: item %s failed to log\n
%s::%s: rooted firmware was personalized already so we should use that to update\n
DSEC
RestoreHost
BinToHex
%s::%s: cache is invalid\n
%s::%s: failed to get byte pointer\n
%s::%s: manifest at the end - startOfManifest: %u, endOfFiles: %u, padding: %u\n
%s::%s: null acipcInterface\n
%s::%s: data type is not recognized\n
moveFileToTop
%s::%s: unknown command type %d\n
copyFDRTrustObjectDigest
performCmd
%s::%s: running custom updater step with id: %d\n
%s::%s: cancelTimer - canceling timer\n
Request Dictionary:
%s::%s: We have exhausted all our allowed attempts! Please file a radar!\n
stopOnQueue
%s::%s: failed to create ftab file path\n
%s::%s: failed to get data from local FDR data store\n
%s::%s: failed to get dict from local FDR data store\n
Path URL: 
%s::%s: using client prepared load image (assuming 4k alignment)\n
%s::%s: failed with error (ret: 0x%08x) (cookie: 0x%08x)\n
bootFirmware
%s::%s: invalid timeout callback\n
%s::%s: Adding new file to FTAB cache. File: %s, offset: %u, size: %u\n
,ChipID
%s::%s: skipping device identity validation against build identity\n
%s::%s: Invalid Type of DebugArgs\n
%s::%s: cowardly retreating because tag '%s' exists. I refuse to overwrite existing files!\n
ACFUDataAccess
%s::%s: key value not provided\n
%s::%s: Using embedded ftab '%s'\n
%s::%s: could not allocate data\n
%s::%s: beginning manifest offset mismatch: %u != %ld\n
ResponseTags
%s::%s: failed to create mutable data in unoptimized path\n
%s::%s: header is invalid\n
%s::%s: Requesting FDR trust object hash\n
%s::%s: failed to receive command from device, error: 0x%x\n
Trusted
%s::%s: failed to get dict entry\n
%s::%s: failed to create client ID\n
UseSOCKSHost
invalid command specified
%s::%s: Missing = for key: %s\n
%s::%s: This function has not been implemented\n
%s::%s: open (write only): %s\n
copyFirmware: updater failed to find firmware data with bundleURL
%s::%s: no conversion necessary\n
%@/
getRequiredFileSize
processReadCommand
Firmware/%@/Rooted/ftab.bin
copyFirmware: failed to get src bundle URL
%s::%s: failed to init ACFUMachO\n
%s::%s: failed to allocate direct data\n
APTicket
%s::%s: invalid file descriptor\n
BORKED
%s::%s: cache does not hold correct size for file %s. Cache size: %d. FTAB size: %d. Cache is invalid\n
%s -- middle of buffer snipped -- \n
Firmware Object: 
%s::%s: failed to find FW (%s) in build ID in personalized path\n
%s::%s: FATAL: no operation for queryCmd\n
%s::%s: failed to push firmware (%d)\n
%s::%s: manifest is at top - endOfManifest: %u, startOfFiles: %u, paddingAfterManifestEnd: %u\n
%s::%s: No manifest present\n
%s::%s: failed to perform preSave actions (%d)\n
createRequest: Production mode not present in device info. This is fatal!
%s::%s: Failed to create macho header data\n
%s::%s: cannot update a file if no files exist\n
%s::%s: invalid FTAB file\n
%s::%s: skipping trust error since FDR validation is disabled (Trust Error: 0x%016llx)\n
%s::%s: failed to allocate ouptut dictionary\n
copyFWContainer
%s::%s: Manifest Offset: %u, Manifest Length: %u, Magic: %s\n
%s::%s: file indicated is within header space\n
writeRegister
%s::%s: failed to process command from device\n
%s::%s: output NVRM allocation failure\n
%s::%s: ticket key must be provided\n
%s::%s: failed to obtain copy of manifest\n
_%cxf
%s::%s: failed to create BTI stage timer\n
sikPubKey.bin
%s::%s: failed to measure fw\n
%s::%s: startOfManifestUnaligned: %ld, startOfManifestAligned: %ld, paddingBeforeManifestStart: %u\n
%s::%s: TRACE EVENT ACFUTrace::kACFUTraceEventTransportInit: 0x%08x\n
createRequest
queryInfo
%s::%s: timer is already running\n
%s::%s: SHA512 failed\n
%s::%s: no manifest found in ftab\n
%s::%s: failed to create manifest data output\n
%s::%s: failed to create dictionary\n
%s::%s: paging in new length for page alignment (Requested: %zu. Aligned: %zu)\n
%s::%s: Invalid token: %s\n
%s::%s: manifest present in space allocated for header\n
%s::%s: device with board id 0x%04x does not support certification\n
%s::%s: failed to read boot nonce from firmware\n
%s::%s: configuring for FDR 1.0 certification\n
copyFirmwareContainer
%s::%s: Has valid boot nonce? %s\n
getTags: failed to create build identity tag list
DestBundlePath
ESEC
%s::%s: something went wrong, extra bytes in file\n
isValidFileData
%s::%s: Failed to set ftab validity\n
%s::%s: failed to process open command for read\n
%s::%s: failed to boot firmware (%d)\n
%s::%s: Invalid FDR trust object hash in updater options override\n
%s::%s: failed to retrieve security mode value\n
%s::%s: Firmware Version: %s\n
getFileOffsetByFileName
ACFU,FDRTrustObjectHash
%s::%s: failed to allocate options dictionary\n
%s::%s: Token: %s\n
%s::%s: timeout in RTI stage\n
%s::%s: failed to copy data to dstPathURL (status: %d)\n
%s::%s: unmaping new length for page alignment (alignedLength: %zu. originalLength: %zu)\n
%s::%s: failed to retain file data\n
%s::%s: failed to start BTI stage timer\n
%s::%s: could not find FW (%s) in build ID\n
%s::%s: updater has not initialized update steps\n
%s::%s: failed to create copy of file path\n
%s::%s: Chip Revision: 0x%s (%s)\n
%s::%s: Boot nonce set for FTAB. Boot nonce value: %llu\n
%s::%s: too many files specified or there are no files. Limit is %d. Num Files: %d\n
%s::%s: timeout in BTI stage\n
%s::%s: there is already a file trasfer in progress\n
Personalized Bundle FW URL: 
copyDirectData
%@\n
%s::%s: TRACE EVENT BEGIN ACFUTrace::kACFUTraceEventBTI: 0x%08x\n
%@/Diagnostics-%s-%u/
failed to create dictionary
%s::%s: data is of an unsupported type\n
copyParametersDictionary
,Nonce
%s::%s: failed to write to file\n
ACFUMachO32
%s::%s: SHA384 failed\n
%s::%s: failed to get header pointer\n
%s::%s: sig cert start falls before start of manifest\n
%s::%s: failed to perform update firmware (ret: %d)\n
%s::%s: data class %s not present in parent data class %s\n
%s::%s: =========== FTAB Header ===========\n\n
%s::%s: Failed to find firmware in restore options\n
certifyChip
%s::%s: failed to create file data\n
%s::%s: unable to allocate data\n
%s::%s: failed to create file transfer session\n
createRequest: esec data to boolean conversion failure
ACFU,RootedFW
createRequest: Failed to validate device identity tags
PostFDRSealing
%s::%s: empty file\n
%s::%s: function does not support memory optimization flow\n
%s::%s: could not obtain file data\n
ACFUFTABFile
%s::%s: failed to initialize RTKitROM object\n
remove
%s::%s: item %s logged successfully\n
%s::%s: reducing requested length %zu -> %zu\n
%s::%s: firmware to push is missing!\n
%s::%s: %s doesn't exist. Skipping...\n
%s::%s: failed to allocate dataIntance, dataClass, or parentDataClass\n
cfTypeDescription
%s::%s: failed to create dispatch queue\n
%s::%s: failed to get manifest, error: %d\n
%s
dumpToIOBuffer
%s::%s: We have completed all enabled restore steps!\n
CertifySikPub
%s::%s: requesting APTicket file path\n
%s::%s: Failed to get DebugArgs buffer\n
init_block_invoke
getCFError
getTags: failed to create response tag list
%s::%s: failed to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: Failed to init macho32\n
::
%s::%s: Security Mode: 0x%s\n
%s::%s: no file name specified\n
%s::%s: initialization failure due to incomplete parameters\n
%s::%s: failed to create mutable data in optimized path\n
%s::%s: failed obtain file size\n
updateTagWithData
%s::%s: TRACE EVENT END ACFUTrace::kACFUTraceEventBTI: 0x%08x\n
sikCSR.bin
%s::%s: firmware file dictionary not provided\n
FDR Validation Options
Query Command
getPathFromBuildID
%s::%s: failed to allocate certification URL\n
startTimer
copyFirmware: failed to create src rooted FW URL
%s::%s: Failed conversion: %s\n
%s::%s: failed to convert from number to data\n
%s::%s: failed to map file: (%s)\n
%s::%s: failed to acquire file path string\n
%s::%s: %s - trying to write to offset %u length %u, but file size is %u\n
%s::%s: file transfer session still not closed\n
%s::%s: failed to create response tag list\n
createRequest: wrong digest type
%s::%s: destination bundle was not specified, so we are skipping the copy step...\n
createMachoHeaderData
copyFirmware: failed to create personalized FW URL
%s::%s: failed to allocate debugPathToCreate\n
%s::%s: failed to handle FDR file\n
hexStringFromCFData
setManifest
%s::%s: Generation: %u, Valid: %u, BootNonce: 0x%08llx\n
%s::%s: failed to copy file header\n
%s::%s: Could not create a valid firmware from restore options (%d).\n
%s::%s: removing any personalized bits of bundle firmware\n
NVRAM variable data:
getLength
%@ (%lu)
%s::%s: fFirmwareFile has not been initialized.\n
updateFileInFTABOnData
%s::%s: Failed to set manifest\n
%s::%s: Populating underlying error\n
%s::%s: failed to initialize diagnostics object\n
getDictLocalCopy
getPrettyChipRevision
fileVersionLog
%s::%s: failed to send response to device error: 0x%x\n
%s::%s: failed to collect download metrics for %s\n
BundleDataDict
%s::%s: failed to get src bundle URL\n
createRequest: Failed to get build identity dict from options
%s::%s: invalid length value\n
%s::%s: Missing ECID\n
%s::%s: failed to get the required path\n
removeFileWithURL
%s::%s: file (%s) not available\n
%s::%s: failed to create build identity tag list\n
%@.%@.%@.%@
build identity value: 
,ChipRev
%s::%s: invalid destination size indicated\n
%s::%s: invalid firmware object when processing open (read) command\n
%s::%s: no debug log path provided by restore\n
x-fdr-metadata-ECID
%s::%s: invalid length\n
,SecurityMode
%s::%s: bad parameters\n
setBootNonce
%s::%s: =========== FTAB Payloads ===========\n\n
%s::%s: failed to convert from string to number\n
ACFUDataContainer
%s::%s: failed to save file (%d)\n
%s::%s: failed to send data to device error: 0x%x\n
%s::%s: TRACE EVENT BEGIN ACFUTrace::kACFUTraceEventRTI: 0x%08x\n
%s::%s: failed to decode manifest: %d\n
%s::%s: BTI stage completed successfully\n
%s::%s: size: %u, fWriteSegmentSize: %u, remains: %lld, offset: %u\n
%s::%s: copyFirmware: failed to create default FW URL, (status: %d)\n
A09
%s::%s: failed to create data\n
Update
%s::%s: configuring for FDR 2.0 certification\n
%s::%s: failed to allocate space for file object\n
%s::%s: failed to open file error: (%s)\n
%s::%s: Production Mode: 0x%s\n
%s::%s: UID Mode: 0x%s\n
0123456789ABCDEF
%s::%s: No error to log. All clear, move along now!\n
RestoreSystemPartition
%s-%s.bin
createFileDatafromFilePath
%s::%s: data exceeds local buffer size\n
processDoneCommand
copyManifestSigCert
copyDataFromFileDictionary
%s::%s: ACFU Version: %s\n
%s::%s: Failed to initialize base object\n
[
%s::%s: failed to create RTI stage timer\n
RestoreOptions
bti
%s::%s: Currently performing: %s\n
FDRAllowUnsealedData
failed to perform update firmware
%s::%s: bad data\n
%s::%s: failed to remove file (%u)\n
%s::%s: numberOfSections is 0\n
%s::%s: moving %s to top\n
prettyLog
%s %04zx  %s
%s::%s: failed to initialize file cache\n
%s::%s: invalid parameter (done)\n
%s::%s: no digest in build ID (%s)\n
%s::%s: failed: unsupported NV flags\n
%s::%s: creating symlink from %s -> %s\n
%s::%s: failed to boot firmware post update (%d)\n
openFirmwareInRestoreOptions
%s::%s: failed to copy ftab file header\n
%s::%s: failed to build parameters out of device identity\n
createRequest: Invalid FDR trust object hash in client updater override
%s::%s: failed to setup http header parameters (rngStatus: %d)\n
%s::%s: failed to get device info list\n
copyFirmware: failed to create personalized rooted FW URL
x-fdr-attestation
%s::%s: input data has no bytes\n
%s::%s: Unrecognized CF object!\n
%s::%s: length reservation requirements not met (max: %d, actual:%d)\n
ACFUROM
%s::%s: failed to get file stats\n
%s::%s: failed to init ACFUTransport\n
%s::%s: failed to process done command\n
%s::%s: failed to perform FDR certification\n
%s::%s: failed to allocate NVRM data\n
AP Ticket Path: 
%s::%s: failed to allocate strings to join array\n
%s::%s: Empty options dict\n
%s::%s: converting from data to number\n
%s::%s: There are more coredump regions than expected in the crashlog\n
createFromHeader
getTagOffsetFromHeader
%s::%s: failed to perform preBoot actions (%d)\n
Info
%s::%s: key '%s' not found\n
getFileSizeByFileName
processCloseCommand
com.apple.acfu.timer
%s::%s: failed to create new data\n
ACFUError
%s::%s: Fusing Config: %s\n
%s::%s: updater failed to find firmware data with bundleURL\n
populateDictFromIdentity
%s::%s: symlink name exists but is not a symlink: 0x%x\n
%s::%s: file is smaller than the ftab header size\n
%s::%s: Number of coredump sections available: %u\n
%s::%s: checksum: 0x%x\n
%s::%s: failed: too many nv items\n
%s::%s: bad parameter: inputs to function are invalid\n
%s::%s: no transport\n
%s::%s: ECID: 0x%s\n
%s::%s: query command is missing chip ecid, chipId, or boardId\n
%s::%s: failed to decode manifest property object (status: %d)\n
%s::%s: unexpected size for ChipID\n
%s::%s: Digest of manifest failed\n
isCacheValid
%s::%s: Failed to parse debugArgs\n
\n------ Internal buffer is too small, truncating bytes! ------\n
logLevel
%s::%s: failed to obtain data ref for %s at offset %u length %u\n
FDRUseEngineering
%s::%s: Empty DebugArgs\n
getTags
%s::%s: no coredump region in the crashlog\n
%s::%s: Current command %s!\n
%s::%s: Missing ChipID\n
%s::%s: Object initialized!\n
%s::%s: firmware data container is invalid\n
%s::%s: Chip major revision seems unreasonable: %d\n
%s::%s: received %u bytes data from device, fFileTransferSession->fileSize: %u\n
%s::%s: failed to collect sik public key (%d)\n
ACFURTKitROM
%s::%s: failed to create file data from file path (status: %u)\n
%s::%s: file name not specified\n
%s::%s: failed to start RTI stage timer\n
%s::%s: firmware is not present! Trying to find firmware from restore options...\n
%s::%s: running device invoked restore info -- using bundleData\n
%s::%s: attempting to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
ACFURestoreHost
%s::%s: invalid offset value\n
A12
%s::%s: cannot save data using optimized flow\n
validateDeviceInfoAgainstBuildIdentity
ACFUMachO
ACFUMachO64
%s::%s: paddingAfterManifestEnd %u bytes\n
EPRO
Invalid Command
%s::%s: tag is either larger or smaller than limit %u (size: %lu)\n
createArrayFromList
%s::%s: failed to init timer object\n
service
%s::%s: booting firmware one more time to make sure everything is good...\n
%s::%s: failed to build parameters out of build identity\n
perform
%s::%s: Operation finished successfully! Moving to next step if one exists for this updater! \n
%s::%s: Looking for '%s' with parent '%s'\n
%s::%s: no write permissions to file... attempting to open file as read-only\n
,RestoreBootNonce
%s::%s: attempting to delete file from cache that does not exist. File: %s\n
createRequest: epro data to boolean conversion failure
copyFWContainerFromOffset
%s::%s: failed to update manifest\n
%s::%s: no read or write permissions to file: (%s)\n
%s::%s: Invalid arguments to parseDebugArgs\n
measureFW
%s::%s: failed to initialize nv object\n
%s::%s: file is empty (file size: %zu)\n
%s::%s: endOfManifestUnaligned: %ld, endOfManifestAligned: %ld, paddingAfterManifestEnd: %u\n
RTKitFirmware
IM4M
x-fdr-client-id
Unknown
%s::%s: padding %ld byte(s) at the end of ftab\n
%s::%s: failed to process open command for write\n
%s::%s: failed to get manifest start\n
%s::%s: running host invoked restore info -- using bundleURL\n
%s::%s: could not add cal file into diagnostics\n
%s::%s: failed to create data container\n
%@/%@
copyFWDataByFileName
copyFirmware: failed to perform destination bundle copy of rooted firmware
%s::%s: Internal Build: %s\n
%s::%s: failed to create CFError object\n
%s::%s: failed to acquire firmware data from file path\n
copyFWDataByTag
%s::%s: command : type %d size %d seqnum %d option %d tag 0x%x offset %d length %d\n
%s::%s: failed to create full description for type ID %lu\n
%s::%s: savePath for FW not specified. This needs to be specified.\n
CopyAllowUnsealed
%s::%s: timer fired\n
%s::%s: FDR trust object override not required\n
Failed to collect preflight info
setData
%s::%s: failed to open file\n
%s::%s: failed to initialize base object\n
%s::%s: Key: %s not found while parsing debugArgs, but this is not error\n
%s::%s: could not collect bti download time data\n
failed to perform query step
%s::%s: manifestOffset: %u, manifestSize: %u\n
%s::%s: ticket key is of unsupported type\n
FDRSkipSealing
Signed Certificate: 
%s::%s: failed to reset chip (%d)\n
CertifyHeaders
%s::%s: Failed to save firmware to path\n
createRequest: Failed to create empty trust object hash
%s::%s: firmware not present to boot\n
%s::%s: invalid file data\n
%s::%s: could not update ftab cache\n
createRequest: no digest in build ID
com.apple.MobileSoftwareUpdate
addTagWithData
Request Tags:
%s::%s: tag '%s' not found in build identity, skipping validation\n
device info value converted: 
%s::%s: failed to retrieve security domain value\n
A00
%s::%s: %s already at top\n
%s::%s: failed to acquire cf data byte pointer\n
%s::%s: failed to format CFString\n
%s::%s: booting firmware...\n
failed to create data container. File path:
CertifyManifestSigCert
logParameters
/
%s::%s: failed to allocate data for personalized path\n
%s::%s: failed to create tag list from vector\n
ACFUDebugArgs
initCache
moveTagToTop
%s::%s: object does not hold any data\n
%Y-%m-%d-%H-%M-%S
collectDebugInfo
%s::%s: TRACE EVENT END ACFUTrace::kACFUTraceEventRTI: 0x%08x\n
%s::%s: failed to set the boot nonce (%d)\n
%s::%s: failed to open file (%s)\n
%s::%s: failed to obtain data ref\n
%s::%s: RTI stage completed successfully\n
getTags: failed to get device info list
createBoolFromData
executeCommand
%s::%s: failed to create directory to save firmware (status: %d)\n
%s::%s: invalid file %s with size 0\n
createURLByAppendingStrings
%s::%s: failed due to incompatible bundle data dictionary\n
%s::%s: Failed to allocate output dictionary\n
%s::%s: %s: 0x%s\n
%s::%s: failed to retrieve chip revision value\n
%s::%s: copyFirmware: failed to create src rooted FW URL\n
%s::%s: Failed to write some or all of data\n
%s::%s: SHA256 failed\n
%s::%s: File indicated is within header space\n
removeTag
%s::%s: invalid file mode for write\n
processCommandFromDevice
%s::%s: failed to remove bundle fw personalized bits\n
,SecurityDomain
%s::%s: failed to create firmware\n
Yes
%s::%s: Missing ChipRev\n
%s::%s: file data must be valid or firmware data must be provided\n
%s::%s: =========== FTAB Payloads ===========\n
error details: 
DeviceInfo
%s::%s: data length %ld is not within range\n
basic_string
GetCombined
%s::%s: cannot aquire reference for a memory optimized data container. Please use copyData() instead\n
%s::%s: didn't find requested tag\n
x-fdr-certification-type
%s::%s: %s\n
%s::%s: Failed to collect preflight info\n
%@/%@/
%s::%s: failed to initialize cache\n
%@/%s
combined
%s::%s: failed to create mutable copy of source device firmware data dictionary (type: %hhu)\n
%s::%s: starting timer\n
ACFUTimer
%s::%s: Chip minor revision seems unreasonable: %d\n
extractCoreDumpRegions
%s::%s: =========== FTAB Header ===========\n
%s::%s: Bad parameter\n
wait
%s::%s: tag '%s' not found in tss-request map, skipping validation\n
%s::%s: Failed to allocate buffer for macho header data\n
copy
%s::%s: failed to encode NVRM variable '%s'\n
v8@?0
%s::%s: boot nonce missing\n
No
%s::%s: no file path provided\n
setManifestToTopOnData
%s::%s: tag '%s' doesn't exist\n
%s::%s: failed: could not allocate variable\n
doesPathExist
setFirmwareNonce
generateBootNonce
createRequest: Invalid FDR trust object hash in updater options override
%s::%s: invalid command %d specified\n
%s::%s: failed to create mutable data\n
getVariableTypeFlag
%s::%s: failed to validate %s\n
createRequest: Failed to build parameters out of device identity
data container created. File path:
FATAL: no operation for performCmd
%s::%s: firmware data is invalid and does not meet ftab standards\n
%s::%s: failed to update cache\n
device info value: 
createNum64Num32FromData
%s::%s: failed to allocate dataIntance, dataClass\n
%s::%s: failed to create directory: %d\n
%s::%s: Manifest is not present in expected data type\n
%s::%s: Using FDR trust object hash in updater options override\n
%s::%s: Current step is complete. Moving onto the next restore step\n
%s::%s: overriding FDR trust object hash from restore options\n
fdr error: 
,ECID
%s::%s: number of files in cache is invalid\n
path: 
DPRO
%s::%s: invalid data, length value\n
%s::%s: firmware file failed to initialize\n
%s::%s: Handling %s\n
FDR Certification URL:
%s::%s: cowardly retreating because tag '%s' exists in runtime MMIO File Data. I refuse to overwrite existing files!\n
%s::%s: Invalid firmware file\n
updateFirmware
%s::%s: Using FDR trust object hash in client updater override\n
UNDEF
%s::%s: cannot setData for a memory optimized data container.\n
getFileSize
,ProductionMode
%s::%s: failed to create url from string\n
%s::%s: failed to update file data\n
%s::%s: header is bigger than the file\n
%s::%s: no manifest input provided\n
%s::%s: FATAL: no operation for performCmd\n
getFusingConfig
hashData
%s::%s: tag '%s' not found in device info, skipping validation\n
%s::%s: failed to get file system reprensetation\n
%s::%s: invalid tag map parameter\n
%s::%s: unexpected (too many) amount of bytes were sent to device, bailing\n
skipping removal of optional file...
ACFUCertUrl
%s::%s: failed to get board params (%d)\n
%s::%s: could not create URL to file\n
] 
%s::%s: failed to allocate output dictionary\n
%s::%s: key '%s' removed\n
%s::%s: failed: data buffer is empty\n
%s::%s: file path has not been initialized\n
%s::%s: failed with bad input parameters\n
ACFUSynchronize
%s::%s: invalid file mode for read\n
Provision
%s::%s: bad input file parameters\n
%s::%s: failed to get byte ptr\n
PreflightTickets
%s::%s: no file path provided.\n
%s::%s: startTimer - starting timer.\n
FDRBootedOSTrustObjectFile
%s::%s: Incomplete parameter set for certification (ret: %d)\n
build identity value converted: 
%s::%s: failed to allocate fDebugLogPath\n
FATAL: no operation for queryCmd
%s::%s: failed to get backing length\n
%s::%s: %s - trying to read from offset %u length %u, but file size is %u\n
Rooted FW URL: 
Certification Error: 
%s::%s: failed to acquire ftab file header\n
-- encoding error (%d) --
saveLogFile
%s::%s: get offset not supported on dynamically added file %s to MMIO optimized FTAB\n
%s::%s: Error Reason: %s, Error Code: 0x%08lx\n
%s::%s: Paged loading is disabled; sending all bytes of requested data in one segment\n
copyToPersonalizedBundlePath
~DirectDataRef
%s::%s: bad parameter!\n
%s::%s: removing file from FTAB cache. File: %s\n
%s::%s: unable to handle unexpected input parameters\n
%s::%s: copying preflighted rooted firmware into the dst bundle...\n
%s::%s: failed to get AP ticket\n
DebugLogPath
%s::%s: failed to acquire file path c string\n
%s::%s: no fw for tag '%s'\n
removeFileFromFTAB
%s::%s: event notification\n
%s::%s: failed to process close command\n
%s::%s: function cannot directly manipulate file data with optimized flow\n
%s::%s: failed to process read command\n
%s::%s: failed to validate device identity tags\n
createRequest: Failed to build parameters out of build identity
%s::%s: FDR Trust Result: 0x%016llx\n
%s::%s: received %u bytes (total: %u)\n
%s::%s: [%s] Performing iteration %d of %d\n
%s::%s: Failed to get value for: %s, exception: %s\n
%s::%s: failed to get stats for symlink name: %d\n
%s::%s: Didn't find a matching embedded ftab\n
setManifestOnData
%s::%s: invalid parameter (acipcInterface)\n
%s::%s: unknown command option %d\n
%s::%s: stopping timer\n
%s::%s: failed to copy ftab header\n
createRequest: could not find FW in build ID
PreflightContext
%s::%s: Assuming updater options dictionary is being passed\n
%s::%s: Failed to save packaged firmware file\n
updateCache
com.apple.AppleConvergedFirmwareUpdater
loadImageOnBTIStage
startOnQueue
%s::%s: Failed to allocate measurements dict\n
logError
%s::%s: unexpected (too many) amount of bytes were received from device, bailing\n
ACFUACIPCTransport
%s::%s: failed to get string\n
%s::%s: failed to get board parameters (%d)\n
%s::%s: bad input parameters\n
saveFirmware
%s::%s: manifest data has no bytes\n
%s::%s: attempting to add new file to cache, but not both size and offset are provided. File: %s\n
%s::%s: failed to create path to firmware directory\n
convertCFType
%s::%s: converting from string to number\n
%s::%s: failed to increase file length: (%s)\n
%s::%s: size: %u, remains: %lld\n
%s::%s: failed to convert from data to boolean\n
performNextStage
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: file data was invalid\n
%s::%s: cache does not hold correct offset for file %s. Cache offset: %d. FTAB offset: %d. Cache is invalid\n
%s::%s: Invalid FDR trust object hash in client updater override\n
%s::%s: failed to obtain file data\n
%s::%s: manifest existing in FTAB is being deleted\n
%s::%s: could not remove file entry from ftab cache\n
%s (snipped)\n
sikManifestSigCert.bin
%s::%s: allowing unsealed FDR data\n
%s::%s: failed to determine variable type\n
%s::%s: failed to ping device after firmware push (%d)\n
%s::%s: security mode not present in device info. This is fatal!\n
%s::%s: converting from data to boolean\n
%s::%s: cowardly retreating since overwrite was not requested\n
getDataLocalCopy
%s::%s: Missing NonceHash\n
%s::%s: file '%s' does not exist\n
%s::%s: processRTIStage - null acipcInterface\n
handleFDR
%s::%s: cache does not have entry for file %s. Cache is invalid\n
copyData
%s::%s: Missing SecurityDomain\n
%s::%s: BoardID: 0x%s\n
%s::%s: path exists but is not a directory: 0x%x\n
r
%s::%s: boot nonce is not present post boot. This is a failure.\n
%s::%s: failed: header length check validation failed\n
saveToPath
copyFWDataByName
%s::%s: firmware downloading finished successfully\n
%s::%s: sig cert start falls after end of manifest\n
getTags: failed to allocate output dictionary
%s::%s: failed to allocate bundle firmware path dictionary (type: %hhu)\n
parseDebugArgs
%s::%s: failed to change directory permissions: %d\n
%s::%s: no firmware file provided\n
%s::%s: failed to add new file\n
removeManifestPadding
%s::%s: copying preflighted bundle firmware into the dst bundle...\n
%s::%s: looking for AP ticket in updater options dictionary\n
[%s] 
%s::%s: failed to get manifest length\n
%s::%s: esec data to boolean conversion failure\n
%s::%s: unrecognized action %hhu\n
ACFUFDR
%s::%s: Manifest is not available\n
copyFirmware
skipping copying of optional file...
TrustObjectDigest
%s::%s: crashLogBuffer is null\n
createDataFromType
-
%s::%s: failed to create manifest\n
%s::%s: close: %s\n
%s::%s: failed to allocate source bundle firmware path dictionary (type: %hhu)\n
%s::%s: read less bytes than required (read: %zu, required: %zu)\n
createRequest: Security mode not present in device info. This is fatal!
%s::%s: wrong digest type (%s)\n
init
createSymlink
%s::%s: open file %s, received request for file %s\n
%s::%s: tag '%s' not found in identity dictionary, ignoring\n
%s::%s: failed to write data to output URL (%d)\n
%s::%s: failed to compute required size\n
%s::%s: failed to get firmware root path\n
%s::%s: failed to obtain file container\n
skipping optional file...
queryCmd
openFileForRead
%s::%s: no data to log\n
%s::%s: Chunking image using paged loading\n
ACFUDiagnostics
%s::%s: %s - attempting to write more bytes (%u) than initially indicated (%u), bailing\n
%s::%s: failed to create debug directory (status: %d)\n
%s::%s: Missing MinEpoch\n
A06
%s::%s: firmware file is invalid\n
%s::%s: path has wrong type %lu\n
%s::%s: length: %u, fReadSegmentSize: %u, remains: %lld, offset: %u\n
%s::%s: attempting copyFirmwareUpdater again with source bundle file map\n
%s::%s: failed to allocate extra options dictionary\n
%s::%s: cannot update tag '%s' because it does not exist\n
%s::%s: failed to allocate data\n
ACFULogging
%s::%s: file name does not exist\n
setFTABValidity
%s::%s: requesting personalized firmware root path\n
,MinEpoch
%s::%s: invalid file transfer session\n
%s::%s: failed: bad input parameter\n
%s::%s: failed: max length reservation is not equal to the data buffer\n
BootedOS
%s::%s: ChipID: 0x%s\n
map::at:  key not found
copyFirmware: failed to find FW in personalized path
%s::%s: failed to overwrite file (%d)\n
BuildIdentity
%s::%s: failed to create symlink: %d\n
%s::%s: file name is empty\n
%s::%s: failed to init data container object\n
copyFirmware: failed to remove rooted fw personalized bits
%s::%s: failed to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
%s::%s: paddingBeforeManifestStart %u bytes\n
%s::%s: file data has no bytes\n
%s::%s: failed to aquire ftab file header\n
embeddedFTABFilenamesForChipRevision
gatherPersonalizationParameters
%s::%s: failed obtain new file data\n
%s::%s: Security Domain: 0x%s\n
%s::%s: failed to reinit cache\n
%s::%s: invalid file open mode\n
%s::%s: Applying FDR trust object hash override\n
getBootNonce
%s::%s: specified tag name is invalid! Tag name: %s\n
createRequest: Failed to allocate output dictionary
%s::%s: optional tag %s missing from build identity, skipping\n
%s::%s: destination path does not exist after creation attempt (status: %d)\n
%s::%s: failed to get AP ticket path\n
ACFURestore
ACFUCommon
%s::%s: Wrote %zu of %zu bytes to %s\n
%s::%s: Missing UID_MODE\n
%s::%s: Minimum Epoch: 0x%s\n
%s::%s: failed to get length\n
saveFirmwareToPath
Incomplete parameter set for certification
processWriteCommand
%s::%s: failed to create personalized rooted FW URL (status: %d)\n
%s::%s: unsupported conversion: desired type %s, received type %s\n
x-fdr-request-uuid
writeData
,UID_MODE
%s::%s: failed to save firmware (%d)\n
%s::%s: copyFirmware: failed to find FW (%s) in build ID\n
Path
logFirmwareVersion
%s::%s: Num Files: %u\n
processRTIStage
%s::%s: startTimer - null timeoutCB.\n
ticket.der
No certification URL found for certification step
%s::%s: performing certification...\n
Perform Command
%s::%s: Looking for '%s'\n
%s::%s: failed to initialize\n
%s::%s: could not determine requested path\n
personalizedURL: 
%s::%s: CoredumpRegions version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: ftab cache entry updated. File: %s, offset: %u, size: %u\n
%s::%s: running generic updater step\n
%s::%s: failed to create path url\n
ACFUFile
%s::%s: payload is out of valid range\n
cancelTimer
x-fdr-metadata-ChipID
%s::%s: failed to decode manifest object (status: %d)\n
%s::%s: first file offset mismatch: %u < %ld\n
BundlePath
%s::%s: failed to format object into string\n
%s::%s: failed to create CFString for error object\n
%s::%s: Missing BoardID\n
createMutableFileDatafromFilePath
%s::%s: Found updater options in dictionary\n
%s::%s: open (read only): %s\n
logACFUConfig
%s::%s: unexpected size for ECID\n
%s::%s: parsing error while extracting the coredump regions. crashlog size: %zu offset and section size: %lu\n
add
%s::%s: failed to setup diagnostics\n
%s::%s: No manifest provided with firmware. Manifest is required!\n
%s::%s: failed to get build identity dict from options\n
%s::%s: failed to extract coredump regions\n
log
%s::%s: file i/o error (code: %d)\n
%s::%s: Manifest digest\n
%s::%s: file data provided is not valid\n
%s::%s: Failed to init macho64\n
%s::%s: Post Sealing: %s\n
%s::%s: failed to obtain file stats: (%s)\n
%s::%s: Boot Nonce Hash: 0x%s\n
%s::%s: failed to create output URL\n
%s::%s: failed to retrieve production mode value\n
copyFWRefByName
%s::%s: no manifest\n
BootedUpdate
%s::%s: unexpected debug log path type\n
%s::%s: Missing BootNonce\n
%s::%s: no file data?!\n
%s::%s: Cached Ticket: %s\n
%s::%s: manifest (%s) not available\n
Generic
copyFirmware: failed to find FW
%s::%s: failed to create destination path URL (status: %d)\n
%s::%s: command not supported in preflight mode\n
%s::%s: Missing SecurityMode\n
%s::%s: failed to copy type description for type ID %lu\n
copyFWDataRefByFileName
%s::%s: No manifest key specified\n
com.apple.acfu.acipcTransport
readRegister
%s::%s: tag '%s' has different values in device info and build identity\n
%s::%s: Preflight: %s\n
%s::%s: failed to append strings together\n
%s::%s: ftab cache had entries before ftab container was initialized. Clearing cache before moving on.\n
%s::%s: Unexpected value: %u for Key: %s\n
%s::%s: production mode not present in device info. This is fatal!\n
%s::%s: tag '%s' not found in tss-request map, ignoring\n
%s::%s: failed to allocate data object to write\n
ACFU,FDRAllowUnsealed
component
%s::%s: failed to create dispatch timer object\n
%s::%s: sent %u bytes (total: %u)\n
%s::%s: failed to remove rooted fw personalized bits\n
%s::%s: CFData to CFBoolean conversion failure\n
,BoardID
%s::%s: tag %s missing from firmware, skipping\n
%s::%s: offset out of range\n
FirmwareData
%s::%s: failed to perform destination bundle copy of rooted firmware\n
%s::%s: removing any personalized bits of rooted firmware\n
%s::%s: bad parameter: there is no data in the container\n
%s::%s: We ran into some issues on try %d of %d!\n
%s::%s: failed to create url from string.\n
%s::%s: file does not exist\n
hasFile
BuildIdentityTags
%s::%s: copyFirmware: failed to create personalized FW URL (status: %d)\n
copyFirmwareNonce
%s::%s: Invalid save path\n
%s::%s: debug log path does not exist\n
%s::%s: invalid timeout value\n
copyManifest
%s::%s: Payload is out of valid range\n
Options
%s::%s: failed to perform query step (ret: %d)\n
%s::%s: Tag: %s :: Offset: 0x%04x Raw address: 0x%lx, size: %u\n
%s::%s: required size %llu\n
processOpenForReadCommand
%s::%s: failed to create directory @ dstPathURL (status: %d)\n
%s::%s: failed to determine file size for path '%s' (%s)\n
%s::%s: sent %u bytes data to device, fFileTransferSession->fileSize: %u\n
%s::%s: attempting to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
%s::%s: desired type %s, received type %s\n
%s::%s: failed to perform certification\n
%s::%s: Failed to measure firmware\n
%s::%s: header only validation unsupported with optimized data\n
initLog
%s::%s: invalid timeout callback parameter\n
%s::%s: failed to send response to device error: 0x%x\n\n
createNum32FromString
%s::%s: failed to get formatted C string\n
FDRTrustObjectFile
%s::%s: failed to unmap file: (%s)\n
%s::%s: specified tag name is invalid!\n
%s::%s: Looks like there is no error present; Nothing to be done here.\n
create
ACFURTKitNVRMGenerator
%s::%s: No save path specified\n
createPersonalizedFirmwarePath
copyFirmware: updater failed to find firmware data with bundleData
copyFirmware: failed to create default FW URL
Digest
%s::%s: epro data to boolean conversion failure\n
%s::%s: Wrong type, expected dict\n
%s::%s: client sik pubkey must be set for FDR 2.0 certification\n
%s::%s: invalid optimization mask\n
copyManifestRef
%s::%s: failed to update file\n
%s::%s: bad parameter: options %p, domain %p\n
%s::%s: failed: NVRM allocation failure\n
createFileDataContainer
%s::%s: Wrong type, expected data\n
%s::%s: Missing ProductionMode\n
 
%s::%s: no manifest preset in dataref\n
%s::%s: failed to allocate internal data structure\n
raw
%s::%s: Failed to open firmware in restore options\n
%s::%s: padding of %zu bytes required\n
vector
%s::%s: We are finished with all the update steps! ^_^\n
%s::%s: Boot Nonce: 0x%s\n
%s::%s: manifest present beyond the bounds of the file data\n
%s::%s: Booted Update: %s\n
%s::%s: failed to un-map file: (%s)\n
_%c%cf
%s::%s: This step is not enabled... setting to DONE and moving along.. \n
CopyAllowRawData
%s::%s: timer is not initialized\n
ftab.bin
%s::%s: failed to allocate hash digest\n
%s::%s: ---- Restore State ----\n
%s::%s: wrong type, expected dict\n
Removing file at URL: 
%s::%s: failed to collect sik csr blob (%d)\n
Failed to perform certification step
%s::%s: failed to copy file data\n
%s::%s: fatal error with exception: %s\n
%s::%s: Successfully gathered personalization parameters\n
x-fdr-metadata-BoardID
%s::%s: file not open\n
createRequest: failed to allocate internal data structure
handleMessageCFType
%s::%s: failed to receive data from device, error: 0x%x\n
%s::%s: invalid sig cert length\n
RestoreInternal
%s::%s: no dataref\n
%s::%s: could not find firmware in restore options (%d)\n
%s::%s: updater failed to find firmware data with bundleData\n
%s::%s: file name is empty\n
%s::%s: failed to get board parameters (%d)\n
%s::%s: failed to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: Missing SecurityDomain\n
%s::%s: could not obtain file data\n
%s::%s: invalid timeout callback parameter\n
%s::%s: failed to process command from device\n
%s::%s: unable to allocate data\n
%s::%s: padding %ld byte(s) at the end of ftab\n
%s::%s: failed to update cache\n
%s::%s: command : type %d size %d seqnum %d option %d tag 0x%x offset %d length %d\n
%s::%s: converting from data to number\n
%s::%s: requesting APTicket file path\n
%s::%s: Bad parameter\n
%s::%s: failed to send response to device error: 0x%x\n
%s::%s: failed to ping device after firmware push (%d)\n
%s::%s: failed to get dict entry\n
%s::%s: failed to determine file size for path '%s' (%s)\n
%s::%s: BoardID: 0x%s\n
%s::%s: failed to create url from string.\n
%s::%s: function is not supported in memory optimized flow. Memory optimized files are read only\n
%s::%s: event wait timeout\n
%s::%s: size: %u, remains: %lld\n
%s::%s: unrecognized action %hhu\n
%s::%s: fatal error with exception: %s\n
%s::%s: firmware is not present! Trying to find firmware from restore options...\n
%s::%s: Using FDR trust object hash in client updater override\n
%s::%s: debug log path does not exist\n
%s::%s: close: %s\n
%s::%s: no conversion necessary\n
%s::%s: failed to initialize nv object\n
%s::%s: firmware not present to boot\n
%s::%s: manifestOffset: %u, manifestSize: %u\n
%s::%s: failed to create firmware\n
%s::%s: failed to allocate string\n
%s::%s: bad parameter: inputs to function are invalid\n
%s::%s: failed to get AP ticket\n
%s::%s: running custom updater step with id: %d\n
%s::%s: file name not specified\n
%s::%s: tag '%s' doesn't exist\n
%s::%s: manifest present beyond the bounds of the file data\n
%s::%s: failed to build parameters out of build identity\n
%s::%s: failed to allocate options dictionary\n
%s::%s: cowardly retreating because tag '%s' exists. I refuse to overwrite existing files!\n
%s::%s: RTI stage completed successfully\n
%s::%s: event notification\n
%s::%s: ticket key is of unsupported type\n
%s::%s: offset out of range\n
%s::%s: failed to obtain reference of data from data container\n
%s::%s: manifest existing in FTAB is being deleted\n
%s::%s: failed to process close command\n
%s::%s: unmaping new length for page alignment (alignedLength: %zu. originalLength: %zu)\n
%s::%s: number of files in cache is invalid\n
%s::%s: unexpected (too many) amount of bytes were received from device, bailing\n
%s::%s: sig cert start falls after end of manifest\n
%s::%s: failed to allocate fDebugLogPath\n
%s::%s: Firmware Version: %s\n
%s::%s: failed to create directory to save firmware (status: %d)\n
%s::%s: failed to perform FDR certification\n
%s::%s: copyFirmware: failed to find FW (%s) in build ID\n
%s::%s: FDR trust object override not required\n
%s::%s: %s doesn't exist. Skipping...\n
%s::%s: failed to acquire file path c string\n
%s::%s: failed to create path url\n
%s::%s: failed to allocate space for file object\n
%s::%s: fFirmwareFile has not been initialized.\n
%s::%s: Failed to measure firmware\n
%s::%s: empty file\n
%s::%s: failed to create copy of file path\n
%s::%s: invalid destination size indicated\n
%s::%s: first file offset mismatch: %u < %ld\n
%s::%s: Failed to parse debugArgs\n
%s::%s: invalid file open mode\n
%s::%s: failed to get manifest length\n
%s::%s: skipping device identity validation against build identity\n
%s::%s: epro data to boolean conversion failure\n
%s::%s: bad input file parameters\n
%s::%s: size: %u, fWriteSegmentSize: %u, remains: %lld, offset: %u\n
%s::%s: booting firmware one more time to make sure everything is good...\n
%s::%s: %s: 0x%s\n
%s::%s: path has wrong type %lu\n
%s::%s: failed to copy data to dstPathURL (status: %d)\n
%s::%s: tag '%s' not found in build identity, skipping validation\n
%s::%s: failed to extract coredump regions\n
%s::%s: failed to get stats for symlink name: %d\n
%s::%s: no manifest input provided\n
%s::%s: open (write only): %s\n
%s::%s: failed to format object into string\n
%s::%s: bad parameter: there is no data in the container\n
%s::%s: Missing ChipID\n
%s::%s: sent %u bytes data to device, fFileTransferSession->fileSize: %u\n
%s::%s: initialization failure due to incomplete parameters\n
%s::%s: failed to initialize RTKitROM object\n
%s::%s: endOfManifestUnaligned: %ld, endOfManifestAligned: %ld, paddingAfterManifestEnd: %u\n
%s::%s: ftab cache had entries before ftab container was initialized. Clearing cache before moving on.\n
%s::%s: Failed to find firmware in restore options\n
%s::%s: failed to modify firmware file\n
%s::%s: Failed to init macho64\n
%s::%s: FDR Trust Result: 0x%016llx\n
%s::%s: configuring for FDR 2.0 certification\n
%s::%s: failed to retain file data\n
%s::%s: Failed to set ftab validity\n
%s::%s: failed to get build identity dict from options\n
%s::%s: Invalid FDR trust object hash in updater options override\n
%s::%s: CFData to CFBoolean conversion failure\n
%s::%s: file i/o error (code: %d)\n
%s::%s: Didn't find a matching embedded ftab\n
%s::%s: failed to add new file\n
%s::%s: Key: %s not found while parsing debugArgs, but this is not error\n
%s::%s: data type is not recognized\n
%s::%s: overriding FDR trust object hash from restore options\n
%s::%s: failed to overwrite file (%d)\n
%s::%s: Payload is out of valid range\n
%s::%s: processRTIStage - null acipcInterface\n
%s::%s: failed to allocate data for personalized path\n
%s::%s: failed: could not allocate variable\n
%s::%s: no debug log path provided by restore\n
%s::%s: read less bytes than required (read: %zu, required: %zu)\n
%s::%s: bad data\n
%s::%s: failed to create full description for type ID %lu\n
%s::%s: TRACE EVENT BEGIN ACFUTrace::kACFUTraceEventBTI: 0x%08x\n
%s::%s: failed: unsupported NV flags\n
%s::%s: Missing UID_MODE\n
%s::%s: timer fired\n
%s::%s: header only validation unsupported with optimized data\n
%s::%s: failed to boot firmware (%d)\n
%s::%s: specified tag name is invalid! Tag name: %s\n
%s::%s: invalid file mode for read\n
%s::%s: key '%s' removed\n
%s::%s: Fusing Config: %s\n
%s::%s: paddingBeforeManifestStart %u bytes\n
%s::%s: cannot update a file if no files exist\n
%s::%s: TRACE EVENT END ACFUTrace::kACFUTraceEventBTI: 0x%08x\n
%s::%s: no digest in build ID (%s)\n
%s::%s: tag '%s' not found in identity dictionary, ignoring\n
%s::%s: failed to perform query step (ret: %d)\n
%s::%s: Failed to initialize base object\n
%s::%s: updater has not initialized update steps\n
%s::%s: failed to get backing length\n
%s::%s: failed obtain new file data\n
%s::%s: Production Mode: 0x%s\n
%s::%s: failed to create mutable data\n
%s::%s: Unexpected value: %u for Key: %s\n
%s::%s: invalid sig cert length\n
%s::%s: object does not hold any data\n
%s::%s: no file data?!\n
%s::%s: failed to acquire ftab file header\n
%s::%s: payload is out of valid range\n
%s::%s: Chip minor revision seems unreasonable: %d\n
%s::%s: copyFirmware: failed to create default FW URL, (status: %d)\n
%s::%s: unsupported conversion: desired type %s, received type %s\n
%s::%s: failed to map file: (%s)\n
%s::%s: Missing NonceHash\n
%s::%s: failed to create dispatch queue\n
%s::%s: Digest of manifest failed\n
%s::%s: invalid file mode for write\n
%s::%s: failed to process done command\n
%s::%s: failed to read boot nonce from firmware\n
%s::%s: failed to save firmware (%d)\n
%s::%s: failed to process read command\n
%s::%s: failed to acquire file path string\n
%s::%s: Missing BoardID\n
%s::%s: invalid timeout value\n
%s::%s: file data was invalid\n
%s::%s: %s\n
%s::%s: Number of coredump sections available: %u\n
%s::%s: failed to retrieve production mode value\n
%s::%s: Invalid Type of Updater Options dict\n
%s::%s: failed to copy type description for type ID %lu\n
%s::%s: header is invalid\n
%s::%s: could not allocate data\n
%s::%s: didn't find requested tag\n
%s::%s: beginning manifest offset mismatch: %u != %ld\n
%s::%s: failed to start RTI stage timer\n
%s::%s: failed to allocate data object to write\n
%s::%s: invalid data, length value\n
%s::%s: failed to create directory: %d\n
%s::%s: failed to remove existing symlink: %d\n
%s::%s: tag is either larger or smaller than limit %u (size: %lu)\n
%s::%s: sent %u bytes (total: %u)\n
%s::%s: failed to allocate internal data structure\n
%s::%s: data length %ld is not within range\n
%s::%s: invalid command %d specified\n
%s::%s: Cached Ticket: %s\n
%s::%s: failed to handle FDR file\n
%s::%s: no firmware file provided\n
%s::%s: %s: file incomplete: expected %u bytes, but received %u\n
%s::%s: length: %u, fReadSegmentSize: %u, remains: %lld, offset: %u\n
%s::%s: Could not create a valid firmware from restore options (%d).\n
%s::%s: desired type %s, received type %s\n
%s::%s: cowardly retreating since overwrite was not requested\n
%s::%s: no read or write permissions to file: (%s)\n
%s::%s: cache does not hold correct size for file %s. Cache size: %d. FTAB size: %d. Cache is invalid\n
%s::%s: Error Reason: %s, Error Code: 0x%08lx\n
%s::%s: updater failed to find firmware data with bundleURL\n
%s::%s: cannot setData for a memory optimized data container.\n
%s::%s: failed to send data to device error: 0x%x\n
%s::%s: Coredump region size is too large: %d\n
%s::%s: failed to obtain file stats: (%s)\n
%s::%s: Missing ProductionMode\n
%s::%s: Boot Nonce Hash: 0x%s\n
%s::%s: Object initialized!\n
%s::%s: failed to reinit cache\n
%s::%s: no manifest preset in dataref\n
%s::%s: Failed to save packaged firmware file\n
%s::%s: failed to find FW (%s) in build ID in personalized path\n
%s::%s: could not find FW (%s) in build ID\n
%s::%s: failed to get AP ticket path\n
%s::%s: failed to allocate http header dictionary\n
%s::%s: failed to create ftab file path\n
%s::%s: could not update ftab cache\n
%s::%s: invalid FTAB file\n
%s::%s: failed to create file transfer session\n
%s::%s: startTimer - failed to create timer.\n
%s::%s: copying preflighted rooted firmware into the dst bundle...\n
%s::%s: failed: too many nv items\n
%s::%s: failed to get formatted C string\n
%s::%s: failed to allocate debugPathToCreate\n
%s::%s: FATAL: no operation for queryCmd\n
%s::%s: unable to handle unexpected input parameters\n
%s::%s: unexpected size for ECID\n
%s::%s: invalid timeout callback\n
%s::%s: Looking for '%s' with parent '%s'\n
%s::%s: could not add cal file into diagnostics\n
%s::%s: Failed to get value for: %s, exception: %s\n
%s::%s: =========== FTAB Header ===========\n\n
%s::%s: Applying FDR trust object hash override\n
%s::%s: failed to perform certification\n
%s::%s: SHA384 failed\n
%s::%s: failed to create new data\n
%s::%s: attempting to delete file from cache that does not exist. File: %s\n
%s::%s: failed to process open command for write\n
%s::%s: optional tag %s missing from build identity, skipping\n
%s::%s: length reservation requirements not met (max: %d, actual:%d)\n
%s::%s: Failed to collect preflight info\n
%s::%s: Wrong type, expected data\n
%s::%s: failed to setup http header parameters (rngStatus: %d)\n
%s::%s: paging in new length for page alignment (Requested: %zu. Aligned: %zu)\n
%s::%s: no file path provided\n
%s::%s: failed to create data container\n
%s::%s: Unrecognized CF object!\n
%s::%s: missing data classes in request\n
%s::%s: file path has not been initialized\n
%s::%s: data exceeds local buffer size\n
%s::%s: no file name specified\n
%s::%s: file data has no bytes\n
%s::%s: =========== FTAB Payloads ===========\n
%s::%s: Failed to open firmware in restore options\n
%s::%s: cancelTimer - canceling timer\n
%s::%s: failed to get board params (%d)\n
%s::%s: Invalid Type of DebugArgs\n
%s::%s: failed to get byte ptr\n
%s::%s: file data must be valid or firmware data must be provided\n
%s::%s: failed to compute required size\n
%s::%s: failed to create debug directory (status: %d)\n
%s::%s: looking for AP ticket in updater options dictionary\n
%s::%s: failed to allocate strings to join array\n
%s::%s: moving %s to top\n
%s::%s: Tag: %s :: Offset: 0x%04x Raw address: 0x%lx, size: %u\n
%s::%s: failed to initialize file cache\n
%s::%s: manifest at the end - startOfManifest: %u, endOfFiles: %u, padding: %u\n
%s::%s: failed to get firmware root path\n
%s::%s: failed to create output URL\n
%s::%s: failed to allocate hash digest\n
%s::%s: failed to allocate dataIntance, dataClass\n
%s::%s: failed to open file (%s)\n
%s::%s: Missing ChipRev\n
%s::%s: Invalid arguments to parseDebugArgs\n
%s::%s: failed to determine if url exists (%u)\n
%s::%s: failed to get device info list\n
%s::%s: skipping trust error since FDR validation is disabled (Trust Error: 0x%016llx)\n
%s::%s: timer is already running\n
%s::%s: Failed to write some or all of data\n
%s::%s: savePath for FW not specified. This needs to be specified.\n
%s::%s: failed to allocate source bundle firmware path dictionary (type: %hhu)\n
%s::%s: CoredumpRegions version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: failed to init ACFUMachO\n
%s::%s: no write permissions to file... attempting to open file as read-only\n
%s::%s: failed to measure fw\n
%s::%s: failed to receive command from device, error: 0x%x\n
%s::%s: Has valid boot nonce? %s\n
%s::%s: no coredump region in the crashlog\n
%s::%s: Minimum Epoch: 0x%s\n
%s::%s: failed to update file\n
%s::%s: file (%s) not available\n
%s::%s: unexpected (too many) amount of bytes were sent to device, bailing\n
%s::%s: failed to create directory @ dstPathURL (status: %d)\n
%s::%s: failed to encode NVRM variable '%s'\n
%s::%s: cache does not have entry for file %s. Cache is invalid\n
%s::%s: requesting personalized firmware root path\n
%s
%s::%s: booting firmware...\n
%s::%s: tag '%s' not found in device info, skipping validation\n
%s::%s: Operation finished successfully! Moving to next step if one exists for this updater! \n
%s::%s: failed to create file data from file path (status: %u)\n
%s::%s: path exists but is not a directory: 0x%x\n
%s::%s: manifest data has no bytes\n
%s::%s: %s - trying to read from offset %u length %u, but file size is %u\n
%s::%s: failed: NVRM allocation failure\n
%s::%s: failed to create mutable data in unoptimized path\n
%s::%s: function does not support memory optimization flow\n
%s::%s: get offset not supported on dynamically added file %s to MMIO optimized FTAB\n
%s::%s: failed to initialize cache\n
%s::%s: failed to remove bundle fw personalized bits\n
%s::%s: failed to allocate ouptut dictionary\n
%s::%s: ECID: 0x%s\n
%s::%s: file indicated is within header space\n
%s::%s: failed to get the required path\n
%s::%s: invalid length\n
%s::%s: No manifest key specified\n
%s::%s: file data provided is not valid\n
%s::%s: =========== FTAB Payloads ===========\n\n
%s::%s: file is smaller than the ftab header size\n
%s::%s: failed to init ACFUTransport\n
%s::%s: failed to create build identity tag list\n
%s::%s: Current command %s!\n
%s::%s: ---- Restore State ----\n
%s::%s: Invalid token: %s\n
%s::%s: failed to get manifest start\n
%s::%s: security mode not present in device info. This is fatal!\n
%s::%s: There are more coredump regions than expected in the crashlog\n
%s::%s: key '%s' not found\n
%s::%s: Missing ECID\n
%s::%s: failed to create symlink: %d\n
%s::%s: Manifest is not present in expected data type\n
%s::%s: failed to create manifest data output\n
%s::%s: =========== FTAB Header ===========\n
%s::%s: could not find firmware in restore options (%d)\n
%s::%s: removing any personalized bits of rooted firmware\n
%s::%s: could not remove file entry from ftab cache\n
%s::%s: failed to create CFString for error object\n
%s::%s: failed to create BTI stage timer\n
%s::%s: failed to obtain file container\n
%s::%s: invalid file transfer session\n
%s::%s: firmware downloading finished successfully\n
%s::%s: copyFirmware: failed to create personalized FW URL (status: %d)\n
%s::%s: failed to perform preSave actions (%d)\n
%s::%s: invalid tag map parameter\n
%s::%s: failed to obtain data ref\n
%s::%s: failed to create CFError object\n
%s::%s: file transfer session still not closed\n
%s::%s: rooted firmware was personalized already so we should use that to update\n
%s::%s: failed to create dictionary\n
%s::%s: failed to aquire ftab file header\n
%s::%s: attempting to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
%s::%s: converting from string to number\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
%s::%s: client sik pubkey must be set for FDR 2.0 certification\n
%s::%s: Manifest is not available\n
%s::%s: sig cert start falls before start of manifest\n
%s::%s: esec data to boolean conversion failure\n
%s::%s: We have completed all enabled restore steps!\n
%s::%s: Internal Build: %s\n
%s::%s: Handling %s\n
%s::%s: failed to create dispatch timer object\n
%s::%s: failed to save file (%d)\n
%s::%s: SHA512 failed\n
%s::%s: startTimer - starting timer.\n
%s::%s: Missing SecurityMode\n
%s::%s: invalid parameter (acipcInterface)\n
%s::%s: failed to allocate output dictionary\n
%s::%s: failed to setup diagnostics\n
%s::%s: cannot save data using optimized flow\n
%s::%s: failed to initialize base object\n
%s::%s: wrong digest type (%s)\n
%s::%s: tag '%s' not found in tss-request map, ignoring\n
%s::%s: Num Files: %u\n
%s::%s: failed to acquire cf data byte pointer\n
%s::%s: failed to validate device identity tags\n
%s::%s: tag %s missing from firmware, skipping\n
%s::%s: We are finished with all the update steps! ^_^\n
%s::%s: unexpected debug log path type\n
%s::%s: Security Mode: 0x%s\n
%s::%s: file is empty (file size: %zu)\n
%s::%s: something went wrong, extra bytes in file\n
%s::%s: cache does not hold correct offset for file %s. Cache offset: %d. FTAB offset: %d. Cache is invalid\n
%s::%s: failed to create response tag list\n
%s::%s: failed to un-map file: (%s)\n
%s::%s: startOfManifestUnaligned: %ld, startOfManifestAligned: %ld, paddingBeforeManifestStart: %u\n
%s::%s: Generation: %u, Valid: %u, BootNonce: 0x%08llx\n
%s::%s: failed with error (ret: 0x%08x) (cookie: 0x%08x)\n
%s::%s: failed to send response to device error: 0x%x\n\n
%s::%s: Failed to create macho header data\n
%s::%s: Assuming updater options dictionary is being passed\n
%s::%s: starting timer\n
%s::%s: failed to open file error: (%s)\n
%s::%s: symlink name exists but is not a symlink: 0x%x\n
%s::%s: %s - trying to write to offset %u length %u, but file size is %u\n
%s::%s: updater failed to find firmware data with bundleData\n
%s::%s: Failed to allocate output dictionary\n
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: invalid length value\n
%s::%s: attempting to add new file to cache, but not both size and offset are provided. File: %s\n
%s::%s: bad parameter: options %p, domain %p\n
%s::%s: checksum: 0x%x\n
%s::%s: cannot aquire reference for a memory optimized data container. Please use copyData() instead\n
%s::%s: copyFirmware: failed to create src rooted FW URL\n
%s::%s: FATAL: no operation for performCmd\n
%s::%s: failed to get file system reprensetation\n
%s::%s: Missing BootNonce\n
%s::%s: padding of %zu bytes required\n
%s::%s: failed to build parameters out of device identity\n
%s::%s: failed to get byte pointer\n
%s::%s: copying preflighted bundle firmware into the dst bundle...\n
%s::%s: Failed conversion: %s\n
%s::%s: [%s] Performing iteration %d of %d\n
%s::%s: bad parameter!\n
%s::%s: open file %s, received request for file %s\n
%s::%s: failed to write to file\n
%s::%s: boot nonce is not present post boot. This is a failure.\n
%s::%s: Currently performing: %s\n
%s::%s: failed to allocate dataIntance, dataClass, or parentDataClass\n
%s::%s: UID Mode: 0x%s\n
%s::%s: failed to retrieve security mode value\n
%s::%s: Token: %s\n
%s::%s: Populating underlying error\n
%s::%s: failed to allocate bundle firmware path dictionary (type: %hhu)\n
%s::%s: key value not provided\n
%s::%s: failed to decode manifest property object (status: %d)\n
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: invalid file data\n
%s::%s: output NVRM allocation failure\n
%s::%s: file not open\n
%s::%s: failed to perform preBoot actions (%d)\n
%s::%s: failed to perform destination bundle copy of rooted firmware\n
%s::%s: failed to remove rooted fw personalized bits\n
%s::%s: tag '%s' has different values in device info and build identity\n
%s::%s: Wrong type, expected dict\n
%s::%s: Found updater options in dictionary\n
%s::%s: no fw for tag '%s'\n
%s::%s: failed to get manifest, error: %d\n
%s::%s: failed to write data to output URL (%d)\n
%s::%s: Security Domain: 0x%s\n
%s::%s: firmware file is invalid\n
%s::%s: failed to start BTI stage timer\n
%s::%s: numberOfSections is 0\n
%s::%s: using client prepared load image (assuming 4k alignment)\n
%s::%s: failed to allocate NVRM data\n
%s::%s: failed to validate %s\n
%s::%s: No save path specified\n
%s::%s: cannot update tag '%s' because it does not exist\n
%s::%s: timeout in BTI stage\n
%s::%s: %s - attempting to write more bytes (%u) than initially indicated (%u), bailing\n
%s::%s: received %u bytes data from device, fFileTransferSession->fileSize: %u\n
%s::%s: startTimer - null timeoutCB.\n
%s::%s: unexpected size for ChipID\n
%s::%s: Looking for '%s'\n
%s::%s: failed to retrieve security domain value\n
%s::%s: failed to open file\n
%s::%s: Failed to save firmware to path\n
%s::%s: performing certification...\n
%s::%s: firmware file dictionary not provided\n
%s::%s: failed to get string\n
%s::%s: manifest present in space allocated for header\n
%s::%s: could not determine requested path\n
%s::%s: production mode not present in device info. This is fatal!\n
%s::%s: failed to copy file data\n
%s::%s: no dataref\n
%s::%s: invalid parameter (done)\n
%s::%s: timer is not initialized\n
%s::%s: failed to get header pointer\n
%s::%s: ftab cache entry updated. File: %s, offset: %u, size: %u\n
%s::%s: failed to create path to firmware directory\n
%s::%s: destination path does not exist after creation attempt (status: %d)\n
%s::%s: attempting to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
%s::%s: failed to create mutable data in optimized path\n
%s::%s: Empty DebugArgs\n
%s::%s: Wrote %zu of %zu bytes to %s\n
%s::%s: %s already at top\n
%s::%s: TRACE EVENT ACFUTrace::kACFUTraceEventTransportInit: 0x%08x\n
%s::%s: no manifest\n
%s::%s: Failed to create empty trust object hash\n
%s::%s: This step is not enabled... setting to DONE and moving along.. \n
%s::%s: could not create URL to file\n
%s::%s: failed to update file data\n
%s::%s: Looks like there is no error present; Nothing to be done here.\n
%s::%s: manifest (%s) not available\n
%s::%s: failed to convert from number to data\n
%s::%s: failed to allocate certification URL\n
%s::%s: invalid offset value\n
%s::%s: failed to create url from string\n
%s::%s: failed to get length\n
%s::%s: Failed to allocate measurements dict\n
%s::%s: failed to copy ftab header\n
%s::%s: manifest is at top - endOfManifest: %u, startOfFiles: %u, paddingAfterManifestEnd: %u\n
%s::%s: No manifest present\n
%s::%s: failed: header length check validation failed\n
%s::%s: no data to log\n
%s::%s: firmware data is invalid and does not meet ftab standards\n
%s::%s: File indicated is within header space\n
%s::%s: Failed to set manifest\n
%s::%s: open (read only): %s\n
%s::%s: received %u bytes (total: %u)\n
%s::%s: TRACE EVENT END ACFUTrace::kACFUTraceEventRTI: 0x%08x\n
%s::%s: failed to perform update firmware (ret: %d)\n
%s::%s: boot nonce missing\n
%s::%s: device with board id 0x%04x does not support certification\n
%s::%s: failed to unmap file: (%s)\n
%s::%s: firmware data container is invalid\n
%s::%s: Adding new file to FTAB cache. File: %s, offset: %u, size: %u\n
%s::%s: failed to collect sik csr blob (%d)\n
%s::%s: running host invoked restore info -- using bundleURL\n
%s::%s: failed to create personalized rooted FW URL (status: %d)\n
%s::%s: failed to convert from data to boolean\n
%s::%s: Manifest digest\n
%s::%s: Using embedded ftab '%s'\n
%s::%s: unknown command type %d\n
%s::%s: failed to create RTI stage timer\n
%s::%s: Failed to create CF number from int value\n
%s::%s: file does not have write permissions\n
%s::%s: data is of an unsupported type\n
%s::%s: no file path provided.\n
%s::%s: This function has not been implemented\n
%s::%s: SHA256 failed\n
%s::%s: failed to reset chip (%d)\n
%s::%s: Using FDR trust object hash in updater options override\n
%s::%s: failed to init timer object\n
%s::%s: failed to create destination path URL (status: %d)\n
%s::%s: failed to append strings together\n
%s::%s: creating symlink from %s -> %s\n
%s::%s: bad parameters\n
%s::%s: null acipcInterface\n
%s::%s: firmware to push is missing!\n
%s::%s: failed to create mutable copy of source device firmware data dictionary (type: %hhu)\n
%s::%s: attempting copyFirmwareUpdater again with source bundle file map\n
%s::%s: parsing error while extracting the coredump regions. crashlog size: %zu offset and section size: %lu\n
%s::%s: reducing requested length %zu -> %zu\n
%s::%s: Boot Nonce: 0x%s\n
%s::%s: cache is invalid\n
%s::%s: failed to create tag list from vector\n
%s::%s: command not supported in preflight mode\n
%s::%s: Booted Update: %s\n
%s::%s: running generic updater step\n
%s::%s: specified tag name is invalid!\n
%s::%s: %s\n%@
%s::%s: failed: data buffer is empty\n
%s::%s: We have exhausted all our allowed attempts! Please file a radar!\n
%s::%s: failed to obtain copy of manifest\n
%s::%s: header is bigger than the file\n
%s::%s: bad input parameters\n
%s::%s: invalid firmware object when processing open (read) command\n
%s::%s: timeout in RTI stage\n
%s::%s: Requesting FDR trust object hash\n
%s::%s: invalid file descriptor\n
%s::%s: failed to increase file length: (%s)\n
%s::%s: function cannot directly manipulate file data with optimized flow\n
%s::%s: input data has no bytes\n
%s::%s: there is already a file trasfer in progress\n
%s::%s: failed to create build ID key path\n
%s::%s: Post Sealing: %s\n
%s::%s: file name does not exist\n
%s::%s: required size %llu\n
%s::%s: TRACE EVENT BEGIN ACFUTrace::kACFUTraceEventRTI: 0x%08x\n
%s::%s: failed to decode manifest: %d\n
%s::%s: failed to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
%s::%s: failed due to incompatible bundle data dictionary\n
%s::%s: wrong type, expected dict\n
%s::%s: failed to init data container object\n
%s::%s: ChipID: 0x%s\n
%s::%s: failed to collect download metrics for %s\n
%s::%s: converting from data to boolean\n
%s::%s: failed: max length reservation is not equal to the data buffer\n
%s::%s: failed to create file data\n
%s::%s: Missing MinEpoch\n
%s::%s: failed to get stats for path: %d\n
%s::%s: failed to obtain file data\n
%s::%s: Failed to init macho32\n
%s::%s: item %s logged successfully\n
%s::%s: failed: bad input parameter\n
%s::%s: failed to initialize\n
%s::%s: failed to create manifest\n
%s::%s: Successfully gathered personalization parameters\n
%s::%s: failed to get dict from local FDR data store\n
%s::%s: file '%s' does not exist\n
%s::%s: query command is missing chip ecid, chipId, or boardId\n
%s::%s: failed to convert from string to number\n
%s::%s: failed to create client ID\n
%s::%s: invalid optimization mask\n
%s::%s: failed to push firmware (%d)\n
%s::%s: Invalid firmware file\n
%s::%s: could not collect bti download time data\n
%s::%s: unknown command option %d\n
%s::%s: Missing = for key: %s\n
%s::%s: Current step is complete. Moving onto the next restore step\n
%s::%s: ticket key must be provided\n
%s::%s: stopping timer\n
%s::%s: No manifest provided with firmware. Manifest is required!\n
%s::%s: destination bundle was not specified, so we are skipping the copy step...\n
%s::%s: failed to decode manifest object (status: %d)\n
%s::%s: failed to retrieve chip revision value\n
%s::%s: no manifest found in ftab\n
%s::%s: cowardly retreating because tag '%s' exists in runtime MMIO File Data. I refuse to overwrite existing files!\n
%s::%s: ACFU Version: %s\n
%s::%s: paddingAfterManifestEnd %u bytes\n
%s::%s: invalid file %s with size 0\n
%s::%s: Failed to allocate buffer for macho header data\n
%s::%s: failed to allocate direct data\n
%s::%s: Empty options dict\n
%s::%s: failed due to unexpected data type\n
%s::%s: Manifest Offset: %u, Manifest Length: %u, Magic: %s\n
%s::%s: Paged loading is disabled; sending all bytes of requested data in one segment\n
%s::%s: failed to process open command for read\n
%s::%s: configuring for FDR 1.0 certification\n
%s::%s: failed to copy file header\n
%s::%s: removing file from FTAB cache. File: %s\n
%s::%s: failed to collect sik public key (%d)\n
%s::%s: failed to create data\n
%s::%s: failed to initialize diagnostics object\n
%s::%s: failed to get data from local FDR data store\n
%s::%s: failed to allocate extra options dictionary\n
%s::%s: failed to allocate data\n
%s::%s: too many files specified or there are no files. Limit is %d. Num Files: %d\n
%s::%s: Invalid save path\n
%s::%s: Chunking image using paged loading\n
%s::%s: crashLogBuffer is null\n
%s::%s: Chip Revision: 0x%s (%s)\n
%s::%s: failed to remove file (%u)\n
%s::%s: Boot nonce set for FTAB. Boot nonce value: %llu\n
%s::%s: failed to copy ftab file header\n
%s::%s: running device invoked restore info -- using bundleData\n
%s::%s: failed to get src bundle URL\n
%s::%s: removing any personalized bits of bundle firmware\n
%s::%s: Invalid FDR trust object hash in client updater override\n
%s::%s: failed to get file stats\n
%s::%s: file does not exist\n
%s::%s: No error to log. All clear, move along now!\n
%s::%s: allowing unsealed FDR data\n
%s::%s: We ran into some issues on try %d of %d!\n
%s::%s: failed with bad input parameters\n
%s::%s: failed to set the boot nonce (%d)\n
%s::%s: failed to determine variable type\n
%s::%s: Preflight: %s\n
%s::%s: data class %s not present in parent data class %s\n
%s::%s: failed to acquire firmware data from file path\n
%s::%s: Failed to get DebugArgs buffer\n
%s::%s: failed obtain file size\n
%s::%s: failed to obtain data ref for %s at offset %u length %u\n
%s::%s: tag '%s' not found in tss-request map, skipping validation\n
%s::%s: item %s failed to log\n
%s::%s: no transport\n
%s::%s: failed to update manifest\n
%s::%s: failed to receive data from device, error: 0x%x\n
%s::%s: failed to boot firmware post update (%d)\n
%s::%s: failed to change directory permissions: %d\n
%s::%s: firmware file failed to initialize\n
%s::%s: Chip major revision seems unreasonable: %d\n
%s::%s: BTI stage completed successfully\n
```
