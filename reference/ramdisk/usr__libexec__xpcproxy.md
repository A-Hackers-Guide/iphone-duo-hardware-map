# `/usr/libexec/xpcproxy`

From the upgrade restore ramdisk (141-29011-104.dmg). 133,600 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 2320)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (2)

- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.coreservices.canmanagebackgroundtasks</key>
	<true/>
	<key>com.apple.private.exclaves.conclave-spawn</key>
	<true/>
	<key>com.apple.private.security.storage.driverkitd</key>
	<true/>
	<key>com.apple.private.shared-region.config</key>
	<true/>
	<key>com.apple.private.spawn-driver</key>
	<true/>
	<key>com.apple.private.spawn-panic-crash-behavior</key>
	<true/>
	<key>com.apple.private.spawn-subsystem-root</key>
	<true/>
	<key>com.apple.private.xpc.is.xpcproxy</key>
	<true/>
</dict>
</plist>
```

## Strings (302)

```
assertion failure: \"posix_spawnattr_set_use_sanitizers_np(&ctx->psattr, attr->sanitizer_flags)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 0)\" -> %llu
assertion failure: \"launch_spawnctx_update_spawn_constraint(&ctx, attr, xtra, ((void*)0), 0)\" -> %llu
assertion failure: \"setiopolicy_np(0, 0, 3)\" -> %llu
assertion failure: \"posix_spawnattr_setcpumonitor(&ctx->psattr, attr->cpumon_percent, attr->cpumon_interval)\" -> %llu
assertion failure: \"posix_spawnattr_set_telemetry_np(&ctx->psattr, PSA_TELEMETRY_PAGEIN, 0)\" -> %llu
assertion failure: \"sandbox_spawnattrs_setcontainer(&ctx->sbattrs, container_id)\" -> %{errno}d
assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 2)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 1)\" -> %llu
assertion failure: \"posix_spawnattr_init(&ctx->psattr)\" -> %llu
assertion failure: \"posix_spawnattr_disable_ptr_auth_a_keys_np(&ctx->psattr, 0)\" -> %llu
assertion failure: \"posix_spawnattr_setcpumonitor_default(&ctx->psattr)\" -> %llu
assertion failure: \"posix_spawnattr_set_threadlimit_ext(&ctx->psattr, attr->ps_jetsam_threadlimit)\" -> %llu
assertion failure: \"posix_spawnattr_set_launch_type_np(&ctx->psattr, attr->ps_launch_type)\" -> %llu
assertion failure: \"posix_spawnattr_setarchpref_np(psattr, self->xb_count, self->xb_cpu_types, self->xb_cpu_subtypes, ((void*)0))\" -> %llu
assertion failure: \"posix_spawnattr_set_qos_class_np(&ctx->psattr, attr->ps_qos_class)\" -> %llu
assertion failure: \"posix_spawnattr_setflags(&ctx->psattr, psflags)\" -> %llu
assertion failure: \"setsid()\" -> %{errno}d
assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 0, \"/dev/null\", 0x0000|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu
assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 2, \"/dev/null\", 0x0002|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu
assertion failure: \"(*__error())\" -> %llu
assertion failure: \"posix_spawnattr_getflags(&ctx->psattr, &psflags)\" -> %llu
assertion failure: \"posix_spawnattr_set_filedesclimit_ext(&ctx->psattr, attr->ps_jetsam_softfiledescriptorlimit, attr->ps_jetsam_hardfiledescriptorlimit)\" -> %llu
assertion failure: \"posix_spawnattr_set_use_sec_transition_shims_np(&ctx->psattr, attr->checked_allocations_posix_spawn_flags)\" -> %llu
assertion failure: \"posix_spawnattr_set_crash_behavior_deadline_np(&ctx->psattr, attr->ps_crash_behavior_deadline, 0)\" -> %llu
assertion failure: \"posix_spawnattr_setjetsam_ext(&ctx->psattr, (short)attr->ps_jetsam_flags, attr->ps_jetsam_priority, attr->ps_jetsam_memlimit_active, attr->ps_jetsam_memlimit_inactive)\" -> %llu
assertion failure: \"posix_spawnattr_set_max_addr_np(&ctx->psattr, attr->ps_jetsam_addresslimit)\" -> %llu
assertion failure: \"posix_spawnattr_set_crash_count_np(&ctx->psattr, attr->ps_crash_count, attr->ps_throttling_timeout)\" -> %llu
assertion failure: \"posix_spawnattr_setdataless_iopolicy_np(&ctx->psattr, 2)\" -> %llu
assertion failure: \"amfi_launch_constraint_set_spawnattr(&ctx->psattr, ctx->spawn_constraint, ctx->spawn_constraint_sz)\" -> %llu
assertion failure: \"posix_spawnattr_init(&psattr)\" -> %llu
assertion failure: \"posix_spawnattr_setprocesstype_np(&ctx.psattr, 0x00000700)\" -> %llu
assertion failure: \"posix_spawn_file_actions_add_fileportdup2_np( &ctx->filact, _xpc_fd_get_port(xfd), dest)\" -> %llu
assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 0)\" -> %llu
assertion failure: \"setiopolicy_np(0, 2, 3)\" -> %llu
assertion failure: \"posix_spawn_file_actions_init(&ctx->filact)\" -> %llu
assertion failure: \"posix_spawn_file_actions_init(&filact)\" -> %llu
assertion failure: \"posix_spawnattr_setspecialport_np(&psattr, globals->bootstrap_port, 4)\" -> %llu
assertion failure: \"posix_spawnattr_set_conclavememlimit_ext(&ctx->psattr, attr->ps_jetsam_conclave_memlimit)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 1, \"/dev/null\", 0x0002|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu
assertion failure: \"nbytes\" -> %{errno}d
assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 2)\" -> %llu
assertion failure: \"posix_spawnattr_set_kqworklooplimit_ext(&ctx->psattr, attr->ps_jetsam_softkqworklooplimit, attr->ps_jetsam_hardkqworklooplimit)\" -> %llu
assertion failure: \"posix_spawnattr_set_crash_behavior_np(&ctx->psattr, attr->ps_crash_behavior)\" -> %llu
assertion failure: \"posix_spawnattr_set_darwin_role_np(&ctx->psattr, attr->ps_role)\" -> %llu
assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 1)\" -> %llu
assertion failure: \"posix_spawnattr_set_portlimits_ext(&ctx->psattr, attr->ps_jetsam_softportlimit, attr->ps_jetsam_hardportlimit)\" -> %llu
assertion failure: \"posix_spawnattr_setdataless_iopolicy_np(&ctx->psattr, 1)\" -> %llu
assertion failure: \"posix_spawnattr_set_registered_ports_np(&ctx->psattr, stash, 1)\" -> %llu
assertion failure: \"sandbox_spawnattrs_setprofilename(&ctx->sbattrs, profile)\" -> %{errno}d
assertion failure: \"posix_spawnattr_setmacpolicyinfo_np(&ctx->psattr, \"Sandbox\", &ctx->sbattrs, sizeof(ctx->sbattrs))\" -> %llu
assertion failure: \"error\" -> %llu
assertion failure: \"setenv(\"PATH\", \"/usr/bin:/bin:/usr/sbin:/sbin\", 1)\" -> %{errno}d
assertion failure: \"revoke(\"/dev/console\")\" -> %{errno}d
assertion failure: \"posix_spawnattr_set_shared_region_config_np(&ctx->psattr, attr->ps_shared_region_config_flags)\" -> %llu
assertion failure: \"posix_spawnattr_setspecialport_np(&ctx->psattr, port2use, dst)\" -> %llu
assertion failure: \"posix_spawnattr_setflags(&psattr, psflags)\" -> %llu
unsupported type: %s
Configuration error: unreasonably large PID or execcnt
@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Thu Oct  8 00:45:07 PDT 2026; root:libxpc_executables-3298.52.1~4/xpcproxy/RELEASE_ARM64E
xml-looking blob was passed in
key length is invalid
der_vm_execute_match_string
%s
numeric string element not allowed
Unknown UTC Time encoding
$or
Unable to unpack argv
Path
Attempting to select a string value from a non-string DER object
HOME
setup_fds bad fd type
SkipImmediatePoll
der_vm_execute_match_integer
Entitlements element not allowed
v16@?0^v8
encountered invalid tag
string_prefix_allowed_iterate
Not eligible for acceleration
dictionary key / value decoding failure
B24@?0r*8^v16
USER
Invalid environment[%zd]: %s
Unable to unpack stdout
Retval
Attempting to select an integer value from a non-integer DER object
der_vm_execute_string_prefix_value_allowed
der_decode_data
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
request originated from a different PID
Missing program
Unable to unpack cwd
GroupName
Unable to unpack bundle path
Unable to merge spawn constraints
Unable to unpack container_id
setup_fds bad int type
fds
Unable to set current working directory. path = %s
der_validate_array
entitlements blob does not have CCDER_ENTITLEMENTS coding
setgid(%d)
com.apple.xpc.roleaccountd
cryptex_trampoline_upgrade_wait() failed with error %d - %s
boolean should be exactly 1 byte
der_vm_execute_select_key
array decoding failure
ds
encountered invalid element in an iterable
key contains an embedded NUL
unknown number encoding
der_vm_data_from_context
CoreEntitlements: unknown DER type
Data corruption: CoreEntitlements has aborted due to an unrecoverable error
posix_spawn(%s)
der_validate_dictionary
fds invalid
-sh
Unable to setup_role_account
Insufficient rlimit: %u > %zd
Unable to unpack group
der_vm_iterate_b
[%s]: entitlements blob has unexpected version %lld\n
dictionary value verification failure
vers
comp
der_decode_numeric_string
calling cryptex_trampoline_upgrade_wait() for %s
mdns
/usr/lib/system/libsystem_trace.dylib
RELEASE
der_vm_integer_from_context
Unexpected type to match against
XPC_SERVICES_UNAVAILABLE=1
Attempting to select a data value from a non-data DER object
API Misuse
der_vm_execute_match_string_prefix
string_value_allowed_iterate
Unexpected type to match against during iteration
XXXXXXXX%s=%llx
setup_role_account missing RETVAL_KEY
getrlimit(%d)
der_vm_execute_integer_value_allowed
Invalid Arguments
could not decode size for next DER sub-sequence
error
SHELL
/dev/null
der_vm_execute_nocopy
rec_execcnt
Unable to open stderr path (%s)
der_vm_bool_from_context
der_vm_execute_match_bool
recursivelyValidateEntitlements
dictionary keys are not sorted or not unique
bootstrap port must lead to PID 1 [actual pid = %d]
initgroups(%s, %d)
com.apple.app-sandbox.read
setup_role_account no reply
getpwuid(%d)
noop
Unknown string encoding
xpc-fault
Unable to create stdout directory (%s)
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
/usr/lib/system/libsystem_info.dylib
string decode failure
Unable to open stdout path (%s)
der_vm_string_from_context
der_decode_string
/usr/bin:/bin:/usr/sbin:/sbin
bool decode failure
UTC Time element not allowed
sub-sequence size is larger than sequence size
key / value decoding failure
/
No spawn attr blob
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Binaries/libxpc_executables/install/Symbols/xpcproxy
XPC_FLAGS
PATH
PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/Developer/usr/bin
no value for key: %s
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
euid of PID 1 must be 0
request originated from a different execcnt
XPC_NULL_BOOTSTRAP=1
Verification failed
could not decode tag for next DER sub-sequence
key-value pair contains extra elements
/usr/lib/system/libsystem_notify.dylib
recursion limit reached
controller died
unable to decode value size for key-value pair
[%s]: %s\n
setup_role_account missing PATH_KEY
posix_spawn(%s) EBADARCH
failed to serialized value for key: %s
CoreEntitlements: not a sequence
Unable to copy merged spawn constraints
Already registered ports
Darwin Bootstrapper Trampoline Version 7.0.0: Thu Oct  8 00:45:07 PDT 2026; root:libxpc_executables-3298.52.1~4/xpcproxy/RELEASE_ARM64E
Unable to unpack stderr
string
getgrnam(%s)
Configuration error: failed to fetch our own audit token
invalid arguments passed in
validate_VNext
der_decode_key_value
req_pid
Unable to generate a fault: %d - %s
setup-event
Special ports invalid
/bin/sh
setup_role_account failed
UserName
invalid dictionary element
setup_fds bad dest: %d table: %d
Unable to setup identify
Insufficient spawnattr length: %zu < %lu
root
der_vm_execute_select_longest_matching_key
Query cannot be satisfied
invalid tag or length
unable to decode value tag for key-value pair
code
dictionary decoding failure
Unable to unpack sandbox profile
Unable to create stderr directory (%s)
%s (backtrace follows)
TMPDIR
%s/%s
self
unhandled opcode
der_vm_execute_string_value_allowed
OK
%s cannot be run directly.\n
CoreEntitlements: Couldn't iterate over DER entitlements\n
com.apple.launchd.helper
Unknown numeric string encoding
der_decode_next
$and
pre-exec
Unable to create stdin directory (%s)
line
uuid
Could not create shell: code %d
setup_role_account reply is error
Sandbox
Unable to unpack environment
TERM=vt100
Unable to unpack username
String contains an embedded NUL
number too large
Executable
der_decode_number
_manufacturingCallback
extra data at the end of element
Invalid special port[%zd]: %d
Unknown boolean encoding
der_decode_utc_time
reqs
_objectForActiveContext
subcode
pc
der_vm_execute_select_index
XXXXXXXX%s=%s
configurable
blob
ports
Unable to open stdin path (%s)
hostpid
Token
CEValidateWithOptions
der_decode_boolean
B24@?0Q8^v16
LOGNAME
No space for special ports: %zu > (%zu - %d)
setuid(%d)
Unable to unpack stdin
/dev/console
data element not allowed
ccat
pid
Unable to unpack program
validate_V0
dictionary key is not a valid string
extensions cannot run as root
der_decode_entitlements
XXXXXXXX%s=%s/tmp
access(%s, X_OK) failed with errno %d - %s
A memory allocation has failed
encountered invalid element in an array
setlogin(%s)
%s: could not exec: %s\n
getpwnam(%s)
iterable decoding failure
integer_allowed_iterate
Unknown data encoding
Too many rlimits: %d
iteration over a non-iterable type
Attempting to select a boolean value from a non-boolean DER object
Unknown DER entitlements encoding
```
