# `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 250,048 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 36 (Size: 5416)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (19)

- `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary (compatibility version 1.0.0, current version 441.26.3, weak)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics (compatibility version 0.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (8 classes, 2 protocols)

Classes: `EmbeddedPanicDataDecoder`, `EmbeddedPanicDataDecoderV5`, `EmbeddedPanicDataDecoderV6`, `EmbeddedPanicDataDecoderV7`, `EmbeddedPanicDataDecoderV8`, `EmbeddedPanicDataDecoderV9`, `PanicReport`, `_TtC22PanicProcessingSupport23PanicProcessingInternal`

Protocols: `NSObject`, `PanicProcessingDelegate`

## Strings (721)

```
PanicReport
PanicProcessingDelegate
PanicProcessingSupport
EmbeddedPanicDataDecoder
EmbeddedPanicDataDecoderV6
EmbeddedPanicDataDecoderV7
EmbeddedPanicDataDecoderV9
_TtC22PanicProcessingSupport23PanicProcessingInternal
NSObject
EmbeddedPanicDataDecoderV5
EmbeddedPanicDataDecoderV8
_logger
release
reportUsedImages
ss_sequence
unsignedIntValue
useSocdContainer:
T@\"NSString\",R,C
_buildVersion
_uuidKernelCache
rootsInstalled
_panicInitiator
_patternType
_socId
extractRemoteProperties
hash
initWithPattern:options:error:
panicInitiator
socRev
setAppleCareDetails:
setBiomeProperties:
uniqueChipID
unsignedLongLongValue
T@\"<PanicProcessingDelegate>\",&,N,V_delegate
timeSecs
_delegate
_foregroundAppHash
initWithBytesNoCopy:length:encoding:freeWhenDone:
panicString
validatePanicLogBounds
dealloc
utilizationInfo
mutableCopy
rangeAtIndex:
setPanicTimeInSecs:andUsecs:
setUtilizationInfo:
TI,R,N,V_socId
_panicProcessingFlags
autorelease
initWithData:encoding:
kernReturnToString:
numberWithInt:
setNotes:
setObject:forKey:
_uuidIBoot1
dumpHexToString:size:
setPanicString:
numberWithUnsignedLongLong:
stringByAppendingString:
useStoragePanicData:
T@\"NSString\",R,N,V_panicInitiator
_bootStage
_otherString
_safeToParseStackshot
description
extractPanicString
isTagCheckFault:
setSOCId:AndRev:
isResearchFused
_ephVersion
_patternUUID
otherString
panicBuffer
panicLength
sendEvent:
setSocDataVersion:
setKernelVersion:
_planeMetadata
_product
dataWithBytes:length:
getHeaderVersion
setValue:forKey:
_timeUsecs
TI,R,N,V_socRev
T@\"NSMutableDictionary\",&,N,V_utilizationInfo
_utilizationInfo
_uuidTXM
isEqual:
setOriginalPanicReportPath:
subdataWithRange:
initWithPanicString:otherString:buildVersion:panicFlags:panicType:incidentID:rootsInstalled:
T@\"NSMutableArray\",&,N,V_notes
_uuidSPTM
appendFormat:
appendNotesTo:
deviceModelType
T@\"NSString\",R,N,V_panicProcessingInfo
crashReporterKey
extractUniqueDeviceProperties
kernelVersionDescription
reportNamePrefix
safeToParseStackshot
T^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}},R,N,V_panicInfo
_deviceModelType
donateToBiome
getStatus
socId
addEntriesFromDictionary:
null
numberWithDouble:
setUUIDKernel:
useExtPaniclog:
parseExtPaniclog
respondsToSelector:
setUUIDTXM:
getHeaderLength
_panicBuffer
_panicInfo
mountVolumeWithRole:mountPath:
stringWithFormat:
useSocdNandContainer:
setPatternUUID:
_timeInSecsAndUsecs
bootProgressRegister
count
isEqualToString:
generateLogAtLevel:withBlock:
name
numberOfRanges
patternTypeString
setObject:forKeyedSubscript:
UTF8String
_isBtnReset
decode
dictionaryWithObjects:forKeys:count:
T@\"NSError\",R,N,V_error
additionalIPSMetadata
extractBasicInfo
setUUIDKernelCache:
createUUIDString:
setIncidentID:
zone
T@\"NSString\",?,R,C
objectAtIndex:
sharedInstance
T@\"NSString\",R,N,V_deviceTargetType
numberWithUnsignedInt:
updateUtilizationInfo:
T#,R
UUIDString
_biomeProperties
_extPaniclog
_macosBuildVersion
dictionaryWithObject:forKey:
removeObjectForKey:
setBoardId:AndRevId:
T@\"NSString\",R,N,V_buildVersion
T@\"NSString\",R,N,V_bootsessionuuid
T@\"NSString\",R,N,V_otherString
Tr*,R,N,V_panicBuffer
_uuidIBoot2
performSelector:withObject:withObject:
platformECID
useCrashlogContainers:
stringByAppendingFormat:
_foregroundAppHashSet
delegate
setPanicProcessingFlags:
setRawPanicData:
_socdNandContainer
appendString:
stringValue
TB,R,N,V_safeToParseStackshot
isInLDM
T@\"NSString\",R,N,V_plainPanicData
extractOtherString
objectForKey:
retain
_boardId
_timeSecs
copy
dataWithBytesNoCopy:length:freeWhenDone:
writePanicReportBodyWithSectionWriter:
dictionaryWithObjectsAndKeys:
extractPanicInfoTracker
init
macosBuildVersion
objectForKeyedSubscript:
testPlanID
_rootsInstalled
bootsessionuuid
TQ,R,N,V_rootsInstalled
_isInterruptedCoredump
deleteBootArgDumppanic
initWithPanicInfo:panicBuffer:panicLength:
isSecurityResearchDeviceERM
setPanicProcessingInfo:
_boardRevisionId
_rawPanicData
error
extractPanicInitiator
getAuxiliaryNVRAMData
getSterilizedStringFromData:size:
panicProcessingInfo
reason
_platformECID
buildVersion
countByEnumeratingWithState:objects:count:
T@\"NSData\",R,N,V_extPaniclog
__swift_setObject:forKeyedSubscript:
deviceTargetType
getBuildVersionString
panicTimingToString:
problemType
initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:
numberWithUnsignedLong:
performSelector:
_awlBuildVersion
_panicString
addObject:
setEPHVersion:
setplatformECID:
Diagnostics
createWithPanicBuffer:panicLength:
panicMedicTelemetry
self
source
stringFromDate:
setDelegate:
T@\"NSString\",R,N,V_product
_notes
_socdContainerArray
isDevFused
numberWithUnsignedChar:
TQ,R,N,V_timeUsecs
initWithCaptureTime:incidentID:patternUUID:patternType:
objectAtIndexedSubscript:
setProduct:
_panicLength
_panicProcessingInfo
_uuidKernel
initWithBase64EncodedString:options:
_socRev
TQ,R,N,V_platformECID
notes
productNameVersionBuildString
_isMTEPanic
extractExtPaniclog
isKindOfClass:
length
modelCode
panicInfo
initWithUUIDBytes:
isIntentionalPanic
kernelVersion
performSelector:withObject:
T@\"NSString\",R,N,V_panicString
T@\"_TtC22PanicProcessingSupport23PanicProcessingInternal\",N,R
codeSigningMonitor
errorWithDomain:code:userInfo:
setBootStage:
_appleCareDetails
_bootsessionuuid
panicFlags
setPanicInitiator:
TQ,R,N,V_panicLength
_panicFlags
_storagePanicData
appleCareDetails
generatePanicSaveOptionsForDirectory:time:prefix:
isProxy
_kernelVersion
setPlaneMetadata:
timeUsecs
product
_deviceTargetType
decodeKCDataWithBlock:withTuning:usingCatalog:
isMemberOfClass:
macosSystemState
plainPanicData
setUUIDSPTM:
substringWithRange:
_socDataVersion
T@\"NSString\",R,N,V_macosBuildVersion
TQ,R,N,V_panicFlags
conformsToProtocol:
isTestAutomationDevice
matchesInString:options:range:
numberWithUnsignedShort:
setDateFormat:
isDeveloperMode
T@\"NSString\",R,N,V_deviceModelType
_plainPanicData
getValueFromDTForNode:key:
processExtPaniclogFlags:data_id:data:additionalBuffers:addToExtPaniclog:
productName
retainCount
base64EncodedStringWithOptions:
TQ,R,N,V_timeSecs
debugDescription
incidentID
setForegroundAppHash:
setUUIDIBoot1:AndIBoot2:
shared
superclass
T@\"NSString\",R,N,V_kernelVersion
$__lazy_storage_$__logger
_macosSystemState
bootIsRecoveryEnvironment
bytes
class
getStackshotData
initWithUnsignedInt:
.cxx_destruct
Panic
T@\"NSString\",R,N,V_macosSystemState
setPatternType:
TQ,R
_crashlogContainerArray
_error
setAWLBuildVersion:
extPaniclog
@40@0:8:16@24@32
@40@0:8^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}}16r*24Q32
@32@0:8r*16Q24
Vv16@0:8
v24@0:8@16
r*16@0:8
@\"NSData\"
v20@0:8I16
@\"NSNumber\"
@40@0:8@16d24@32
B28@0:8I16^@20
B16@0:8
^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}}16@0:8
I
Q
@\"NSMutableDictionary\"
B24@0:8@16
@24@0:8:16
^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}}
r*
v24@0:8C16C20
C
v24@0:8@?16
@72@0:8@16@24@32Q40@48@56@64
@\"NSDictionary\"
B24@0:8@\"NSString\"16
B24@0:8#16
v24@0:8@\"NSString\"16
B24@0:8:16
I16@0:8
@\"NSMutableArray\"
@20@0:8i16
@16@0:8
^{_NSZone=}16@0:8
@\"<PanicProcessingDelegate>\"
v32@0:8Q16Q24
@20@0:8I16
@32@0:8:16@24
@\"NSString\"
v16@0:8
@\"NSError\"
@\"NSArray\"
@\"NSMutableDictionary\"40@0:8@\"NSURL\"16d24@\"NSString\"32
@32@0:8^v16Q24
B
#16@0:8
v24@0:8I16I20
v20@0:8C16
v32@0:8@16@24
Q16@0:8
@32@0:8@16@24
@\"NSString\"16@0:8
@\"NSArray\"16@0:8
@\"NSString\"28@0:8r*16I24
v24@0:8Q16
v52@0:8I16@20@28@36^B44
v28@0:8B16@?20
@\"NSNumber\"32@0:8@\"NSString\"16@\"NSString\"24
@28@0:8r*16I24
B24@0:8@\"Protocol\"16
Already in set
Memory data moved
Lock owned
panic_ts
boardId
Invalid task
RPC terminate orphan
Invalid argument
Invalid status 0x%x
Lock set destroyed
Invalid guard object slot
panicTimeInSecsAndUsecs
binaryImages
notes
Truncated panic string to 0x%x bytes, and dump it in rawPanicData (ignoring other log)
Name exists
Right exists
Lock owned by self
chip-id
kernel
uuidIBoot1
repairStatus
Policy static
Missing KC
outCmd
product
Already waiting
Not supported
panicProcessingInfo
uuidIBoot2
outReportErr
PS_ENABLE_BORA_LOCAL_PASSTHROUGH_STREAMS
PS_INTERNAL_ANALYTICS_COMMAND
DecodedData
Not waiting
[Error: Invalid timing offset at entry %u]; 
%llx
PS_TEST_TRANSITION_2
ED96D2EC-F22F-05F4-F3E2-5DDEC8CA9031
Memory failure
Memory error
User references overflow
co-processor name: %@, status: %@; 
IODeviceTree:/chosen
clientPID
69D10244-4BCE-43C2-9D27-42499B943EBF
Invalid ledger
nested panic occurred
developerMode
bootProgressRegister
uuidKernel
yyyy-MM-dd-HHmmss
kern.roots_installed
interrupted_coredump
hw.osenvironment
Debugger lock acquired
panic
source
PS_TEST_TRANSITION
Parsed empty panic string from panic log buffer even though expected non-zero length: eph_panic_log_len %u eph_panic_log_offset %u embedded_panic_length %lu
Aborted
Invalid processor set
Code signature error
PS_SELECT_GFX_CONTAINER_DIM_A
Denied
Not found
extPaniclogData
410
plane_node
<mysterious>
interfaceID
lastPktType
PanicLogLengthInBytes
kernelVersion
Invalid security
Node down
%.16s
prevSMName
Panic log creation started
Coredump completed
Failure
[Error: Coprocessor array out of bounds]
Invalid timing %d
uuidKernelCache
socRevision
interrupted coredump panic
os_version
rawPanicData
development-cert
nextSMName
fallback_latency
PS_SWITCH_TO_UNPROTECTED_SURFACES
RPC continue orphan
i
ldm
customerFused
uuidResampling
PS_ENABLE_VR_STREAMS
Panic info created
-%@
CrashlogContainers
intentional panic
kern.bootargs
inCmd
outReport
PS_ENABLE_MR_STREAMS
PS_TRANSITION_TO_100_FPS
%@ %@
Prefix of panic string dumped as hex: %@
%@
CrashlogContainer
PS_TRANSITION_SLEEP
Coredump generation started
Kernel coredump finished
-base+socd
Implausible embedded panic header version: %d
Invalid name
Lock unstable
[Error: Invalid name at entry %u]; 
Data
embedded panic data was failed to be parsed from panic buffer, check notes for more details
Invalid object
Operation timed out
ED96D2EC-F22F-05F4-F3E2-5DDEC8CA9030
Embedded panic header contains invalid magic, expected 0x%x found 0x%x
Cores halted
Resource shortage
(timing: %@, timestamp: %llu) 
ExtensiblePaniclog
Embedded panic log header contained bad magic
UsedSizeInBytes
Success
Invalid right
string
kOSALogOptionOverridePath
BE94D68E-486C-475D-800E-37C151D4869A
Userspace coredumps finished
Panic Timing info: 
incident
boardRevisionId
uuidSPTM
allPids
inResp
Exception protected
%02hhx%02hhx
chosen
%x
SOCDNandContainer
SOCDContainers
PS_ENABLE_PANIC_PASSTHROUGH
PS_TRANSITION_WAKE
com.apple.PanicProcessingSupport.EmbeddedPanicDataDecoder
Data ID
Invalid policy
SOCDPanicString
com.apple.dumppanic
deviceModelType
Coprocessor coredumps finished
Invalid capability
Memory restart copy
Invalid KC
RPC server terminated
%llu
com.apple.DumpPanic
Invalid embedded panic header magic
type
Protection failure
outRespErr
outCmdErr
embedded-panic-log-size
timeUsecs
inReport
PS_ENABLE_SECONDARY_STREAMS
chip-revision
panicProcessingFlags
embeddedPanicHeaderVersion
PS_DISABLE_DISPLAY_WRITE_BACK_STREAM
      , Panic co-processors info: 
PanicLogUtilizationMetrics
performed
panicFlags
socDataVersion
ECID
PercentUsed
Invalid value
com.apple.stability.panic
0x%llx
otherString
timeSecs
lastPktTimestamp
[No timing entries found]
210
BATS_TESTPLAN_ID
panicInitiator
-full
Stackshot collection finished
Not depressed
(timing: Unknown(%d), timestamp: %llu) 
-base+storage_crash
build
kOSALogOptionFilenamePrefix
Truncated panic string from 0x%x to 0x%x bytes (ignoring other log)
OtherLogLengthInBytes
PanicMedicReports
eventName
Memory present
forceReset
uuidTXM
truncated other string
-base
%@%@
sroute_id
Debug IPI sent
Unknown status %d
PanicGenerated
patternUUIDs
Embedded panic log header contains invalid panic log offset
Stackshot collection started
Default set
@\"NSDictionary\"8@?0
arm-io
StackshotLengthInBytes
Insufficient buffer size
platformSOCDBuffer
=(0x[a-fA-F0-9]+|[0-9]+)(?:[ \\t\\r\\n]|$)
smStatus
inRespErr
socId
Terminated
tExecute
deviceTargetType
151
nodeName
Invalid address
additionalData
storagePanicData
Debug Testing
socRev
Secure kernel coredump finished
roots_installed
foregroundAppHash
tAction
Policy limit
PS_ENABLE_DISPLAY_WRITE_BACK_STREAM
Embedded panic header doesn't contain valid panic log: eph_panic_log_len %u eph_panic_log_offset %u embedded_panic_length %lu
SOCDContainer
PS_SWITCH_TO_PROTECTED_SURFACES
No access
Not in set
codeSigningMonitor
PS_DISABLE_ALL_STREAMS
v8@?0
panicString
outResp
Expected 0x%x but found 0x%x
Invalid host
Semaphore destroyed
test automation device
No space
Invalid memory control
plane_supervisor
date
test plan id: %llu
PS_ENABLE_MR_NO_MATTING_STREAMS
PS_TRANSITION_TO_96_FPS
wall %llu s %llu us
crashReporterKey
stackResampling
PS_DISABLE_SECONDARY_STREAMS
platformECID
com.apple.PanicProcessingSupport
default
com.apple.coreOS.forceReset
fallback_started
PS_TRANSITION_TO_90_FPS
PanicRegionSizeInBytes
extPaniclog
bootStage
kOSALogOptionFilenameTimestamp
Not receiver
No timing entries recorded (offset is 0)
%@
unique device properties extracted - device target type: %@, device model type: %@
WARNING: unable to calculate panic region utilization
invalid eph_stackshot_offset %u, eph_stackshot_len %u
found other log with %u bytes
truncating eph_other_log_offset %u, eph_other_log_len %u
found ext paniclog with %u bytes
Could not get panic initiator data
Panic info timing first entry offset %u
Invalid panic info tracker timing offset %u (length: %zu)
Coprocessor name not null-terminated at entry %u
setOriginalPanicReportPath: %s
The panic info tracker magic invalid: found 0x%x, expected 0x%x
no 'other' log found in embedded panic log
invalid eph_panic_log_len %u eph_panic_log_offset %u, embedded_panic_length %lu, header length %u
Panic Initiator offset %u Length %u
failed to delete dumppanic in boot-args
Coprocessor array extends beyond panic buffer: offset %u, count %u, size %zu, buffer length %zu
Unable to create UUID object
Invalid version. Version in paniclog: %d\n
invalid panic initiator eph_panic_initiator_len %u eph_panic_initiator_offset %u,
invalid eph_panic_log_len %u eph_other_log_offset %u,
Extracting remote properties: SoC ID, SoC Rev, Product, Kernel Version, Platform ECID, Time
Data len is invalid: %d
Extensible Paniclog offset %u Length %u
remote properties extracted - SoC ID: %x, SoC Rev: %x, Product: %@, Kernel Version: %@, Platform ECID: 0x%llx, Time: %llu s %06llu us
Unable to create Data ID and Data dict
Could not create ext paniclog data
Did not find valid panic info coprocessor entries (count is 0).
deleteBootArgDumppanic: no-op in default implementation
invalid panic info tracker coprocessor offset %u (length: %zu)
Unable to create Buffer data string
invalid eph_magic 0x%08X
invalid extensible paniclog eph_ext_paniclog_len %u eph_ext_paniclog_offset %u,
found panic info coprocessor array
Invalid no_of_logs %d
*** %lu ***
(embedded) length: %zu eph: magic %08X vers %u flags 0x%016llX panic_log offset %u, len %u, other_log offset %u, len %u, osversion: %@, macosversion: %@, bootsessionuuid: %@, roots_installed: %lld
truncating eph_panic_log_offset %u, eph_panic_log_len %u (ignoring other log)
Panic info tracker processing
The co-processor name: %@, status: %@ at index %d
Panic info coprocessor first entry offset %u, count %u
Unable to create UUID String
Reason: %@
found panic initiator with %u bytes
Unable to create Data ID String
donate panic with pattern uuid %@ type %@
found embedded panic log with %u bytes
Did not find a valid ext paniclog. Found with length: %d
Invalid timing entry offset %u at entry %u
*** esrString %s ***
rejecting implausible buffer!
Unknown embedded panic header version: %d
Did not find a valid panic initiator. Found with length: %d
Unable to create array
*** isTagCheckFault ***
embedded panic string decoded: %@
Extracting unique device properties: device target type, device model type
```
