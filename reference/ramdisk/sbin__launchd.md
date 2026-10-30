# `/sbin/launchd`

From the upgrade restore ramdisk (141-29011-104.dmg). 639,552 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 4408)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (10)

- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libsandbox.1.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftDarwin.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.apfs.get-dev-by-role</key>
	<true/>
	<key>com.apple.developer.hardened-process</key>
	<true/>
	<key>com.apple.developer.hardened-process.hardened-heap</key>
	<true/>
	<key>com.apple.developer.lockdown-mode.state</key>
	<true/>
	<key>com.apple.private.amfi.can-allow-non-platform</key>
	<true/>
	<key>com.apple.private.delegate-signals</key>
	<true/>
	<key>com.apple.private.endpoint-security.submit.bootstrap</key>
	<true/>
	<key>com.apple.private.iokit.system-nvram-allow</key>
	<true/>
	<key>com.apple.private.kernel.darkboot</key>
	<true/>
	<key>com.apple.private.kernel.system-override</key>
	<true/>
	<key>com.apple.private.persona-mgmt</key>
	<true/>
	<key>com.apple.private.pmap.load-trust-cache</key>
	<array>
		<string>cryptex1.boot.os</string>
		<string>cryptex1.boot.app</string>
		<string>cryptex1.boot.rosetta</string>
		<string>cryptex1.safari-downlevel</string>
		<string>cryptex1.generic</string>
	</array>
	<key>com.apple.private.record_system_event</key>
	<true/>
	<key>com.apple.private.roots-installed-read-write</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.signal-critical-processes</key>
	<true/>
	<key>com.apple.private.security.signal-exempt</key>
	<true/>
	<key>com.apple.private.security.storage.driverkitd</key>
	<true/>
	<key>com.apple.private.security.storage.launchd</key>
	<true/>
	<key>com.apple.private.security.system-mount-authority</key>
	<true/>
	<key>com.apple.private.set-atm-diagnostic-flag</key>
	<true/>
	<key>com.apple.private.shared-region.config</key>
	<true/>
	<key>com.apple.private.spawn-panic-crash-behavior</key>
	<true/>
	<key>com.apple.private.spawn-subsystem-root</key>
	<true/>
	<key>com.apple.private.vfs.allow-low-space-writes</key>
	<true/>
	<key>com.apple.private.vfs.graftdmg</key>
	<true/>
	<key>com.apple.private.vfs.pivot-root</key>
	<true/>
	<key>com.apple.rootless.restricted-block-devices</key>
	<true/>
	<key>com.apple.rootless.storage.early_boot_mount</key>
	<true/>
	<key>com.apple.rootless.volume.Preboot</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
	<key>com.apple.security.script-restrictions</key>
	<true/>
</dict>
</plist>
```

## Objective-C (24 classes, 0 protocols)

Classes: `OS_launch_array`, `OS_launch_attribution_node`, `OS_launch_cache`, `OS_launch_coalition`, `OS_launch_dictionary`, `OS_launch_domain`, `OS_launch_domain_aggregate_io`, `OS_launch_domain_io`, `OS_launch_endpoint`, `OS_launch_event_provider`, `OS_launch_event_realm`, `OS_launch_event_stream`, `OS_launch_event_subscription`, `OS_launch_io`, `OS_launch_log`, `OS_launch_plist`, `OS_launch_service`, `OS_launch_service_static`, `OS_launch_service_stub`, `OS_launch_service_stub_static`, `OS_launch_socket`, `OS_launch_uint64_dictionary`, `_TtC7launchd12SerialLogger`, `_TtC7launchd14SerialLogQueue`

## Strings (2,836)

First 2,500 of 2,836.
```
Invalid enum value on pack: %d\n
Failed to pack event for downcall using ES syscall %d
Failed to submit event using ES syscall %d: %d %s
Is this process entitled properly for submitting events to EndpointSecurity?
Non-system service tried to claim task-special port: %d
Unprivileged caller tried to check into job's endpoints: caller = %s.%d, owner = %s
hw.%s
<endpoint name too long>
launch_kern_credentials_resolve_by_uid(%d) failed
EX_NOHOST
jetsam hard file descriptor limit = %u
interactive
entering bootstrap mode
Failed to deregister daemon notification endpoint '%s': %s
DriverKit
dgram
high bits aslr
unpending launches
SIGABRT
der_vm_iterate_b
AuxiliaryBootstrapper
Could not convert value for OSLogRateLimit to str: %lld
failed to add interest notification
userspace reboot into boot mode not allowed: %s
Dropping coalition notification from unknown source (%llu)
Unknown ProcessType: %s
Shutdown stall event fired with no activations (skipping report)
Could not remove job: error = %d: %s
OS_REASON_DYLD
finish-obliteration
xpc demux succeeded
Unknown key for Boolean: %s
load-jetsam-properties-path
_LimitLoadFromBootarg
</dict>\n
der_decode_utc_time
MultipleInstances
_RecoverOnCrash key: RecoverOnCrashDeadline overflowed converting to ns (%lld)
__TRIFactors
no service, code = %d
v16@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
REMOVE_ALIASED_ENDPOINTS
[
execs = %hu
event triggers = {
mobile
w
comp
extensions cannot run as root
System shutdown
com.apple.xpc.launchd.logq
Unknown string encoding
Queue.h
ContainingBundleID
SLAY_CHILD_DOMAIN
SockFamily
extension removal request finished, sending reply
multiple removals of port entry
com.apple.private.xpc.domain-extension
com.apple.private.xpc.launchd.allowed-coalition-quiesce
%lu = 
instance-specific endpoints = {
The endpoint \"%s\" would shadow a trusted one owned by %s, ignoring
Failed to disable service %s, error=%d - %s
spawn failed
%s.%d sent an invalid request
_AdditionalSubServices
LimitLoadToHosts
ConclaveMemoryLimit
userspace shutdown timed out: %s (%d).%s
multiple attempts to remove service instance
der_validate_array
LimitLoadToSessionType
SecureSocketWithKey
workload-properties-init
obliteration
%lld file logs dropped [in-flight %lld]: %lld os_log_simple logs dropped
Flushing logs before initialization. Early logs may not be written to file.
ThrottleInterval
object, 
%s - 
%s throttled
Too many instances (%d >= %lu : %d), but nothing to slay since all instances are already being removed.
com.apple.private.xpc.launchd.per-user-lookup
No space for special ports: %zu > (%zu - %d)
Missing executable detected. Job: '%s' Executable: '%s'
failed lookup due to non-launching property mismatch: name = %s, requestor = %s.%d
persistent jetsam properties object is invalid
com.apple.private.xpc.allowed-launch-types
SizeLimit
com.apple.private.xpc.launchd.app-server
Missing ProductBuildVersion
IPv4
+ %s
OS_REASON_COREANIMATION
_RoleAccount
Plist preprocessing failed, rejecting
submitted job. ignore execute allowed
LogServiceLifecycle
%s is too large. Ignoring.
com.apple.launchd.calendarinterval
null bootstrap port
removing active service: %s
/var/run/utmpx
Doing boot task
Could not find exception endpoint for service: %s
%s=%s
unix
attractive services = {
load-jetsam-properties
IOMatchLaunchStream
hide = %s
Service does not specify a valid argument array.
The key is ignored, please switch to (Active|Inactive)(Soft|Hard)MemoryLimit
Invalid type (%s) for _ProvenanceData
did not initialize jetsam properties category: %s
failed to process path: %s: %s: %d
Already registered ports
kern.initproc_spawned
protocol = %s
OSLogRateLimit
initialization failure: %s: %s + %llu [%llu][%s]: 0x%llx
endpoints = {
Could not find domain from request: type=%s handle=%lu
EmbeddedMainThreadPriority
v16@?0^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}8
%s coalition = {
Could not submit extension %s: %d - %s
RebootOnExitCode
PID size for exit reason mismatch
attempt to watch unmanaged endpoint
Failed to %s endpoint '%s' as throttled
HopefullyExitsLast
%s (%s)
der_vm_data_from_context
Default
XPC_UNLOCK_TIMESTAMP
Could not opt into %d MB Jetsam high watermark: %d: %s
lazy initialization of endpoint on active service
parent
validate_V0
LAUNCH_KEY_UNSETUSERENVIRONMENT is only valid for user domains.
unhandled opcode
Old socket path is not a socket; path=%s
Could not cleanly tear down userspace. Will force a full hardware reboot. (%s)
last exit code = (extension watchdogged)
persistent object size is %zu bytes
Warning
Invalid get_port() flags
CheckedAllocationsPosixSpawnFlagsGlobal
pushBackMulti
Wait
com.apple.private.spawn-driver
Unable to copy merged spawn constraints
not running
XPC API Misuse: %s
/System/Library/xpc/foreground_user_endpoints.plist
Ignoring launch events for a bundle
/Library/LaunchAgents/
Invalid type for environment variable value (env/type): %s/%s
.pluginkit
managed
libdispatch bug: Unknown send-right
is from a cryptex
Unable to stat %s [%d:%s]
node name = %s
RELEASE
HardPortLimit
read resource usage
jetsam properties object is not an array
ExecuteAllowed
_LimitLoadFromVariant
QueueDirectories
%s = 
inactive domain is not shutting down
service start (%s)
Failed to activate endpoint for legacy check-in. Please just don't use this API: %s
endpoint deallocation while still being watched
Executable not in bundle
setting launch watchdog timeout to %u secs from overlay
system shutdown has begun
A memory allocation has failed
attempted to petrify a service twice
service state: %s
last exit code = %d: %s
jetsam hard port limit = %u
peeking at message: seqno = %u, pid = %d
Failed to create the implicit endpoint
keep-alive
services
Endpoint has been activated through legacy launch(3) APIs. Please switch to XPC or bootstrap_check_in(): %s
Interactive
security.mac.amfi.developer_mode_status
Please use JetsamProperties instead.
Size limit for Datastore entry not specified: %s
Failed to respawn: %d: %s
System reboot
Assuming EnablePressuredExit=false given EnableTransactions=false.
removing inactive unmanaged service: %s
attempt-unload-protected
array decoding failure
attempted to petrify a service that hasn't been animated
NSExtension
_AdditionalProperties
Found lingering process: %d (%s)
kpersona_find_by_type() failed with ret %d errno %d - %s
-s
Failed to fstatat() secure socket path: path=%s, error=%s (%d)
Overlay plist is missing.
%s => (timeout = %hus, consecutive crash count = %hu/%hu)
checked allocations = %s (queried = %s)
underflow of active count during activate
Sandbox violation: endpoint = %s
Domain creation failed: %d %s
/sbin/launchd
resolving its username/groupname failed
Extension
%s is out of range, ignoring
Shutting the system down has taken too long. launchd is rebooting\n(or halting) the system now. Any processes that are still running\nwill be abandoned to the mercy of the kernel.\n
session uid = %d
in initial on-demand
skipping over obliterator: %s
session_uid
MallocAggressiveMadvise
caller = %s.%d, event = %d
/usr/lib/system/libsystem_trace.dylib
SIGTRAP
xpc demux failed
XPC bundles can't have KeepAlive, they can't even set it as a plist key, how did we get here?
arm
Path not allowed in target domain: type = %s, path = %s error = %d: %s, origin = %s
(no daemon cache)
OS_REASON_TCC
boot
unknown number encoding
number too large
BundleProgram
Could not convert value for MallocMaxMagazines to str: %lld
SystemRoots
The launch(3) APIs cannot be used to check in MultipleInstance endpoints.
attempt to drain active endpoint
RemoteServices
UNINITIALIZED
Cannot setup an event for proxyless spawns!
added unmanaged active
%a %b %d %T %Y %Z
HOLD_ON
immediate reason = %s
%s => {
spawn-constraint
OS_REASON_WATCHKIT
kern.osrelease
PersonaEnterprise
RunAtLoad
kill
will-spawn received on active service
refusing to persist enabled/disabled state for '%s' as it contains illegal XML character '<'
Could not make system logger socket world-writable: error = %d: %s
Program
ProcessType
}
XXXXXXXX%s=%llx
.%lu
obliterating semi-active service: %s
data-protection
launchd_upward_connections_support=
SandboxContainer
it has a control port set
OS_REASON_ENDPOINTSECURITY
rec_execcnt
subcode
+ (unlimited)
SetUserEnvironment
unknown IPC
UserName
XPC Service Info.plist is missing XPCService dictionary
Service specifies both standard out file descriptor and path.
SOURCE_ATTACH
pended spawn reason '%s': redriving controller attach request
Bootout error: %d
death port = 0x%x
set
HardResourceLimits
Cannot abandon languishing service: %d: %s
jetsam thread limit = %d
removing job: caller = %s
managed = %s
_NeedsSystemThreadGroup
process-info-pidinfo
SIGPROF
undefined boot task %s
_POSIXSpawnTelemetryPageIn not allowed
%s/
envvar
domain exec event
%s/%s/%s
Log level out of bounds for system state conversion: %d
required boot task executable not found
attempt to cancel notification on non-existent port entry
_imagePathToInfo
Unknown service
failed to boot out inactive service during obliteration; endpoint event
port = 0x%x%s
MallocStackLogging
%s failed: conclave id too long
Secure socket path is not a socket; path=%s
incomplete work
pid
controller attached, spawning
cache
OS_REASON_REPORTCRASH
AppExtensions
ui focal
Self
StandardOutPath
Service tried to claim home screen from: %s
com.apple.private.xpc.launchd.app-state-manager
pending submissions = {
COMMITTED
false
xpcservice
bundle cache = 
DisallowAllLookups is not supported for non-System services.
_BTMItemUUID
Non-entitled process tried to control service \"%s\": %s.%d
Application
all services read
 %s
invalid client reply port %d
data
CPUType
CheckedAllocations
disallow all lookups
uncorked
signal service
sandbox-container
draining message: id = 0x%x
caller failed %s sandbox check on path %s
Version
Restore environment starting.
PATH
path
service-type
configurable
force
CPUMonitorPercentage is out of range, ignoring
com.apple.private.xpc.launchd.event-monitor
com.apple.private.xpc.launchd.allowed-complete-urgent-log-submission
sequence packet
program
_dirty
domain already initialized
domain shutdown
bundle id = %s
uncorking exec source upfront
job-handle
tzinit
JETSAM_REASON_MEMORY_IDLE_EXIT
String contains an embedded NUL
Accessibility
managed-lwcr
deferring exec source uncork
Booting non-external volume, skipping boot-task: %s
Skipping setting up shared memory with cache loader
%s: exited successfully, removing
launch_max_exit_timeout=
recursivelyValidateEntitlements
XPC_USERSPACE_REBOOT_TO_BOOT_MODE
dictionary, 
creator
uncorking exec source for disposal
Skipping boot-task
ipc: caller = %s.%d, subsystem = %d, routine = %d, %s
TaskSpecialPort
Socket entry is not a dictionary. Skipping: %s
MemoryLock
SIGILL
_launch_log_format failed\n
Bogus TaskSpecialPort number: %d
SupplementalUserPaths
NumberOfFiles
%s is not an int, ignoring
(invalid)
reason
teardown of process-scoped services after host exited
disk will be searched for uncached services
mount-phase-2
Panicking in 3 seconds.
Cannot set boot-mode after it has been committed: (%s, %s)
(null)
InternalOnly
system app
marked
sparc
Service did not exit %u seconds after SIGKILL.
going into initial on-demand mode for a multiuser device
Loading Cryptex overlay plist from: %s
launch already in progress
its working directory has been overridden
Obliterator task exited: %s
resetting service: %s
 (development)
failed to validate remapped services header: %d
persistent services header size is less than header size
OSLogClientType
SanitizersAllocationTracesDurationInSeconds=172800
system support
cannot spawn: service is throttled
EX_NOUSER
enter kdp before kill
Endpoint \"%s\" tried to steal host %s port (%d) from \"%s\"
Could not spawn dedicated inetd instance: %d: %s
_AbandonCoalition
canceling old domain attach request to %s
uniqueid = %llu
restoring %zu persistent services
XPC_SERVICES_UNAVAILABLE=1
libdispatch bug: Unknown receive-right
Query cannot be satisfied
Unsupported type for index %lu of _LimitLoadToDeviceTree
failed to read known factors plist from %s: %d
speculatively converting service to spawned, pid=%d
Service tried to register a port for an endpoint declared in its launchd.plist(5): service = %s, endpoint = %s
Unable to record system event. Result: %d errno: %d Message: %s
Killing sender of bogus IPC message: %s.%d
der_vm_execute_match_string_prefix
found multiple jetsam property plists for category %s
completed urgent log submission for %s; pid = %d, version = %d, rtt = %llus
auto-completing urgent log submission for pid = %d, version = %d
SanitizersAllocationTraces
exited with exit reason (namespace: %d code: 0x%llx) - %s
cannot reset service active endpoints: %s
SIGURG
<dict>\n
optional cannot be created with NULL value
SystemXPCService
INIT
voluntary exit timeout = %u
domain disposal while still in the children list
mdns
key-value pair contains extra elements
_manufacturingCallback
Service was sent unexpected signal: %s
could not set create %s: %s
ElideRoleAccountSetupPathPrefixes
launchd_proxyless_spawn=
RequireDomainBinding
XPC_SERVICE_NAME
Bootstrap
userspace reboot
SubmitJob
OS_REASON_OBJC
keybag
Can't create PID domain for PID 0
pending lookup during user switch: name = %s, requestor = %s[%d]
com.apple.launchd.helper
unable to decode value size for key-value pair
deallocation of active service
shutdown timeout
Device unlocked %qus ago
set dyld environment variable
instance creation failed: %d %s
Entitlements element not allowed
Could not get path for service bundle.
kern.osproductversion
, time-to-relaunch: %ums
pending spawn, service not yet activated: %s
%s:
Boot task failed: %s
Invalid type for event (event/type): %s/%s
%s is already set, skipping
couldn't handoff domain IO, asynced away
Failure info has no line number.
select-boot-mode
cpu
Failed to stat() socket directory path: path=%s, error=%s (%d)
Failed to basename_r() a socket path: path=%s, error=%s (%d)
Version4
service exceeded successive crash limit. launch will be throttled
controller-supplied environment = {
abandon process group
inherited
no bootargs string
%s/%s
com.apple.xpc.launchd.xsc.plist_key
unsupported cached entry type %d
run interval = %u seconds
conclave = %s
system
NoExcResourceDuringAudio
/System/Library/LaunchDaemons/com.apple.jetsamproperties
port
abandoning
environment = {
OS_REASON_EXEC
Could not opt into Always-On VPN: %d: %s
binpref
endpoint deallocation without cancellation
_RecoverOnCrash key: RecoverOnCrashCount invalid value. Ignoring.
Unexpected shutdown transition %s -> %s
tcp
type
umask = %o
Expected string for a variant, got %s
job-state
results
%s: urgent log submission key already in stats: 0x%llx
MTESystemWidePreflight
scheduling cleanup in %llu sec after sending %s
failed to remove inactive service
failed activation: name = %s, flags = 0x%llx, requestor = %s[%d], error = %d: %s
PerformInRestore
misfired notification: no-senders
DOMAIN_DEACTIVATE
xpcservice-dict
forks = %hu
force-enabled
mach-register
kern.workload_config
gathered %zu jetsam property overlays to persist into %s
waiting for boot-task %s with pid %d
Retaining, but not starting, service %s
SanitizersAllocationTraces=tagged
SockPassive
os-reason-ns
Could not unlink previous system logger socket: error = %d: %s
EXAppExtensionAttributes
StandardInPath
CPUMonitorInterval
Failed to fchownat() a socket: path=%s, uid=%d, gid=%d, error=%s (%d)
CONFIGURED
, ran for %qums
%s/%lu
_LimitLoadFromClarityMode
Lingering coalition: %llu (%s)
com.apple.xpc.launchd.ioq
bootout-error
DYLD_
urgent log submission
draining messages from %s
jetsam address limit = %llu
committing to system shutdown
name
Active user login, initiated by: %s[%d]
monitor_id
CFBundleIdentifier
reaped
LOGNAME
Cannot remove old socket path; UIDs mismatch: socket owner=%d, path=%d
jetsam
LimitLoadFromBootModes
iteration over a non-iterable type
SandboxFlags
SandboxProfile
ThreadLimit
passive = %s
%s: caller = %s, value = 0x%llx
%04d-%02d-%02d %02d:%02d:%02d.%06d
checked-allocations
launchd_log_serial=
launchd_sync_interval=
Improper type for _RecoverOnCrash key: %s
Unable to unpack argv
Service tried to %s global environment variable with reserved name: %s
Could not neuter bootstrap port: 0x%x
WILL_SPAWN
system domain deallocated
creator euid = %d
externally-hosted endpoints = {
OS_REASON_LIBXPC
unable to decode value tag for key-value pair
domain = %s
CSIdentityOverride
WaitForDebugger
Unable to reload kern.osversion: %d
%#8x %-4u %12s  %s
Too many sockets for name \"%s\". Some will be skipped.
no client port found
Rejected invalid request.
%d: [
EventMonitor
SuccessfulExit
_infoPlist
Attempting to select a data value from a non-data DER object
network-outbound
%8s %6s \t%s
bundle path = %s
%s initiated by: %s
_PanicOnCrash
_serviceBundles
exited
service-ctl-reply-port
Could not reap abandoned service instance: %d: %s
event monitor
OS_REASON_SIGNAL
launch_service_stubs_disabled=
Background
DisableASLR
KnownFactors
FairPlay decryption failed on binary.
powerpc64
keepalive
login
job-creation
_InitialSystemSupport
JetsamProperties plist is malformed - missing Version4 dictionary
EX_PROTOCOL
could not get audit token for service (PID %d): %d: %s
exclaves_boot failed: %d
Invalid type given for bootstrap path sanitization
SIGKILL
remaining_active_service
v24@?0r*8@16
pending spawn, domain in on-demand-only mode: %s
__TEXT
com.apple.
Unknown key for dictionary: %s
Failed to open() socket directory: path=%s, error=%s (%d)
CANCEL_DEATH_SOURCE
DYLD_PRINT_BINDINGS
Failure info has no image UUID.
low priority background i/o
XPC_FLAGS=0x0000000000000000
DomainInternal
SockPathName
(animating)
canceling old global attach request to %s
termination-state
successive crashes = %u
Failed to resolve BundlePath: error=%s: %d, caller=%s
Invalid CPU type value type specified: %s
daemon
Calling into AMFI to enable REM.
sub-sequence size is larger than sequence size
trial factors reload initiated by %s[%d]
%s by %s[%d] for %s succeeded (%d: %s)
IPv4v6
PID
out-of-order spawn event received
Unable to find boot task block for: %s
failure to remove semi-active service
service removal (%s)
Invalid type for a LaunchEvent (stream/name/type): %s/%s/%s
no requestor found for token %llu
boot task %s is not a dictionary
DisableAllMemoryLimit
Successfully spawned %s[%d] because %s
Failure info has no PC.
retain only = %s
usermanagerd
dictionary keys are not sorted or not unique
v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
invalid syscall mask key: %s (%i)
spawning %zu deferred services
sanitizers
gathered %zu services to persist into %s
after the userspace pivot & reboot, os_variant_is_basesystem() should not be true
caller failed file-write-create sandbox check on grand parent directory %s
JetsamProperties plist is malformed
endpoint destination = %s
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
DYLD_PRINT_OPTS
uncorking exec source after service init
disable
targetpid
_VoluntaryExitTimeOut
Override
no EXC_RESOURCE during audio
Deactivated abandoned endpoint: %s
Rebooting now, so the finish-obliteration boot task can clean things up.
Error during cryptex termination: %d - %s
Unknown service type. flags: %llx
_RecoverOnCrash key: RecoverOnCrashDeadline invalid. Ignoring.
Service cannot reset: active unmanaged endpoints
names
get user context
OS_REASON_GUARD
launchd_automation=
hard reboot
No matching personas of type %d uid %d, found %zu
Queried %zu attributed services: caller=%s[%d], service=%s
B24@?0Q8^v16
com.apple.private.xpc.allowed-get-service-name
%f
service has crashed into the shared cache area
code
Could not create copy of service: %d: %s
exception
request
EmbeddedHomeScreen
Socket's service points to a non-existent executable. The application firewall will not work with this service.
could not chown mobile/mobile %s: %s
der_vm_execute_select_longest_matching_key
HardFileDescriptorLimit
com.apple.private.xpc.cryptex.submit
bundle-id
EX_NOPERM
Failed to kill extension. It may linger forever: %d: %s
ContainingBundleVersion
MallocMaxMagazines
EX_SOFTWARE
extension attempting to exit cleanly
exponential throttling
domain print
missing token in request from pid %d
dictionary key is not a valid string
Sockets
enable
alias endpoint given to endpoint interface
attempt to ignore endpoint that is already ignored
v8@?0
%s =>
failed to validate services header: %d
RequireRun
it set an io priority
_ResourceCoalition
supports idle hysteresis
platform binary
Attempt to re-bootstrap service from different path, will use existing: service = %s, existing = %s, conflicting = %s
file-write-unlink
SIGTERMed
abandoned xpcproxy before exec
Failed to register daemon notification endpoint '%s': %s
created the implicit endpoint upfront
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">
HardKqWorkloopLimit
inherited environment = {
bringup time = %llu ms
hw.osenvironment
Failed to fchown() secure socket directory: path=%s, uid=%d, gid=%d, error=%s (%d)
pended nondemand spawn = %s
empty boot-mode name given
Failed to bind() a socket: path=%s, error=%s (%d)
%s%s
com.apple.private.xpc.cryptex.terminate
Lean Testing Environment starting.
vproc not allowed by caller %s
launch only once
Failed to bootstrap path: path = %s, error = %d: %s
#IfFeatureFlagDisabled
_SandboxContainer
0
XPC_IN_REM_DEVELOPMENT
Could not convert value for OSLogClientType to str: %lld
%s: name = %s, 
Terminating with cryptex %s, caller = %s[%d]
Unknown boolean encoding
ClarityUI
interval event: domain response: %d
inferred program
/System/Library/DeveloperModeLaunchDaemons/
Tried to set an unknown task-special port: %s
.plist
denying spawn, domain shutting down: %s
instance overrides spawn constraint must be a dictionary
SIGTERM
Malformed boot-task (missing block key): %s
Rejected bogus request: %d: %s
launchd_force_data_status=
/usr/local/share/launchd-disable-memory-limits
job state = %s
rss
_UIApplicationMain
com.apple.private.xpc.launchd.obliterator
SockType
pc
exiting bootstrap mode
value
timestamp
PathState
v24@?0r*8^{_launch_service_stats_s=IIII*[0{_launch_service_stats_record_s=^vQQiICQIIISIi}]}16
bootout
Cannot look up instances for shared endpoints.
JETSAM_REASON_MEMORY_PERPROCESSLIMIT
Invalid environment[%zd]: %s
boot task failure: %s
resolving its UID failed
Nice
Failed to dirname_r() socket directory path: path=%s, error=%s (%d)
failed to validate known factors plist from %s: %s: %d
enable-transactions
Failed to create a job monitor. error = %d: %s
OS_REASON_FOUNDATION
init_featureflags
com.apple.private.xpc.launchd.service-stats
BoundInterface
%s,
failed to get the code signing identity for a boot-task (%s, %s) errno: %d
\"%s\" exited with signal = %s
der_vm_execute_select_index
stream
jetsamproperties category = %s
it is being debugged
could not open %s: %s
Caller specified a plist with bad ownership/permissions: path = %s, caller = %s[%d]
starting obliteration
Feature flag string must have domain/feature format: %s
JETSAM_REASON_MEMORY_HIGHWATER
uses proxy = %s
could not get unique pid
EX_USAGE
speculatively converted service to spawned with PID %d, but the PID is %d
disable service
start service (%s)
properties
Missing conditions
system-wide preflight
Supplied value (%lld) for _LaunchType key not allowed
Found XPCService bundle by executable: %s
PETRIFIED
on-demand count = %d
failed to serialize persistent object: %p
Unable to apply LWCR (spawn constraint) - %d %s
invalid xpaths type
AbortOnUnknownIPC
/var/run/syslog
EXITED
Ignoring a request to unset ondemand
SIGTTOU
LogToFlatFile
v16@?0^{?=[2^{_launch_dictionary_s}]I*}8
xpcproxy exited due to exit(%d)
denied attach request from %s - missing entitlement %s
managedby_services = {
working directory = %s
.%s
response
/System/Library/xpc/WorkloadProperties.plist
FileSize
com.apple.xpc.launchd.xsc.container_id
%s spawned with pid %d
binary order preference = {
resolved uid = %d
Removing unexpected non-dynamic endpoint: %s
Obliteration
RequireSuccess
EnvironmentVariables
ShutdownMonitor
posix_spawn(%s) failed
OS_REASON_METAL
Got first unlock unregistering for AKS events
%s is being activated by a mismatched domain %s. Managed:%d.
XPC_NULL_BOOTSTRAP=1
%s.%s
PanicOnCrashDeadline
non-ui
UnsetUserEnvironment
SessionCreate
com.apple.private.xpc.launchd.allow-submit-launch-angels
already handled failed init, ignoring
service bootstrap (%s, io flags=%#llx, eval flags=%#llx)
load mounted jetsam properties initiated by %s: %s
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Binaries/libxpc_executables/install/Symbols/launchd
Angel
EX_CANTCREAT
monitor
spawn reason filter = %s
persistent resource coalition = %s
System session daemon must not initiate XPC to the User session: endpoint = %s
hardened-ipc = 1
Unknown key for string: %s
nano-allocator
in-progress bootstraps = %hu
Caller tried to check into a named job: %s
XPC_FLAGS=0x%llx
Small
CACHE INVARIANT VIOLATED: %s | %s != %s
68k
system shutdown
instance = %s, 
SetResourceLimits
stream = %s
device-recovery
Policies
failed to add extension %s: %d - %s
/usr/lib/system/libsystem_notify.dylib
AllowCrash
string_prefix_allowed_iterate
Bug in libxpc: mach_port_construct() failed
Global
Shutdown already started: %s
No PATH environment variable set. The application firewall will not work with this service.
sysstatuscheck
key length is invalid
provides events
Invalid special port[%zd]: %d
setup unix domain socket
redriving pending stop
An extension-removal request is already in flight; chaining
_HighBitsASLR
Please remove it.
UIKitApplication:
service bundles => 
max_task_pmem
\t<false/>\n
wheel
SERVICE CACHE DELETE UNEXPECTEDLY DELAYED: %s replaced: %s by %s, %s by %s
service is already a zombie
service enumeration
entering ondemand mode
non-launching = 1
%d.%d
shell
%5d %10d   %-25s   %s
multicast group = %s
justdoit
]
_ThrottleInterval set to zero. You're not that important. Ignoring.
NumberOfProcesses
failed to create notification port for AKS
inetd-compatible service with no sockets.
launch watchdog timeout = (globally disabled)
+ %d MB
framework cache = 
ConsecutiveCrashCount
LaunchOnlyOnce
ThrottleInterval set to zero. You're not that important. Ignoring.
ActiveSoftMemoryLimit
com.apple.private.xpc.launchd.job-manager
XPC_USERSPACE_REBOOTED
checked allocations reason = %s
has spawn constraint
couldn't find domain to attach to %s, error %d - %s
Event stream %s is already monitored by %s, ignoring
capacity
mount-phase-1
posix_spawn(): %d: %s
XPCService
Unknown key for integer: %s
An empty dictionary needs to be used as the value for %s.
Unknown DER entitlements encoding
Service: %s has leaked pended requests
LimitLoadToHardware
Unknown property %s for PublishesEvents
EnergyEfficiencyMode
Will be calling reboot(2) with flags: 0x%x
com.apple.keyboard-service
OS_REASON_ANALYTICS
/private/var/db/com.apple.xpc.launchd
AssociatedBundleIdentifiers
AlternateSystemApplication:
com.apple.private.xpc.launchd.reboot
SockPathOwner
Exponential throttling is in effect for %llu seconds.
spawn constraint
unset domain environment
token
EXExtensionPointIdentifier
XPC_FLAGS
LD_LIBRARY_PATH
background
job not found, returning ENOSERVICE to %d with manual pipe reply
services[%zu] is missing or has invalid plist key
attempt to remove non-existent server port
hw.jetsam_properties_product_type
EX Extension Info.plist missing EXExtensionPointIdentifier
_ExponentialThrottling
Could not set string argument for key: %s
The %s key is no longer respected. %s
WatchPaths
service name = %s
Setting sysctl kern.darkboot to %u
could not find active service for lookup: pid = %d, name = %s
Missing program
service not running, not stopping
exited due to exit(%d)
Start job failed: service = %s, error = %d: %s
services[%zu] is not a dictionary
finish-demo-restore
RamDisk
xpc event
last exit reason = %s
crash behavior = %x
Non-system service tried to claim host-special port: %d: %s
service = %s
(signal info malformed)
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
Message buffer was shorter than mach_msg_header
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Sources/libxpc_executables/launchd/service_create.c
NSExtensionPointIdentifier
persist-to-boot-mode
could not signal service for %s: %d: %s
exclaves-boot
memlock
fsck
fixup-mobile-tmp
uuids
com.apple.xpc.launchd.unmanaged.%s.%d
boot-mode set by sysctl: %s
ipc (socket)
process exited in a dirty state
jetsam memory limit (active, %s) = %d MB
rootport
SIGSTOP
exists()
it set a non standard umask
com.apple.private.xpc.launchd.service-hold
kern.willshutdown
EX_NOINPUT
extension timed out trying to exit; killing
last terminating signal = %s
multiple instances = %s
ResolveProgramIdentifier
%s by %s[%d] for %s failed (%d: %s)
Unknown socket key %s
spawn completed after a speculative conversion
activation of deactivated domain
subscriber-pid
SIGUSR1
launchd_sudden_shutdown=
The %s key is not yet implemented. %s
%s.%llu
AppleKeyStore
Coalition Cache Evicted: %s [%llu]
 | 
%s%s%s
creator = %s[%d]
SIGQUIT
UNPEND_REQUESTS
LaunchDaemons
datagram
argv
com.apple.xpc.launchd.domain.pid
OS_REASON_SETTINGS
on-system-volume
OK
_LaunchWatchdogTimeOut
WRITE_DISABLED
DYLD_PRINT_DOFS
socket deallocated while still active
unmanaged service deactivated with active dynamic endpoints
set domain environment
JetsamProperties not loaded
GetJob
reload-error
pid-local endpoints = {
pid-version
OS_REASON_HANGTRACER
devicerecoverytool
launchd_log_verbose_meta_limit=
der_decode_string
Quiescing queues
CFBundleVersion
proxy started suspended = %s
unlimited
monitor = %s
diagnostics
Failed to fchmodat() a socket: path=%s, mode=%o, error=%s (%d)
ipv4
nano allocator
ps telemetry page-in
system is in sudden shutdown mode. All processes will be SIGKILLed immediately.
LAUNCH_KEY_SETUSERENVIRONMENT is only valid for user domains.
UseGuardMalloc
System
com.apple.private.xpc.launchd.reboot-pivot-root
%lu
EX_TEMPFAIL
control
exponential throttling grace limit = %u
dataless file mode
Service attempted to %s environment variable with reserved name: %s
WAITING_ON_SHUTDOWN_STALL_REPORT
out
container id = %s
which
Failed to statfs(\"/\"): %d: %s
The endpoint name %s is too long to support some features
XPCServiceEndpointPort
reset = %s
LowPriorityBackgroundIO
checked allocations crashed
attempting to re-add an endpoint into service
origin
GroupName
_objectForActiveContext
unknown
shared region config flags = 0x%x
Endpoint with unexpected domain type \"%s\"
lookup-handle
XPCServiceEndpointNonLaunching
Attempting to select an integer value from a non-integer DER object
mode = %o
TCP
ports
force-kill
boot task has no program
Attempt to share port-destroyed. Ignoring.
StartCalendarInterval
attempt to ignore socket that is already ignored
no name, failing
enabled
uninitialized
_ExperimentalNonLaunching
Invalid value for DeveloperTools: %s
(not running)
cannot reset service: active instance endpoints: %s
mach-cross-domain-lookup
SyncInterval
plist
Debug
successful exit
trial factors = {
READY_FOR_REBOOT
event publisher
aborting trampoline
inetd-compatible
BinaryOrderPreference
%s not permitted to be set on non-submitted jobs
Invalid type for a Datastores entry, should be a dictionary (key/type): %s/%s
after crash
IOGeneralInterest
Unable to open %s [%d:%s]
filesystem mount
reslide shared cache
XPCService must be dictionary
ServiceType
skipping successive crash reset
instances = {
port has message from obliterator or kernel
System shutdown initiated by kernel - launchd got a SIGTERM
OS_REASON_SPRINGBOARD
/private/%s
DisableReslide
userspace shutdown timed out: %s
owner uid = %u
trampolined = %s
pending spawn, service not yet quiesced: %s
failed to boot out inactive service during obliteration; socket event
keepalive = %s
can not find service for caller pid %d
additional-properties
xpcproxy could not exec: %d: %s
OS_REASON_CODESIGNING
dictionary decoding failure
, 
MaterializeDatalessFiles
DYLD_PRINT_
spawn scheduled
running
Could not find and/or execute program specified by service: %d: %s: %s
(infinity)
lwcr
_LimitLoadFromDeviceTree
Crashed
com.apple.private.xpc.unauthenticated-bless
panic on consecutive crashes (%zd)
failed to unset env: XPC_USERSPACE_REBOOT_TO_BOOT_MODE: %d
Did not import service from caller: path = %s, caller = %s[%d], error = %d: %s
<dict/>\n
App
reqs
Not calling into AMFI to enable REM.
LAUNCH_KEY_SINGLEUSER never did anything anyway.
Root node of launchd.plist is not a dictionary.
ProductVersion
active = %s
active count = %d
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Sources/libxpc_executables/launchd/domain.c
cached daemons = {
SIGXFSZ
post-upgrade
SockNodeName
non-ipc demand
services = {
der_decode_next
extension is being debugged; not timing out exit
default environment = {
StartOnMount
interval
Program specified by service does not contain one of the requested architectures: %s
trial factors memory limit = %d MB
shutting down
Cannot safely abandon service instance. Leaving it to languish. This may lead to deadlocks.
_StandardErrorFd
SockServiceName
attempt to launch while in penalty box
supports pressured exit
RemoveJob
SIGCHLD
Unable to unpack stdout
xpc bundle
Submit job failed: service = %s, error = %d: %s
Failed to import key SpawnConstraint - %d: %s
com.apple.xpc.launchd.xsc.sandbox_profile
socket deallocated while still in service list
disclaim responsibility
Could not import service from caller: caller = %s[%d], job is not a dictionary
Could not find job with label %s
Unknown numeric string encoding
_UrgentLogSubmission
service disposal while still in list
SystemApp
Failed to resolve LaunchAngel: error=%s: %d, caller=%s
DaemonNotifications requires a valid _Conclave
WAITING_ON_COALITIONS
environment
denying spawn, invalid reason (%d) for PID domain service: %s
SupplementalPaths
SentinelA
v20@?0^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1b1b1}}8i16
%s|%s
req_pid
</plist>\n
Operating in pure on-demand mode. Ignoring events
MachService endpoint name specified was same as implicitly created endpoint: %s
Instances
com.apple.private.xpc.aux-bootstrap
com.apple.private.xpc.smappservice.update
bootstrap-error
(no framework cache)
__OSINSTALL_ENVIRONMENT
Conflicting request: resliding disabled, but requesting a shared cache reslide. No reslide will be performed.
Service plist has an empty label.
CPU
Clamping socket path mode %o to %o
WiredMemoryLimit
CoreEntitlements: Couldn't iterate over DER entitlements\n
kernel
attempting to enter REM%s
service disposal while in parent instance list
DisallowAllLookups
[%s]: %s\n
label
Block
/System/Library/UserManagement/com.apple.xpc.launchd.personas.plist
DisabledInSafeBoot
com.apple.private.xpc.launchd.setenv-pid-domain
%s spawn failed: %d: %s
obliterating active service: %s
client-port
integer_allowed_iterate
Feature flag string must not have multiple '/' separators: %s
failed to create shmem
(dead-on-arrival)
der_validate_dictionary
Managed
cid
extension is being stopped
failed lookup
kern.maxprocperuid
variant
shmem
der_decode_number
LogicalWritesLimit
com.apple.private.xpc.domain-extension.proxy
No MRM cache found
enable checked allocations
invalid syscall mask value at index: %zu  (%i)
its binary is missing or not executable
refusing to read cache protected location from disk: %s
powerpc
label override
Service cannot reset: active endpoints
service count = %u
PATH=/usr/bin:/bin:/usr/sbin:/sbin
Verification failed
failed to persist services: %d
No cookie: %s
\t
misfired notification: dead-name
unsupported IO type %d
needs_rename = %s
?
developer-tools
kern.maxfiles
OS_REASON_AGGREGATED
\"%s\" exited with exit code = %d
The HideUntilCheckIn property is an architectural performance issue. Please transition away from it.
_PersistToBootMode
1
Failed to set %s: %d - %s
Skipping remaining event endpoints for importance boosting.
recorded reslide request for this instance in the original service
identifier
multiple will-spawn events received
kill(-1, SIGKILL) returned EPERM (expected at most twice)
/AppleInternal/Library/LaunchDaemons/com.apple.jetsamproperties
sanitizer flags = 0x%x
angel
PerformAlways
der_vm_execute_string_value_allowed
_AdditionalServices
host not found
can't ask for the string for 'none' boot mode!
Service sets EnableTransactions=false and EnablePressuredExit=true, which makes no sense. Enabling Transactions.
jetsam property category (%s) is not initialized
CPUMonitorInterval is out of range, ignoring
x86_64
i386
blocking xpcproxy until controller configures the service
routine
_DisclaimResponsibility
_POSIXSpawnTelemetryPageIn
info plist = 
Persisted
This service is defined to be constantly running and is inherently inefficient.
%u
Caller not allowed to perform action: %s.%d, action = %s, code = %d: %s, uid = %u, euid = %u, gid = %u, egid = %u, asid = %u
MSUEarlyBootTask
MobileAssetEarlyBootTask
HOME
extension alive = %s
instance overrides sandbox container must be a string
RecoverOnCrashDeadline
Bug in libxpc: mach_port_assert_attributes() failed
load jetsam properties path initiated by %s: %s
failed to fts_open(%s, 0x%x): %d: %s
userreboot_purpose
signing-identifier
%s/disabled.migrated
SpawnConstraint
SoftPortLimit
SharedRegionConfigFlags
SanitizersAllocationTracesMemoryBudget=production
Cannot set configure key endpoint on service: service has dext checkin port %#x
jetsam hard kqworkloop limit = %u
cryptex = %s
validating %zu persistent services
launchd has not fixed mobile/tmp (socket)
Userspace reboot changed system version: previous %s != current %s
launchd_instance_limit=
BATS_TESTPLAN_ID=
it disabled initgroups
unsupported type: %s
handle
exception handler endpoint = %s
uid = %u
default-enabled
event
app (nonui)
manager
pending attachments = {
der_vm_execute_integer_value_allowed
invalid tag or length
bundle_identifier
arm64
no initgroups
query
Unable to stash abandoned service port 0x%x owner PID %d (%s)
boot-mode forced to (%s) skipping set: %s
Failed to mkdir() socket directory: path=%s, mode=%o, error=%s (%d)
handle = %llu, 
%s: _ExperimentalNonLaunching is not compatible with HideUntilCheckIn, ignoring
Unknown data encoding
 [%d]
pended spawn = %s
legacy shutdown, caller = %s
misfired notification: send-once
mark
ExceptionServer
der_vm_execute_match_bool
LaunchServices returned a bundle URL that does not match with the LoginItem's known association.
Saved the port to stash
Unknown key for array: %s
%s is less than zero. Ignoring.
signaled service for %s: %s
service deactivated with active endpoints
PureOnDemand
HighWatermark
Not eligible for acceleration
MinimalBootProfile
/System/Library
Bootout
Removed service on spawn failure
removing unmanaged pid-local endpoint: %s
ProgramArguments is not an array of strings.
SoftResourceLimits
ReceivePacketInfo
slaying domain for rebirth
Active user logout, initiated by: %s[%d]
/System/Library/LaunchDaemons/com.apple.jetsamproperties.NonUI.plist
launchd
session = %s
deactivated
kern.minimalboot
kern.osversion
Memory limit override file is present, disabling memory limits.
unexpected subdio for an app extension bundle
IPv6
LaunchDaemon
Error during registration of '%s', Daemon Notification requires _Conclave key
Unable to find managed service for pid %d. Trying unmanaged services
reboot
_Quarantined
Cannot rename secure socket; UIDs mismatch: socket owner=%d, path=%d
Unsupported value for OSLogRTBufferConfig: %s
com.apple.private.xpc.launchd.userspace-reboot
%u:%s 
kern.roots_installed
by-cli
persistent services object is invalid
_Conclave
incomplete CPUMonitor, ignoring
bound interface = %s
Could not import service from caller: path = %s, caller = %s[%d], error = %d: %s
SIGTTIN
Could not bind to system logger socket: error = %d: %s
MaxExitTimeOut
com.apple.xpc.launchd
could not set up inheritance port
disable pointer auth
total of %lu extension (%s) instances were found to remove, of which %lu were removed instantly
Invalid Arguments
Exceeded max diagnostic thread count for type %s (%u)
.xpc
path = %s
jetsam soft port limit = %u
persona id = %u
Skipped persisting services in domain: %s
failed to lookup domain for persisted service
It never did anything anyway.
throttle
Skipping remaining service endpoints for importance boosting.
com.apple.xpc.workload_properties
failed to merge persisted jetsam property overlay[%zu]: %d
Info
der_vm_string_from_context
[%s]: entitlements blob has unexpected version %lld\n
Service: %s has leaked endpoints
cpumon = %d%% over %u seconds
SIGSYS
seqpacket
timed out initial on-demand mode for a multiuser device
/usr/libexec/devicerecoverytool
mig-request
If you rely on this key, please file a bug.
service spawn failed after attach: %d: %s
fds
could not terminate service after SIGTERM timeout: %d: %s
An extension-removal request failed, error: %d - %s
Frameworks
SockPathGroup
suspended
Finished boot task
com.apple.private.xpc.launchd.allow-set-bundle-path
Unable to unpack stdin
tried to overwrite service timeout_source
Boot mode forced.
invalid arguments passed in
active count = %llu
SHELL
Abandoning service: %s
kern.maxfilesperproc
prng_seedctl
der_decode_numeric_string
Daemon
spawning after urgent log submission completion
com.apple.xpc.launchd.domain.system
Device recovery
HostSpecialPort
Service did not exit %u seconds after SIGTERM. Sending SIGKILL.
%s: will reboot if exits with code: %d
Tried to set an unknown host-special port: %s
SoftKqWorkloopLimit
sudden shutdown
legacy-service-lookup
system reboot
Unknown key for data: %s
InactiveHardMemoryLimit
requested SIGTERM
Could not activate socket named \"%s\": %d: %s
Stack
AddressLimit
Efficient
com.apple.private.xpc.launchd.per-user-create.mbsetupuser
CoreEntitlements: not a sequence
global environment = {
dirs_cleaner
Unrecognized MachService property: %s
_AdaptiveUtility
Failed to set hw.mempath
Unix
instances
No cookie from system volume
Unentitled submitter specifies _PersistToBootMode in service, which is not permitted
iOSSupportVersion
wait for debugger
Unknown UTC Time encoding
NS Extension Info.plist missing NSExtensionPointIdentifier
config = {
persistent services object is not an array
extension already attempting clean exit
der_vm_execute_select_key
usrctl(0x%x) returned %d (errno %d)
service stats = {
spawn-error
SIGTERMTimeout
EndpointSecurity
Core
string
/System/Library/LaunchAngels/
failed to uncork PID domain on first bootstrap: %d - %s
get domain environment
no services found in persistent object
size >= sizeof(uint64_t)
reading known trial factors from %zu paths
endpoint
managed_by = {
attempted to enter REM in unsupported variant
%s (%s) <%s>: %s\n
attempt to watch an active endpoint
no boot tasks
service will always use xpcproxy, elision was disabled by boot-arg
both NonUI & target-specific JetsamProperties plists are present. This is an error in the OS build configuration.
resolved gid = %d
OS_REASON_TEST
GroupName is not supported by the domain, ignoring.
_LimitLoadFromBootMode
Invalid type for %s importer (key: %s type: %s), accepted types: [
attempt to ignore canceled socket
username = %s
legacy-remove service
job is already monitored
EX_CONFIG
kern.userspacereboottime
TIMEOUT
LAUNCH_DID_REEXEC
_LaunchEvents
daemon notification name '%s' is invalid (must be non-empty and less than %d bytes)
cannot reset service active event channels: %s
#IfFeatureFlagEnabled
persona can only be set on submitted jobs and extensions
checked allocations flags = 0x%x
uid unset
caller removing service: caller = %s[%d]
Abandoning send right to 0x%x (canceled notification)
endpoint %s has unexpected receive_source
Bonjour
job is not monitored, can't poll
no elide roleaccount setup path prefixes
%s\n
boot-mode committed: %s
/Library/JetsamProperties/com.apple.jetsamproperties.DDI.plist
security.mac.asp.willshutdown
languishing
adaptive
JetsamProperties loaded from path : %s
core
init-exclavekit
com.apple.xpc.launchd.xsc.bundle_id
+ %d
failed to map persistent services: %s: %d
%s.%d sent an invalid request: msgh_bits = 0x%x, msgh_size = %u, msgh_remote_port = 0x%x, msgh_local_port = 0x%x, msgh_id = 0x%x
multiple-instance service has no initialized endpoints
EX_UNAVAILABLE
controller-supplied arguments = {
LaunchAgent
removing child: %s
JETSAM_REASON_MEMORY_VMCOMPRESSOR_SPACE_SHORTAGE
 (dead)
ExtensionWatchdogTimeout
could not get jetsam coalition ID for service: %s: %s: %d
version
domain disposal while still in the domains list
unexpected exec of non-platform binary: %s: %s [%d]
%s (%d records)
sysctl failed with error (%i)
%s/overrides.plist
Darwin Bootstrapper Version 7.0.0: Thu Oct  8 00:42:48 PDT 2026; root:libxpc_executables-3298.52.1~4/launchd/RELEASE_ARM64E
cleaning up
true
underflow of active count during deactivate
POSIXSpawnType
InactiveSoftMemoryLimit
Invalid type for a LaunchEvent stream, should be a dictionary (stream/type): %s/%s
PanicOnNonZeroExit
deferred services = {
sockets = {
removing service since it exited with consistent failure - %s
service deactivated with active event endpoints
ForceEnableHack
%s
name = %s
exec count or caller mismatch: caller exec cnt = %u, creator exec cnt = %u, caller pid = %d, creator pid = %d
Tried to set a reserved task special port: %d
LogFileMaxSize
ShutdownTimeout
IgnoreProcessGroupAtShutdown
MallocNanoZone
v20@?0i8*12
run-at-load
stdout path = %s
removing service: %s
extra activation on unmanaged service
Service \"%s\" tried to register for endpoint \"%s\" already registered by owner: %s
integer, 
Reseting consecutive crash history
initial system support
launchd_cache_loader
encountered invalid element in an iterable
Wrong CPUSubtype type - expecting int64
shutting down system: flags = 0x%x, time = %llu ms
violation: %s.%d, action = %s, code = %d: %s, uid = %u, euid = %u, gid = %u, egid = %u, asid = %u
Could not spawn process %s: %d: %s
runs = %u
domain deallocated with services
removing unmanaged endpoint: %s
Last log repeated %llu times
v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
@bundle {
Can't have both %s and %s
Spawning a service in state %s
error
exit timeout = %u
last exit code = (failed reap)
needs proxy
_Cryptex
RecoverOnCrash
ProductBuildVersion
BOOTOUT_SEMI_ACTIVE_SERVICES
/usr/local/lib
Could not find user/group associated with service: %d: %s %s/%s
exceeded sigkill timeout: %u
inconsistency between domain and service semi-active state during semi-active bootout
_NullBootstrapPort
com.apple.xpc.launchd.system-override
active service has zero active count
none
wait
PerformInLeanTestEnvironment
localhost
%s | %s
retry launch on service that was not deferred
Mismatched binprefs: %s != %s
service read
launchd.log: open(%s): %d\n
--recovery-reason
/private/var/log/com.apple.xpc.launchd
launchd built improperly: no __TEXT,__config
Boot
com.apple.libxpc.launchd
boolean should be exactly 1 byte
Platform
v16@?0^{_launch_event_realm_s={_launch_object_s=^vB}{?={?=^{_launch_event_realm_s}^^{_launch_event_realm_s}}}{?=^{_launch_dictionary_s}{?=^{_launch_event_realm_s}}^{_launch_event_realm_s}^{_launch_dictionary_s}Qb1}{?=Q}}8
attempt to re-enter the server layer
UserEnvironmentVariables
v12@?0I8
kern.darkboot
dump jetsam property category
Could not stop service: name = %s, error = %d: %s
descriptor = 
killing extension hanging on launch
service inactive: %s%s
Program specified by service does not contain any valid architectures for this system.
program = %s
multiple invocations of death handler for domain
wait4-status
Tried to set an invalid host-special port: %lld
PublishesEvents
setup_fds bad dest: %d table: %d
LAUNCH_SHUTDOWN_TEARDOWN
xpcproxy
failed to query memory status priority for PID %d: %s (%d)
attrs
%s already exists, skipping
mount-point
Ignoring events for retain only services
network-inbound
service
pid = %d
underflow of on-demand count
key contains an embedded NUL
Disallowing environment variable: %s
Service specifies no Program and empty ProgramArguments.
<private>
initial-load-completed
Notice
it has limits set
subsystem root = %s
non-system session had no name
rebooting on exit code: %d
key / value decoding failure
Unsupported type for index: %lu of _LimitLoadToBootarg
inetdCompatibility
spawned
SIGKILLed
couldn't handoff a spawn, asynced away
started suspended = %s
resource limits = {
_PanicOnCrash key: InternalOnly not enabled in the current environment
RecoverOnCrashCount
%lld
launch job demand
SIGFPE
AssumeSingleUserSuccess
Unknown key for %s importer (key: %s type: %s)
com.apple.private.xpc.launchd.storage-mounter
%d (%sbytes to read)
exited due to %s
service deactivated with active instance endpoints
app
speculative
setting persona requires an entitlement
%s%s => %u
csops returned %d
reentrant call into server layer
%s (soft) => %s
-no-corpses
SanitizerFlags
launch watchdog timeout = %u
no host
Unable to get boot-object-path. Giving up
AuxiliaryBootstrapperAllowDemand
launchd(proxyless)
Service did not exit %u seconds after SIGTERM. Terminating with a crash report.
.darwin
EnableCheckedAllocations
SubmissionTimeout
LimitLoadFromHardware
Configuration error: failed to fetch our own audit token
EX_OSERR
service will use proxy because %s
Preventing \"%s\" from registering for %s due to non-launching property mismatch
query service enabled state
Re-opening serial log (error: 
unmanaged service given to service interface. pid: %d service: %s
Loading overlay plist from: %s
terminated
com.apple.xpc.launchd.timeout
unmanaged processes = {
Found cookie: %s
EnablePressuredExit
cannot reset service active pid-local endpoints: %s
misfired notification: port-deleted
subsystem
Unable to merge spawn constraints
Deferred spawn of service failed: %d: %s
global
ui non-focal
alias-removal attempt of non-aliased endpoint
Accumulated more than %d subscriptions for stream %s
recursion limit reached
vers
alpha
Queried sysctl kern.darkboot: %u
cputypes
user.%d
instance overrides sandbox profile must be a string
overflow detected
In boot-mode %s, skipping boot-task %s
\"%s\" = {
StopJob
v24@?0Q8@16
Caller not allowed to perform action: %s[%d], action = %s, code = %d: %s, uid = %u, euid = %u, gid = %u, egid = %u, asid = %u
<-%s[%d]
_JoinGUISession
com.apple.rootless.xpc.effective-root
will attach to %s next time it's created
fips
perform reboot failed: %d
Found roots installed cookie
GetResourceUsageSelf
Either %s or %s must be present
required
CEValidateWithOptions
LegacyTimers
_Protected
bundle ID = %s
SERVICE CACHE DELETE INVARIANT VIOLATED: %s not found
run
Extension remained dirty for too long after trying to exit. Killing.
hard
mach_ports_lookup() failed: %d
Feature disabled, device would have rebooted due to %s
service is still not a zombie, abandoning
Could not import service from caller: caller = %s[%d], service = %s, error = %d: %s
OS_REASON_RUNNINGBOARD
dictionary value verification failure
_LimitLoadToDeviceTree
service-port
numeric string element not allowed
Unknown key for KeepAlive: %s
errors
%016llx
SPAWNED
Could not parse plist: path = %s, error = %d: %s
Ignored socket %s: %s
iOSUser
(unknown reason)
com.apple.fsevents.matching
Could not find uid associated with service: %d: %s %u
extension already interrupted clean exit attempt
domain shutting down, not uncorking
src != (A *)data_
Unknown boot-mode: %s
Please switch away from OnDemand to KeepAlive.
_DextCheckInPort
invalid jetsam property category type: 0x%x
Unable to create stdout directory (%s)
proxy
archpref
Service specifies neither Program nor ProgramArguments.
com.apple.remoted.service
reload count = %zu
\"%s\" => 
Could not get interface index (name = %s, idx = %lu)
jetsam wired memory limit = %u
role account
Failed to enable service %s, error=%d - %s
Disabled
DrainMessagesOnFailedInit
initialized = %s
all-jobs
vm.shared_region_pivot
key
JETSAM_REASON_MEMORY_LONGIDLE_EXIT
XPC_USERSPACE_PIVOTEDROOT
_PanicOnCrash key: PanicOnCrashDeadline overflowed converting to ns (%lld)
Unable to create stdin directory (%s)
service print
Setting service %s to %s
OS_REASON_WATCHDOG
ResetAtClose
Child
SIGKILLTimeout
ExitTimeOut
BaseSystem environment starting.
Service only ran for %llu seconds. Pushing respawn out by %llu seconds.
rem-enable-fuse
GetResourceLimits
Could not set up nowait inetd service: %d: %s
  [%zu] => %s
MultipleInstance XPC services are not supported for any service type other than Application. Forcing service to PID domain.
Service stub initialized for %s
_launch_service_set_conclave
ServiceIPC
UserInterface
mips
already shutting down or slain
type = %s
\"%s\"
/System/AppleInternal/Library
DYLD_PRINT_INITIALIZERS
deferral event on service in penalty box
removing semi-active service: %s
Domain creation failed: it already exists
PassLaunchBootModeAsArgument
/System/Library/CoreServices/SystemVersion.plist
No service cache
service is being debugged, not timing out launch
Program specified by service is not a Mach-O executable file.
Wipe them out. All of them.
posix_spawn: %d: %s
Restored the port from stash
%s less than zero. Ignoring.
UDP
Could not get domain target from bundle: path = %s, error = %d: %s
Bundle has no executable
_AllowedClients
ResidentSetSize
hello, launchd UUID: %s
/usr/lib/system/libsystem_info.dylib
DYLD_PRINT_LIBRARIES
Abandoning PID %d and its process group
Service cannot reset: active PID-local endpoints
error parsing the workload properties plist in the kernel (%u)
(submitted by %s.%d)
optional cannot be created with zero error
DeveloperTools
memory = %d/%d
:
jetsam priority = %d
ios home screen app
Shutdown
Socket entry is not a dictionary or array. Skipping: %s
CPUSubtype
could not find endpoint in pid namespace: pid = %d, name = %s
OS_REASON_SKYWALK
active
shutdown already committed
stdin path = %s
com.apple.xpc.launchd.domain.user
 [%s]
status
persisting service %s (%s) into %s
finish-restore
com.apple.launchd.PathState
com.apple.private.xpc.launchd.allowed-manage-trial-factors
resource
hppa
Could not accept new inetd connection: %d: %s
requestor = %s[%d], error = %d: %s
Non-system service tried to claim event stream %s
kernel returned invalid sender procname for signal
Improper type for KeepAlive key: %s
Unable to unpack environment
attempt to watch canceled socket
cannot spawn: service is in penalty box
Got dead control port
der_vm_execute_string_prefix_value_allowed
service will attempt to elide xpcproxy
Unsupported type for _LimitLoadToBootarg
Service (pid %d) does not have spawn driver entitlement
com.apple.xpc.launchd.eventq
coalition_reap(%llu) [%s]
SIGTERM timeout
legacy-load
domain creation
ActiveHardMemoryLimit
JetsamProperties
soft
darwin bg
returning username for get_uid_for_token: %s
.DarwinDepot
bytes-written
endpoint deallocation while still in domain list
_LimitLoadToClarityMode
MachServices
_ServiceJetsamCoalitionToJoin
ipv4v6 = %s
Rejecting untrusted event subscription on stream %s
rebooting after success
HideUntilCheckIn
/private/etc/com.apple.xpc.launchd.limits.plist
abandoned
com.apple.private.xpc.launchd.loginitem-bootstrapper
runatload
disabled
 [%lu]
cryptex
xml-looking blob was passed in
encountered invalid element in an array
CPUMonitorPercentage
%s: inserting zero urgent log submission key
Unable to open stderr path (%s)
com.apple.xpc.launchd.spawn
last exit code = (abandoned)
writeBytes
recoveryos
JetsamMemoryLimit
 %llu (%s),
/AppleInternal/Library/LaunchAngels/
cannot userspace reboot while in REM
extra data at the end of element
lockdown.
Not allowed to set SockPathOwner to UID %d. Remove key.
Userspace reboot
throttling
initiated at %ld by %s
xpc-domain
validating %zu jetsam property overlays
SIGXCPU
der_vm_integer_from_context
xpcproxy exited due to %s
deferred
speculatively converted service to spawned, but spawn failed with error %d
cannot safely abandon: %d: %s
exception handler
maxproc
LogIPC
BundleProgram(%s) is not the same as Program(%s). Bug in ServiceManagement?
_BundlePath
Failed to fstatat() socket path: path=%s, error=%s (%d)
Rebooting to device recovery environment
Service could not initialize: %s, error 0x%llx - %s
blob
created
#IfVariant
Unknown key for double: %s
system xpcservice
%s/launchd.log.1
failed to restore persistent object: %d
persisted submit job failed: service = %s, error = %d: %s
der_vm_bool_from_context
RootDirectory
kern.proc.all
self
cannot reset service active unmanaged endpoints: %s
subdomains = {
%s/launchd.log
SupplementalJetsamProperties
InitialTaskRole
service only configured to run once, removing
no reply expected, failing
maximum allowed shutdown time = %d s
dictionary key / value decoding failure
Maybe.h
/AppleInternal/Library
Could not activate inetd socket: %d: %s
is copy
/private/preboot
GetJobs
unable to resolve 'mobile': %d - %s
persistent services header magic is invalid
Failed to open() socket parent directory: path=%s, error=%s (%d)
ID = %llu
launching: %s
Critical
noop
data element not allowed
Data
(lint): %s
fstatfs failed, treating ownership as untrusted: %d: %s
PATH contains lots of paths. Some will be skipped.
%d
 after %s
managed_by = %s
hardened ipc
_PanicOnCrash key: PanicOnCrashDeadline less than zero. Ignoring.
clearing pending urgent log submission for %s; pid = %d, version = %d
jetsam-flags
service bootout (%s)
unmanaged service deactivated with active pid endpoints
The system may be in an inconsistent half-obliterated state.
%#8x %4c%4c   %s
launchd_workload_properties_disabled=
_MultipleInstances
XXXXXXXX%s=%s
shutdown %s -> %s
events
Error
Invalid item type %s in PublishesEvents, expected string
%hd
service spawn reason '%s' pended until controller attaches
domain deferral
SystemPersonaServices
bool decode failure
it has a roleaccount set
StandardErrorPath
canceling penalty-box spawn
PerformAfterUserspaceReboot
dirs_cleaner-usr
UseNanoAllocator
EnableHardenedIPC=>false is not allowed
{
com.apple.%s
com.apple.launchd
ReslideSharedCache
Could not activate socket group: %s: %d: %s
%s is being removed from a mismatched domain %s
recovery-mode
DisableExtensionMemoryLimit
LimitLoadFromHosts
MallocLargeCache
Conflicts exist in System services. Randomly deciding: path1 = %s, path2 = %s
leader-pid
persona set at = %u
paths
Expected string for a feature flag, got %s
Plist has the com.apple.quarantine xattr set: %s
always sigterm on shutdown
not XPCService
XPC_IN_REM
%s coalition ID = %llu
denied lookup
Async
host-special port = %u (%s)
%s is ignored in favor of %s
urgent log submission = {
_executablePath
Got a socket event for an inetd service, but couldn't accept any sockets
invalid syscall mask array type (%i)
SoftFileDescriptorLimit
kern.osreleasetype
DYLD_PRINT_STATISTICS
boot task is not a platform binary (%s, %s)
AbandonProcessGroup
pid-extend
endpoint deallocation while still active
 during %s
obliteration complete, sending reply
unrecognized launch diagnostic thread type: %u
pended
print
Emergency
Invalid socket name: %s
ABANDONED
%s is larger than the maximum allowed. Changing it to %d.
_ProvenanceData
cannot abandon languishing service: %d
Service setup event to handle failure and will not launch until it fires.
Endpoint \"%s\" tried to steal host exception port from \"%s\"
Attempting to select a string value from a non-string DER object
Unable to unpack stderr
%s cannot be run directly.\n
LastExitStatus
unidomain
jetsam-memlimit
copy count = %d
services[%zu] is missing or has invalid origin key
attempt to ignore unmanaged endpoint
_OmitSandboxParameters
Failed to connect() a socket: path=%s, error=%s (%d)
Invalid type for socket dictionary (key/type): %s/%s
minimum runtime = %u
could not set protection class on %s: %s
domain is not initialized, can't uncork
coalition-id
$or
kern.bootargs
unthrottle
Label
_SandboxProfile
InitGroups
abandoning languishing service
caller failed %s sandbox check on parent directory %s
Unable to monitor socket #%zu
retry launch
semaphore
wait4() failed
Caller tried to import service with same label as an existing service: path = %s, caller = %s[%d]
kill service (%s)
inconsistency between domain and service semi-active state during obliterate
Adaptive
__Proxyless
B24@?0Q8r*16
EX_OSFILE
Abandoning service instance. This may lead to deadlocks.
pending bootstrap lookup during user switch: name = %s, requestor = %s[%d]
Unable to find persona with type %d: %d - %s
Refusing to make a port for a canceled endpoint
com.apple.cryptex.app
Wrong CPUType type - expecting int64
/var/run/com.apple.launchd.XXXXXXXXXX
bonjour = %s
event channels = {
inactive
SingleUser
RemoveOnSuccess
com.apple.xpc.datastores.publish
Invalid value for MultipleInstances '%s'
internal event: %s, code = %ld
retrieved exit reason with invalid reason buffer size
dispatching request
_ManagedBy_Services
Unable to unpack sandbox profile
DYLD_PRINT_REBASINGS
ui
DaemonNotifications
com.apple.private.xpc.persona-manager
/
Will be re-execing for a userspace reboot
ess bootstrap_look_up: endpoint owner == NULL for service %s
Datastores
_RecoverOnCrash
disabled services = {
launchd_verbose_coalition_logs=
der_vm_execute_match_integer
com.apple.xpc.launchd.serialq
com.apple.xpc.launchd.bgioq
EX_DATAERR
Could not accept inetd connection to retain-only service
RebootOnSuccess
eacs
i680
v20@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
SIGSEGV
der_decode_entitlements
extension
_instance
kern.bootobjectspath
SIGVTALRM
signal
LogToConsole
Unknown boot-mode: %d
PanicOnConsecutiveCrash
%s = {
remove all extension instances
Improper type for %s
service spawn deferred by %llu seconds due to %s
disabled services = (no disabled services)
system services must be in cache
fvunlock
$and
kern.userspacerebootpurpose
Unknown family encountered during multicast group bind: %d
Service stub initialization failed for %s [%d]
OtherJobEnabled
urgent log submission completed, pushing out %llu more seconds
setup_fds bad fd type
denied kick request from %s - missing entitlement %s
#Else
/etc/nologin
spawn of %s failed: %s
com.apple.launchd.QueueDirectories
INVALIDATE_UNMANAGED_ENDPOINTS
no 
Service could not notify controller.
mc98000 (best MC ever)
needs implicit endpoint
Given object not of required type.
(submitted by %s[%d])
Improper type for _PanicOnCrash key: %s
critical process crashes: %s
signaled service: %s
commit-boot-mode
no jetsam property overlays found in persistent object
aidearlyboot
%s boot task not present
_StandardOutFd
Userspace teardown took: %llu ms
no-einprogress
kern.hostname
OnDemand
Skipping extension launch watchdog
state = %s
LaunchInstanceID
Please use _AdditionalSubServices instead.
NetworkState
PerformInBaseSystem
ServiceStubsDisabled
disable resliding
domain has no corresponding special port entry
_LimitLoadToVariant
com.apple.private.xpc.launchd.job-manager-remove-any
active config = {
arguments = {
sandbox profile = %s
task-special ports = {
joining jetsam coalition of %s: %llu
_SubsystemRoot
cannot spawn: service is configured as retain only
stderr path = %s
inetd listener
Setting boot mode to %s
(no bundle cache)
SIGTSTP
DYLD_PRINT_RPATHS
Invalid XPCService dictionary.
GET_PORT_FORCE for endpoint %s but port not yet made
\t<string>%s</string>\n
der_decode_data
jetsam conclave memory limit = %u
matched domain attach request on creation
failed to reload active trial factors because it is currently locked
%s 
one-shot
service jetsam coalition to join = %s
OS_REASON_SANDBOX
entitlements blob does not have CCDER_ENTITLEMENTS coding
_AbandonCoalition is only available to Application services.
com.apple.private.xpc.launchd.job-query
booting out service
instance-uuid
der_decode_key_value
udp
filesize
array, 
/private/var/mobile/Library/Trial/NamespaceDescriptors/v2/activeLowLevelFactors.plist
slaying domain
PackedDataBuffer.cpp
Disallowing panic-on-crash behavior for non-system service
unpend launches
developer_tools_options must be a dictionary
successfully submitted persisted service: %s to %s domain
Could not create system logger path: error = %d: %s
kern.willuserspacereboot
Unable to parse MRM cache
Overriding specified stdin path for inetd-compatible service.
jp-priority
SuddenShutdown
root
Service specifies _PersistToBootMode which is not permitted for services that were not dynamically submitted
os-code
xpc service paths = {
it set a non standard working directory
KeepAlive
Unsupported type for _LimitLoadToDeviceTree
Invalid item %s in PublishesEvents, expected dictionary or bool
ActiveLowLevelFactors
Could not parse plist: path = %s, error = %d: %s:
pended nondemand spawn failed: %d
legacy-stop service
Replacing controller %s[%d] with %s[%d]
trampoline
(confusing)
maxfiles
restore-datapartition
Activated a directory (%s) and found no files
service already stopped
lazy initialization of endpoint on semi-active service
copy busy extensions
der_decode_boolean
User
Sandbox
receive_packet_info = %s
getaddrinfo(3): %d: %s
labels
auearlyboot
@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Thu Oct  8 00:42:48 PDT 2026; root:libxpc_executables-3298.52.1~4/launchd/RELEASE_ARM64E
USER
XXXXXXXX%s=%s/tmp
instance
Cannot look up instances for sub-instances.
Unexpected type to match against
/System/Library/xpc/launchd.plist
extension check-in timeout
mach-lookup
os-reason-flags
LowPriorityIO
outgsk
exiting ondemand mode
active service count = %u
count
TimeOut
LoginWindowUserName
jetsam memory limit (inactive) = (unlimited)
Start job failed: another start request is already inflight
instance overrides environment variables must be a dictionary containing strings only
could not decode size for next DER sub-sequence
_autounlock
v28@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
JetsamPriority
DYLD_PRINT_SEGMENTS
service has crashed %u times in a row (last was%s dirty)
has provenance
LaunchAngel
overflow of service activation count during activate. Managed:%d. Domain:'%s'. Service:'%s'
com.apple.private.xpc.conclave.submit
logout
SIGALRM
LogAllBootstrapErrors
Conclave can only be set on LaunchDaemons or Extensions
MallocSpaceEfficient
com.apple.private.xpc.launchd.persist-to-boot-mode
Service attempted to specify secure socket key with reserved name: %s
boot task argument vector is not an array
overflow of service activation count during deactivation. Managed:%d. Domain: %s. Service:%s
Unmanaged endpoint \"%s\" was canceled to transfer the ownership to: %s
PostLogOutSync
Could not create new instance of inetd service: %d: %s
service stubs = {
StartInterval
Failed to basename_r() socket directory path: path=%s, error=%s (%d)
Denied access to socket; caller = %s[%d], trusted = %d, error = %s: %d
group id = %u
Skipping remaining instance endpoints for importance boosting.
device recovery on crashes (%zd)
descriptor
dropped-count
ProgramArguments is not an array.
BOOTOUT_SERVICES
jetsam-priority
Service \"%s\" tried to register for aliased endpoint: %s
refusing to add a duplicate domain: type=%s handle=%lu
xpcroleaccountd
sent by %s[%d]
Paths
LaunchEvents
Medium
attempt to watch socket that is already watched
original = %s
underflow of service activation count during activate. Managed:%d. Domain:'%s'. Service:'%s'
rebirth already in progress
SystemCalls
launchd_usr_abandon_unmanaged=
string, 
forbidden-launchd-operation
service \"%s\" tried to claim task-%s port from endpoint \"%s\"
rlimit(3)? Really?
client-reply-port
Could not get Info.plist for bundle at %s
99Z999
domain already deactivated
failed to map persistent services header: %s: %d
SIGHUP
Alert
cpumon = default
low priority i/o
string decode failure
Unexpected type to match against during iteration
Standard
penalty box
hardlimit
EnablePressuredExit is not compatible with KeepAlive=true. Ignoring EnablePressuredExit.
EnableIdleHysteresis
com.apple.private.xpc.launchd.loginitem-outside-bundle
Data corruption: CoreEntitlements has aborted due to an unrecoverable error
pending requests = {
flags = 0x%llx, 
optional
LogFileVerboseMetaLimit
__Angel
AlwaysSIGTERMOnShutdown
file-write-create
BEGIN_SHUTDOWN
v28@?0^{_launch_domain_io_s={_launch_object_s=^vB}{?=*{_xpc_token_s=IIIIIiii}Q^{dispatch_queue_s}@?@?^{_launch_array_s}ICb1}}8^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iS
Deferring IPC (%d) while service is spawning
last exit code = %d
Async boot task %s must not have flags
MulticastGroup
bootstrap
supports transactions
encountered invalid tag
/var/mobile/Library/Accessibility/ClarityBoardEnabled
Invalid type for a RemoteServices entry, should be a dictionary (key/type): %s/%s
setup_fds bad int type
pid %d not allowed to get properties for service
Service cannot reset: active event channels
bootout initiated by: %s
service stop (%s)
The launch_msg(3) API may only be used on the system or user domains.
com.apple.launchd.WatchPaths
com.apple.private.xpc.launchd.enable-disable-system-services
PrivateFrameworks
Overflow calculating deadline: %lld + %lld
properties = %s
enable service
.roots-installed
kern.maxproc
invalid domain io type
posix_spawnp() returned 0 but pid=%d
 not
/private/var/mobile/tmp
user
removing unmanaged service: %s
error parsing the workload properties plist in launchd (%u)
failed to serialize service plist: %s
Provenance data too big: %zu
Unsupported value for EnergyEfficiencyMode: %s
com.apple.private.xpc.service-instance-manager
com.apple.private.xpc.launchd.allow-posixspawn-telemetry
proc source registration handler invoked twice
canceling throttled spawn
The endpoint \"%s\" defined in plist already exists and is owned by: %s
legacy shutdown initiated by: %s
ProgramArguments
_DisablePointerAuth
EX_IOERR
cwd
failed to serialize jetsam properties[%zu]
sending reply
demux error = %d
Non-empty dictionary property on MachService: %s
/System/Library/JetsamProperties/com.apple.jetsamproperties.cryptex.plist
yesno
com.apple.xpc.launchd.domain.user-login
%s/launchd.log.2
SIGPIPE
\n
/private/var/db/launchd.db
Loading DDI overlay plist from: %s
Large
Attempting to select a boolean value from a non-boolean DER object
EnableGlobbing
CoreEntitlements: unknown DER type
(n/a)
 (initiated by %s)
#IfNotVariant
failed to restore service[%zu]: %d
OS_REASON_JETSAM
launchd logging initialized. name: %s pid: %d
v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
Could not resolve CFBundleIdentifier specified by service: %d: %s
failed to reap boot-task (%s, %s)
Unable to create stderr directory (%s)
Aqua
jetsam memory limit (active) = (unlimited)
Unable to unpack cwd
in
exec hack
uncorking domain
modify rlimits
failed to fts_open(/private/var/db/launchd.db, 0x%x): %d: %s
_PanicOnCrash key: AutomationOnly not enabled in the current environment
KSS_CHECKED_ALLOCATIONS_PREFLIGHT:Enable=1
controller = %s.%d
Could not create system logger socket: error = %d: %s
hw.mempath
jetsam soft file descriptor limit = %u
%s - %s
Program specified by service is malformed.
spawn role = %s (%lu)
pid-local registration
Could not setup inetd descriptors: %d: %s
(unspecified)
pending spawn, service not yet imported: %s
com.apple.quarantine
removing
ds
LimitLoadToDeveloperMode
Service specifies non-absolute Program path.
-%d
inefficient
last exit code = (never exited)
spawn type = %s (%lu)
softlimit
dump state
/dev/console
Ignoring _JetsamPropertiesIdentifier on a service which isn't submitted
Got a socket event but accept() failed with errno %d - %s
underflow of service activation count during deactivate. Managed:%d. Domain: %s. Service:%s
_ManagedBy
AutomationOnly
EXEC_EXIT_REASON_FAIRPLAY_DECRYPT
MachExceptionHandler
AfterInitialDemand
Attempting to commit shutdown unexpectedly: %s
extension removal
%s <%s>: %s\n
_LaunchType
MallocMediumZone
com.apple.xpc.launchd.bglogq
extension checked in as alive
jetsam-properties
failed to marshall spawnattrs: offset = %u, left = %lu, expected = %lu
com.apple.private.domain-extension
com.apple.private.xpc.is.xpcproxy
ignoring spawn reason '%s' due to filter
```
