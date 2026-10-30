# `AVAssetWriterInputMediaDataRequester`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _requestQueue;
@? _requestBlock;
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@"AVWeakReference" _weakReferenceToDelegate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_requestQueue) requestQueue;
@property (T@"<AVAssetWriterInputMediaDataRequesterDelegate>",W) delegate;
```

## Instance methods

```
-[AVAssetWriterInputMediaDataRequester requestQueue];
-[AVAssetWriterInputMediaDataRequester init];
-[AVAssetWriterInputMediaDataRequester dealloc];
-[AVAssetWriterInputMediaDataRequester setDelegate:];
-[AVAssetWriterInputMediaDataRequester delegate];
-[AVAssetWriterInputMediaDataRequester _collectUncollectables_invokedFromDeallocAndFinalize];
-[AVAssetWriterInputMediaDataRequester initWithRequestQueue:requestBlock:];
-[AVAssetWriterInputMediaDataRequester requestMediaDataIfNecessary];
```
