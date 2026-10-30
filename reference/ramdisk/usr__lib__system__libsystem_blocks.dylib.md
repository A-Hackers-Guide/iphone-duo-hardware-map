# `/usr/lib/system/libsystem_blocks.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 116,768 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2904)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, upward)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6, upward)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libunwind.dylib (compatibility version 1.0.0, current version 2200.5.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (6 classes, 0 protocols)

Classes: `__NSAutoBlock__`, `__NSBlockVariable__`, `__NSFinalizingBlock__`, `__NSGlobalBlock__`, `__NSMallocBlock__`, `__NSStackBlock__`

## Strings (48)

```
v16@0:8
^{Block_byref=^v^{Block_byref}iI}
i
@
Q16@0:8
B16@0:8
@24@0:8@16
^?
@16@0:8
Vv16@0:8
false
_call_generic_copy_helper
getNextOpcodeAndCount
destroyBlock
endptr && \"endptr isn't expected to be null\"
info->state == EXCP_DESTROY_GENERIC
helper && \"helper is expected to be non-null\"
_cleanup_generic_captures
false && \"unexpected opcode\"
copyCapture
cleanup_captures
runtime.cpp
false && \"unexpected helper kind\"
_call_generic_destroy_helper
copyBlock
false && \"helper should be null in this case\"
capcounter == 0 && \"capcounter expected to be zero\"
__NSAutoBlock__
__NSFinalizingBlock__
__NSGlobalBlock__
__NSBlockVariable__
__NSStackBlock__
__NSMallocBlock__
copy
size
forwarding
retainCount
_isDeallocating
copyWithZone:
finalize
flags
autorelease
byref_keep
retain
release
_tryRetain
containedObject
byref_destroy
```
