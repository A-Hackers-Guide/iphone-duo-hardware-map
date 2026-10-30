# `AVAsynchronousCIImageFilteringRequestInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"AVAsynchronousVideoCompositionRequest" _compositingRequest;
@? _cancellationTest;
@? _defaultCIContextProvider;
@? _completionHandler;
@"CIImage" _sourceCIImage;
^{__CVBuffer=} _sourcePBuf;
```

## Properties

```
@property (T@"AVAsynchronousVideoCompositionRequest",&,N,V_compositingRequest) compositingRequest;
@property (T@?,C,N,V_cancellationTest) cancellationTest;
@property (T@?,C,N,V_defaultCIContextProvider) defaultCIContextProvider;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"CIImage",&,N,V_sourceCIImage) sourceCIImage;
@property (T^{__CVBuffer=},&,N,V_sourcePBuf) sourcePBuf;
```

## Instance methods

```
-[AVAsynchronousCIImageFilteringRequestInternal setCompletionHandler:];
-[AVAsynchronousCIImageFilteringRequestInternal completionHandler];
-[AVAsynchronousCIImageFilteringRequestInternal dealloc];
-[AVAsynchronousCIImageFilteringRequestInternal _willDeallocOrFinalize];
-[AVAsynchronousCIImageFilteringRequestInternal cancellationTest];
-[AVAsynchronousCIImageFilteringRequestInternal compositingRequest];
-[AVAsynchronousCIImageFilteringRequestInternal defaultCIContextProvider];
-[AVAsynchronousCIImageFilteringRequestInternal setCancellationTest:];
-[AVAsynchronousCIImageFilteringRequestInternal setCompositingRequest:];
-[AVAsynchronousCIImageFilteringRequestInternal setDefaultCIContextProvider:];
-[AVAsynchronousCIImageFilteringRequestInternal setSourceCIImage:];
-[AVAsynchronousCIImageFilteringRequestInternal setSourcePBuf:];
-[AVAsynchronousCIImageFilteringRequestInternal sourceCIImage];
-[AVAsynchronousCIImageFilteringRequestInternal sourcePBuf];
```
