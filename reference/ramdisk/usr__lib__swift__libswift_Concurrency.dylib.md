# `/usr/lib/swift/libswift_Concurrency.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,198,832 bytes.

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
not all allocations are deallocated
Not on the main executor
accumulating task group should never use raw-errors!
TaskGroupStatus{ 
y
_Concurrency/DiscardingTaskGroup.swift
Impossible to have cancelled before we began
ManagedBufferPointer buffer class must be non-@objc
Unknown
com.apple.swift.concurrency
TaskPriority.high
Double value cannot be converted to Int because the result would be greater than Int.max
_Concurrency/UnsafeMutableBufferPointer+Utilities.swift
attempt to await next() on more than one task
Swift/ManagedBuffer.swift
warning
Resuming continuation for task %p that is not awaited (may have already been resumed).\n
Actor
Continuation was deinitialized without being resumed.
run(until condition:) not supported on this executor
Swift/RangeReplaceableCollection.swift
Swift/Array.swift
Index range out of bounds
actor-isolation-violation
Negative value is not representable
UnsafeMutablePointer.initialize overlapping range
Invalid slice
Closure must not replace the provided buffer
_Concurrency/CFExecutor.swift
 leaked its continuation without resuming it. This may cause tasks waiting on it to remain suspended forever.\n
Discarding
 P:
Precondition failed
Can't prefix a negative number of elements from an async sequence
UnownedJob(id: nil)
_Concurrency/UnimplementedExecutor.swift
Unknown clock ID 
Can't remove more elements than there are in the Collection
Can't drop a negative number of elements from an async sequence
UnsafeBufferPointer has a nil start and nonzero count
Can't remove first element from an empty collection
Array replace: subrange extends past the end
swift6
Unexpected IsIsolatingCurrentContextDecision value
__DATA
Range requires lowerBound <= upperBound
task-group-violation
task-local-violation
TaskPriority.background
_Concurrency/TaskGroup.swift
Double value cannot be converted to Int because the result would be less than Int.min
Swift/Collection.swift
/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
Swift/ArrayBufferProtocol.swift
the main thread
 }
Sorry, cannot schedule on an unknown clock
_Concurrency/_UnsafeWrappedBuffer.swift
Swift/ContiguousArray.swift
Index out of bounds
_Concurrency/TaskSleepDuration.swift
error: %sTaskGroup: detected pending task count overflow, in task group %p! Status: %s
n
_Concurrency/CooperativeExecutor.swift
Swift/Range.swift
_Concurrency/Deque+Storage.swift
Swift/IntegerTypes.swift
TaskGroup exceeded supported pending task count
__s64async_hook
_Concurrency/AsyncThrowingStream.swift
ExecutorJob(id: 
baseAddress must be a properly aligned pointer for type T
unknown clock in Dispatch Executor
@MainActor function
only errors can be stored by a discarding task group, yet it wasn't an error! 2
Task-local bound in illegal context
Unexpected isolation context, expected to be executing on 
DispatchMainExecutor does not support recursion
Number of elements to remove should be non-negative
UnsafeMutablePointer.deinitialize with negative count
legacy
_Concurrency/AsyncDropFirstSequence.swift
_Concurrency/Continuation.swift
Incorrect actor executor assumption; Expected '
ExecutorJob(id: nil)
_Concurrency/PartialAsyncTask.swift
Swift/UnsafeBufferPointer.swift
Cannot wake before we even started
Fatal error: invalid clock ID %d\n
only errors can be stored by a discarding task group, yet it wasn't an error! 1
_Concurrency/Executor.swift
UnsafeMutablePointer.initialize with negative count
UnsafeMutableBufferPointer has a nil start and nonzero count
Can't insert element at invalid index
Unable to look up 
invalid job priority %#zx
SWIFT TASK CONTINUATION MISUSE: 
_Concurrency/ExecutorImpl.swift
invalid Collection: count differed in successive traversals
Object %p of class %s deallocated with non-zero retain count %zd. This object's deinit, or something called from it, may have created a strong reference to self which outlived deinit, resulting in a dangling reference.\n
Initializing continuation for task %p that was already initialized.\n
Task
 tried to resume its continuation more than once, returning 
 tried to resume its continuation more than once, throwing 
crash
error
 R:
Can't removeLast from an empty Array
Range cannot have an unordered upper bound.
Actor-isolated function called from another thread
Initialized count must be in 0 ... unsafeUninitializedCapacity.
Can't remove a negative number of elements
CFRunLoopGetMain
_Concurrency/Deque+UnsafeHandle.swift
actor-isolated function
Incorrect actor executor assumption; expected '%.*s' executor.\n
_Concurrency/TaskSleep.swift
Double value cannot be converted to Int because it is either infinite or NaN
<unknown>
future reported an error, but wait cannot throw
C:
 W:
Fatal error: Call of deleted method
UnsafeMutableRawBufferPointer with negative count
TaskPriority(rawValue: 
_Concurrency/Deque+Collection.swift
nocrash
 
_Concurrency/CheckedContinuation.swift
Range out of bounds
the same actor
error: task-local: detected illegal task-local value binding at %.*s:%d.\nTask-local values must only be set in a structured-context, such as: around any (synchronous or asynchronous function invocation), around an 'async let' declaration, 
PotentialPriorityInversion
Swift/Integers.swift
Invalid state for non-cancelled sleep task
UnsafeMutableBufferPointer with negative count
Cannot remove last element of an empty Deque
 in CoreFoundation
Can't reassign buffer in Array(unsafeUninitializedCapacity:initializingWith:)
Incorrect actor executor assumption; Expected same executor as 
Array replace: subrange start is negative
SWIFT_UNEXPECTED_EXECUTOR_LOG_LEVEL
_Concurrency/AsyncStream.swift
Global executor does not support thread donation
Can't remove more items from a collection than it has
_Concurrency/Errors.swift
Not enough bits to represent the passed value
Swift/UnsafePointer.swift
_Concurrency/DispatchExecutor.swift
DispatchMainExecutor cannot be stopped
Impossible to have multiple active continuations
freed pointer not among allocations
Unexpectedly found nil while unwrapping an Optional value
_Concurrency/_DequeSlot.swift
Range cannot have an unordered lower bound.
%s: data race detected: %s at %.*s:%d was not called on %s\n
NotIsolated
Illegal attempt to set a TaskLocal value, use `withValue(...) { ... }` instead.
freed pointer was not the last allocation
Fatal error
UnsafeBufferPointer with negative count
Swift/ContiguousArrayBuffer.swift
ManagedBufferPointer buffer class has illegal stored properties
_Concurrency/AsyncPrefixSequence.swift
Swift/UnsafeRawBufferPointer.swift
TaskPriority.low
_Concurrency/TaskLocal.swift
There is no executor implementation active
Assertion failed
Can't insert elements at an invalid index
Already finished normally, can't do that again
Isolated
Claimed NULL waitingTask!
TaskPriority.medium
Index out of range
UnsafeMutablePointer.moveInitialize with negative count
Can't remove last element from an empty collection
Cannot remove first element of an empty Deque
_Concurrency/AsyncStreamBuffer.swift
actor_enqueue
task=%lld waitingOnTask=%lld status=0x%lx taskPointer=%p
context=%p
task=%lld
actor_job_queue
actor_dequeue
task=%lld taskPointer=%p
context=%p error=%{bool}d
actor_lifetime
actor=%p task=%lld taskPointer=%p metadata=%p descriptor=%p
 enableTelemetry=YES actor=%p oldPriority=%zu newPriority=%zu
task=%lld jobPriority=%u isChildTask=%{bool}d, isFuture=%{bool}d isGroupChildTask=%{bool}d isAsyncLetTask=%{bool}d taskPointer=%p
job_enqueue_global
job_enqueue_global_with_delay
task_lifetime
task_continuation_await
task_status_changed
actor=%p typeName=%.*s
scheduled_actor_inversion
task_continuation
enqueued_task_inversion
job_run
actor_state_changed
actor=%p jobCount=%u
actor=%p
task_flags_changed
task=%lld resumefn=%p maxPriority=%u, isCancelled=%{bool}d isEscalated=%{bool}d, isRunning=%{bool}d, isEnqueued=%{bool}d taskName=%{public}s taskPointer=%p
task_switch_executor
task=%lld delay=%llu taskPointer=%p
task_wait
task=%lld resumefn=%p jobPriority=%u isChildTask=%{bool}d, isFuture=%{bool}d isGroupChildTask=%{bool}d isAsyncLetTask=%{bool}d parent=%lld group=%p asyncLet=%p isDiscardingTask=%{bool}d hasInitialTaskExecutorPreference=%{bool}d taskName=%{p
 enableTelemetry=YES task=%llx oldPriority=%zu newPriority=%zu
task=%lld taskPointer=%p actor=%p executor=%p metadata=%p descriptor=%p taskName=%{public}s executorKind=%u
task=%lld taskPointer=%p executor=%p metadata=%p descriptor=%p executorKind=%u
actor=%p needsPreprocessing=%d state=%u isDistributedRemote=%{bool}d isPriorityEscalated=%{bool}d, maxPriority=%u
actor_deallocate
job_enqueue_executor
task=%lld context=%p taskPointer=%p
_TtCs14CFTaskExecutor
_TtCs19CooperativeExecutor
_TtCs17DispatchQueueShim
_TtCs32_DefaultGlobalConcurrentExecutor
_TtCs25UnimplementedMainExecutor
_TtCs25UnimplementedTaskExecutor
_TtCs20DispatchMainExecutor
_TtCs26DispatchGlobalTaskExecutor
_TtCs25CheckedContinuationCanary
_TtCs9MainActor
_TtCs14CFMainExecutor
produce
shouldStop
state
suspendingWaitQueue
threaded
continuousWaitQueue
storage
_value
defaultValue
runQueue
```
