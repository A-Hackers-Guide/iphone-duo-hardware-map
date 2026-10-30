# `/System/Library/Frameworks/Combine.framework/Combine`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 2,372,064 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 4288)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/Library/Frameworks/Combine.framework/Combine (compatibility version 1.0.0, current version 3023.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftObservation.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (4 classes, 0 protocols)

Classes: `_TtC7Combine14AnyCancellable`, `_TtC7Combine25ObservableObjectPublisher`, `_TtC7Combine9DebugHook`, `_TtCC7Combine25ObservableObjectPublisherP33_40FA7804DFFDD9097A0F4AE4A57029327Conduit`

## Strings (188)

```
receiveSubscription
receiveValueThunk
recursion
storage
downstreamLock
recursive
createSubject
cancelled
encode
sequence
subscriptions
currentValue
finished
receiveSubscriptionThunk
sendOnFailure
continuation
active
parent
playgroundDescriptionThunk
decode
demand
downstreamRequested
last
receiveOutput
initialDemand
otherSubscription
pendingCompletion
upstreamFinished
established
result
termination
cancelledOrCompleted
scheduledToEmit
completion
connections
terminated
downstreamNeedsSubscription
handlers
remainingUntilStart
keyPath
initial
pending
nextInnerIndex
prefixState
receiveCompletion
sentCompletion
completed
completionRecursion
trigger
lock
upstreamSubscriptions
scheduled
handler
downstreamSubject
next
pendingSubscriptions
receiveCompletionThunk
receiveValue
remaining
count
iterator
size
triggered
awaitingInnerSubscription
_registrar
combineIdentifier
receiveRequest
errored
invoke
finishCount
upstreamCount
buffers
delivered
otherFinished
upstream
values
predicate
upstreamLock
subject
dueTime
options
base
outstandingRequests
prefetch
whenFull
descriptionThunk
remainingCount
state
strategy
suffix
map
currentGeneration
currentInnerSubscription
receivedUpstream
inner
innerRecursive
status
terminal
value
alreadySentSubscription
finishedWithoutUpstream
object
outerFinished
target
didTimeout
downstreamDemand
identifier
interval
nextPartialResult
prefix
subscription
maxPublishers
pendingDemand
buffer
box
outerSubscription
timer
downstream
receiveCancel
reduce
triggerSink
upstreamCompleted
upstreamSubscription
dropping
currentInnerIndex
customMirrorThunk
downstreamRecursive
stream
terminationState
scheduler
changePublisher
needsSubscribe
output
suffixState
tolerance
upstreamFailed
currentCancellers
customError
downstreams
filter
hasAnyDownstreamDemand
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/ReduceProducer.swift
Combine/Catch.swift
Invalid state: Received value before receiving subscription
Invalid state: Received request before sending subscription
Cancelled Events
receive finished
receive value: (
Combine/Publisher.swift
success
Received an output without requesting demand
Anonymous AnySubscriber
upstreamSubscription
Combine/Published.swift
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/AnyPublisher.swift
Combine.PublisherBox
Unexpected state: request before subscription sent
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/AnySubscriber.swift
init()
error
Combine/Publisher+AsyncSequence.swift
Combine/FilterProducer.swift
Attempted to hook into a SubscriberTapMarker with an inner that was not an AnySubscriber. The inner variable for a SubscriberTapMarker must be an AnySubscriber with matching input and failure types.
parentSubscription
downstreamDemand
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/Zip.swift
Combine.AnySubscriberBox
receive error: (
downstreamSubject
Unexpected state: received completion but do not have subscription
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/FilterProducer.swift
completion
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/CombineLatest.swift
lower upper 
Invalid state: Received completion before receiving subscription
output
identification-source-type
receive subscription: (
wrappedValue getter should be unreachable
wrappedValue setter should be unreachable
Fatal error
offset element 
Combine.ClosureBasedAnySubscriber
upstreamSubscriptions
_TtC7Combine14AnyCancellable
_TtC7Combine25ObservableObjectPublisher
_TtCC7Combine25ObservableObjectPublisherP33_40FA7804DFFDD9097A0F4AE4A57029327Conduit
_TtC7Combine9DebugHook
```
