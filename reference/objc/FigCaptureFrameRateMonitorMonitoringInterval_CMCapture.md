# `FigCaptureFrameRateMonitorMonitoringInterval`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _title;
d _interval;
B _shouldLog;
@? _monitoringBlock;
B _paused;
B _firstFrameAfterTimerStart;
B _skipFirstStatsAfterResume;
q _preStartFramesCount;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSObject<OS_dispatch_source>" _timer;
@"NSObject<OS_dispatch_queue>" _timerQueue;
@"BWStats" _framePeriodStats;
@"BWStats" _latencyStats;
q _intervalFramesCount;
{?="value"q"timescale"i"flags"I"epoch"q} _intervalStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _intervalLastFramePTS;
```

## Instance methods

```
-[FigCaptureFrameRateMonitorMonitoringInterval stop];
-[FigCaptureFrameRateMonitorMonitoringInterval dealloc];
-[FigCaptureFrameRateMonitorMonitoringInterval start];
-[FigCaptureFrameRateMonitorMonitoringInterval _startTimer];
-[FigCaptureFrameRateMonitorMonitoringInterval _stopTimer];
-[FigCaptureFrameRateMonitorMonitoringInterval resumeIfNeeded];
-[FigCaptureFrameRateMonitorMonitoringInterval pauseIfNeeded];
-[FigCaptureFrameRateMonitorMonitoringInterval _initializeStats];
-[FigCaptureFrameRateMonitorMonitoringInterval _processInterval];
-[FigCaptureFrameRateMonitorMonitoringInterval addPTS:latency:framePeriod:];
-[FigCaptureFrameRateMonitorMonitoringInterval initWithTitle:interval:shouldLog:monitoringBlock:];
```
