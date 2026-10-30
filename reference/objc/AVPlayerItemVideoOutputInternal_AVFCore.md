# `AVPlayerItemVideoOutputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
^{OpaqueCMTimebase=} timebase;
d currentRate;
^{OpaqueFigVisualContext=} vc;
@"AVWeakReference" playerItemWeakReference;
@"AVWeakReferencingDelegateStorage" delegateStorage;
^{OpaqueVTPixelBufferConformer=} pixelBufferConformer;
@"NSObject<OS_dispatch_queue>" stateQueue;
@"NSObject<OS_dispatch_source>" delegateWakeupSource;
d advanceWakeUpInterval;
B advanceWakeUpIntervalIsValid;
{?="value"q"timescale"i"flags"I"epoch"q} wakeUpImageTime;
B immediateWakeUp;
q clientStateOnRequestedMediaDataChangeNotification;
B suppressesPlayerRendering;
B shouldTagBuffersWithInfo;
@"AVVideoOutputSettings" videoSettings;
```
