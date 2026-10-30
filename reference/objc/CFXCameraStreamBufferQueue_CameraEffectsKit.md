# `CFXCameraStreamBufferQueue`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _accessQueue;
@"NSMutableArray" _outputBuffers;
Q _maxCapacity;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessQueue) accessQueue;
@property (T@"NSMutableArray",&,N,V_outputBuffers) outputBuffers;
@property (TQ,N,V_maxCapacity) maxCapacity;
```

## Instance methods

```
-[CFXCameraStreamBufferQueue accessQueue];
-[CFXCameraStreamBufferQueue count];
-[CFXCameraStreamBufferQueue initWithMaxCapacity:];
-[CFXCameraStreamBufferQueue setAccessQueue:];
-[CFXCameraStreamBufferQueue setMaxCapacity:];
-[CFXCameraStreamBufferQueue dequeue];
-[CFXCameraStreamBufferQueue maxCapacity];
-[CFXCameraStreamBufferQueue enqueue:];
-[CFXCameraStreamBufferQueue outputBuffers];
-[CFXCameraStreamBufferQueue headBufferTimestamp];
-[CFXCameraStreamBufferQueue setOutputBuffers:];
```
