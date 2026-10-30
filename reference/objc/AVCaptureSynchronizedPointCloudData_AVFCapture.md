# `AVCaptureSynchronizedPointCloudData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureSynchronizedData`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"AVPointCloudData" _pointCloudData;
B _pointCloudDataWasDropped;
q _droppedReason;
```

## Properties

```
@property (T@"AVPointCloudData",R) pointCloudData;
@property (TB,R) pointCloudDataWasDropped;
@property (Tq,R) droppedReason;
```

## Instance methods

```
-[AVCaptureSynchronizedPointCloudData dealloc];
-[AVCaptureSynchronizedPointCloudData _initWithPointCloudDataBuffer:timestamp:pointCloudDataWasDropped:droppedReason:];
-[AVCaptureSynchronizedPointCloudData droppedReason];
-[AVCaptureSynchronizedPointCloudData pointCloudData];
-[AVCaptureSynchronizedPointCloudData pointCloudDataWasDropped];
```
