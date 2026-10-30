# `BKTouchLifecycleObserver` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance methods

```
-[BKTouchLifecycleObserver touch:pathIndex:downAtPoint:eventMask:transducerType:];
-[BKTouchLifecycleObserver touch:didAlwaysRouteToTargetID:clientTaskName:];
-[BKTouchLifecycleObserver touchDidFinishProcessingTouchCollection];
-[BKTouchLifecycleObserver touch:didMoveToPoint:eventMask:z:maxZ:];
-[BKTouchLifecycleObserver touch:didHitTestToDestination:hostingChainIndex:];
-[BKTouchLifecycleObserver hitTestRegionsDidChange:];
-[BKTouchLifecycleObserver touchWillStartProcessingTouchCollection];
-[BKTouchLifecycleObserver touchDidHIDCancel:];
-[BKTouchLifecycleObserver touchDidSoftCancel:];
-[BKTouchLifecycleObserver touch:pathIndex:rangeInAtPoint:eventMask:z:maxZ:transducerType:];
-[BKTouchLifecycleObserver touch:pathIndex:upAtPoint:detached:];
-[BKTouchLifecycleObserver touch:pathIndex:rangeOutAtPoint:];
-[BKTouchLifecycleObserver touchDidDetach:destinations:];
-[BKTouchLifecycleObserver touchDidTransfer:destination:];
```
