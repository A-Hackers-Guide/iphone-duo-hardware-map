# `UIEventSessionHeatMapAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 10 instance methods, 5 class methods

## Instance variables

```
@"NSMutableDictionary" _gesturesByTouchID;
@"UIEventSessionHeatMapGesture" _currentGesture;
@"NSMutableArray" _pendingGestures;
```

## Class methods

```
+[UIEventSessionHeatMapAnalyzer determineGridCoordinateWithLocationInWindow:withWindowFrame:withTouchType:];
+[UIEventSessionHeatMapAnalyzer distanceBetweenPoint:andPoint:];
+[UIEventSessionHeatMapAnalyzer stringForHardwareAttachedType:];
+[UIEventSessionHeatMapAnalyzer stringForTouchPhase:];
+[UIEventSessionHeatMapAnalyzer stringForTouchType:];
```

## Instance methods

```
-[UIEventSessionHeatMapAnalyzer init];
-[UIEventSessionHeatMapAnalyzer checkIfGestureComplete:];
-[UIEventSessionHeatMapAnalyzer completeGesture:];
-[UIEventSessionHeatMapAnalyzer didTouchWithID:withPhase:withType:withLocationInWindow:withWindowFrame:withUIInterfaceOrientation:withHardwareKeyboardState:withMagicKeyboardState:];
-[UIEventSessionHeatMapAnalyzer sendAnalyticsEventWithName:payload:];
-[UIEventSessionHeatMapAnalyzer sendDirectTouchCoordinateReportForTouch:atCoordinate:withGesture:];
-[UIEventSessionHeatMapAnalyzer sendDirectTouchFingerReportsForGesture:];
-[UIEventSessionHeatMapAnalyzer sendDirectTouchGestureReportForGesture:];
-[UIEventSessionHeatMapAnalyzer sendPencilCoordinateReportForTouch:atCoordinate:withGesture:];
-[UIEventSessionHeatMapAnalyzer sendPencilGestureReportForGesture:];
```
