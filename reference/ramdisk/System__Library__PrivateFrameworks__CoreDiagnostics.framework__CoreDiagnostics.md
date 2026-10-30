# `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,075,024 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 55 (Size: 8224)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (37)

- `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics (compatibility version 0.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/TrialProto.framework/TrialProto (compatibility version 1.0.0, current version 511.1.2, weak)`
- `/System/Library/PrivateFrameworks/Trial.framework/Trial (compatibility version 1.0.0, current version 511.1.2, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/SecureConfigDB.framework/SecureConfigDB (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary (compatibility version 1.0.0, current version 441.26.3, weak)`
- `/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams (compatibility version 1.0.0, current version 259.0.0, weak)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication (compatibility version 1.0.0, current version 64578.104.1)`
- `/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels (compatibility version 1.0.0, current version 297.12.4, weak)`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/RTBuddyCrashlogDecoder.framework/RTBuddyCrashlogDecoder (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/Symbolication.framework/Symbolication (compatibility version 1.0.0, current version 64578.132.1)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/swift/libswiftAccelerate.dylib (compatibility version 1.0.0, current version 82.0.0, weak)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreAudio.dylib (compatibility version 1.0.0, current version 482.208.0, weak)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftMetal.dylib (compatibility version 1.0.0, current version 383.1.2, weak)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftQuartzCore.dylib (compatibility version 1.0.0, current version 5.0.0, weak)`
- `/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib (compatibility version 1.0.0, current version 919.1.13, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1, weak)`
- `/usr/lib/swift/libswift_StringProcessing.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`
- `/usr/lib/swift/libswiftsimd.dylib (compatibility version 1.0.0, current version 25.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (28 classes, 4 protocols)

Classes: `AirPodsCrashReportObjc`, `CDJetsamReport`, `CDStackshotReport`, `CDSystemWatchdogStackshotReport`, `CDTerminatingStackshotReport`, `CPUTracePIDSelectorObjC`, `NSArray`, `NSError`, `NSMutableDictionary`, `NSMutableString`, `ReportViewerObjC`, `SharedCacheEntry`, `_SwiftDiagnosticPatternMatching`, `_SwiftPanicPatternInfo`, `_TtC15CoreDiagnostics11DeviceState`, `_TtC15CoreDiagnostics11PatternInfo`, `_TtC15CoreDiagnostics16CrashPatternInfo`, `_TtC15CoreDiagnostics19CPUTracePIDSelector`, `_TtC15CoreDiagnostics19CompatibilityBridge`, `_TtC15CoreDiagnostics21CrashReportBodyBridge`, `_TtC15CoreDiagnostics22AppleIntelligenceState`, `_TtC15CoreDiagnostics24WatchdogExitReasonHelper`, `_TtC15CoreDiagnostics27TextualRepresentationBridge`, `_TtC15CoreDiagnostics31DiagnosticReportCollectorBridge`, `_TtCC15CoreDiagnostics11CrashReport13CrashRedacter`, `_TtCFC15CoreDiagnostics22AppleIntelligenceStateP33_088BB0F0F87A4F30D60030036C3E7D2E28updateAppleIntelligenceStateFT_T_L_14XPCQueryResult`, `objcDiagnosticPatternMatching`, `objcPanicPatternInfo`

Protocols: `NSObject`, `OSAConcreteReport`, `OS_xpc_object`, `_TtP15CoreDiagnostics29ReportSystemMemoryXPCProtocol_`

## Strings (1,668)

```
softlink:o:path:/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices
_TtC15CoreDiagnostics11CrashReport
_TtC15CoreDiagnostics27TextualRepresentationBridge
_TtC15CoreDiagnostics21CrashReportBodyBridge
CDSystemWatchdogStackshotReport
_TtC15CoreDiagnostics19CPUTracePIDSelector
_TtCC15CoreDiagnostics11CrashReport13CrashRedacter
_TtCFC15CoreDiagnostics22AppleIntelligenceStateP33_088BB0F0F87A4F30D60030036C3E7D2E28updateAppleIntelligenceStateFT_T_L_14XPCQueryResult
objcDiagnosticPatternMatching
NSObject
_TtC15CoreDiagnostics22AppleIntelligenceState
CDJetsamReport
SharedCacheEntry
_TtC15CoreDiagnostics24WatchdogExitReasonHelper
_TtC15CoreDiagnostics12JetsamReport
_TtC15CoreDiagnostics11DeviceState
CDTerminatingStackshotReport
ReportViewerAugment
_TtC15CoreDiagnostics11PatternInfo
_TtC15CoreDiagnostics19CompatibilityBridge
_TtC15CoreDiagnostics31DiagnosticReportCollectorBridge
OSAConcreteReport
_TtP15CoreDiagnostics29ReportSystemMemoryXPCProtocol_
CPUTracePIDSelectorObjC
AirPodsCrashReportObjc
CoreDiagnostics
PIDListExtension
CDStackshotReport
ReportViewerObjC
OS_xpc_object
_SwiftDiagnosticPatternMatching
_TtC15CoreDiagnostics16CrashPatternInfo
_SwiftPanicPatternInfo
StackshotKCDataExtension
objcPanicPatternInfo
_procPath
TB,R,V_isSnapshotDisabled
_isSnapshotDisabled
componentsJoinedByString:
initWithCapacity:
initWithKCData:
addTurnstileInfoDesc:count:elSize:
mutableCopy
sampleThread:
T^{dyld_uuid_info_64=Q[16C]},R,N,V_layout
removeObjectForKey:
T^[37c],R,N,V_sharedCacheUuid
kernelVersionDescription
readDataToEndOfFileAndReturnError:
T@\"NSString\",?,R,C
sharedScheduler
_visibilityEndowmentState
compare:
getEventPriority:terminationReason:priority:
original
setReason:
UTF8String
capture_absoluteTime
initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:
resampleUUIDsForTask:usingCatalog:
userAppName
T@\"NSDictionary\",&,N,V_spindump
setLog_path:
uid
domain
frontmostPids
sharedCacheID
addCustomField:value:into:
getFramesForThread:usingCatalog:
state
appendFormat:
autorelease
rollSchemaForward:
ss_trace_length
_thermalNotificationCurrentLevel
bootProgressRegister
getTaskingKey:
initWithZoneNames:nameCount:zoneInfo:zoneInfoCount:wiredInfo:wiredInfoCount:
push:
getVMStatistics
_largestActiveApp
launchAppWith:options:completion:
launchDiagnosticsReporter
performSelector:withObject:
stringValue
writeReportBodyWithSectionWriter:
_flags
top
codeSigningFlags
formatCallstacks:withImages:macosStyle:
writeData:
_snapshot
acquireJetsamData
createForSubmission:metadata:options:error:writing:
rangeOfString:options:
acquireStackshot
isCustomerFused
dateFromString:
isProxy
arrayWithObjects:count:
formatMemoryErrorReport:
matchesInString:options:range:
unsignedLongLongValue
_swiftPanicPatternInfo
getStackshotData
_dead_snapshot
_daysSince1970
appleCareDetails
regularExpressionWithPattern:options:error:
_original
copy
row
characterSetWithCharactersInString:
respondsToSelector:
setLocale:
sharedCacheUnreliableSlidBaseAddress
buildVersion
setSymbolicator:
addImage:address:size:
transformLines:withDefinitions:body:header:report:error:streamingBlock:
TQ,R,N,V_sharedCacheUnreliableSlidBaseAddress
initWithPID:options:
setPid:
_ss_sequence
kernelTextBase
setUnindexed_frames:
zoneInfo
initWithKey:ascending:
lastPathComponent
reduceToTwoSigFigures:
stringWithFormat:
bodyJson
metaData
setKernelImages:
logfile
code
data
numberWithDouble:
setSharedCacheInfo:
appleInternal
crashReport
dataWithJSONObject:options:error:
setInterval:
TQ,R,N,V_capture_absoluteTime
intValue
_layoutImageCount
_sharedCacheID
__swift_objectForKeyedSubscript:
bootSessionUUID
_additionalPayload
codeSigningMonitor
commonFieldsForBody:
debugDescription
firstMatchInString:options:range:
_getValueForKey:fromBody:orHeader:
addJITImage:size:
localizedDescription
objectForKeyedSubscript:
patternMatcher
removeAllObjects
sharedInstance
_extras
Ti,N,V_jetsamLevel
containsObject:
array
dictionary
initWithDictionary:
resampleTruncatedBacktracesForTask:forThreads:usingCatalog:in:usingSymbolicator:
TI,R,N,V_layoutImageCount
_includeSyslog
_thermalSensorValues
codeSigningID
_setDumpedSuspendedJetsamLog
appendString:
initWithPattern:options:error:
findBundleAtPath:withKeys:bundleURL:
isAddressInTargetedCache:
performSelector:withObject:withObject:
isAppleTV
saveWithOptions:
ss_trace_buffer
allObjects
setObject:forKey:
TB,N,V_includeSyslog
appendPortLabelInfo:portlabels:
truncated_threads
osTrain
componentsSeparatedByString:
T#,R
acquireJetsamDataWithFlags:
depth
iBootVersion
reportUsedImages
additionalIPSMetadata
isEqualToString:
setFlags:
stringWithContentsOfURL:encoding:error:
backtraceLength
dealloc
dictionaryWithObjects:forKeys:count:
initWithIdentifier:
lookForPatternAsync::
panicFrames
setInteger:forKey:
updateLogLimitFor:
panicPC
TQ,R
numberWithUnsignedInt:
randGenerator
dead_snapshot
incidentID
parsePortLabelContainer:
queue
ss_sequence
longLongValue
numberWithInt:
spindump
unsignedIntValue
TI,N,V_flags
reportNamePrefix
description
Tr^v,R,N,V_ss_trace_buffer
initWithMachServiceName:options:
setRequiresExternalPower:
standardUserDefaults
_pid
fetchSnapshotWithFlags:error:
superclass
cpuType
initWithSuiteName:
rangeAtIndex:
_jetsamLevel
usedImages
formatLastException:withImages:
_hexDump:offset:indicator:
instrumentEventsWithAudioAssertionState:visibliltyEndowmentState:
invalid_images
dispose
boolValue
sortedArrayUsingDescriptors:
hwModel
backtrace
getMatcherType
alreadyDumpedSuspendedJetsamLogToday
formatImages:macosStyle:
numberWithUnsignedShort:
value
isInLDM
_event_reason
sharedCacheUuid
stringWithUTF8String:
numberWithBool:
_exceptionCodeCount
sharedCacheSlide
substringWithRange:
flags
generateLogAtLevel:withBlock:
setThreadId:withScId:
startWithCallback:
init
TB,N,V_dead_snapshot
_cpuType
substringFromIndex:
isRedactionEnabled
isSnapshotDisabled
retainCount
setTaskCompleted
formatInstructionState:index:
initWithSwiftPanicPatternInfo:
etlKey
addEntriesFromDictionary:
addNotes:
_isSuspendedOnlyJetsam
errorWithDomain:code:userInfo:
initWithIncidentID:visibilityEndowmentState:audioAssertionState:
isEqual:
_bundleID
isActionable
setPriority:
pid
exceptionCodesDescription
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:
_sharedCacheSlide
filteredArrayUsingPredicate:
resume
unindexed_frames
_termination_info
asyncQueue
isLowPowerModeEnabled
lastObject
panicStringDelimiter
initWithPid:procName:bundleID:exitSnapshot:reason:
numberWithUnsignedLong:
numberWithUnsignedLongLong:
reasons
productNameVersionBuildString
setSpindump:
$__lazy_storage_$_getReportDate
_audioAssertionState
lookForPattern:
useStackshotData:frontmostPids:atTime:machTime:sequence:
pop
TI,R,N,V_sharedCacheID
_killedActiveApps
_sharedCacheUnreliableSlidBaseAddress
_ss_trace_length
self
_sharedCacheUuid
clientWithIdentifier:
includeSyslog
objectAtIndexedSubscript:
redacter
writeJetsamMemoryReportWithVisibilityEndowmentSet:audioAssertionSet:with:
_reason
formatArm64ThreadState:index:
formatFrame:withImages:macosStyle:
formatLastBranchState:index:withImages:
next
fetchWiredMemoryInfo
stringByPaddingToLength:withString:startingAtIndex:
stringByTrimmingCharactersInSet:
setJetsamLevel:
TQ,R,N,V_sharedCacheSlide
coldestElided
hash
integerForKey:
setRemoteObjectInterface:
initForPid:exitSnapshot:reason:
crashReporterKey
decode_cpuType
dictionaryWithCapacity:
formatProbGuardReport:
seekToOffset:error:
decode_reason:reason:
isDefaultSharedCache
isKindOfClass:
predicateWithFormat:
transformURL:template:options:
_spindump
setAdditionalPayload:
setKernelTextExecImages:
sortedPids
release
_isDefaultSharedCache
.cxx_destruct
_awakeSystemUptime
decodeKCDataWithBlock:withTuning:usingCatalog:
getPanicPatternInfo
initWithFileDescriptor:
parent
getDisplayState
numberOfRanges
objectForKey:
queryThermalData
transformReport:templateString:header:report:error:streamingBlock:
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:isSnapshotDead:
formatX86ThreadState:index:
generateReportWithBinary:testMode:productId:applicationInfo:description:
setInvalid_images:
stringByReplacingOccurrencesOfString:withString:
setIncidentID:
sortedArrayUsingSelector:
setRequiresNetworkConnectivity:
arrayWithCapacity:
panicReasonString
T@\"NSArray\",R,N,V_frontmostPids
_wiredBytes
hottestElided
_capture_absoluteTime
crashReportBody:
exceptionCode1
kernelSlide
isPatternPayloadAvailable
_swiftDiagnosticPatternMatching
TI,N,V_ss_sequence
_ss_trace_buffer
_tags
codeSigningValidationCategory
error
getThermalPressureLevel
modelCode
exceptionType
setKernelCache:address:size:
_aleFlag
_stackshot_config
getSyslogForPids:andOptionalSenders:additionalPredicates:
interfaceWithProtocol:
stringForKey:
hasPrefix:
report
initWithPatternInfo:
layoutImageCount
path
stream
firstObject
length
JSONObjectWithData:options:error:
_largestProcess
initWithTask:
exceptionCode0
retain
setDead_snapshot:
setRootedCacheLibs:count:
setSharedCacheLayout:andCount:
TB,R,N,V_isDefaultSharedCache
appendNotesTo:
augmentWithPrefix:
coalitionName
initWithName:reason:exceptionCode:exceptionCodeCount:
processInfo
stringByAppendingString:
ExcResourceReportPaths
_appName
_frontmostPids
addObjectsFromArray:
layout
instrumentEvents:
T@\"NSString\",R,C
optIn3rdParty
setIncludeSyslog:
addWaitInfoDesc:count:elSize:
invalidate
searchFrame:in:result:
synchronousRemoteObjectProxyWithErrorHandler:
type
_killed_or_suspended_count
dictionaryForKey:
integerValue
isMemberOfClass:
numberWithShort:
performSelector:
_getSnapshotWithFlags:
_exceptionCodes
iterateLogsWithOptions:usingBlock:
registerForTaskWithIdentifier:usingQueue:launchHandler:
zone
_layout
threads
class
conformsToProtocol:
formatFrame:withImages:macosStyle:showBinaryImage:
_event_code
getExtraData:
releaseType
TB,N,R
sortByAddressAndSetInferredSizes
submitTaskRequest:error:
valueForKey:
WriteJetsamMemoryReportWithVisibilityEndowmentSet:audioAssertionSet:
initWithSwiftDiagnosticPatternMatching:
descriptionFromCode:
name
parseKCdata:
bugType
fileValue
setSs_sequence:
initWithType:
omit
TI,R,N,V_ss_trace_length
_zones
formatArm32ThreadState:index:
initWithPath:forRouting:options:error:
problemType
dataWithBytes:length:
jetsamLevel
isDeveloperMode
formatMTEPageTags:report:
initWithPid:
bytes
count
setObject:forKeyedSubscript:
executeWithTimeout:Code:
levelForFactor:withNamespaceName:
T^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII},R,N,V_original
procName
reverseObjectEnumerator
tag
addObject:
countByEnumeratingWithState:objects:count:
taskRequestForIdentifier:
enumerateMatchesInString:options:range:usingBlock:
getAppleIntelligenceAvailability
setDateFormat:
vmRegionInfo
interval
targetSharedCache:withSlide:atBaseAddress:
v32@0:8r^v16I24I28
@28@0:8i16@20
v16@0:8
v32@0:8{kcdata_iter=^{kcdata_item}^v}16
v40@0:8r*16@24@32
^{_NSZone=}16@0:8
@48@0:8@16B24I28@32@40
^v
B24@0:8:16
I16@0:8
^[37c]16@0:8
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}
r^v16@0:8
@\"NSDictionary\"
B72@0:8@16@24@32@40@48^@56@?64
B24@0:8@16
i32@0:8@16@24
v20@0:8I16
@28@0:8@16B24
v16@?0@\"NSURL\"8
Vv16@0:8
v28@0:8B16@?<v@?@\"NSDictionary\">20
@\"NSString\"
Q
@\"_SwiftPanicPatternInfo\"
@28@0:8@16i24
v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?B>32
v16@?0@\"NSError\"8
B24@0:8#16
@40@0:8@16@24@32
v56@0:8r^v16I24@28d36Q44I52
v60@0:8r^v16I24@28d36Q44I52B56
^q
@\"NSMutableDictionary\"
r^v
q16@0:8
v20@0:8B16
v24@0:8@16
@20@0:8i16
v32@0:8@16@?24
@40@0:8@16@24B32B36
v24@0:8@?16
B32@0:8@16@24
#16@0:8
I
i16@0:8
@32@0:8@16i24B28
@\"NSDictionary\"16@0:8
Q40@0:8@16Q24q32
@44@0:8@16@24^q32I40
i60@0:8i16@20@28@36{_CSTypeRef=QQ}44
@32@0:8@16@24
@16@0:8
v16@?0@\"BGSystemTask\"8
v16@?0@\"NSFileHandle\"8
B16@0:8
@\"NSString\"16@0:8
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16@0:8
^[37c]
@24@0:8@16
@\"NSArray\"
@52@0:8i16@20@28^{exit_reason_snapshot=IQQ}36@44
@36@0:8@16@24B32
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}
v28@0:8^{dyld_uuid_info_64=Q[16C]}16I24
B64@0:8@16@24@32@40^@48@?56
@36@0:8@16i24@28
v40@0:8@16@24@?32
@32@0:8:16@24
B24@0:8@\"Protocol\"16
v16@?0@\"NSString\"8
v28@0:8B16@?20
@\"NSMutableArray\"
v52@0:8@16@24d32Q40I48
v20@0:8i16
@32@0:8^{exit_reason_snapshot=IQQ}16@24
@40@0:8:16@24@32
v8@?0
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}28@0:8I16^@20
@\"NSArray\"16@0:8
@\"NSSet\"
v28@0:8i16@20
@24@0:8:16
^{dyld_uuid_info_64=Q[16C]}
v40@0:8@?16@24@32
i
@\"_SwiftDiagnosticPatternMatching\"
v24@0:8^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16
@52@0:8i16@20@28^q36I44I48
@36@0:8i16^{exit_reason_snapshot=IQQ}20@28
Q16@0:8
@\"NSDictionary\"8@?0
v12@?0B8
v24@0:8Q16
B
^{dyld_uuid_info_64=Q[16C]}16@0:8
thawed
%d
trap
Heap underflow of 
resampledUserFrames
kernelFrames
schedFlags
com.apple.corediagnostics.diagnostic-intelligence
blamedAllocation
Terminated by Unblock framework for unrecoverable deadlock
vnode-limit
external_page_count
rip
triggered
The diagnostic service crashed or hung
inactive
swapouts
displayState
%p %@
(unknown)
additionalDetails
visVisible
TH_SFLAG_THREAD_GROUP_AUTO_JOIN
recursionInfoArray
Kernel UUID:\\s*([A-F0-9-]{36})
kThreadFaultedBT
Report transformation returned an unexpected output format.
faults
Unable to load log '%@'
lastSuspendedLogDumpedDaySince1970
busy compressor segment %#llx owned by thread %llu
\n
Thread %d last branch register state:
accessory
rpages
active_scenarios
compressor_page_count
r13
\nBlamed allocation: [
<data>
eventCode
process_images
kThreadSuspended
kThreadOnCore
fp
0x%llX
kKernel64_p
imageIndex
 (%@:%@)
INVALID
stackshot_duration_prior_nsec
krwlock %#llx for writing
free_count
%@
data
tracked
page list requests for VM object %#llx
rawFlags
none
kernel mutex %#llx
syslog
kGlobalForcedIdle
(\\S+)\\([^)]+\\)\\[([A-Fa-f0-9-]{36})\\]@(0x[0-9A-Fa-f]+)->(0x[0-9A-Fa-f]+)
customerFused
pagesReclaimed
procname
kThreadIdleWorker
imageExtraInfo
no shared cache available from the kernel snapshot -- this may impact symbolication
disableWatchdogStackshot
.
Terminated by Unblock framework for not recovering after hitting thread limit
LibCall_ACMKernelControl_Block
Stackshot syscall failed (from euid %d) with error %d: %s
hits
isLiveImpDonor
com.apple.gmAvailability.queue
IN_EAR
r8
log
memorystatus_control gave snapshot size (%lu) not multiple of jetsam entry type (%lu)
dispatch_queue_label
codeName
%18p - %18p %@ %@  <%@> %@
bluetooth
namespace
deallocationTrace
TH_SFLAG_RT_DISALLOWED
symbolTransitions
excess-shared-memory
blocked memory access for VM object %#llx
binaryImages
internal_page_count
pageIns
r9
threadState
isDirtyTracked
modelCode
Task List Section
stack
MTE Page Tags (faulting address: %p)
semaphore port %#llx
out-of-budget
container && (container.type == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK)
kStacksPCOnly
osVersion
%@%@%@\n%@\n
crashReporterKey
accessory_release_type
panic
pthread rwlock %#llx for writing
-----------\nFull Report\n-----------\n
No heap allocation information available
 (%@)
threadById
ip
Failed to allocate memory for stackshot config
userFrames
userTimeTask
--------
#
pthread rwlock %#llx for reading
exceededWQConstrainedLimit
parentPid
%s RECURSION LEVEL %u
rbp
com.apple.diagnosticservicesd
location
procPath
XPC request timed out
accessory_os_train
commandCursor == commandBuffer + sizeof(commandBuffer)
long-idle-exit
portlabels
Kernel text base:\\s*(0x[0-9A-Fa-f]+)
acm_mem_free_info
385
stack-description
anonymous
stacks
  cr2: 0x%016qx\n  \nLogical CPU:     %d\nError Code:      0x%08x %@\nTrap Number:     %d\n
com.apple.corediagnostics.patternMatchingQueue
throttled_count
copyOnWriteFaults
codeSigningAuxiliaryInfo
-
MTE Malloc Size Class: 
spin
Unmapped pages caused truncated backtrace; re-sampled %d frames
panicReasonString
CoreDiagnostics.PanicPatternInfo
TH_SFLAG_EXEC_PROMOTED
%s ELIDED %u LEVELS OF RECURSION THROUGH %s
background
 owned by thread %lld
Stackshot key-combo received while a prior stackshot was still processing.
container && (container.type == STACKSHOT_KCCONTAINER_THREAD)
processByPid
suppressed
xform-error
kcdata_iter_container_type(iter) == STACKSHOT_KCCONTAINER_PORTLABEL
%02x%c
port %#llx
esr
uuid_faulting
suspensionTime
dyldCompactInfoNone
QOS_CLASS_UTILITY
PanicPatternDefinition
Failed to allocate memory for jetsam status list
pageouts
nonpaging
TH_SFLAG_RW_PROMOTED
...%@
cr2
codeSigningFlags
fileBacked
stackshot_duration_nsec
!KCDATA_ITER_FOREACH_FAILED(kcData)
speculative
krwlock %#llx for reading
kcdata_iter_container_id(kcData) == end.tag
suspensionLastStart
TH_SFLAG_NO_SMT
(%@)
^([A-Z_]+), (\\[0x[0-9a-zA-Z]\\] )?(.*)$
backboardd
%-*u %@
performCommand
JetsamEvent
purgeable_count
spawnFlags
variantVersion
lowPowerMode
sp
offset
frames
unknown-arch
QOS_CLASS_UNSPECIFIED
Unknown
UI_country_code
dyldCompactInfoTriedFault
event_number
\\n\\s*loaded kexts:
fc-thrashing
shared_cache_layout
x
macOS
%s: %s: called.\n
residentMemoryBytes
CASE_LID_OPEN
container && ((container.type == STACKSHOT_KCCONTAINER_TASK) || (container.type == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK))
boosted
releaseType
%02x%02x%02x%02x
routed_to_source
reason
(unprintable)
 Crashed
assertiond
processes
v32@?0Q8r*16r*24
description
TH_SFLAG_RT_CPULIMIT
Unable to parse template
DIAGNOSTIC_PATTERN_MATCHING_CRASH
298_HIGH_PRIORITY
TH_SFLAG_ABORT
frozen_to_swap_pages
turnstile was in the process of being updated
<0x%X>
rsi
#(
CoreDiagnostics.DiagnosticPatternMatching
template has illformed definition
states
per-process-limit
bundleInfo
yyyy-MM-dd HH:mm:ss.SS Z
init
resampleIncomplete
spindump
table
page-ins throttled for VM object %#llx
ioStats
faultingThread
unsupported JSON schema version
availability
assertion
suspending
OSADiagnosticsReporter
rsp
ANC
DOCKED
SPARE_2
 owned by thread %llu
r15
com.apple.iokit.hid.displayStatus
is_beta
Product Version Section
LibCall.c
accessory_machine_config
Kernel Extensions in backtrace:
SPARE_3
no-swap-space
blocked on workqueue: 0x%llx, hops: %d, priority: %d
total_uncompressed_pages_in_compressor
suspensionThreadID
Panicked thread:.*?backtrace:.*?tid:\\s*\\d+\\s*\\n(.*?)(?:
incident
container.type == STACKSHOT_KCCONTAINER_THREAD
QOS_CLASS_USER_INTERACTIVE
Unable to read log stream: %@
SPARE_5
suspended-only jetsam log already dumped today
cpuTime
-%u
dirty
codeSigningMonitor
mach_msg send on port %#llx in transit to 
TALEngaged
tmp2
com.apple.corediagnostics.pattern-lookup-async
unfair 
parsedData
vm-compressor-space-shortage
Syslog query timed out
state
qosRequested
pc
unknown
intransit port %#llx
userID
flag
reactivations
kUser64_p
reportNotes
call-stack
locked port %#llx
pagesWanted
Faulting access is at offset 
Unknown transformation error.
%s: %s: returning, err = %ld.\n
no-compressor-space
 (service throttled by launchd)
%@ + %llu%@%@
frozen
bootProgressRegister
kThreadDarwinBG
captureTime
409
ThermalPressureLevelNominal
Kernel text exec base:\\s*(0x[0-9A-Fa-f]+)
v20@?0I8r^{stackshot_thread_turnstileinfo_v2=QQCCQs}12
\"
freeze_skip_reason:
jetsamCoalition
0x%016qx
Kernel Extensions in backtrace:\\s*\\n(.*?)(?:\\nloaded kexts:)
stackshot_tuning
isLocked
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
purgeable
highwater
Thread %d%@:
%18p - %18p %@ (%@) <%@> %@
Thread %d crashed with ARM Thread State (64-bit):\n    x0: 0x%016qx   x1: 0x%016qx   x2: 0x%016qx   x3: 0x%016qx\n    x4: 0x%016qx   x5: 0x%016qx   x6: 0x%016qx   x7: 0x%016qx\n    x8: 0x%016qx   x9: 0x%016qx  x10: 0x%016qx  x11: 0x%016qx\n
log-version
Got fewer jetsam entries from the kernel; received %zu, expected %zu
isTranslated
TH_SFLAG_BASE_PRI_FROZEN
kThreadIOPassive
\\n\\s*Kernel Extensions in backtrace:
kThreadTruncUserAsyncBT
<unknown>
%d unindexed user-stack frames from %d pids: %@
tmp1
timesThrottled
writes
[kc_stack count] == 0
TH_SFLAG_ABORTSAFELY
frontmost
disabled
suspendCount
waitEvent
turnstile blocked on task pid %lld, hops: %d, priority: %d
TH_SFLAG_POLLDEPRESS
<unavailable>     
)#
AirPodsReporting
TH_TERMINATE2
TH_SFLAG_ECORE_ONLY
<NO_NS>
notice
kThreadTriedFaultBT
509
Failed to send message or decode reply: 
mem_regions
%p + %llu
threads
<value>
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
%s: %s: returning.\n
(unknown-reason)
jettisoned
,
lookups
metadata:
notes
 
thermalPressureLevel
 [inlined]
arch
isBeta
ioKitTransport
0x%llx
[kc_stack count]
cpsr
is_non_fatal
Debugger message
panic\\(cpu\\s+\\d+\\s+caller\\s+(0x[0-9A-Fa-f]+)\\)
suspensionProcID
TH_SFLAG_PROMOTED
_dyld_process_info_create(%d) for resampling UUIDs failed with %d
kThreadMain
Thread %d%@:%@%@%@%@
sw_ver
port %#llx owned by pid %llu
busy VM page %#llx
CDStackshotReport.m
ThermalPressureLevelTrapping
 Dispatch queue: 
usage_since_last_crash_user_facing
heap-usage
snapshotFlags
crashlog-version
code
ThermalPressureLevelSleeping
tmp0
rax
ReportViewer
timesDidThrottle
rdx
ACMLib
A2DP
low-private-shared-ratio
value
  Cacheline:
probGuardReport
FWUP
etl_key
\t<==
{%@}
incident_id
ON
memoryPages
, 
<key>
Failed to decode crash report
tasks
timestamp
TRANSPARENCY
PSE
build
continuous
QOS_CLASS_BACKGROUND
crk
Thread %d instruction stream:
requireCrashingThread
iokit
paging/activity for VM object %#llx
suspensionSources
uuidResampling
\\$\\((([^\\)\"]+|\"[^\"]+\")+)\\)
mtePageTags
accessory_pid
 owned by pid %lld
Unable to create VMUSampler for %d
TH_SFLAG_EAGERPREEMPT
kThreadTruncatedBT
size
portlabel_info->portlabel_id == portlabel_id
swapins
user_usec
symbolicated_log
scenario
vid
lr:\\s*(0x[0-9A-Fa-f]+)\\s+fp:
298
eventReason
daemon
container
active
conclave-limit
error
task_threads() for %d failed
sourceLine
298_LOW_PRIORITY
systemDefaultSharedCache
TH_SFLAG_DEPRESS
%@_0x%04X
kernel
tags
pager ready for VM object %#llx
TH_SFLAG_THROTTLED
<item>
memorystatus_control returned unexpected value - %d: %s
audio
decompressions
kThreadTruncKernBT
SELECT COUNT(*) as count, processName \nFROM \"
product
TH_SFLAG_PCORE_ONLY
Length is zero for attribute: 
turnstile has unknown inheritor
Thread %llu has an incorrect exclave frame offset %d
dyldCompactInfoTooBig
QOS_CLASS_USER_INITIATED
CoreDiagnostics.CrashReportBodyBridge
\\bat pc\\s+(0x[0-9A-Fa-f]+)
queue that is suspended
region
time_since_last_transition
sustained-memory-pressure
processUptime
Thread %d name:  %@%@%@
bug_type
wired
Thread %llu has exclave frames but no kernel frames
allowIdleExit
is_simulated
pageFaults
TH_SFLAG_FAILSAFE
symbolLocation
com.apple.corediagnostics.cputrace
sharedRegionSystem
usage_since_last_crash_in_ear
CONNECTION_IN_PROGRESS
inline
waitInfo
dyldCompactInfoFaultedIn
<unprintable>
train
CFBundleShortVersionString
r12
<index>
isSimulated
pageSize
busyBufferCount
TH_TERMINATE
monitoring timed out for service
Unexpected error
date
coalition
-------------------------------------\nTranslated Report (Full Report Below)\n-------------------------------------\n
section-signature
AppleCredentialManager
idle-exit
speculative_count
asi
queryBiomeForCrashes(topN:daysBack:)
csFlags
system_usec
v16@?0@\"NSError\"8
reasons
288
dyldCompactInfoMissing
mach_msg receive on 
%@\t%18p %@
The received pattern info are not valid
Error in pattern matching: (
elapsed time
pthread condvar %#llx
lastMadeRunnableTime
idle
systemTime
Unable to read JSON
core
physicalPages
rsrcFlagged
|
flavor
(unknown-%llu)
QOS_CLASS_UNKNOWN (%u)
\nGROUP BY processName \nORDER BY count DESC \nLIMIT 
CrashReporterKey:
LibCall_ACMKernelControl
groupID
TH_SFLAG_FLOOR_PROMOTED
WATCHDOG
version
platform
SENSOR_PKT_SERVICE
qosOverride
cpu
registers
actions
genCount
inactive_count
%@ (%@)
Failed to connect to listener, error: 
queue processed by thread %llu
LIVE_LISTEN
visible
v8@?0
waitinfos
sampleTruncatedStacks
isImpDonor
Callstack Section
mapping-in-progress for VM object %#llx
jitStartAddress
r
Thread %d crashed with X86 Thread State (64-bit):\n  rax: 0x%016qx  rbx: 0x%016qx  rcx: 0x%016qx  rdx: 0x%016qx\n  rdi: 0x%016qx  rsi: 0x%016qx  rbp: 0x%016qx  rsp: 0x%016qx\n   r8: 0x%016qx   r9: 0x%016qx  r10: 0x%016qx  r11: 0x%016qx\n  r
can_idle_exit
suspensionProcName
analytics_test_mode
port %#llx name %#llx
app_name
index
out-of-slots
slide
Unable to load full report.
panicStringDelimiter
memoryStatus
purgeable_nv
TH_SFLAG_UNKNOWN
age
killDelta
memoryPressureDetails
missing stackshot buffer or size
: 
logwritten
%@%s
CFBundleIdentifier
compressions
largestZoneSize
lifetimeMax
Register Frame Section
Process:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.C
priority
allPids
TH_SFLAG_PRI_UPDATE
below-min-pages
monitoring timed out for service without diags
HS
far
err
legacyInfo
DIAGNOSTIC_PATTERN_MATCHING_PANIC
additionalPayload
ThermalPressureLevelLight
usage_since_last_crash
krwlock %#llx for upgrading
sensors
darwinBG
qosEffective
This is a watchdog-triggered termination event, and not expected to be well-represented in the legacy crash format
route-number
terminatedSnapshot
Unknown KCDATA %X, size %d, flags %X
exception
0x%08x
sharedRegionNone
Failed to set flags for stackshot config
purges
DiagnosticsReporterLaunchOptions
rosetta
&
vmregioninfo
TIPI
%p + %llu%@%@
active_count
pageins
reads
vm-pageshortage
cpuType
309
accessory_os_version
Heap overflow by at least 
donatingPids
schedPriority
resampled %d of %d images missing from %d pids: %@
327
com.apple.Jetsam.Kill
memoryPressure
unindexed_rs_frames
rbx
flags
originalLength
rflags
Done with pattern check
textualRepresentation
298_ALE
idleDelta
csTrustLevel
blocked on %lld, hops: %d, priority: %d
invalid_images
resampledAllImages
variant
JSON schema not understood
NULL
free
resume
absoluteTime
jitEndAddress
TH_WAIT
No payload found on device
crashlogs
ACMKernelControl
genCounter
stacks+%@
xform-full-report
Address Range: [Start, End)
locked 
ThermalPressureLevelModerate
wasUnlockedSinceBoot
timeDelta
uptime
suspended
v20@?0I8r^{stackshot_thread_waitinfo_v2=QQQCsI}12
indicator
Thread %d crashed with ARM Thread State (32-bit):\n    r0: 0x%08x    r1: 0x%08x      r2: 0x%08x      r3: 0x%08x\n    r4: 0x%08x    r5: 0x%08x      r6: 0x%08x      r7: 0x%08x\n    r8: 0x%08x    r9: 0x%08x     r10: 0x%08x     r11: 0x%08x\n   
threadTriggered
developerMode
 in spin mode
r14
308
com.apple.corediagnostics.patternMatched
accessory_crashreporter_key
userTime
kHasDispatchSerial
event_history
LibCall_BuildCommand
low-swap
resampled %d of %d threads with truncated backtraces from %d pids: %@
Unable to find class %s
ARM_THREAD_STATE32
source
stackResampling
%s
%u
name
stackshot_duration_outer_nsec
sharedRegionOther
TABLE_TOP
largestZone
TH_SFLAG_WAITQ_PROMOTED
vmRegionInfo
ale_flag
other
extDarwinBG
\" \nWHERE eventTimestamp >= 
unable to allocate %d bytes for jetsam snapshot
ldm
-[CDStackshotReport decodeKCDataWithBlock:withTuning:usingCatalog:]
BUD_SWAP_IN_PROGRESS
-[NSMutableDictionary(StackshotKCDataExtension) parsePortLabelContainer:]
resampled_images
rcx
neuralPages
proc-thrashing
uuidFaultFlags0x%08llX
OFF
appleIntelligenceStatus
Thread %llu with %lu kernel frames has exclave frames but invalid exclave frame offset of %d. Skipping adding exclave frames into kernel frames 
stringByTrimming
%@: %@
com.apple.corediagnostics.pidselection.retry
panicFramesMatchMode
kernel returned (0) from memorystatus_control(MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT) -- no jetsam data available
alternate
 with unknown owner
passcodeSet
non-parseable kc snapshot buffer
vm-pageout-starvation
unknown type %u (owner %llu, context %#llx)
frontmostPids
SELF != ''
lr
memoryErrorReport
periodic
zone-map-exhaustion
i
paging
Memory Safety Violation (
SPARE_4
compressorSize
vm-compressor-thrashing
paging-in-progress for VM object %#llx
zero_fill_count
stackshot
ThermalPressureLevelHeavy
bytes
Failed to get jetsam status list (query returned %d)
Process %@ is in transition type %@
TH_SFLAG_BOUND_SOFT
mailbox-error
isCorpse
accessory_fusing
kThreadTruncUserBT
connected
):\nFault: Invalid 
is_corpse
Failed to read attribute as string for: 
uncompressed
x86_THREAD_STATE
throttled
suspensionCount
rdi
%-3d %@
Failed to send message or get reply: 
uuid
r11
HFP
SPLITTER
details
basePriority
<exempt>
com.apple.corediagnostics.visualization
Probabilistic Guard Malloc
%@lock %#llx
TH_IDLE
com.apple.CoreDiagnostics
queue thread to be allocated
queue in a transient state
visNonvisible
exceededWQTotalLimit
resampledExtraImages
mailboxes
COUPLED
zoneMapCap
ON_HEAD
termination
task_read_for_pid(%d) for resampling backtraces failed with %d
QOS_CLASS_MAINTENANCE
stackshot inclusion disabled
osVersion.train
Unable to transform log
pattern
mach_msg send on 
taskSpecificSharedCache
share_with_app_devs
runawayMitigation
TH_SFLAG_REEVALUTE_TG_HIERARCHY_LATER
  [%02d] (%@) -> (%@)\t%@
max_pages
priorities
imageOffset
%s RECURSION %u, LEVEL %u
No jetsam status list available (size query returned %d)
NEW_FW_BOOT
procName
\\^\\([^\\)]+\\)
thermalLevel
container && (container.type == STACKSHOT_KCCONTAINER_TASK)
TH_RUN
v24@?0r^v8Q16
r10
PIDSelection.previousProcessName
nearestAllocation
SPARE_1
exclaveScid
metadata
QOS_CLASS_DEFAULT
cacheLine
v32@?0@\"NSTextCheckingResult\"8Q16^B24
init()
<port label truncated>
bootArgs
!
com.apple.ReportSystemMemory
PIDSelection.previousPID
application-info
;
mach_msg receive on %@port set %#llx
keyFrame
unindexed_frames
bootSessionUUID
\n tmp0: 0x%016qx tmp1: 0x%016qx tmp2: 0x%016qx\n
disk-space-shortage
suspensionDuration
TH_SUSP
deployVersion
Thread %d instruction stream (single cacheline):
usedImages
signal
os_version
Failed to send message or get reply:
crashlog
fds
internal
port %#llx owned by kernel
Unmapped pages caused truncated backtrace (resampling disabled)
Missing report body to transform
codeSigningValidationCategory
com.apple.corediagnostics
port %#llx with unknown owner
wire_count
thermalData
cow_faults
id
???
Invalid number of keys found, expected one.
No processes were jettisoned (either killed or suspended)
thread %llu: 
turnstile had unknown status (flags: 0x%llx)!
host_statistics64 failed
%d unindexed re-sampled frames from %d pids: %@
ARM_THREAD_STATE64
Transformation not supported for log type
acm_mem_alloc_info
memorystatus_control(MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT) failed: %s
task_read_for_pid(%d) for resampling UUIDs failed with %d
systemTimeTask
(invalid-reason)
sourceFile
instructionState
foreground
postSampleVMStats
isNonFatal
CoreDiagnostics.CrashPatternInfo
Unknown KCDATA ARRAY type %X, count %d, size %d, flags %llX
continuation
v16@?0@\"NSString\"8
accessory_type
crashTime
pid
queue
ACM
SpringBoard
largestProcess
turnstileInfo
lastRunTime
telemetry_mode
*
lastExceptionBacktrace
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
low-probability-of-use
suspensionLastEnd
Kernel text base
zoneMapSize
tuning
instructionStream
lastBranchState
kThreadUnknown
symbol
path
unknown error
zones
unknown port
pthread mutex %#llx
TH_UNINT
base
this log appears to be from the DA grid, using parsedData section
Not sending Core Analytics events because snapshot is missing.
failed to create registration token for pressure level: %d
failed to get display state: %d
Received response: %s
Unable to find incident in report body
Background system task handler registered, waiting for it to fire
Invoking client callback with PID %d
Failed to send message or decode reply: %@
Background system task handler registration failed
Biome SQL query returned %ld processes: %s
Biome SQL query failed: %@
Generated random number %ld for redaction
Failed to redact frames for lastExceptionBacktrace
Initializing AirPodsCrashReport
Failed to create AirPods crash report
Missing asset for %s in namespace %s
Matched the pattern definition with UUID %s
BackgroundSystemTasks not available on this OS version
No callback registered, cannot deliver PID %d
Invalid bug_type for Jetsam report: %s
Invalid or missing Mailbox log
Invalid or missing Mailbox route number
Invalid or missing Mailbox registers
*** ignoring non-numeric symbolLocation: '%@'
unsupported log type '%@' effective (%@)
look for known pattern other error: %@
Failed to encode JSON: %@
RTBuddyCrashlogDecode not available
Skipping final frame with LR 0x%s not in kext/kernel range
Failed to create symbolicator
Exclave frames offset of %d for thread %llu is invalid
isProcessAlive(%d) -> %s
Top crashing process list from Biome: %s
Size section not available to decode MTBF
%s: %s: called.\n
OSADiagnosticsReporter or DiagnosticsReporterLaunchOptions class not available
Invalid size and offset for Csif
Invalid MTBF section offset and size
Unknown KCDATA CONTAINER %X
Panic matcher could not be initialized
Callback completed, success=%s
Failed to get proc_name for pid %d
Crash report missing thread data
Error: RTBuddyCrashlogDecode returned nil
Offset section not available to decode MTBF
Error connecting to remote object: %@
Submitting background task: %@
Size section not available to decode Csif
Cannot retrieve file size for %{public}s: %@
Failed to create regex
AnalyticsQueryValuesFor timed out after 10s; clearing AI state
unable to allocate %d bytes for wired memory info
failed to get pressure level state: %d
Error fetching TRM status: %i
Failed to connect to listener, error: %@
Value '%s' not found: %s\nCoding Path: %s
Offset section not available to decode Csif
Failed to retrieve base address from raw buffer binary
Scenario information with range %u indicates trailer present but not enough space in section size %ld
Error decoding payload: %@
Thread has backtrace with unexpected type
Invalid or no section name/signature found
Unable to represent visibility endowments as a set as PIDs: %s
GM availability string not found
%s: %s: returning, err = %ld, code=%u.\n
Failed to create UserDefaults for suite: %s. Falling back to standard
Payload %ld: %s
Scenario information range %u too large for section size %ld
%@
Error loading full report: %{public}@
Unable to find date in report body
Failed to convert to body to json
Got no value from SecureConfig for crashRedactionEnabled, returning false
Scenario information range %u and trailer length %hu too large for section size %ld
found at pc match: %s
Expected a task specific shared cache with ID %{public}@ but none was found
%s fired
All %ld processes checked, none running
Crash frame has valid image index, but image missing source name
Failed to create OSALog file: %@
Failed to parse heap usage from section contents: %s
Invalid or missing Mailbox error
Error retrieving file CreationDate: %@
Unable to convert report body to JSON for file %s
There are no crash payloads available
The panic reason string does not match, skip this pattern
No ExcResource reports found
AnalyticsQueryValuesFor returned non-dictionary result
%s: %s: cmd(%u) on CS[%u] -> ok.\n
Failed to redact frames for normal thread
Scenario information trailer length too small %hu < %ld
Report has missing or malformed exception codes.
memorystatus_control for command %d returned %d - No data available
Unable to parse report for file %s
Successfully parsed payload for %s in namespace %s as type %s. Count = %ld
Key '%s' not found: %s\nCoding Path: %s
Unexpected type for exception backtrace
Signature mismatch for section %s. Found: %s, expected: %s
Unable to determine malloc size class for empty MTE tags
look for known pattern error: %s
panic string matched: %s
Crash frame missing image index
Failed to launch DR with error: %@
Background task %s already exists (interval: %fs), skipping submission
Using custom process list (%ld processes): %s
Failed to calculate start date for biome query
Binary not available to decode MTBF
MTBF section too small to decode: (%ld < %ld)
Unable to represent audio assertions as a set as PIDs: %s
memorystatus_control for command %d failed with error %d
Type '%s' mismatch: %s\nCoding Path: %s
Found PID %d for process %s
Invalid bug_type for crash report: %s
Invalid scenarioType %hhu
Cannot retrieve creationDateKey for file %s
Failed to look for pattern %@
Biome query timed out after %f seconds
BiomeStreams (BMSQLDatabase) not available on platform
create a regex %s
SecureConfig error for crashRedactionEnabled, defaulting to true: %@
Unable to retrieve extended attribute \"bug_type\" for file %s with Error: %@
Unable to extract report body for file %s
BGRepeatingSystemTaskRequest not available
Frame %ld (non-final): LR 0x%s not in any kext/kernel range - backtrace corrupted
Failed to get reasons array
Unable to serialize report body as JSON: %@
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
memorystatus_control for command %d returned unexpected valud of %d which does not match buffer size of %d
ips metadata not detected (%ld bytes before newline), attempting to read entire file as payload
PID %d still running as '%s', skipping selection
Process '%s' is running (PID %d)
failed to create registration token for display state: %d
Unknown panicFramesMatchMode: %s
Report timestamp could not be parsed; defaulting to full redaction
Processing binary for core: %s
Process %{public}@ [%d] killed by jetsam reason %{public}@
DiagnosticsReporterServices.framework is unavailable
No processes available, will retry next interval
Crash redaction is disabled
crashRedactionEnabled: found value of %{public}s from Secure Config
synthesizing %d items from payload as metadata
%s
Pattern %s has multiple donation types (%ld)
Error: expecting max of %ld reports per hour, but found %ld
Unable to parse RTBuddy crash log dictionary
Binary not available to decode Csif
key %s -> %s
Unable to find panicString in report body
Missing level for %s in namespace %s
Callback failed, will retry next interval
Crash report frames have unexpected type
MTBF section too small to decode beyond usage_time_btw_crashes: (%ld < %ld)
Expected a task specific shared cache with id %@ but none was found
Unable to parse payload for %s in namespace %s as type %s
Selected PID %d (%s)
Failed to decode as CrashReportBody: %@
Unable to retrieve extended attribute %s for file %s with Error: %@
failed task_read_for_pid with %d
Failed to send message: %@
There is no panic payload available
Unable to determine malloc size class for uniform MTE tags
found panic caller: %s
%s: %s: returning, err = %ld.\n
failed to create VMUProcInfo
there is no available matcher with type %u
Conflicting donation types found: %u vs %u
Found donation type %u with UUID: %s
Failed to read payload at %s
Using Trial payload at %s for %s in namespace %s
Failed to submit background task: %@
lastProvidedPID: %s, processName: %s
Trial is not available
```
