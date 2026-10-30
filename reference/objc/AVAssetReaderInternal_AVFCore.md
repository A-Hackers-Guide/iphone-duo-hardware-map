# `AVAssetReaderInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
@"AVAsset" asset;
^{OpaqueFigAssetReader=} figAssetReader;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} timeRange;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} windowExtendedTimeRange;
B readSingleSample;
B realTime;
@"NSMutableArray" outputs;
@"NSMutableSet" outputFinishedCallbackInvokers;
q status;
@"NSError" error;
@"NSError" errorThatOccurredBeforeStartReading;
@"NSObject<OS_dispatch_queue>" statusReadWriteQueue;
```
