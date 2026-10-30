# `/usr/lib/swift/libswiftDistributed.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 271,152 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 4024)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/swift/libswiftDistributed.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (4 classes, 0 protocols)

Classes: `_TtC11Distributed29LocalTestingInvocationDecoder`, `_TtC11Distributed34LocalTestingDistributedActorSystem`, `_TtC11Distributed39DistributedRemoteActorReferenceExecutor`, `_TtC11DistributedP33_670906D6F767C8D8F71D2E8FF1D478F75_Lock`

## Strings (66)

```
assignedIDsLock
assignedIDs
idProvider
underlying
activeActorsLock
activeActors
Unexpectedly found nil while unwrapping an Optional value
\nmangled name: 
Swift/Integers.swift
 (
invoked distributed stub '
Precondition failed
Cannot assume to be 'isolated 
' since distributed actor '
Distributed/DistributedActor.swift
Failed to decode distributed target return type
Swift/UnsafeBufferPointer.swift
Cannot call generic method without generic argument substitutions
Failed to locate distributed function accessor
Failed to resolve id '
Attempted to mark an unknown actor '
Attempted to make remote call to 
Failed to allocate buffer for distributed target return type
UnsafeMutableBufferPointer with negative count
Missing DistributedActorSystem userInfo while decoding
Insufficient space allocated to copy string contents
Swift/StringUTF8View.swift
Swift/ContiguousArrayBuffer.swift
Incorrect actor executor assumption; Expected '
Incorrect actor executor assumption; Expected same executor as 
\ndecoded: 
 do not satisfy generic requirements of 
Swift/UnsafePointer.swift
UnsafeMutablePointer.initialize with negative count
) on executor of remote distributed actor reference!
 using a local-only actor system
Attempted to call decoder method in a local-only actor system
Swift/Dictionary.swift
in Decoder.userInfo, while decoding 
Unexpected invocation of distributed method '
$distributed_actor_system
, expected params: 
Negative value is not representable
Distributed/DistributedAssertions.swift
Attempted to call encoder method in a local-only actor system
Missing system (for key .actorSystemKey) 
)
Distributed/DistributedDefaultExecutor.swift
Attempted to enqueue ExecutorJob (
Unable to locate id '
 using  a local-only actor system
Failed to decode distributed invocation target expected parameter count,\nerror code: 
Failed to decode the expected number of params of distributed invocation target, error code: 
UnsafeMutablePointer.moveInitialize with negative count
UnsafeMutablePointer.initialize overlapping range
Fatal error
Distributed/LocalTestingDistributedActorSystem.swift
Generic substitutions 
invalid Collection: less than 'count' elements in collection
' is a remote actor reference.
UnsafeMutablePointer.update(repeating:count:) with negative count
Dictionary literal contains duplicate keys
_TtC11DistributedP33_670906D6F767C8D8F71D2E8FF1D478F75_Lock
_TtC11Distributed39DistributedRemoteActorReferenceExecutor
_TtC11Distributed34LocalTestingDistributedActorSystem
_TtC11Distributed29LocalTestingInvocationDecoder
```
