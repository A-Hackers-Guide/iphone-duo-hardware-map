# `/usr/lib/system/libsystem_trace.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 324,912 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 41 (Size: 5072)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (22)

- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libmacho.dylib (compatibility version 1.0.0, current version 1040.0.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_m.dylib (compatibility version 1.0.0, current version 3326.40.2)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0)`
- `/usr/lib/system/libsystem_sandbox.dylib (compatibility version 1.0.0, current version 3051.40.81)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, upward)`
- `/usr/lib/system/libunwind.dylib (compatibility version 1.0.0, current version 2200.5.0)`
- `/usr/lib/system/libsystem_symptoms.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libcorecrypto.dylib (compatibility version 1.0.0, current version 2109.40.22, upward)`
- `/usr/lib/system/libsystem_asl.dylib (compatibility version 1.0.0, current version 409.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (7 classes, 1 protocols)

Classes: `OSLogCoder`, `OS__os_metric`, `OS_os_activity`, `OS_os_log`, `OS_os_metric_dimensions`, `OS_os_metric_group`, `OS_os_metric_label`

Protocols: `OSLogCoder`

## Strings (499)

```
^{?=b4b4C[0C]}
S
B
v32@0:8r^v16Q24
^{os_trace_blob_s=(?=*^v**)IIISB}
C
{os_trace_blob_s=\"\"(?=\"ob_b\"*\"ob_v\"^v\"ob_s\"*\"ob_c\"*)\"ob_len\"I\"ob_size\"I\"ob_maxsize\"I\"ob_flags\"S\"ob_binary\"B}
[128c]
Q
v16@0:8
[sig%s: %s]
Private
RTLogRingBufferReadAt
header->catalog.count < RTLOG_RESOURCE_COUNT
.%03ld
Invalid scalar size
builtin
Mbps
<%s instance>
i16@?0r^{load_command=II}8
 public
Tbps
BUG IN CLIENT OF LIBTRACE: Calling the unreliable interfaces on a fault is not supported
buffer && base
buffer
com.apple.diagnosticd
BUG IN CLIENT OF LIBTRACE: Activities are all global objects
…'
metric->metadata.type == _OS_METRIC_TYPE_HISTOGRAM
commands
(uint64_t)ptr % RTLOG_BUFFER_ALIGN == 0
BUG IN LIBTRACE: ulock_wake() failed
no path for address %p
Re: 
%+05ld
PB
Enable
category
RTLogRingBufferInit
RTLogRingBufferGetSegmentCount
formatoffset
BUG IN LIBTRACE: Unable to get unique pid
disable
Tibps
Level
stream_id
OSStateCreateStringWithData
_os_metric_get_bin_count
bps
Symptoms
 %s\n
process
%u
_os_metric_double_op_impl
Signpost-Scope
%s +0x%x\n
quarantined
OS_ACTIVITY_FORMATTER
size >= LOGUTIL_ROUNDUP(sizeof(RTLogBufferHeader), RTLOG_BUFFER_ALIGN)
OS_ACTIVITY_STREAM
ZB
Enable-Oversize-Messages
%s/%s.plist
v8@?0
uuid
Invalid access result
procpath
%hi
RTLogRingBufferCreateManaged
ring && size && data
callback
OS_LOG_FAULT_REPORTS
OSLogClientType
%0.16g
%llu
shared_memory.c
RTLogBufferGetResourceSize
BUG IN CLIENT OF LIBTRACE: label cannot be NULL
md->type == _OS_METRIC_TYPE_HISTOGRAM
SCALAR
MB
com.apple.logd
mach.errno
uuid_t
B
KiB
Persist
subfilters
message_id
version
unknown to old reader
%llu.%02u %s
Kibps
muted
System
 %s[%d:%llu] 
com.apple.runtime-issues
.%06ld
darwin.errno
[%d: Unknown signal]
B24@?0r*8^v16
BUG IN CLIENT OF LIBTRACE: Absurdly large size
rt_shmem_size
/usr/local/lib/log/
ringbuffer.c
RTLogRingBufferWriteWithCallback
BUG IN LIBTRACE: Invalid metadata buffer size
%04d-%02d-%02d %02d:%02d:%02d
os_trace_procmode_t
global
BUG IN LIBTRACE: Can't use addf() in binary blobs
ring && buffer && callback
imagepath
OSLogRateLimit
INBOX
__TEXT
com.apple.trace
ttl
.dylib
RTLogBufferAddResource
paid
traceid
Libtrace
personas_in_oslog
live
(null)
redactedDescription
RTLogBufferInitialize
OS_ACTIVITY_TOOLS_OVERSIZE
/System/Cryptexes/OS/System/Library/Preferences/Logging
Default
Cannot shim OS_LOG_DISABLED to stdout
Signpost-Allow-Streaming
pid
Fwd: 
length=%u
Mibps
/System/Library/Preferences/Logging
none
data
entries
default
com.apple.logd.events
dest
,}
darwin.mode
[%d: %s]
com.apple.diagnosticd.filter
large
/usr/lib/system/libsystem_asl.dylib
0 == RTLogRingBufferCreateManaged( &rt_globals.eventBin[i], placement_in_logbuffer, log_bin_config[i].segment_count, log_bin_config[i].segment_size)
launch_persona_id
 sz:%d]>
com.apple.os.log.notify
 %s[%d:%llx]
Default-Privacy-Setting
RTLogRingBufferIterate
%f
iec-bytes
/AppleInternal/Library/Preferences/Logging
off
ring && offset && buffer && callback
%lld
__OS_LOG
kr == KERN_SUCCESS
BUG IN LIBTRACE: _os_trace_mig_server doesn't handle replies
Invalid mask
MiB
Once
Bug in Client: unexpected activity on thread during scope_leave, this will become a hard failure
BUG IN LIBTRACE: Buffer needs free
<(null)>
<
Fault
Public
uid
NSString
<NSNumber: invalid type>
/usr/lib/log/
formatstring
, 
<…>
…
%s/%s/%s.plist
Enable-Fault-Crashlog-Excerpts
%0.7g
<invalid NS/CF object>
ring && callback
%llu %s
GB
Gibps
kern.bootsessionuuid
RTLogConnectRingBuffer
BUG IN LIBTRACE: ulock_wait() failed
OS_ACTIVITY_DT_MODE
BUG IN CLIENT OF LIBTRACE: histogram cannot have greater than 128 bins.
%d
TB
Success
0x%X
%s
Log formatter uncaught exception in [%s]
timezoneMinutesWest
/private/var/db/diagnostics/logd
Signpost-Enabled
Message
OSLogCopyFormattedString
seg_count > 0
writeIovMessageParts
OS_ACTIVITY_MODE
BUG IN CLIENT OF LIBTRACE: A reference to the coder escaped
timeGMTusec
thread
name
kB
Unknown log type
dsc_uuid
connection.c
offset + aligned_size <= header->RTLogBufferSize
TiB
DEFAULT-OPTIONS
NSData
use OS_ACTIVITY_STREAM for configuring streaming.\n
atm_diagnostic_config=
/Library/Preferences/Logging
privdata
timezoneDSTflag
com.apple.private.disable-log-mach-ports
DynamicStackTracing
timeGMTsec
_os_metric_get_bins
/System/Developer/
Critical
rt_message_type
liblog_
RTLogBufferGetResource
BUG IN LIBTRACE: os log handles are never freed
 private
 )
Enable-Fault-Crashlogs
logicalExp
%lu
RTLogRingBufferWriteBuffer
signpostname
YB
EiB
Error
Always
operation
device_salt
0123456789ABCDEF
mask.
STRING
errno
kbps
stream
[%s]
ring && data
info
Thread
small
placement_in_logbuffer
RTLogRingBufferGetSegmentSize
<decode: can't compose [%.*s]>
/System/Cryptexes/App/System/Library/Preferences/Logging
com.apple.logd.realtime
__CTF
[==========LOGBUFFER==========]
COUNT
false
EB
PiB
operator
[%s] %s
BUG IN LIBTRACE: Should start with '%'
propagate w/activity
Sensitive
Enable-Private-Data
com.apple.libtrace
procid
i28@?0[16c]8I16I20I24
out_ring_buffer && size_buffer && msg_part_buffer && data_buffer
transport_ringbuffer.c
>
RTLogRingBufferJoinManaged
(len + 1) == RTLOG_BUFFER_HEADER_MARKER_LENGTH
BUG IN CLIENT OF LIBTRACE: lock not owned by current thread
signpostid
metric_internal.h
%
<decode: mismatch for [%.*s] got [
unknown to old emitter
HasFullLogging
OSLogPreferences
<decode: mask \"%.*s\" is %s>
Info
Cannot shim OS_LOG_DEFAULT to stdout
 %s
Process
None
timespec
pubdata
[%s] 
medium
\n\r
RTSharedMemoryConfigure
BUG IN LIBTRACE: Unexpected type
OBJECT
bitrate
subsystem
xcode:text-backtrace
v16@?0^v8
sections
<mask.%.*s: 
YiB
com.apple.libtrace.state.block-list
AMFI
%hu
%ld
RTLogBufferGetHeader
procuuid
OS_ACTIVITY_PROPAGATE_MODE
ACTIVITY_LOG_STDERR
<private>
NSNumber
ring
Invalid cmd type
<decode: bad range for [%.*s] got [offs:%d len:%d within:%d]>
BOOL
%llu.%01u %s
disabled
Processes
OS_ACTIVITY_TOOLS_PRIVACY
debug
BUG IN LIBTRACE: Unable to grab boot uuid
type
Supports-Signpost-Introspection
BUG IN CLIENT OF LIBTRACE: Too many os_log_t objects
Signpost-Persisted
/System/Library/
RuntimeIssues
v12@?0i8
/usr/lib/
iec-bitrate
Debug
Signpost-Backtraces-Enabled
B16@?0^{os_log_pref_cache_record_s=III{os_log_options_s=(?={?=CCCCb3b3b3b1b1b2b2b2b1b1b1b2b1b2b1b1b3b1b1}Q)}[0c]}8
OSLogRTBufferConfig
rt_shmem_descriptor
%sliblog_%s.dylib
configureEventBins
ring && buffer
oslogbuffer.c
@
multichar
\n
ts
RTLogBufferIterate
action
metric.c
[%#x: %s]
Privacy-Enable-Level
aid
persona_id
<xpc object>
v16@?0r^{dyld_shared_cache_dylib_text_info=QQQ[16C]*Q}8
_os_metric_uint64_op_impl
Subsystems
TTL
[%s:%s]
DynamicTracing
RTLogBufferAllocateResource
entryData
CFBundleIdentifier
_os_metric_int64_op_impl
unknown
YES
NO
inherit
BUG IN LIBTRACE: Nope. Invalid stream object version
writeIovOnePart
BUG IN CLIENT OF LIBTRACE: OS_ACTIVITY_CURRENT passed
persisted
always
darwin.signal
SkipRuntimeIssues
i24@?0r^v8r^v16
imageuuid
timeToLive
CFLOG_FORCE_STDERR
bool
true
BUG IN LIBTRACE: Using oversized messages with unreliable interfaces shouldn't be possible
config
BUG IN CLIENT OF LIBTRACE: Parent must be OS_ACTIVITY_CURRENT when OS_ACTIVITY_FLAG_NONE_PRESENT is used
offset
BUG IN CLIENT OF LIBTRACE: custom histogram cannot have greater than (128 / 2) bins.
timeval
Gbps
ZiB
 ( 
RTLogBufferCheckStatus
BUG IN CLIENT OF LIBTRACE: trying to lock recursively
metric->metadata.bins > 0
-pc#d#b#-#l#s#w#
processImagePath
32bits
BUG IN CLIENT OF LIBTRACE: Cannot force Public over Private
kern.bootargs
<decode: missing data>
DATA
com.apple.system.logging.prefschanged
payload
path
builtin:
bytes
GiB
B24@?0Q8^v16
BUG IN CLIENT OF LIBTRACE: don't close random fds
RTLogRingBufferIterateFrom
syscall-unix
BUG IN CLIENT OF LIBTRACE: Invalid flags passed
timestamp
.%09ld
0
time_t
invalid property list at %{public}s
System-wide statedump
Statedump too large
Change Mode: %{os_trace_procmode_t}d, Final: %{os_trace_procmode_t}d, Interval: %d, Filter: 0x%x
Timed out get mode error %d
QUARANTINED DUE TO HIGH LOGGING VOLUME
Activity for state dumps
failed to read %{public}s: %{darwin.errno}d
OS_os_metric_group
OS__os_metric
OSLogCoder
OS_os_log
OS_os_activity
OS_os_metric_label
OS_os_metric_dimensions
_truncated
initWithLong:
_maskbuf
_privacy_level
getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
initWithUnsignedChar:
initWithUnsignedLongLong:
initWithUnsignedShort:
isKindOfClass:
_offset
isNSDate__
dealloc
doubleValue
setPublic
string
_mask
initWithBytes:length:encoding:
initWithInt:
initWithShort:
unsignedCharValue
length
lengthOfBytesUsingEncoding:
_fmt_cmd
initWithDouble:
_fastCStringContents:
_ob_mask
charValue
intValue
isNSCFConstantString__
isProxy
encodeWithOSLogCoder:options:maxLength:
_written
floatValue
shortValue
timeIntervalSince1970
unsignedLongValue
_initialized
isNSNumber__
retainCount
unsignedLongLongValue
initWithBytes:length:
initWithUnsignedInt:
setTruncated
_ob
_ob_priv
_initBlob
unsignedShortValue
objCType
unsignedIntValue
_ob_pub
isNSString__
initWithFormat:arguments:
_maxsz
appendBytes:length:
initWithChar:
initWithLongLong:
longLongValue
longValue
```
