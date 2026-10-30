# `CAMBuffer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 12 properties, 39 instance methods, 2 class methods

## Instance variables

```
B _bufferQueueEnabled;
@"NSObject<OS_dispatch_queue>" __bufferQueue;
@"<NSCopying>" _bufferQueueCurrentValue;
@"NSMutableArray" __bufferQueueBufferedValues;
@"NSMutableDictionary" __bufferQueueObservers;
@"NSMutableArray" __bufferQueueObservances;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__bufferQueue) _bufferQueue;
@property (TB,N,GisBufferQueueEnabled,V_bufferQueueEnabled) bufferQueueEnabled;
@property (T@"<NSCopying>",&,N,V_bufferQueueCurrentValue) bufferQueueCurrentValue;
@property (T@"NSMutableArray",R,N,V__bufferQueueBufferedValues) _bufferQueueBufferedValues;
@property (T@"NSMutableDictionary",R,N,V__bufferQueueObservers) _bufferQueueObservers;
@property (T@"NSMutableArray",R,N,V__bufferQueueObservances) _bufferQueueObservances;
@property (TB,R,N,GisEnabled) enabled;
@property (T@,R,N) currentValue;
@property (TB,R,N) isBufferEmpty;
@property (T@,R,N) firstBufferedValue;
@property (T@,R,N) lastBufferedValue;
@property (T@"NSArray",R,N) bufferedValues;
```

## Class methods

```
+[CAMBuffer keyPathsForValuesAffectingCurrentValue];
+[CAMBuffer keyPathsForValuesAffectingEnabled];
```

## Instance methods

```
-[CAMBuffer push:];
-[CAMBuffer observeValueForKeyPath:ofObject:change:context:];
-[CAMBuffer init];
-[CAMBuffer dealloc];
-[CAMBuffer currentValue];
-[CAMBuffer isEnabled];
-[CAMBuffer addObserver:];
-[CAMBuffer reevaluate];
-[CAMBuffer removeObserverForKey:];
-[CAMBuffer _bufferQueueEvaluateObservances];
-[CAMBuffer _bufferQueueTeardownObservance:];
-[CAMBuffer _addObserver:onMainQueue:];
-[CAMBuffer _bufferQueue];
-[CAMBuffer _bufferQueueBufferedValues];
-[CAMBuffer _bufferQueueFulfillAndEvaluateWithChange:];
-[CAMBuffer _bufferQueueFulfillObservancesWithChange:];
-[CAMBuffer _bufferQueueObservances];
-[CAMBuffer _bufferQueueObservers];
-[CAMBuffer _bufferQueueSetupObservance:];
-[CAMBuffer _bufferQueueTeardownObservances:];
-[CAMBuffer _emitBufferedValues];
-[CAMBuffer _isBufferQueue];
-[CAMBuffer addMainQueueObserver:];
-[CAMBuffer bufferQueueCurrentValue];
-[CAMBuffer bufferedValues];
-[CAMBuffer disableUntil:];
-[CAMBuffer disableUntilKeyPath:ofObject:evaluates:];
-[CAMBuffer disableUntilNotification:fromObject:usingNotificationCenter:];
-[CAMBuffer disableWhile:];
-[CAMBuffer disableWhileKeyPath:ofObject:evaluates:];
-[CAMBuffer disableWhileNotification:fromObject:usingNotificationCenter:];
-[CAMBuffer firstBufferedValue];
-[CAMBuffer handleObservedNotification:];
-[CAMBuffer isBufferEmpty];
-[CAMBuffer isBufferQueueEnabled];
-[CAMBuffer lastBufferedValue];
-[CAMBuffer replaceWith:];
-[CAMBuffer setBufferQueueCurrentValue:];
-[CAMBuffer setBufferQueueEnabled:];
```
