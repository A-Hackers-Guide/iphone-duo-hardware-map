# `/usr/lib/system/libsystem_trace.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 324,912 bytes.

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
C
{os_trace_blob_s=\"\"(?=\"ob_b\"*\"ob_v\"^v\"ob_s\"*\"ob_c\"*)\"ob_len\"I\"ob_size\"I\"ob_maxsize\"I\"ob_flags\"S\"ob_binary\"B}
S
^{os_trace_blob_s=(?=*^v**)IIISB}
[128c]
Q
B
v16@0:8
v32@0:8r^v16Q24
^{?=b4b4C[0C]}
%d
%s
process
INBOX
STRING
YB
Signpost-Allow-Streaming
pubdata
privdata
ring && data
ring && size && data
RTLogBufferCheckStatus
errno
-pc#d#b#-#l#s#w#
/System/Library/
entries
rt_shmem_descriptor
placement_in_logbuffer
procid
Gibps
BUG IN CLIENT OF LIBTRACE: Invalid flags passed
MiB
Process
NSString
procpath
 ( 
/System/Developer/
xcode:text-backtrace
OSLogRTBufferConfig
AMFI
NSData
i16@?0r^{load_command=II}8
__OS_LOG
RTLogRingBufferJoinManaged
transport_ringbuffer.c
Fwd: 
%llu.%01u %s
OS_ACTIVITY_MODE
unknown
os_trace_procmode_t
false
EB
[%d: %s]
BUG IN CLIENT OF LIBTRACE: Too many os_log_t objects
Public
%0.7g
always
.%03ld
Mibps
Enable-Fault-Crashlogs
OS_ACTIVITY_FORMATTER
Invalid mask
%04d-%02d-%02d %02d:%02d:%02d
BUG IN LIBTRACE: Unexpected type
Default-Privacy-Setting
32bits
message_id
BUG IN LIBTRACE: Using oversized messages with unreliable interfaces shouldn't be possible
ring && offset && buffer && callback
paid
buffer
signpostname
mach.errno
operation
com.apple.logd.realtime
RTLogBufferGetResource
Invalid cmd type
ZiB
Supports-Signpost-Introspection
com.apple.libtrace.state.block-list
%lu
Tibps
YiB
liblog_
OS_ACTIVITY_PROPAGATE_MODE
BUG IN LIBTRACE: os log handles are never freed
<decode: missing data>
com.apple.system.logging.prefschanged
Cannot shim OS_LOG_DISABLED to stdout
timezoneDSTflag
payload
builtin
unknown to old reader
/System/Library/Preferences/Logging
Enable-Private-Data
%ld
%f
procuuid
<…>
off
uid
default
timeGMTusec
signpostid
HasFullLogging
Tbps
com.apple.runtime-issues
%sliblog_%s.dylib
shared_memory.c
com.apple.logd
category
v8@?0
no path for address %p
%+05ld
0123456789ABCDEF
0
YES
Debug
Unknown log type
Signpost-Persisted
RTLogBufferIterate
writeIovOnePart
_os_metric_get_bin_count
multichar
com.apple.trace
buffer && base
name
use OS_ACTIVITY_STREAM for configuring streaming.\n
COUNT
disabled
0x%X
BUG IN CLIENT OF LIBTRACE: Cannot force Public over Private
%s/%s/%s.plist
Cannot shim OS_LOG_DEFAULT to stdout
Sensitive
persona_id
<%s instance>
i24@?0r^v8r^v16
offset
live
OS_ACTIVITY_TOOLS_OVERSIZE
OSLogRateLimit
metric->metadata.type == _OS_METRIC_TYPE_HISTOGRAM
BUG IN LIBTRACE: Should start with '%'
Log formatter uncaught exception in [%s]
formatstring
…'
<(null)>
NO
Mbps
kB
Success
(uint64_t)ptr % RTLOG_BUFFER_ALIGN == 0
BUG IN LIBTRACE: Unable to get unique pid
darwin.errno
time_t
stream
Privacy-Enable-Level
DynamicTracing
processImagePath
__CTF
formatoffset
@
mask.
…
uuid_t
Level
Info
none
operator
\n
__TEXT
BUG IN LIBTRACE: Unable to grab boot uuid
small
/usr/lib/system/libsystem_asl.dylib
ring && buffer && callback
com.apple.diagnosticd
atm_diagnostic_config=
OSLogPreferences
%
B24@?0Q8^v16
 %s[%d:%llu] 
%s +0x%x\n
type
BUG IN CLIENT OF LIBTRACE: histogram cannot have greater than 128 bins.
 private
true
bps
%llu %s
TiB
Enable-Oversize-Messages
header->catalog.count < RTLOG_RESOURCE_COUNT
version
CFBundleIdentifier
OSLogClientType
/AppleInternal/Library/Preferences/Logging
data
large
rt_message_type
syscall-unix
_os_metric_get_bins
metric_internal.h
Invalid scalar size
,}
SkipRuntimeIssues
ts
ttl
timeGMTsec
personas_in_oslog
.%09ld
/Library/Preferences/Logging
%u
OSStateCreateStringWithData
RTLogBufferGetHeader
BUG IN CLIENT OF LIBTRACE: Activities are all global objects
 %s
Signpost-Enabled
subsystem
/usr/lib/
(len + 1) == RTLOG_BUFFER_HEADER_MARKER_LENGTH
BUG IN CLIENT OF LIBTRACE: OS_ACTIVITY_CURRENT passed
BUG IN LIBTRACE: Buffer needs free
Default
[%s] 
aid
/usr/local/lib/log/
.dylib
entryData
BUG IN CLIENT OF LIBTRACE: label cannot be NULL
BUG IN CLIENT OF LIBTRACE: custom histogram cannot have greater than (128 / 2) bins.
propagate w/activity
pid
\n\r
RTLogRingBufferReadAt
size >= LOGUTIL_ROUNDUP(sizeof(RTLogBufferHeader), RTLOG_BUFFER_ALIGN)
OS_ACTIVITY_STREAM
OS_ACTIVITY_TOOLS_PRIVACY
metric.c
Critical
RTLogConnectRingBuffer
out_ring_buffer && size_buffer && msg_part_buffer && data_buffer
_os_metric_int64_op_impl
md->type == _OS_METRIC_TYPE_HISTOGRAM
 sz:%d]>
PiB
TTL
%lld
RTLogRingBufferIterate
RTLogBufferGetResourceSize
callback
ACTIVITY_LOG_STDERR
unknown to old emitter
kbps
Persist
%hi
RTLogBufferInitialize
RTLogBufferAddResource
_os_metric_uint64_op_impl
TB
commands
BUG IN LIBTRACE: ulock_wait() failed
com.apple.private.disable-log-mach-ports
Bug in Client: unexpected activity on thread during scope_leave, this will become a hard failure
<mask.%.*s: 
info
Signpost-Scope
seg_count > 0
<decode: bad range for [%.*s] got [offs:%d len:%d within:%d]>
%llu.%02u %s
[sig%s: %s]
muted
Enable
%s/%s.plist
<invalid NS/CF object>
RTLogRingBufferCreateManaged
thread
device_salt
DEFAULT-OPTIONS
v12@?0i8
Once
BUG IN LIBTRACE: Can't use addf() in binary blobs
redactedDescription
%0.16g
BUG IN LIBTRACE: Nope. Invalid stream object version
action
 public
iec-bytes
<decode: can't compose [%.*s]>
/System/Cryptexes/App/System/Library/Preferences/Logging
RTLogRingBufferInit
RTLogRingBufferGetSegmentCount
offset + aligned_size <= header->RTLogBufferSize
OS_ACTIVITY_DT_MODE
, 
BOOL
darwin.mode
B
BUG IN LIBTRACE: ulock_wake() failed
.%06ld
global
subfilters
connection.c
config
v16@?0^v8
RTLogRingBufferIterateFrom
dest
writeIovMessageParts
kern.bootargs
path
sections
_os_metric_double_op_impl
Enable-Fault-Crashlog-Excerpts
%llu
launch_persona_id
timeval
Symptoms
i28@?0[16c]8I16I20I24
RTLogBufferAllocateResource
OS_LOG_FAULT_REPORTS
GiB
Subsystems
uuid
persisted
DATA
Invalid access result
iec-bitrate
PB
Fault
 %s\n
com.apple.diagnosticd.filter
ZB
[%#x: %s]
Thread
bool
bytes
Gbps
[%d: Unknown signal]
B24@?0r*8^v16
com.apple.libtrace
<NSNumber: invalid type>
v16@?0r^{dyld_shared_cache_dylib_text_info=QQQ[16C]*Q}8
CFLOG_FORCE_STDERR
bitrate
Kibps
KiB
 %s[%d:%llx]
com.apple.logd.events
timespec
Error
BUG IN CLIENT OF LIBTRACE: Absurdly large size
0 == RTLogRingBufferCreateManaged( &rt_globals.eventBin[i], placement_in_logbuffer, log_bin_config[i].segment_count, log_bin_config[i].segment_size)
[==========LOGBUFFER==========]
/private/var/db/diagnostics/logd
[%s]
Signpost-Backtraces-Enabled
None
RuntimeIssues
[%s] %s
configureEventBins
metric->metadata.bins > 0
com.apple.os.log.notify
debug
BUG IN CLIENT OF LIBTRACE: don't close random fds
rt_shmem_size
BUG IN CLIENT OF LIBTRACE: A reference to the coder escaped
%hu
oslogbuffer.c
BUG IN LIBTRACE: Invalid metadata buffer size
>
MB
 )
/System/Cryptexes/OS/System/Library/Preferences/Logging
<decode: mask \"%.*s\" is %s>
<xpc object>
timezoneMinutesWest
disable
<private>
[%s:%s]
imagepath
/usr/lib/log/
OSLogCopyFormattedString
kr == KERN_SUCCESS
RTLogRingBufferWriteWithCallback
imageuuid
SCALAR
inherit
ringbuffer.c
RTLogRingBufferGetSegmentSize
darwin.signal
System
DynamicStackTracing
dsc_uuid
medium
NSNumber
ring && callback
RTLogRingBufferWriteBuffer
ring && buffer
timestamp
Libtrace
OBJECT
stream_id
<
Processes
BUG IN CLIENT OF LIBTRACE: Calling the unreliable interfaces on a fault is not supported
Always
logicalExp
B16@?0^{os_log_pref_cache_record_s=III{os_log_options_s=(?={?=CCCCb3b3b3b1b1b2b2b2b1b1b1b2b1b2b1b1b3b1b1}Q)}[0c]}8
quarantined
ring
BUG IN CLIENT OF LIBTRACE: Parent must be OS_ACTIVITY_CURRENT when OS_ACTIVITY_FLAG_NONE_PRESENT is used
GB
EiB
Private
Message
<decode: mismatch for [%.*s] got [
RTSharedMemoryConfigure
timeToLive
BUG IN LIBTRACE: _os_trace_mig_server doesn't handle replies
Re: 
length=%u
kern.bootsessionuuid
BUG IN CLIENT OF LIBTRACE: trying to lock recursively
BUG IN CLIENT OF LIBTRACE: lock not owned by current thread
traceid
builtin:
(null)
Activity for state dumps
failed to read %{public}s: %{darwin.errno}d
invalid property list at %{public}s
System-wide statedump
Statedump too large
Change Mode: %{os_trace_procmode_t}d, Final: %{os_trace_procmode_t}d, Interval: %d, Filter: 0x%x
Timed out get mode error %d
QUARANTINED DUE TO HIGH LOGGING VOLUME
OSLogCoder
OS_os_log
OS_os_activity
OS_os_metric_label
OS_os_metric_dimensions
OS_os_metric_group
OS__os_metric
initWithInt:
longValue
retainCount
unsignedShortValue
_fmt_cmd
_fastCStringContents:
shortValue
encodeWithOSLogCoder:options:maxLength:
floatValue
initWithShort:
lengthOfBytesUsingEncoding:
objCType
timeIntervalSince1970
_ob_pub
_ob_priv
appendBytes:length:
isKindOfClass:
initWithDouble:
_initBlob
doubleValue
initWithBytes:length:
intValue
isNSString__
isProxy
charValue
initWithChar:
isNSDate__
unsignedLongValue
getBytes:maxLength:usedLength:encoding:options:range:remainingRange:
initWithUnsignedLongLong:
initWithLong:
unsignedCharValue
unsignedLongLongValue
_truncated
initWithBytes:length:encoding:
initWithUnsignedShort:
setTruncated
_offset
longLongValue
initWithUnsignedChar:
_mask
_maxsz
_ob
dealloc
_ob_mask
initWithLongLong:
isNSCFConstantString__
initWithFormat:arguments:
setPublic
unsignedIntValue
_privacy_level
initWithUnsignedInt:
length
string
_maskbuf
_written
isNSNumber__
_initialized
```
