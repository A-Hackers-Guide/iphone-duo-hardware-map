# `AVCaptureDeferredPhotoProcessingRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _photoProxies;
I _firedCallbackFlags;
@"NSMutableArray" _delegatesStorage;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
i _expectedPhotoCount;
i _firedPhotoCallbacksCount;
@"NSString" _originalDeferredPhotoIdentifier;
I _qosClass;
@"NSObject<OS_os_transaction>" _transaction;
```

## Properties

```
@property (T@"NSArray",R,V_delegatesStorage) delegatesStorage;
@property (TI,V_firedCallbackFlags) firedCallbackFlags;
@property (T@"NSMutableArray",R,V_photoProxies) photoProxies;
@property (Ti,N,V_expectedPhotoCount) expectedPhotoCount;
@property (Ti,N,V_firedPhotoCallbacksCount) firedPhotoCallbacksCount;
@property (T@"NSString",C,N,V_originalDeferredPhotoIdentifier) originalDeferredPhotoIdentifier;
@property (TI,N,V_qosClass) qosClass;
```

## Instance methods

```
-[AVCaptureDeferredPhotoProcessingRequest setFiredCallbackFlags:];
-[AVCaptureDeferredPhotoProcessingRequest addDelegate:];
-[AVCaptureDeferredPhotoProcessingRequest dealloc];
-[AVCaptureDeferredPhotoProcessingRequest description];
-[AVCaptureDeferredPhotoProcessingRequest expectedPhotoCount];
-[AVCaptureDeferredPhotoProcessingRequest qosClass];
-[AVCaptureDeferredPhotoProcessingRequest firedCallbackFlags];
-[AVCaptureDeferredPhotoProcessingRequest setFiredPhotoCallbacksCount:];
-[AVCaptureDeferredPhotoProcessingRequest firedPhotoCallbacksCount];
-[AVCaptureDeferredPhotoProcessingRequest originalDeferredPhotoIdentifier];
-[AVCaptureDeferredPhotoProcessingRequest addProxy:];
-[AVCaptureDeferredPhotoProcessingRequest delegatesStorage];
-[AVCaptureDeferredPhotoProcessingRequest initWithPhotoProxy:delegate:delegateQueue:qosClass:];
-[AVCaptureDeferredPhotoProcessingRequest photoProxies];
-[AVCaptureDeferredPhotoProcessingRequest setExpectedPhotoCount:];
-[AVCaptureDeferredPhotoProcessingRequest setOriginalDeferredPhotoIdentifier:];
-[AVCaptureDeferredPhotoProcessingRequest setQosClass:];
```
