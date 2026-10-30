# `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,075,024 bytes.

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
B24@0:8#16
@\"NSString\"16@0:8
v28@0:8i16@20
v40@0:8r*16@24@32
@28@0:8@16B24
B24@0:8@16
@48@0:8@16B24I28@32@40
v16@0:8
I16@0:8
^{dyld_uuid_info_64=Q[16C]}16@0:8
@\"NSMutableDictionary\"
@52@0:8i16@20@28^{exit_reason_snapshot=IQQ}36@44
v32@0:8@16@?24
Q
i16@0:8
@\"NSDictionary\"
@\"_SwiftDiagnosticPatternMatching\"
B
@52@0:8i16@20@28^q36I44I48
i60@0:8i16@20@28@36{_CSTypeRef=QQ}44
@40@0:8@16@24B32B36
v20@0:8I16
@\"NSString\"
@24@0:8@16
v20@0:8i16
i
@\"NSArray\"
r^v
@36@0:8i16^{exit_reason_snapshot=IQQ}20@28
@\"NSArray\"16@0:8
@\"NSDictionary\"16@0:8
@\"NSSet\"
@28@0:8i16@20
@\"_SwiftPanicPatternInfo\"
B64@0:8@16@24@32@40^@48@?56
@36@0:8@16@24B32
v52@0:8@16@24d32Q40I48
v20@0:8B16
v24@0:8^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}16@0:8
^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII}
^{dyld_uuid_info_64=Q[16C]}
@20@0:8i16
@\"NSDictionary\"8@?0
@24@0:8:16
Vv16@0:8
@44@0:8@16@24^q32I40
v40@0:8@?16@24@32
@32@0:8^{exit_reason_snapshot=IQQ}16@24
@32@0:8@16@24
v16@?0@\"NSFileHandle\"8
v16@?0@\"NSError\"8
i32@0:8@16@24
^q
@36@0:8@16i24@28
@40@0:8:16@24@32
v16@?0@\"BGSystemTask\"8
v12@?0B8
B32@0:8@16@24
v16@?0@\"NSString\"8
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}28@0:8I16^@20
I
^[37c]
v56@0:8r^v16I24@28d36Q44I52
v60@0:8r^v16I24@28d36Q44I52B56
^v
v40@0:8@16@24@?32
^{_NSZone=}16@0:8
B16@0:8
v28@0:8B16@?<v@?@\"NSDictionary\">20
@32@0:8@16i24B28
Q40@0:8@16Q24q32
^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}
v28@0:8^{dyld_uuid_info_64=Q[16C]}16I24
@28@0:8@16i24
Q16@0:8
#16@0:8
v16@?0@\"NSURL\"8
v24@0:8@?16
v28@0:8B16@?20
v24@0:8Q16
^[37c]16@0:8
v24@0:8@16
B72@0:8@16@24@32@40@48^@56@?64
r^v16@0:8
q16@0:8
@40@0:8@16@24@32
v32@0:8{kcdata_iter=^{kcdata_item}^v}16
@32@0:8:16@24
v8@?0
@16@0:8
@\"NSMutableArray\"
v32@0:8r^v16I24I28
v40@0:8@\"NSSet\"16@\"NSSet\"24@?<v@?B>32
B24@0:8:16
B24@0:8@\"Protocol\"16
stackshot_tuning
blocked on workqueue: 0x%llx, hops: %d, priority: %d
active_count
systemDefaultSharedCache
resampled %d of %d threads with truncated backtraces from %d pids: %@
unknown-arch
x86_THREAD_STATE
No payload found on device
rbp
panic
commandCursor == commandBuffer + sizeof(commandBuffer)
i
vnode-limit
v20@?0I8r^{stackshot_thread_waitinfo_v2=QQQCsI}12
uuid_faulting
pagesWanted
TH_SFLAG_EAGERPREEMPT
Kernel text base
jetsamCoalition
jitStartAddress
mach_msg receive on 
page-ins throttled for VM object %#llx
suspensionLastEnd
r13
threadState
sp
frontmost
uuidResampling
isBeta
Transformation not supported for log type
panicFramesMatchMode
Product Version Section
com.apple.ReportSystemMemory
TH_SFLAG_THREAD_GROUP_AUTO_JOIN
xform-error
SPARE_1
dyldCompactInfoMissing
kThreadOnCore
\"
ARM_THREAD_STATE64
internal
Unknown KCDATA ARRAY type %X, count %d, size %d, flags %llX
 Dispatch queue: 
Unable to transform log
TABLE_TOP
locked 
unfair 
taskSpecificSharedCache
allowIdleExit
panicStringDelimiter
TH_SFLAG_WAITQ_PROMOTED
tags
container && (container.type == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK)
connected
incident
code
r11
[kc_stack count] == 0
%@%@%@\n%@\n
com.apple.diagnosticservicesd
FWUP
age
TALEngaged
memoryErrorReport
%d unindexed re-sampled frames from %d pids: %@
sampleTruncatedStacks
%@_0x%04X
reportNotes
flavor
none
daemon
v20@?0I8r^{stackshot_thread_turnstileinfo_v2=QQCCQs}12
qosEffective
Unable to find class %s
trap
binaryImages
, 
container
r14
^([A-Z_]+), (\\[0x[0-9a-zA-Z]\\] )?(.*)$
385
fc-thrashing
invalid_images
visNonvisible
share_with_app_devs
r8
stackshot_duration_prior_nsec
kThreadTruncatedBT
train
%s
mtePageTags
ACM
#(
vmRegionInfo
DiagnosticsReporterLaunchOptions
performCommand
eventReason
isNonFatal
Invalid number of keys found, expected one.
no-compressor-space
com.apple.iokit.hid.displayStatus
accessory_type
AirPodsReporting
crashlog
csFlags
qosOverride
krwlock %#llx for reading
continuation
isLocked
QOS_CLASS_USER_INTERACTIVE
%s ELIDED %u LEVELS OF RECURSION THROUGH %s
snapshotFlags
OSADiagnosticsReporter
reason
isImpDonor
Thread %d crashed with ARM Thread State (32-bit):\n    r0: 0x%08x    r1: 0x%08x      r2: 0x%08x      r3: 0x%08x\n    r4: 0x%08x    r5: 0x%08x      r6: 0x%08x      r7: 0x%08x\n    r8: 0x%08x    r9: 0x%08x     r10: 0x%08x     r11: 0x%08x\n   
\n tmp0: 0x%016qx tmp1: 0x%016qx tmp2: 0x%016qx\n
platform
mem_regions
pageouts
<item>
CoreDiagnostics.DiagnosticPatternMatching
foreground
uncompressed
(unknown-reason)
codeName
container.type == STACKSHOT_KCCONTAINER_THREAD
queue thread to be allocated
parentPid
is_beta
accessory_os_version
active
alternate
pthread mutex %#llx
Syslog query timed out
speculative_count
Error in pattern matching: (
frozen_to_swap_pages
processes
pager ready for VM object %#llx
postSampleVMStats
TH_SFLAG_ECORE_ONLY
.
audio
NEW_FW_BOOT
timeDelta
thermalData
hits
userTimeTask
suspensionLastStart
TH_SUSP
accessory_pid
max_pages
killDelta
,
slide
namespace
spindump
*
tmp1
 owned by thread %lld
rsp
crashlogs
analytics_test_mode
Register Frame Section
CASE_LID_OPEN
boosted
ip
TRANSPARENCY
memorystatus_control returned unexpected value - %d: %s
This is a watchdog-triggered termination event, and not expected to be well-represented in the legacy crash format
compressions
cpuTime
PanicPatternDefinition
Failed to decode crash report
no shared cache available from the kernel snapshot -- this may impact symbolication
requireCrashingThread
coalition
container && (container.type == STACKSHOT_KCCONTAINER_TASK)
<exempt>
registers
exceededWQTotalLimit
largestZone
table
page list requests for VM object %#llx
waitInfo
symbol
application-info
paging/activity for VM object %#llx
shared_cache_layout
0x%llX
kUser64_p
Report transformation returned an unexpected output format.
<data>
cpuType
com.apple.CoreDiagnostics
CoreDiagnostics.CrashPatternInfo
ThermalPressureLevelSleeping
Got fewer jetsam entries from the kernel; received %zu, expected %zu
Failed to set flags for stackshot config
dyldCompactInfoTriedFault
userFrames
uuidFaultFlags0x%08llX
x
source
monitoring timed out for service without diags
timestamp
LibCall_ACMKernelControl_Block
Done with pattern check
log-version
section-signature
eventCode
Unmapped pages caused truncated backtrace; re-sampled %d frames
waitEvent
rflags
swapouts
suspensionThreadID
kThreadTruncUserAsyncBT
deallocationTrace
\t<==
turnstile has unknown inheritor
QOS_CLASS_DEFAULT
...%@
com.apple.corediagnostics.pattern-lookup-async
blamedAllocation
passcodeSet
kGlobalForcedIdle
com.apple.corediagnostics.pidselection.retry
Process:             $(procName|\"???\") [$(pid)]\nPath:                $(procPath|\"???\")\nIdentifier:          $(bundleInfo.CFBundleIdentifier|procName|\"???\")\n^(bundleInfo.CFBundleShortVersionString)Version:             $(bundleInfo.C
product
resampledExtraImages
writes
esr
cow_faults
donatingPids
unindexed_rs_frames
monitoring timed out for service
bug_type
SPARE_4
pthread rwlock %#llx for writing
kcdata_iter_container_id(kcData) == end.tag
suppressed
ThermalPressureLevelNominal
r12
The diagnostic service crashed or hung
symbolTransitions
memoryPages
Stackshot key-combo received while a prior stackshot was still processing.
absoluteTime
accessory_machine_config
lookups
bundleInfo
lr:\\s*(0x[0-9A-Fa-f]+)\\s+fp:
largestProcess
Process %@ is in transition type %@
ThermalPressureLevelHeavy
yyyy-MM-dd HH:mm:ss.SS Z
background
%p + %llu
com.apple.corediagnostics.patternMatched
task_read_for_pid(%d) for resampling backtraces failed with %d
CDStackshotReport.m
QOS_CLASS_USER_INITIATED
<unknown>
kThreadDarwinBG
frozen
states
%@lock %#llx
kThreadTriedFaultBT
327
usage_since_last_crash
kThreadTruncUserBT
actions
port %#llx with unknown owner
kThreadFaultedBT
(unknown)
exclaveScid
TH_SFLAG_RW_PROMOTED
kThreadMain
com.apple.corediagnostics
usage_since_last_crash_user_facing
%02x%02x%02x%02x
event_number
zone-map-exhaustion
port %#llx owned by pid %llu
v32@?0Q8r*16r*24
TH_RUN
displayState
tmp2
QOS_CLASS_UNSPECIFIED
keyFrame
threads
os_version
tracked
ThermalPressureLevelModerate
%u
-
v16@?0@\"NSString\"8
 (%@:%@)
inline
inactive_count
stack
idle
locked port %#llx
com.apple.corediagnostics.diagnostic-intelligence
continuous
krwlock %#llx for writing
-%u
lastExceptionBacktrace
298_ALE
Failed to allocate memory for jetsam status list
[kc_stack count]
details
runawayMitigation
com.apple.corediagnostics.patternMatchingQueue
\nGROUP BY processName \nORDER BY count DESC \nLIMIT 
MTE Malloc Size Class: 
sustained-memory-pressure
kHasDispatchSerial
template has illformed definition
crk
busy compressor segment %#llx owned by thread %llu
suspendCount
jitEndAddress
ThermalPressureLevelTrapping
CFBundleShortVersionString
throttled_count
kernelFrames
cpsr
idle-exit
lastMadeRunnableTime
qosRequested
QOS_CLASS_BACKGROUND
TH_SFLAG_BOUND_SOFT
bytes
threadTriggered
COUPLED
disableWatchdogStackshot
vmregioninfo
heap-usage
298_LOW_PRIORITY
turnstile was in the process of being updated
scenario
log
isLiveImpDonor
resume
 with unknown owner
exception
internal_page_count
suspensionCount
suspensionProcName
variantVersion
LibCall.c
purgeable
pthread condvar %#llx
pageIns
sourceFile
0x%016qx
CrashReporterKey:
route-number
ioStats
crashReporterKey
(invalid-reason)
xform-full-report
dyldCompactInfoTooBig
TH_SFLAG_RT_DISALLOWED
com.apple.corediagnostics.cputrace
ACMKernelControl
BUD_SWAP_IN_PROGRESS
wired
sharedRegionOther
kKernel64_p
<index>
ARM_THREAD_STATE32
imageExtraInfo
SPARE_2
resampled %d of %d images missing from %d pids: %@
r10
assertiond
state
lastBranchState
(unprintable)
<value>
v32@?0@\"NSTextCheckingResult\"8Q16^B24
isTranslated
SENSOR_PKT_SERVICE
SpringBoard
fileBacked
location
Stackshot syscall failed (from euid %d) with error %d: %s
process_images
Thread %d crashed with ARM Thread State (64-bit):\n    x0: 0x%016qx   x1: 0x%016qx   x2: 0x%016qx   x3: 0x%016qx\n    x4: 0x%016qx   x5: 0x%016qx   x6: 0x%016qx   x7: 0x%016qx\n    x8: 0x%016qx   x9: 0x%016qx  x10: 0x%016qx  x11: 0x%016qx\n
HFP
No processes were jettisoned (either killed or suspended)
notes
unknown type %u (owner %llu, context %#llx)
Thread %d last branch register state:
Failed to connect to listener, error: 
DIAGNOSTIC_PATTERN_MATCHING_PANIC
additionalDetails
Unknown transformation error.
init
largestZoneSize
accessory_fusing
Kernel UUID:\\s*([A-F0-9-]{36})
neuralPages
vm-compressor-thrashing
notice
reads
portlabels
container && (container.type == STACKSHOT_KCCONTAINER_THREAD)
Panicked thread:.*?backtrace:.*?tid:\\s*\\d+\\s*\\n(.*?)(?:
fds
Failed to get jetsam status list (query returned %d)
SELF != ''
dyldCompactInfoFaultedIn
processByPid
copyOnWriteFaults
rdx
purges
usedImages
zoneMapSize
mach_msg send on port %#llx in transit to 
%@ + %llu%@%@
  Cacheline:
Missing report body to transform
panicReasonString
TIPI
turnstile blocked on task pid %lld, hops: %d, priority: %d
metadata
|
TH_SFLAG_ABORTSAFELY
v24@?0r^v8Q16
ioKitTransport
backboardd
stackshot_duration_nsec
TH_SFLAG_FLOOR_PROMOTED
bootSessionUUID
<key>
codeSigningValidationCategory
date
resampledUserFrames
Terminated by Unblock framework for not recovering after hitting thread limit
name
freeze_skip_reason:
queue in a transient state
v8@?0
%@
crashTime
Kernel Extensions in backtrace:
pc
err
acm_mem_alloc_info
compressorSize
turnstileInfo
mach_msg receive on %@port set %#llx
kcdata_iter_container_type(iter) == STACKSHOT_KCCONTAINER_PORTLABEL
memoryPressure
-[CDStackshotReport decodeKCDataWithBlock:withTuning:usingCatalog:]
resampleIncomplete
modelCode
ANC
procname
triggered
%18p - %18p %@ (%@) <%@> %@
#
Heap overflow by at least 
sharedRegionNone
schedPriority
%d unindexed user-stack frames from %d pids: %@
rsi
tasks
out-of-budget
free_count
sourceLine
memorystatus_control gave snapshot size (%lu) not multiple of jetsam entry type (%lu)
suspending
TH_UNINT
region
ACMLib
uuid
\n
(%@)
acm_mem_free_info
%d
priorities
disabled
intransit port %#llx
Failed to allocate memory for stackshot config
-----------\nFull Report\n-----------\n
out-of-slots
schedFlags
dispatch_queue_label
call-stack
pid
CFBundleIdentifier
host_statistics64 failed
QOS_CLASS_UTILITY
dyldCompactInfoNone
queue
queryBiomeForCrashes(topN:daysBack:)
systemTime
codeSigningAuxiliaryInfo
QOS_CLASS_MAINTENANCE
  [%02d] (%@) -> (%@)\t%@
%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n
queue that is suspended
Thread %d%@:%@%@%@%@
accessory_os_train
port %#llx
groupID
TH_SFLAG_RT_CPULIMIT
per-process-limit
 in spin mode
No jetsam status list available (size query returned %d)
flags
compressor_page_count
deployVersion
symbolLocation
kThreadIdleWorker
time_since_last_transition
spin
task_threads() for %d failed
faultingThread
thread %llu: 
waitinfos
unindexed_frames
flag
usage_since_last_crash_in_ear
Debugger message
other
<NO_NS>
unknown
id
pageFaults
fp
rosetta
event_history
CoreDiagnostics.PanicPatternInfo
PSE
logwritten
variant
 Crashed
%s: %s: called.\n
dirty
build
jettisoned
TH_SFLAG_PRI_UPDATE
Unable to load log '%@'
\\n\\s*loaded kexts:
turnstile had unknown status (flags: 0x%llx)!
Callstack Section
IN_EAR
procPath
vid
resampled_images
<0x%X>
imageOffset
routed_to_source
Probabilistic Guard Malloc
%s: %s: returning.\n
assertion
rsrcFlagged
data
Thread %d name:  %@%@%@
lr
accessory_crashreporter_key
Heap underflow of 
lifetimeMax
TH_IDLE
codeSigningFlags
ale_flag
%-3d %@
mailbox-error
panic\\(cpu\\s+\\d+\\s+caller\\s+(0x[0-9A-Fa-f]+)\\)
PIDSelection.previousProcessName
<unprintable>
TH_SFLAG_UNKNOWN
Failed to send message or decode reply: 
suspensionProcID
osVersion
offset
legacyInfo
JetsamEvent
unable to allocate %d bytes for jetsam snapshot
0x%llx
zero_fill_count
com.apple.gmAvailability.queue
;
idleDelta
additionalPayload
inactive
TH_TERMINATE
base
%p + %llu%@%@
Thread %d crashed with X86 Thread State (64-bit):\n  rax: 0x%016qx  rbx: 0x%016qx  rcx: 0x%016qx  rdx: 0x%016qx\n  rdi: 0x%016qx  rsi: 0x%016qx  rbp: 0x%016qx  rsp: 0x%016qx\n   r8: 0x%016qx   r9: 0x%016qx  r10: 0x%016qx  r11: 0x%016qx\n  r
task_read_for_pid(%d) for resampling UUIDs failed with %d
vm-pageout-starvation
stacks
rcx
ldm
suspensionSources
Memory Safety Violation (
thawed
Kernel text base:\\s*(0x[0-9A-Fa-f]+)
missing stackshot buffer or size
QOS_CLASS_UNKNOWN (%u)
size
genCount
suspended-only jetsam log already dumped today
timesDidThrottle
instructionStream
low-probability-of-use
queue processed by thread %llu
isDirtyTracked
rax
!
Unexpected error
DIAGNOSTIC_PATTERN_MATCHING_CRASH
conclave-limit
excess-shared-memory
bootProgressRegister
stackResampling
termination
sw_ver
kernel
No heap allocation information available
(unknown-%llu)
timesThrottled
non-parseable kc snapshot buffer
captureTime
Thread %d instruction stream:
index
incident_id
309
Thread %llu has an incorrect exclave frame offset %d
suspensionDuration
Thread %d%@:
Terminated by Unblock framework for unrecoverable deadlock
mapping-in-progress for VM object %#llx
arch
periodic
proc-thrashing
kStacksPCOnly
The received pattern info are not valid
com.apple.corediagnostics.visualization
wasUnlockedSinceBoot
\\n\\s*Kernel Extensions in backtrace:
Kernel text exec base:\\s*(0x[0-9A-Fa-f]+)
OFF
vm-compressor-space-shortage
genCounter
residentMemoryBytes
processUptime
userTime
XPC request timed out
LibCall_ACMKernelControl
highwater
portlabel_info->portlabel_id == portlabel_id
TH_SFLAG_PROMOTED
kThreadIOPassive
SPARE_3
cacheLine
is_non_fatal
kernel mutex %#llx
pthread rwlock %#llx for reading
ThermalPressureLevelLight
Task List Section
409
frames
%s RECURSION %u, LEVEL %u
path
-------------------------------------\nTranslated Report (Full Report Below)\n-------------------------------------\n
syslog
rawFlags
signal
isCorpse
SELECT COUNT(*) as count, processName \nFROM \"
pattern
LIVE_LISTEN
port %#llx owned by kernel
kThreadUnknown
unknown port
HS
ON
TH_WAIT
iokit
thermalLevel
long-idle-exit
below-min-pages
TH_SFLAG_BASE_PRI_FROZEN
: 
stack-description
\nBlamed allocation: [
Failed to read attribute as string for: 
availability
SPARE_5
nonpaging
Unable to parse template
DOCKED
container && ((container.type == STACKSHOT_KCCONTAINER_TASK) || (container.type == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK))
resampledAllImages
\\^\\([^\\)]+\\)
core
%s: %s: returning, err = %ld.\n
reactivations
pageins
!KCDATA_ITER_FOREACH_FAILED(kcData)
far
{%@}
paging-in-progress for VM object %#llx
external_page_count
stackshot inclusion disabled
recursionInfoArray
Failed to send message or get reply:
accessory
<port label truncated>
total_uncompressed_pages_in_compressor
stackshot_duration_outer_nsec
originalLength
no-swap-space
 owned by pid %lld
allPids
faults
Unmapped pages caused truncated backtrace (resampling disabled)
TH_SFLAG_THROTTLED
tmp0
can_idle_exit
memoryStatus
low-swap
pagesReclaimed
cr2
):\nFault: Invalid 
busy VM page %#llx
blocked memory access for VM object %#llx
Thread %llu has exclave frames but no kernel frames
r15
nearestAllocation
ON_HEAD
uptime
 (service throttled by launchd)
WATCHDOG
INVALID
pageSize
imageIndex
isSimulated
Unable to load full report.
\\bat pc\\s+(0x[0-9A-Fa-f]+)
memorystatus_control(MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT) failed: %s
Thread %d instruction stream (single cacheline):
Failed to send message or get reply: 
init()
csTrustLevel
semaphore port %#llx
sharedRegionSystem
TH_SFLAG_FAILSAFE
Unable to read JSON
elapsed time
CoreDiagnostics.CrashReportBodyBridge
textualRepresentation
speculative
stringByTrimming
 (%@)
LibCall_BuildCommand
 [inlined]
suspended
mach_msg send on 
exceededWQConstrainedLimit
TH_SFLAG_POLLDEPRESS
kThreadTruncKernBT
codeSigningMonitor
lastRunTime
A2DP
bluetooth
low-private-shared-ratio
port %#llx name %#llx
TH_SFLAG_ABORT
%p %@
--------
rdi
purgeable_nv
TH_SFLAG_EXEC_PROMOTED
%-*u %@
%18p - %18p %@ %@  <%@> %@
priority
lastSuspendedLogDumpedDaySince1970
298_HIGH_PRIORITY
indicator
thermalPressureLevel
%@\t%18p %@
)#
wire_count
parsedData
krwlock %#llx for upgrading
value
visible
releaseType
probGuardReport
is_simulated
free
%@ (%@)
metadata:
darwinBG
SPLITTER
com.apple.Jetsam.Kill
developerMode
memoryPressureDetails
TH_SFLAG_DEPRESS
r9
crashlog-version
system_usec
Thread %llu with %lu kernel frames has exclave frames but invalid exclave frame offset of %d. Skipping adding exclave frames into kernel frames 
kThreadSuspended
procName
description
osVersion.train
unsupported JSON schema version
appleIntelligenceStatus
v16@?0@\"NSError\"8
\\$\\((([^\\)\"]+|\"[^\"]+\")+)\\)
Length is zero for attribute: 
stackshot
Unable to read log stream: %@
Faulting access is at offset 
Kernel Extensions in backtrace:\\s*\\n(.*?)(?:\\nloaded kexts:)
swapins
JSON schema not understood
disk-space-shortage
 owned by thread %llu
user_usec
userID
???
AppleCredentialManager
kernel returned (0) from memorystatus_control(MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOT) -- no jetsam data available
zones
error
suspensionTime
cpu
instructionState
paging
-[NSMutableDictionary(StackshotKCDataExtension) parsePortLabelContainer:]
purgeable_count
extDarwinBG
509
rip
298
anonymous
sensors
UI_country_code
terminatedSnapshot
Unknown
&
version
Address Range: [Start, End)
CONNECTION_IN_PROGRESS
decompressions
 
frontmostPids
macOS
customerFused
Unable to create VMUSampler for %d
TH_SFLAG_REEVALUTE_TG_HIERARCHY_LATER
app_name
reasons
\" \nWHERE eventTimestamp >= 
accessory_release_type
MTE Page Tags (faulting address: %p)
symbolicated_log
308
%@%s
bootArgs
systemTimeTask
%02x%c
asi
unknown error
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
throttled
tuning
0x%08x
_dyld_process_info_create(%d) for resampling UUIDs failed with %d
lowPowerMode
288
etl_key
%s RECURSION LEVEL %u
rbx
stacks+%@
spawnFlags
TH_SFLAG_PCORE_ONLY
visVisible
r
  cr2: 0x%016qx\n  \nLogical CPU:     %d\nError Code:      0x%08x %@\nTrap Number:     %d\n
<unavailable>     
is_corpse
zoneMapCap
blocked on %lld, hops: %d, priority: %d
busyBufferCount
active_scenarios
rpages
TH_SFLAG_NO_SMT
PIDSelection.previousPID
mailboxes
telemetry_mode
(\\S+)\\([^)]+\\)\\[([A-Fa-f0-9-]{36})\\]@(0x[0-9A-Fa-f]+)->(0x[0-9A-Fa-f]+)
NULL
threadById
basePriority
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c
ReportViewer
physicalPages
vm-pageshortage
Unknown KCDATA %X, size %d, flags %X
TH_TERMINATE2
%@: %@
Crash redaction is disabled
unable to allocate %d bytes for wired memory info
Expected a task specific shared cache with id %@ but none was found
there is no available matcher with type %u
Callback failed, will retry next interval
PID %d still running as '%s', skipping selection
look for known pattern error: %s
MTBF section too small to decode: (%ld < %ld)
memorystatus_control for command %d returned unexpected valud of %d which does not match buffer size of %d
Unable to extract report body for file %s
%s fired
Error: expecting max of %ld reports per hour, but found %ld
RTBuddyCrashlogDecode not available
failed to get pressure level state: %d
Unable to convert report body to JSON for file %s
There are no crash payloads available
Submitting background task: %@
Background task %s already exists (interval: %fs), skipping submission
Found PID %d for process %s
failed to create registration token for pressure level: %d
Unexpected type for exception backtrace
Failed to redact frames for normal thread
Invalid or no section name/signature found
Offset section not available to decode Csif
Failed to retrieve base address from raw buffer binary
Unable to determine malloc size class for uniform MTE tags
ips metadata not detected (%ld bytes before newline), attempting to read entire file as payload
Key '%s' not found: %s\nCoding Path: %s
Crash frame has valid image index, but image missing source name
No ExcResource reports found
Error retrieving file CreationDate: %@
Report timestamp could not be parsed; defaulting to full redaction
Frame %ld (non-final): LR 0x%s not in any kext/kernel range - backtrace corrupted
memorystatus_control for command %d returned %d - No data available
Received response: %s
Error decoding payload: %@
Biome SQL query failed: %@
Failed to convert to body to json
Unable to represent audio assertions as a set as PIDs: %s
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
Pattern %s has multiple donation types (%ld)
Unable to parse report for file %s
BGRepeatingSystemTaskRequest not available
All %ld processes checked, none running
Failed to create OSALog file: %@
Signature mismatch for section %s. Found: %s, expected: %s
Size section not available to decode MTBF
Unable to represent visibility endowments as a set as PIDs: %s
*** ignoring non-numeric symbolLocation: '%@'
Failed to read payload at %s
Binary not available to decode MTBF
memorystatus_control for command %d failed with error %d
this log appears to be from the DA grid, using parsedData section
Unable to find date in report body
Trial is not available
Matched the pattern definition with UUID %s
Failed to create UserDefaults for suite: %s. Falling back to standard
Failed to redact frames for lastExceptionBacktrace
Failed to look for pattern %@
Conflicting donation types found: %u vs %u
Found donation type %u with UUID: %s
Type '%s' mismatch: %s\nCoding Path: %s
Missing asset for %s in namespace %s
isProcessAlive(%d) -> %s
There is no panic payload available
%s: %s: returning, err = %ld.\n
DiagnosticsReporterServices.framework is unavailable
Biome query timed out after %f seconds
Scenario information range %u too large for section size %ld
Unable to retrieve extended attribute %s for file %s with Error: %@
failed to create registration token for display state: %d
%s
Using custom process list (%ld processes): %s
Top crashing process list from Biome: %s
The panic reason string does not match, skip this pattern
look for known pattern other error: %@
Invalid bug_type for Jetsam report: %s
Failed to create AirPods crash report
Scenario information trailer length too small %hu < %ld
AnalyticsQueryValuesFor timed out after 10s; clearing AI state
Unable to serialize report body as JSON: %@
failed to create VMUProcInfo
failed task_read_for_pid with %d
Value '%s' not found: %s\nCoding Path: %s
Invalid bug_type for crash report: %s
Invalid or missing Mailbox registers
Failed to get reasons array
Payload %ld: %s
Background system task handler registration failed
Failed to submit background task: %@
Unknown panicFramesMatchMode: %s
Invalid size and offset for Csif
Offset section not available to decode MTBF
Invalid or missing Mailbox route number
%@
Error: RTBuddyCrashlogDecode returned nil
Invalid or missing Mailbox error
Exclave frames offset of %d for thread %llu is invalid
Failed to connect to listener, error: %@
Unable to find incident in report body
Using Trial payload at %s for %s in namespace %s
Failed to calculate start date for biome query
crashRedactionEnabled: found value of %{public}s from Secure Config
GM availability string not found
OSADiagnosticsReporter or DiagnosticsReporterLaunchOptions class not available
synthesizing %d items from payload as metadata
Selected PID %d (%s)
Got no value from SecureConfig for crashRedactionEnabled, returning false
Crash report missing thread data
Processing binary for core: %s
Scenario information with range %u indicates trailer present but not enough space in section size %ld
Report has missing or malformed exception codes.
BackgroundSystemTasks not available on this OS version
Binary not available to decode Csif
Invalid scenarioType %hhu
Failed to decode as CrashReportBody: %@
Cannot retrieve creationDateKey for file %s
key %s -> %s
%s: %s: called.\n
Failed to send message or decode reply: %@
Invoking client callback with PID %d
panic string matched: %s
create a regex %s
Invalid or missing Mailbox log
failed to get display state: %d
Error loading full report: %{public}@
Missing level for %s in namespace %s
Failed to get proc_name for pid %d
found panic caller: %s
No processes available, will retry next interval
Callback completed, success=%s
Crash report frames have unexpected type
Unable to parse RTBuddy crash log dictionary
Panic matcher could not be initialized
Unable to find panicString in report body
Failed to send message: %@
Background system task handler registered, waiting for it to fire
SecureConfig error for crashRedactionEnabled, defaulting to true: %@
Cannot retrieve file size for %{public}s: %@
Expected a task specific shared cache with ID %{public}@ but none was found
BiomeStreams (BMSQLDatabase) not available on platform
Invalid MTBF section offset and size
MTBF section too small to decode beyond usage_time_btw_crashes: (%ld < %ld)
Skipping final frame with LR 0x%s not in kext/kernel range
AnalyticsQueryValuesFor returned non-dictionary result
Failed to create symbolicator
unsupported log type '%@' effective (%@)
Successfully parsed payload for %s in namespace %s as type %s. Count = %ld
Biome SQL query returned %ld processes: %s
Scenario information range %u and trailer length %hu too large for section size %ld
Error connecting to remote object: %@
found at pc match: %s
Failed to create regex
Generated random number %ld for redaction
Crash frame missing image index
Initializing AirPodsCrashReport
Unable to determine malloc size class for empty MTE tags
%s: %s: cmd(%u) on CS[%u] -> ok.\n
Process %{public}@ [%d] killed by jetsam reason %{public}@
Failed to launch DR with error: %@
Failed to encode JSON: %@
%s: %s: returning, err = %ld, code=%u.\n
Unknown KCDATA CONTAINER %X
Unable to parse payload for %s in namespace %s as type %s
Unable to retrieve extended attribute \"bug_type\" for file %s with Error: %@
No callback registered, cannot deliver PID %d
lastProvidedPID: %s, processName: %s
Size section not available to decode Csif
Failed to parse heap usage from section contents: %s
Thread has backtrace with unexpected type
Not sending Core Analytics events because snapshot is missing.
Error fetching TRM status: %i
Process '%s' is running (PID %d)
softlink:o:path:/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices
_TtP15CoreDiagnostics29ReportSystemMemoryXPCProtocol_
CDJetsamReport
_SwiftDiagnosticPatternMatching
_TtCC15CoreDiagnostics11CrashReport13CrashRedacter
AirPodsCrashReportObjc
_TtC15CoreDiagnostics22AppleIntelligenceState
CDStackshotReport
_TtC15CoreDiagnostics27TextualRepresentationBridge
CoreDiagnostics
CDTerminatingStackshotReport
objcDiagnosticPatternMatching
ReportViewerAugment
OS_xpc_object
NSObject
_TtC15CoreDiagnostics16CrashPatternInfo
objcPanicPatternInfo
_TtC15CoreDiagnostics21CrashReportBodyBridge
_SwiftPanicPatternInfo
PIDListExtension
StackshotKCDataExtension
ReportViewerObjC
_TtC15CoreDiagnostics11CrashReport
_TtC15CoreDiagnostics12JetsamReport
_TtC15CoreDiagnostics31DiagnosticReportCollectorBridge
_TtCFC15CoreDiagnostics22AppleIntelligenceStateP33_088BB0F0F87A4F30D60030036C3E7D2E28updateAppleIntelligenceStateFT_T_L_14XPCQueryResult
CDSystemWatchdogStackshotReport
_TtC15CoreDiagnostics19CPUTracePIDSelector
CPUTracePIDSelectorObjC
_TtC15CoreDiagnostics11PatternInfo
_TtC15CoreDiagnostics24WatchdogExitReasonHelper
_TtC15CoreDiagnostics19CompatibilityBridge
_TtC15CoreDiagnostics11DeviceState
OSAConcreteReport
SharedCacheEntry
isCustomerFused
T^{dyld_shared_cache_loadinfo_v2=Q[16C]QQII},R,N,V_original
fetchWiredMemoryInfo
formatCallstacks:withImages:macosStyle:
initWithSuiteName:
metaData
truncated_threads
jetsamLevel
panicReasonString
decode_reason:reason:
findBundleAtPath:withKeys:bundleURL:
integerValue
saveWithOptions:
setSharedCacheLayout:andCount:
exceptionType
count
isAppleTV
_extras
cpuType
initWithKCData:
initWithCapacity:
_thermalSensorValues
patternMatcher
rangeAtIndex:
setKernelCache:address:size:
appendPortLabelInfo:portlabels:
_includeSyslog
numberWithDouble:
removeObjectForKey:
setKernelTextExecImages:
_isSuspendedOnlyJetsam
dictionary
firstObject
getThermalPressureLevel
setAdditionalPayload:
ExcResourceReportPaths
_sharedCacheUnreliableSlidBaseAddress
enumerateMatchesInString:options:range:usingBlock:
parseKCdata:
setFlags:
_tags
flags
panicStringDelimiter
_daysSince1970
setPid:
optIn3rdParty
setDead_snapshot:
release
_sharedCacheUuid
autorelease
bodyJson
codeSigningMonitor
interval
lookForPatternAsync::
type
_setDumpedSuspendedJetsamLog
appleCareDetails
getTaskingKey:
unindexed_frames
_termination_info
fileValue
formatImages:macosStyle:
stream
stringValue
formatLastException:withImages:
getPanicPatternInfo
setRootedCacheLibs:count:
_visibilityEndowmentState
initWithPath:forRouting:options:error:
initWithPatternInfo:
path
_ss_trace_length
objectForKeyedSubscript:
coldestElided
_killedActiveApps
fetchSnapshotWithFlags:error:
interfaceWithProtocol:
numberWithShort:
transformURL:template:options:
initWithPid:procName:bundleID:exitSnapshot:reason:
WriteJetsamMemoryReportWithVisibilityEndowmentSet:audioAssertionSet:
TB,N,R
acquireJetsamData
setSymbolicator:
JSONObjectWithData:options:error:
TI,N,V_ss_sequence
additionalIPSMetadata
crashReport
setIncidentID:
dataWithBytes:length:
isRedactionEnabled
retainCount
writeJetsamMemoryReportWithVisibilityEndowmentSet:audioAssertionSet:with:
T@\"NSString\",R,C
augmentWithPrefix:
reportUsedImages
superclass
commonFieldsForBody:
_swiftDiagnosticPatternMatching
launchDiagnosticsReporter
processInfo
generateReportWithBinary:testMode:productId:applicationInfo:description:
initWithPattern:options:error:
formatMTEPageTags:report:
initForPid:exitSnapshot:reason:
_awakeSystemUptime
coalitionName
etlKey
isDefaultSharedCache
queryThermalData
setThreadId:withScId:
updateLogLimitFor:
_procPath
data
procName
appendString:
initWithSwiftDiagnosticPatternMatching:
next
_sharedCacheID
isProxy
componentsSeparatedByString:
depth
setReason:
sharedCacheSlide
stringByPaddingToLength:withString:startingAtIndex:
formatFrame:withImages:macosStyle:
_original
getEventPriority:terminationReason:priority:
parsePortLabelContainer:
setInterval:
backtraceLength
_spindump
performSelector:withObject:withObject:
setObject:forKeyedSubscript:
_snapshot
addEntriesFromDictionary:
performSelector:
resume
vmRegionInfo
T#,R
_getSnapshotWithFlags:
pid
_sharedCacheSlide
componentsJoinedByString:
numberWithInt:
randGenerator
regularExpressionWithPattern:options:error:
isInLDM
panicPC
numberWithUnsignedLongLong:
releaseType
getDisplayState
_ss_trace_buffer
initWithSwiftPanicPatternInfo:
name
transformReport:templateString:header:report:error:streamingBlock:
_largestProcess
boolValue
initWithMachServiceName:options:
numberOfRanges
queue
setUnindexed_frames:
substringFromIndex:
.cxx_destruct
reasons
_ss_sequence
addJITImage:size:
bootProgressRegister
exceptionCode0
panicFrames
sharedCacheID
TI,R,N,V_sharedCacheID
_getValueForKey:fromBody:orHeader:
numberWithBool:
_zones
kernelVersionDescription
_largestActiveApp
original
setDateFormat:
T@\"NSArray\",R,N,V_frontmostPids
sharedScheduler
sampleThread:
state
_cpuType
bootSessionUUID
getSyslogForPids:andOptionalSenders:additionalPredicates:
initWithTask:
setObject:forKey:
countByEnumeratingWithState:objects:count:
UTF8String
formatInstructionState:index:
hasPrefix:
initWithPID:options:
numberWithUnsignedShort:
stringWithUTF8String:
hash
push:
writeData:
dealloc
Tr^v,R,N,V_ss_trace_buffer
_thermalNotificationCurrentLevel
capture_absoluteTime
stringForKey:
setSs_sequence:
_frontmostPids
_isSnapshotDisabled
addWaitInfoDesc:count:elSize:
appendFormat:
codeSigningValidationCategory
initWithIdentifier:
_dead_snapshot
acquireJetsamDataWithFlags:
setRequiresNetworkConnectivity:
lookForPattern:
_exceptionCodeCount
iBootVersion
dictionaryForKey:
includeSyslog
isEqualToString:
_bundleID
asyncQueue
problemType
stringByAppendingString:
_audioAssertionState
dataWithJSONObject:options:error:
firstMatchInString:options:range:
instrumentEventsWithAudioAssertionState:visibliltyEndowmentState:
invalidate
T^{dyld_uuid_info_64=Q[16C]},R,N,V_layout
decodeKCDataWithBlock:withTuning:usingCatalog:
filteredArrayUsingPredicate:
rangeOfString:options:
containsObject:
setRemoteObjectInterface:
invalid_images
synchronousRemoteObjectProxyWithErrorHandler:
formatMemoryErrorReport:
instrumentEvents:
localizedDescription
rollSchemaForward:
sortedPids
startWithCallback:
launchAppWith:options:completion:
removeAllObjects
setKernelImages:
setTaskCompleted
TI,N,V_flags
__swift_objectForKeyedSubscript:
TB,N,V_includeSyslog
incidentID
isLowPowerModeEnabled
redacter
useStackshotData:frontmostPids:atTime:machTime:sequence:
createForSubmission:metadata:options:error:writing:
initWithPid:
length
_swiftPanicPatternInfo
isActionable
setInteger:forKey:
osTrain
_jetsamLevel
decode_cpuType
domain
stringWithContentsOfURL:encoding:error:
row
initForPid:process:withReason:exceptionCode:exceptionCodeCount:stackshotFlags:
numberWithUnsignedInt:
$__lazy_storage_$_getReportDate
_layout
TB,R,V_isSnapshotDisabled
crashReporterKey
getMatcherType
resampleUUIDsForTask:usingCatalog:
T^[37c],R,N,V_sharedCacheUuid
_killed_or_suspended_count
arrayWithCapacity:
registerForTaskWithIdentifier:usingQueue:launchHandler:
objectForKey:
setInvalid_images:
sortByAddressAndSetInferredSizes
getVMStatistics
isDeveloperMode
clientWithIdentifier:
initWithFileDescriptor:
isMemberOfClass:
zone
_event_reason
dictionaryWithObjects:forKeys:count:
stringWithFormat:
retain
codeSigningFlags
intValue
alreadyDumpedSuspendedJetsamLogToday
initWithType:
setLocale:
submitTaskRequest:error:
TB,N,V_dead_snapshot
_aleFlag
_isDefaultSharedCache
_reason
unsignedIntValue
TI,R,N,V_layoutImageCount
setJetsamLevel:
descriptionFromCode:
_hexDump:offset:indicator:
characterSetWithCharactersInString:
isEqual:
readDataToEndOfFileAndReturnError:
TQ,R,N,V_sharedCacheSlide
hwModel
setRequiresExternalPower:
transformLines:withDefinitions:body:header:report:error:streamingBlock:
TQ,R,N,V_sharedCacheUnreliableSlidBaseAddress
TQ,R
backtrace
code
dictionaryWithCapacity:
stringByReplacingOccurrencesOfString:withString:
TI,R,N,V_ss_trace_length
dead_snapshot
formatArm32ThreadState:index:
usedImages
executeWithTimeout:Code:
logfile
_flags
getExtraData:
lastObject
bytes
sharedCacheUnreliableSlidBaseAddress
standardUserDefaults
valueForKey:
writeReportBodyWithSectionWriter:
tag
addObjectsFromArray:
respondsToSelector:
TQ,R,N,V_capture_absoluteTime
_capture_absoluteTime
compare:
exceptionCodesDescription
frontmostPids
reduceToTwoSigFigures:
reportNamePrefix
_stackshot_config
layout
omit
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:isSnapshotDead:
class
getFramesForThread:usingCatalog:
numberWithUnsignedLong:
integerForKey:
bugType
ss_trace_length
allObjects
copy
init
sortedArrayUsingDescriptors:
pop
isSnapshotDisabled
longLongValue
productNameVersionBuildString
spindump
substringWithRange:
targetSharedCache:withSlide:atBaseAddress:
formatLastBranchState:index:withImages:
uid
mutableCopy
addImage:address:size:
_event_code
appleInternal
codeSigningID
exceptionCode1
matchesInString:options:range:
acquireStackshot
crashReportBody:
formatArm64ThreadState:index:
resampleTruncatedBacktracesForTask:forThreads:usingCatalog:in:usingSymbolicator:
kernelSlide
_additionalPayload
errorWithDomain:code:userInfo:
getAppleIntelligenceAvailability
isAddressInTargetedCache:
ss_sequence
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:
unsignedLongLongValue
ss_trace_buffer
top
appendNotesTo:
formatX86ThreadState:index:
performSelector:withObject:
setPriority:
isPatternPayloadAvailable
_exceptionCodes
_wiredBytes
addTurnstileInfoDesc:count:elSize:
arrayWithObjects:count:
kernelTextBase
predicateWithFormat:
setSpindump:
stringByTrimmingCharactersInSet:
addCustomField:value:into:
hottestElided
report
reverseObjectEnumerator
setIncludeSyslog:
sharedInstance
sortedArrayUsingSelector:
T@\"NSDictionary\",&,N,V_spindump
value
error
formatFrame:withImages:macosStyle:showBinaryImage:
initWithZoneNames:nameCount:zoneInfo:zoneInfoCount:wiredInfo:wiredInfoCount:
objectAtIndexedSubscript:
addObject:
debugDescription
userAppName
TB,R,N,V_isDefaultSharedCache
_pid
array
zoneInfo
threads
_layoutImageCount
generateLogAtLevel:withBlock:
isKindOfClass:
T@\"NSString\",?,R,C
dateFromString:
initWithKey:ascending:
self
sharedCacheUuid
buildVersion
lastPathComponent
modelCode
seekToOffset:error:
addNotes:
initWithName:reason:exceptionCode:exceptionCodeCount:
levelForFactor:withNamespaceName:
parent
_appName
description
layoutImageCount
setSharedCacheInfo:
formatProbGuardReport:
initWithIncidentID:visibilityEndowmentState:audioAssertionState:
iterateLogsWithOptions:usingBlock:
setLog_path:
Ti,N,V_jetsamLevel
getStackshotData
searchFrame:in:result:
taskRequestForIdentifier:
dispose
conformsToProtocol:
initWithDictionary:
```
