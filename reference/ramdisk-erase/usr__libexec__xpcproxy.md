# `/usr/libexec/xpcproxy`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 133,600 bytes.

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
assertion failure: \"posix_spawnattr_set_telemetry_np(&ctx->psattr, PSA_TELEMETRY_PAGEIN, 0)\" -> %llu
assertion failure: \"posix_spawnattr_disable_ptr_auth_a_keys_np(&ctx->psattr, 0)\" -> %llu
assertion failure: \"posix_spawnattr_set_crash_behavior_deadline_np(&ctx->psattr, attr->ps_crash_behavior_deadline, 0)\" -> %llu
assertion failure: \"posix_spawnattr_setflags(&psattr, psflags)\" -> %llu
assertion failure: \"launch_spawnctx_update_spawn_constraint(&ctx, attr, xtra, ((void*)0), 0)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 1)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 2)\" -> %llu
assertion failure: \"posix_spawn_file_actions_init(&ctx->filact)\" -> %llu
assertion failure: \"posix_spawnattr_set_kqworklooplimit_ext(&ctx->psattr, attr->ps_jetsam_softkqworklooplimit, attr->ps_jetsam_hardkqworklooplimit)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 1, \"/dev/null\", 0x0002|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu
assertion failure: \"setenv(\"PATH\", \"/usr/bin:/bin:/usr/sbin:/sbin\", 1)\" -> %{errno}d
assertion failure: \"posix_spawnattr_set_threadlimit_ext(&ctx->psattr, attr->ps_jetsam_threadlimit)\" -> %llu
assertion failure: \"posix_spawnattr_set_max_addr_np(&ctx->psattr, attr->ps_jetsam_addresslimit)\" -> %llu
assertion failure: \"posix_spawn_file_actions_init(&filact)\" -> %llu
assertion failure: \"posix_spawnattr_set_use_sec_transition_shims_np(&ctx->psattr, attr->checked_allocations_posix_spawn_flags)\" -> %llu
assertion failure: \"posix_spawnattr_set_conclavememlimit_ext(&ctx->psattr, attr->ps_jetsam_conclave_memlimit)\" -> %llu
assertion failure: \"sandbox_spawnattrs_setcontainer(&ctx->sbattrs, container_id)\" -> %{errno}d
assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 0, \"/dev/null\", 0x0000|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu
assertion failure: \"setiopolicy_np(0, 2, 3)\" -> %llu
assertion failure: \"posix_spawnattr_setflags(&ctx->psattr, psflags)\" -> %llu
assertion failure: \"posix_spawnattr_set_darwin_role_np(&ctx->psattr, attr->ps_role)\" -> %llu
assertion failure: \"amfi_launch_constraint_set_spawnattr(&ctx->psattr, ctx->spawn_constraint, ctx->spawn_constraint_sz)\" -> %llu
assertion failure: \"posix_spawnattr_init(&psattr)\" -> %llu
assertion failure: \"posix_spawnattr_setprocesstype_np(&ctx.psattr, 0x00000700)\" -> %llu
assertion failure: \"posix_spawnattr_setcpumonitor(&ctx->psattr, attr->cpumon_percent, attr->cpumon_interval)\" -> %llu
assertion failure: \"posix_spawnattr_setdataless_iopolicy_np(&ctx->psattr, 1)\" -> %llu
assertion failure: \"posix_spawn_file_actions_add_fileportdup2_np( &ctx->filact, _xpc_fd_get_port(xfd), dest)\" -> %llu
assertion failure: \"posix_spawnattr_set_use_sanitizers_np(&ctx->psattr, attr->sanitizer_flags)\" -> %llu
assertion failure: \"posix_spawnattr_set_filedesclimit_ext(&ctx->psattr, attr->ps_jetsam_softfiledescriptorlimit, attr->ps_jetsam_hardfiledescriptorlimit)\" -> %llu
assertion failure: \"posix_spawnattr_setspecialport_np(&ctx->psattr, port2use, dst)\" -> %llu
assertion failure: \"nbytes\" -> %{errno}d
assertion failure: \"posix_spawnattr_init(&ctx->psattr)\" -> %llu
assertion failure: \"posix_spawnattr_set_shared_region_config_np(&ctx->psattr, attr->ps_shared_region_config_flags)\" -> %llu
assertion failure: \"error\" -> %llu
assertion failure: \"posix_spawnattr_setarchpref_np(psattr, self->xb_count, self->xb_cpu_types, self->xb_cpu_subtypes, ((void*)0))\" -> %llu
assertion failure: \"posix_spawnattr_setjetsam_ext(&ctx->psattr, (short)attr->ps_jetsam_flags, attr->ps_jetsam_priority, attr->ps_jetsam_memlimit_active, attr->ps_jetsam_memlimit_inactive)\" -> %llu
assertion failure: \"setiopolicy_np(0, 0, 3)\" -> %llu
assertion failure: \"posix_spawnattr_set_qos_class_np(&ctx->psattr, attr->ps_qos_class)\" -> %llu
assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 2)\" -> %llu
assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 2, \"/dev/null\", 0x0002|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu
assertion failure: \"revoke(\"/dev/console\")\" -> %{errno}d
assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, 0)\" -> %llu
assertion failure: \"posix_spawnattr_setcpumonitor_default(&ctx->psattr)\" -> %llu
assertion failure: \"posix_spawnattr_set_crash_behavior_np(&ctx->psattr, attr->ps_crash_behavior)\" -> %llu
assertion failure: \"sandbox_spawnattrs_setprofilename(&ctx->sbattrs, profile)\" -> %{errno}d
assertion failure: \"posix_spawnattr_setmacpolicyinfo_np(&ctx->psattr, \"Sandbox\", &ctx->sbattrs, sizeof(ctx->sbattrs))\" -> %llu
assertion failure: \"posix_spawnattr_setspecialport_np(&psattr, globals->bootstrap_port, 4)\" -> %llu
assertion failure: \"(*__error())\" -> %llu
assertion failure: \"posix_spawnattr_getflags(&ctx->psattr, &psflags)\" -> %llu
assertion failure: \"posix_spawnattr_set_crash_count_np(&ctx->psattr, attr->ps_crash_count, attr->ps_throttling_timeout)\" -> %llu
assertion failure: \"setsid()\" -> %{errno}d
assertion failure: \"posix_spawnattr_set_portlimits_ext(&ctx->psattr, attr->ps_jetsam_softportlimit, attr->ps_jetsam_hardportlimit)\" -> %llu
assertion failure: \"posix_spawnattr_setdataless_iopolicy_np(&ctx->psattr, 2)\" -> %llu
assertion failure: \"posix_spawnattr_set_launch_type_np(&ctx->psattr, attr->ps_launch_type)\" -> %llu
assertion failure: \"posix_spawnattr_set_registered_ports_np(&ctx->psattr, stash, 1)\" -> %llu
assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 0)\" -> %llu
assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 1)\" -> %llu
Entitlements element not allowed
sub-sequence size is larger than sequence size
fds
Insufficient rlimit: %u > %zd
Darwin Bootstrapper Trampoline Version 7.0.0: Thu Oct  8 00:45:07 PDT 2026; root:libxpc_executables-3298.52.1~4/xpcproxy/RELEASE_ARM64E
dictionary value verification failure
Sandbox
code
ports
XPC_SERVICES_UNAVAILABLE=1
UserName
calling cryptex_trampoline_upgrade_wait() for %s
dictionary key / value decoding failure
unknown number encoding
com.apple.app-sandbox.read
Attempting to select a boolean value from a non-boolean DER object
key contains an embedded NUL
LOGNAME
Unable to unpack sandbox profile
pc
Unable to unpack group
/Library/Caches/com.apple.xbs/93B26037-3CA0-450D-A480-C6C95BDEE88C/TemporaryDirectory.0yOfDg/Binaries/libxpc_executables/install/Symbols/xpcproxy
string decode failure
Unknown numeric string encoding
CoreEntitlements: unknown DER type
Unable to unpack environment
uuid
could not decode tag for next DER sub-sequence
setuid(%d)
Insufficient spawnattr length: %zu < %lu
validate_VNext
der_vm_execute_integer_value_allowed
could not decode size for next DER sub-sequence
Unable to copy merged spawn constraints
SkipImmediatePoll
RELEASE
der_decode_boolean
der_decode_entitlements
request originated from a different PID
Unable to merge spawn constraints
Unable to create stdin directory (%s)
hostpid
posix_spawn(%s)
recursivelyValidateEntitlements
[%s]: %s\n
Invalid special port[%zd]: %d
Unable to create stdout directory (%s)
setup_role_account no reply
Too many rlimits: %d
USER
Unable to unpack bundle path
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
bool decode failure
Unknown data encoding
Unable to open stdout path (%s)
setup_fds bad dest: %d table: %d
Unable to unpack container_id
string_prefix_allowed_iterate
validate_V0
key length is invalid
recursion limit reached
ds
der_vm_execute_select_key
ccat
Configuration error: unreasonably large PID or execcnt
PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/Developer/usr/bin
TERM=vt100
access(%s, X_OK) failed with errno %d - %s
der_vm_execute_match_string
fds invalid
Unable to unpack program
iterable decoding failure
dictionary decoding failure
_manufacturingCallback
Unable to setup identify
getrlimit(%d)
root
getgrnam(%s)
der_vm_execute_match_bool
pid
controller died
iteration over a non-iterable type
Verification failed
der_decode_number
key-value pair contains extra elements
Unknown boolean encoding
no value for key: %s
xpc-fault
No space for special ports: %zu > (%zu - %d)
setgid(%d)
Could not create shell: code %d
getpwnam(%s)
der_vm_execute_nocopy
der_vm_bool_from_context
der_decode_numeric_string
comp
subcode
noop
Unknown DER entitlements encoding
Unable to setup_role_account
Unable to unpack cwd
/dev/null
Unable to unpack stderr
Special ports invalid
/dev/console
getpwuid(%d)
encountered invalid element in an iterable
Unable to set current working directory. path = %s
initgroups(%s, %d)
blob
/usr/lib/system/libsystem_notify.dylib
@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Thu Oct  8 00:45:07 PDT 2026; root:libxpc_executables-3298.52.1~4/xpcproxy/RELEASE_ARM64E
Unknown UTC Time encoding
pre-exec
vers
CoreEntitlements: Couldn't iterate over DER entitlements\n
rec_execcnt
XPC_FLAGS
CEValidateWithOptions
Missing program
%s: could not exec: %s\n
setup_role_account failed
entitlements blob does not have CCDER_ENTITLEMENTS coding
API Misuse
der_decode_data
failed to serialized value for key: %s
der_validate_dictionary
error
Unknown string encoding
string_value_allowed_iterate
%s/%s
setup_role_account reply is error
OK
No spawn attr blob
der_decode_utc_time
bootstrap port must lead to PID 1 [actual pid = %d]
TMPDIR
XXXXXXXX%s=%s
Unable to unpack stdout
reqs
_objectForActiveContext
euid of PID 1 must be 0
PATH
invalid dictionary element
dictionary keys are not sorted or not unique
setup_fds bad fd type
unhandled opcode
[%s]: entitlements blob has unexpected version %lld\n
der_vm_execute_match_integer
String contains an embedded NUL
UTC Time element not allowed
unable to decode value tag for key-value pair
der_validate_array
req_pid
cryptex_trampoline_upgrade_wait() failed with error %d - %s
der_vm_integer_from_context
der_vm_execute_select_index
Unexpected type to match against
Query cannot be satisfied
HOME
XXXXXXXX%s=%llx
setup_role_account missing RETVAL_KEY
invalid arguments passed in
der_decode_string
setup_fds bad int type
xml-looking blob was passed in
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
invalid tag or length
key / value decoding failure
Unable to unpack stdin
%s
request originated from a different execcnt
Unable to create stderr directory (%s)
der_decode_next
B24@?0Q8^v16
/bin/sh
Token
Retval
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
/
configurable
com.apple.xpc.roleaccountd
GroupName
/usr/lib/system/libsystem_trace.dylib
dictionary key is not a valid string
Configuration error: failed to fetch our own audit token
CoreEntitlements: not a sequence
extensions cannot run as root
setlogin(%s)
self
der_vm_string_from_context
array decoding failure
Unable to generate a fault: %d - %s
der_vm_iterate_b
encountered invalid tag
Already registered ports
setup_role_account missing PATH_KEY
SHELL
Path
Attempting to select an integer value from a non-integer DER object
data element not allowed
extra data at the end of element
boolean should be exactly 1 byte
$or
%s cannot be run directly.\n
/usr/lib/system/libsystem_info.dylib
A memory allocation has failed
$and
Unable to unpack username
mdns
Invalid Arguments
Not eligible for acceleration
unable to decode value size for key-value pair
Attempting to select a string value from a non-string DER object
der_vm_execute_string_value_allowed
der_decode_key_value
unsupported type: %s
XPC_NULL_BOOTSTRAP=1
der_vm_execute_string_prefix_value_allowed
der_vm_execute_select_longest_matching_key
encountered invalid element in an array
posix_spawn(%s) EBADARCH
string
com.apple.launchd.helper
-sh
Executable
Unable to unpack argv
v16@?0^v8
/usr/bin:/bin:/usr/sbin:/sbin
der_vm_data_from_context
numeric string element not allowed
Data corruption: CoreEntitlements has aborted due to an unrecoverable error
XXXXXXXX%s=%s/tmp
Unable to open stderr path (%s)
Attempting to select a data value from a non-data DER object
der_vm_execute_match_string_prefix
Unexpected type to match against during iteration
integer_allowed_iterate
%s (backtrace follows)
line
number too large
setup-event
B24@?0r*8^v16
Invalid environment[%zd]: %s
Unable to open stdin path (%s)
```
