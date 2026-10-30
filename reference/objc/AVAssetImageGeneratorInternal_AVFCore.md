# `AVAssetImageGeneratorInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
^{OpaqueFigAssetImageGenerator=} generator;
@"AVAsset" asset;
B appliesPreferredTrackTransform;
{CGSize="width"d"height"d} maximumSize;
@"NSString" apertureMode;
{?="value"q"timescale"i"flags"I"epoch"q} requestedTimeToleranceBefore;
{?="value"q"timescale"i"flags"I"epoch"q} requestedTimeToleranceAfter;
@"NSMutableArray" requests;
@"NSObject<OS_dispatch_queue>" requestsQueue;
i nextRequestID;
@"AVVideoComposition" videoComposition;
@"AVCustomVideoCompositorSession" customVideoCompositorSession;
@"NSObject<OS_dispatch_queue>" imageRequestQueue;
i cancelledRequestIDThreshold;
@"NSObject<OS_dispatch_queue>" generateImagesAsyncQueue;
@"NSString" dynamicRangePolicy;
B allowsProfessionalVideoWorkflowVideoDecoders;
B useSWDecoderForAV1;
q status;
```
