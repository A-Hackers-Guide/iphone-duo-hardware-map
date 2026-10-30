# `UIScreenEdgePanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- Protocols: `_UISEGestureFeatureDelegate`, `_UIAssertionControllerSubject`
- 9 instance variables, 5 properties, 33 instance methods, 4 class methods

## Instance variables

```
@"_UISEGestureFeatureSettings" _settings;
@? _createFeatureBlock;
@"_UISEMuxGestureFeature" _rootFeature;
Q _touchedEdges;
B _recognizesWithoutEdge;
B _recognizesAtViewEdges;
@"<_UIInvalidatable>" _mustIgnoreHIDEdgeFlagsAssertion;
@"_UIAssertionController" _ignoreHIDEdgeFlagsAssertionController;
Q _edges;
```

## Properties

```
@property (TQ,N,V_edges) edges;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIScreenEdgePanGestureRecognizer supportsSecureCoding];
+[UIScreenEdgePanGestureRecognizer _supportsDefaultTouchTypes];
+[UIScreenEdgePanGestureRecognizer _supportsDefaultPressTypes];
+[UIScreenEdgePanGestureRecognizer _supportsStylusTouches];
```

## Instance methods

```
-[UIScreenEdgePanGestureRecognizer initWithTarget:action:type:options:];
-[UIScreenEdgePanGestureRecognizer _touchInterfaceOrientation];
-[UIScreenEdgePanGestureRecognizer touchesEnded:withEvent:];
-[UIScreenEdgePanGestureRecognizer assertionActivationStateForType:];
-[UIScreenEdgePanGestureRecognizer edges];
-[UIScreenEdgePanGestureRecognizer setEdges:];
-[UIScreenEdgePanGestureRecognizer dealloc];
-[UIScreenEdgePanGestureRecognizer featureDidChangeState:];
-[UIScreenEdgePanGestureRecognizer reset];
-[UIScreenEdgePanGestureRecognizer touchesBegan:withEvent:];
-[UIScreenEdgePanGestureRecognizer touchesMoved:withEvent:];
-[UIScreenEdgePanGestureRecognizer touchedEdges];
-[UIScreenEdgePanGestureRecognizer initWithTarget:action:];
-[UIScreenEdgePanGestureRecognizer _shouldTryToBeginWithEvent:];
-[UIScreenEdgePanGestureRecognizer encodeWithCoder:];
-[UIScreenEdgePanGestureRecognizer setMinimumNumberOfTouches:];
-[UIScreenEdgePanGestureRecognizer assertionActivationStateChangedToState:forType:];
-[UIScreenEdgePanGestureRecognizer initWithCoder:];
-[UIScreenEdgePanGestureRecognizer debugDictionary];
-[UIScreenEdgePanGestureRecognizer _resetHystersis];
-[UIScreenEdgePanGestureRecognizer _edgeRegionSize];
-[UIScreenEdgePanGestureRecognizer _setHysteresis:];
-[UIScreenEdgePanGestureRecognizer _beginRequiringIgnoresHIDEdgeFlagsForReason:];
-[UIScreenEdgePanGestureRecognizer _bottomEdgeAngleWindow];
-[UIScreenEdgePanGestureRecognizer _bottomEdgeRegionSize];
-[UIScreenEdgePanGestureRecognizer _recognizesAtViewEdges];
-[UIScreenEdgePanGestureRecognizer _recognizesWithoutEdge];
-[UIScreenEdgePanGestureRecognizer _rootFeatureState];
-[UIScreenEdgePanGestureRecognizer _setBottomEdgeAngleWindow:];
-[UIScreenEdgePanGestureRecognizer _setBottomEdgeRegionSize:];
-[UIScreenEdgePanGestureRecognizer _setEdgeRegionSize:];
-[UIScreenEdgePanGestureRecognizer _setRecognizesAtViewEdges:];
-[UIScreenEdgePanGestureRecognizer _setRecognizesWithoutEdge:];
```
