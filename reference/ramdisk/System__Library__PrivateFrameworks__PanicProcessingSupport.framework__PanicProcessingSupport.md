# `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport`

From the upgrade restore ramdisk (141-29011-104.dmg). 250,048 bytes.

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
initWithBytesNoCopy:length:encoding:freeWhenDone:
ss_sequence
updateUtilizationInfo:
product
dealloc
isMemberOfClass:
retain
_socRev
class
dictionaryWithObjects:forKeys:count:
rangeAtIndex:
setSOCId:AndRev:
useExtPaniclog:
_isInterruptedCoredump
_macosBuildVersion
error
getStackshotData
getValueFromDTForNode:key:
setUUIDTXM:
socRev
T@\"NSString\",R,C
_uuidIBoot2
dataWithBytesNoCopy:length:freeWhenDone:
getStatus
subdataWithRange:
T@\"NSString\",R,N,V_kernelVersion
_safeToParseStackshot
sendEvent:
setIncidentID:
setPlaneMetadata:
shared
_uuidIBoot1
appleCareDetails
crashReporterKey
setObject:forKey:
_panicLength
bootIsRecoveryEnvironment
_boardId
_error
_panicFlags
extractBasicInfo
macosSystemState
setAWLBuildVersion:
setPanicInitiator:
source
conformsToProtocol:
getBuildVersionString
reportUsedImages
validatePanicLogBounds
isTestAutomationDevice
performSelector:withObject:withObject:
setAppleCareDetails:
testPlanID
TQ,R,N,V_panicFlags
countByEnumeratingWithState:objects:count:
getSterilizedStringFromData:size:
self
stringWithFormat:
_rootsInstalled
_uuidTXM
addEntriesFromDictionary:
initWithPanicInfo:panicBuffer:panicLength:
respondsToSelector:
substringWithRange:
T@\"NSError\",R,N,V_error
T@\"NSString\",R,N,V_panicInitiator
_uuidKernelCache
dumpHexToString:size:
getHeaderVersion
hash
init
isProxy
isInLDM
_timeInSecsAndUsecs
debugDescription
decode
dictionaryWithObjectsAndKeys:
initWithBase64EncodedString:options:
performSelector:
setSocDataVersion:
_kernelVersion
_notes
_product
unsignedIntValue
useSocdContainer:
useStoragePanicData:
T@\"NSMutableDictionary\",&,N,V_utilizationInfo
_timeSecs
createWithPanicBuffer:panicLength:
panicLength
stringValue
uniqueChipID
T@\"NSString\",?,R,C
numberWithUnsignedShort:
panicFlags
reportNamePrefix
timeUsecs
T@\"NSString\",R,N,V_panicString
TB,R,N,V_safeToParseStackshot
dataWithBytes:length:
extractRemoteProperties
objectForKey:
panicBuffer
.cxx_destruct
zone
_extPaniclog
isEqual:
length
productNameVersionBuildString
setProduct:
TQ,R
T@\"NSString\",R,N,V_panicProcessingInfo
T@\"_TtC22PanicProcessingSupport23PanicProcessingInternal\",N,R
delegate
kernReturnToString:
Panic
_socDataVersion
appendNotesTo:
numberWithUnsignedLongLong:
_logger
_deviceTargetType
panicMedicTelemetry
setNotes:
setValue:forKey:
_deviceModelType
_patternType
_timeUsecs
initWithUUIDBytes:
panicString
T@\"NSString\",R,N,V_bootsessionuuid
_awlBuildVersion
deleteBootArgDumppanic
initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:
initWithPattern:options:error:
objectAtIndexedSubscript:
panicProcessingInfo
setUUIDKernel:
T^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}},R,N,V_panicInfo
_buildVersion
_isMTEPanic
_panicProcessingFlags
additionalIPSMetadata
buildVersion
generatePanicSaveOptionsForDirectory:time:prefix:
objectForKeyedSubscript:
_uuidKernel
bootProgressRegister
initWithPanicString:otherString:buildVersion:panicFlags:panicType:incidentID:rootsInstalled:
reason
setBootStage:
setPanicTimeInSecs:andUsecs:
stringByAppendingFormat:
_panicInfo
bytes
extractOtherString
kernelVersionDescription
numberWithInt:
setObject:forKeyedSubscript:
_plainPanicData
T@\"NSString\",R,N,V_macosBuildVersion
productName
$__lazy_storage_$__logger
_foregroundAppHash
_platformECID
decodeKCDataWithBlock:withTuning:usingCatalog:
extractPanicInitiator
mutableCopy
retainCount
T@\"NSString\",R,N,V_buildVersion
matchesInString:options:range:
numberWithUnsignedChar:
setDelegate:
T@\"NSString\",R,N,V_product
_socId
setPanicProcessingFlags:
TI,R,N,V_socRev
setPatternType:
_bootsessionuuid
processExtPaniclogFlags:data_id:data:additionalBuffers:addToExtPaniclog:
setDateFormat:
setUUIDKernelCache:
TQ,R,N,V_panicLength
_otherString
extractExtPaniclog
notes
problemType
setBoardId:AndRevId:
setKernelVersion:
stringByAppendingString:
T@\"NSString\",R,N,V_macosSystemState
_macosSystemState
initWithUnsignedInt:
release
incidentID
plainPanicData
T@\"NSString\",R,N,V_deviceTargetType
__swift_setObject:forKeyedSubscript:
_panicBuffer
numberOfRanges
numberWithUnsignedLong:
count
extPaniclog
setUtilizationInfo:
_bootStage
_utilizationInfo
createUUIDString:
extractUniqueDeviceProperties
isKindOfClass:
objectAtIndex:
setUUIDSPTM:
isResearchFused
Tr*,R,N,V_panicBuffer
_panicString
mountVolumeWithRole:mountPath:
otherString
setBiomeProperties:
setPanicProcessingInfo:
useSocdNandContainer:
deviceModelType
T@\"NSString\",R,N,V_plainPanicData
TI,R,N,V_socId
_biomeProperties
initWithCaptureTime:incidentID:patternUUID:patternType:
initWithData:encoding:
panicTimingToString:
unsignedLongLongValue
_socdNandContainer
codeSigningMonitor
numberWithUnsignedInt:
_foregroundAppHashSet
addObject:
_delegate
_storagePanicData
modelCode
parseExtPaniclog
platformECID
setRawPanicData:
_crashlogContainerArray
generateLogAtLevel:withBlock:
isIntentionalPanic
macosBuildVersion
setUUIDIBoot1:AndIBoot2:
useCrashlogContainers:
T#,R
TQ,R,N,V_platformECID
_panicProcessingInfo
kernelVersion
rootsInstalled
setplatformECID:
errorWithDomain:code:userInfo:
null
sharedInstance
_panicInitiator
T@\"NSMutableArray\",&,N,V_notes
isTagCheckFault:
stringFromDate:
_isBtnReset
bootsessionuuid
deviceTargetType
Diagnostics
_ephVersion
isDevFused
removeObjectForKey:
safeToParseStackshot
setOriginalPanicReportPath:
TQ,R,N,V_timeSecs
TQ,R,N,V_timeUsecs
UTF8String
_patternUUID
_rawPanicData
panicInfo
T@\"<PanicProcessingDelegate>\",&,N,V_delegate
T@\"NSString\",R,N,V_otherString
_boardRevisionId
_planeMetadata
isEqualToString:
numberWithDouble:
panicInitiator
extractPanicInfoTracker
performSelector:withObject:
setForegroundAppHash:
superclass
setPatternUUID:
utilizationInfo
_socdContainerArray
appendFormat:
setEPHVersion:
timeSecs
_appleCareDetails
autorelease
copy
extractPanicString
patternTypeString
T@\"NSData\",R,N,V_extPaniclog
dictionaryWithObject:forKey:
appendString:
socId
donateToBiome
getAuxiliaryNVRAMData
writePanicReportBodyWithSectionWriter:
TQ,R,N,V_rootsInstalled
UUIDString
isSecurityResearchDeviceERM
name
setPanicString:
base64EncodedStringWithOptions:
getHeaderLength
_uuidSPTM
description
isDeveloperMode
T@\"NSString\",R,N,V_deviceModelType
@\"NSData\"
@20@0:8I16
@40@0:8@16d24@32
^{_NSZone=}16@0:8
@\"NSMutableDictionary\"
v20@0:8C16
v24@0:8Q16
v20@0:8I16
@28@0:8r*16I24
B24@0:8#16
@72@0:8@16@24@32Q40@48@56@64
v32@0:8@16@24
@\"NSArray\"
@24@0:8:16
@\"NSMutableArray\"
@32@0:8@16@24
B28@0:8I16^@20
B24@0:8@\"NSString\"16
B24@0:8:16
v32@0:8Q16Q24
@32@0:8r*16Q24
@\"NSString\"28@0:8r*16I24
@\"NSDictionary\"
Q16@0:8
@\"NSNumber\"32@0:8@\"NSString\"16@\"NSString\"24
B
Q
@\"NSError\"
@32@0:8^v16Q24
B24@0:8@\"Protocol\"16
v24@0:8C16C20
@\"NSString\"16@0:8
^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}}
v24@0:8@\"NSString\"16
v16@0:8
C
@20@0:8i16
v24@0:8@16
r*16@0:8
@\"NSNumber\"
v24@0:8I16I20
@\"NSMutableDictionary\"40@0:8@\"NSURL\"16d24@\"NSString\"32
@\"NSString\"
@\"NSArray\"16@0:8
@40@0:8^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}}16r*24Q32
^{embedded_panic_header=IIIQIIIIII(?={?=b8b8b8b40}Q)[32c][32c][37c]QIIIIII[32c][512c]QQQ[16c][32c]{?=IIII}}16@0:8
@\"<PanicProcessingDelegate>\"
v28@0:8B16@?20
#16@0:8
v24@0:8@?16
v52@0:8I16@20@28@36^B44
I
r*
I16@0:8
B16@0:8
@16@0:8
B24@0:8@16
@32@0:8:16@24
@40@0:8:16@24@32
Vv16@0:8
Policy limit
Not waiting
PS_ENABLE_BORA_LOCAL_PASSTHROUGH_STREAMS
%@ %@
panicInitiator
Stackshot collection finished
Not found
foregroundAppHash
bootStage
PS_TRANSITION_TO_100_FPS
Memory failure
chip-id
kOSALogOptionFilenamePrefix
PercentUsed
Kernel coredump finished
RPC server terminated
[Error: Coprocessor array out of bounds]
<mysterious>
69D10244-4BCE-43C2-9D27-42499B943EBF
BE94D68E-486C-475D-800E-37C151D4869A
Prefix of panic string dumped as hex: %@
kOSALogOptionOverridePath
PS_ENABLE_PANIC_PASSTHROUGH
Data
-full
socRevision
interrupted_coredump
nested panic occurred
Debug Testing
BATS_TESTPLAN_ID
Name exists
Operation timed out
Invalid guard object slot
com.apple.coreOS.forceReset
Implausible embedded panic header version: %d
No access
uuidIBoot2
@\"NSDictionary\"8@?0
410
binaryImages
DecodedData
Embedded panic log header contained bad magic
kern.roots_installed
plane_node
embeddedPanicHeaderVersion
uuidKernel
test automation device
Invalid name
Invalid task
eventName
embedded panic data was failed to be parsed from panic buffer, check notes for more details
chosen
Already in set
Aborted
Parsed empty panic string from panic log buffer even though expected non-zero length: eph_panic_log_len %u eph_panic_log_offset %u embedded_panic_length %lu
Panic info created
PS_ENABLE_SECONDARY_STREAMS
Truncated panic string from 0x%x to 0x%x bytes (ignoring other log)
Invalid timing %d
panicProcessingInfo
forceReset
outRespErr
com.apple.PanicProcessingSupport.EmbeddedPanicDataDecoder
Embedded panic log header contains invalid panic log offset
Semaphore destroyed
Debugger lock acquired
(timing: Unknown(%d), timestamp: %llu) 
%@%@
inRespErr
PS_SELECT_GFX_CONTAINER_DIM_A
%02hhx%02hhx
deviceModelType
patternUUIDs
PS_ENABLE_MR_NO_MATTING_STREAMS
Secure kernel coredump finished
Memory data moved
v8@?0
developerMode
bootProgressRegister
SOCDContainer
inResp
PS_SWITCH_TO_UNPROTECTED_SURFACES
Unknown status %d
arm-io
os_version
Data ID
kernel
allPids
source
interfaceID
Lock owned
Lock owned by self
extPaniclog
Lock unstable
panicString
test plan id: %llu
Terminated
Code signature error
Insufficient buffer size
panicProcessingFlags
Debug IPI sent
Resource shortage
storagePanicData
PS_ENABLE_MR_STREAMS
prevSMName
Invalid memory control
uuidResampling
com.apple.DumpPanic
PS_TRANSITION_WAKE
Already waiting
Policy static
interrupted coredump panic
sroute_id
-base+storage_crash
additionalData
panicFlags
No space
PS_DISABLE_ALL_STREAMS
Userspace coredumps finished
ExtensiblePaniclog
PS_INTERNAL_ANALYTICS_COMMAND
Expected 0x%x but found 0x%x
Embedded panic header doesn't contain valid panic log: eph_panic_log_len %u eph_panic_log_offset %u embedded_panic_length %lu
Protection failure
PS_DISABLE_SECONDARY_STREAMS
PS_TEST_TRANSITION_2
Cores halted
Panic log creation started
Coprocessor coredumps finished
Not supported
uuidIBoot1
PS_TRANSITION_TO_90_FPS
socRev
[No timing entries found]
wall %llu s %llu us
151
boardId
Invalid host
com.apple.stability.panic
panic
fallback_latency
timeSecs
Not in set
[Error: Invalid name at entry %u]; 
default
PanicGenerated
plane_supervisor
PS_ENABLE_DISPLAY_WRITE_BACK_STREAM
Embedded panic header contains invalid magic, expected 0x%x found 0x%x
inCmd
development-cert
Invalid KC
extPaniclogData
tAction
-base
performed
Default set
outResp
Invalid status 0x%x
incident
string
rawPanicData
PS_TRANSITION_SLEEP
embedded-panic-log-size
CrashlogContainers
-%@
SOCDNandContainer
=(0x[a-fA-F0-9]+|[0-9]+)(?:[ \\t\\r\\n]|$)
smStatus
      , Panic co-processors info: 
nextSMName
truncated other string
platformECID
User references overflow
Invalid capability
Not depressed
Invalid argument
Failure
Not receiver
i
crashReporterKey
uuidTXM
outReport
PS_TEST_TRANSITION
socId
ED96D2EC-F22F-05F4-F3E2-5DDEC8CA9030
Invalid value
Invalid policy
[Error: Invalid timing offset at entry %u]; 
co-processor name: %@, status: %@; 
PanicLogLengthInBytes
UsedSizeInBytes
Stackshot collection started
date
Panic Timing info: 
otherString
boardRevisionId
Node down
uuidSPTM
uuidKernelCache
Coredump completed
Invalid processor set
socDataVersion
SOCDContainers
platformSOCDBuffer
IODeviceTree:/chosen
outReportErr
kOSALogOptionFilenameTimestamp
kernelVersion
intentional panic
com.apple.PanicProcessingSupport
roots_installed
hw.osenvironment
Truncated panic string to 0x%x bytes, and dump it in rawPanicData (ignoring other log)
Memory error
210
OtherLogLengthInBytes
Coredump generation started
Right exists
RPC terminate orphan
type
nodeName
Missing KC
PanicMedicReports
tExecute
Invalid address
Memory present
Denied
build
notes
%.16s
StackshotLengthInBytes
customerFused
SOCDPanicString
PS_TRANSITION_TO_96_FPS
Success
RPC continue orphan
ECID
CrashlogContainer
stackResampling
kern.bootargs
0x%llx
outCmdErr
(timing: %@, timestamp: %llu) 
chip-revision
panicTimeInSecsAndUsecs
outCmd
PS_ENABLE_VR_STREAMS
product
Invalid object
%llx
repairStatus
lastPktTimestamp
ED96D2EC-F22F-05F4-F3E2-5DDEC8CA9031
Invalid right
Memory restart copy
%@
panic_ts
Exception protected
Invalid ledger
clientPID
Invalid security
codeSigningMonitor
inReport
lastPktType
PanicRegionSizeInBytes
ldm
%llu
yyyy-MM-dd-HHmmss
fallback_started
Lock set destroyed
-base+socd
%x
PanicLogUtilizationMetrics
PS_SWITCH_TO_PROTECTED_SURFACES
PS_DISABLE_DISPLAY_WRITE_BACK_STREAM
Invalid embedded panic header magic
com.apple.dumppanic
timeUsecs
deviceTargetType
Invalid no_of_logs %d
donate panic with pattern uuid %@ type %@
invalid eph_panic_log_len %u eph_panic_log_offset %u, embedded_panic_length %lu, header length %u
Panic info tracker processing
invalid panic info tracker coprocessor offset %u (length: %zu)
invalid eph_magic 0x%08X
unique device properties extracted - device target type: %@, device model type: %@
Coprocessor array extends beyond panic buffer: offset %u, count %u, size %zu, buffer length %zu
Coprocessor name not null-terminated at entry %u
found panic initiator with %u bytes
Extracting remote properties: SoC ID, SoC Rev, Product, Kernel Version, Platform ECID, Time
*** esrString %s ***
Could not create ext paniclog data
invalid extensible paniclog eph_ext_paniclog_len %u eph_ext_paniclog_offset %u,
The panic info tracker magic invalid: found 0x%x, expected 0x%x
Invalid timing entry offset %u at entry %u
Unable to create UUID String
setOriginalPanicReportPath: %s
no 'other' log found in embedded panic log
remote properties extracted - SoC ID: %x, SoC Rev: %x, Product: %@, Kernel Version: %@, Platform ECID: 0x%llx, Time: %llu s %06llu us
No timing entries recorded (offset is 0)
(embedded) length: %zu eph: magic %08X vers %u flags 0x%016llX panic_log offset %u, len %u, other_log offset %u, len %u, osversion: %@, macosversion: %@, bootsessionuuid: %@, roots_installed: %lld
invalid eph_panic_log_len %u eph_other_log_offset %u,
Extensible Paniclog offset %u Length %u
Did not find a valid panic initiator. Found with length: %d
Panic info timing first entry offset %u
Panic info coprocessor first entry offset %u, count %u
truncating eph_panic_log_offset %u, eph_panic_log_len %u (ignoring other log)
invalid eph_stackshot_offset %u, eph_stackshot_len %u
The co-processor name: %@, status: %@ at index %d
Unknown embedded panic header version: %d
found other log with %u bytes
truncating eph_other_log_offset %u, eph_other_log_len %u
Panic Initiator offset %u Length %u
Invalid version. Version in paniclog: %d\n
found embedded panic log with %u bytes
Invalid panic info tracker timing offset %u (length: %zu)
WARNING: unable to calculate panic region utilization
Extracting unique device properties: device target type, device model type
Unable to create Data ID and Data dict
Unable to create array
%@
*** %lu ***
found ext paniclog with %u bytes
Unable to create UUID object
Unable to create Data ID String
Data len is invalid: %d
failed to delete dumppanic in boot-args
*** isTagCheckFault ***
Did not find a valid ext paniclog. Found with length: %d
Reason: %@
rejecting implausible buffer!
invalid panic initiator eph_panic_initiator_len %u eph_panic_initiator_offset %u,
found panic info coprocessor array
Did not find valid panic info coprocessor entries (count is 0).
embedded panic string decoded: %@
Could not get panic initiator data
Unable to create Buffer data string
deleteBootArgDumppanic: no-op in default implementation
NSObject
PanicProcessingSupport
EmbeddedPanicDataDecoder
EmbeddedPanicDataDecoderV9
PanicProcessingDelegate
EmbeddedPanicDataDecoderV5
EmbeddedPanicDataDecoderV6
EmbeddedPanicDataDecoderV7
EmbeddedPanicDataDecoderV8
PanicReport
_TtC22PanicProcessingSupport23PanicProcessingInternal
```
