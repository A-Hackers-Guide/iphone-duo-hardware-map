# `AVCaptureTimecodeGenerator`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 7 properties, 34 instance methods, 2 class methods

## Instance variables

```
@"NSOperationQueue" _statusNotificationSchedulingQueue;
^{?={AVCaptureTimecode=CCCCI{?=qiIq}q}Qq} _timecodeRingBuffer;
Q _timecodeRingBufferHead;
B _isTimecodeRingBufferFull;
Q _timecodeRingBufferCapacity;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _resourceLock;
d _timecodeRingBufferIngestTimeStamp;
@"NSOperationQueue" _ringBufferStatusPollingQueue;
q _synchronizationStatus;
I _midiSourceDiscoveryClient;
I _midiClient;
I _midiInputPort;
d _localGMTOffset;
{mach_timebase_info="numer"I"denom"I} _machTimebase;
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"NSMutableArray" _mutableSynchronizationSources;
@"AVCaptureTimecodeSource" _currentSource;
@"NSObject<OS_dispatch_queue>" _delegateCallbackQueue;
d _synchronizationTimeout;
d _timecodeAlignmentOffset;
{?="value"q"timescale"i"flags"I"epoch"q} _timecodeFrameDuration;
```

## Properties

```
@property (T@"NSArray",R,C) availableSources;
@property (T@"AVCaptureTimecodeSource",R,N,V_currentSource) currentSource;
@property (T@"<AVCaptureTimecodeGeneratorDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_delegateCallbackQueue) delegateCallbackQueue;
@property (Td,N,V_synchronizationTimeout) synchronizationTimeout;
@property (Td,N,V_timecodeAlignmentOffset) timecodeAlignmentOffset;
@property (T{?=qiIq},N,V_timecodeFrameDuration) timecodeFrameDuration;
```

## Class methods

```
+[AVCaptureTimecodeGenerator frameCountSource];
+[AVCaptureTimecodeGenerator realTimeClockSource];
```

## Instance methods

```
-[AVCaptureTimecodeGenerator setDelegate:queue:];
-[AVCaptureTimecodeGenerator currentSource];
-[AVCaptureTimecodeGenerator init];
-[AVCaptureTimecodeGenerator dealloc];
-[AVCaptureTimecodeGenerator callbackQueue];
-[AVCaptureTimecodeGenerator delegate];
-[AVCaptureTimecodeGenerator delegateCallbackQueue];
-[AVCaptureTimecodeGenerator _registerSynchronizationSource:];
-[AVCaptureTimecodeGenerator _addTimecodeToRingBuffer:timestamp:baseOffset:];
-[AVCaptureTimecodeGenerator _isTimecodeRingBufferEmpty];
-[AVCaptureTimecodeGenerator _isTimecodeRingBufferStale];
-[AVCaptureTimecodeGenerator _newestTimecodeRingBufferEntry];
-[AVCaptureTimecodeGenerator _notifyDelegateOfSourceListUpdate:];
-[AVCaptureTimecodeGenerator _notifyDelegateOfSynchronizationStatusChange:filterRedundancy:];
-[AVCaptureTimecodeGenerator _notifyDelegateOfTimecodeUpdate:];
-[AVCaptureTimecodeGenerator _openMidiTimecodeDataStreamWithUUID:success:];
-[AVCaptureTimecodeGenerator _pollRingBufferStatus];
-[AVCaptureTimecodeGenerator _registerMidiEndpointAsSynchronizationSource:];
-[AVCaptureTimecodeGenerator _removeMidiEndpointAsSynchronizationSource:];
-[AVCaptureTimecodeGenerator _removeSynchronizationSource:];
-[AVCaptureTimecodeGenerator _resetTimecodeRingBuffer];
-[AVCaptureTimecodeGenerator _scheduleTimecodeRingBufferPolling];
-[AVCaptureTimecodeGenerator _timeOfDay];
-[AVCaptureTimecodeGenerator _timecodeIsCoherent:];
-[AVCaptureTimecodeGenerator availableSources];
-[AVCaptureTimecodeGenerator generateInitialTimecode];
-[AVCaptureTimecodeGenerator setSynchronizationTimeout:];
-[AVCaptureTimecodeGenerator setTimecodeAlignmentOffset:];
-[AVCaptureTimecodeGenerator setTimecodeFrameDuration:];
-[AVCaptureTimecodeGenerator startExternalSourceObserver];
-[AVCaptureTimecodeGenerator startSynchronizationWithTimecodeSource:];
-[AVCaptureTimecodeGenerator synchronizationTimeout];
-[AVCaptureTimecodeGenerator timecodeAlignmentOffset];
-[AVCaptureTimecodeGenerator timecodeFrameDuration];
```
