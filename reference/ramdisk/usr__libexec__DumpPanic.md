# `/usr/libexec/DumpPanic`

From the upgrade restore ramdisk (141-29011-104.dmg). 356,320 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 43 (Size: 5872)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (25)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics (compatibility version 0.0.0, current version 1.0.0)`
- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeNamespaceDevice.allow</key>
	<true/>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.osanalytics.otatasking-service-access</key>
	<true/>
	<key>com.apple.private.ApplePMGRUserClient.access</key>
	<true/>
	<key>com.apple.private.ApplePMGRUserClient.get-bpr</key>
	<true/>
	<key>com.apple.private.AppleSoCMiscUserClient.access</key>
	<true/>
	<key>com.apple.private.AppleSoCMiscUserClient.get-bpr</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>InverseDeviceID</string>
	</array>
	<key>com.apple.private.applecredentialmanager.allow</key>
	<true/>
	<key>com.apple.private.coredump-encryption-key</key>
	<true/>
	<key>com.apple.private.diagnostic-intelligence</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.DumpPanic</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>PanicPatternMatching</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Diagnostics.Panic</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.iokit.system-nvram-allow</key>
	<true/>
	<key>com.apple.private.roots-installed-read-only</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.file-unencrypt-access</key>
	<true/>
	<key>com.apple.private.security.storage.DumpPanic</key>
	<true/>
	<key>com.apple.private.security.storage.spindump</key>
	<true/>
	<key>com.apple.rootless.volume.VM</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleSoCMiscUserClient</string>
		<string>ApplePMGRUserClient</string>
		<string>AppleNVMeNamespaceUC</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>
```

## Objective-C (14 classes, 2 protocols)

Classes: `ArgParser`, `CoreFileHandler`, `CoreFileHandlerV1`, `CoreFileHandlerV2`, `CoresPruner`, `DumpPanicArgParser`, `KeyStore`, `LockedReadOnlyKeyStore`, `PanicProcessingAdapter`, `PanicUtilArgParser`, `ReadOnlyKeyStore`, `SOCDReportInfo`, `UserCoreFileHandler`, `_TtC9DumpPanic27PanicPatternMatchingWrapper`

Protocols: `NSObject`, `PanicProcessingDelegate`

## Strings (1,344)

```
_rtkit_crashlog_binary
crashReporterKey
length
readKeyFile:::::
setOriginalPanicReportPath:
useCrashlogContainers:
lowercaseString
_eph_binary
fileExistsAtPath:
setDelegate:
unlock
allValues
createWithPanicBuffer:panicLength:
getCoreDumpEncryptionKey:
getNumCoreDumps
dictionary
kernelVersion
panicProcessingInfo
respondsToSelector:
saveWithOptions:
setClassification:
setProduct:
T@\"NSArray\",N,C
base64EncodedStringWithOptions:
_corefileSize
_keystore
init:
performSelector:
removeObject:
replaceObjectAtIndex:withObject:
_filesToScreen
iph_binary
numberWithUnsignedChar:
setIph_binary:
setProblemDescription:
setTimeZone:
testPlanID
writeToFile:options:error:
containsObject:
TB,V_restoreos
setCoresToKeep:
launchAppWith:options:completion:
setForce_run:
setForegroundAppHash:
stringByReplacingOccurrencesOfString:withString:
unsignedLongLongValue
_encryptionPublicKey
arrayWithObjects:
componentsJoinedByString:
dataWithContentsOfURL:options:error:
dictionaryWithDictionary:
errorWithDomain:code:userInfo:
timeUsecs
fileSize
getAuxiliaryNVRAMData
numberWithUnsignedLongLong:
patternTypeString
removeObjectForKey:
boolForKey:
error
containsString:
_userspaceCorefileName
description
force_run
incidentID
numberWithInt:
stringByReplacingCharactersInRange:withString:
useExtPaniclog:
_input_core
defaultManager
objectForKey:
saveUserSpaceCoreToDisk:
writeData:error:
numberWithUnsignedLong:
objectAtIndexedSubscript:
setHelp:
shared
sharedInstance
stringByAppendingFormat:
_agentId
_input_corefile_name
eph_binary
initWithCoreFilePath::
isKindOfClass:
retain
setMatchedActions:
_singleFileMode
T@\"NSString\",N,C
_force_run
extPaniclog
initWithBytes:length:encoding:
rangeOfString:options:
restoreos
scanFilesInURL:pullinFiles:screenFiles:andTimeStamps:
product
.cxx_destruct
isMemberOfClass:
plainPanicData
setUUIDSPTM:
stringWithCString:encoding:
timeIntervalSince1970
dateFromString:
T@\"NSURL\",&,V_plane_json
_error
_help
buildVersion
TB,V_is_userspace
setPanicString:
initWithArgs:count:
patternType
setplatformECID:
T@\"NSData\",&,N,V_data
_output_dir
help
initWithCString:encoding:
notes
sharedAdapter
socId
addObject:
hasInputFiles
saveKernelCoreToDisk:::::
self
type
dataWithBytesNoCopy:length:
integerValue
panicString
panic_string
privateKeyChecking
rtkit_crashlog_binary
setIsUserInitiated:
stringWithFormat:
_corefileHeader
logfile
UUIDString
TB,V_help
utilizationInfo
bootfault_json
mutableBytes
removeItemAtURL:error:
URLByAppendingPathComponent:
_socd_binaries
getStackshotData
setPanicInitiator:
stringByDeletingLastPathComponent
getBytes:range:
release
conformsToProtocol:
createForSubmission:metadata:options:error:writing:
dataWithPropertyList:format:options:error:
dateWithTimeIntervalSince1970:
initWithUnsignedInt:
setOutput_dir:
TC,N,V_agentId
setPatternUUID:
_corefileURL
initWithFileDescriptor:closeOnDealloc:
setData:
timeZoneWithName:
TB,V_force_run
TI,V_coresToKeep
_is_userspace
_type
coreFileWithCoreFilePath::::
output_dir
subdataWithRange:
stringFromDate:
dataWithLength:
isResearchFused
_iph_binary
compare:
countByEnumeratingWithState:objects:count:
isDevFused
JSONObjectWithData:options:error:
T@\"NSString\",?,R,C
appendString:
matchedActions
prune
setEPHVersion:
setPanic_string:
setSocd_binaries:
T@\"NSURL\",&,V_corefileURL
_coresToKeep
_keyStorePath
hash
initWithObjectsAndKeys:
timeIntervalSinceDate:
setCorefileURL:
withArgs:count:
enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
getHeaderVersion
initWithPanicString:
panicMedicTelemetry
plane_json
useSocdContainer:
T@\"NSNumber\",N,&,VpatternType
debugDescription
initWithCorefileURL:CoresToKeep:userspaceCorefileName:
isTagCheckFault:
numberWithLongLong:
panicInitiator
setTitle:
filesToScreen
firstObject
getCoreDumpInfoWithIndex::::
lastPathComponent
T@\"NSURL\",&,V_eph_binary
data
dataWithBytesNoCopy:length:freeWhenDone:
initWithPanicString:otherString:buildVersion:panicFlags:panicType:incidentID:rootsInstalled:
isTestAutomationDevice
moveItemAtURL:toURL:error:
setAWLBuildVersion:
setPanicProcessingInfo:
_corefile_fd
addObjectsFromArray:
setType:
setUUIDKernelCache:
substringToIndex:
serviceSettings
_restoreos
absoluteString
dictionaryWithCapacity:
setSOCId:AndRev:
deviceModelType
TC,N,V_type
TQ,R
dataWithContentsOfFile:options:error:
fileCreationDate
filesToPullIn
firstMatchInString:options:range:
mountVolumeWithRole:mountPath:
_isDefaultKeyStorePath
otherString
rangeAtIndex:
setObject:forKey:
stringWithString:
useStoragePanicData:
setPatternType:
class
copy
getSterilizedStringFromData:size:
log_path
setKeywords:
setPanicTimeInSecs:andUsecs:
useSocdNandContainer:
initWithFormat:
initWithLength:
saveCoreDumpAtOffset:withLength:named:encryptedWithPublicKey:toFileName:flags:
setAgentId:
setDateFormat:
setKernelVersion:
setRawPanicData:
setUUIDIBoot1:AndIBoot2:
T@\"NSMutableDictionary\",&,V_filesToPullIn
bootsessionuuid
_zero_on_close
characterAtIndex:
currentDirectoryPath
propertyListWithData:options:format:error:
setFiles_to_attach:
setUUIDKernel:
initWithCoreFilePath::::::
T#,R
stringByAppendingPathComponent:
array
date
saveCoreDumpWithIndex:named:toFileName:
userspaceCorefileName
_bootfault_json
_filesToPullIn
appendBytes:length:
arrayWithCapacity:
coresToKeep
donateToBiome
exceptionWithName:reason:userInfo:
setUUIDTXM:
patternUUID
stringWithUTF8String:
zone
T@\"NSMutableDictionary\",&,V_filesToScreen
T@\"NSURL\",&,V_rtkit_crashlog_binary
createDraft:forProcessNamed:withDisplayReason:error:
getCoreDumpNameWithIndex:
setFilesToPullIn:
socd_binaries
setAttachments:
componentsSeparatedByString:
rootsInstalled
setBoardId:AndRevId:
setError:
_input_corefile_path
fileExistsAtPath:isDirectory:
getCoreDumpContentsWithOffset:AndLength:
initWithName:version:identifier:
retainCount
writeToFile:atomically:
arrayWithObjects:count:
autorelease
hasMatchingPrivateKey::
isZeroes:
setActions:
fileType
getCorefileLogInfo:::
initWithUUIDBytes:
setAppleCareDetails:
setLog_path:
_scratchBufSize
T@\"NSURL\",&,V_bootfault_json
_scratchBuf
anyObject
dataUsingEncoding:allowLossyConversion:
getEccFormat:
is_userspace
rangeOfString:
agentId
isIntentionalPanic
platformECID
socRev
stringByAppendingString:
T@\"NSString\",R,C
T@\"NSString\",&,V_userspaceCorefileName
corefileURL
filepath
init
initWithArray:
initWithData:encoding:
isEqual:
bytes
decode
getMatchingPrivateKey::
isEqualToString:
setEph_binary:
setLocale:
setPlane_json:
standardUserDefaults
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:
getCorefileZeroRanges
initWithLocaleIdentifier:
panicFlags
path
regularExpressionWithPattern:options:error:
setDiagnosticExtensionIDs:
uniqueChipID
isProxy
T@\"NSURL\",&,V_output_dir
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
dataWithJSONObject:options:error:
deleteBootArgDumppanic
fileURLWithPathComponents:
hasSuffix:
initWithKeyStorePath::
cleanup
_log_handle
intValue
objectAtIndex:
performSelector:withObject:
removeItemAtPath:error:
setBootfault_json:
stringValue
count
numberWithDouble:
performSelector:withObject:withObject:
removeAllObjects
setFilesToScreen:
substringFromIndex:
usage
RotateKeys:
dealloc
initWithCoreFilePath:::
localizedDescription
objectForKeyedSubscript:
setComponent:
sortUsingComparator:
superclass
T@\"NSMutableArray\",&,V_socd_binaries
problemType
setPanicProcessingFlags:
setPlaneMetadata:
setRtkit_crashlog_binary:
setSocDataVersion:
unsignedIntValue
T@\"NSURL\",&,V_iph_binary
_data
setUserspaceCorefileName:
substringWithRange:
timeSecs
unsignedCharValue
dataWithBytes:length:
generatePanicSaveOptionsForDirectory:time:prefix:
initWithBase64EncodedString:options:
setUtilizationInfo:
writeData:
T@\"NSError\",&,V_error
bootIsRecoveryEnvironment
fileSystemRepresentation
setIs_userspace:
files_to_attach
_headerData
fileURLWithPath:
getCorefileLogEncryptionKey
setRestoreos:
_corefilePath
addNotes:
authorizationStatus
dateWithTimeIntervalSinceReferenceDate:
getValueFromDTForNode:key:
setBootStage:
setObject:forKeyedSubscript:
dictionaryWithObjects:forKeys:count:
getPanicRegion
mutableCopy
numberWithUnsignedInt:
removeObjectAtIndex:
setAutoDiagnostics:
timeIntervalSinceNow
UTF8String
_plane_json
Failed to set %s xattr returned error : %s
Skipping non-file type '%@'
Failed to parse the file contents as JSON. Error: %@
Mismatched key hash lengths
No data was read from the file or device (buffer length was zero).
Found storage dump log of length 0x%llx
Device tree indicates that device never supported legacy panic path
DumpPanic launched after boot to check for device panic data
Failed to write standalone socd panic report
Invalid parameters for get_awl_platform_data
Invalid parameters for set_awl_platform_data_in_report
Failed to read report data for report %d: %d
Failed to get kern.bootsessionuuid
Failed to allocate memory for kdp_corefile buffer
Failed to open file output stream.
File seems to be too large to be useful. Skipping
Failed to setup the key-store directory.Error: %@
Current key does not match expected key format. Skipping
Warning: preoslog log timestamps are not original, they are assigned later when the buffer is being flushed
Pattern matching failed: %s
Opening paniclog path '%@'\n
Found matched panic pattern
read out auxiliary PMU fault data: boot fault info: %@
%s of unexpected type %lu
loaded socd data from: %@
Failed to enumerate the directory at '%@'
Deleting unparseable file '%@'
Upper buffer is at va %p, size %zu bytes
This device does not support the AppleNVMeDevice API and no paniclog block device was found.
failed to write fallback data to file: %@
failed to write embedded panic data to file: %@
ready to submit %s
Failed to close AEA decrypt stream source.
Neither can find %@
Keystore unlock has failed
gzopen %s
Failed to write panic log with SOCD data
unable to write json to file: %@
LZ4 decode stream is not supported.
Failed to open gzip output stream.
The input public key did not pass basic validation checks
Failed to set the '%@' NVRAM variable. Error 0x%04x
DR launched.
Stored %ld matched actions: %s
Warning: Failed to set AWL platform data from platformSocdBuffer in plane metadata
Error getting a reference to IODeviceTree:/options
TapToRadarService does not exist and thus we cannot start a radar
Failed to open directory: %s (%{errno}d)
Found %lu matched actions from pattern matching
%.*s
Pattern matching service crashed or hung
Failed to query disk block size -- DKIOCGETBLOCKSIZE failed with %d : %s
%llu bytes were read from the file or device, but it did not contain any paniclog data (buffer was all zeros).
Found embedded panic log of length 0x%llx
Faled to write panic log breadcrumb: %s
Failed to allocate lz4 decode stream data buffer.
gzopen(%s, wb) error: %s
getCoreDumpContentsWithOffset called with zero length
Found a valid preoslog buffer at va %{private}p, size %zu bytes, write offset %d, source %s, wrapped %d
Paniclog data size (%llu bytes) size greater than max buffer size. Truncating.
Wrote log with storage data, discarding initial safe log
failed to write boot fault data to file: %@
Write a standalone socd panic report
lseek() to file offset 0x%llx returned -1 (%{errno}d)
Couldn't obtain preoslog buffer size, result %s
DumpPanic has already finished running for current boot
Failed to remove non-directory entry '%@'. Error: %s
Failed to create EmbeddedPanicDataDecoder instance
Created legacy panic data marker file: %s
SOCD data collection is complete. Checking for data
Found panic log breadcrumb with duplicated boot session uuid
failed to creat() PMU fault data processed cookie at path %s with error %s
Prune kernel core files
Failed to parse the input public key with the given format. CoreCrypto error %d
attempting to discard safe log at %@
Failed to get the number of agents: %d
failed to setup corefile stage directory with error: %s
Reusing an existing key file
Failed to parse the current private key. CoreCrypto error %d
skipping launching TTR because DumpPanic is currently rate limited...
Failed to create a regex matching expression: %@
Pattern Matching initialized with payload available: %s
%llu bytes were read from the file or device, but at least %lu are required to fit the iBoot panic header.
Matched registered panic device: %s
No boot fault data found in local device
Failed to get the agent IDs: %d
Corefile corrupted. Public key (offset %llu, length %hu) extends past end of file (length %zu).
Successfully read %hu bytes for the public encryption key
Failed to read content from %s core
No panic data detected from '%@'
open_dprotected_np(%s, O_RDONLY): -1 (%{errno}d)
Reading public encryption key from corefile
boot-args NVRAM variable does not have a '%@'=<value> arg
Magic for preoslog buffer doesn't match, expected %08X, given %08X
failed to write ResetCounter log to disk
boot fault data found in local device
Error creating CFString for key %s
Failed to allocate %zu bytes for report %d
On-disk zlib-compressed cores are not supported.
Misformatted key file. Public key hash not found
Failed to write panic file
invalid core file signature: %#llx (expected :%#llx or %#llx)
Creating a new key file
Failed to launch DR with error: %@.
Failed to write panic log with storage data
failed to clear PMU boot-properties with error: %d
Failed to get the exclusive section for agent %d: %d
Found %lu sets of cores under staged folder
Misformatted key file. Full key not found
Failed to generate JSON data for key file. Error: %@
kern.preoslog is not supported by this kernel
No previous DumpPanic finish cookie
failed to write socd data to file: %@
Failed to get reports count in SOCD container size: %d
Failed to find a matching private key for the public key.
failed to creat() DumpPanicDone cookie at path %s with error %s
No donate type specified in matched actions
Error getting a reference to IODeviceTree:/defaults
searching IORegistry again after %lds sleep
Failed to read from AEA decrypt stream source.
Failed to read from lz4 decode stream source.
Failed to rename compressed %s from %s to %s
boot-args NVRAM variable is either not set or inaccessible
No socd data found in local device
Attempting to extract kernel core if it exists...
Corefile corrupted. File %zu's name is not a valid string.
Misformatted key file. Mismatched magic
Error creating CFString %s
Failed to flush the NVRAM store when setting '%@': Error 0x%04x
Compressed kcdata buffer doesn't contain a stackshot, iter_type is %d
Failed to extract AWL platform data from SOCD buffer
Failed to parse breadcrumb with error : %s
Failed to create draft in Tap-to-Radar: %@
No matched actions available from pattern matching
erased corefile contents
open %s failed with error: %s
Found a matching private key
unable to read out auxiliary PMU properties
No %s core found at %s
Failed to delete file '%@'. Error: %@
Invalid parameters for RTKit crashlog processing
Empty RTKit crashlog data
opened corefile, header indicates %llu files present
Failed to open %s to mark as purgeable. Error: %s
Failed to allocate memory for the boot-args
Machine configured for intentional panic
Machine configured to reboot on a panic
preoslog dump begin
Skipping writing ResetCounter log as no unexpected resets detected
Prune %@ userspace core files
Found %lu sets of corefiles (policy limit %u, %lu set staged), not cleaning up
Moved staged '%{public}@ to panics folder
Corefile corrupted. Log (offset %llu, length %llu) extends past end of file (length %zu).
Successfully read %llu bytes for the corefile headers
Found %s core at %s
Couldn't allocate a large enough (%zu bytes) buffer for inflating the compressed panic stackshot
unable to write socd data to file: %@
Failed to write %s
Failed to parse the Base64-encoded hash
Failed to gather the file attributes for '%@'.
failed to check whether PMU fault data has been processed using access(%s, O_RDONLY) returned: %s
Failed to set the private key. Error %d
Detected stress rack device, setting xattr on original %s core
skipping launching TTR because of user defaults...
Failed to stat file: %s (%{errno}d)
Waiting for DR to launch.
Failed to unlock a keystore. Encryption not vailable.
Failed to remove directory: %@ -> %@
Failed to create directory: %@ -> %@
Failed to allocate AEA decryption stream data.
stat(%@): -1 (%{errno}d)
Found corefile with signature %#llx
failed to look up hw.osenvironment: %s(%d)
Flush preoslog
Found SOCD container with length 0x%llx
Failed to write out error panic log
Skip writing ResetCounter log to disk for intentional panic
SOCD data collection still in progress
Failed to get SOCD container size if report record ID: %d, error: %d
Failed to remove file %@ with error %@
open_dprotected_np(%@, O_RDWR): -1 (%{errno}d)
Failed to read the file contents for panic region file. Error: %@
failed to write paniclog data to file: %@
Cannot move staged '%{public}@' to panics folder : %{public}@
failed to setup corefile output directory with error: %s
Compressed stackshot metadata: type: %lld totalout: %lld totalin %lld
invalid core file signature: %#llx (expected :%#llx)
Lower buffer is at va %p, size %zu bytes
Launching DiagnosticsReporter with files to attach: %@, log_path: %@, and panic string: %@
Failed to write full panic log
Failed to create matching dict
EmbeddedPanicDataDecoder initialization error: %@
unable to parse date from filename %@, skipping
Failed to query the size of kdp_corefile. Error: %d
%s core already compressed, skipping collection
Failed to get encoded report from SOCD buffer
Failed to write to gzip output file with error: %s.
error zeroing corefile, attempted to write %zu bytes, wrote %zu bytes
Failed to gather the file attributes for key file at path: %@
NVRAM is not supported on this system
no %@ in NVRAM
no stackshot found
Device supported legacy panic path, file marker found
read out PMU fault data: resetCount: %d, bootFailCount: %d, boot stage: 0x%x, boot app hash: %d, boot faults: %@, universal boot faults: %@:
Failed to load SOCD container: %d
Failed to open AEA decryption stream.
Failed to remove inaccessible entry '%@'. Error: %s
Failed to unlink prior stashed panic log breadcrumb %s
Failed to allocate section input stream.
Failed to initialize lz4 decode stream data.
error zeroing corefile: write(%zu): (%{errno}d)
Failed to parse the Base64-encoded key
Failed to allocate memory for preoslog buffer
Failed to initialize Pattern Matching
Failed to get matching socd ioservices: 0x%x
Finished extracting core file data from file offset %llu\n
Failed to read the file contents for key file. Error: %@
TapToRadarServiceSettings does not exist and thus we cannot start a radar
Unexpected donate action count %ld
Failed to write initial safe panic log
Removing prior corefiles, found %lu sets (policy limit %u, %lu set staged)
Unable to register for device lock state notification.
Failed to create file: %s with error: %s
PMU fault data already processed this boot
Waiting for SOCD data collection to complete
Cannot find matching private encryption key for encrypted core
Populated launchOptions.options with matched actions: %@
Failed to initialize the z_stream for this panic stackshot: rc = %d
Failed to seek to offset %lld in kernelcore.
Failed to process the coredump through the byte streams. Error %lld
failed to allocate staging directory string
Failed to mark %s as purgeable. Error: %s
%s core is empty
Not a key file. Magic not found
Unable to get device lock state
Failed to query the size of the boot-args. Error: %d
Failed to find matched panic pattern
Discarding 'safe' log %@
Failed to decode base64 SOCD report
Failed to process RTKit crashlog data
Corefile corrupted. Header (size %zu) and %llu file headers (each of size %zu) extend past end of file (length %zu).
Deleting dumppanic boot-arg...
Failed to inflate the compresssed panic stackshot buffer: rc = %d
ERROR: '%s' when opening '%@'
failed to write system watchdog reset panic log
Failed to locate primary PMU service
Failed to write boot fault report
Found %@: offset: 0x%llx, length: 0x%llx, flags: 0x%x. Writing to disk
failed to find panic region in corefile with %llu files
Corefile corrupted. File %zu's name was not terminated.
preoslog dump end
Unexpected pread result (%zd of %zu bytes) of panic data (%@): errno %d
The boot fault doesn't meet the promotion criterias, reportSingleUnexpectedReset: %d, reportiBootHang : %d, bootFaultsMatchCriteria: %d, ibootPanicSavePanic: %d, bailing out panic promotion
Failed to safely open file : %s
Failed to create an AEA context.
Removing prior corefiles, found %lu sets (policy limit %u)
Waiting for first unlock ...
no safe log will be discarded
Found panic log of unknown type (%d) length 0x%llx
wrote ResetCounter log to disk: %@
Failed to read %s in %s. This most probably means there's just no SOCD data
Failed to create SOCD handle: %d
Failed to allocate gzip output stream.
failed to setup corefile stage directory due to error: %s
AppleNVMeReadPanicLogData successfully extracted %llu bytes of data.
unable to serialize json: %@
no core file data found
Device already after first unlock
Expected to find donate action but none found in matched patterns
Failed to allocate matching dictionary to match against PMU
bootFaults contained uncategorized PMU fault(s) : %@
Prune core files in %@
Not pruning because the policy limit is set to 0
Failed to call the new public key callback
Failed to parse the value of the '%@' boot-arg as an integer. Remainder = '%s'
Failed to enumerate the contents of the sandbox directory: %@
invalid kcdata iter type in %s(): %d
Wrote log with SOCD data, discarding initial safe log
Failed to allocate lz4 decode stream data.
Unknown key format %d
found hw.osenvironment: %s
PanicMedic telemetry(valid:%d, reported:%d,panic count:%d) should be valid, hasn't been reported and has panic, skipping parsing...
Failed to encode RTKit crashlog data to base64
The kernel core is not encrypted
Failed to parse the file contents as a dictionary
preoslog buffer size is 0
Failed to create directory: %s with error: %s
Use '-f/--force' to run DumpPanic manually
Failed to allocate lz4 decode stream.
NULL input for scanFilesInURL, skipping scanning in URL %@
Received confirmation that a Tap-to-Radar draft has been started
the feature flag is not enabled, skipping PanicMedic telemetry...
open_dprotected_np(%@, O_RDONLY): -1 (%{errno}d)
loaded %@ from NVRAM: %@
Failed to query kdp_corefile. Error: %d
failed to read header from corefile (%zd bytes) with error: %{errno}d
failed to setup corefile output directory with error: %@
gzwrite failed to write %s core
Failed to close compressed %s core with error : %d
Unknown file version %d
Mismatched key hashes. Skipping
skipping launching TTR...
Failed to release socd ioservice (%s) iterator: 0x%x
Breadcrumb file contains invalid data
Skip handling kernel corefile which suggests 0 files present
Failed to call the new public key callback with an existing key
OSADiagnosticsReporter does not exist and thus we cannot launch DR
PanicMedic telemetry is nil, skipping parsing...
Successfully set AWL platform data in report
write %@ to %s
Read of %lu bytes from dataOffset %llu (file offset from %llu)(total length %llu) failed with error %{errno}d
Failed to close compressed %s core with error : %s
Failed to read existing key file
Machine configured to NOT reboot on a panic
Failed to notify kernel of new public encryption key. Error: %{errno}d
Removing non-directory entry '%@'
%@
iBoot panic header indicates %d panic logs available
panic stackshot is type %d
IOService match returned an empty iterator
Current key does not match input key format. Skipping
Required metadata from compressed panic stackshot is unexpected: type: %lld totalout %lld totalin %lld
Falling back to corefile embedded panic log of length 0x%lx
socd data found in local device
Failed to allocate section input stream data.
Failed to allocate gzip output stream data.
Failed to decode from lz4 stream source.
copying %llu bytes
Corefile corrupted. File %zu's (name %s, offset %llu, length %llu) extends past end of file (length %zu).
implausible data type for %@, abandoning data
Failed to open section input stream.
Failed to open lz4 decode stream.
Misformatted key file. Version not found
Unsupported key format in key file: %d
Failed to get response for tap to radar notification with error: %d
Failed to query the boot-args. Error: %d
kcdata iterator was invalid while collecting compression metadata
unable to read out primary PMU properties
Failed to open report record ID: %d, error: %d
Misformatted key file. Key format not found
Detected stress rack device, skipping prompting user for panic
No valid storage dump data found
Device supported legacy panic path, no existing marker file found
No paniclog data found in local device
Failed to create a SOCD handle: %d
Failed to load the SOCD container: %d
Cannot find %@
Failed to open %s core compressed output file with error %s
Failed to display tap to radar notification with error: %d
Unable to open file: %@
wrote boot fault data to: %@
No reports in SOCD container for v2 fallback
Warning: Failed to set AWL platform data from local platform_socd_buff
Failed to open report %d: %d
Removing file %@
getxattr %s returned error : %s
Finished processing %@ core, available at %@
IOService match returned an empty iterator for PMU services
0x%llx bytes of paniclog data found in local device
The platform data is not with expected version, version: %d, expected: %d
Failed to get SOCD v2 container agent ID: %d, num_agents: %zu
Failed to construct panic log breadcrumb: %s
saved core file %@
Failed to write to the new key file. Error: %@
Buffer size returned by sysctl doesn't match buffer size recorded in the header, preoslog buffer is corrupted
Failed to unlink panic data -- DKIOCUNMAP failed with %d : %s
Read of %lu bytes from fileoffset 0 only read %lu bytes
Failed to mark the coredump output file as purgeable.
failed to query sysct hw.memsize: %s
TapToRadarService reports the user has turned off DumpPanic prompts, skipping prompting user for panic
Couldn't obtain preoslog buffer, sysctl failed with result %s
Successfully processed RTKit crashlog data (%zu bytes)
Pattern matching failed: %@
SOCD report too small for AWLDataPlatform_v3: %zu < %zu
Failed to read from kernelcore file.
Failed to allocate compression buffer for %s core
unable to write %@ back to NVRAM, it is not marked as reported!
Found donate action type %u with UUID: %s
Read %ld bytes from panic device
Failed to stat %s with error %s
detected interesting reset, promoting to panic
Failed to get matching PMU ioservices: 0x%x
AppleArchive is not supported.
Failed to allocate AEA decryption stream.
Public encryption key is empty. Corefile is not encrypted
Unsupported encryption key format in corefile flags: %llu
Failed to get reports count: %d
Read from panic log breadcrumb failed due to %s
Read of %lu bytes from dataOffset %llu (file offset from %llu)(total length %llu) only read %lu bytes
Removing original %s core
Source: %@
com.apple.PanicUtil
socd-smc panic
socd-iboot panic
corefile with name %s
coreName
coreSize
kernel core log
 (iBoot panic)
iBoot header contained bad magic (possible legacy panic data)
 after panic save CE trigger
staged
DRAMSizeMB
ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n
  -r, --restoreos DIRECTORY\n\t\t               special-case mode for restore environment\n\n
 panic save chip reset
type
Triage
stress-rack
help
check_log_metadata called with invalid log_type
IOPMUBootErrorAppName
0 5
sgpio
 (iBoot async abort)
%s must be implemented
Invalid argument
%@/%@
com.apple.dumppanic
Encryption key format
PanicMedicEntryBootTarget
AppleNVMeReadPanicLogData suffered from an unknown error.
/var/root/Library/Application Support/DumpPanic/LegacyDataProcessed
upc_reset
%@%skernel.core.log
IOPropertyMatch
resetCount
bootStage
arm-io
com.apple.coreOS.restartReason
gpu_therm
/private/var/mobile/Library/Logs/CrashReporter/Panics
/staged
 after iBoot panic save storage init
com.apple.coreOS.resetTelemetry
AppleSMC
socd-data-in-progress
IONVRAM-FORCESYNCNOW-PROPERTY
kern.hv_vmm_present
com.apple.osanalytics.preoslog
ccrng_process_atfork_parent
+[ArgParser withArgs:count:]
IOPMUBootErrorStage
 (AP watchdog expired)
launchd
EnablePanicMedicTelemetryInRecoveryEnv
Retired
w
IOParentMatch
/var/root/Library/Application Support/DumpPanic/
ResetCounter
\n
 panic diags
clock_gettime()
ccdrbg_nistctr: invalid block size
IODeviceTree:/options
socd.bin
lz4DecodeStreamClose
wdog
Unexpected SPMI fault reset occurred
 iBoot panic save reboot
CorefileDataSize
iBoot panic header magic invalid: found 0x%x, expected 0x%x
dbg_rst
.core
iboot
 iBoot end
-corefile_paths
.gz
PanicMedicEntryBootStage
ccrng_process_atfork_prepare
Your device has rebooted after a force reset
resetType
  -o, --outputpath DIRECTORY\n\t\t              output directory for logs\n\n
outputpath
AppleNVMePanicLogGetSize received an invalid argument.
unique-chip-id
AppleDisplay
kcd_c_totalin
rtkit-crashlog
AppleNVMeReadPanicLogData could not find panic log namespace service in registry.
iboot-panic-header
platformSOCDBuffer
panic_region
socd
!(cur_metadata->lm_flags & IBOOT_PANICLOG_BAD_MAGIC_FLAG)
sochot
864502
sectionInputStreamRead
corefilestreams.m
 while x86 panic diagnostics being saved
iboot_panic_header.bin
forceReset
(?:^|[ \t\r\n])%@=(0x[a-fA-F0-9]+|-?[0-9]+)(?:[ \t\r\n]|$)
usage: PanicUtil [OPTIONS] \n
Failed to base64 encode SOCD container of length %u
Unexpected uncategorized reset occurred
@\"NSDictionary\"8@?0
YES
panicmedic-telemetry
ExclaveCapability
BSD Name
 iBoot Stage LLB end
ov
bootfault.json
hw.osenvironment
 sleep/wake transition
vdd_hi_and_chg_pok
unlock_sema != nil
Your device has recovered from a panic
aia
fchown of path : %@ failed with error : %s
Cancel
IOPMUBootErrorFailCount
UTC
magic
esr: 
BAD MAGIC! (flag set in iBoot panic header), no panic log available
DeviceClassNumber
interrupted coredump panic
 (AppleLPM crashed)
device panic
AppleNVMeReadPanicLogData suffered from an internal error.
Reset count
aeaDecryptStreamClose
data
en_US_POSIX
q24@?0@8@16
handlekernelcore.m
coreDumpDuration
609970
BATS_TESTPLAN_ID
EnablePanicPatternMatching
iBoot header contained bad magic
IOPMUBootErrorPanicCount
development-cert
  -f, --force\n\t\t             force DumpPanic to run\n
spmi
 panic start
com.apple.DumpPanic.corefileSummary
ccrng failed assert key_nbytes = %lu\n
AppleNVMeReadPanicLogData failed to unmap data from panic log namespace.
 panic save CE trigger
 after iBoot LLB Autoboot
forceSeedFeedbackPrompting
%x
At least one input file required
btn_shdn
No usable panic logs available from iBoot headers
 after AP Watchdog reboot
-[CoreFileHandler getNumCoreDumps]
IODeviceTree:/chosen
ap watchdog
failed to open directory at path : %@ with error : %s
%s/%@.
usage: DumpPanic [OPTIONS] \n
chosen
1111324
IOPMUBootFaultInfo
 panic diags complete
-[CoreFileHandler getCorefileLogEncryptionKey]
AppleNVMePanicLogGetSize failed to query panic log namespace size.
115
ntc_shdn
por
Error getting a reference to IODeviceTree:/options
ccdrbg_nistctr: key length too long
crash
com.apple.DiagnosticExtensions.Panic
+3Uf0Pm5F8Xy7Onyvko0vA
ArgParser.m
 iBoot panic save power init
IOService
/private/var/db/DumpPanic
 (AWL AP Panic)
UnexpecteResetReason
Panic Triage
ota-uuid
/var/db/com.apple.DumpPanic.panicLogPathBreadcrumb
init()
  -o, --outputpath DIRECTORY\n              output directory for logs\n\n
 while panic diagnostics being saved
 (AWL watchdog expired)
chip-id
sys watchdog
socd-iboot sync abort
ccrng_process_init
force_off
%s must be overridden in a subclass/category
embedded_panic_header.bin
  -r, --rtkit-crashlog FILE\n              use raw RTKit crashlog binary file\n\n
IOPMUBootSOCDClear
/private/var/db/DumpPanic/Coredumps
/private/var/db/DumpPanic/Keys
buffer
/var/tmp/dumppanic
 after iBoot Autoboot
iBoot indicates storage dump CRC mismatch
iOS
i
rawBootFaults
fstat of %@ failed with error: %s
hw.memsize
invalid iBoot log metadata: (type %d) points outside of panic buffer : offset: %llu, size: %llu, bytes_read: %llu
 after iBoot kernel handoff
key_format
force
embedded-panic-header
AppleNVMePanicLogGetSize could not find panic log namespace service in registry.
 after AP Watchdog expired
version
default
decompress_stackshot
Whole
 after iBoot panic save power init
-PanicMedic_info
kern.kdp_corefile
OK
corrupt data
 AP Watchdog reboot
 after iBoot LLB start
1028387
AppleNVMePanicLogGetSize could not connect to panic log namespace service.
IOPMUPrimary
SOCD report detected: failed to read socd header
debug
OSAnalytics
bootFailCount
chip-revision
 (AIA crashed)
/var/cores/launchd.developm.core
OnlyUseNvramKeyStore
device unexpected reset
Failed to base64 encode storage dump of length %llu
r
/private/var/mobile/Library/Logs/CrashReporter/Panics/staged
device force reset
supported-legacy-panic-flow
ARMPanicSupport.m
remote_pmic
com.apple.mobile.keybagd.lock_status
invalid iBoot log metadata: (type %d) size invalid, found %llu, expected at least %lu
v16@?0@\"NSError\"8
hs:i:p:r:b:e:o:
,
 after iBoot start
iBoot panic-save unexpected reset, boot faults: %@
DumpPanic.PanicPatternMatchingWrapper
IOPMUBootErrorClear
clean restart
AppleNVMeReadPanicLogData failed to query panic log namespace size.
%s/staged
 after panic save chip reset initiated and x86 panic diagnostics were interrupted
IOPMUBootSOCD
-interrupted_coredump_paniclog
IODeviceTree:/defaults
wb
/var/cores/launchd.debug.core
Unexpected arguments
panic
AppleNVMeReadPanicLogData could not connect to panic log namespace service.
pthread_atfork
public_key_hash
  -i, --iboot-panic-header FILE\n              use iboot panic data binary file (struct iboot_panic_header)\n\n
kern.preoslog
plane
 during iBoot panic save reboot
pmu crash
v12@?0i8
panicprocessing
;
/var/mobile/Library/Logs/CrashReporter/ForceResetTailspins
invalid reset type
 after iBoot LLB end
 after iBoot end
bootAppHash
 (SMC panic)
core.%llu.gz
%02llX
btn_rst
%@%s%s.core.gz
Shared.m
864503
PanicReason
com.apple.DumpPanic.corefileSize
1176064
No valid SOCD nand container present
 after panic diagnostics were completed
 (Unknown)
 during sleep/wake transition
AppleDialogSPMIPMU
aeaDecryptStreamRead
corecrypto process rng
getentropy
EmbeddedDeviceTypePanicLog
nodeName
socd-iboot async abort
-[CoreFileHandler getCoreDumpNameWithIndex:]
\n\n%@
uv
  -s, --socd FILE\n              use socd binary file\n\n
-[ArgParser usage]
path exists but is not directory : %@
IOMedia
failed to clear PMU boot properties
AppleNVMePanicLogGetSize suffered from an unknown error.
AppleNVMeReadPanicLogData failed to read data from panic log namespace.
%@\n%@
 
fchmod of path : %@ failed with error : %s
/private/var/vm/kernelcore
dumppanic
PanicMedicEntryTimestampDiff
1.2.12
core
-[CoreFileHandler getPanicRegion]
No panic log found
yyyy-MM-dd-HHmmss
  -h, --help\n\t\t              show this help\n\n
-[CoreFileHandler getCoreDumpInfoWithIndex::::]
\n%@
Force Resets
ccrng failed assert cbc_info->block_size = %lu\n
BAD MAGIC! (flag set in iBoot panic header), no SOCD container available
ot
kcd_c_totalout
universalBootFaults
 iBoot Stage LLB start
 after iBoot panic save memory init
oc
/private/var/tmp/panicregion.XXX
PanicMedicEntryTimestamp
restoreos
IOPropertyExistsMatch
 iBoot panic save memory init
otherResetCount
0
Failed to create EmbeddedPanicDataDecoder instance
Failed to decode embedded panic data
plane_node
check_log_metadata
lz4DecodeStreamRead
cp.core.gz
Q
/private/var/mobile/Library/Logs/CrashReporter/Panics/staged/tempUserSpaceCore.XXX
%@.%s%@.core.gz
%s/%@
Unable to find usable panic log after traversing %d iBoot metadata logs
 (iBoot sync abort)
%s
-[CoreFileHandler getCorefileZeroRanges]
bootfault
embedded panic data not available
v16@?0@\"NSFileHandle\"8
 iBoot panic save entry
unlock_register
ccrng_process_atfork_child
alloc ws
cpu_therm
embedded_panic_header_corefile_fallback.bin
unknown
boot-args
kcd_c_type
Unexpected SoC (system) watchdog reset occurred
 (AWL panic)
panic region
 after iBoot panic save entry
NumCores
ips
panic_pattern_matching
free ws
  -h, --help\n              show this help\n\n
v8@?0
File a radar now?
socd-data
secure
macefi
  -e, --plane FILE\n              use plane panic test input JSON file with multiple nodes\n\n
UserSpaceCoreCompressed
/var/run/com.apple.DumpPanic.finishedThisBoot
kern.coredump_encryption_key
  -p, --embedded-panic-header FILE\n              use xnu panic data binary file (struct embedded_panic_header)\n\n
 panic DRAM flush
 AP Watchdog expired
chg_pok_fall
it rebooted after an unexpected reset
OTA UUID: %.*s\n
iBoot indicates CRC mismatch
/var/run/com.apple.DumpPanic.finishedPMUFaultHandling
timeout
 iBoot panic save storage init
-[CoreFileHandler getCorefileLogInfo:::]
Your device has rebooted after an unexpected reset
  -b, --bootfault FILE\n              use boot fault JSON file\n\n
Incident Identifier: %@\nCrashReporter Key:   %@\nDate: %@\nReset count: %@\nBoot failure count: %@\nBoot faults: %@\nBoot stage: 0x%x\nBoot app: %@\nsocId: %x\nsocRevision: %x
Unexpected force reset occurred
panicCount
gzipOutputStreamWrite
-[CoreFileHandler getCoreDumpEncryptionKey:]
full_key
panicRegionTempFile != NULL
it recovered from a panic
Unexpected Resets
 iBoot start
rst
com.apple.DumpPanic.KernelCoreDump
 after panic called
DumpPanic
com.apple.DumpPanic
AppleNVMePanicLogGetSize suffered from an internal error.
InDiagnosticsMode
Failed to generate random
SOCD report detected:
socd-ap watchdog
skipTTR
backpow
PanicDev
it rebooted after a force reset
ar:chf
 while panic DRAM flush in progress
socd-multi
%@/%llu.key
Error creating directory at : %@ : %s
.synced
UNKNOWN
iBoot panic header indicates invalid number of logs available (%d)
 x86 panic diags
 panic save x86 panic diags interrupted
sstate
[Warning: The attachments may contain privacy-sensitive sensor data.]
kern.bootargs
ResearchFuse
iBoot header contains invalid number of logs
DRAM panic log missing; corefile fallback log in use
kern.bootsessionuuid
coproc.core.gz
remove-socd-data
AppleNVMeReadPanicLogData received an invalid argument.
 after panic save chip reset initiated
PanicUtilArgParser
SOCDReportInfo
PanicProcessingAdapter
CoreFileHandler
PanicProcessingDelegate
LockedReadOnlyKeyStore
_TtC9DumpPanic27PanicPatternMatchingWrapper
ArgParser
CoresPruner
NSObject
CoreFileHandlerV1
KeyStore
DumpPanicArgParser
CoreFileHandlerV2
UserCoreFileHandler
ReadOnlyKeyStore
@\"NSData\"
v48@0:8@16@24@32@40
@32@0:8Q16Q24
I
@\"NSString\"16@0:8
@\"NSObject<OS_os_log>\"
@\"NSError\"
C16@0:8
@24@0:8:16
@32@0:8:16@24
@\"NSArray\"16@0:8
@48@0:8r*16I24d28B36@?40
@24@0:8Q16
@28@0:8^*16i24
@\"NSURL\"
B24@0:8#16
B24@0:8@\"NSString\"16
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}
B28@0:8i16@20
v16@0:8
@40@0:8:16@24@32
@44@0:8*16B24@28@36
B40@0:8Q16@24^@32
@36@0:8*16B24@28
^{ccec_cp=QQ^{cczp_funcs}[1Q]}20@0:8i16
@\"NSMutableArray\"
Vv16@0:8
@32@0:8@16@24
v24@0:8@\"NSString\"16
B60@0:8Q16Q24@32@40@48I56
?
v24@0:8@16
@60@0:8*16B24@28Q36^v44Q52
B40@0:8^Q16^Q24^I32
@\"ReadOnlyKeyStore\"
@32@0:8r*16r*24
B24@0:8:16
@24@0:8@16
@36@0:8@16I24@28
I16@0:8
B28@0:8I16^@20
@\"NSString\"28@0:8r*16I24
@28@0:8i16@20
@\"NSNumber\"
r*24@0:8Q16
Q
@24@0:8d16
v20@0:8B16
v20@0:8I16
B24@0:8@16
@40@0:8@16d24@32
{mach_core_fileheader=\"signature\"Q\"log_offset\"Q\"log_length\"Q\"num_files\"Q\"files\"[16{mach_core_details=\"gzip_offset\"Q\"gzip_length\"Q\"core_name\"[16c]}]}
v24@0:8^?16
v48@0:8Q16^Q24^Q32^I40
^v
@\"NSMutableDictionary\"
Q16@0:8
B24@0:8@\"Protocol\"16
@\"NSMutableDictionary\"40@0:8@\"NSURL\"16d24@\"NSString\"32
B56@0:8@16^@24^i32^@40^@48
v20@0:8C16
@\"NSString\"
@\"NSNumber\"32@0:8@\"NSString\"16@\"NSString\"24
^{mach_core_fileheader_v2=QIQQSQQQ[0{mach_core_details_v2=QQQ[16c]}]}
B
^{_NSZone=}16@0:8
@28@0:8r*16I24
B16@0:8
@16@0:8
C
#16@0:8
i
```
