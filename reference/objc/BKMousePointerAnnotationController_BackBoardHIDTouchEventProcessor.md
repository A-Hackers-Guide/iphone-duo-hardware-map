# `BKMousePointerAnnotationController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKMousePointerLifecycleObserver`, `BSInvalidatable`
- 7 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
d _startTime;
q _inputEventsPerSecond;
q _outputEventsPerSecond;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"<BKOrientationProvider>" _orientationProvider;
@"CADisplay" _currentDisplay;
@"BKDisplayAnnotationController" _currentAnnotationController;
```

## Properties

```
@property (T@"CADisplay",&,N,V_currentDisplay) currentDisplay;
@property (T@"BKDisplayAnnotationController",&,N,V_currentAnnotationController) currentAnnotationController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKMousePointerAnnotationController dealloc];
-[BKMousePointerAnnotationController invalidate];
-[BKMousePointerAnnotationController currentDisplay];
-[BKMousePointerAnnotationController _stringDescribingContextID:pid:];
-[BKMousePointerAnnotationController setCurrentAnnotationController:];
-[BKMousePointerAnnotationController _updateEventsPerSecond];
-[BKMousePointerAnnotationController currentAnnotationController];
-[BKMousePointerAnnotationController didPostEvent];
-[BKMousePointerAnnotationController didReceiveEventFromDevice];
-[BKMousePointerAnnotationController initWithDisplayRenderSpace:orientationProvider:];
-[BKMousePointerAnnotationController observeMouseAbsolutePointDidChange:];
-[BKMousePointerAnnotationController observeMouseAvailabilityDidChange:];
-[BKMousePointerAnnotationController observeMouseButtonMaskDidChange:];
-[BKMousePointerAnnotationController observeMouseDidEnterContextID:pid:];
-[BKMousePointerAnnotationController observeMouseDidExitContextID:pid:];
-[BKMousePointerAnnotationController observeMouseForceDidChange:stage:];
-[BKMousePointerAnnotationController observeMouseModelPointDidChange:display:reason:];
-[BKMousePointerAnnotationController observeMouseRelativePointDidChange:];
-[BKMousePointerAnnotationController observeMouseScrollPhaseDidChange:];
-[BKMousePointerAnnotationController observeMouseTouchCountDidChange:];
-[BKMousePointerAnnotationController setCurrentDisplay:];
```
