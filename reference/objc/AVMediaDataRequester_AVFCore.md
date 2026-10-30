# `AVMediaDataRequester`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<AVMediaDataRequesterConsumer>" _mediaDataConsumer;
@"NSObject<OS_dispatch_queue>" _requestQueue;
@? _requestBlock;
^{OpaqueFigSimpleMutex=} _invalidateMutex;
B _invalidatePending;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_requestQueue) requestQueue;
@property (T@?,R,N,V_requestBlock) requestBlock;
```

## Instance methods

```
-[AVMediaDataRequester requestQueue];
-[AVMediaDataRequester init];
-[AVMediaDataRequester dealloc];
-[AVMediaDataRequester invalidate];
-[AVMediaDataRequester _isInvalidatePending];
-[AVMediaDataRequester _requestMediaDataIfReady];
-[AVMediaDataRequester _setInvalidatePending];
-[AVMediaDataRequester initWithMediaDataConsumer:requestQueue:requestBlock:];
-[AVMediaDataRequester requestBlock];
-[AVMediaDataRequester startRequestingMediaData];
```
