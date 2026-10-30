# `AudioRemixSubscriber`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<SNMovieRemixSubscriptionProtocol>" _subscription;
@"NSObject<OS_dispatch_queue>" _workQueue;
B _subscriptionIsTerminated;
@? _subscriptionCompletionHandler;
@"SNMovieRemixSession" _session;
@"BWNodeOutput" _nodeMetadataOutput;
B _usePIPAIngestSignalingDomain;
@"NSObject<OS_dispatch_semaphore>" _resultHandlerSemaphore;
@"NSObject<OS_dispatch_semaphore>" _completionHandlerSemaphore;
^{opaqueCMFormatDescription=} _audioMetadataFormatDescription;
{?="value"q"timescale"i"flags"I"epoch"q} _startingPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _endingPTS;
```

## Instance methods

```
-[AudioRemixSubscriber init];
-[AudioRemixSubscriber dealloc];
-[AudioRemixSubscriber activate];
-[AudioRemixSubscriber cancelSubscription];
-[AudioRemixSubscriber finishAndGetResultsBlockingWithStartingPTS:andEndingPTS:];
-[AudioRemixSubscriber handleReceiveCompletion:];
-[AudioRemixSubscriber handleReceiveResult:];
-[AudioRemixSubscriber initWithSession:andNodeMetadataOutput:usePIPAIngestSignalingDomain:completionHandler:];
```
