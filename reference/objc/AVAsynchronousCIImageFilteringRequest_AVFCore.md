# `AVAsynchronousCIImageFilteringRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"AVAsynchronousCIImageFilteringRequestInternal" _internal;
```

## Properties

```
@property (T{CGSize=dd},R,N) renderSize;
@property (T{?=qiIq},R,N) compositionTime;
@property (T@"CIImage",R,N) sourceImage;
```

## Instance methods

```
-[AVAsynchronousCIImageFilteringRequest renderSize];
-[AVAsynchronousCIImageFilteringRequest finishWithError:];
-[AVAsynchronousCIImageFilteringRequest dealloc];
-[AVAsynchronousCIImageFilteringRequest copyWithZone:];
-[AVAsynchronousCIImageFilteringRequest _willDeallocOrFinalize];
-[AVAsynchronousCIImageFilteringRequest compositionTime];
-[AVAsynchronousCIImageFilteringRequest finishWithImage:context:];
-[AVAsynchronousCIImageFilteringRequest initUsingCompositingRequest:sourceFrame:cancellationTest:defaultCIContextProvider:completionHandler:];
-[AVAsynchronousCIImageFilteringRequest sourceImage];
```
