# `/usr/lib/libcryptex_interface.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 187,600 bytes.

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
MOUNT:VOLHASH_FD
com.apple.security.cryptex
info
UNINSTALL:CXVER
upgrade_lock
MOUNT:INFO_FD
MOUNT
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Binaries/libcryptex/install/Symbols/libcryptex_interface
target
com.apple.security.cryptex.xpc
mount_interface_create_unmount_request
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/util/rpc.c
underlying_cferr
com.apple.security.libcryptex.interface
upgrade_trampoline
nonce-domain-handle
CFMutableDictionary
UNINSTALL:FORCE_UNMOUNT
mount_interface_create_mount_request
MOUNT:LTRS_FD
@(#)VERSION:Cryptex IPC Interface Version 2.0.0: Sat Oct  3 17:50:13 PDT 2026; root:libcryptex-761.40.23~881/libcryptex_interface/RELEASE_ARM64E
ENDPOINT_INDEX
v8@?0
auth
remote-cryptex-identifier
com.apple.security.libcryptex.interface.daemon
MOUNT:DMG_ASSET_IDX_INT64
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/upgrade_abort_interface.m
rpc_call
[anonymous]
enable-install-events
im4m
Cryptex IPC Interface Version 2.0.0: Sat Oct  3 17:50:13 PDT 2026; root:libcryptex-761.40.23~881/libcryptex_interface/RELEASE_ARM64E
RELEASE
SUBSYSTEM
nonce-persistence
trustcache
install
com.apple.security.libcryptex.interface.upgrade_abort
target-type
cferr_domain
image-type-index
nonce-domain
upgrade_lock_error
UNMOUNT:INFO_FD
argv
persistence
FunctionName
v16@?0@\"NSObject<OS_xpc_object>\"8
MOUNT:IM4M_FD
MOUNT:CX1_PROPERTIES
REQ:UNMOUNT
UNMOUNT:FORCE
UPGRADE_ABORT
cryptex_name
v12@?0i8
image
remote-cryptex-version
CODEX_SUB_REQ
UNINSTALL
com.apple.security.libcryptex.interface.session
com.apple.security.libcryptex.interface.upgrade_lock
UPGRADE_WAIT
copy-installed
client-version
REQ:MOUNT
MOUNT_SUB_REQ
rpc_init_local
xpc
v16@?0^v8
com.apple.security.libcryptex.interface.upgrade_trampoline
uninstall
com.apple.security.cryptex.posix
UPGRADE_LOCK
-[UpgradeInterfaceLock _acquireLockOnQueue]
mount_interface
761.40.23
codex_interface_create_uninstall_request
cryptex_actor
MOUNT:DMG_FD
subsystem
cferr_userinfo
cferr_code
remote_service_create_install_request
cryptex1-properties
com.apple.security.libcryptex.interface.codex
cryptex_upgrade_interface_abort
routine
cferror
UNINSTALL:CXID
ENDPOINT_LOOKUP
com.apple.libcryptex
get-nonce
read-personalization-id
remote_service_interface
known-constant allocation
LineNumber
actor
roll-nonce
B16@?0^{__CFError=}8
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/codex_xpc_interface.m
COLLATION
user
endpoint
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/upgrade_lock_interface.m
unexpected failure: Messages should not be sent to this connection.
com.apple.security.cryptexd
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/remote_service_interface.m
volumehash
FileName
CODEX
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Sources/libcryptex/interface/mount_interface.m
%{public}s: ipc failure: %{darwin.errno}d
Failed to lock upgrade interface
%{public}s: looked up port: %#x
im4m transfer: %{darwin.errno}d
No reply to request to lock upgrade interface.
got reply: %s
%{public}s: ipc: %@
image transfer: %{darwin.errno}d
Invalid info plist.
routine succeeded
Invalid cryptex identifier.
%{public}s: pipe went dead: %{darwin.errno}d
failed to get argv: %{darwin.errno}d
Error unpacking upgrade lock response: %{darwin.errno}d
Error from daemon
Failed to create CFError.: %{darwin.errno}d
Error from cryptexd while waiting on upgrade: %{public}s: %{darwin.errno}d
c411 transfer: %{darwin.errno}d
Invalid input.: %{darwin.errno}d
Unexpected message: %{public}s: %{darwin.errno}d
Invalid trust cache.
%{public}s: setting name: %s
Invalid type for rpc subsystem %{darwin.errno}d
trustcache fd is invalid
allocation failed: obj = %s, size = %lu, error = %s
Invalid Cryptex1 properties.
CFError XPC dictionary is missing user info.: %{darwin.errno}d
Failed to unpack underlying error.: %{darwin.errno}d
Received error: %s
%{public}s: ipc [no error]
trustcache transfer: %{darwin.errno}d
XPC error while upgrade interface was locked: %{public}s
Invalid value for rpc target %{darwin.errno}d
image fd is invalid
Invalid image.
Error from cryptexd while aborting upgrade: %{public}s
Invalid type for rpc routine %{darwin.errno}d
sending request: %s
xpc_pipe_routine %{darwin.errno}d
Failed to convert CF to XPC.: %{darwin.errno}d
%{public}s: ipc routine succeeded
Invalid im4m.
im4m fd is invalid
trustcache transfer [no error]
Upgrade interface is already locked by the current process.
Failed to create XPC request.
XPC error while locking upgrade interface: %{public}s
No reply from cryptexd while aborting upgrade.
Invalid type for rpc target %{darwin.errno}d
Failed to create mutable dictionary.: %{darwin.errno}d
Failed to get XPC connection.
Failed to allocate dictionary.
Invalid type for rpc argv %{darwin.errno}d
key %s doesn't exist
Failed to create string.: %{darwin.errno}d
No reply from cryptexd while waiting on upgrade.: %{darwin.errno}d
c411 transfer [no error]
image transfer [no error]
cf create failed: obj = %s
%{public}s: changing name: %s -> %s
%{public}s: bootstrap_look_up: %{mach.errno}x
volume hash transfer [no error]
volume hash transfer: %{darwin.errno}d
im4m transfer [no error]
key %s isn't of type %s
OS_cryptex_actor
UpgradeInterfaceLock
init
T@\"NSMutableArray\",R,N,V_onNextLockReleaseCallbacks
log
_log
queue
releaseLock
dealloc
setLog:
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
T@\"NSObject<OS_xpc_object>\",&,N,V_lockConn
_createXPCRequest
addObject:
isLocked
onNextLockReleaseCallbacks
_acquireLockOnQueue
lockConn
T@\"NSObject<OS_os_log>\",&,N,V_log
_onNextLockRelease:
setQueue:
_isLockedOnQueue
_queue
countByEnumeratingWithState:objects:count:
removeAllObjects
setLockConn:
_handleXPCMessage:
acquireLock
getSharedInstance
.cxx_destruct
_lockConn
_onNextLockReleaseCallbacks
@16@0:8
v24@0:8@?16
@\"NSObject<OS_dispatch_queue>\"
@\"NSObject<OS_os_log>\"
B16@0:8
i16@0:8
v24@0:8@16
@\"NSObject<OS_xpc_object>\"
@\"NSMutableArray\"
v16@0:8
```
