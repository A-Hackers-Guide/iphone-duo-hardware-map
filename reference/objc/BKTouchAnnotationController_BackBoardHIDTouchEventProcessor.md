# `BKTouchAnnotationController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKTouchLifecycleObserver`
- 7 instance variables, 9 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _visualizedHitTestRegions;
B _shouldVisualizeTouches;
B _shouldVisualizeHitTestRegions;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"<BKOrientationProvider>" _orientationProvider;
@"BKDisplayAnnotationController" _displayAnnotationController;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"BKDisplayAnnotationController",&,N,V_displayAnnotationController) displayAnnotationController;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (TB) shouldVisualizeTouches;
@property (TB) shouldVisualizeHitTestRegions;
@property (T@"<BKDisplayRenderSpace>",R,V_displayRenderSpace) displayRenderSpace;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKTouchAnnotationController workQueue];
```

## Instance methods

```
-[BKTouchAnnotationController setWorkQueue:];
-[BKTouchAnnotationController touch:pathIndex:downAtPoint:eventMask:transducerType:];
-[BKTouchAnnotationController touch:didAlwaysRouteToTargetID:clientTaskName:];
-[BKTouchAnnotationController touchDidFinishProcessingTouchCollection];
-[BKTouchAnnotationController touch:didMoveToPoint:eventMask:z:maxZ:];
-[BKTouchAnnotationController touch:didHitTestToDestination:hostingChainIndex:];
-[BKTouchAnnotationController hitTestRegionsDidChange:];
-[BKTouchAnnotationController workQueue];
-[BKTouchAnnotationController touchWillStartProcessingTouchCollection];
-[BKTouchAnnotationController touchDidHIDCancel:];
-[BKTouchAnnotationController touchDidSoftCancel:];
-[BKTouchAnnotationController touch:pathIndex:rangeInAtPoint:eventMask:z:maxZ:transducerType:];
-[BKTouchAnnotationController touch:pathIndex:upAtPoint:detached:];
-[BKTouchAnnotationController touch:pathIndex:rangeOutAtPoint:];
-[BKTouchAnnotationController touchDidDetach:destinations:];
-[BKTouchAnnotationController touchDidTransfer:destination:];
-[BKTouchAnnotationController _pidForClientTaskName:];
-[BKTouchAnnotationController displayRenderSpace];
-[BKTouchAnnotationController setDisplayAnnotationController:];
-[BKTouchAnnotationController annotateTouch:withUniqueString:];
-[BKTouchAnnotationController _keyPathForTouchIdentifier:];
-[BKTouchAnnotationController _queue_annotateTouch:withString:uniqueIdentifier:fromPID:];
-[BKTouchAnnotationController _queue_annotateTouch:withUniqueString:];
-[BKTouchAnnotationController _queue_applyBasicAnnotationTextForTouchIdentifier:pathIndex:];
-[BKTouchAnnotationController _queue_removeAnnotationForTouch:withUniqueIdentifier:];
-[BKTouchAnnotationController _queue_setCenter:forTouchIdentifier:];
-[BKTouchAnnotationController _queue_touchWasHardCanceled:];
-[BKTouchAnnotationController _queue_touchWasSoftCanceled:];
-[BKTouchAnnotationController _queue_updateHoverStateForTouchIdentifier:z:maxZ:];
-[BKTouchAnnotationController _stringByRemovingPrefix:fromString:];
-[BKTouchAnnotationController _stringDescribingPID:];
-[BKTouchAnnotationController _stringDescribingTargetID:clientTaskName:];
-[BKTouchAnnotationController annotateTouch:withString:uniqueIdentifier:];
-[BKTouchAnnotationController annotateTouch:withString:uniqueIdentifier:fromPID:];
-[BKTouchAnnotationController displayAnnotationController];
-[BKTouchAnnotationController hitTestRegionsDidChangeSwift:displayAnnotationController:];
-[BKTouchAnnotationController initWithDisplayUUID:displayRenderSpace:orientationProvider:];
-[BKTouchAnnotationController setShouldVisualizeHitTestRegions:];
-[BKTouchAnnotationController setShouldVisualizeTouches:];
-[BKTouchAnnotationController shouldVisualizeHitTestRegions];
-[BKTouchAnnotationController shouldVisualizeTouches];
```
