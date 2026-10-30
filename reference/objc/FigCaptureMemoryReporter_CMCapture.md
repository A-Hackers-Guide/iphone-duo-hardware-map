# `FigCaptureMemoryReporter`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 30 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _memoryReporterDispatchQueue;
@"NSObject<OS_dispatch_source>" _memoryReporterTimer;
@"NSObject<OS_dispatch_source>" _memgraphCoolDownTimer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _memgraphLock;
B _stateChangedSinceLastReport;
i _numActiveClients;
B _activeClientsIncludeCamera;
B _activeClientsIncludeCameraMessagesApp;
I _hostPort;
Q _pageSize;
i _my_pid;
B _alwaysGenerateMemGraph;
B _alwaysListTransactions;
B _alwaysGenerateLog;
I _memGraphFootprintLowerKb;
I _listTransactionsFootprintLowerKb;
I _reportFootprintUpperBandkB;
I _reportFootprintLowerBandkB;
I _reportWiredUpperBandkB;
I _reportWiredLowerBandkB;
B _anyLoggingEnabled;
Q _highFrequencyMilliseconds;
Q _lowFrequencyMilliSeconds;
Q _currentFootprint;
AQ _peakFootprint;
@"NSObject<OS_os_log>" _log;
@"BWMemoryPool" _memoryPool;
B _ttrFiledForStuckMMAssertion;
d _mmAssertionHeldSecondsAtIdleTransition;
```

## Properties

```
@property (TQ,R,V_currentFootprint) currentFootprint;
```

## Class methods

```
+[FigCaptureMemoryReporter sharedInstance];
```

## Instance methods

```
-[FigCaptureMemoryReporter init];
-[FigCaptureMemoryReporter dealloc];
-[FigCaptureMemoryReporter currentFootprint];
-[FigCaptureMemoryReporter decrementActiveClientCount:clientIsCameraMessagesApp:];
-[FigCaptureMemoryReporter generateMemgraphWithReason:];
-[FigCaptureMemoryReporter incrementActiveClientCount:clientIsCameraMessagesApp:withMemoryPool:];
-[FigCaptureMemoryReporter peakFootprintSinceReset];
-[FigCaptureMemoryReporter resetPeakFootprint];
```
