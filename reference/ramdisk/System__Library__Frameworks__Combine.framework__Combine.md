# `/System/Library/Frameworks/Combine.framework/Combine`

From the upgrade restore ramdisk (141-29011-104.dmg). 2,372,064 bytes.

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
wrappedValue setter should be unreachable
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/AnySubscriber.swift
Anonymous AnySubscriber
upstreamSubscription
Combine/Publisher.swift
Attempted to hook into a SubscriberTapMarker with an inner that was not an AnySubscriber. The inner variable for a SubscriberTapMarker must be an AnySubscriber with matching input and failure types.
Received an output without requesting demand
parentSubscription
Invalid state: Received request before sending subscription
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/CombineLatest.swift
receive subscription: (
Combine/Publisher+AsyncSequence.swift
offset element 
Combine/Catch.swift
Unexpected state: request before subscription sent
Cancelled Events
init()
Combine.ClosureBasedAnySubscriber
success
error
Fatal error
downstreamDemand
Combine/FilterProducer.swift
Invalid state: Received completion before receiving subscription
output
completion
lower upper 
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/FilterProducer.swift
Combine.AnySubscriberBox
upstreamSubscriptions
identification-source-type
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/AnyPublisher.swift
Combine.PublisherBox
Unexpected state: received completion but do not have subscription
Invalid state: Received value before receiving subscription
receive error: (
Combine/Published.swift
wrappedValue getter should be unreachable
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/ReduceProducer.swift
/Library/Caches/com.apple.xbs/A3601E47-B864-489E-98DF-02B2C8B2DD35/TemporaryDirectory.b73QLS/Sources/PubSub/Combine/Source/Zip.swift
receive finished
receive value: (
downstreamSubject
_TtC7Combine14AnyCancellable
_TtC7Combine25ObservableObjectPublisher
_TtCC7Combine25ObservableObjectPublisherP33_40FA7804DFFDD9097A0F4AE4A57029327Conduit
_TtC7Combine9DebugHook
parent
upstreamLock
dueTime
options
finishCount
outerFinished
result
triggerSink
upstreamSubscription
buffer
nextInnerIndex
terminal
scheduledToEmit
prefixState
count
pendingSubscriptions
prefetch
receiveSubscriptionThunk
stream
subscription
subscriptions
timer
decode
descriptionThunk
established
object
receiveCompletion
upstreamFinished
errored
demand
identifier
initialDemand
terminationState
alreadySentSubscription
customError
interval
lock
maxPublishers
otherSubscription
remainingCount
strategy
inner
outerSubscription
pendingCompletion
sendOnFailure
receivedUpstream
upstream
base
downstreamRecursive
invoke
sentCompletion
customMirrorThunk
connections
completion
reduce
size
suffix
active
handler
trigger
receiveValueThunk
scheduled
state
triggered
completed
pendingDemand
upstreamCount
values
iterator
encode
receiveOutput
buffers
currentInnerSubscription
didTimeout
handlers
last
remaining
box
map
downstream
innerRecursive
remainingUntilStart
dropping
subject
cancelled
initial
combineIdentifier
receiveSubscription
terminated
downstreams
createSubject
_registrar
hasAnyDownstreamDemand
upstreamCompleted
downstreamDemand
next
playgroundDescriptionThunk
receiveRequest
whenFull
currentGeneration
downstreamLock
finished
finishedWithoutUpstream
predicate
recursion
termination
upstreamFailed
pending
completionRecursion
delivered
outstandingRequests
receiveValue
sequence
currentCancellers
filter
output
prefix
recursive
storage
scheduler
status
value
currentValue
receiveCompletionThunk
tolerance
downstreamNeedsSubscription
downstreamSubject
cancelledOrCompleted
changePublisher
awaitingInnerSubscription
currentInnerIndex
needsSubscribe
otherFinished
receiveCancel
upstreamSubscriptions
keyPath
suffixState
continuation
downstreamRequested
nextPartialResult
target
```
