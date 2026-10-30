# `AVSampleBufferRenderSynchronizerInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakObserver;
^{OpaqueCMTimebase=} readOnlyTimebase;
@"NSObject<OS_dispatch_queue>" rateQueue;
f rate;
{?="value"q"timescale"i"flags"I"epoch"q} mostRecentlySetTime;
@"NSObject<OS_dispatch_queue>" rendererListQueue;
@"NSMutableArray" renderers;
@"NSMutableArray" timedRenderRemovals;
@"NSObject<OS_dispatch_queue>" figSynchronizerAccessQueue;
^{OpaqueFigSampleBufferRenderSynchronizer=} figSynchronizer;
@"<AVLoggingIdentifier>" loggingIdentifier;
@"AVSampleBufferVideoRenderer" rendererTrackedBySTS;
@"NSMutableDictionary" STSLabelSinks;
```
