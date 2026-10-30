# `/sbin/launchd`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 639,552 bytes.

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
Endpoint \"%s\" tried to steal host exception port from \"%s\"
cryptex
rebooting on exit code: %d
sent by %s[%d]
dictionary decoding failure
EnableCheckedAllocations
_UrgentLogSubmission
_RecoverOnCrash key: RecoverOnCrashDeadline overflowed converting to ns (%lld)
removing child: %s
%s[%d]
Log level out of bounds for system state conversion: %d
routine
</plist>\n
_DisclaimResponsibility
com.apple.xpc.launchd.xsc.sandbox_profile
multiple attempts to remove service instance
developer_tools_options must be a dictionary
_VoluntaryExitTimeOut
Enabling panic-on-crash due to consecutive crashes
jetsam-priority
Service cannot reset: active unmanaged endpoints
which
all services read
ThrottleInterval
KSS_CHECKED_ALLOCATIONS_PREFLIGHT:Enable=1
INVALIDATE_UNMANAGED_ENDPOINTS
SupplementalUserPaths
string, 
com.apple.private.xpc.launchd.app-state-manager
Overflow calculating deadline: %lld + %lld
Mismatched binprefs: %s != %s
cached daemons = {
failed to map persistent services: %s: %d
endpoint deallocation while still in service list
Improper type for %s
Attempt to re-bootstrap service from different path, will use existing: service = %s, existing = %s, conflicting = %s
Small
sequence packet
attempt to launch while in penalty box
extension checked in as alive
exec count or caller mismatch: caller exec cnt = %u, creator exec cnt = %u, caller pid = %d, creator pid = %d
get domain environment
EnablePressuredExit
Please use _AdditionalSubServices instead.
checked allocations reason = %s
exception handler
Endpoint has been activated through legacy launch(3) APIs. Please switch to XPC or bootstrap_check_in(): %s
Could not submit extension %s: %d - %s
MSUEarlyBootTask
Not eligible for acceleration
_ExponentialThrottling
Cannot rename secure socket; UIDs mismatch: socket owner=%d, path=%d
panic on consecutive crashes (%zd)
select-boot-mode
domain print
Will be pending launches until told otherwise
launchd built improperly: no __TEXT,__config
SizeLimit
com.apple.private.xpc.launchd.service-stats
/private/var/mobile/Library/Trial/NamespaceDescriptors/v2/activeLowLevelFactors.plist
jetsam hard kqworkloop limit = %u
value
JetsamProperties plist is malformed
Rebooting to device recovery environment
Coalition Cache Evicted: %s [%llu]
Skipping remaining event endpoints for importance boosting.
recorded reslide request for this instance in the original service
Invalid type given for bootstrap path sanitization
Unable to stash abandoned service port 0x%x owner PID %d (%s)
SIGKILLTimeout
Ignoring _JetsamPropertiesIdentifier on a service which isn't submitted
ActiveHardMemoryLimit
uses proxy = %s
No matching personas of type %d uid %d, found %zu
Failed to resolve BundlePath: error=%s: %d, caller=%s
LaunchEvents
disclaim responsibility
inactive domain is not shutting down
lazy initialization of endpoint on active service
failed to stop active service %s: %d
failed to map persistent services header: %s: %d
MinimalBootProfile
sockets = {
EX_NOHOST
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">
could not decode tag for next DER sub-sequence
_JetsamPropertiesIdentifier
failed to read known factors plist from %s: %d
Restore environment starting.
out
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Sources/libxpc_executables/launchd/domain.c
SIGABRT
%d: [
DisableASLR
com.apple.private.xpc.launchd.job-query
/System/Library
attempt to watch canceled socket
Reseting consecutive crash history
UTC Time element not allowed
PATH contains lots of paths. Some will be skipped.
run
darwin bg
Could not accept inetd connection to retain-only service
attractive services = {
uncorking domain
response
UserInterface
pid-local endpoints = {
invalid type for persistent services
Invalid type for a LaunchEvent (stream/name/type): %s/%s/%s
archpref
subsystem root = %s
non-ui
rlimit(3)? Really?
_ServiceJetsamCoalitionToJoin
rebirth already in progress
Tried to set an unknown host-special port: %s
Unsupported type for _LimitLoadToDeviceTree
LaunchOnlyOnce
LogicalWritesLimit
%s.%s%s.plist
process exited in a dirty state
resource limits = {
invalid client reply port %d
overflow detected
PanicOnNonZeroExit
MallocMediumZone
%s: inserting zero urgent log submission key
overflow of service activation count during activate. Managed:%d. Domain:'%s'. Service:'%s'
starting obliteration
obliterating semi-active service: %s
descriptor
cpu
file-write-unlink
domain creation
PassLaunchBootModeAsArgument
CFBundleIdentifier
Unable to copy merged spawn constraints
blob
Got a socket event for an inetd service, but couldn't accept any sockets
%s (%d records)
cannot userspace reboot while in REM
domain exec event
In boot-mode %s, skipping boot-task %s
Failed to basename_r() a socket path: path=%s, error=%s (%d)
services = {
by-cli
AssumeSingleUserSuccess
JetsamProperties
CARRY_ON
LaunchServices returned a bundle URL that does not match with the LoginItem's known association.
GetResourceUsageChildren
__TEXT
\t<true/>\n
com.apple.xpc.launchd
posix_spawnp() returned 0 but pid=%d
no initgroups
Sandbox violation: endpoint = %s
failed to reap boot-task (%s, %s)
No hidden path for socket: path=%s
Could not activate inetd socket: %d: %s
managed_by = %s
<dict>\n
EX_CONFIG
checked allocations crashed
removing inactive unmanaged service: %s
OS_REASON_CODESIGNING
SuccessfulExit
ios home screen app
Submit job succeeded: service = %s
launchd_verbose_coalition_logs=
der_decode_entitlements
%d (%sbytes to read)
failed to remove inactive service
Too many sockets for name \"%s\". Some will be skipped.
No cookie from system volume
retrieved exit reason with invalid reason buffer size
Unknown boot-mode: %s
service disposal while still in list
jetsam memory limit (active, %s) = %d MB
TaskSpecialPort
<endpoint name too long>
Unable to unpack stdin
setup unix domain socket
pended nondemand spawn = %s
inconsistency between domain and service semi-active state during active bootout
lazy initialization of endpoint on semi-active service
99Z999
already handled failed init, ignoring
ingsk
pid = %d
com.apple.xpc.launchd.domain.user-login
active service count = %u
job is not monitored, can't poll
failed to deserialize persistent object
IgnoreProcessGroupAtShutdown
_serviceBundles
group = %s
force-enabled
OS_REASON_TCC
checked allocations flags = 0x%x
(infinity)
/
SLAY_CHILD_DOMAIN
ipc (mach)
uuids
service is already a zombie
cannot reset service active endpoints: %s
legacy shutdown, caller = %s
com.apple.private.xpc.aux-bootstrap
%lu = 
%s (hard) => %s
failed lookup due to non-launching property mismatch: name = %s, requestor = %s.%d
dirs_cleaner-usr
com.apple.private.xpc.allowed-get-service-name
Userspace reboot changed system version: previous %s != current %s
SERVICE CACHE DELETE UNEXPECTEDLY DELAYED: %s replaced: %s by %s, %s by %s
v16@?0^{_launch_coalition_s={_launch_object_s=^vB}CiQQi^v^v^{coalition_resource_usage}^?}8
cannot safely abandon: %d: %s
managed_by = {
program = %s
interactive
_DisablePointerAuth
has provenance
/AppleInternal/Library/LaunchAngels/
spawn failed
ExtensionWatchdog
kern.userspacereboottime
com.apple.xpc.launchd.xsc.bundle_id
Unknown key for string: %s
Failed to fstatat() socket path: path=%s, error=%s (%d)
string
 | 
CheckedAllocationsPosixSpawnFlagsGlobal
abandoned xpcproxy before exec
deferred event: domain spawn response: %d
properties = %s
/private/var/mobile/tmp
extra activation on unmanaged service
Could not parse plist: path = %s, error = %d: %s:
CPUMonitorPercentage is out of range, ignoring
hard reboot
will-spawn received on active service
modify rlimits
Skipping setting up shared memory with cache loader
posix_spawn: %d: %s
Could not setup inetd descriptors: %d: %s
initialized endpoint after lookup
on-demand count = %d
in initial on-demand
service remove (%s)
#IfVariant
Queried %zu attributed services: caller=%s[%d], coalition=%llu
endpoint %s has unexpected receive_source
\"%s\"
true
v24@?0r*8@16
SIGFPE
LimitLoadFromBootModes
speculatively converting service to spawned, pid=%d
deferred
Setting boot mode to %s
mdns
der_vm_bool_from_context
com.apple.private.spawn-driver
unknown
TIMEOUT
(lint): %s
i386
system domain deallocated
underflow of on-demand count
Failed to deregister daemon notification endpoint '%s': %s
hw.mempath
pending spawn, service not yet quiesced: %s
%#8x %4c%4c   %s
Non-system service tried to claim event stream %s
Could not remove job: error = %d: %s
boolean should be exactly 1 byte
B24@?0r*8^v16
attempted to petrify a service twice
LowPriorityBackgroundIO
UIKitApplication:
Could not get interface index (name = %s, idx = %lu)
dataless file mode
OS_REASON_RUNNINGBOARD
_ThrottleInterval set to zero. You're not that important. Ignoring.
stream
(invalid)
XPC_IN_REM
.%s
Service cannot reset: active PID-local endpoints
post-upgrade
DomainInternal
stdin path = %s
_AdditionalProperties
invalid domain io type
managedby_services = {
RequireRun
attempt to remove non-existent server port
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Binaries/libxpc_executables/install/Symbols/launchd
Conclave can only be set on LaunchDaemons or Extensions
DaemonNotifications
DYLD_PRINT_INITIALIZERS
enable checked allocations
%s is being added to a mismatched domain %s
OS_REASON_SETTINGS
StandardInPath
reaped
OS_REASON_SKYWALK
OS_REASON_FOUNDATION
WaitForDebugger
trial-factors-v1
DYLD_PRINT_APIS
unable to resolve 'mobile': %d - %s
_BundlePath
plist
com.apple.private.xpc.launchd.setenv-pid-domain
%s 
inconsistency between domain and service semi-active state during obliterate
attempt to ignore endpoint that is already ignored
%s is too large. Ignoring.
/System/Library/JetsamProperties/com.apple.jetsamproperties.cryptex.plist
System reboot
Userspace reboot
EnvironmentVariables
StandardOutPath
Failure info has no PC.
resolved gid = %d
signal
refusing to persist enabled/disabled state for '%s' as it contains illegal XML character '<'
localhost
daemon notification name '%s' is invalid (must be non-empty and less than %d bytes)
memory = %d/%d
\"%s\" exited with exit code = %d
__Proxyless
ID = %llu
Application
endpoint lookup
obliteration
daemon
exceeded sigkill timeout: %u
Path not allowed in target domain: type = %s, path = %s error = %d: %s, origin = %s
spawn of %s failed: %s
launchd_force_data_status=
EXExtensionPointIdentifier
Socket's service points to a non-existent executable. The application firewall will not work with this service.
%s throttled
SIGURG
interval event: domain response: %d
initial system support
dump state
Unknown service type. flags: %llx
Ignoring disabled state because DisableAllowed=false: %s
This service is defined to be constantly running and is inherently inefficient.
Improper type for KeepAlive key: %s
DYLD_PRINT_SEGMENTS
family = %s
unhandled opcode
Caller not allowed to perform action: %s.%d, action = %s, code = %d: %s, uid = %u, euid = %u, gid = %u, egid = %u, asid = %u
exclaves_boot failed: %d
Could not get domain target from bundle: path = %s, error = %d: %s
Supplied value (%lld) for _LaunchType key not allowed
_NeedsSystemThreadGroup
_POSIXSpawnTelemetryPageIn
system shutdown has begun
failed to create notification port for AKS
unmanaged service given to service interface. pid: %d service: %s
Failed to dirname_r() socket path: path=%s, error=%s (%d)
kern.osversion
exponential throttling
death port = 0x%x
Service tried to %s global environment variable with reserved name: %s
domain shutdown
DisableExtensionMemoryLimit
DYLD_PRINT_STATISTICS
dynamic endpoints = {
Persisted
MultipleInstanceLimit
xml-looking blob was passed in
service state: %s
pid
reboot
required boot task executable not found
%s.%d sent an invalid request: msgh_bits = 0x%x, msgh_size = %u, msgh_remote_port = 0x%x, msgh_local_port = 0x%x, msgh_id = 0x%x
Service specifies both standard out file descriptor and path.
Wrong CPUType type - expecting int64
set
error parsing the workload properties plist in launchd (%u)
Notice
Failed to statfs(\"/\"): %d: %s
MachServices
dgram
Abandoning PID %d and its process group
perform reboot failed: %d
TMPDIR
SIGILL
_UIApplicationMain
Failed to dirname_r() a socket path: path=%s, error=%s (%d)
B24@?0Q8r*16
BEGIN_SHUTDOWN
%llu
ipc (socket)
persistent resource coalition = %s
SubmitJob
Failed to resolve LaunchAngel: error=%s: %d, caller=%s
Missing executable detected. Job: '%s' Executable: '%s'
#Else
Submit job failed: service = %s, error = %d: %s
draining message: id = 0x%x
max_task_pmem
coalition_reap(%llu) [%s]
supports pressured exit
%lld file logs dropped [in-flight %lld]: %lld os_log_simple logs dropped
bootstrap-error
Spawning a service in state %s
initialization failure: %s: %s + %llu [%llu][%s]: 0x%llx
CoreEntitlements: Couldn't iterate over DER entitlements\n
lookup-handle
os-reason-flags
Paths
Maybe.h
HardKqWorkloopLimit
Unable to open stderr path (%s)
SockType
null bootstrap port
removing unmanaged service: %s
skipping over obliterator: %s
%s\n
DeveloperTools
exception handler endpoint = %s
%s initiated by: %s
</dict>\n
unknown number encoding
config = {
%lld
BoundInterface
non-ipc demand
Could not find uid associated with service: %d: %s %u
bye
iterable decoding failure
invalid arguments passed in
com.apple.xpc.launchd.timeout
hw.jetsam_properties_product_type
AuxiliaryBootstrapper
KnownFactors
enable-transactions
pending global attachments = {
device recovery on crashes (%zd)
failed to persist services: %d
v16@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
SIGHUP
_InitialSystemSupport
EX_NOUSER
Program specified by service is malformed.
ui
Deactivated abandoned endpoint: %s
Service cannot reset: active endpoints
creator = %s[%d]
domain shutting down, not uncorking
kern.userspacerebootpurpose
/System/Library/xpc/launchd.plist
domain cleaning up with services still in list
foreground_uid
client-reply-port
JETSAM_REASON_MEMORY_VMCOMPRESSOR_SPACE_SHORTAGE
sending reply
key length is invalid
Remove ability to use bypass the proxy: spawn failed: %d: %s
wait for debugger
OS_REASON_COREANIMATION
multiple removals of port entry
MachService endpoint name specified was same as implicitly created endpoint: %s
failed to validate known factors plist from %s: %s: %d
LD_LIBRARY_PATH
Service could not notify controller.
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
checked allocations = %s (queried = %s)
%s%s => %u
dispatching request
invalid dictionary element
name
com.apple.libxpc.launchd
/System/Library/UserManagement/com.apple.xpc.launchd.personas.plist
Executable not in bundle
ContainingBundleID
wait4() failed
fds
sysctl failed with error (%i)
client-port
DisableReslide
launchd quiesce complete\n
com.apple.xpc.launchd.bgioq
internal event: %s, code = %ld
Service tried to claim home screen from: %s
failed to serialized value for key: %s
$and
checked-allocations
alias-removal attempt of non-aliased endpoint
OS_REASON_OBJC
optional cannot be created with NULL value
Unknown service
Interval spawn of service failed: %d: %s
SetUserEnvironment
SIGXCPU
key-value pair contains extra elements
LimitLoadFromHardware
WAITING_ON_COALITIONS
%s is being deactivated by a mismatched domain %s. Managed:%d.
stream = %s
%s - %s
wait
No cookie: %s
Could not set up nowait inetd service: %d: %s
The key is ignored, please switch to (Active|Inactive)(Soft|Hard)MemoryLimit
%s
Overlay plist is missing.
unsupported type: %s
controlled preflight
com.apple.private.xpc.launchd.obliterator
%s value is too long.
Too many instances (%d >= %lu : %d), slaying '%s' to make room
OS_REASON_LIBXPC
exit()
numeric string element not allowed
Bundle has no executable
Unknown key for KeepAlive: %s
Improper type for _PanicOnCrash key: %s
spawning after urgent log submission completion
SandboxProfile
pended spawn reason '%s': redriving controller attach request
service spawn reason '%s' pended until controller attaches
underflow of service activation count during activate. Managed:%d. Domain:'%s'. Service:'%s'
#IfFeatureFlagEnabled
SIGTRAP
CPUMonitorInterval
Userspace teardown took: %llu ms
%s by %s[%d] for %s failed (%d: %s)
pending spawn, service not yet activated: %s
legacy-load
Disallowing environment variable: %s
%s: urgent log submission key already in stats: 0x%llx
User
disabled
Endpoint with unexpected domain type \"%s\"
Unknown numeric string encoding
NS Extension Info.plist missing NSExtensionPointIdentifier
MallocAggressiveMadvise
multicast group = %s
slaying domain for rebirth
System session daemon must not initiate XPC to the User session: endpoint = %s
copy busy extensions
COMMITTED
subcode
extension already attempting clean exit
load mounted jetsam properties initiated by %s: %s
HostSpecialPort
Policies
Extension
%u
%s: urgent log submission key already in map: 0x%llx
kern.willuserspacereboot
/AppleInternal/Library
SecureSocketWithKey
uuid
com.apple.private.xpc.allowed-launch-types
_ThrottleInterval
_Cryptex
Angel
deferred services = {
arguments = {
userspace reboot into boot mode not allowed: %s
manager
ServiceType
_DextCheckInPort
[%zu] => %s
exited due to exit(%d)
GetResourceUsageSelf
launchd.log: fdopen(%s): %d\n
OS_REASON_TEST
OS_REASON_SPRINGBOARD
UDP
low priority i/o
Bootout error: %d
StartJob
SIGCHLD
PerformInLeanTestEnvironment
init_featureflags
misfired notification: no-senders
Unable to apply LWCR (spawn constraint) - %d %s
EmbeddedHomeScreen
DOMAIN_DEACTIVATE
userspace shutdown timed out: %s (%d).%s
DYLD_PRINT_LIBRARIES
domain deallocated with service stubs
com.apple.xpc.launchd.logq
%s: will reboot if exits with code: %d
ShutdownMonitor
Could not convert value for OSLogClientType to str: %lld
did not initialize jetsam properties category: %s
tcp
no reply expected, failing
AllowCrash
CSIdentityOverride
kern.hostname
SoftResourceLimits
Invalid Arguments
%s failed: conclave id too long
com.apple.fsevents.matching
Non-entitled process tried to control service \"%s\": %s.%d
controller-supplied arguments = {
ui focal
port has message from obliterator or kernel
Flushing logs before initialization. Early logs may not be written to file.
launchd_upward_connections_support=
FileSize
Could not create socket for resolved listener (family = %d, type = %d, protocol = %d, idx = %lu: 
system support
Could not make system logger socket world-writable: error = %d: %s
Invalid environment[%zd]: %s
service inactive: %s%s
fsck
/System/Library/xpc/foreground_user_endpoints.plist
extension timed out trying to exit; killing
domain deallocated with services
SyncInterval
der_vm_integer_from_context
v8@?0
hppa
der_validate_dictionary
shell
EnablePressuredExit is not compatible with KeepAlive=true. Ignoring EnablePressuredExit.
StandardErrorPath
Unable to unpack container_id
ignoring spawn reason '%s' due to filter
der_vm_execute_select_longest_matching_key
jetsam-properties
Refusing to make a port for a canceled endpoint
__config
PersonaEnterprise
_OmitSandboxParameters
_LimitLoadToDeviceTree
MallocMaxMagazines
sysctl hw.jetsam_properties_product_type was not set
com.apple.private.xpc.cryptex.terminate
service exceeded successive crash limit. launch will be throttled
The endpoint \"%s\" defined in plist already exists and is owned by: %s
%s is not an int, ignoring
Unable to open stdin path (%s)
fstatfs failed, treating ownership as untrusted: %d: %s
v24@?0Q8@16
com.apple.xpc.launchd.domain.user
uid = %u
force
Could not activate socket named \"%s\": %d: %s
Could not convert value for OSLogRateLimit to str: %lld
argv
returning username for get_uid_for_token: %s
%s:
no services found in persistent object
persisted submit job failed: service = %s, error = %d: %s
kern.maxfiles
restore-datapartition
Failed to open() socket parent directory: path=%s, error=%s (%d)
timed out initial on-demand mode for a multiuser device
bundle cache = 
v16@?0^{_launch_event_realm_s={_launch_object_s=^vB}{?={?=^{_launch_event_realm_s}^^{_launch_event_realm_s}}}{?=^{_launch_dictionary_s}{?=^{_launch_event_realm_s}}^{_launch_event_realm_s}^{_launch_dictionary_s}Qb1}{?=Q}}8
event
LogFileVerboseMetaLimit
\t<string>%s</string>\n
%s is not supported by the domain, ignoring.
Attempting to select a data value from a non-data DER object
Plist preprocessing failed, rejecting
ResolveProgramIdentifier
Nice
[
retain only = %s
Removing unexpected event endpoint: %s
OS_REASON_JETSAM
LaunchAgent
Killing sender of bogus IPC message: %s.%d
device-recovery
kern.osproductversion
joining jetsam coalition of %s: %llu
underflow of service activation count during deactivate. Managed:%d. Domain: %s. Service:%s
service stop (%s)
matched domain attach request on creation
com.apple.
AutomationOnly
extension already interrupted clean exit attempt
Data corruption: CoreEntitlements has aborted due to an unrecoverable error
Sandbox
additional-properties
jetsam soft port limit = %u
managed-lwcr
mount-point
recursivelyValidateEntitlements
unrecognized launch diagnostic thread type: %u
Conclave can only be set on trusted services
Non-empty dictionary property on MachService: %s
successful exit
found multiple jetsam property plists for category %s
bundle ID = %s
minimum runtime = %u
Found roots installed cookie
Failed to enable service %s, error=%d - %s
Obliteration
der_vm_execute_select_index
Disallowing panic-on-crash behavior for non-system service
jetsam-flags
could not chown mobile/mobile %s: %s
Caller tried to import service with same label as an existing service: path = %s, caller = %s[%d]
attempt to watch an active endpoint
validate_V0
migration
USER
mips
pc
inferred program
com.apple.launchd.helper
Info
no 
cannot reset service active pid-local endpoints: %s
der_decode_key_value
BinaryOrderPreference
v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
, time-to-relaunch: %ums
Calling into AMFI to enable REM.
no jetsam property overlays found in persistent object
StartCalendarInterval
Could not parse plist: path = %s, error = %d: %s
caller removing service: caller = %s[%d]
(confusing)
Device unlocked %qus ago
Could not opt into %d MB Jetsam high watermark: %d: %s
pended spawn = %s
paths
ForceEnableHack
it disabled initgroups
The launch(3) APIs cannot be used to check in MultipleInstance endpoints.
session_uid
controller attached, spawning
outgsk
creator euid = %d
Skipping remaining service endpoints for importance boosting.
bootstrap
cpumon = %d%% over %u seconds
disable resliding
System shutdown initiated by kernel - launchd got a SIGTERM
OS_REASON_REPORTCRASH
Re-opening serial log (error: 
incomplete CPUMonitor, ignoring
vers
reqs
BOOTOUT_SEMI_ACTIVE_SERVICES
service-ctl-reply-port
bundle id = %s
LogToFlatFile
couldn't handoff a spawn, asynced away
extension alive = %s
reslide shared cache
MaxExitTimeOut
array decoding failure
Ignoring launch events for a bundle
init-exclavekit
EndpointSecurity
_PanicOnCrash key: PanicOnCrashDeadline overflowed converting to ns (%lld)
Polling for lingering coalitions stopped
attempt-unload-protected
Event stream %s is already monitored by %s, ignoring
kern.osrelease
reading active trial factors from %s
%s%s%s
%s <%s>: %s\n
Message buffer was shorter than mach_msg_header
type = %s
Emergency
not setting boot-mode to hw.osenvironment due to USR to boot-mode
incomplete work
default environment = {
Efficient
jetsam memory limit (inactive) = (unlimited)
envvar
An extension-removal request failed, error: %d - %s
BundleProgram
com.apple.private.xpc.launchd.allow-submit-launch-angels
com.apple.xpc.launchd.spawn
%s spawn failed: %d: %s
trampolined = %s
needs proxy
Service attempted to specify secure socket key with reserved name: %s
<-%s[%d]
jetsam
path = %s
flags = 0x%llx, 
signing-identifier
undefined boot task %s
PerformAfterUserspaceRebootOnly
XPC Service Info.plist is missing XPCService dictionary
EnableGlobbing
com.apple.private.xpc.persona-manager
Abandoning lingering coalitions
EX_USAGE
in
inetd-compatible
com.apple.keyboard-service
ExecuteAllowed
controller = %s.%d
service enumeration
unset domain environment
handles
Booting non-external volume, skipping boot-task: %s
recursion limit reached
bundle path = %s
crash behavior = %x
_POSIXSpawnTelemetryPageIn not allowed
%s cannot be run directly.\n
tle system
SIGPIPE
endpoint deallocation while still in domain list
EnableCheckedAllocations=>false is not allowed
jp-priority
killing extension hanging on launch
system shutdown
ProgramArguments is not an array.
Failed to dirname_r() socket directory path: path=%s, error=%s (%d)
userspace shutdown timed out: %s. Unable to identify lingering coalitions.
configurable
Standard
MultipleInstances
Wait
RecoverOnCrashDeadline
com.apple.xpc.launchd.bglogq
Bootout
Denied access to socket; caller = %s[%d], trusted = %d, error = %s: %d
service jetsam coalition to join = %s
reading known trial factors from %zu paths
started suspended = %s
needs implicit endpoint
exclaves-boot
multiple invocations of death handler for domain
boot task is not a platform binary (%s, %s)
der_decode_utc_time
XPCService
Unknown key for Boolean: %s
stderr path = %s
OS_REASON_METAL
Failed to basename_r() socket directory path: path=%s, error=%s (%d)
/System/Library/LaunchDaemons/com.apple.jetsamproperties
errors
v28@?0^{_launch_domain_io_s={_launch_object_s=^vB}{?=*{_xpc_token_s=IIIIIiii}Q^{dispatch_queue_s}@?@?^{_launch_array_s}ICb1}}8^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iS
Failed to bootstrap path: path = %s, error = %d: %s
Aqua
LAUNCH_KEY_SETUSERENVIRONMENT is only valid for user domains.
SystemCalls
SystemApp
Umask
cwd
jetsam hard file descriptor limit = %u
SIGBUS
XPC_FLAGS=0x0000000000000000
der_decode_boolean
LaunchInstanceID
Unsupported type for _LimitLoadToBootarg
Skipping remaining instance endpoints for importance boosting.
aborting trampoline
pending bootstrap lookup during user switch: name = %s, requestor = %s[%d]
Either %s or %s must be present
tzinit
@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Thu Oct  8 00:42:48 PDT 2026; root:libxpc_executables-3298.52.1~4/launchd/RELEASE_ARM64E
Invalid type for environment variable value (env/type): %s/%s
%s/launchd.log.2
SIGTERM
noop
Failed to fstatat() old socket path: path=%s, error=%s (%d)
usrctl(0x%x) returned %d (errno %d)
AppExtensions
Exponential throttling is in effect for %llu seconds.
launchd_log_verbose_meta_limit=
Service plist does not specify a label.
soft
SIGUSR2
Could not create system logger path: error = %d: %s
Unknown DER entitlements encoding
JoinExistingSession
completed urgent log submission for %s; pid = %d, version = %d, rtt = %llus
Unexpected shutdown transition %s -> %s
SockFamily
event monitor
Booting-out existing multi-instance extension with different path: existing = %s, conflicting = %s
Bundle Info.plist at %s does not have a CFBundleIdentifier
spawning %zu deferred services
interval
not XPCService
\"%s\" => %s
failed activation: name = %s, flags = 0x%llx, requestor = %s[%d], error = %d: %s
kern.maxprocperuid
v16@?0^{?=[2^{_launch_dictionary_s}]I*}8
LAUNCH_SHUTDOWN_TEARDOWN
Found lingering process: %d (%s)
could not signal service for %s: %d: %s
low priority background i/o
removing semi-active service: %s
xpc-domain
ResidentSetSize
bool, 
setup_fds bad dest: %d table: %d
Unable to merge spawn constraints
SockServiceName
requestor = %s[%d], error = %d: %s
extension removal
Root node of launchd.plist is not a dictionary.
%s is less than zero. Ignoring.
ShutdownTimeout
com.apple.private.xpc.launchd.per-user-lookup
(unspecified)
wait4-status
/usr/libexec/xpcproxy
OK
Non-system service tried to claim host-special port: %d: %s
is from a cryptex
Memory limit override file is present, disabling memory limits.
SIGTERM timeout
removing job: caller = %s
instance-uuid
%s.%s
_LightweightCodeRequirement
Secure socket path is not a socket; path=%s
CPUMonitorInterval is out of range, ignoring
Unable to parse MRM cache
Failure info has no line number.
PerJobMachServices
failed to validate remapped services header: %d
Service did not exit %u seconds after SIGTERM. Terminating with a crash report.
denying spawn, domain shutting down: %s
POSIXSpawnType
com.apple.remoted.service
Invalid value for MultipleInstances '%s'
Early boot complete. Continuing system boot.
der_decode_numeric_string
Quiescing queues
v20@?0^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1b1b1}}8i16
(unknown)
service will use proxy because %s
timestamp
If you rely on this key, please file a bug.
AbandonProcessGroup
EnergyEfficiencyMode
kern.proc.all
exiting ondemand mode
uncorked
kill service (%s)
Remove subscription with token %llu
os-reason-code
persisting service %s (%s) into %s
jetsam properties object is not an array
maxfiles
(signal info malformed)
Unknown data encoding
boot-mode set by sysctl: %s
InactiveSoftMemoryLimit
_RecoverOnCrash key: RecoverOnCrashDeadline invalid. Ignoring.
speculatively converted service to spawned, but spawn failed with error %d
Did not import service from caller: path = %s, caller = %s[%d], error = %d: %s
pushBackMulti
_LaunchWatchdogTimeOut
One-shot property mismatch: requested=%d existing=%d
bool decode failure
com.apple.xpc.launchd.eventq
SystemLoggingSocket
%8s %6s \t%s
cannot spawn: service is throttled
Failed to kill extension. It may linger forever: %d: %s
username = %s
service stubs = {
cache
datagram
service spawning, defer stopping
canceling penalty-box spawn
activation of deactivated domain
(submitted by %s.%d)
Tried to set a reserved task special port: %d
launchd_log_serial=
invalid xpaths type
slaying domain
%s boot task not present
SockPathMode
pending lookup during user switch: name = %s, requestor = %s[%d]
invalid syscall mask key: %s (%i)
managed = %s
MaterializeDatalessFiles
Provenance data too big: %zu
kern.osreleasetype
service print
last exit code = (extension watchdogged)
Setting sysctl kern.darkboot to %u
LAUNCH_KEY_SINGLEUSER never did anything anyway.
Cannot set boot-mode after it has been committed: (%s, %s)
Failed to create the implicit endpoint
urgent log submission = {
overlay
Bogus TaskSpecialPort number: %d
launchd_sync_interval=
__XPC_
bundle-id
exit timeout = %u
jetsam address limit = %llu
unpend launches
LAUNCH_KEY_UNSETUSERENVIRONMENT is only valid for user domains.
persistent jetsam properties object is invalid
Service specifies _PersistToBootMode which is not permitted for services that were not dynamically submitted
com.apple.xpc.datastores.publish
active config locked = %d
PID
app
mobile
 [%s]
failed to add extension %s: %d - %s
attempted to petrify a service that hasn't been animated
_LaunchEvents
InitialTaskRole
Default
original = %s
bringup time = %llu ms
Rejected invalid request.
der_vm_execute_nocopy
%d.%d
Version
EX_IOERR
Tried to set a reserved host-special port: %lld: %s
der_vm_execute_integer_value_allowed
com.apple.xpc.launchd.serialq
This key does not do anything: OnDemand
TCP
LaunchDaemon
der_vm_execute_match_integer
Platform
UNPEND_REQUESTS
SystemLibraryTreeState
\"%s\" = {
service only configured to run once, removing
extension canceled clean exit attempt
jetsam thread limit = %d
SystemCallMasks
_PanicOnCrash key: PanicOnCrashDeadline less than zero. Ignoring.
$or
abandoning languishing service
Service did not exit %u seconds after SIGTERM. Sending SIGKILL.
shared region config flags = 0x%x
disabled services = (no disabled services)
PerformAlways
PerformInBaseSystem
can't ask for the string for 'none' boot mode!
Activated a directory (%s) and found no files
Invalid type for socket dictionary (key/type): %s/%s
%u:%s 
last exit code = %d
Failed to register daemon notification endpoint '%s': %s
/var/run/utmpx
<dict/>\n
com.apple.private.xpc.unauthenticated-bless
%5d %10d   %-25s   %s
Unable to reload kern.osversion: %d
XPCServiceEndpointNonLaunching
%s/overrides.plist
Unentitled submitter specifies _PersistToBootMode in service, which is not permitted
Bug in libxpc: mach_port_construct() failed
Daemon
Unsupported value for EnergyEfficiencyMode: %s
attrs
darwinos-boot-task
XPCServiceEndpointPort
der_decode_data
active = %s
jetsam priority = %d
on-system-volume
Alert
der_vm_execute_match_bool
key contains an embedded NUL
domain has no corresponding special port entry
uniqueid = %llu
mach-register
attempt to cancel notification on non-existent port entry
LogAllBootstrapErrors
Disabled
Service: %s has leaked sockets
DisallowAllLookups is not supported for non-System services.
%s cannot be run directly (stdout: %d)
CONFIGURED
Service attempted to %s environment variable with reserved name: %s
/etc/nologin
lockdown.
CoreEntitlements: unknown DER type
WAITING_ON_QUIESCE
system reboot
com.apple.%s
der_vm_execute_string_prefix_value_allowed
Crashed
creator
Could not import service from caller: caller = %s[%d], job is not a dictionary
%s: _ExperimentalNonLaunching is not compatible with HideUntilCheckIn, ignoring
der_decode_next
Extension is hanging on launch. Killing.
service bootstrap (%s, io flags=%#llx, eval flags=%#llx)
%#8x %-4u %12s  %s
gui/%u
boot task dictionary is not populated
Unknown property %s for PublishesEvents
Could not cleanly tear down userspace. Will force a full hardware reboot. (%s)
base minimum runtime = %u
CACHE INVARIANT VIOLATED: %s | %s != %s
shutdown
UNINITIALIZED
bundle_identifier
Could not unlink previous system logger socket: error = %d: %s
unable to decode value size for key-value pair
LimitLoadToHosts
Failed to stat() socket directory path: path=%s, error=%s (%d)
system xpcservice
xpcproxy
com.apple.xpc.launchd.domain.system
Wipe them out. All of them.
RebootOnSuccess
XPC_FLAGS=0x%llx
com.apple.private.xpc.service-instance-manager
force-kill
process-info-pidinfo
subdomains = {
failed to merge persisted jetsam property overlay[%zu]: %d
AbortOnUnknownIPC
abandoned
unthrottle
angel
framework cache = 
com.apple.private.xpc.launchd.enable-disable-system-services
x86_64
Dropping coalition notification from unknown source (%llu)
maximum allowed shutdown time = %d s
Entitlements element not allowed
com.apple.xpc.launchd.ioq
@bundle {
signaled service: %s
XPC_IN_REM_DEVELOPMENT
#IfFeatureFlagDisabled
ports
forks = %hu
devicerecoverytool
Malformed boot-task (missing block key): %s
\t<key>%s</key>\n
OSLogRTBufferConfig
refusing to read cache protected location from disk: %s
active
penalty box
mach-lookup
com.apple.quarantine
EX_UNAVAILABLE
Unknown
Unknown boolean encoding
AppleKeyStore
control
active count = %d
booting out service
/System/Library/LaunchAngels/
status
diagnostics
InactiveHardMemoryLimit
SystemXPCService
role account
GetJob
CheckIn
kern.workload_config
.roots-installed
Service instances do not support XPC events.
Unsupported type for index %lu of _LimitLoadToDeviceTree
clearing pending urgent log submission for %s; pid = %d, version = %d
security.mac.asp.willshutdown
DYLD_PRINT_REBASINGS
proxy
Unmanaged service with non-dynamic endpoints: %s
SanitizersAllocationTracesDurationInSeconds=172800
EXITED
Extension remained dirty for too long after trying to exit. Killing.
port = 0x%x%s
Unknown key for dictionary: %s
Unix
xpcproxy exited due to %s
Service could not initialize: %s, error 0x%llx - %s
ServiceIPC
EX_OSFILE
its working directory has been overridden
Could not import service from caller: path = %s, caller = %s[%d], error = %d: %s
failed lookup
number too large
CPUSubtype
IPv6
EX_CANTCREAT
could not set create %s: %s
Failed to create a job monitor. error = %d: %s
SIGSEGV
SIGPROF
encountered invalid element in an array
comp
udp
SOURCE_ATTACH
last exit code = (never exited)
unmanaged processes = {
attempted to enter REM in unsupported variant
%s | %s
Could not get Info.plist for bundle at %s
EventMonitor
Failed to fchown() secure socket directory: path=%s, uid=%d, gid=%d, error=%s (%d)
com.apple.private.xpc.launchd.storage-mounter
Missing ProductBuildVersion
tal
SetResourceLimits
OS_REASON_WATCHKIT
com.apple.private.xpc.launchd.persist-to-boot-mode
EX_SOFTWARE
endpoint destination = %s
RequireSuccess
mig-request
Cryptex can only be set on trusted services
_autounlock
deferring exec source uncork
hardened-ipc = 1
failed to marshall spawnattrs: offset = %u, left = %lu, expected = %lu
LowPriorityIO
Please use JetsamProperties instead.
Error during cryptex termination: %d - %s
launchd_cache_loader
/private/var/db/launchd.db
Socket entry is not a dictionary or array. Skipping: %s
caller failed %s sandbox check on path %s
Could not convert value for MallocMaxMagazines to str: %lld
attempt to watch socket that is already watched
will attach to %s next time it's created
GetJobs
active count = %llu
passive = %s
Too many instances (%d >= %lu : %d), but nothing to slay since all instances are already being removed.
subscriber-pid
Exceeded max diagnostic thread count for type %s (%u)
Invalid item %s in PublishesEvents, expected dictionary or bool
successfully submitted persisted service: %s to %s domain
SIGINT
recovery-mode
_HighBitsASLR
com.apple.private.xpc.launchd.job-manager-remove-any
extension is being stopped
supports idle hysteresis
instance = %s, 
UserPaths
Service specifies no Program and empty ProgramArguments.
failed to process path: %s: %s: %d
HOME
removed
finish-demo-restore
misfired notification: dead-name
boot-mode committed: %s
com.apple.private.xpc.launchd.allowed-coalition-quiesce
Unknown socket key %s
Failed to kill hanging extension: %d: %s
default-enabled
request
Could not stop service: name = %s, error = %d: %s
uncorking exec source upfront
urgent log submission completed, pushing out %llu more seconds
pended
failed to boot out inactive service during obliteration; socket event
session = %s
JetsamProperties loaded from path : %s
invalid syscall mask array type (%i)
services[%zu] is missing or has invalid xpc-domain key
/private/etc/com.apple.xpc.launchd.limits.plist
_AdditionalSubServices
RemoteServices
SanitizersAllocationTraces=tagged
%s: exited successfully, removing
persona can only be set on submitted jobs and extensions
it set an io priority
ThrottleInterval set to zero. You're not that important. Ignoring.
Failed to unlinkat() old socket path: path=%s, error=%s (%d)
:
INIT
spawn role = %s (%lu)
is copy
Socket entry is not a dictionary. Skipping: %s
checked allocations
cannot spawn: service is configured as retain only
inactive
refusing to add a duplicate domain: type=%s handle=%lu
Unable to unpack cwd
removing active service: %s
Could not create system logger socket: error = %d: %s
Saved the port to stash
caller failed file-write-create sandbox check on grand parent directory %s
Could not reap abandoned service instance: %d: %s
no requestor found for token %llu
LogToConsole
service will always use xpcproxy, elision was disabled by boot-arg
invalid jetsam property category type: 0x%x
receive_packet_info = %s
service stats = {
launch job demand
launchd
controller-supplied environment = {
NSBuiltWithThreadSanitizer
Service only ran for %llu seconds. Pushing respawn out by %llu seconds.
exited due to %s
environment
vm.shared_region_pivot
com.apple.xpc.launchd.xsc.plist_key
seqpacket
runs = %u
spawn type = %s (%lu)
pending attachments = {
variant
UseNanoAllocator
Lean Testing Environment starting.
removing service since it exited with consistent failure - %s
persist to boot modes = {
uncorking exec source for disposal
no-einprogress
--recovery-reason
The %s key is not yet implemented. %s
com.apple.private.xpc.domain-extension.proxy
launch watchdog timeout = (globally disabled)
server
Service: %s has leaked endpoints
+ %d MB
com.apple.launchd.calendarinterval
service has crashed %u times in a row (last was%s dirty)
xpcproxy exited due to exit(%d)
extension attempting to exit cleanly
going into initial on-demand mode for a multiuser device
trial factors reload initiated by %s[%d]
Service was sent unexpected signal: %s
xpc bundle
mode = %o
ipv4
environment = {
An extension-removal request is already in flight; chaining
Missing conditions
Start job failed: error = %d: %s
Child
InternalOnly
com.apple.private.xpc.launchd.reboot-pivot-root
Already registered ports
boot-args = %s
/System/Library/DeveloperModeLaunchDaemons/
mach_ports_lookup() failed: %d
no bootargs string
yesno
Failed to disable service %s, error=%d - %s
Service has increased maximum shutdown time to %d seconds. This will create a poor experience for the user.
%s/
%s is out of range, ignoring
empty boot-mode name given
68k
multiple will-spawn events received
error parsing the workload properties plist in the kernel (%u)
HardPortLimit
com.apple.private.xpc.launchd.loginitem-outside-bundle
false
SoftFileDescriptorLimit
rerouted lookup to a foreground user endpoint: name = %s, caller = %s[%d]
validating %zu jetsam property overlays
Unrecognized MachService property: %s
kern.minimalboot
/var/mobile/Library/Accessibility/ClarityBoardEnabled
Loading Cryptex overlay plist from: %s
Successfully spawned %s[%d] because %s
 [%lu]
SystemPersonaServices
XPC_USERSPACE_REBOOT_TO_BOOT_MODE
com.apple.launchd.QueueDirectories
com.apple.private.xpc.launchd.job-manager
Removing unexpected non-dynamic endpoint: %s
com.apple.xpc.launchd.unmanaged.%s.%d
added unmanaged active
service read
service will always use xpcproxy because %s
Please remove it.
_PanicOnCrash key: InternalOnly not enabled in the current environment
domain deferral
persona id = %u
launchd_proxyless_spawn=
validate_VNext
Unknown key for double: %s
v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
_BTMItemUUID
%s%s
unix
hardlimit
SIGUSR1
rec_execcnt
throttling
/System/Library/Trial/AllowedFactorsAndDefaults
%d
%s/disabled.migrated
String contains an embedded NUL
_Protected
endpoint
services[%zu] is not a dictionary
non-launching = 1
der_vm_execute_string_value_allowed
com.apple.private.xpc.launchd.allow-set-bundle-path
Will be calling reboot(2) with flags: 0x%x
Invalid socket name: %s
cid
binary order preference = {
inherited
Queried sysctl kern.darkboot: %u
sub-sequence size is larger than sequence size
PublishesEvents
draining messages from %s
last exit code = %d: %s
%s coalition = {
StopJob
fips
EX_PROTOCOL
Rebooting now, so the finish-obliteration boot task can clean things up.
launch_max_exit_timeout=
unsupported IO type %d
SockPathName
sparc
domain disposal while still in the children list
logout
restoring %zu persistent services
RunLoopType
AlwaysSIGTERMOnShutdown
GroupName
NetworkState
%016llx
monitor
persona set at = %u
has spawn constraint
Accessibility
LegacyTimers
legacy-service-lookup
names
(no bundle cache)
data-protection
unknown IPC
 (dead)
EmbeddedMainThreadPriority
jetsam property category (%s) is not initialized
abandon during shutdown
SIGXFSZ
]
service bundles => 
working directory = %s
Could not spawn dedicated inetd instance: %d: %s
created the implicit endpoint upfront
monitor_id
.DarwinDepot
rem
Invalid type for a LaunchEvent stream, should be a dictionary (stream/type): %s/%s
ActiveLowLevelFactors
app (nonui)
rem-enable-fuse
xpc demux succeeded
launchd_instance_limit=
%s not permitted to be set on non-submitted jobs
init-with-data-volume
ProcessType
%s by %s[%d] for %s succeeded (%d: %s)
com.apple.xpc.launchd.unmanaged.confusing.%d.%d
envvars
reentrant call into server layer
Invalid item type %s in PublishesEvents, expected string
state = %s
%s - 
Failure info has no image UUID.
invalid type for persistent service[%zu]
_MultipleInstances
Failed to import key SpawnConstraint - %d: %s
Failed to connect() a socket: path=%s, error=%s (%d)
Large
+ %s
(premature birth)
_LimitLoadFromVariant
%s is being activated by a mismatched domain %s. Managed:%d.
%s/launchd.log
RequireDomainBinding
Service plist has an empty label.
marked
launching: %s
suspended
rootport
fixup-mobile-tmp
SIGTERMed
no name, failing
Async boot task %s must not have flags
security.mac.amfi.developer_mode_status
file-write-create
SHELL
CFBundleVersion
cannot reset service active unmanaged endpoints: %s
invalid tag or length
SockPathOwner
Shutdown
GroupName is not supported by the domain, ignoring.
XPC bundles can't have KeepAlive, they can't even set it as a plist key, how did we get here?
_PanicOnCrash key: AutomationOnly not enabled in the current environment
high bits aslr
required
EXEC_EXIT_REASON_FAIRPLAY_DECRYPT
Unknown string encoding
UserEnvironmentVariables
attempt to ignore canceled socket
mark
Unknown key for integer: %s
Unsupported type for index: %lu of _LimitLoadToBootarg
XPC_FLAGS
state
Start job failed: service = %s, error = %d: %s
/sbin/launchd
rebooting after success
RecoverOnCrashCount
service has crashed into the shared cache area
rss
/private/%s
Debug
_SubsystemRoot
Cannot remove old socket path; UIDs mismatch: socket owner=%d, path=%d
AlternateSystemApplication:
BaseSystem environment starting.
Could not resolve CFBundleIdentifier specified by service: %d: %s
setup-event
trampoline
it set a non standard working directory
Version4
cpumon = default
unmanaged service deactivated with active pid endpoints
exception
failed to lookup domain for persisted service
kern.maxfilesperproc
libdispatch bug: Unknown send-right
launchd has not fixed mobile/tmp (socket)
com.apple.xpc.launchd.xsc.container_id
languishing
xpcservice-dict
enabled
Found unsupported directives
/usr/lib/system/libsystem_trace.dylib
kern.maxproc
_LimitLoadToVariant
_ProvenanceData
Global
 %llu (%s),
targetpid
der_decode_number
com.apple.private.xpc.is.xpcproxy
task-special ports = {
Setting service %s to %s
IOMatchLaunchStream
SIGKILL
_JoinGUISession
com.apple.launchd.PathState
Feature disabled, device would have rebooted due to %s
kern.syscall_rejection_masks
gathered %zu services to persist into %s
CrashOnSIGTERMTimeout
%s =>
secure key = %s
Unable to create stderr directory (%s)
kernel
bound interface = %s
keepalive
job not found, returning ENOSERVICE to %d with manual pipe reply
OS_REASON_DYLD
NumberOfProcesses
REMOVE_ALIASED_ENDPOINTS
xpcservice
system app
EX_NOPERM
endpoints = {
instances = {
jetsam soft kqworkloop limit = %u
cannot abandon languishing service: %d
%s: caller = %s, value = 0x%llx
labels
%s|%s
launchd_workload_properties_disabled=
attempted to pre-animate dispose an animated service: %s
system
MobileAssetEarlyBootTask
Sockets
com.apple.private.xpc.conclave.submit
socket deallocated while still active
unmarked
copy count = %d
_dirty
parent
capacity
[%s]: %s\n
Submitted
loaded
 %s
validating %zu persistent services
filesize
posix_spawn(): %d: %s
fvunlock
its binary is missing or not executable
Failed to set %s: %d - %s
voluntary exit timeout = %u
bootout
os-reason-ns
dictionary keys are not sorted or not unique
com.apple.cryptex.app
inherited environment = {
SIGTTOU
Invalid type for %s importer (key: %s type: %s), accepted types: [
node name = %s
Got dead control port
missing token in request from pid %d
Failed to %s endpoint '%s' as throttled
der_vm_data_from_context
der_decode_string
Program
Please switch away from OnDemand to KeepAlive.
AssociatedBundleIdentifiers
last exit reason = %s
Unprivileged caller tried to check into job's endpoints: caller = %s.%d, owner = %s
initial-load-completed
XPC API Misuse: %s
EXAppExtensionAttributes
EX Extension Info.plist missing EXExtensionPointIdentifier
iOSSupportVersion
DYLD_PRINT_RPATHS
umask = %o
inetd listener
denied lookup
can not find service for caller pid %d
background
no value for key: %s
shutdown timeout
ipv6
powerpc
kill
non-launching
launchd logging initialized. name: %s pid: %d
jetsam soft file descriptor limit = %u
label override
provides events
System logger socket was not opened during early boot. (Proceeding anyway)
Cannot abandon languishing service: %d: %s
denying spawn, invalid reason (%d) for PID domain service: %s
Could not create new instance of inetd service: %d: %s
boot task %s key %s must be an array of strings.
it has a control port set
_AbandonCoalition
CPU
%s (approx)
redriving pending stop
Service cannot reset: active event channels
signal service
Failed to activate endpoint for legacy check-in. Please just don't use this API: %s
extension check-in timeout
+ (unlimited)
jetsam conclave memory limit = %u
_PersistToBootMode
com.apple.private.domain-extension
com.apple.private.xpc.launchd.loginitem-bootstrapper
_executablePath
service not running, not stopping
_LimitLoadFromBootarg
ClarityUI
Old socket path is not a socket; path=%s
_objectForActiveContext
arm64
bootout initiated by: %s
XPC_SERVICES_UNAVAILABLE=1
der_validate_array
Managed
enable
The launch_msg(3) API may only be used on the system or user domains.
read resource usage
prng_seedctl
RELEASE
string_value_allowed_iterate
Driver
Ignoring events for retain only services
KeepAlive
matched global attach request before spawn
disable
system services must be in cache
Failed to fchownat() a socket: path=%s, uid=%d, gid=%d, error=%s (%d)
EX_DATAERR
originator = %s
query
kern.initproc_spawned
results
XPC_USERSPACE_PIVOTEDROOT
mc88000 (ain't got nothing on mc98000)
supports transactions
ProgramArguments is not an array of strings.
LimitLoadToHardware
v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
_imagePathToInfo
exited
non-system session had no name
 (initiated by %s)
SanitizersAllocationTracesMemoryBudget=production
load-jetsam-properties
no client port found
SupplementalPaths
_PanicOnCrash
ProductVersion
reload-error
SystemRoots
Program specified by service does not contain any valid architectures for this system.
line
JETSAM_REASON_MEMORY_LONGIDLE_EXIT
XXXXXXXX%s=%s
count
Failed to fchmodat() a socket: path=%s, mode=%o, error=%s (%d)
/dev/null
IOGeneralInterest
Obliterator task exited: %s
Invalid XPCService dictionary.
keybag
launchd_disable_all_timeouts=
_SandboxContainer
Bug in libxpc: mach_port_assert_attributes() failed
Restore
service name = %s
failed to query memory status priority for PID %d: %s (%d)
inconsistency between domain and service semi-active state during semi-active bootout
externally-hosted endpoints = {
WRITE_DISABLED
Critical
der_vm_execute_match_string
_LimitLoadFromDeviceTree
CPUMonitorPercentage
rebooting due to %s
caller (PID %d) is not allowed to signal target process: %s
launch watchdog timeout = %u
%s (soft) => %s
Not calling into AMFI to enable REM.
service \"%s\" tried to claim task-%s port from endpoint \"%s\"
Size limit for Datastore entry not specified: %s
leader-pid
properties
OS_REASON_AGGREGATED
Boot task failed: %s
ElideRoleAccountSetupPathPrefixes
WorkingDirectory
DrainMessagesOnFailedInit
READY_FOR_REBOOT
event publisher
kpersona_find_by_type() failed with ret %d errno %d - %s
mount-phase-1
RebootOnExitCode
LOGNAME
global
Unable to unpack argv
LastExitStatus
Could not import service from caller: caller = %s[%d], service = %s, error = %d: %s
failed to restore persistent object: %d
/usr/lib/system/libsystem_notify.dylib
deallocation of active service
Invalid CPU type value type specified: %s
MallocStackLogging
OtherJobEnabled
No PATH environment variable set. The application firewall will not work with this service.
Service setup event to handle failure and will not launch until it fires.
service-name
disk will be searched for uncached services
%s/launchd.log.1
OS_REASON_EXEC
watching = %s
active config = {
Unexpected error when looking up endpoint: %s
Domain creation failed: it already exists
validation-category
Attempting to select an integer value from a non-integer DER object
A memory allocation has failed
UserName
Failed to open() socket directory: path=%s, error=%s (%d)
setup_fds bad int type
semaphore
submitted job. ignore execute allowed
userspace reboot
ExtensionWatchdogTimeout
_AdaptiveUtility
object, 
OSLogClientType
com.apple.private.xpc.service-configure
could not get unique pid
query service enabled state
userreboot_purpose
kern.bootobjectspath
RecoverOnCrash
set domain environment
OS_REASON_SIGNAL
An empty dictionary needs to be used as the value for %s.
SuddenShutdown
Failed to import key %s - %d: %s
ps telemetry page-in
service deactivated with active instance endpoints
%s: name = %s, 
LoginWindowUserName
com.apple.private.xpc.launchd.allow-posixspawn-telemetry
could not set up inheritance port
SockProtocol
out-of-order spawn event received
The endpoint name %s is too long to support some features
launchd_sudden_shutdown=
Unknown UTC Time encoding
Loading DDI overlay plist from: %s
Unable to unpack environment
service bootout (%s)
Assuming EnablePressuredExit=false given EnableTransactions=false.
service
last exit code = (failed reap)
commit-boot-mode
attempt to re-enter the server layer
ServiceStubsDisabled
SanitizersAllocationTraces
socket deallocated while still in service list
cryptex = %s
peeking at message: seqno = %u, pid = %d
service will attempt to elide xpcproxy
LimitLoadToDeveloperMode
EnterKernelDebuggerBeforeKill
caller failed %s sandbox check on parent directory %s
Start job failed: another start request is already inflight
Flushed %lld logs [limit: %d]
ipc: caller = %s.%d, subsystem = %d, routine = %d, %s
(system logger socket)
legacy shutdown initiated by: %s
coalition-id
no mach port for persistent services: %d
launchd_usr_abandon_unmanaged=
EnableHardenedIPC=>false is not allowed
/usr/lib
Cannot look up instances for shared endpoints.
(no daemon cache)
Service stub initialized for %s
AppRemovalServices
PATH
EX_TEMPFAIL
os-namespace
Service stub initialization failed for %s [%d]
OS_REASON_WATCHDOG
host-special port = %u (%s)
com.apple.launchd
Unrecognized %s
extension is being debugged; not timing out exit
could not open %s: %s
auto-completing urgent log submission for pid = %d, version = %d
removing unmanaged endpoint: %s
%s (%s)
SIGVTALRM
%s/%s
%s cannot be run directly (pid = %d)
WILL_SPAWN
resolved uid = %d
created
instance creation failed: %d %s
NSExtension
Invalid type for a RemoteServices entry, should be a dictionary (key/type): %s/%s
Invalid special port[%zd]: %d
denied kick request from %s - missing entitlement %s
sanitizers
service deactivated with active endpoints
Async
wheel
com.apple.rootless.xpc.effective-root
managed
pending requests = {
Service \"%s\" tried to register for endpoint \"%s\" already registered by owner: %s
com.apple.private.xpc.launchd.app-server
CheckedAllocations
canceling old domain attach request to %s
PostLogOutSync
BATS_TESTPLAN_ID=
Failed to fstatat() secure socket path: path=%s, error=%s (%d)
com.apple.private.xpc.service-attach
mc98000 (best MC ever)
Given object not of required type.
Active user logout, initiated by: %s[%d]
/System/Library/xpc/WorkloadProperties.plist
stack
Service does not specify a valid argument array.
SoftPortLimit
_infoPlist
The system may be in an inconsistent half-obliterated state.
ExitTimeOut
CANCEL_DEATH_SOURCE
detect-installed-roots
print
instance overrides sandbox container must be a string
\"%s\" exited with signal = %s
Label
after crash
Loading overlay plist from: %s
ThreadLimit
v20@?0^{_launch_array_s={_launch_object_s=^vB}^^vQQ}8i16
Bonjour
Unknown family encountered during multicast group bind: %d
The endpoint \"%s\" would shadow a trusted one owned by %s, ignoring
App
SessionCreate
_LaunchType
com.apple.rootless.xpc.bootstrap
name = %s
deferral event on service waiting for controller
service is still not a zombie, abandoning
%s is being removed from a mismatched domain %s
_AdditionalServices
%s is ignored in favor of %s
cannot spawn: service is in penalty box
 not
v16@?0^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}8
could not find endpoint in pid namespace: pid = %d, name = %s
Domain creation failed: %d %s
sandbox-container
recoveryos
_StandardOutFd
Invalid type (%s) for _ProvenanceData
resource
SingleUser
services[%zu] is missing or has invalid plist key
Core
immediate reason = %s
obliteration complete, sending reply
SPAWNED
Skipping extension launch watchdog
jetsam wired memory limit = %u
Rejecting untrusted event subscription on stream %s
%s not set, Skipping boot-task: %s
PureOnDemand
\t<false/>\n
0
jetsam-memlimit
multiple instances = %s
%s: caller = %s.%d, extension = %s
HardFileDescriptorLimit
com.apple.private.xpc.launchd.allowed-manage-trial-factors
extension point = %s
processing dispatched request
endpoint deallocation while still active
Clamping socket path mode %o to %o
flags
job-state
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
com.apple.launchd.WatchPaths
attempt to ignore socket that is already ignored
Could not find and/or execute program specified by service: %d: %s: %s
could not chmod 1777 on %s: %s
Caller specified a plist with bad ownership/permissions: path = %s, caller = %s[%d]
[%s]: entitlements blob has unexpected version %lld\n
XPCService must be dictionary
_StandardErrorFd
Failed to mkdir() socket directory: path=%s, mode=%o, error=%s (%d)
network-inbound
attempt to watch unmanaged endpoint
SpawnConstraint
Invalid type for _PersistToBootMode at index: %lu
OSLogRateLimit
Non-system service tried to claim task-special port: %d
BundleProgram(%s) is not the same as Program(%s). Bug in ServiceManagement?
Improper type for _RecoverOnCrash key: %s
MulticastGroup
platform binary
disallow all lookups
Failed to stash endpoint %s: %d - %s
launchd.log: open(%s): %d\n
, 
Unable to unpack sandbox profile
shutting down system: flags = 0x%x, time = %llu ms
Could not create copy of service: %d: %s
Error
LAUNCH_DID_REEXEC
multiple-instance service has no initialized endpoints
abandon process group
events
/Library/JetsamProperties/com.apple.jetsamproperties.DDI.plist
v12@?0I8
Can't have both %s and %s
launch only once
MultipleInstance XPC services are not supported for any service type other than Application. Forcing service to PID domain.
kernel returned invalid sender procname for signal
inetdCompatibility
hello, launchd UUID: %s
protocol = %s
throttle
self
service-port
forbidden-launchd-operation
Service tried to register a port for an endpoint declared in its launchd.plist(5): service = %s, endpoint = %s
com.apple.private.xpc.launchd.event-monitor
core
unmark
DisableAllMemoryLimit
Stack
System
failed to fts_open(%s, 0x%x): %d: %s
(submitted by %s[%d])
Rejected bogus request: %d: %s
userspace shutdown timed out: %s
Bootstrap
PETRIFIED
container id = %s
removing
Failed to set hw.mempath
failed to add interest notification
Not allowed to set SockPathOwner to UID %d. Remove key.
Could not find job with label %s
maxproc
UseGuardMalloc
ConclaveMemoryLimit
terminated
DYLD_PRINT_
posix_spawn(%s) failed
blocking xpcproxy until controller configures the service
binpref
user
SIGQUIT
AddressLimit
could not terminate service: %d: %s
key
ess bootstrap_look_up: audit_token_for_pid(%d) → %d for service %s, JOB arm
could not decode size for next DER sub-sequence
%s : %s
could not set protection class on %s: %s
persistent services header size is less than header size
array, 
CoreEntitlements: not a sequence
ReceivePacketInfo
Program specified by service does not contain one of the requested architectures: %s
%s = 
resetting service: %s
keepalive = %s
Service sets EnableTransactions=false and EnablePressuredExit=true, which makes no sense. Enabling Transactions.
/private/preboot
Could not accept new inetd connection: %d: %s
domain is not initialized, can't uncork
Submit job failed. Unable to find domain. Service = %s, error = %d: %s
/var/run/com.apple.launchd.XXXXXXXXXX
Shutdown already started: %s
unsupported cached entry type %d
process-type
/Library/LaunchAgents/
entering ondemand mode
iOSUser
Self
DriverKit
needs_rename = %s
EX_OSERR
Could not monitor job: error = %d: %s
dictionary key is not a valid string
root
RunAtLoad
JetsamProperties plist is malformed - missing Version4 dictionary
/var/run/syslog
, leaving extension group
 (development)
boot-mode forced to (%s) skipping set: %s
Unknown key for array: %s
committing to system shutdown
%s => %s
inefficient
domain already initialized
failed to serialize jetsam properties[%zu]
RemoveOnSuccess
WiredMemoryLimit
ABANDONED
Unable to find managed service for pid %d. Trying unmanaged services
%s.%llu
FairPlay decryption failed on binary.
last jetsam exit details = %s
dropped-count
Shutting the system down has taken too long. launchd is rebooting\n(or halting) the system now. Any processes that are still running\nwill be abandoned to the mercy of the kernel.\n
unmanaged service deactivated with active dynamic endpoints
removing unmanaged pid-local endpoint: %s
slain
justdoit
PackedDataBuffer.cpp
PanicOnConsecutiveCrash
couldn't find domain to attach to %s, error %d - %s
signaled service for %s: %s
initiated at %ld by %s
service = %s
mount-phase-2
/usr/libexec/devicerecoverytool
MallocSpaceEfficient
caller = %s.%d, event = %d
cannot reset service: active instance endpoints: %s
Terminating with cryptex %s, caller = %s[%d]
LimitLoadToBootingExternalVolume
shutting down
(no framework cache)
job-handle
xpcroleaccountd
attempt to watch endpoint that is already watched
No space for special ports: %zu > (%zu - %d)
Error during registration of '%s', Daemon Notification requires _Conclave key
misfired notification: port-deleted
Failed to bind() a socket: path=%s, error=%s (%d)
BOOTOUT_ACTIVE_SERVICES
{
SockPassive
remove all extension instances
developer-tools
hw.osenvironment
com.apple.private.xpc.protected-services
%lu
jetsam hard port limit = %u
%s coalition ID = %llu
SIGTSTP
Unknown key for %s importer (key: %s type: %s)
/System/Library/LaunchDaemons/com.apple.jetsamproperties.NonUI.plist
%a %b %d %T %Y %Z
Cannot setup an event for proxyless spawns!
spawn reason filter = %s
in-progress bootstraps = %hu
com.apple.iokit.matching
Skipping boot-task
_RoleAccount
Could not opt into Always-On VPN: %d: %s
/private/var/log/com.apple.xpc.launchd
Invalid type for event stream (stream/type): %s/%s
Service specifies neither Program nor ProgramArguments.
SharedRegionConfigFlags
com.apple.private.xpc.launchd.per-user-create.mbsetupuser
it is being debugged
kern.roots_installed
token
invalid syscall mask value at index: %zu  (%i)
OS_REASON_LIBSYSTEM
exit(%d)
NoExcResourceDuringAudio
shutdown %s -> %s
Unable to find boot task block for: %s
services
OS_REASON_ENDPOINTSECURITY
XPC_NULL_BOOTSTRAP=1
Verification failed
1
system-wide preflight
pending spawn, service not yet imported: %s
origin
boot
The %s key is no longer respected. %s
JetsamMemoryLimit
XXXXXXXX%s=%s/tmp
abandoning
jetsam memory limit (inactive, %s) = %d MB
waiting for boot-task %s with pid %d
xpc demux failed
endpoint deallocation without cancellation
Could not find exception endpoint for service: %s
Cannot set configure key endpoint on service: service has dext checkin port %#x
boot task argument vector is not an array
extra data at the end of element
WAITING_ON_SHUTDOWN_STALL_REPORT
 during %s
reason
.darwin
Conflicting request: resliding disabled, but requesting a shared cache reslide. No reslide will be performed.
_Conclave
RequireTrusted
DYLD_PRINT_DOFS
attempting to re-add an endpoint into service
EnableTransactions
ActiveSoftMemoryLimit
Unable to create stdout directory (%s)
port
none
iteration over a non-iterable type
der_vm_execute_match_string_prefix
optional cannot be created with zero error
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Sources/libxpc_executables/launchd/service_create.c
StartInterval
Configuration error: failed to fetch our own audit token
retry launch on service that was not deferred
xpc event
service removal (%s)
no elide roleaccount setup path prefixes
Unknown key for data: %s
HOLD_ON
type
com.apple.xpc.launchd.domain.pid
Expected string for a variant, got %s
/usr/lib/system/libsystem_info.dylib
%s (%s) <%s>: %s\n
JETSAM_REASON_MEMORY_CONCLAVELIMIT
_ProcessType
SubmissionTimeout
shmem
persistent object size is %zu bytes
Attempt to share port-destroyed. Ignoring.
rd=md0
/usr/local/lib
error
Abandoning service instance. This may lead to deadlocks.
jetsamproperties category = %s
(unknown reason)
__OSINSTALL_ENVIRONMENT
encountered invalid element in an iterable
service disposal while in parent instance list
ConsecutiveCrashCount
_LimitLoadToClarityMode
extensions cannot run as root
Got first unlock unregistering for AKS events
.xpc
sandbox profile = %s
disable pointer auth
remaining_active_service
%s = {
Abandoning service: %s
failed to validate services header: %d
RamDisk
_LimitLoadToBootarg
%s/%s/%s
OtherJobActive
Found XPCService bundle by executable: %s
disabled services = {
monitor = %s
failed to restore service[%zu]: %d
com.apple.private.xpc.launchd.reboot
%s=%s
service is being debugged, not timing out launch
inetd-compatible service with no sockets.
ds
data
aidearlyboot
.pluginkit
launchd(proxyless)
launch already in progress
src != (A *)data_
integer, 
Unable to create stdin directory (%s)
BOOTOUT_SERVICES
<private>
abandon coalition
LaunchAngel
domain already deactivated
Failed to renameat() passive socket from secure path to known path: secure path=%s, known path=%s, error=%s (%d)
ProductBuildVersion
service-type
semaphores = {
exiting bootstrap mode
Unmanaged endpoint \"%s\" was canceled to transfer the ownership to: %s
pid-local registration
Caller not allowed to perform action: %s[%d], action = %s, code = %d: %s, uid = %u, euid = %u, gid = %u, egid = %u, asid = %u
resolving its UID failed
com.apple.private.xpc.cryptex.submit
ccat
extension
SIGSYS
_launch_log_format failed\n
after the userspace pivot & reboot, os_variant_is_basesystem() should not be true
_StandardInFd
HopefullyExitsLast
__TRIFactors
error = %d
domain disposal while still in the domains list
XPC_SERVICE_NAME
sanitizer flags = 0x%x
Doing boot task
_ManagedBy_Services
_LimitLoadFromBootMode
OnDemand
(animating)
owner uid = %u
initialized = %s
unexpected exec of non-platform binary: %s: %s [%d]
LogIPC
__Angel
will attach to %s next time it is spawned
start service (%s)
com.apple.private.xpc.domain-extension
DYLD_PRINT_ENV
login
ContainingBundleVersion
Frameworks
successive crashes = %u
mach-cross-domain-lookup
JETSAM_REASON_MEMORY_IDLE_EXIT
dictionary key / value decoding failure
ProgramArguments
it has limits set
LimitLoadToSessionType
_RecoverOnCrash
XPC_USERSPACE_REBOOTED
vproc not allowed by caller %s
PID size for exit reason mismatch
com.apple.bonjour.registration
nano allocator
instances
JetsamProperties not loaded
ResetAtClose
Plist has the com.apple.quarantine xattr set: %s
Datastores
procinfo failed for PID %d: %s: %d
services[%zu] is missing or has invalid origin key
der_vm_execute_select_key
integer_allowed_iterate
SandboxContainer
MTESystemWidePreflight
PATH=/usr/bin:/bin:/usr/sbin:/sbin
CEValidateWithOptions
setting launch watchdog timeout to %u secs from overlay
group id = %u
-s
misfired notification: send-once
data element not allowed
Service: %s has leaked pended requests
.
vax (i know, right?)
instance-specific endpoints = {
dext checkin port = %#x [unable to get port information]
Could not bind to system logger socket: error = %d: %s
ReslideSharedCache
Lingering coalition: %llu (%s)
trial factors memory limit = %d MB
hardened ipc
softlimit
persistent services object is not an array
Attempting to select a string value from a non-string DER object
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
already shutting down or slain
PrivateFrameworks
BootShell
.plist
powerpc64
extension removal request finished, sending reply
urgent log submission completion initiated by: %s (pid = %d, version = %d)
-no-corpses
StartOnMount
JetsamPriority
TimeOut
NumberOfFiles
com.apple.xpc.launchd.system-override
info plist = 
No MRM cache found
launch_kern_credentials_resolve_by_uid(%d) failed
path
canceling throttled spawn
Unexpected type to match against during iteration
Invalid type for event (event/type): %s/%s
RootDirectory
unexpected subdio for an app extension bundle
Coalition Cache Hit: %s [%llu]
_instance
RemoveJob
Caller tried to check into a named job: %s
Feature flag string must have domain/feature format: %s
_Quarantined
 after %s
host not found
Ignoring a request to unset ondemand
%s/%lu
user cannot create its own domain
entitlements blob does not have CCDER_ENTITLEMENTS coding
DisallowAllLookups
Overriding specified stdin path for inetd-compatible service.
Could not find user/group associated with service: %d: %s %s/%s
speculatively converted service to spawned with PID %d, but the PID is %d
exponential throttling grace limit = %u
Attempting to select a boolean value from a non-boolean DER object
eacs
Invalid type for service dictionary (key/type): %s/%s
It never did anything anyway.
com.apple.private.xpc.persona-creator
filesystem mount
spawn scheduled
code
event channels = {
failed to reload active trial factors because it is currently locked
entering bootstrap mode
uncorking exec source after service init
sandbox-profile
Skipped persisting services in domain: %s
failed to create shmem
attempt to ignore unmanaged endpoint
encountered invalid tag
Retaining, but not starting, service %s
failed to find %s service
%f
getaddrinfo(3): %d: %s
handle
(n/a)
reload count = %zu
Replacing controller %s[%d] with %s[%d]
overflow of service activation count during deactivation. Managed:%d. Domain: %s. Service:%s
obliterating active service: %s
_ExperimentalNonLaunching
Invalid value for DeveloperTools: %s
DisableAllowed
\"%s\" => 
System shutdown
load jetsam properties path initiated by %s: %s
failed to fts_open(/private/var/db/launchd.db, 0x%x): %d: %s
ReleaseType
SockNodeName
pid %d not allowed to get properties for service
Unable to open %s [%d:%s]
No service cache
stdout path = %s
resolved groups = {
Service cannot reset: active instance endpoints
Feature flag string must not have multiple '/' separators: %s
Unknown ProcessType: %s
com.apple.private.xpc.smappservice.update
Unable to unpack stderr
v20@?0i8*12
one-shot
not running
Service did not exit %u seconds after SIGKILL.
Endpoint \"%s\" tried to steal host %s port (%d) from \"%s\"
Adaptive
v20@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch
Accumulated more than %d subscriptions for stream %s
spawning
deferral event on service in penalty box
always sigterm on shutdown
no EXC_RESOURCE during audio
boot task failure: %s
SoftKqWorkloopLimit
com.apple.private.xpc.launchd.load-jetsam-properties-path
persistent services header magic is invalid
_AbandonCoalition is only available to Application services.
SockPathGroup
%s,
service count = %u
Could not find domain from request: type=%s handle=%lu
Missing CPUType
%s => (timeout = %hus, consecutive crash count = %hu/%hu)
couldn't handoff domain IO, asynced away
configured
Ignored socket %s: %s
Expected string for a feature flag, got %s
OS_REASON_SANDBOX
string decode failure
CPUType
MallocLargeCache
run-at-load
spawned
requested SIGTERM
gathered %zu jetsam property overlays to persist into %s
XXXXXXXX%s=%llx
program
service spawn failed after attach: %d: %s
sudden shutdown
session uid = %d
hide = %s
ExceptionServer
unable to decode value tag for key-value pair
%hd
SIGKILLed
%-12s%-15s%-15s
uid
%04d-%02d-%02d %02d:%02d:%02d.%06d
JETSAM_REASON_MEMORY_HIGHWATER
HideUntilCheckIn
SIGTERMTimeout
SanitizerFlags
resolving its username/groupname failed
Attempting to commit shutdown unexpectedly: %s
DYLD_PRINT_OPTS
urgent log submission
could not get audit token for service (PID %d): %d: %s
cputypes
OS_REASON_HANGTRACER
_AllowedClients
network-outbound
handle = %llu, 
Preventing \"%s\" from registering for %s due to non-launching property mismatch
enable service
failed to serialize service plist: %s
Block
Abandoning send right to 0x%x (canceled notification)
/dev/console
PanicOnCrashDeadline
retry launch
persist-to-boot-mode
Service \"%s\" tried to register for aliased endpoint: %s
libdispatch bug: Unknown receive-right
string_prefix_allowed_iterate
setting persona requires an entitlement
IPv4v6
ChildDefaults
ess bootstrap_look_up: endpoint owner == NULL for service %s
der_vm_iterate_b
Got a socket event but accept() failed with errno %d - %s
service blame
Override
DYLD_PRINT_BINDINGS
Program specified by service is not a Mach-O executable file.
GetResourceLimits
spawn-constraint
PerformInRestore
it has a roleaccount set
Unable to setup identify
/System/AppleInternal/Library
```
