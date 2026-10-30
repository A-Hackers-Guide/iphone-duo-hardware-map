# `AVPlayerTaggedBufferOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVPlayerVideoOutput" _realOutput;
```

## Class methods

```
+[AVPlayerTaggedBufferOutput taggedBufferOutputWithVideoOutput:];
```

## Instance methods

```
-[AVPlayerTaggedBufferOutput init];
-[AVPlayerTaggedBufferOutput dealloc];
-[AVPlayerTaggedBufferOutput initWithSpecification:];
-[AVPlayerTaggedBufferOutput _attachToPlayer:];
-[AVPlayerTaggedBufferOutput _detachFromPlayer:];
-[AVPlayerTaggedBufferOutput _setResourceLifeCycleHandler:];
-[AVPlayerTaggedBufferOutput copyTaggedBufferGroupForHostTime:presentationTimeStamp:];
-[AVPlayerTaggedBufferOutput hasNewTaggedBufferGroupForHostTime:];
-[AVPlayerTaggedBufferOutput initWithVideoOutput:];
-[AVPlayerTaggedBufferOutput realOutput];
```
