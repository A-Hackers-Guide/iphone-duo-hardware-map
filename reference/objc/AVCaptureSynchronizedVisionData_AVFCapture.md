# `AVCaptureSynchronizedVisionData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureSynchronizedData`
- 1 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureSynchronizedVisionDataInternal" _internal;
```

## Properties

```
@property (T^{__CVBuffer=},R) visionDataPixelBuffer;
@property (TB,R) visionDataWasDropped;
@property (Tq,R) droppedReason;
```

## Instance methods

```
-[AVCaptureSynchronizedVisionData dealloc];
-[AVCaptureSynchronizedVisionData _initWithVisionDataPixelBuffer:timestamp:visionDataWasDropped:droppedReason:];
-[AVCaptureSynchronizedVisionData droppedReason];
-[AVCaptureSynchronizedVisionData visionDataPixelBuffer];
-[AVCaptureSynchronizedVisionData visionDataWasDropped];
```
