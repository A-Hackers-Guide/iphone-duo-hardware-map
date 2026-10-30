# `FigCaptureFrameRateMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSString" _title;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _started;
@"NSMutableArray" _monitoringIntervals;
q _totalFramesCount;
{?="value"q"timescale"i"flags"I"epoch"q} _totalFirstFramePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _totalLastFramePTS;
```

## Properties

```
@property (T@"NSString",R,N,V_title) title;
@property (TB,R,N) started;
```

## Class methods

```
+[FigCaptureFrameRateMonitor initialize];
+[FigCaptureFrameRateMonitor osStateData];
```

## Instance methods

```
-[FigCaptureFrameRateMonitor addPTS:];
-[FigCaptureFrameRateMonitor addPTS:latency:];
-[FigCaptureFrameRateMonitor initWithTitle:];
-[FigCaptureFrameRateMonitor stop];
-[FigCaptureFrameRateMonitor dealloc];
-[FigCaptureFrameRateMonitor started];
-[FigCaptureFrameRateMonitor start];
-[FigCaptureFrameRateMonitor addMonitoringInterval:shouldLog:monitoringBlock:];
-[FigCaptureFrameRateMonitor title];
-[FigCaptureFrameRateMonitor resumeIfNeeded];
-[FigCaptureFrameRateMonitor _summaryIsolated];
-[FigCaptureFrameRateMonitor summary];
-[FigCaptureFrameRateMonitor addMonitoringInterval:];
-[FigCaptureFrameRateMonitor pauseIfNeeded];
```
