# `/usr/lib/swift/libswift_Concurrency.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,198,832 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 4576)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (11 classes, 0 protocols)

Classes: `_TtCs14CFMainExecutor`, `_TtCs14CFTaskExecutor`, `_TtCs17DispatchQueueShim`, `_TtCs19CooperativeExecutor`, `_TtCs20DispatchMainExecutor`, `_TtCs25CheckedContinuationCanary`, `_TtCs25UnimplementedMainExecutor`, `_TtCs25UnimplementedTaskExecutor`, `_TtCs26DispatchGlobalTaskExecutor`, `_TtCs32_DefaultGlobalConcurrentExecutor`, `_TtCs9MainActor`

## Strings (238)

```
Can't insert element at invalid index
only errors can be stored by a discarding task group, yet it wasn't an error! 2
TaskGroupStatus{ 
Illegal attempt to set a TaskLocal value, use `withValue(...) { ... }` instead.
Double value cannot be converted to Int because it is either infinite or NaN
Can't remove a negative number of elements
Object %p of class %s deallocated with non-zero retain count %zd. This object's deinit, or something called from it, may have created a strong reference to self which outlived deinit, resulting in a dangling reference.\n
__DATA
There is no executor implementation active
_Concurrency/Deque+Collection.swift
attempt to await next() on more than one task
Initializing continuation for task %p that was already initialized.\n
TaskPriority.high
UnsafeBufferPointer has a nil start and nonzero count
Index out of bounds
Closure must not replace the provided buffer
CFRunLoopGetMain
Already finished normally, can't do that again
Array replace: subrange extends past the end
future reported an error, but wait cannot throw
_Concurrency/AsyncPrefixSequence.swift
Swift/RangeReplaceableCollection.swift
ManagedBufferPointer buffer class must be non-@objc
task-group-violation
Task-local bound in illegal context
TaskPriority(rawValue: 
_Concurrency/TaskSleepDuration.swift
freed pointer not among allocations
 W:
Precondition failed
Initialized count must be in 0 ... unsafeUninitializedCapacity.
invalid Collection: count differed in successive traversals
Swift/UnsafeBufferPointer.swift
%s: data race detected: %s at %.*s:%d was not called on %s\n
Incorrect actor executor assumption; Expected '
_Concurrency/TaskGroup.swift
_Concurrency/Deque+UnsafeHandle.swift
Not on the main executor
Discarding
Negative value is not representable
baseAddress must be a properly aligned pointer for type T
Assertion failed
Can't remove more elements than there are in the Collection
Impossible to have multiple active continuations
_Concurrency/AsyncStreamBuffer.swift
_Concurrency/Continuation.swift
Fatal error: Call of deleted method
ExecutorJob(id: 
UnsafeMutablePointer.initialize with negative count
Can't reassign buffer in Array(unsafeUninitializedCapacity:initializingWith:)
 R:
TaskPriority.medium
TaskPriority.low
DispatchMainExecutor cannot be stopped
 leaked its continuation without resuming it. This may cause tasks waiting on it to remain suspended forever.\n
Actor
_Concurrency/PartialAsyncTask.swift
_Concurrency/TaskSleep.swift
Unknown clock ID 
UnsafeMutablePointer.initialize overlapping range
Swift/ContiguousArray.swift
_Concurrency/DispatchExecutor.swift
ManagedBufferPointer buffer class has illegal stored properties
Swift/IntegerTypes.swift
Double value cannot be converted to Int because the result would be less than Int.min
warning
y
error: task-local: detected illegal task-local value binding at %.*s:%d.\nTask-local values must only be set in a structured-context, such as: around any (synchronous or asynchronous function invocation), around an 'async let' declaration, 
Unexpectedly found nil while unwrapping an Optional value
Not enough bits to represent the passed value
Task
TaskPriority.background
Can't remove last element from an empty collection
Cannot wake before we even started
Can't remove first element from an empty collection
Can't remove more items from a collection than it has
@MainActor function
swift6
 tried to resume its continuation more than once, throwing 
_Concurrency/Executor.swift
_Concurrency/UnimplementedExecutor.swift
Global executor does not support thread donation
_Concurrency/Deque+Storage.swift
Range cannot have an unordered lower bound.
only errors can be stored by a discarding task group, yet it wasn't an error! 1
__s64async_hook
Sorry, cannot schedule on an unknown clock
UnsafeMutableBufferPointer with negative count
Swift/Array.swift
_Concurrency/_DequeSlot.swift
Range requires lowerBound <= upperBound
Actor-isolated function called from another thread
_Concurrency/AsyncDropFirstSequence.swift
ExecutorJob(id: nil)
_Concurrency/TaskLocal.swift
_Concurrency/ExecutorImpl.swift
_Concurrency/UnsafeMutableBufferPointer+Utilities.swift
Range cannot have an unordered upper bound.
unknown clock in Dispatch Executor
Fatal error
_Concurrency/AsyncThrowingStream.swift
Array replace: subrange start is negative
Unknown
Resuming continuation for task %p that is not awaited (may have already been resumed).\n
 tried to resume its continuation more than once, returning 
UnsafeMutableRawBufferPointer with negative count
Unexpected isolation context, expected to be executing on 
Number of elements to remove should be non-negative
com.apple.swift.concurrency
_Concurrency/CheckedContinuation.swift
Double value cannot be converted to Int because the result would be greater than Int.max
Cannot remove first element of an empty Deque
_Concurrency/CFExecutor.swift
NotIsolated
Claimed NULL waitingTask!
Can't prefix a negative number of elements from an async sequence
_Concurrency/Errors.swift
Can't removeLast from an empty Array
Can't insert elements at an invalid index
/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
Swift/ManagedBuffer.swift
Isolated
C:
UnownedJob(id: nil)
Range out of bounds
Swift/Collection.swift
DispatchMainExecutor does not support recursion
Impossible to have cancelled before we began
UnsafeMutablePointer.deinitialize with negative count
UnsafeMutablePointer.moveInitialize with negative count
error
<unknown>
Fatal error: invalid clock ID %d\n
SWIFT_UNEXPECTED_EXECUTOR_LOG_LEVEL
legacy
the same actor
Incorrect actor executor assumption; expected '%.*s' executor.\n
freed pointer was not the last allocation
TaskGroup exceeded supported pending task count
run(until condition:) not supported on this executor
UnsafeBufferPointer with negative count
Invalid slice
error: %sTaskGroup: detected pending task count overflow, in task group %p! Status: %s
n
invalid job priority %#zx
Can't drop a negative number of elements from an async sequence
Swift/UnsafePointer.swift
_Concurrency/_UnsafeWrappedBuffer.swift
UnsafeMutableBufferPointer has a nil start and nonzero count
_Concurrency/AsyncStream.swift
Swift/ContiguousArrayBuffer.swift
_Concurrency/CooperativeExecutor.swift
actor-isolation-violation
nocrash
the main thread
actor-isolated function
 
Swift/UnsafeRawBufferPointer.swift
Unable to look up 
accumulating task group should never use raw-errors!
PotentialPriorityInversion
SWIFT TASK CONTINUATION MISUSE: 
_Concurrency/DiscardingTaskGroup.swift
Swift/Range.swift
Cannot remove last element of an empty Deque
 in CoreFoundation
Incorrect actor executor assumption; Expected same executor as 
Swift/ArrayBufferProtocol.swift
crash
Unexpected IsIsolatingCurrentContextDecision value
task-local-violation
Invalid state for non-cancelled sleep task
Index range out of bounds
 P:
 }
not all allocations are deallocated
Continuation was deinitialized without being resumed.
Swift/Integers.swift
Index out of range
task=%lld delay=%llu taskPointer=%p
task_lifetime
task=%lld resumefn=%p jobPriority=%u isChildTask=%{bool}d, isFuture=%{bool}d isGroupChildTask=%{bool}d isAsyncLetTask=%{bool}d parent=%lld group=%p asyncLet=%p isDiscardingTask=%{bool}d hasInitialTaskExecutorPreference=%{bool}d taskName=%{p
 enableTelemetry=YES task=%llx oldPriority=%zu newPriority=%zu
task=%lld
actor_enqueue
actor=%p
 enableTelemetry=YES actor=%p oldPriority=%zu newPriority=%zu
task=%lld taskPointer=%p
task_wait
context=%p
task=%lld resumefn=%p maxPriority=%u, isCancelled=%{bool}d isEscalated=%{bool}d, isRunning=%{bool}d, isEnqueued=%{bool}d taskName=%{public}s taskPointer=%p
actor_lifetime
actor=%p jobCount=%u
actor_dequeue
scheduled_actor_inversion
task_flags_changed
task=%lld taskPointer=%p actor=%p executor=%p metadata=%p descriptor=%p taskName=%{public}s executorKind=%u
actor=%p task=%lld taskPointer=%p metadata=%p descriptor=%p
actor_job_queue
context=%p error=%{bool}d
task=%lld context=%p taskPointer=%p
task_status_changed
actor=%p needsPreprocessing=%d state=%u isDistributedRemote=%{bool}d isPriorityEscalated=%{bool}d, maxPriority=%u
job_enqueue_executor
enqueued_task_inversion
job_run
actor=%p typeName=%.*s
task_continuation
actor_deallocate
task_switch_executor
task=%lld jobPriority=%u isChildTask=%{bool}d, isFuture=%{bool}d isGroupChildTask=%{bool}d isAsyncLetTask=%{bool}d taskPointer=%p
job_enqueue_global
task=%lld waitingOnTask=%lld status=0x%lx taskPointer=%p
task_continuation_await
actor_state_changed
task=%lld taskPointer=%p executor=%p metadata=%p descriptor=%p executorKind=%u
job_enqueue_global_with_delay
_TtCs20DispatchMainExecutor
_TtCs25CheckedContinuationCanary
_TtCs19CooperativeExecutor
_TtCs9MainActor
_TtCs25UnimplementedTaskExecutor
_TtCs14CFMainExecutor
_TtCs26DispatchGlobalTaskExecutor
_TtCs17DispatchQueueShim
_TtCs32_DefaultGlobalConcurrentExecutor
_TtCs25UnimplementedMainExecutor
_TtCs14CFTaskExecutor
continuousWaitQueue
storage
_value
produce
defaultValue
shouldStop
state
suspendingWaitQueue
runQueue
threaded
```
