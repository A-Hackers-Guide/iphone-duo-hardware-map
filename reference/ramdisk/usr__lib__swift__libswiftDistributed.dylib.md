# `/usr/lib/swift/libswiftDistributed.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 271,152 bytes.

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
Cannot assume to be 'isolated 
Distributed/DistributedDefaultExecutor.swift
in Decoder.userInfo, while decoding 
Unexpectedly found nil while unwrapping an Optional value
Failed to decode distributed invocation target expected parameter count,\nerror code: 
UnsafeMutableBufferPointer with negative count
 (
invalid Collection: less than 'count' elements in collection
Precondition failed
Failed to locate distributed function accessor
UnsafeMutablePointer.initialize with negative count
Distributed/DistributedActor.swift
\ndecoded: 
Generic substitutions 
Cannot call generic method without generic argument substitutions
invoked distributed stub '
Incorrect actor executor assumption; Expected same executor as 
Attempted to enqueue ExecutorJob (
$distributed_actor_system
)
UnsafeMutablePointer.initialize overlapping range
Insufficient space allocated to copy string contents
Fatal error
Attempted to call encoder method in a local-only actor system
UnsafeMutablePointer.update(repeating:count:) with negative count
Swift/UnsafeBufferPointer.swift
Failed to resolve id '
 using a local-only actor system
Attempted to call decoder method in a local-only actor system
 using  a local-only actor system
Swift/Dictionary.swift
Failed to decode distributed target return type
Failed to allocate buffer for distributed target return type
' is a remote actor reference.
Unable to locate id '
\nmangled name: 
Failed to decode the expected number of params of distributed invocation target, error code: 
Negative value is not representable
 do not satisfy generic requirements of 
UnsafeMutablePointer.moveInitialize with negative count
) on executor of remote distributed actor reference!
Distributed/LocalTestingDistributedActorSystem.swift
Attempted to mark an unknown actor '
Missing system (for key .actorSystemKey) 
Unexpected invocation of distributed method '
, expected params: 
Swift/UnsafePointer.swift
' since distributed actor '
Attempted to make remote call to 
Dictionary literal contains duplicate keys
Swift/Integers.swift
Missing DistributedActorSystem userInfo while decoding
Swift/StringUTF8View.swift
Swift/ContiguousArrayBuffer.swift
Incorrect actor executor assumption; Expected '
Distributed/DistributedAssertions.swift
_TtC11Distributed29LocalTestingInvocationDecoder
_TtC11DistributedP33_670906D6F767C8D8F71D2E8FF1D478F75_Lock
_TtC11Distributed39DistributedRemoteActorReferenceExecutor
_TtC11Distributed34LocalTestingDistributedActorSystem
activeActorsLock
activeActors
assignedIDsLock
assignedIDs
idProvider
underlying
```
