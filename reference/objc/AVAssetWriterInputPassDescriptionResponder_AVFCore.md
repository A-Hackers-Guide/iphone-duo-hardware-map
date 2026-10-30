# `AVAssetWriterInputPassDescriptionResponder`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _callbackQueue;
i _stoppedResponding;
@"NSObject<OS_dispatch_queue>" _serializationQueue;
B _hasRespondedAtLeastOnce;
@"AVAssetWriterInputPassDescription" _mostRecentPassDescription;
@? _callbackBlock;
```

## Instance methods

```
-[AVAssetWriterInputPassDescriptionResponder init];
-[AVAssetWriterInputPassDescriptionResponder dealloc];
-[AVAssetWriterInputPassDescriptionResponder _hasStoppedResponding];
-[AVAssetWriterInputPassDescriptionResponder _releaseAndClearCallbackBlock_invokeOnSerializationQueue];
-[AVAssetWriterInputPassDescriptionResponder initWithCallbackQueue:block:];
-[AVAssetWriterInputPassDescriptionResponder respondToNewPassDescription:];
-[AVAssetWriterInputPassDescriptionResponder stopRespondingToPassDescriptions];
```
