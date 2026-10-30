# `AudioRemixSessionManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
@"AudioRemixSubscriber" _subscriber;
@"SNMovieRemixSession" _session;
@"BWNodeOutput" _nodeMetadataOutput;
B _multiCamClientCompositingEnabled;
d _sampleRate;
I _channelCount;
```

## Properties

```
@property (Td,R,N) sampleRate;
@property (TI,R,N) channelCount;
```

## Instance methods

```
-[AudioRemixSessionManager sampleRate];
-[AudioRemixSessionManager channelCount];
-[AudioRemixSessionManager init];
-[AudioRemixSessionManager dealloc];
-[AudioRemixSessionManager setMultiCamClientCompositingEnabled:];
-[AudioRemixSessionManager _handleSessionCreated:];
-[AudioRemixSessionManager _handleSubscriberCompletedFromCancellation:];
-[AudioRemixSessionManager abortSessionIfNeeded];
-[AudioRemixSessionManager finishAndGetResultsBlockingWithStartingPTS:andEndingPTS:];
-[AudioRemixSessionManager initWithNodeMetadataOutput:];
-[AudioRemixSessionManager sessionReady];
-[AudioRemixSessionManager setFormatSampleRate:andChannelCount:];
-[AudioRemixSessionManager startNewSessionBlocking];
-[AudioRemixSessionManager submitAudioBuffer:];
```
