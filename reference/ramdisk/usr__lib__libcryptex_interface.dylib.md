# `/usr/lib/libcryptex_interface.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 187,600 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 3624)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libcryptex_interface.dylib (compatibility version 1.0.0, current version 761.40.23)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (2 classes, 0 protocols)

Classes: `OS_cryptex_actor`, `UpgradeInterfaceLock`

## Strings (219)

```
setQueue:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
_onNextLockRelease:
countByEnumeratingWithState:objects:count:
isLocked
queue
setLockConn:
setLog:
_acquireLockOnQueue
onNextLockReleaseCallbacks
T@\"NSMutableArray\",R,N,V_onNextLockReleaseCallbacks
.cxx_destruct
removeAllObjects
_lockConn
_log
T@\"NSObject<OS_xpc_object>\",&,N,V_lockConn
_isLockedOnQueue
_onNextLockReleaseCallbacks
acquireLock
_queue
addObject:
T@\"NSObject<OS_os_log>\",&,N,V_log
getSharedInstance
lockConn
releaseLock
dealloc
log
_createXPCRequest
_handleXPCMessage:
init
@16@0:8
B16@0:8
i16@0:8
v24@0:8@?16
@\"NSObject<OS_xpc_object>\"
@\"NSObject<OS_dispatch_queue>\"
@\"NSMutableArray\"
v16@0:8
v24@0:8@16
@\"NSObject<OS_os_log>\"
uninstall
LineNumber
COLLATION
endpoint
com.apple.security.cryptex.xpc
com.apple.security.cryptexd
roll-nonce
info
REQ:UNMOUNT
RELEASE
get-nonce
install
com.apple.security.cryptex.posix
FunctionName
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/codex_xpc_interface.m
-[UpgradeInterfaceLock _acquireLockOnQueue]
MOUNT:LTRS_FD
mount_interface_create_unmount_request
MOUNT:INFO_FD
mount_interface
MOUNT_SUB_REQ
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Binaries/libcryptex/install/Symbols/libcryptex_interface
ENDPOINT_LOOKUP
com.apple.libcryptex
im4m
remote-cryptex-identifier
FileName
B16@?0^{__CFError=}8
cryptex_actor
com.apple.security.libcryptex.interface.upgrade_lock
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/remote_service_interface.m
persistence
volumehash
remote-cryptex-version
com.apple.security.libcryptex.interface.daemon
UPGRADE_LOCK
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/upgrade_lock_interface.m
MOUNT:VOLHASH_FD
ENDPOINT_INDEX
upgrade_trampoline
known-constant allocation
UNINSTALL:CXVER
MOUNT:DMG_FD
cryptex_upgrade_interface_abort
com.apple.security.libcryptex.interface.upgrade_abort
routine
com.apple.security.cryptex
MOUNT:DMG_ASSET_IDX_INT64
MOUNT
761.40.23
Cryptex IPC Interface Version 2.0.0: Sat Oct  3 17:50:13 PDT 2026; root:libcryptex-761.40.23~881/libcryptex_interface/RELEASE_ARM64E
target
underlying_cferr
com.apple.security.libcryptex.interface
cryptex1-properties
remote_service_interface
CODEX
upgrade_lock
MOUNT:CX1_PROPERTIES
@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Sat Oct  3 17:50:13 PDT 2026; root:libcryptex-761.40.23~881/libcryptex_interface/RELEASE_ARM64E
subsystem
UPGRADE_WAIT
nonce-domain-handle
UNINSTALL:FORCE_UNMOUNT
com.apple.security.libcryptex.interface.codex
v16@?0@\"NSObject<OS_xpc_object>\"8
REQ:MOUNT
target-type
cferr_code
SUBSYSTEM
CFMutableDictionary
rpc_call
cferr_userinfo
cferr_domain
nonce-persistence
trustcache
CODEX_SUB_REQ
codex_interface_create_uninstall_request
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/mount_interface.m
v16@?0^v8
image
copy-installed
UNINSTALL
UNINSTALL:CXID
com.apple.security.libcryptex.interface.session
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/upgrade_abort_interface.m
UPGRADE_ABORT
[anonymous]
com.apple.security.libcryptex.interface.upgrade_trampoline
auth
enable-install-events
user
mount_interface_create_mount_request
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/util/rpc.c
unexpected failure: Messages should not be sent to this connection.
image-type-index
v12@?0i8
read-personalization-id
upgrade_lock_error
MOUNT:IM4M_FD
UNMOUNT:FORCE
rpc_init_local
actor
v8@?0
client-version
UNMOUNT:INFO_FD
argv
cferror
xpc
cryptex_name
nonce-domain
remote_service_create_install_request
im4m fd is invalid
c411 transfer [no error]
Failed to get XPC connection.
XPC error while locking upgrade interface: %{public}s
%{public}s: bootstrap_look_up: %{mach.errno}x
No reply to request to lock upgrade interface.
Invalid type for rpc routine %{darwin.errno}d
Failed to create mutable dictionary.: %{darwin.errno}d
volume hash transfer: %{darwin.errno}d
volume hash transfer [no error]
Invalid type for rpc argv %{darwin.errno}d
image transfer [no error]
Failed to lock upgrade interface
Invalid image.
Received error: %s
%{public}s: pipe went dead: %{darwin.errno}d
trustcache fd is invalid
im4m transfer: %{darwin.errno}d
failed to get argv: %{darwin.errno}d
CFError XPC dictionary is missing user info.: %{darwin.errno}d
Failed to create CFError.: %{darwin.errno}d
Error unpacking upgrade lock response: %{darwin.errno}d
key %s doesn't exist
Failed to create string.: %{darwin.errno}d
Failed to convert CF to XPC.: %{darwin.errno}d
Error from cryptexd while waiting on upgrade: %{public}s: %{darwin.errno}d
image transfer: %{darwin.errno}d
Invalid im4m.
Error from cryptexd while aborting upgrade: %{public}s
%{public}s: setting name: %s
%{public}s: ipc failure: %{darwin.errno}d
Invalid cryptex identifier.
Invalid Cryptex1 properties.
Error from daemon
%{public}s: ipc routine succeeded
%{public}s: looked up port: %#x
Failed to create XPC request.
Invalid info plist.
xpc_pipe_routine %{darwin.errno}d
%{public}s: ipc: %@
c411 transfer: %{darwin.errno}d
cf create failed: obj = %s
trustcache transfer [no error]
Failed to allocate dictionary.
No reply from cryptexd while aborting upgrade.
Invalid type for rpc target %{darwin.errno}d
image fd is invalid
Invalid value for rpc target %{darwin.errno}d
Failed to unpack underlying error.: %{darwin.errno}d
Upgrade interface is already locked by the current process.
No reply from cryptexd while waiting on upgrade.: %{darwin.errno}d
trustcache transfer: %{darwin.errno}d
XPC error while upgrade interface was locked: %{public}s
Invalid trust cache.
got reply: %s
%{public}s: changing name: %s -> %s
%{public}s: ipc [no error]
allocation failed: obj = %s, size = %lu, error = %s
sending request: %s
routine succeeded
key %s isn't of type %s
im4m transfer [no error]
Invalid input.: %{darwin.errno}d
Unexpected message: %{public}s: %{darwin.errno}d
Invalid type for rpc subsystem %{darwin.errno}d
OS_cryptex_actor
UpgradeInterfaceLock
```
