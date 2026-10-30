# `AVCaptureSynchronizedDepthData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureSynchronizedData`
- 1 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureSynchronizedDepthDataInternal" _internal;
```

## Properties

```
@property (T@"AVDepthData",R) depthData;
@property (TB,R) depthDataWasDropped;
@property (Tq,R) droppedReason;
```

## Class methods

```
+[AVCaptureSynchronizedDepthData initialize];
```

## Instance methods

```
-[AVCaptureSynchronizedDepthData debugDescription];
-[AVCaptureSynchronizedDepthData dealloc];
-[AVCaptureSynchronizedDepthData description];
-[AVCaptureSynchronizedDepthData depthData];
-[AVCaptureSynchronizedDepthData _initWithDepthData:timestamp:depthDataWasDropped:droppedReason:];
-[AVCaptureSynchronizedDepthData depthDataWasDropped];
-[AVCaptureSynchronizedDepthData droppedReason];
```
