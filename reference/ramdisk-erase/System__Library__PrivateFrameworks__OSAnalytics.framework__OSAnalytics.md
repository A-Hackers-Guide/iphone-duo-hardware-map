# `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 919,216 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 42 (Size: 6208)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (24)

- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication (compatibility version 1.0.0, current version 64578.104.1)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication (compatibility version 1.0.0, current version 64578.132.1)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_StringProcessing.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (39 classes, 2 protocols)

Classes: `ExclaveAddressSpace`, `ExclaveLayout`, `ExclaveStackEntry`, `ExclaveThread`, `FileUtils`, `KCContainer`, `NSArray`, `NSError`, `NSMutableArray`, `NSMutableDictionary`, `NSMutableString`, `NSString`, `OSABinaryImageCatalog`, `OSABinaryImageSegment`, `OSABridgeLinkProxy`, `OSACrackShotReport`, `OSADateCounter`, `OSADefaults`, `OSADiagnosticsReporterSupport`, `OSAExclaveContainer`, `OSAJetsamReport`, `OSALegacyXform`, `OSALog`, `OSALogTrackerObject`, `OSAOsLogPackParser`, `OSAParsedOsLogPart`, `OSAProxyConfiguration`, `OSAReport`, `OSASafeCreateDirectoryOptions`, `OSASharedCacheEntry`, `OSAStackShotReport`, `OSAStateMonitor`, `OSASymbolInfo`, `OSASystemConfiguration`, `OSASystemWatchdogCrashReport`, `OSATasking`, `_TtC11OSAnalytics11DeviceState`, `_TtC11OSAnalytics24WatchdogExitReasonHelper`, `_TtC11OSAnalytics9IPSReport`

Protocols: `NSObject`, `OSAConcreteReport`

## Strings (3,088)

First 2,500 of 3,088.
```
softlink:o:path:/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting
softlink:o:path:/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices
softlink:o:path:/System/Library/Frameworks/Accounts.framework/Accounts
softlink:o:path:/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess
softlink:o:path:/System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
softlink:o:path:/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
PIDListExtension
NSObject
OSAKCDataExtension
OSAStateMonitor
OSABinaryImageSegment
_TtC11OSAnalytics11DeviceState
OSATasking
OSAOsLogPackParser
OSALog
OSAExclaveContainer
OSASafeCreateDirectoryOptions
OSACrackShotReport
OSAReport
OSADateCounter
Trimming
OSAProxyConfiguration
OSASystemConfiguration
OSADiagnosticsReporterSupport
SectionStackExtension
optIn
ExclaveAddressSpace
ExclaveThread
OSALegacyXform
OSAConcreteReport
OSAJetsamReport
KCContainer
OSABinaryImageListExtension
OSABridgeLinkProxy
_TtC11OSAnalytics9IPSReport
OSABinaryImageCatalog
OSAStackShotReport
OSASystemWatchdogCrashReport
ExclaveLayout
ExclaveStackEntry
OSALogTrackerObject
OSALogTrackerExtension
FileUtils
OSASymbolInfo
OSAStackshotKCDataExtension
OSASharedCacheEntry
OSADefaults
OSAParsedOsLogPart
OSASanitizerCondensor
OSAXformAugment
_TtC11OSAnalytics24WatchdogExitReasonHelper
isExclaveValid
stringByExpandingTildeInPath
timeIntervalSince1970
_preserveFiles
_appleInternal
initWithObjects:
isAppleTV
T@\"NSString\",C,V_formatString
pathDiagnostics
isReadableFileAtPath:
setFileProtectionNone:
setValue:forKey:
_targetAudience
Ti,N,V_pid
_wiredBytes
getResourceValue:forKey:error:
integerValue
T{?=@},R
_exceptionCodes
dealloc
TB,V_createIntermediates
formatFrame:withImages:macosStyle:
osa_logTracker_trackLogTypes_internal:forOwner:rescan:
setThreadId:withScId:
_capture_absoluteTime
getExtraData:
numberWithShort:
Ti,N,V_jetsamLevel
_layoutImageCount
copy
indexOfObject:
T@\"NSNumber\",&,N,V_addressSpaceId
_oldLogFile
getPropsForLogType:
setTarget:
additionalRootsInstalled
T@\"NSDictionary\",R,V_metaData
appendFormat:
setFormatString:
submissionsDisabled
logExt:
hwModel
osa_logTracker_incrementForSubtype:signature:filepath:
hottestElided
optIn3rdParty
useStackshotData:frontmostPids:atTime:machTime:sequence:
isProxy
appleInternal
formatCallstacks:withImages:macosStyle:
userID
_logBlacklist
performSelector:withObject:
_reason
_stream
layouts
TI,N,V_ss_sequence
invalid_images
osa_logTracker_recordNixedDuplicate:
_ss_sequence
accountType
flags
getFramesForThread:usingCatalog:
isSafe
pathSubmissionWithHomeDirectory:
setSource:
_isComputeNode
body
T@\"NSMutableArray\",&,N,V_stackEntries
_thermalNotificationCurrentLevel
isEqual:
setString:
writeToURL:atomically:
initWithSource:size:for:source:
stringByAppendingString:
numberWithBool:
arrayWithObjects:count:
descriptionFromCode:
omit
original
stringValue
selectConfigFromBlob:withError:
setSharedCacheIndex:
writeToFile:atomically:
TQ,N,V_count
acquireJetsamData
addEntriesFromDictionary:
clearExclaveSharedCaches
codeSigningMonitor
pointerPointsToSafeMemory
spindump
markWithKey:value:
_releaseType
formatImages:macosStyle:
parent
stream
substringToIndex:
TB,R,N,V_isComputeController
JSONObjectWithData:options:error:
formatLastException:withImages:
decodeKCDataWithBlock:withTuning:usingCatalog:
frames
transferInternal:key:
_modelCode
orPredicateWithSubpredicates:
TQ,R
UUIDString
componentsSeparatedByString:
decode_cpuType
formatLastBranchState:index:withImages:
getStackshotData
multiUserMode
numberWithLongLong:
osa_logTracker_isLog:byKey:count:withinLimit:withOptions:errorDescription:
setFiles_to_attach:
uiCountryCode
_kernel_text_exec_segments
fileURLWithPathComponents:
frontmostPids
cpuType
_stringValue
augmentWithPrefix:
TB,R,N,V_isDefaultSharedCache
_extras
T^[37c],R,N,V_sharedCacheUuid
_logfile
_original
enumerateKeysAndObjectsUsingBlock:
layoutImageCount
numberWithUnsignedInt:
TI,R,N,V_ss_trace_length
_additionalPayload
processInfo
setReason:
stringByPaddingToLength:withString:startingAtIndex:
getDisplayState
currentLocale
_layoutId
dataWithJSONObject:options:error:
logDomain
regularExpressionWithPattern:options:error:
process
checkAndReportCALogStates
whitespaceCharacterSet
zoneInfo
bundleForClass:
appendString:
initWithSessionInfo:userInfo:frameworksToCheck:
setPrefsKey:value:forDomain:withSync:
sortedPids
_fileProtectionNone
createRetiredDirectory:
osa_logTracker_getForSubtype:forOwner:
sampleThread:
T#,R
T@\"NSString\",R,V_oldLogFile
pid
kernelVersionDescription
launchAppWith:options:completion:
queryThermalData
allKeys
_logPath
_pathCATasking
null
removeObjectAtIndex:
setOldestDate:
usesLegacySubmission:
URLWithString:
_isInDeviceRecoveryEnvironment
dateWithTimeIntervalSinceReferenceDate:
dictionaryWithContentsOfFile:
T@\"NSString\",R,V_releaseType
automatedDeviceGroup
copyItemAtPath:toPath:error:
localizedDescription
targetSharedCache:withSlide:atBaseAddress:
_argSpecifier
_logDomain
_pathDiagnostics
pathExtension
set
autorelease
setUsesSignificantDigits:
setJetsamLevel:
_sharedCacheUnreliableSlidBaseAddress
backtrace
fetchSnapshotWithFlags:error:
reason
T@\"NSString\",R,N,V_logfile
tracker
initWithArray:
sharedTrackers
T@\"NSString\",&,V_cpuArch
containsString:
ss_trace_length
installCATasking:withId:untasked:
pairedWatchOS
setSegments:
userAppName
writeData:error:
TQ,V_start
setSs_sequence:
initWithCapacity:
T@\"NSString\",R,V_productName
_getValueForKey:fromBody:orHeader:
locallyCreateForSubmission:metadata:options:error:writing:
TQ,R,N,V_sharedCacheUnreliableSlidBaseAddress
_productName
array
firstObject
_audioAssertionState
_layouts
capture_time
scanProxies:
zone
_hexDump:offset:indicator:
isWritableFileAtPath:
_size
initWithDomain:code:userInfo:
isDefaultSharedCache
numberWithDouble:
setModulePathForMemoryPointer:
transformURL:options:
_formatString
_isExclaveValid
streamContentAtLevel:withBlock:
T^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq},R,V_stream
T@\"NSString\",&,V_name
_setDumpedSuspendedJetsamLog
isComputeNode
uidForUser:
TI,N,V_flags
_oldFilePath
addObject:
characterAtIndex:
_symbolInfo
layoutId
T@\"NSString\",R,C,V_argSpecifier
T@\"NSNumber\",&,N,V_schedulingContextId
TQ,V_size
activateStreamFromDate:
getActivePairedDevice
initWithIncidentID:visibilityEndowmentState:audioAssertionState:
sortByAddressAndSetInferredSizes
T@\"NSString\",R,V_uiCountryCode
T@\"NSDictionary\",R,V_currentTaskingIDByRouting
TQ,V_used_index
_path
compare:
iterateLogsWithOptions:usingBlock:
setEtlKey:
ss_sequence
pop
_logType
_rootedCacheLibs
formatString
T@\"NSString\",R,V_bugType
_sharedCacheSlide
addStackEntries:
domain
removeItemAtPath:error:
_invalid_images
_isDefaultSharedCache
_thermalSensorValues
bundleWithURL:
initWithPath:forRouting:options:
setInvalidationHandler:
T@\"NSString\",R,V_experimentGroup
sortedArrayUsingDescriptors:
addWaitInfoDesc:count:elSize:
notes
setDREOptIn:
systemId
_includeSyslog
date
productNameVersionBuildString
resampleTruncatedBacktracesForTask:forThreads:usingCatalog:in:usingSymbolicator:
_seedGroup
addCustomField:value:into:
count
initWithKey:ascending:
performSelector:withObject:withObject:
timeIntervalSinceNow
oldLogFile
pathWithComponents:
T@\"NSString\",R,V_productNameVersionBuildString
T@\"OSASymbolInfo\",R,N,V_symbolInfo
_kernel_segments
signatures
TB,R,N,V_panicReportSubmissionDisabled
setOldFilePath:
initWithData:encoding:
pathComponents
removeItemAtURL:error:
rollSchemaForward:
setSize:
formatArm32ThreadState:index:
isEqualToNumber:
initWithBytes:length:encoding:
logPrefix:
osa_logTracker_incrementForSubtype_internal:signature:filepath:scan:
T@\"NSString\",R,V_buildVersion
_event_code
_cpuArch
_sharedCacheID
compose:
initWithMaxNumAruments:
path
TQ,R,N,V_sharedCacheSlide
checkCALogWrittenStatus
full_details
objectAtIndex:
objectForKey:
now
reportUsedImagesFullInfoUsingBlock:
additionalIPSMetadata
extractArguments:
getSyslogAtCaptureTime:forPids:andOptionalSenders:additionalPredicates:
markDescriptor:forKey:withObj:
objectForKeyedSubscript:
_createIntermediates
markFile:withKey:value:
setIncidentID:
transformJSON:header:error:streamingBlock:
_panicReportSubmissionDisabled
_procPath
identifier
isAllowed:forDomain:
initWithFileDescriptor:
details
_threadIdToScId
_pathRoot
crashReporterKey
valueForProperty:
_sharedCaches
mutableCopy
optInDRE
panicReportSubmissionDisabled
sendMessageWithCategory:type:payload:error:
setPath:
maxNumArguments
rename:
_count
type
_frames
T@\"NSString\",C,N,V_name
closeFileStream
TI,R,N,V_layoutImageCount
reportUsedImages
T^{dyld_uuid_info_64=Q[16C]},R,N,V_layout
_ss_trace_buffer
countByEnumeratingWithState:objects:count:
initWithDictionary:
T@\"NSString\",R,V_productVersion
isActionable
setAddressSpaceId:
setMaximumSignificantDigits:
initWithArgument:argSpecifier:isSafe:
logPathForType:at:options:
numberWithUnsignedLong:
setCreateIntermediates:
writeToURL:options:error:
_sharedCacheUuid
serialNumber
sharedCacheIndex
superclass
enabled
_countKey
initWithSymbol:source:
scanLogs:from:options:
_event_reason
_whitelistedDomains
isEqualToString:
isWhitelisted:forDomain:
visibleTopLevelAccountsWithAccountTypeIdentifiers:completion:
TI,R,N,V_sharedCacheID
currentTaskingIDByRouting
legacy_arch
T@\"NSString\",R,V_modelCode
logType
_ss_trace_length
numberWithUnsignedInteger:
setUserID:
appendBytes:length:
initWithSuiteName:
setSymbolicator:
setPid:
tag
T@\"NSString\",R,V_automatedDeviceGroup
sharedCacheUuid
retain
setOldestLogPath:
_isSystemWatchdog
T@\"NSMutableDictionary\",R,N,V_truncated_threads
infoDictionary
recoveryModeReason
T@\"NSMutableArray\",&,N,V_sharedCaches
_oldestLogPath
recordEvent:with:
setEventHandler:
submissionMetadata
T@\"NSString\",R,V_filepath
T@?,C,V_modulePathForMemoryPointer
_spindump
self
T@?,C,V_readCStringFromTarget
_pairedWatchOS
setResourceValue:forKey:error:
setDeleteOnRetire:
Tr^v,R,N,V_ss_trace_buffer
cleanupRetired:
arrayByAddingObjectsFromArray:
jetsamLevel
purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:
seedGroup
backtraceLength
T@\"NSString\",C,V_formatStringOriginatingModulePath
schedulingContextId
sortedArrayUsingSelector:
automatedContextURL
decode_reason:reason:
rangeAtIndex:
startConfigurationWithCompletionHandler:
randomizedCRKey
_shared_segments
addTurnstileInfoDesc:count:elSize:
exceptionCodesDescription
resume
_signatures
increment
markDescriptor:withPairs:andOptions:
pathSubmissionSubdirDiagnosticLogs
availableData
_automatedContextURL
addressSpaceId
push:
sortUsingComparator:
T@\"NSString\",R,V_identifier
setAdditionalPayload:
_recoveryModeReason
formatArm64ThreadState:index:
isReasonableSize:forRouting:
resampleUUIDsForTask:usingCatalog:
setHTTPContentType:
setFlags:
setWithObjects:
_killedActiveApps
setHTTPMethod:
_isSafe
isCustomerFused
stringByTrimmingColumnSensitive
initWithPath:forRouting:usingConfig:options:error:
TB,V_formatStringIsSafe
UUID
addImage:address:size:
getPrefsKey:forDomain:withOptions:
getThermalPressureLevel
isMemberOfClass:
setKernelImages:
dictionaryWithCapacity:
oldFilePath
problemType
subarrayWithRange:
T@\"NSString\",R,V_recoveryModeReason
TB,R,V_isArgument
_data
_isComputeController
filepath
initWithUTF8String:
scanLogs:from:
_targeted_cache
stringByAppendingPathComponent:
evaluateState
T@\"NSDictionary\",&,N,V_spindump
initWithKCData:
acquireStackshot
coldestElided
intValue
pathSubmission
setFrames:
T@\"NSString\",R,C,V_stringValue
hasPrefix:
initWithPath:options:error:
stringWithFormat:
stringWithUTF8String:
respondsToSelector:
initWithSource:
T@\"NSString\",R,V_hwModel
TB,N,V_includeSyslog
setSharedCacheInfo:
sharedMCProfileConnection
transformLines:withDefinitions:body:header:error:streamingBlock:
segments
setRootedCacheLibs:count:
T@\"NSString\",?,R,C
_productBuildString
incidentID
isInDeviceRecoveryEnvironment
isSnapshotDisabled
readXattrWithReader:errorContext:
UTF8String
isPaired
size
sysVersionData
transformURL:template:options:
removeLastObject
_automatedDeviceGroup
_uuid
dataWithCapacity:
preference:alreadySetInInstructions:
searchFrame:in:regions:result:
_carrierInstall
isSecurityResearchDeviceERM
pathSubmissionDataVault
_exclave_shared_caches
ephemeralSessionConfiguration
integerForKey:
sendOperation:forKey:withBlock:
T@\"NSArray\",R,N,V_notes
logPath
get_uuid
headerJson
isPrivateServerOS
modulePathForMemoryPointer
pathContainerRoot
_largestActiveApp
_submissionParams
indexOfObjectPassingTest:
retire:
isLowPowerModeEnabled
stringByDeletingPathExtension
_formatStringIsSafe
_identifier
_multiUserMode
_oldestDate
setSchedulingContextId:
Ti,N,V_unindexed_frames
T@\"NSString\",R,V_osTrain
TB,R,N,V_isPrivateServerOS
invalidate
_etlKey
_threads
plumbEmail:
systemIDWithDescription:
truncated_threads
setHTTPBody:
Td,R,N,V_capture_time
_addressSpaces
formatStringOriginatingModulePath
layout
removeAllObjects
arrayWithObject:
dateForEvent:
enumerateMatchesInString:options:range:usingBlock:
alreadyDumpedSuspendedJetsamLogToday
readCStringFromTarget
setFormatStringIsSafe:
statusCode
stringByTrimming
T@\"NSString\",C,V_oldFilePath
dictionary
initWithZoneNames:nameCount:zoneInfo:zoneInfoCount:wiredInfo:wiredInfoCount:
prepareTemplate:forLogType:error:
setSpindump:
_deleteOnRetire
isInLDM
_isPrivateServerOS
_modulePathForMemoryPointer
_truncated_threads
_zones
doubleValue
threadIdToScId
dictionaryWithObject:forKey:
setIncludeSyslog:
updateLogLimitFor:
setCpuArch:
setSharedCaches:
sharedCacheID
standardUserDefaults
temporaryFileWithPrefix:fd:
TB,V_fileProtectionNone
T@\"NSMutableDictionary\",R,N,V_layouts
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:
subdataWithRange:
TB,N,R
requestWithURL:
setObject:forKeyedSubscript:
unsignedLongLongValue
T@\"NSString\",R,V_path
addSuiteNamed:
buildVersion
etlKey
pathForResource:ofType:
processIdentifier
saveWithOptions:
setActions:
_dead_snapshot
_stackEntries
setUsed_index:
boolValForMCSetting:
data
dictionaryRepresentation
getTaskingKey:
lastPathComponent
sender
setKernelCache:address:size:
TB,V_deleteOnRetire
_factoryDevice
reduceToTwoSigFigures:
containsObject:
initWithString:
valueForKey:
T@\"NSString\",R,V_awdReporterKey
pathPreferences
debugDescription
removeObjectsForKeys:
TQ,R,N,V_capture_absoluteTime
logfile
setBool:forKey:
T@\"NSString\",&
hasXattrWithName:at:
sharedClient
_largestProcess
isKindOfClass:
T@\"NSDate\",&,N,V_oldestDate
ss_trace_buffer
initWithName:reason:exceptionCode:exceptionCodeCount:
CALogStateToString:
T@\"NSMutableArray\",&,N,V_frames
TB,R,V_isSnapshotDisabled
_templates
T^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII},R,N,V_original
_used_segments
hash
lastObject
numberWithUnsignedLongLong:
TI,R,N,V_type
_stackshot_config
defaultTasking
fileProtectionNone
modelCode
setCount:
_productVersion
boolValue
characterSetWithCharactersInString:
removeObjectForKey:
setKernelTextExecImages:
bugType
URLByAppendingPathComponent:
initWithIdentifier:
checkTaskingRelevance
dateByAddingTimeInterval:
hasSuffix:
isDataVaultEnabled
setFilterPredicate:
T@\"NSString\",&,N,V_etlKey
_pointerPointsToSafeMemory
appendNotesTo:
dataUsingEncoding:allowLossyConversion:
fileURLWithPath:
threads
_getSnapshotWithFlags:
allObjects
logObjForBugType:
optInApple
recordEvent:
_cpuType
overrideMountPath
setLayoutId:
userInfo
TQ,R,N,V_tag
filterOutSensitiveParts:withFormats:
getSyslogForPids:andOptionalSenders:additionalPredicates:
getXattrWithName:at:
_pid
_readCStringFromTarget
ensureUsablePath:component:options:
initAlertDelegate
localStore
randomlySelectForRetention:
experimentGroup
listXattrsAt:
productVersion
isFile:validForSubmission:reasonableSize:to:internalTypes:result:
parseKCdata:
resetCount
_notes
_osTrain
initWithType:filepath:metadata:options:at:error:
T@\"NSMutableDictionary\",R,N,V_threads
arrayWithCapacity:
generateLogAtLevel:withBlock:
initWithContentsOfFile:
initWithPid:
setStart:
stringWithContentsOfURL:encoding:error:
used_index
_dayKey
_type
floatValue
timeIntervalSinceReferenceDate
_segments
createIntermediates
factoryDevice
propertyListWithData:options:format:error:
setLog_path:
setObject:forKey:
TB,V_isAppleCode
_unindexed_frames
appleCareDetails
class
parsePortLabelContainer:
_pathContainerRoot
_serialNumber
addPart:
initWithPID:options:
stringWithFileSystemRepresentation:length:
_layout
TQ,R,N,V_maxNumArguments
_logWritingOptions
stringForObjectValue:
osa_logTracker_shouldRotateLog:
checkSubmissionStatus
initWithPid:procName:bundleID:exitSnapshot:reason:
reportNamePrefix
setSharedCacheLayout:andCount:
length
_formatStringOriginatingModulePath
initWithTask:
pathRoot
setValue:forHTTPHeaderField:
unsignedIntegerValue
bundleURL
_userID
release
_exceptionCodeCount
addExclaveSharedCache:
isArgument
searchFrame:in:result:
setPathRoot:
findBundleAtPath:withKeys:bundleURL:
init:fromMetadata:
setTimeoutInterval:
_termination_info
bootArgs
code
sharedCacheUnreliableSlidBaseAddress
T@\"NSArray\",R,N,V_frontmostPids
_snapshot
prepareWithCompletionHandler:
assembleMetadataAt:withOptions:
performSelector:
TB,R,V_isInDeviceRecoveryEnvironment
_buildVersion
acquireJetsamDataWithFlags:
setXattrWithName:value:at:
T@\"NSString\",R,C
dead_snapshot
vmRegionInfo
_killed_or_suspended_count
addressSpaces
moveItemAtURL:toURL:error:
numberOfMatchesInString:options:range:
oldestLogPath
dataUsingEncoding:
URLByDeletingLastPathComponent
_appName
localizedStringForStatusCode:
sharedCaches
T@\"NSMutableDictionary\",R,N,V_data
_internalKey
_tag
setStackEntries:
ensureConformanceOfFile:options:
substringWithRange:
formatInstructionState:index:
setDead_snapshot:
transfer:key:
isInternalBridge
productBuildString
sharedInstance
cleanupForUser:
T@\"NSNumber\",C,V_groupID
setIsAppleCode:
_isSnapshotDisabled
metadata
numberWithInt:
_isArgument
commonFieldsForBody:
setAutomatedDeviceGroup:
setLink:
source
getVMStatistics
_awakeSystemUptime
_incidentID
dateWithTimeIntervalSince1970:
defaultManager
insertObject:atIndex:
internalKey
seekToFileOffset:
_visibilityEndowmentState
filteredArrayUsingPredicate:
sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:isSnapshotDead:
_isSuspendedOnlyJetsam
_aleFlag
_used_index
removeObject:
addImageLegacy:address:size:name:path:arch:
T@\"NSMutableArray\",&,N,V_notes
_groupID
predicateWithFormat:
proxyTasking:taskId:usingConfig:fromBlob:
bootSessionUUID
.cxx_destruct
_flags
createReportMetadata:with:at:usingOptions:
initWithAddress:size:for:
instrumentEvents:
parse:
pathSubmissionForOwner:
stringByStandardizingPath
appendPortLabelInfo:portlabels:
Ti,N,V_invalid_images
T@\"NSString\",R,V_logPath
getEventPriority:terminationReason:priority:
getXattrBoolValWithName:at:
initWithSharedCache:atBaseAddress:
setFormatStringOriginatingModulePath:
_logConfig
formatX86ThreadState:index:
handleDiagnosticLog:logPath:patternMatchActions:files_to_attach:completion:
postFailureWithReason:
productReleaseString
setPointerPointsToSafeMemory:
start
stringWithCString:encoding:
bootUUID
initFromPath:
isConfigEnabled:
setIsExclaveValid:
conformsToProtocol:
markPurgeableLevel:path:
T@\"NSString\",C
executeWithTimeout:Code:
initWithLiteral:isSafe:
_name
setNotes:
targetAudience
timeIntervalSinceDate:
writeData:
T@\"NSMutableArray\",&,N,V_segments
T@\"NSNumber\",&,N,V_layoutId
getXattrWithName:onFile:
initWithFileDescriptor:closeOnDealloc:
T@?,C,V_pointerPointsToSafeMemory
_crashReporterKey
_hwModel
_sharedCacheIndex
unindexed_frames
T@\"NSString\",R
cleanupLogs:withFilters:error:
username
_awdReporterKey
T@\"NSString\",R,V_internalKey
processCALogEvent:eventPayload:into:
composedMessage
_bundleID
depth
indexOfObject:inSortedRange:options:usingComparator:
shared
arrayWithObjects:
evaluateCALogStates:
formatStringIsSafe
moveItemAtPath:toPath:error:
productName
submissionParam:
_kernel_cache_segment
awdReporterKey
carrierInstall
deleteOnRetire
top
_jetsamLevel
addJITImage:size:
stringByReplacingOccurrencesOfString:withString:
threadIdentifier
T@\"NSMutableDictionary\",R
_uiCountryCode
description
substringFromIndex:
addNotes:
captureTime
fileSystemRepresentation
initWithPath:forRouting:options:error:
isComputeController
metaData
pathCATasking
section_pop
TB,R
TB,R,V_isSafe
activityIdentifier
setDateFormat:
_frontmostPids
isOnDeviceLogType:
onceConfig
sharedCacheSlide
T@\"NSMutableDictionary\",R,N,V_addressSpaces
T@\"NSNumber\",&,N,V_sharedCacheIndex
T@\"NSString\",R,V_seedGroup
errorWithDomain:code:userInfo:
fastLane
saveToPath:
stringByTrimmingCharactersInSet:
_pathPreferences
_schedulingContextId
_start
isAddressInTargetedCache:
_productReleaseString
dataWithBytes:length:
longLongValue
releaseType
T@\"NSString\",R,V_targetAudience
Ti,V_source
init
TB,N,V_dead_snapshot
TB,N,V_isExclaveValid
stringByAppendingPathExtension:
addObjectsFromArray:
dataTaskWithRequest:completionHandler:
instrumentEventsWithAudioAssertionState:visibliltyEndowmentState:
T@\"NSString\",R,V_legacyAutomatedDeviceGroup
getAvailableTaskingRoutings
capture_absoluteTime
T@\"NSMutableDictionary\",R,N,V_threadIdToScId
_tags
argSpecifier
keyForEvent:
T@\"NSMutableDictionary\",R,V_signatures
groupID
_productNameVersionBuildString
boolForKey:
bootProgressRegister
getInstalledTaskIds
retainCount
sessionWithConfiguration:
cpuArch
T@\"NSString\",&,N,V_oldestLogPath
rangeOfString:options:
section_push:
setUnindexed_frames:
stringByReplacingPathBeforeComponent:with:
_currentTaskingIDByRouting
_maxNumArguments
initWithFilepath:type:
initWithUUIDBytes:
normalizeInstructions:forSamplingKey:
T@\"NSNumber\",C,V_userID
getLogBlacklist
objectAtIndexedSubscript:
setInvalid_images:
T@\"NSString\",R,V_crashReporterKey
initForPid:exitSnapshot:reason:
includeSyslog
rangeOfString:
stringByDeletingLastPathComponent
applyTasking:taskId:fromBlob:
oldestDate
sharedConnection
_targeted_slide
enumerateObjectsUsingBlock:
fileModificationDate
setGroupID:
dateFromString:
_metaData
setInteger:forKey:
setReadCStringFromTarget:
_submissionMetadata
effectiveBoolValueForSetting:
attributesOfItemAtPath:error:
isDeveloperMode
_isAppleCode
reverseObjectEnumerator
T@\"NSString\",R,V_systemId
osTrain
_absolute_segment
dictionaryWithValuesForKeys:
_addressSpaceId
TB,R,N,V_isComputeNode
_experimentGroup
componentsJoinedByString:
legacyAutomatedDeviceGroup
symbolInfo
samplingKey
_filepath
crashreporterKey
fileExistsAtPath:
isApplePath:orBundle:
_legacyAutomatedDeviceGroup
_systemId
appendData:
createForSubmission:metadata:options:error:writing:
createRetiredDirectoriesForUser:
fetchWiredMemoryInfo
numberWithUnsignedShort:
unsignedIntValue
_source
addFrames:
isAppleCode
setName:
shouldApplyPreference:forSamplingKey:
stackEntries
getAllXattrsAt:
bytes
markImageAsUsed:from:
name
symlink:
_bugType
_daysSince1970
dictionaryWithObjects:forKeys:count:
globallyUniqueString
T@\"NSString\",R,V_automatedContextURL
_capture_time
initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:
v52@0:8@16@24d32Q40I48
r^v16@0:8
q16@0:8
v40@0:8[16C]16Q24Q32
@\"OSASymbolInfo\"
@28@0:8i16@20
v40@0:8Q16@24@?32
Q40@0:8@16Q24q32
@24@0:8q16
B24@0:8@\"Protocol\"16
v40@0:8@16r*24r*32
v64@0:8[16C]16Q24Q32r*40r*48r*56
B64@0:8@16@24^Q32^Q40@48^@56
@20@0:8i16
v48@0:8@16r*24B32B36@?40
^{_NSZone=}16@0:8
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16@0:8
@28@0:8@16B24
v36@0:8@16@24B32
B16@0:8
^[37c]
v32@0:8r^v16I24I28
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}
v28@0:8B16@?20
i16@0:8
v20@0:8I16
^v
@40@0:8@16d24@32
@48@0:8d16@24@32@40
B48@0:8@16@24^@32@?40
v40@0:8@16@24r*32
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}28@0:8I16^@20
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}
@\"NSSet\"
@36@0:8i16^{exit_reason_snapshot=IQQ}20@28
i28@0:8B16@?20
B24@0:8Q16
^{dyld_uuid_info_64=Q[16C]}
Q16@0:8
@\"NSArray\"16@0:8
@24@0:8Q16
@56@0:8@16@24@32^@40@?48
C28@0:8I16@?20
[16C]
@24@0:8@?16
@32@0:8:16@24
i
B32@0:8@16r*24
@?
B64@0:8@16@24q32@40@48r^*56
I32@0:8@16@24
B64@0:8@16@24@32@40^@48@?56
B
i60@0:8i16@20@28@36{_CSTypeRef=QQ}44
@48@0:8@16@24@32^@40
v20@0:8B16
@48@0:8@16@24@32@40
@40@0:8@16@24^@32
@\"OSABinaryImageSegment\"
B40@0:8@16@24@32
@28@0:8d16I24
I16@0:8
r*16@0:8
@32@0:8{kcdata_iter=^{kcdata_item}^v}16
@32@0:8@16i24B28
@\"NSDate\"
@\"NSString\"8@?0
@\"NSDictionary\"
@32@0:8@16^@24
{?=@}16@0:8
v32@0:8Q16@24
v32@0:8@16@?24
B32@0:8q16@24
v32@0:8r*16r*24
d16@0:8
v24@0:8^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16
@40@0:8@16@24N^@32
B40@0:8@16@24^@32
v32@0:8Q16Q24
Q32@0:8@16@24
@32@0:8@16^i24
@52@0:8i16@20@28^{exit_reason_snapshot=IQQ}36@44
Q28@0:8@16i24
v44@0:8@16@24r*32B40
@24@0:8:16
@52@0:8i16@20@28^q36I44I48
v40@0:8@?16@24@32
r^v
v24@0:8@?16
{?=\"daFlow\"@\"NSObject<OS_os_log>\"}
v36@0:8i16@20@28
{kcdata_iter=^{kcdata_item}^v}32@0:8{kcdata_iter=^{kcdata_item}^v}16
B24@0:8r*16
@16@0:8
v28@0:8^{dyld_uuid_info_64=Q[16C]}16I24
v40@0:8r*16@24@32
v32@0:8@16@24
I
v32@0:8{kcdata_iter=^{kcdata_item}^v}16
v24@0:8@16
@\"NSMutableArray\"
@32@0:8^{exit_reason_snapshot=IQQ}16@24
@28@0:8@16i24
@32@0:8@?16@?24
^[37c]16@0:8
B24@0:8#16
@\"NSString\"
@36@0:8@16@24B32
@32@0:8[16C]16Q24
v56@0:8q16@24@32@40@?48
@32@0:8@16@24
@48@0:8Q16@24@32^@40
Q
@\"NSMutableDictionary\"
@56@0:8@16@24@32@40^@48
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16@0:8
@32@0:8@16r*24
@36@0:8@16i24@28
^q
#16@0:8
Vv16@0:8
v28@0:8B16@?<v@?@\"NSDictionary\">20
@24@0:8@16
v20@0:8i16
B44@0:8@16@24@32B40
@\"NSArray\"
B24@0:8@16
v24@0:8Q16
I40@0:8@16@24@32
@64@0:8@16@24@32@40d48^@56
v28@0:8i16@20
@\"NSDictionary\"16@0:8
v16@0:8
@48@0:8@16@24d32@40
@20@0:8B16
v24@0:8r*16
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}
v60@0:8r^v16I24@28d36Q44I52B56
B32@0:8@16@24
v28@0:8B16@20
@40@0:8Q16Q24[16C]32
@\"NSNumber\"
@\"NSString\"16@0:8
@44@0:8@16@24^q32I40
v56@0:8r^v16I24@28d36Q44I52
@?16@0:8
i32@0:8@16@24
d
@44@0:8Q16Q24[16C]32i40
@40@0:8Q16@24^@32
^{dyld_uuid_info_64=Q[16C]}16@0:8
@40@0:8:16@24@32
@40@0:8@16@24@32
v40@0:8@16@24^@32
q24@?0^v8q16
B24@0:8:16
AppleCareSupport: existing log is valid, %s
AppleCareSupport: ERROR[%d] failed to create %s, %s
Error reading %s: expected to read %ld bytes but read %ld bytes
Missing or invalid 'User' key
Auto deletion of '%{public}@'
Failed to set DRE opt-in value to %d
Invalid PayloadContent entry - expected dictionary
setPrefs: attempt to change protection class for '%@' returned %d: %d %s
Unable to load %@
Mount path can only be overridden in the device recovery environment
sent RTCReporting %@
new signature found -- but no room available
%@
Saved da3 tasking for deferred installation
Using ACAccountPropertyIdentityEmailAddress to fetch email addresses.
Skipping log limit check on proxy-configured device with disableLogLimits set
Error while writing file: %{public}@
Logfile '%@' allowed for submission for testing
Logfile '%{public}@' blacklisted from submission
Logfile '%@' rejected for submission: missing metadata (or fread errno %d)
AppleCareSupport: rolling log -> %@
synthesizing %d items from payload as metadata
Unable to retrieve file attributes at path %@. Error: %@
memorystatus_control for command %d returned unexpected valud of %d which does not match buffer size of %d
Report of type '%{public}@(%@)' not saved because the destination is unavailable
Failed to call getBootProgressRegisterMethod with error: 0x%x
AppleCareSupport: scanning '%s'
unrecognized date format %d
Missing 'Value' key for %@ / %@ / %@
No addresses fetched. So using username. %@
%@ is valid but couldn't stat or it's not a directory
sending sync request to %@
Logfile '%@' fstat errno %d
C4. write payload using file descriptor (%d)
crash_mover service FAILED with XPC error: %s
Failed to list xattrs at path '%{public}s': error %d (%s)
Expected a task specific shared cache with ID %{public}@ but none was found
Logfile '%{public}@' not submittable on opted out device
(C6. report request completed successfully, but no filename returned!)
Identified heartbeat mismatch. Reporting to RTC now.
Tasking blob was not encodable: %@
failed to save ca1 tasking: %@
Failed to convert %@ to an XPC object
unable to override default log root location because already set as %@
RTCReporting.framework is unavailable
Exclave frames offset of %d for thread %llu is invalid
DiagnosticsReporterServices.framework is unavailable
After normalization, combinedConfig is %{public}@
saving ca1 tasking as %@
Failed to retrieve a valid user to access preferences container for key %{public}@
Unsupported ips/xattr type %@ for '%@'
Cleanup %s '%{public}@'
no URL for '%{private}@'
failed to set NSURLIsExcludedFromBackupKey '%{public}@': %{public}@
Unable to move tmp file '%{public}@': %{public}@
Error retiring '%{public}@': %{public}@
Error setting protection class after retiring %{public}@: %{public}s (%{public}i)
path is not whitelisted for listing: %@
task_config is %{public}@
osanalyticshelper replied with an XPC error: %s
setPrefs: not created '%@' returned %d: %d %s
failed to modify permissions of %@: %s
Got xpc error message from %{public}s: %{public}s\n
failed to save proxy tasking: [%d] %s
removing outdated da tasking (and restoring hotship) %@ -> %@
Unable to dynamically load NanoRegistry framework
=== Attempted change gid on new dir: %{public}@ from %d to _analyticsusers (%u) with result %d %{public}s
scanned %zu logs with %lu types and %zu unknowns (sentinel is %@)
Error: bug_type key not found in report header
defaultConfig is %{public}@
Logfile '%{public}@' invalid for submission: no type
failed to get pressure level state: %d
report not saved because it is non-actionable (ie: extension hangs or internal-only)
Successfully set DRE opt-in value to %d
Not in DRE, ignoring request to set DRE opt-in.
Failed to update header as the provided data is not valid JSON
Saved type '%{public}@(%@)' report (%lu of max %lu) at %{public}@
AppleCareSupport: event \"%@\"
Skipping transfer from unsupported device
Error initializing report: unable to convert body stream to data
Opted in for DRE
failed to modify ownership of %@: %s
found prefix in domain %@
OSLogEventStream query '%@'
OSLogEvent unsupported in this environment
No XPC connection to %s
JSON ERROR: %s, payload:\n%s
Error getting system group container: %llu
locallyCreateForSubmission: Failed to create copy of data vaulted crash report with error %@
crash_mover service FAILED to connect
Failed to set ownership while creating %{public}@: %s
Error retiring %s/%s while purging logs
Running the state monitor.
*** ignoring non-numeric symbolLocation: '%@'
Failed to set xattr '%s' at path '%s': error %d (%s)
Not applying %@ as it is sampled and this device isn't IN
Forcing Multi User Mode behavior due to the presence of /var/db/forceMultiUserMode
synced after %lld total events
Log::initWithPath:'%@' forRouting:'%@' options:%@
Logfile '%@' is too old for submission
Moving source file '%{public}@' into submission directory
Failed to remove retiring log '%{public}@': %{public}@
Failed to retrieve creation date from %@: %@
chmod(%d)
C4. ERROR Unable to reply
Failed to remove retired log '%@': %@
Error deleting non-retirable log at %s/%s while purging: %@
no bundle found
NSBundle URL refined %@ to %@
Unable to load ManagedConfiguration, falling back to MobileGestalt
Will discard keys: %@
validated %@@%@:%@=%@
mode ok
failed to get display state: %d
AppleCareSupport: new %s
Error issuing sandbox extension: %i (%s)
Invalid connection to %s. Caller may need sandbox exception.
Not purging %s/%s: log did not meet criteria
crash_mover service returned ambiguous response, assuming failure
AppleCareSupport: ERROR unable to intialize data
releasing RTCReporting
samplingKey [randomizing due to failure] was %{public}@
Logfile '%{public}@' type %{public}@ invalid for platform
C6. report request completed: %s
OSLogEventStream enumerate from %@ to %@
Failed to retrieve DRE opt-in value
search for matches in '%@'
checking domain %@ prefix '%@'
local log create type %{public}@ result %@: %{public}@
C5. payload writing complete, return status %d
C1. request '%@' report service via XPC/osanalyticshelper
Unable to get XPC connection to osanalyticshelper for DRE opt-in get
AppleCareSupport: ERROR[%d] opening %s, %s
Expected a task specific shared cache with id %@ but none was found
Invalid regex '%@'
Attempted xpc_user_sessions_get_foreground_uid() while fetching preferences for key %{public}@ but failed with error %{public}d - %{public}s
SimulateCrash() on another process is not supported
created directory '%{public}@'
Failed to fetch UID from unknown user '%@'
Couldn't config private XPC connection
Couldn't get XPC connection to %s
CFBundle URL refined %@ to %@
AppleCareSupport: ERROR[%d] scanning '%s', %s
'%{public}s' is not safe because it has at least one hard link
setPrefs: can't open '%@': %d %s
FAILED untrusted path validation '%{public}@' -> '%{public}@' [%{public}@]. Error: %d %s
=== Attempted change gid on existing path: %{public}@ from %d to _analyticsusers (%u) with result %d %{public}s
Exclave data not present for thread %llu
error configuring RTCReporting
known duplicate signature
tasked blacklist: %@
Error while writing ips header: %{public}@
Failed to get attrs for retired log '%@': %@
processing %zu events from queue
failed to create registration token for pressure level: %d
evaluate domain %@ (%@) option %@ check %d
Failed to find subdirectory for proxied device with ID %@
Stackshot requires reason; ignoring request
Removing old log '%@'
AppleCareSupport: WARN: limit exceeded, ignoring event
Path was safe to open, but no block was provided
Failed to stat '%{public}s'
event queued pending RTCReporting intialization
unique signature: %@ from original %s
Fetched addresses: %@
Log cleanup request successfully completed
Failed to release sandbox extension: %s (%i)
%s: %@ vs %@
unable to allocate %d bytes for wired memory info
no blacklist tasking: applying default: %@
Skipping rename of %{public}@ because the updated path is nil.
No matching service found
Failed to safely open '%{public}s': %{public}s
Logfile '%{public}@' tagged DoNotSubmit
group ok
Using system group container: '%{public}@'
Error creating temporary file for symbolicated log
Skipping transfer from proxy-configured device with disablePushOnWrite set
Warning: Logfile '%{public}@' type %{public}@ routing %{public}@ does not match config %{public}@
overriding default log root location to %@
Invalid XPC response
client log create type %{public}@ result %@: %{public}@
Failed to modify permissions while creating %{public}@: %s
unable to lookup port for %@
Gathering non-mobile logs via crash_mover
xpc error message from %s: %s\n
Report data has unexpected number of elements: %ld
Not applying %@ as it has already been set
scan: skipping '%@': failed to find a matching routing
unsupported log type '%@' effective (%@)
successfully applied ca1 tasking update: %@
Unable to load Accounts framework
Report of type '%{public}@(%@)' not saved because the limit of %lu logs has been reached
Failed to get the data vault submission path.
crash_mover is taking too long!
ips metadata not detected (%ld bytes before newline), attempting to read entire file as payload
Failed to convert to header to json
Missing or invalid 'Key' key for %@ / %@
Unable to dynamically link NRPairedDeviceRegistry from NanoRegistry
Using kDAAccountEmailAddress to fetch Exchange email addresses.
Logfile '%@' failed to open (errno %d)
applyTasking routing %@ id %@ length %d; untasked %d
found ManagedPreferences pref %@: %@
Failed override mount path: current root paths did not start with expected prefixes
parts %d (%@), new_parts %d (%@) mask %d
Logfile '%@' rejected for submission: bad metadata (or json error %@)
failed to remove previous ca1 tasking: %@
setPrefs: delete old prefs and create placeholder
owners: %d, %d mode 0x%X
scan: including '%@' (explicitly added)
scan: including '%@'
scan: skipping '%@': hit log limit
Failed to read developer mode status: %{darwin.errno}d
%s %@
crash_mover service FAILED on setup: %s
failed to extract JSON data from speedtracer result: %@
ns2xpc: unrecognized class: %@
Failed to read %s: error %d (%s)
Failed to create symbolicator
Missing or invalid 'Domain' key
Not sending Core Analytics events because snapshot is missing.
failed task_read_for_pid with %d
Failed to open log directory '%s': %s
Failed to mark %s as purgeable %d (%s) (flags 0x%11llx)
No reply received from osanalyticshelper for DRE opt-in request
unable to convert localtime from %ld secs
Tasking selection error: %@
Logfile '%{public}@' invalid for submission: unknown type %{public}@
creating type %{public}@ as %{public}@
createForSubmission: %@ metadata: %@ options: %@ block: %p (by %@)
Got xpc error message from %s: %s\n
C4. ERROR no file descriptor (%d)
Error while writing report payload: %{public}@
Retrieved DRE opt-in value: %d
C4.! payload writer exception: %@
Exclave data not present for SCID %@
Write failed to file %s - %zd of %d bytes written - uid: %d gid: %d, euid: %d egid: %d - error %d: %s
new signature found -- prioritizing over duplicate (removing %@)
deferring da3 task failed
failed to create directory '%{public}@': %{public}@
Removing old retired log '%@'
Initializing event date for %{public}@
xpc2ns: unrecognized type: %p
Failed override mount path: failed to generate new root paths
Logfile '%@' is too large (%lld) for submission
Retaining additional log with bug type %{public}@
Failed to override opt-in for '%@' log: option not supported when moving a log
OSLogEventStream found %lu lines after %.1f secs (invalidation: %@)
speedtracer error response: %@
Sandbox extension token was missing.
Error listing xattrs at path '%{public}s': expected to read %ld bytes but read %ld bytes
DiagnosticsReporter or DiagnosticsReporterLaunchOptions class not found.
failed to write CA tasking blob to temporary path: %@
Error while serializing ips metadata %{public}@. Error: %{public}@
Failed to get the home directory submission path for %{private}@.
%{public}s %@
AppleCareSupport: purging old (limit %d vs actual %d) %s
SpeedTracer response %d '%@' received %d bytes\n
Error initializing report: unable to serialize header as JSON
nothing to do for ca1 tasking update
failed to clean up ca1 tasking: %@
memorystatus_control for command %d returned %d - No data available
Submissions were disabled over a week ago: re-enabling submissions
Cleaning up retired logs (in %@)
Failed to open service %@ with error: 0x%x
%@ taskId %@ with rawblob (%lu bytes) is inconsistent
Failed to remove old log '%@': %@
%s
error configuring RTCReporting; initWithSessionInfo failed
Unknown KCDATA CONTAINER %X
failed to send tasking availability notification to analyticsd
owner ok
failed to create registration token for display state: %d
C6. report request failed: %s
OSLogEventStream query ALL
No reply received from osanalyticshelper for DRE opt-in get request
Error reading report %{public}s: %s
The location of the CA taskedConfig is %{public}@
found fallback user defaults %@: %@
Unexpected tasking value type for key 'fastLane' (type: %{public}@, value: %{public}@) encountered
Failed to stat %@ while creating Retired directory
unable to run sysctl hw.machine
Unable to determine UUID for host. Error: %d %s
intializing RTCReporting...
memorystatus_control for command %d failed with error %d
XPC Response: '%s'
Unable to set xattr '%@', errno=%d: %s
Creating Retired directory in %@
crash_mover service %s
AppleCareSupport: ERROR[%d] setting xattrs on %s, %s
Failed to stat %{public}@ when checking group ownership: %s
this log appears to be from the DA grid, using parsedData section
C3. private back-channel connection established
RTCReporting Realtime: sendOneMessageWithSessionInfo succeeded
configured RTCReporting with session id: %d
Sparing %s '%{public}@'
State monitor observed a failure: %{public}@
Event within submission window. Ignoring, will pick up next run.
=== Attempted change perms on new dir: %{public}@ from 0x%X to 0x%X with result %d %{public}s
linking RTCReporting.framework
Configured value for submissionsDisabledSince key is not in the expected format: deleting key
%@ could not be safely opened
failed to create VMUProcInfo
Error creating file %{public}@, %{public}s
unable to strftime with format '%s' from %lds+%dus}
Process %{public}@ [%d] killed by jetsam reason %{public}@
chown(%d, -1)
chown(-1, %d)
Failed to get the root submission path.
Error getting security.codesigning.monitor: %d %{public}s
scanning logs...
found containerized defaults from %@: %@
%@:\n%@
Couldn't get XPC connection to %{public}s
AppleCareSupport: ERROR[%d] rename failed, %s
nixed dupes bumped to %d on original %s
Failed to generate temporary file: error %d (%s)
Logfile '%{public}@' is too large (%lld) for submission
setPrefs: already class D '%@'
*** found alternate bundle
Failed to set file protection class while creating %{public}@
RTCReporting Realtime: sendOneMessageWithSessionInfo failed
Failed to launch DR with error: %@
Successfully overrode mount path. New root path: %@. New container root path: %@
marking failed for %@, [%d] %s
Skipping safe open because no path was provided
Failed to consume sandbox extension: %s (%i)
=== Attempted change perms on existing path: %{public}@ from 0x%X to 0x%X with result %d %{public}s
no reason to scan
Error creating log at %s/%s while purging: %@
Error loading full report: %{public}@
duplicate signature: %@
proxy %@ taskId %@ with rawblob (%lu bytes) is inconsistent
Expected to find xattr with name %s at '%s', but it was missing
WARNING: Failed to close %@. Please do NOT call -[NSFileHandle closeFile] errno=%d: %s
%{public}@
Retiring (%{public}@) %{public}s '%{public}@': %s
Unable to get XPC connection to osanalyticshelper for DRE opt-in
symbolLocation
rsp
platform
turnstileInfo
Failed to get jetsam status list (query returned %d)
Preferences
    last <keeping    > => %@[%@]
__KEEP_ONE
pll.anon
extensions
%@_CountLimit
TH_SFLAG_RT_CPULIMIT
Primary
keep       
  [%02d] (%@) -> (%@)\t%@
unknown type %u (owner %llu, context %#llx)
processUptime
sbin
presig_hash
CrashReporter
+[OSABridgeLinkProxy setLink:]
OSASandboxExtensionKey
QOS_CLASS_UTILITY
modify_gid
Public
sourceFile
log_filepath
port %#llx owned by kernel
cow_faults
systemTime
vm-pageshortage
disk-space-shortage
kern.version
/usr/lib
lastSuspendedLogDumpedDaySince1970
DeviceClassNumber
Too few path components
X-ST-GroupName
OSAnalytics
B24@?0r*8r*16
...%@
Delete oldest file failed
-%u
compressions
stackshot_duration_outer_nsec
dirty
TH_SFLAG_EXEC_PROMOTED
GM
%F-%H%M%S
%@ (%@)
original_perms
331
Error creating temporary file for symbolicated log
imageIndex
tmp1
%F %T.%%04u %z
kThreadTruncUserAsyncBT
zoneMapCap
table
@files
%s/%s
-[OSAReport streamContentAtLevel:withBlock:]_block_invoke
locked port %#llx
 
bootArgs
TH_SFLAG_PRI_UPDATE
%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x
fastLane
/private/var/mobile/Library
namespace
customerFused
reportNotes
UnknownType
override-fileName
LockdownModeManager
value
os_build
308
u
com.apple.OSAnalytics
ProxiedDevice-
%@-%@%@
optInStatus
Version
largestZone
observer_info
-------------------------------------\nTranslated Report (Full Report Below)\n-------------------------------------\n
TH_UNINT
com.apple.osanalytics.submissions.retire
_sharedProxyInstance == nil
exception_code
stackshot_duration_prior_nsec
donatingPids
boot_time_appx
restrictedBool
Thread:%@; Layout info does not exist for layout id %@
uuid_faulting
boosted
stackshot inclusion disabled
Spelling
CA_endTimestamp
Log limit exceeded
defaults_value
vm-pageout-starvation
largestZoneSize
multi_user_mode
 owned by pid %lld
v16@?0@\"NSObject<OS_xpc_object>\"8
no-compressor-space
internal
Log age filter incorrectly formatted
com.apple.OTACrashCopier
com.apple.osanalytics.AppleCareSupport.open
macOS
userTime
kThreadSuspended
Removal
Shared
rejected-age
/usr/bin
<item>
usedImages
v8@?0
suspended-only jetsam log already dumped today
share_with_app_devs
/Users/USER
Perl
submission-http-post-started
imageOffset
rsi
savedAs
synced
Log cleanup request failed. Error: %s
rdi
Thread %d instruction stream (single cacheline):
pids
foreground
OSATasking.m
StagedVolume
bug_type
[section_stack count] == 1
xform-metadata
stackshot_tuning
timesDidThrottle
blob failed to unserialize (error %@:%ld)
retiredReason
Thread %d%@:
analyticsd_sub
unknown failure to apply ca1 tasking
system_ID
@keep
expired
dupes
MATCH
__BUNDLE
Unable to read JSON
osanalytics_monitor_hb_diff
Terminated by Unblock framework for unrecoverable deadlock
qosOverride
;
alternate
MSK
override-limit
logLimitRate_309
symbol
%18p - %18p %@ %@  <%@> %@
action
298_LOW_PRIORITY
Updates
tmp
kern.bootsessionuuid
-[NSMutableDictionary(OSALogTrackerExtension) osa_logTracker_isLog:byKey:count:withinLimit:withOptions:errorDescription:]
input of String.init(cString:encoding:) must be null-terminated
MIDI Drivers
q
%@\n%@%@\n%@\n
free
q24@?0@\"NSString\"8@\"NSString\"16
StartupItems
UDID was null
ca-log-written-new
queue
esr
portlabel_info->portlabel_id == portlabel_id
suspensionDuration
OSAnalytics/Preferences
Invalid XPC response
zero_fill_count
Thread %llu has an incorrect exclave frame offset %d
schedPriority
TH_SFLAG_ABORT
disabled
submission-logs-added-to-archive
far
task_threads() for %d failed
uuidResampling
SecurityAgentPlugins
@executable_path
{%@}
priorities
TH_RUN
senderImagePath CONTAINS[cd] %@
metriclog
%lu
vnode-limit
298_ALE
state-monitor.ca.allLogsInfo
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_SCRESULT)
x86_THREAD_STATE
unknown-%u
WATCHDOG
KPX
iTunes Plug-ins
caller
id
TH_SFLAG_NO_SMT
low-probability-of-use
%@:%@
com.apple.iokit.hid.displayStatus
/Volumes/NETWORK
dev
%hhd
suspending
com.apple.da
/Library/Preferences
ThermalPressureLevelTrapping
rejected-fopen
Analytics-2
/sbin
com.apple.
227
Thread %llu has exclave frames but no kernel frames
rawFlags
v32@?0Q8r*16r*24
_dyld_process_info_create(%d) for resampling UUIDs failed with %d
missing stackshot buffer or size
proxiedDeviceID
rejected-fstat
ARM-64
binaryImages
low-swap
low-private-shared-ratio
device_in_recovery_mode_with_reason
<descend>
v20@?0I8r^{exclave_textlayout_segment=[16C]Q}12
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
 nope
locked 
 (service throttled by launchd)
container && (container.type == STACKSHOT_KCCONTAINER_THREAD)
plist
w
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_IPCSTACKENTRY)
kernelFrames
PayloadType
ColorPickers
<%lu>
inline
rip
instructionState
product
disable-panic-report-submission
create-tmp
Unable to access log from existing file
FAILED
foundLogs
kRTCReportingSessionInfoBatchEvent
suspensionLastEnd
!KCDATA_ITER_FOREACH_FAILED(kcData)
%lx
deployVersion
.synced
twoHrHeartbeat
state-monitor
%@\t%18p %@
v16@?0@\"OSLogEventProxy\"8
general.log
instructionStream
osatool
ThermalPressureLevelSleeping
lastSubmissionStartTimestamp
untasked
/
Retired
succeeded
v32@?0@\"NSTextCheckingResult\"8Q16^B24
portlabels
none
Plug-Ins
private
urgent
ReopenPath
threadTriggered
ioStats
Logs/CrashReporter
termination
<inactive>
ARM64_32
RTCReporting
pagesWanted
taskId
hhu
log_types
displayName
DeviceDefaultsToAnalyticsOptIn
<unavailable>     
kThreadDarwinBG
highwater
variant
alt-metadata
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_TEXTLAYOUT)
log_content
QOS_CLASS_UNKNOWN (%u)
assertion
fds
/System/Library/PrivateFrameworks/OSAnalytics.framework/submissionConfig.plist
modelCode
NetworkVolume
  error
ProxiedCrashCopier
/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
ACAccountTypeIdentifierExchange
/System
r14
ARM_THREAD_STATE32
Error reading file stream
incident
defaults_key
%u
com.apple.ReportCrash
memorystatus_control returned unexpected value - %d: %s
procName
]
ca-2hr-heartbeat
radars
krwlock %#llx for writing
TALEngaged
Success
absoluteTime
paging
eOS
v16@?0@\"NSFileHandle\"8
187
non-parseable kc snapshot buffer
-[OSAExclaveContainer parseKCdata:]
turnstile had unknown status (flags: 0x%llx)!
exception
invalid_images
residentMemoryBytes
modify_gid_value
HomeDirectory
datawriter_endpoint
%F %T.%%02u %z
lastMadeRunnableTime
killDelta
disableWatchdogStackshot
ThermalPressureLevelLight
 in spin mode
csFlags
User
DoNotSubmit
Input Methods
<exempt>
-[OSAReport streamContentAtLevel:withBlock:]
OSALegacyTransform
TaskingPayload
%p + %llu
r8
LibraryDirectory
iChat
incident_id
application/octet-stream
ers_namespace
resampledUserFrames
codeSigningAuxiliaryInfo
Product
visible
/private/var/containers
@loader_path
TH_SFLAG_PCORE_ONLY
excess-shared-memory
uncompressed
rejected-unregistered
progname
/AppleInternal/Library/OSAnalytics/defaultTasking.plist
triggered
com.apple.osanalytics.logs.sandboxViolation
com.apple.Jetsam.Kill
reject_reason
Missing CA log after rollover
speculative_count
copyOnWriteFaults
mask       
Analytics-Never
kern.roots_installed
r9
r15
kernel mutex %#llx
error_code
-[OSAReport generateLogAtLevel:withBlock:]
Log submission is overdue
409
kernel returned (0) from memorystatus_control(MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT) -- no jetsam data available
2
fc-thrashing
PrivateFrameworks
.pll.anon
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_ADDRESSSPACE)
  cr2: 0x%016qx\n  \nLogical CPU:     %d\nError Code:      0x%08x %@\nTrap Number:     %d\n
Unable to load log '%@'
 owned by thread %lld
swapouts
TH_SFLAG_ECORE_ONLY
Unable to create a new log file
Couldn't config private XPC connection
\\$\\((([^\\)\"]+|\"[^\"]+\")+)\\)
\nIncident Identifier: $(metadata:incident_id)\n^(!isBeta)CrashReporter Key:   $(crashReporterKey)\n^(isBeta)Beta Identifier:     $(storeInfo.deviceIdentifierForVendor|\"Unknown\")\nHardware Model:      $(modelCode)\n^(codeName)Device Model
operation
TaskingOS
/private/var/mobile
codeName
app_description
POST
sampleTruncatedStacks
inactive
speculative
TH_SFLAG_THREAD_GROUP_AUTO_JOIN
Invalid XPC response from %s
ErrorFileNotFound
monitoring timed out for service without diags
PostgreSQL
%p + %llu%@%@
isLiveImpDonor
dyldCompactInfoTriedFault
llx
failed
frames
%@lock %#llx
298_HIGH_PRIORITY
Unable to move tmp file
plugin
<incident x>
is_corpse
os_version
v12@?0i8
Spotlight
override-filePrefix
v24@?0Q8@\"OSLogEventStreamPosition\"16
Unable to load full report.
busyBufferCount
captureTime
LaunchDaemons
AppleInternal
.mss.anon
mach_msg send on port %#llx in transit to 
stacks
user_usec
JetsamEvent
<unknown (error %d)>
}
source
Failed to open intermediate path
purgeable_nv
state-monitor.%@
327
%02X
purges
<unprintable>
kKernel64_p
model
ARM
trap
rax
deviceMetadata.proxy
Alternate
q24@?0@8@16
OSALogCleanup
cacheLine
lastBranchState
https://speedtracer.apple.com/api/v2/trace?detail=full
osanalytics_beacon
resampledAllImages
dyldCompactInfoNone
kThreadTruncUserBT
%@_0x%04X
kDAAccountEmailAddress
Internet Plug-Ins
include-hidden
Unable to open file '%@': [%d] %s
0x%llx
resampled_images
kThreadTruncKernBT
mobile
IsComputeController
com.apple.osanalytics.logRetentionCount
com.apple.osanalytics.osanalyticshelper
serial
pagesReclaimed
unindexed_rs_frames
isSafe: %d, isArgument: %d, stringValue: %@
vm-compressor-thrashing
errno
v24@?0@\"OSLogEventSource\"8@\"NSError\"16
queue that is suspended
PayloadContent
@
tags
IODeviceTree:/product
SubmissionPolicy
%@ %@ 0x%05llx 0x%llx %@[%d] (%@): %@%@
OSALegacyXform
OSAStackShotReport.m
<null>
cpuType
r10
isSimulated
var
Unable to open file
hw.machine
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
pthread rwlock %#llx for reading
resampleIncomplete
\nProcess:               $(procName|\"???\") [$(pid|\"Unknown\")]\nPath:                  $(procPath|\"???\")\nIdentifier:            $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:       
internal_key
lastExceptionBacktrace
vmRegionInfo
crashReporterKey
QOS_CLASS_DEFAULT
content invalid
awd_device_ID
submissionTime
logs
%@Count
throttled_count
systemDefaultSharedCache
failed to generate temporary file
dyldCompactInfoFaultedIn
%ld
neuralPages
thermalPressureLevel
free_count
suspendCount
 Crashed
--%@--\r\n
TH_IDLE
com.apple.osanalytics.bundlereader.serialqueue
flavor
pageIns
/private/var/mnt
/Library/CoreAnalytics
Unknown
bootSessionUUID
Install
ers_code
frontmostPids
backboardd
Incomplete XPC result -- no filename
kRTCReportingSessionInfoContainsRealtimeEvents
lookups
visVisible
suspensionCount
TH_TERMINATE2
create_dir
ThermalPressureLevelHeavy
lastSubmissionError
-[OSABridgeLinkProxy transferInternal:key:]
port %#llx name %#llx
No jetsam status list available (size query returned %d)
\r\n
~/Library/Logs/DiagnosticReports/
, 
frozen
Extensions
datavault-filePath
capture-time
prependString
blocked on %lld, hops: %d, priority: %d
@mask
Dictionaries
Security
file-owner
ErrorHTTPPost
Thread %d instruction stream:
Unable to transform log
resampled %d of %d images missing from %d pids: %@
product_version
ips
ACAccountStore
329
+[OSAStateMonitor processCALogEvent:eventPayload:into:]
state
resampled %d of %d threads with truncated backtraces from %d pids: %@
Domain
<whitelist>
ca-log-written
pc
intransit port %#llx
suspensionSources
reads
eventCode
proxyingDevice
ERROR UDID was not a string
JIT
userUUID
OSLogEventStore
Failed to open newly created directory
0x%016qx
tmpname
event_code
purgeable
vm-compressor-space-shortage
Stackshot syscall failed (from euid %d) with error %d: %s
suspensionLastStart
%lld
accessory
)#
shared_cache_layout
sharedRegionSystem
no matching configs
Movies
submission-completed
errstr
isImpDonor
tasked-cfg_%@
currentTaskingIDByRouting
330
name
OSASystemConfiguration.m
  debug
-----------\nFull Report\n-----------\n
thread %llu in compressor segment %#llx
-[OSAStackShotReport decodeKCDataWithBlock:withTuning:usingCatalog:]
QOS_CLASS_MAINTENANCE
com.apple.osanalytics.factoryproxysync
#(
no shared cache available from the kernel snapshot -- this may impact symbolication
data
resampledUserFrames might be missing second-to-leaf frame
unexpected tasking result
states
file-owner-uid
v16@?0@\"NSURL\"8
fileBacked
kThreadUnknown
lx
freeze_skip_reason:
Destination unavailable
expectedCAHeartbeats
xform-full-report
userFrames
timesThrottled
kThreadTriedFaultBT
rejected-config
/var/mobile
Documentation
terminatedSnapshot
%p
coalition
bundle
invalid position
logPath
ErrorPowerAssertionExpired
Thread %d crashed with ARM Thread State (32-bit):\n    r0: 0x%08x    r1: 0x%08x      r2: 0x%08x      r3: 0x%08x\n    r4: 0x%08x    r5: 0x%08x      r6: 0x%08x      r7: 0x%08x\n    r8: 0x%08x    r9: 0x%08x     r10: 0x%08x     r11: 0x%08x\n   
thermalData
memoryPages
snapshotFlags
app_name
Printers
com.apple.osanalytics.stateMonitor
Thread:%@; Address space info does exist for asid %@
err
stacks+%@
kThreadIOPassive
UI_country_code
configureProxyDevice
QuickLook
submitted
unable to instantiate shared cache %@
updated
Unmapped pages caused truncated backtrace (resampling disabled)
ca1
OFF
Screen Savers
v16@?0@\"NSDictionary\"8
v20@?0I8r^Q12
\\^\\([^\\)]+\\)
kRTCReportingSessionInfoSessionID
Downloads
Fonts
Frameworks
Python
OSLogEventStream
v16@?0r^{dyld_shared_cache_dylib_text_info=QQQ[16C]*Q}8
keyFrame
asi
kcdata_iter_container_id(kcData) == end.tag
idle
ca1-ohttp
com.apple.osanalytics.daFlow
/Volumes/VOLUME
...
userTimeTask
%
continuous
bundleInfo
109
obj
0x%08x
stackshot_duration_nsec
Process %@ is in transition type %@
taskingID
location
LogType
rejected-header
offset
decompressions
com.apple.osanalytics.sanitizer
<sort>
installed
com.apple.app-sandbox.read-write
ers_flags
system_usec
-1
+[OSATasking applyTasking:taskId:fromBlob:]
zoneMapSize
301
<cleanup>
B20@?0i8^@12
suspensionThreadID
 -> *
Desktop
Speech
set-log-limit
dre_optIn_operation
com.apple.CrashReporter
/dev/urandom
only-retired
AppleSoCMisc
submission-started
CFBundleShortVersionString
r12
queue in a transient state
waitinfos
physicalPages
timestamp
Filesystems
fileDesc
arch
sourceLine
(unknown-%llu)
explicit   
state-monitor.ca.event.%f
cleanup_paths
pageFaults
schedFlags
^([A-Z_]+), (\\[0x[0-9a-zA-Z]\\] )?(.*)$
kernel
proxyingDeviceTimeAtReceipt
v32@?0@8@16^B24
MCFeatureDiagnosticsSubmissionAllowed
/usr/sbin
rdx
kThreadMain
en
reasons
Syslog query timed out
hhd
<transfer>
bundleID
Thread %d crashed with X86 Thread State (64-bit):\n  rax: 0x%016qx  rbx: 0x%016qx  rcx: 0x%016qx  rdx: 0x%016qx\n  rdi: 0x%016qx  rsi: 0x%016qx  rbp: 0x%016qx  rsp: 0x%016qx\n   r8: 0x%016qx   r9: 0x%016qx  r10: 0x%016qx  r11: 0x%016qx\n  r
ScheduledTasking
startTimestamp
xform-tracer-url
symbolicated_log
(unknown)
x
timeDelta
/var/db/forceMultiUserMode
CFBundleIdentifier
+
193
CA_startTimestamp
kGlobalForcedIdle
defaults_operation
http_post_started
xform-error
osanalytics_monitor
' on file with descriptor '
swapins
QOS_CLASS_BACKGROUND
%llx
Library
errorDesc
v16@?0@\"NSArray\"8
rsrcFlagged
Library/Logs/DiagnosticReports
ext
procPath
debug_block
  domain %@ => [%@]
added_to_archive
%@ + %llu%@%@
reason
faults
TH_SFLAG_PROMOTED
submission_params
ACEmailAliasKeyEmailAddresses
ThermalPressureLevelModerate
Audio
rejected-rawsize
com.apple.crash_mover
 (%@:%@)
: 
osanalytics_jetsam
SELF != ''
328
sustained-memory-pressure
subrouting
notes
thawed
Q
disconnected
JSON schema not understood
isNonFatal
pthread mutex %#llx
0x%llX
crashreporter_key
MountedVolume
start_path
port %#llx with unknown owner
i
total_uncompressed_pages_in_compressor
isDirtyTracked
TH_SFLAG_ABORTSAFELY
CATaskingID
@\"NSDictionary\"8@?0
app_build_version
kcdata_iter_container_type(iter) == STACKSHOT_KCCONTAINER_PORTLABEL
OS Version
datawriter returned with negative response
  Cacheline:
--%@\r\nContent-Disposition: form-data; name=\"%@\"; filename=\"%@\"\r\nContent-Type: %@\r\n\r\n
%FT%T%z
osanalyticshelper
original
n/a
OSAReport.m
q24@?0@\"OSABinaryImageSegment\"8@\"OSABinaryImageSegment\"16
create_dir_success
com.apple.osanalytics
Foundation/arm64e-apple-ios.private.swiftinterface
additionalDetails
wired
ON
keepFile
System/Library/CoreServices/SystemVersion.plist
proxy
threadById
ProductVersion
idle-exit
conclave-limit
Device Software Diagnostic Log
kRTCReportingUserInfoClientName
flags
 (%@)
turnstile has unknown inheritor
ConfigurationContent
tracer_url
dispatch_queue_label
%x
submissionTimeISO
systemgroup.com.apple.osanalytics
+[OSAStateMonitor recordEvent:with:]
llu
anon
%-3d %@
bytes
largestProcess
XPC Error: %s
osanalytics_monitor_ca_submission
%d
semaphore port %#llx
dyldCompactInfoTooBig
%f
%@%@
code
spindump
PlugIns
purgeable_count
compressorSize
extDarwinBG
TH_SFLAG_RT_DISALLOWED
0 && \"Unsupported routing used in tasking\"
logwritten
Containers
proxied
error
frontmost
staged
<no_sn>
/Library/Logs/AppleSupport/
ip
unsupported JSON schema version
basePriority
TH_SFLAG_DEPRESS
submissionConfig
filterByLogAge
success
%c
Unknown KCDATA %X, size %d, flags %X
%d unindexed re-sampled frames from %d pids: %@
p
periodic
opt
security.mac.amfi.developer_mode_status
%02x%c
sendAsMessage
rejected-doNotSubmit
systemBuildVersion
indicator
Unexpected reply from %s
%-*u %@
csTrustLevel
TH_SFLAG_UNKNOWN
Bridge
original_gid
framework
multipart/form-data; boundary=%@
taskSpecificSharedCache
TH_SFLAG_THROTTLED
crk
SerialNumber
unknown-arch
```
