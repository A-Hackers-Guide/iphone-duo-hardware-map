# `AVSampleBufferGenerator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"AVSampleBufferGeneratorInternal" _generator;
```

## Class methods

```
+[AVSampleBufferGenerator initialize];
+[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:];
```

## Instance methods

```
-[AVSampleBufferGenerator init];
-[AVSampleBufferGenerator dealloc];
-[AVSampleBufferGenerator copyWithZone:];
-[AVSampleBufferGenerator _figSampleGenerator];
-[AVSampleBufferGenerator createSampleBufferForRequest:];
-[AVSampleBufferGenerator createSampleBufferForRequest:addingToBatch:error:];
-[AVSampleBufferGenerator createSampleBufferForRequest:error:];
-[AVSampleBufferGenerator initWithAsset:timebase:];
-[AVSampleBufferGenerator makeBatch];
```
