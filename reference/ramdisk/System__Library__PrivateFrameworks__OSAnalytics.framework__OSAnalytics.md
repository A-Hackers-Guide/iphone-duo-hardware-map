# `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

From the upgrade restore ramdisk (141-29011-104.dmg). 919,216 bytes.

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
OSADefaults
OSASymbolInfo
OSAExclaveContainer
OSALogTrackerObject
OSABridgeLinkProxy
NSObject
OSACrackShotReport
OSAStateMonitor
OSAStackShotReport
optIn
OSABinaryImageCatalog
OSAXformAugment
_TtC11OSAnalytics11DeviceState
PIDListExtension
OSAParsedOsLogPart
ExclaveThread
Trimming
OSALogTrackerExtension
_TtC11OSAnalytics24WatchdogExitReasonHelper
OSAStackshotKCDataExtension
OSAOsLogPackParser
KCContainer
OSAKCDataExtension
OSADateCounter
OSATasking
OSAProxyConfiguration
OSASystemWatchdogCrashReport
OSASanitizerCondensor
OSAReport
OSASafeCreateDirectoryOptions
OSALegacyXform
OSASharedCacheEntry
OSADiagnosticsReporterSupport
SectionStackExtension
OSABinaryImageSegment
ExclaveAddressSpace
ExclaveLayout
ExclaveStackEntry
_TtC11OSAnalytics9IPSReport
OSAConcreteReport
OSAJetsamReport
OSASystemConfiguration
OSALog
OSABinaryImageListExtension
FileUtils
TQ,R
augmentWithPrefix:
parseKCdata:
T@\"NSDate\",&,N,V_oldestDate
TB,R,N,V_isComputeController
pop
_isSuspendedOnlyJetsam
_sharedCacheUuid
formatCallstacks:withImages:macosStyle:
getTaskingKey:
numberWithLongLong:
requestWithURL:
formatImages:macosStyle:
notes
username
_stream
_segments
productBuildString
_experimentGroup
_threads
stream
timeIntervalSinceReferenceDate
_targeted_slide
pathPreferences
.cxx_destruct
Ti,N,V_jetsamLevel
setSchedulingContextId:
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:isSnapshotDead:
T@\"NSNumber\",&,N,V_sharedCacheIndex
_kernel_segments
_pairedWatchOS
errorWithDomain:code:userInfo:
findBundleAtPath:withKeys:bundleURL:
systemId
initWithString:
URLByDeletingLastPathComponent
_ss_trace_buffer
appleCareDetails
backtrace
dictionaryWithObject:forKey:
getExtraData:
dateForEvent:
getXattrWithName:at:
_targetAudience
_filepath
createRetiredDirectoriesForUser:
sendMessageWithCategory:type:payload:error:
setUserID:
sharedConnection
T@\"NSString\",&,N,V_etlKey
_deleteOnRetire
dateFromString:
_event_reason
_bugType
_procPath
T@\"NSString\",R,V_seedGroup
readXattrWithReader:errorContext:
sharedCacheSlide
fileSystemRepresentation
bootSessionUUID
_productReleaseString
domain
transfer:key:
TB,N,V_dead_snapshot
isInLDM
resampleUUIDsForTask:usingCatalog:
saveToPath:
ss_trace_buffer
addObject:
automatedDeviceGroup
T@\"NSMutableArray\",&,N,V_segments
initWithType:filepath:metadata:options:at:error:
isComputeController
numberWithUnsignedLongLong:
internalKey
initWithSource:
checkSubmissionStatus
getXattrWithName:onFile:
retainCount
TB,R,V_isArgument
_maxNumArguments
T@\"NSString\",R,V_buildVersion
coldestElided
deleteOnRetire
isAllowed:forDomain:
TB,V_formatStringIsSafe
_includeSyslog
_pathContainerRoot
_pointerPointsToSafeMemory
initWithName:reason:exceptionCode:exceptionCodeCount:
sortedPids
activityIdentifier
submissionParam:
T@\"NSString\",R,V_bugType
initWithMaxNumAruments:
initWithSessionInfo:userInfo:frameworksToCheck:
markWithKey:value:
T@\"NSString\",R,C
_recoveryModeReason
pointerPointsToSafeMemory
T@\"NSString\",R,V_legacyAutomatedDeviceGroup
T@\"NSString\",R,V_recoveryModeReason
TB,R,V_isInDeviceRecoveryEnvironment
recoveryModeReason
T^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII},R,N,V_original
initWithPath:forRouting:options:
initWithPath:forRouting:options:error:
moveItemAtURL:toURL:error:
osa_logTracker_incrementForSubtype:signature:filepath:
releaseType
filterOutSensitiveParts:withFormats:
initAlertDelegate
numberWithDouble:
setIsAppleCode:
setIncludeSyslog:
maxNumArguments
pid
_start
omit
optInApple
parsePortLabelContainer:
subarrayWithRange:
unsignedIntegerValue
_thermalNotificationCurrentLevel
_used_segments
insertObject:atIndex:
numberWithBool:
T@?,C,V_pointerPointsToSafeMemory
identifier
TB,R,N,V_isPrivateServerOS
addExclaveSharedCache:
layoutImageCount
metaData
sharedCacheID
rename:
ss_trace_length
_truncated_threads
data
removeObjectAtIndex:
standardUserDefaults
stringByAppendingPathExtension:
T@\"NSString\",R,N,V_logfile
_logPath
sortUsingComparator:
uiCountryCode
T@\"NSMutableDictionary\",R,N,V_addressSpaces
T@\"NSString\",R,V_automatedContextURL
isFile:validForSubmission:reasonableSize:to:internalTypes:result:
sharedMCProfileConnection
stringWithContentsOfURL:encoding:error:
_capture_time
addNotes:
bundleWithURL:
getSyslogAtCaptureTime:forPids:andOptionalSenders:additionalPredicates:
TB,R,N,V_isDefaultSharedCache
Td,R,N,V_capture_time
_oldFilePath
appendString:
setLink:
bugType
TQ,V_start
TB,V_isAppleCode
_isDefaultSharedCache
initWithFilepath:type:
listXattrsAt:
_sharedCacheID
doubleValue
initWithBytes:length:encoding:
invalid_images
modelCode
T@\"NSMutableDictionary\",R,V_signatures
T@\"NSMutableArray\",&,N,V_frames
composedMessage
filepath
handleDiagnosticLog:logPath:patternMatchActions:files_to_attach:completion:
transformJSON:header:error:streamingBlock:
writeToURL:options:error:
logExt:
_hwModel
_sharedCacheIndex
createReportMetadata:with:at:usingOptions:
depth
shouldApplyPreference:forSamplingKey:
stackEntries
targetSharedCache:withSlide:atBaseAddress:
bootArgs
ensureUsablePath:component:options:
formatStringIsSafe
_killed_or_suspended_count
initWithLiteral:isSafe:
oldestDate
problemType
_invalid_images
_schedulingContextId
performSelector:withObject:
setDead_snapshot:
_formatStringIsSafe
conformsToProtocol:
stringByAppendingString:
cleanupLogs:withFilters:error:
instrumentEvents:
null
unsignedIntValue
T@\"NSMutableDictionary\",R
isArgument
preference:alreadySetInInstructions:
saveWithOptions:
T@\"NSString\",R,V_oldLogFile
_formatString
_logWritingOptions
_zones
initWithKey:ascending:
prepareWithCompletionHandler:
addStackEntries:
formatArm64ThreadState:index:
initWithCapacity:
UUIDString
_termination_info
compose:
onceConfig
shared
body
getLogBlacklist
URLByAppendingPathComponent:
indexOfObjectPassingTest:
setGroupID:
setKernelImages:
T@\"NSString\",C,V_formatStringOriginatingModulePath
TB,R,N,V_panicReportSubmissionDisabled
_systemId
T@\"NSString\",R,V_productNameVersionBuildString
isSnapshotDisabled
substringToIndex:
TQ,R,N,V_sharedCacheSlide
_event_code
localizedDescription
markDescriptor:withPairs:andOptions:
dealloc
_layoutId
alreadyDumpedSuspendedJetsamLogToday
_addressSpaceId
pathContainerRoot
pathSubmissionDataVault
rangeOfString:options:
readCStringFromTarget
stringByReplacingOccurrencesOfString:withString:
zoneInfo
applyTasking:taskId:fromBlob:
push:
_stackEntries
isAddressInTargetedCache:
oldFilePath
T@\"NSString\",R,V_experimentGroup
_wiredBytes
initWithDomain:code:userInfo:
isSafe
sharedCacheIndex
T@\"NSString\",C,N,V_name
_identifier
_templates
fileProtectionNone
pathSubmission
pathSubmissionSubdirDiagnosticLogs
_logBlacklist
init:fromMetadata:
longLongValue
performSelector:
setSharedCacheLayout:andCount:
signatures
substringWithRange:
getVMStatistics
_productBuildString
_signatures
arrayWithObjects:count:
dateByAddingTimeInterval:
ensureConformanceOfFile:options:
samplingKey
TB,N,R
_isPrivateServerOS
_preserveFiles
formatArm32ThreadState:index:
logPathForType:at:options:
allKeys
_oldestLogPath
T@\"NSMutableArray\",&,N,V_sharedCaches
T@\"NSString\",R,V_internalKey
_submissionParams
addObjectsFromArray:
pathCATasking
_awakeSystemUptime
sharedCacheUuid
dictionaryRepresentation
objectAtIndexedSubscript:
T@\"NSMutableDictionary\",R,N,V_layouts
checkTaskingRelevance
full_details
numberWithUnsignedLong:
timeIntervalSinceNow
TI,R,N,V_type
argSpecifier
formatString
initWithTask:
dead_snapshot
fastLane
setHTTPContentType:
TB,R
countByEnumeratingWithState:objects:count:
createIntermediates
defaultManager
increment
performSelector:withObject:withObject:
setHTTPMethod:
userID
oldLogFile
proxyTasking:taskId:usingConfig:fromBlob:
setValue:forKey:
length
path
productName
numberWithUnsignedInt:
setAdditionalPayload:
_etlKey
threads
_stringValue
name
setDateFormat:
_dayKey
URLWithString:
pathSubmissionWithHomeDirectory:
setKernelCache:address:size:
TI,R,N,V_ss_trace_length
copy
_isExclaveValid
invalidate
whitespaceCharacterSet
top
addImage:address:size:
recordEvent:
_internalKey
infoDictionary
searchFrame:in:result:
unsignedLongLongValue
isEqualToString:
overrideMountPath
setActions:
stringByStandardizingPath
sendOperation:forKey:withBlock:
_sharedCacheUnreliableSlidBaseAddress
jetsamLevel
setSpindump:
stringValue
stringByPaddingToLength:withString:startingAtIndex:
containsString:
_appleInternal
addressSpaces
pathExtension
T@\"NSString\",R,V_systemId
_killedActiveApps
evaluateState
isDataVaultEnabled
layoutId
setPathRoot:
_carrierInstall
_buildVersion
_bundleID
logPrefix:
setFiles_to_attach:
productNameVersionBuildString
_reason
_cpuArch
addTurnstileInfoDesc:count:elSize:
formatStringOriginatingModulePath
includeSyslog
initWithArray:
oldestLogPath
initWithSource:size:for:source:
iterateLogsWithOptions:usingBlock:
bootProgressRegister
Ti,N,V_invalid_images
T@\"NSString\",&
TQ,R,N,V_sharedCacheUnreliableSlidBaseAddress
autorelease
_source
isProxy
acquireJetsamDataWithFlags:
getInstalledTaskIds
modulePathForMemoryPointer
bytes
lastPathComponent
now
addJITImage:size:
firstObject
propertyListWithData:options:format:error:
setHTTPBody:
_exceptionCodes
T@\"NSMutableDictionary\",R,N,V_threadIdToScId
selectConfigFromBlob:withError:
_appName
formatLastBranchState:index:withImages:
segments
symbolInfo
T@\"NSArray\",R,N,V_frontmostPids
_pathPreferences
acquireStackshot
initWithArgument:argSpecifier:isSafe:
initWithFileDescriptor:closeOnDealloc:
sampleThread:
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:
_exceptionCodeCount
_isComputeController
getPropsForLogType:
isExclaveValid
isInDeviceRecoveryEnvironment
isMemberOfClass:
initWithKCData:
pathWithComponents:
T@\"NSString\",R,V_releaseType
_kernel_text_exec_segments
componentsJoinedByString:
initWithPath:options:error:
setStackEntries:
sharedCaches
setInvalid_images:
T@\"NSString\",&,N,V_oldestLogPath
_capture_absoluteTime
appendBytes:length:
carrierInstall
processCALogEvent:eventPayload:into:
submissionMetadata
_createIntermediates
_shared_segments
osa_logTracker_getForSubtype:forOwner:
details
initWithIdentifier:
stringByDeletingLastPathComponent
fetchWiredMemoryInfo
fileModificationDate
getFramesForThread:usingCatalog:
isWritableFileAtPath:
predicateWithFormat:
setXattrWithName:value:at:
T@\"NSString\",R,V_targetAudience
T@\"NSDictionary\",R,V_metaData
T^{dyld_uuid_info_64=Q[16C]},R,N,V_layout
resetCount
_audioAssertionState
_getValueForKey:fromBody:orHeader:
_ss_sequence
enumerateMatchesInString:options:range:usingBlock:
ephemeralSessionConfiguration
isReadableFileAtPath:
numberOfMatchesInString:options:range:
setDREOptIn:
closeFileStream
_metaData
_name
_rootedCacheLibs
schedulingContextId
spindump
setJetsamLevel:
characterAtIndex:
isKindOfClass:
setKernelTextExecImages:
stringByReplacingPathBeforeComponent:with:
T@\"OSASymbolInfo\",R,N,V_symbolInfo
getActivePairedDevice
reverseObjectEnumerator
writeToURL:atomically:
getAllXattrsAt:
_layout
_thermalSensorValues
crashreporterKey
isLowPowerModeEnabled
markImageAsUsed:from:
setString:
setMaximumSignificantDigits:
assembleMetadataAt:withOptions:
T^[37c],R,N,V_sharedCacheUuid
_isAppleCode
appendData:
getXattrBoolValWithName:at:
bundleForClass:
allObjects
initWithObjects:
TI,N,V_flags
_modelCode
hasPrefix:
objectAtIndex:
setOldestLogPath:
_ss_trace_length
sortedArrayUsingDescriptors:
rollSchemaForward:
TQ,R,N,V_tag
_logConfig
isConfigEnabled:
multiUserMode
setResourceValue:forKey:error:
backtraceLength
TQ,R,N,V_maxNumArguments
_spindump
logDomain
sortByAddressAndSetInferredSizes
streamContentAtLevel:withBlock:
initWithContentsOfFile:
vmRegionInfo
T@\"NSString\",&,V_name
stringByAppendingPathComponent:
boolValForMCSetting:
descriptionFromCode:
dictionaryWithValuesForKeys:
initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:
initFromPath:
mutableCopy
TQ,R,N,V_capture_absoluteTime
Tr^v,R,N,V_ss_trace_buffer
dictionaryWithCapacity:
lastObject
setSource:
sharedTrackers
statusCode
initWithUUIDBytes:
setLayoutId:
JSONObjectWithData:options:error:
_readCStringFromTarget
decode_reason:reason:
etlKey
logObjForBugType:
recordEvent:with:
T@\"NSString\",R,C,V_argSpecifier
set
_submissionMetadata
boolForKey:
integerValue
isEqual:
reportUsedImages
setUnindexed_frames:
T@\"NSNumber\",&,N,V_schedulingContextId
_productNameVersionBuildString
_uuid
characterSetWithCharactersInString:
fileExistsAtPath:
pairedWatchOS
setReason:
T@\"NSString\",C,V_formatString
crashReporterKey
T@\"NSNumber\",&,N,V_layoutId
setFormatStringOriginatingModulePath:
sharedClient
substringFromIndex:
_awdReporterKey
retain
valueForProperty:
_extras
pathDiagnostics
_flags
numberWithUnsignedShort:
rangeAtIndex:
setPid:
T@\"NSString\",R,V_productVersion
_isSafe
_argSpecifier
isAppleTV
setNotes:
useStackshotData:frontmostPids:atTime:machTime:sequence:
_groupID
_tag
setCount:
isDefaultSharedCache
T@\"NSString\",R,V_automatedDeviceGroup
_path
getAvailableTaskingRoutings
moveItemAtPath:toPath:error:
symlink:
T@\"NSString\",R,V_filepath
_exclave_shared_caches
_isSystemWatchdog
transformURL:template:options:
TB,V_createIntermediates
initWithUTF8String:
sessionWithConfiguration:
setSegments:
systemIDWithDescription:
truncated_threads
T^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq},R,V_stream
_layouts
_logDomain
_releaseType
pathForResource:ofType:
acquireJetsamData
availableData
init
markDescriptor:forKey:withObj:
subdataWithRange:
T@\"NSMutableDictionary\",R,N,V_data
getStackshotData
array
formatX86ThreadState:index:
osa_logTracker_recordNixedDuplicate:
isPaired
legacyAutomatedDeviceGroup
objectForKeyedSubscript:
type
_factoryDevice
getSyslogForPids:andOptionalSenders:additionalPredicates:
_symbolInfo
appendFormat:
dataTaskWithRequest:completionHandler:
isEqualToNumber:
cpuType
_pid
TB,V_deleteOnRetire
arrayByAddingObjectsFromArray:
decodeKCDataWithBlock:withTuning:usingCatalog:
keyForEvent:
original
scanProxies:
setOldestDate:
TB,V_fileProtectionNone
UUID
_sharedCacheSlide
debugDescription
generateLogAtLevel:withBlock:
setFileProtectionNone:
setObject:forKeyedSubscript:
T@\"NSMutableArray\",&,N,V_notes
_largestActiveApp
rangeOfString:
setSize:
stringByTrimming
stringWithUTF8String:
T@\"NSNumber\",C,V_userID
appendNotesTo:
isWhitelisted:forDomain:
pathRoot
_dead_snapshot
_kernel_cache_segment
setInvalidationHandler:
T@\"NSString\",R,V_path
createRetiredDirectory:
stringByTrimmingCharactersInSet:
date
setFlags:
T@\"NSNumber\",C,V_groupID
addImageLegacy:address:size:name:path:arch:
attributesOfItemAtPath:error:
capture_time
T@\"NSString\",R,V_modelCode
release
userAppName
setOldFilePath:
setThreadId:withScId:
updateLogLimitFor:
_logfile
accountType
addFrames:
checkCALogWrittenStatus
hottestElided
setName:
_getSnapshotWithFlags:
_isArgument
isAppleCode
removeItemAtURL:error:
self
T@\"NSMutableArray\",&,N,V_stackEntries
groupID
used_index
initWithPath:forRouting:usingConfig:options:error:
isSecurityResearchDeviceERM
dataUsingEncoding:
launchAppWith:options:completion:
purgeLogs:withReason:includeRetired:deleteOnRetire:usingPredicate:
setUsed_index:
appendPortLabelInfo:portlabels:
targetAudience
threadIdToScId
uidForUser:
_productVersion
locallyCreateForSubmission:metadata:options:error:writing:
addPart:
evaluateCALogStates:
isDeveloperMode
_used_index
hash
initWithSharedCache:atBaseAddress:
_cpuType
_notes
checkAndReportCALogStates
initWithDictionary:
T@\"NSString\",R,V_productName
T@?,C,V_readCStringFromTarget
cleanupRetired:
hwModel
osTrain
_currentTaskingIDByRouting
_panicReportSubmissionDisabled
stringForObjectValue:
T@\"NSString\",R,C,V_stringValue
initWithZoneNames:nameCount:zoneInfo:zoneInfoCount:wiredInfo:wiredInfoCount:
prepareTemplate:forLogType:error:
writeToFile:atomically:
cleanupForUser:
bootUUID
get_uuid
initWithAddress:size:for:
plumbEmail:
removeLastObject
setCreateIntermediates:
_frames
productReleaseString
TB,R,V_isSafe
addEntriesFromDictionary:
arrayWithCapacity:
hasSuffix:
setIsExclaveValid:
setPath:
_seedGroup
fileURLWithPath:
optIn3rdParty
T#,R
addressSpaceId
decode_cpuType
factoryDevice
setDeleteOnRetire:
_original
formatFrame:withImages:macosStyle:
submissionsDisabled
cpuArch
_oldLogFile
_size
dateWithTimeIntervalSinceReferenceDate:
isInternalBridge
transformLines:withDefinitions:body:header:error:streamingBlock:
T@\"NSString\",R,V_uiCountryCode
retire:
Ti,N,V_unindexed_frames
UTF8String
layout
osa_logTracker_incrementForSubtype_internal:signature:filepath:scan:
osa_logTracker_shouldRotateLog:
_legacyAutomatedDeviceGroup
sharedInstance
T@\"NSNumber\",&,N,V_addressSpaceId
_targeted_cache
formatLastException:withImages:
setSs_sequence:
count
experimentGroup
tag
Ti,V_source
setTimeoutInterval:
sharedCacheUnreliableSlidBaseAddress
TQ,V_used_index
T{?=@},R
_formatStringOriginatingModulePath
_isSnapshotDisabled
arrayWithObject:
seekToFileOffset:
scanLogs:from:
hasXattrWithName:at:
localStore
processInfo
setInteger:forKey:
source
setBool:forKey:
class
componentsSeparatedByString:
removeObjectsForKeys:
writeData:
arrayWithObjects:
_type
additionalIPSMetadata
boolValue
effectiveBoolValueForSetting:
setRootedCacheLibs:count:
T@\"NSString\",R,V_logPath
_automatedContextURL
_sharedCaches
isPrivateServerOS
sysVersionData
reduceToTwoSigFigures:
T@\"NSString\",C
_setDumpedSuspendedJetsamLog
dataWithCapacity:
start
sendOneMessageWithSessionInfo:userInfo:category:type:payload:error:
valueForKey:
_frontmostPids
createForSubmission:metadata:options:error:writing:
kernelVersionDescription
optInDRE
_jetsamLevel
removeItemAtPath:error:
scanLogs:from:options:
writeData:error:
T@\"NSDictionary\",&,N,V_spindump
numberWithUnsignedInteger:
_pathCATasking
addWaitInfoDesc:count:elSize:
incidentID
postFailureWithReason:
setReadCStringFromTarget:
temporaryFileWithPrefix:fd:
unindexed_frames
_hexDump:offset:indicator:
_tags
localizedStringForStatusCode:
isApplePath:orBundle:
seedGroup
enabled
_aleFlag
visibleTopLevelAccountsWithAccountTypeIdentifiers:completion:
isCustomerFused
tracker
_oldestDate
setTarget:
timeIntervalSince1970
logType
_pathRoot
dictionary
fetchSnapshotWithFlags:error:
indexOfObject:
containsObject:
_layoutImageCount
TB,R,V_isSnapshotDisabled
logPath
_logType
setEventHandler:
size
T@\"NSString\",R
_multiUserMode
initWithPID:options:
installCATasking:withId:untasked:
setUsesSignificantDigits:
setValue:forHTTPHeaderField:
bundleURL
frames
getThermalPressureLevel
intValue
osa_logTracker_isLog:byKey:count:withinLimit:withOptions:errorDescription:
transformURL:options:
additionalRootsInstalled
dictionaryWithObjects:forKeys:count:
setSharedCacheIndex:
threadIdentifier
usesLegacySubmission:
instrumentEventsWithAudioAssertionState:visibliltyEndowmentState:
section_pop
setAddressSpaceId:
T@\"NSDictionary\",R,V_currentTaskingIDByRouting
dataWithJSONObject:options:error:
formatInstructionState:index:
legacy_arch
panicReportSubmissionDisabled
pathComponents
setSharedCaches:
_addressSpaces
_serialNumber
extractArguments:
stringWithFileSystemRepresentation:length:
_modulePathForMemoryPointer
compare:
enumerateKeysAndObjectsUsingBlock:
isActionable
respondsToSelector:
setFilterPredicate:
T@\"NSMutableDictionary\",R,N,V_truncated_threads
currentTaskingIDByRouting
numberWithShort:
orPredicateWithSubpredicates:
CALogStateToString:
T@\"NSString\",?,R,C
_threadIdToScId
TB,R,N,V_isComputeNode
process
headerJson
T@\"NSString\",R,V_crashReporterKey
addCustomField:value:into:
dataUsingEncoding:allowLossyConversion:
queryThermalData
productVersion
section_push:
setPrefsKey:value:forDomain:withSync:
T@\"NSString\",R,V_identifier
T@\"NSArray\",R,N,V_notes
_snapshot
dataWithBytes:length:
_stackshot_config
code
integerForKey:
setSharedCacheInfo:
setFormatString:
TB,N,V_isExclaveValid
addSuiteNamed:
parent
TI,R,N,V_sharedCacheID
_whitelistedDomains
codeSigningMonitor
globallyUniqueString
resume
layouts
initWithData:encoding:
metadata
_isComputeNode
TI,N,V_ss_sequence
exceptionCodesDescription
isReasonableSize:forRouting:
removeObjectForKey:
searchFrame:in:regions:result:
logfile
_incidentID
_unindexed_frames
enumerateObjectsUsingBlock:
osa_logTracker_trackLogTypes_internal:forOwner:rescan:
ss_sequence
T@?,C,V_modulePathForMemoryPointer
_automatedDeviceGroup
copyItemAtPath:toPath:error:
executeWithTimeout:Code:
stringWithCString:encoding:
zone
_userID
setWithObjects:
awdReporterKey
removeObject:
resampleTruncatedBacktracesForTask:forThreads:usingCatalog:in:usingSymbolicator:
stringByExpandingTildeInPath
stringWithFormat:
superclass
setEtlKey:
T@\"NSString\",&,V_cpuArch
TB,N,V_includeSyslog
numberWithInt:
TI,R,N,V_layoutImageCount
T@\"NSMutableDictionary\",R,N,V_threads
appleInternal
dictionaryWithContentsOfFile:
transferInternal:key:
flags
setObject:forKey:
buildVersion
clearExclaveSharedCaches
fileURLWithPathComponents:
initWithPid:
_daysSince1970
description
objectForKey:
reason
setLog_path:
stringByDeletingPathExtension
timeIntervalSinceDate:
T@\"NSString\",R,V_awdReporterKey
T@\"NSString\",R,V_osTrain
_absolute_segment
capture_absoluteTime
dateWithTimeIntervalSince1970:
defaultTasking
getPrefsKey:forDomain:withOptions:
_largestProcess
randomizedCRKey
floatValue
stringByTrimmingColumnSensitive
automatedContextURL
userInfo
TQ,V_size
_osTrain
initWithPid:procName:bundleID:exitSnapshot:reason:
sender
setPointerPointsToSafeMemory:
frontmostPids
isComputeNode
setModulePathForMemoryPointer:
commonFieldsForBody:
normalizeInstructions:forSamplingKey:
parse:
_data
setCpuArch:
setFormatStringIsSafe:
currentLocale
initWithIncidentID:visibilityEndowmentState:audioAssertionState:
initWithSuiteName:
reportUsedImagesFullInfoUsingBlock:
serialNumber
setStart:
initForPid:exitSnapshot:reason:
_crashReporterKey
pathSubmissionForOwner:
setSymbolicator:
getDisplayState
Ti,N,V_pid
activateStreamFromDate:
filteredArrayUsingPredicate:
reportNamePrefix
_fileProtectionNone
indexOfObject:inSortedRange:options:usingComparator:
isOnDeviceLogType:
randomlySelectForRetention:
startConfigurationWithCompletionHandler:
T@\"NSString\",C,V_oldFilePath
_productName
_uiCountryCode
initWithFileDescriptor:
regularExpressionWithPattern:options:error:
_isInDeviceRecoveryEnvironment
initWithSymbol:source:
setAutomatedDeviceGroup:
sortedArrayUsingSelector:
captureTime
markPurgeableLevel:path:
_count
_countKey
setIncidentID:
TQ,N,V_count
_visibilityEndowmentState
getResourceValue:forKey:error:
markFile:withKey:value:
removeAllObjects
setFrames:
T@\"NSString\",R,V_hwModel
getEventPriority:terminationReason:priority:
processIdentifier
_additionalPayload
_pathDiagnostics
@52@0:8i16@20@28^q36I44I48
v24@0:8@16
^q
@32@0:8@16r*24
v24@0:8@?16
{?=\"daFlow\"@\"NSObject<OS_os_log>\"}
@52@0:8i16@20@28^{exit_reason_snapshot=IQQ}36@44
v28@0:8^{dyld_uuid_info_64=Q[16C]}16I24
Q16@0:8
v36@0:8i16@20@28
@36@0:8i16^{exit_reason_snapshot=IQQ}20@28
I40@0:8@16@24@32
@20@0:8B16
v32@0:8Q16Q24
B40@0:8@16@24@32
Q
B24@0:8@16
B24@0:8#16
B32@0:8@16@24
@48@0:8d16@24@32@40
B40@0:8@16@24^@32
@16@0:8
B16@0:8
@40@0:8@16@24@32
@40@0:8Q16@24^@32
v16@0:8
v52@0:8@16@24d32Q40I48
B44@0:8@16@24@32B40
C28@0:8I16@?20
@24@0:8q16
@32@0:8@16i24B28
v60@0:8r^v16I24@28d36Q44I52B56
@32@0:8@16^@24
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}
@24@0:8@?16
@36@0:8@16i24@28
@32@0:8@?16@?24
B24@0:8r*16
@28@0:8@16i24
v40@0:8@?16@24@32
v56@0:8q16@24@32@40@?48
d
@\"NSDictionary\"
Q40@0:8@16Q24q32
@48@0:8@16@24d32@40
v32@0:8r*16r*24
v36@0:8@16@24B32
@\"NSMutableArray\"
^{dyld_uuid_info_64=Q[16C]}16@0:8
@28@0:8i16@20
i32@0:8@16@24
q16@0:8
v24@0:8r*16
q24@?0^v8q16
Vv16@0:8
v28@0:8B16@?20
@\"NSArray\"16@0:8
@24@0:8@16
@?
B64@0:8@16@24q32@40@48r^*56
@32@0:8^{exit_reason_snapshot=IQQ}16@24
Q28@0:8@16i24
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16@0:8
^[37c]16@0:8
^{_NSZone=}16@0:8
@40@0:8@16@24^@32
@32@0:8[16C]16Q24
@44@0:8Q16Q24[16C]32i40
B64@0:8@16@24@32@40^@48@?56
@64@0:8@16@24@32@40d48^@56
Q32@0:8@16@24
v24@0:8^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16
v40@0:8r*16@24@32
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}28@0:8I16^@20
v40@0:8@16r*24r*32
I
r*16@0:8
v28@0:8B16@20
@28@0:8d16I24
i28@0:8B16@?20
v44@0:8@16@24r*32B40
v40@0:8@16@24r*32
r^v16@0:8
@32@0:8@16@24
@32@0:8@16^i24
@48@0:8@16@24@32@40
v32@0:8@16@?24
@48@0:8@16@24@32^@40
d16@0:8
@24@0:8:16
i
@\"NSString\"
@\"NSMutableDictionary\"
@24@0:8Q16
@\"NSSet\"
r^v
^v
v40@0:8Q16@24@?32
#16@0:8
@\"NSDictionary\"16@0:8
v24@0:8Q16
@48@0:8Q16@24@32^@40
{kcdata_iter=^{kcdata_item}^v}32@0:8{kcdata_iter=^{kcdata_item}^v}16
B
^{dyld_uuid_info_64=Q[16C]}
v32@0:8Q16@24
v40@0:8@16@24^@32
v64@0:8[16C]16Q24Q32r*40r*48r*56
@40@0:8Q16Q24[16C]32
B24@0:8:16
B24@0:8@\"Protocol\"16
v56@0:8r^v16I24@28d36Q44I52
v40@0:8[16C]16Q24Q32
@\"NSNumber\"
v28@0:8i16@20
@32@0:8:16@24
@40@0:8:16@24@32
I32@0:8@16@24
@40@0:8@16@24N^@32
@\"OSABinaryImageSegment\"
B48@0:8@16@24^@32@?40
@\"NSString\"16@0:8
@56@0:8@16@24@32^@40@?48
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}
@36@0:8@16@24B32
B32@0:8@16r*24
{?=@}16@0:8
^[37c]
I16@0:8
i60@0:8i16@20@28@36{_CSTypeRef=QQ}44
v20@0:8I16
@\"NSArray\"
@?16@0:8
@32@0:8{kcdata_iter=^{kcdata_item}^v}16
v48@0:8@16r*24B32B36@?40
@44@0:8@16@24^q32I40
v20@0:8i16
@56@0:8@16@24@32@40^@48
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16@0:8
[16C]
@\"OSASymbolInfo\"
@20@0:8i16
v20@0:8B16
@40@0:8@16d24@32
i16@0:8
v32@0:8@16@24
@28@0:8@16B24
B32@0:8q16@24
B24@0:8Q16
B64@0:8@16@24^Q32^Q40@48^@56
@\"NSString\"8@?0
v32@0:8{kcdata_iter=^{kcdata_item}^v}16
v28@0:8B16@?<v@?@\"NSDictionary\">20
@\"NSDate\"
v32@0:8r^v16I24I28
Not in DRE, ignoring request to set DRE opt-in.
Failed to safely open '%{public}s': %{public}s
Unable to set xattr '%@', errno=%d: %s
Error retiring '%{public}@': %{public}@
overriding default log root location to %@
task_config is %{public}@
failed to create registration token for pressure level: %d
failed to create registration token for display state: %d
=== Attempted change perms on new dir: %{public}@ from 0x%X to 0x%X with result %d %{public}s
Error loading full report: %{public}@
Failed to retrieve a valid user to access preferences container for key %{public}@
new signature found -- but no room available
Failed to list xattrs at path '%{public}s': error %d (%s)
Error reading %s: expected to read %ld bytes but read %ld bytes
AppleCareSupport: ERROR unable to intialize data
Error issuing sandbox extension: %i (%s)
defaultConfig is %{public}@
osanalyticshelper replied with an XPC error: %s
Logfile '%{public}@' tagged DoNotSubmit
failed to modify permissions of %@: %s
group ok
Failed to open log directory '%s': %s
AppleCareSupport: WARN: limit exceeded, ignoring event
Failed to convert %@ to an XPC object
memorystatus_control for command %d failed with error %d
C3. private back-channel connection established
AppleCareSupport: ERROR[%d] failed to create %s, %s
Failed to set file protection class while creating %{public}@
RTCReporting Realtime: sendOneMessageWithSessionInfo succeeded
Failed to release sandbox extension: %s (%i)
Warning: Logfile '%{public}@' type %{public}@ routing %{public}@ does not match config %{public}@
Couldn't config private XPC connection
Will discard keys: %@
AppleCareSupport: rolling log -> %@
Unknown KCDATA CONTAINER %X
%s: %@ vs %@
Logfile '%{public}@' invalid for submission: no type
created directory '%{public}@'
sent RTCReporting %@
After normalization, combinedConfig is %{public}@
failed task_read_for_pid with %d
report not saved because it is non-actionable (ie: extension hangs or internal-only)
No reply received from osanalyticshelper for DRE opt-in request
crash_mover service FAILED to connect
No XPC connection to %s
tasked blacklist: %@
Failed override mount path: failed to generate new root paths
Failed override mount path: current root paths did not start with expected prefixes
Logfile '%@' is too old for submission
C4. ERROR Unable to reply
Retiring (%{public}@) %{public}s '%{public}@': %s
Failed to open service %@ with error: 0x%x
Error initializing report: unable to serialize header as JSON
Unable to dynamically link NRPairedDeviceRegistry from NanoRegistry
unable to lookup port for %@
Failed to remove retired log '%@': %@
No reply received from osanalyticshelper for DRE opt-in get request
Failed to update header as the provided data is not valid JSON
Failed to create symbolicator
setPrefs: attempt to change protection class for '%@' returned %d: %d %s
no URL for '%{private}@'
Event within submission window. Ignoring, will pick up next run.
Unable to retrieve file attributes at path %@. Error: %@
Report data has unexpected number of elements: %ld
Missing or invalid 'Domain' key
setPrefs: can't open '%@': %d %s
search for matches in '%@'
Creating Retired directory in %@
State monitor observed a failure: %{public}@
AppleCareSupport: existing log is valid, %s
error configuring RTCReporting; initWithSessionInfo failed
ns2xpc: unrecognized class: %@
Logfile '%@' fstat errno %d
Failed to override opt-in for '%@' log: option not supported when moving a log
crash_mover service %s
Expected a task specific shared cache with id %@ but none was found
Failed to launch DR with error: %@
setPrefs: already class D '%@'
found containerized defaults from %@: %@
evaluate domain %@ (%@) option %@ check %d
Failed to mark %s as purgeable %d (%s) (flags 0x%11llx)
Skipping log limit check on proxy-configured device with disableLogLimits set
scan: skipping '%@': hit log limit
Removing old retired log '%@'
Exclave data not present for SCID %@
Skipping transfer from proxy-configured device with disablePushOnWrite set
failed to write CA tasking blob to temporary path: %@
Not sending Core Analytics events because snapshot is missing.
Logfile '%{public}@' is too large (%lld) for submission
WARNING: Failed to close %@. Please do NOT call -[NSFileHandle closeFile] errno=%d: %s
Failed to remove retiring log '%{public}@': %{public}@
failed to create directory '%{public}@': %{public}@
%@:\n%@
Logfile '%@' is too large (%lld) for submission
AppleCareSupport: ERROR[%d] opening %s, %s
Sandbox extension token was missing.
Logfile '%{public}@' blacklisted from submission
local log create type %{public}@ result %@: %{public}@
Error retiring %s/%s while purging logs
AppleCareSupport: scanning '%s'
unable to strftime with format '%s' from %lds+%dus}
no bundle found
unique signature: %@ from original %s
setPrefs: not created '%@' returned %d: %d %s
failed to modify ownership of %@: %s
%@
Saved da3 tasking for deferred installation
setPrefs: delete old prefs and create placeholder
C4. write payload using file descriptor (%d)
'%{public}s' is not safe because it has at least one hard link
Failed to consume sandbox extension: %s (%i)
unable to override default log root location because already set as %@
failed to create VMUProcInfo
marking failed for %@, [%d] %s
Failed to read developer mode status: %{darwin.errno}d
Failed to set ownership while creating %{public}@: %s
failed to save proxy tasking: [%d] %s
no blacklist tasking: applying default: %@
Unable to load %@
Failed to get attrs for retired log '%@': %@
scan: including '%@' (explicitly added)
Path was safe to open, but no block was provided
scanned %zu logs with %lu types and %zu unknowns (sentinel is %@)
failed to send tasking availability notification to analyticsd
DiagnosticsReporterServices.framework is unavailable
Error deleting non-retirable log at %s/%s while purging: %@
synthesizing %d items from payload as metadata
Unable to load Accounts framework
=== Attempted change perms on existing path: %{public}@ from 0x%X to 0x%X with result %d %{public}s
Error while writing file: %{public}@
C4. ERROR no file descriptor (%d)
*** ignoring non-numeric symbolLocation: '%@'
memorystatus_control for command %d returned %d - No data available
owner ok
Initializing event date for %{public}@
crash_mover is taking too long!
duplicate signature: %@
synced after %lld total events
configured RTCReporting with session id: %d
Got xpc error message from %{public}s: %{public}s\n
Auto deletion of '%{public}@'
Failed to retrieve creation date from %@: %@
Failed to call getBootProgressRegisterMethod with error: 0x%x
Error getting system group container: %llu
Failed to fetch UID from unknown user '%@'
Saved type '%{public}@(%@)' report (%lu of max %lu) at %{public}@
scanning logs...
OSLogEventStream enumerate from %@ to %@
failed to save ca1 tasking: %@
Not applying %@ as it has already been set
Logfile '%{public}@' not submittable on opted out device
chown(-1, %d)
failed to get pressure level state: %d
Error while writing ips header: %{public}@
Error creating file %{public}@, %{public}s
sending sync request to %@
OSLogEventStream query ALL
crash_mover service returned ambiguous response, assuming failure
Failed to modify permissions while creating %{public}@: %s
%s
processing %zu events from queue
Expected to find xattr with name %s at '%s', but it was missing
Failed to generate temporary file: error %d (%s)
failed to set NSURLIsExcludedFromBackupKey '%{public}@': %{public}@
successfully applied ca1 tasking update: %@
Exclave frames offset of %d for thread %llu is invalid
proxy %@ taskId %@ with rawblob (%lu bytes) is inconsistent
Forcing Multi User Mode behavior due to the presence of /var/db/forceMultiUserMode
=== Attempted change gid on existing path: %{public}@ from %d to _analyticsusers (%u) with result %d %{public}s
Failed to retrieve DRE opt-in value
AppleCareSupport: ERROR[%d] setting xattrs on %s, %s
CFBundle URL refined %@ to %@
DiagnosticsReporter or DiagnosticsReporterLaunchOptions class not found.
Missing 'Value' key for %@ / %@ / %@
Got xpc error message from %s: %s\n
Skipping safe open because no path was provided
event queued pending RTCReporting intialization
xpc2ns: unrecognized type: %p
Failed to read %s: error %d (%s)
nothing to do for ca1 tasking update
failed to remove previous ca1 tasking: %@
unable to allocate %d bytes for wired memory info
Retaining additional log with bug type %{public}@
(C6. report request completed successfully, but no filename returned!)
Invalid XPC response
unable to convert localtime from %ld secs
found fallback user defaults %@: %@
%@ could not be safely opened
Error getting security.codesigning.monitor: %d %{public}s
NSBundle URL refined %@ to %@
No matching service found
deferring da3 task failed
client log create type %{public}@ result %@: %{public}@
Error setting protection class after retiring %{public}@: %{public}s (%{public}i)
SpeedTracer response %d '%@' received %d bytes\n
Failed to convert to header to json
Fetched addresses: %@
scan: skipping '%@': failed to find a matching routing
Failed to set DRE opt-in value to %d
crash_mover service FAILED with XPC error: %s
AppleCareSupport: purging old (limit %d vs actual %d) %s
ips metadata not detected (%ld bytes before newline), attempting to read entire file as payload
JSON ERROR: %s, payload:\n%s
samplingKey [randomizing due to failure] was %{public}@
Failed to find subdirectory for proxied device with ID %@
*** found alternate bundle
failed to extract JSON data from speedtracer result: %@
releasing RTCReporting
Error initializing report: unable to convert body stream to data
Not applying %@ as it is sampled and this device isn't IN
Failed to get the root submission path.
unsupported log type '%@' effective (%@)
error configuring RTCReporting
%@ taskId %@ with rawblob (%lu bytes) is inconsistent
No addresses fetched. So using username. %@
Logfile '%@' rejected for submission: missing metadata (or fread errno %d)
XPC Response: '%s'
Running the state monitor.
%{public}s %@
Error listing xattrs at path '%{public}s': expected to read %ld bytes but read %ld bytes
parts %d (%@), new_parts %d (%@) mask %d
Report of type '%{public}@(%@)' not saved because the limit of %lu logs has been reached
Cleaning up retired logs (in %@)
Failed to stat %@ while creating Retired directory
Unable to get XPC connection to osanalyticshelper for DRE opt-in get
RTCReporting Realtime: sendOneMessageWithSessionInfo failed
failed to clean up ca1 tasking: %@
removing outdated da tasking (and restoring hotship) %@ -> %@
found ManagedPreferences pref %@: %@
Log::initWithPath:'%@' forRouting:'%@' options:%@
Failed to stat %{public}@ when checking group ownership: %s
Tasking blob was not encodable: %@
Logfile '%{public}@' type %{public}@ invalid for platform
Sparing %s '%{public}@'
speedtracer error response: %@
Attempted xpc_user_sessions_get_foreground_uid() while fetching preferences for key %{public}@ but failed with error %{public}d - %{public}s
Unexpected tasking value type for key 'fastLane' (type: %{public}@, value: %{public}@) encountered
creating type %{public}@ as %{public}@
Not purging %s/%s: log did not meet criteria
Failed to get the data vault submission path.
Unable to load ManagedConfiguration, falling back to MobileGestalt
AppleCareSupport: new %s
Stackshot requires reason; ignoring request
Unable to dynamically load NanoRegistry framework
chmod(%d)
Mount path can only be overridden in the device recovery environment
found prefix in domain %@
%{public}@
Cleanup %s '%{public}@'
Unable to get XPC connection to osanalyticshelper for DRE opt-in
The location of the CA taskedConfig is %{public}@
validated %@@%@:%@=%@
Report of type '%{public}@(%@)' not saved because the destination is unavailable
Failed to remove old log '%@': %@
Identified heartbeat mismatch. Reporting to RTC now.
this log appears to be from the DA grid, using parsedData section
Using kDAAccountEmailAddress to fetch Exchange email addresses.
FAILED untrusted path validation '%{public}@' -> '%{public}@' [%{public}@]. Error: %d %s
failed to get display state: %d
Successfully set DRE opt-in value to %d
crash_mover service FAILED on setup: %s
Write failed to file %s - %zd of %d bytes written - uid: %d gid: %d, euid: %d egid: %d - error %d: %s
Successfully overrode mount path. New root path: %@. New container root path: %@
memorystatus_control for command %d returned unexpected valud of %d which does not match buffer size of %d
Using ACAccountPropertyIdentityEmailAddress to fetch email addresses.
Invalid connection to %s. Caller may need sandbox exception.
%s %@
linking RTCReporting.framework
Opted in for DRE
locallyCreateForSubmission: Failed to create copy of data vaulted crash report with error %@
nixed dupes bumped to %d on original %s
checking domain %@ prefix '%@'
Moving source file '%{public}@' into submission directory
OSLogEvent unsupported in this environment
Error creating temporary file for symbolicated log
Unable to determine UUID for host. Error: %d %s
intializing RTCReporting...
Logfile '%@' rejected for submission: bad metadata (or json error %@)
C6. report request failed: %s
Unsupported ips/xattr type %@ for '%@'
Log cleanup request successfully completed
C4.! payload writer exception: %@
known duplicate signature
Logfile '%{public}@' invalid for submission: unknown type %{public}@
Using system group container: '%{public}@'
Error creating log at %s/%s while purging: %@
Failed to get the home directory submission path for %{private}@.
OSLogEventStream query '%@'
unable to run sysctl hw.machine
Gathering non-mobile logs via crash_mover
=== Attempted change gid on new dir: %{public}@ from %d to _analyticsusers (%u) with result %d %{public}s
Invalid PayloadContent entry - expected dictionary
Submissions were disabled over a week ago: re-enabling submissions
Removing old log '%@'
xpc error message from %s: %s\n
Couldn't get XPC connection to %{public}s
Failed to set xattr '%s' at path '%s': error %d (%s)
saving ca1 tasking as %@
%@ is valid but couldn't stat or it's not a directory
C6. report request completed: %s
AppleCareSupport: ERROR[%d] scanning '%s', %s
Exclave data not present for thread %llu
Expected a task specific shared cache with ID %{public}@ but none was found
Tasking selection error: %@
Missing or invalid 'User' key
Process %{public}@ [%d] killed by jetsam reason %{public}@
Error while serializing ips metadata %{public}@. Error: %{public}@
Couldn't get XPC connection to %s
Retrieved DRE opt-in value: %d
Failed to stat '%{public}s'
unrecognized date format %d
Error reading report %{public}s: %s
SimulateCrash() on another process is not supported
applyTasking routing %@ id %@ length %d; untasked %d
Invalid regex '%@'
Missing or invalid 'Key' key for %@ / %@
Logfile '%@' allowed for submission for testing
scan: including '%@'
new signature found -- prioritizing over duplicate (removing %@)
mode ok
Skipping rename of %{public}@ because the updated path is nil.
Error while writing report payload: %{public}@
Error: bug_type key not found in report header
Configured value for submissionsDisabledSince key is not in the expected format: deleting key
chown(%d, -1)
no reason to scan
AppleCareSupport: event \"%@\"
RTCReporting.framework is unavailable
Skipping transfer from unsupported device
Unable to move tmp file '%{public}@': %{public}@
createForSubmission: %@ metadata: %@ options: %@ block: %p (by %@)
C1. request '%@' report service via XPC/osanalyticshelper
path is not whitelisted for listing: %@
AppleCareSupport: ERROR[%d] rename failed, %s
OSLogEventStream found %lu lines after %.1f secs (invalidation: %@)
owners: %d, %d mode 0x%X
Logfile '%@' failed to open (errno %d)
C5. payload writing complete, return status %d
StagedVolume
roots_installed
Connection error to %s: %s
visVisible
mobile
v12@?0i8
Public
rejected
state-monitor.ca.event
/usr/bin
failed to persist symbolicated log
system_usec
lu
crashreporter_key
w
%@ (%@:%ld:%d)
\"%@\" : \"%@\"
retiredReason
ioStats
v24@?0@\"NSArray\"8@\"NSError\"16
Containers
optinOverride
[section_stack count] == 1
staged
proc_uptime_appx
errorDesc
exceededWQConstrainedLimit
kThreadUnknown
kDAAccountEmailAddress
xform-persist
 with unknown owner
pageins
<null>
disabledLogs
Failed to open newly created directory
%@Count
lx
purgeable_nv
AutomatedContextURL
<%lu>
CFBundleShortVersionString
com.apple.osanalytics.daFlow
frames
event_code
container
gm
capture-time
X-ST-GroupName
multipart/form-data; boundary=%@
caller
missing stackshot buffer or size
value
expectedCAHeartbeats
tmp1
monitoring timed out for service without diags
TH_SFLAG_RW_PROMOTED
idle-exit
rpages
/private/var/mobile/Library/OSAnalytics/Preferences
  fault
)#
TH_SFLAG_BOUND_SOFT
no-compressor-space
ACEmailAliasKeyEmailAddresses
Fonts
com.apple.ReportCrash.stackshot.sharedCacheLoader
#(
!
turnstileInfo
failed to generate temporary file
v16@?0q8
routing
app_name
rsp
mach_msg send on port %#llx in transit to 
stacks
priorities
location
disable-panic-report-submission
%s/%s
\r\n
ProxiedCrashCopier
TH_TERMINATE2
-----------\nFull Report\n-----------\n
+[OSABridgeLinkProxy setLink:]
submission_from_recovery_mode_with_reason
modify_perms_success
MountedVolume
general.*\\.log
hits
kThreadDarwinBG
ld
iokit
pathOptionNoBackup
rejected-config
override-filePath
analyticsd_sub
darwinBG
zone-map-exhaustion
etl_key
filterByHeaders
/bin
start_path
pageouts
purgeable_count
QOS_CLASS_USER_INITIATED
product_version
com.apple.OSAnalytics
disableWatchdogStackshot
v16@?0@\"NSString\"8
Error creating temporary file for symbolicated log
isComputeController
AppleTV
submissionStartTimestamp
log_file_created
CrashReporter
queue thread to be allocated
additionalDetails
Primary
Preferences
v32@?0@\"NSTextCheckingResult\"8Q16^B24
pids
non-parseable kc snapshot buffer
TH_SFLAG_ABORT
OSASyncCrashReporter
__APPLE_OWNED
Application Support
Spotlight
Widgets
set-log-limit
DeviceDefaultsToAnalyticsOptIn
Ozone
Thread %d name:  %@%@%@
-[NSMutableDictionary(OSALogTrackerExtension) osa_logTracker_isLog:byKey:count:withinLimit:withOptions:errorDescription:]
external_page_count
ACAccountTypeIdentifierExchange
  domain %@ => [%@]
iDisk
rosetta
osanalytics_beacon
userID
dyldCompactInfoFaultedIn
TH_SFLAG_POLLDEPRESS
vm-compressor-thrashing
only-proxied-device
security.codesigning.monitor
{%@}
unsupported JSON schema version
busyBufferCount
conclave-limit
@\"NSDictionary\"8@?0
ThermalPressureLevelLight
Thread %d crashed with ARM Thread State (32-bit):\n    r0: 0x%08x    r1: 0x%08x      r2: 0x%08x      r3: 0x%08x\n    r4: 0x%08x    r5: 0x%08x      r6: 0x%08x      r7: 0x%08x\n    r8: 0x%08x    r9: 0x%08x     r10: 0x%08x     r11: 0x%08x\n   
Thread %d instruction stream (single cacheline):
xform-tracer-group
187
kThreadMain
Value
crk
procName
Alternate
rejected-rawsize
log-submission
%p + %llu%@%@
stacks+%@
lookups
wired
ReopenPath
osatool
container && (container.type == STACKSHOT_KCCONTAINER_TASK)
low-private-shared-ratio
__BUNDLE
AppleInternal
include-hidden
tmp0
rdi
kernelFrames
sharedRegionNone
%lld
table
limit
309
configureProxyDevice
compressor_page_count
/Library/Preferences
progname
Printers
dupes
port %#llx with unknown owner
0x%08x
OSASystemConfiguration.m
alt-metadata
Log age filter incorrectly formatted
kUser64_p
original_gid
<value>
%F-%H%M%S.%%03u
turnstile had unknown status (flags: 0x%llx)!
\"%@\" : {
submission-logs-added-to-archive
keyFrame
  Cacheline:
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
Fatal error
v20@?0I8r^{stackshot_thread_waitinfo_v2=QQQCsI}12
rejected-doNotSubmit
KPX
Audio
v20@?0I8r^{exclave_textlayout_segment=[16C]Q}12
kRTCReportingSessionInfoContainsRealtimeEvents
procname
TH_SFLAG_ABORTSAFELY
internal
notes
unexpected tasking result
JetsamEvent
    last <keeping    > => %@[%@]
%@: %@
symbol
9
B24@?0r*8@\"NSObject<OS_xpc_object>\"16
state
codeSigningAuxiliaryInfo
OS Version
keepFile
@mask
kern.version
%-*u %@
kernel returned (0) from memorystatus_control(MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT) -- no jetsam data available
eventCode
Spelling
unknown-%u
task_read_for_pid(%d) for resampling UUIDs failed with %d
ProductVersion
-[OSAProxyConfiguration isFile:validForSubmission:reasonableSize:to:internalTypes:result:]
2
Retired
cleanup_paths
No jetsam status list available (size query returned %d)
509
lastMadeRunnableTime
Country
resume
displayState
submission-started
OSAExclave.m
TH_SFLAG_EAGERPREEMPT
lastSuspendedLogDumpedDaySince1970
%@-internal
ips
OSAReport.m
-[OSAExclaveContainer parseKCdata:]
\n tmp0: 0x%016qx tmp1: 0x%016qx tmp2: 0x%016qx\n
usedImages
suspended
modify_gid_value
    last <masking    > => %@[%@ -> %@]
Unable to move tmp file
legacyInfo
uuid
kRTCReportingUserInfoClientName
locked 
blob
added_to_archive
mach_msg receive on %@port set %#llx
wire_count
stackshot_duration_outer_nsec
zoneMapCap
DnUOverride
errno
unknown-arch
%FT%T%z
 owned by pid %lld
frontmost
tmp2
com.apple.CrashReporter
bugType
ldm
exceededWQTotalLimit
iTunes Plug-ins
%@ %@ 0x%05llx 0x%llx %@[%d] (%@): %@%@
com.apple.osanalytics.monitors
%18p - %18p %@ (%@) <%@> %@
turnstile blocked on task pid %lld, hops: %d, priority: %d
suspensionProcID
containers
System/Library/CoreServices/SystemVersion.plist
ARM-64
Failed to open intermediate path
%18p - %18p %@ %@  <%@> %@
disablePushOnWrite
dyldCompactInfoTooBig
only-retired
containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist
Failed to get jetsam status list (query returned %d)
TH_SFLAG_BASE_PRI_FROZEN
Motion
reasons
%x
stringByTrimming
hw.machine
swapins
TH_SFLAG_PRI_UPDATE
opt
r11
  [%02d] (%@) -> (%@)\t%@
waitinfos
ColorPickers
330
imageOffset
xform-trace
resampled %d of %d threads with truncated backtraces from %d pids: %@
ca1-ohttp
oldFilePath
v16@?0@\"NSFileHandle\"8
faultingThread
port %#llx owned by kernel
postSampleVMStats
file-read-data
urgent
rflags
227
monitoring timed out for service
<0x%X>
variantVersion
blocked on workqueue: 0x%llx, hops: %d, priority: %d
absoluteTime
isSafe: %d, isArgument: %d, stringValue: %@
vm-compressor-space-shortage
http_post_started
com.apple.
%d
inactive
-[OSAStackShotReport decodeKCDataWithBlock:withTuning:usingCatalog:]
userFrames
snapshotFlags
kThreadIOPassive
proxyingDeviceTimeAtReceipt
idleDelta
backboardd
Volumes
flag
userUUID
rejected-unregistered
<item>
total_uncompressed_pages_in_compressor
qosEffective
anonymous
StartupItems
.mss.anon
trap
kHasDispatchSerial
kThreadOnCore
tasked-cfg_%@
UnknownType
override-fileName
com.apple.osanalytics.submissions.retire
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_SCRESULT)
additional_payload
schedFlags
uptime
submission_params
HomeDirectory
Invalid XPC response
ErrorPowerAssertionExpired
triggered
memoryStatus
paging
systemgroup.com.apple.osanalytics
\\^\\([^\\)]+\\)
OSALegacyTransform
_sharedProxyInstance == nil
sampleTruncatedStacks
rawFlags
metadata
<sync>
/Library/Managed Preferences/mobile/
385
System
rdx
-1
<no_sn>
!3
'%@' template not found
recently
progName
exception_code
resampleIncomplete
TH_SFLAG_PCORE_ONLY
TaskingOS
boot_time_appx
/private/var/mobile/Library
osVersion
incident_id
pagesReclaimed
com.apple.da
<preserve>
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_IPCSTACKENTRY)
Thread %d instruction stream:
No speedtracer results
%F-%H%M%S
suspensionTime
kThreadTriedFaultBT
NRPairedDeviceRegistry
%@ %@ (%@)
.GlobalPreferences
Users
kern.roots_installed
<unknown (error %d)>
container && (container.type == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK)
x
DiagnosticLogs
AppleSoCMisc
Install
os_build
Thread:%@; Layout info does not exist for layout id %@
ARM64_32
threadById
isTranslated
serial
cpsr
r12
offset
Unable to transform log
obj
port %#llx name %#llx
n/a
(invalid-reason)
ThermalPressureLevelTrapping
/Volumes/NETWORK
plugin
Input Methods
AnonymousIdentifier_%@.plist
incident
reactivations
TH_SFLAG_UNKNOWN
/private/var/containers
endTimestamp
pagesWanted
data
saved
SeedGroup
unknown type %u (owner %llu, context %#llx)
dyldCompactInfoMissing
TH_TERMINATE
reports
namespace
variant
Delete oldest file failed
PayloadType
release_type
state-monitor
imageIndex
sourceFile
 owned by thread %lld
additionalPayload
@keep
ScriptingAdditions
create-tmp
lastSuccessfulState
%F %T %z
210
QOS_CLASS_USER_INTERACTIVE
kThreadFaultedBT
OSADiagnosticsReporter
fds
pll.anon
%@ + %llu%@%@
index
internal_page_count
Domain
tasking.%@.proxy
fastLane
cpuType
reportNotes
Updates
thermalLevel
userTime
kThreadTruncUserBT
%f
%p
other
custom_headers
kern.bootargs
sustained-memory-pressure
rejected-size
166
failed
<descend>
ca-2hr-heartbeat
 Crashed
lastExceptionBacktrace
compressions
kThreadTruncUserAsyncBT
ApplePMGR
%@Day
{column %lu}
%F %T.%%02u %z
flags
resampledUserFrames
memorystatus_control gave snapshot size (%lu) not multiple of jetsam entry type (%lu)
328
OSABridgeLinkProxy.m
krwlock %#llx for writing
codeSigningMonitor
cpuTime
Sites
lastBranchState
details
port %#llx
waitInfo
Removal
defaults_key
app
turnstile has unknown inheritor
pthread condvar %#llx
lld
No processes were jettisoned (either killed or suspended)
reject_reason
OSAnalytics
stackshot inclusion disabled
debug_block
uuid_faulting
SystemVolume
bundle(%@)
errorMessage
report
ARM
ip
osanalytics_monitor_ca_submission
portlabels
_dyld_process_info_create(%d) for resampling UUIDs failed with %d
sync request failed (mach ipc: %s)
keep       
-[OSAReport streamContentAtLevel:withBlock:]_block_invoke
Thread %llu has exclave frames but no kernel frames
bluetooth
ThermalPressureLevelNominal
Extensions
build
@
physicalPages
unable to lookup port for %@
CA_endTimestamp
JSON schema not understood
osanalyticshelper
v16@?0@\"NSArray\"8
pageSize
unknown
background
ExperimentGroup
???
Q
-[OSABridgeLinkProxy transferInternal:key:]
developerMode
systemTimeTask
pageIns
visible
{ \"notice\": \"This log is currently stored only on your device.\" }
symbolLocation
cacheLine
stackshot_duration_nsec
suspensionProcName
captureTime
tmp
Device Software Diagnostic Log
vmRegionInfo
speculative
TH_SFLAG_RT_DISALLOWED
AppleConnect
...
xform-full-report
threadTriggered
vmregioninfo
isCorpse
409
instructionState
id
assertion
framework
OSLogEventStore
%llu
/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
NetworkVolume
%@-%@%@
Logs
app_build_version
+[OSAStateMonitor recordEvent:with:]
q
failed to save da3 tasking for scheduled installation
PrivateFrameworks
observer_info
proxy
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_TEXTLAYOUT)
taskId
rejected-platform
FAILED
v32@?0@8@16^B24
rcx
threads
reason
OSAStackShotReport.m
memorystatus_control returned unexpected value - %d: %s
PreferencePanes
-
template has illformed definition
log_countkey
krwlock %#llx for reading
systemDefaultSharedCache
User
genCounter
DoNotSubmit
GM
com.apple.osanalytics.directory_modification
]
donatingPids
jitEndAddress
share_with_app_devs
B24@?0r*8r*16
v24@?0@\"OSLogEventSource\"8@\"NSError\"16
Unable to read JSON
long-idle-exit
/
Dictionaries
bundleID
presig_hash
restrictedBool
+[OSAStateMonitor processCALogEvent:eventPayload:into:]
succeeded
blocked on %lld, hops: %d, priority: %d
frozen
resampledAllImages
resampledExtraImages
daemon
ACAccountTypeIdentifierIMAP
Ruby
i16@?0@\"NSData\"8
allowIdleExit
taskingID
%
%llx
PlugIns
Timestamp                         Type Thread  Act Process[pid] (Sender)
/System
ARM_THREAD_STATE32
frontmostPids
TH_RUN
p
ErrorFileNotReadable
inline
&
tracer_url
mach_msg send on 
queue processed by thread %llu
Failed to set flags for stackshot config
copyOnWriteFaults
QOS_CLASS_BACKGROUND
hhd
(unknown-reason)
com.apple.osanalytics.factoryproxysync
resampled %d of %d images missing from %d pids: %@
kStacksPCOnly
system_ID
watch-companion
Internet Plug-Ins
<cleanup>
rejected-fstat
v24@?0r*8r*16
v8@?0
%s
/var/db/forceMultiUserMode
unknown reason
Unexpected reply from %s
com.apple.osanalytics.AppleCareSupport.open
thread %llu in compressor segment %#llx
%@
Frameworks
rsi
OSALegacyXform
xform-fileURL
~/Library/Logs/DiagnosticReports/
uuidResampling
processes
ext
v16@?0r^{dyld_shared_cache_dylib_text_info=QQQ[16C]*Q}8
%08X
err
--%@\r\nContent-Disposition: form-data; name=\"%@\"; filename=\"%@\"\r\nContent-Type: %@\r\n\r\n
%@lock %#llx
task_read_for_pid(%d) for resampling backtraces failed with %d
exclaveScid
dirty
periodic
DeviceClassNumber
Too few path components
port %#llx owned by pid %llu
Unmapped pages caused truncated backtrace; re-sampled %d frames
OSATasking
internal_key
File doesn't exist
<unavailable>     
SpringBoard
visNonvisible
csTrustLevel
Couldn't get XPC connection to %s
OSLogEventStream
twoHrHeartbeat
OSAFileOperations
 (%@:%@)
0x%llX
reads
audio
neuralPages
timestamp
found_for_submission
Documentation
<exempt>
logPath
<index>
xform-metadata
osanalytics_jetsam
osanalytics_monitor_hb_diff
com.apple.CA
queue that is suspended
isDirtyTracked
jetsamCoalition
llx
deployVersion
submitted
%ld
SystemProfiler
disconnected
actualCAHeartbeats
ConfigurationContent
operation
,
container && (container.type == STACKSHOT_KCCONTAINER_THREAD)
no shared cache available from the kernel snapshot -- this may impact symbolication
suspensionDuration
highwater
multi_user_mode
taskedConfig.json
TH_SFLAG_NO_SMT
DiagnosticsReporterLaunchOptions
modify_gid_success
ACAccountStore
Utilities
datawriter returned with negative response
\"%@\" : [
bad_blob_%@_%@
per-process-limit
max_pages
/System/Library/PrivateFrameworks/OSAnalytics.framework/submissionConfig.plist
extensions
Day_Seq
r15
threadState
watchSync
CarrierInstallCapability
create_dir
rejected-fopen
retired-reason
pc
\"
xform-error
pageFaults
out-of-slots
rbp
isSimulated
suspendCount
runawayMitigation
TH_SUSP
defaultTasking
(%@)
macOS
device_in_recovery_mode_with_reason
model
...%@
<unknown>
systemBuildVersion
error_desc
v24@?0Q8@\"OSLogEventStreamPosition\"16
container && (container.type == STACKSHOT_KCCONTAINER_EXCLAVE_ADDRESSSPACE)
failed to open tasking payload file: %s
Got fewer jetsam entries from the kernel; received %zu, expected %zu
ThermalPressureLevelModerate
com.apple.osanalytics.sanitizer
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
memoryPressure
[kc_stack count] == 0
QOS_CLASS_MAINTENANCE
v16@?0@\"OSLogEventProxy\"8
%@\n%@%@\n%@\n
ers_namespace
, 
container && ((container.type == STACKSHOT_KCCONTAINER_TASK) || (container.type == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK))
suppressed
isImpDonor
inconsistant tasking
unable to allocate %d bytes for jetsam snapshot
uncompressed
QuickTime
only-urgent
Unable to open file
<sort>
ErrorFileNotFound
v20@?0I8r^Q12
esr
allPids
TH_SFLAG_REEVALUTE_TG_HIERARCHY_LATER
Unable to find class %s
untasked
displayName
<whitelist>
vm-pageshortage
disk-space-shortage
AutomatedDeviceGroup
Internal
r9
osanalytics_logEr
name
%@%@
ThermalPressureLevelSleeping
dev
Couldn't config private XPC connection
submission-found-logs
https://speedtracer.apple.com/api/v2/trace?detail=full
(unknown)
B20@?0i8^@12
platform
327
stackshot_tuning
waitEvent
%lu
Developer
proxiedDeviceID
systemTime
file-owner-uid
com.apple.osanalytics.stateMonitor
com.apple.OTACrashCopier
recursionInfoArray
ers_code
 owned by thread %llu
fileBacked
Unknown KCDATA ARRAY type %X, count %d, size %d, flags %llX
301
Logs/CrashReporter
transfer_paths
 in spin mode
suspensionCount
eOS
stackshot
q24@?0@8@16
queue
308
ers_flags
unindexed_frames
accessory
rejected-header
r10
extDarwinBG
298_HIGH_PRIORITY
Movies
@loader_path
log_filepath
free
<unprintable>
nonpaging
kThreadTruncKernBT
u
is_non_fatal
error
TH_SFLAG_FAILSAFE
bundle
UDID was null
CA_startTimestamp
analyticsd
PID
invalid_images
kGlobalForcedIdle
log_types
Diagnostics
/Users/USER
331
%p + %llu
@rpath
MCFeatureAppAnalyticsAllowed
rbx
radars
spindump
@files
Thread %d%@:%@%@%@%@
Unable to create VMUSampler for %d
foreground
boosted
isLiveImpDonor
mask       
override-limit
UDID:                %@\n
\\$\\((([^\\)\"]+|\"[^\"]+\")+)\\)
active_count
throttled_count
processUptime
action
datavault-filePath
state-monitor.ca.event.%f
Version
isNonFatal
bootProgressRegister
suspensionSources
resampledUserFrames might be missing second-to-leaf frame
%@ %@
codeName
thermalPressureLevel
-upgrade
ca-log-written
os_version
whitelisted_domains
totalHeartbeats
<key>
-------------------------------------\nTranslated Report (Full Report Below)\n-------------------------------------\n
free_count
notice
suspensionThreadID
TaskingPayload
Unknown
@bundles
tuning
%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x
low-swap
excess-shared-memory
@apple.com
modify_gid
train
file-owner
stackResampling
\n
disabled
zoneMapSize
```
