# `_UIScreenEdgePanRecognizerEdgeSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISettings`
- 6 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
d _hysteresis;
d _edgeRegionSize;
d _bottomEdgeRegionSize;
d _edgeAngleWindow;
d _edgeAngleWindowDecayTime;
d _maximumSwipeDuration;
```

## Properties

```
@property (Td,N,V_hysteresis) hysteresis;
@property (Td,N,V_edgeRegionSize) edgeRegionSize;
@property (Td,N,V_bottomEdgeRegionSize) bottomEdgeRegionSize;
@property (Td,N,V_edgeAngleWindow) edgeAngleWindow;
@property (Td,N) edgeAngleWindowDegreees;
@property (Td,N,V_edgeAngleWindowDecayTime) edgeAngleWindowDecayTime;
@property (Td,N,V_maximumSwipeDuration) maximumSwipeDuration;
```

## Class methods

```
+[_UIScreenEdgePanRecognizerEdgeSettings settingsControllerModule];
+[_UIScreenEdgePanRecognizerEdgeSettings keyPathsForValuesAffectingEdgeAngleWindowDegreees];
```

## Instance methods

```
-[_UIScreenEdgePanRecognizerEdgeSettings setHysteresis:];
-[_UIScreenEdgePanRecognizerEdgeSettings maximumSwipeDuration];
-[_UIScreenEdgePanRecognizerEdgeSettings hysteresis];
-[_UIScreenEdgePanRecognizerEdgeSettings edgeAngleWindow];
-[_UIScreenEdgePanRecognizerEdgeSettings edgeRegionSize];
-[_UIScreenEdgePanRecognizerEdgeSettings edgeAngleWindowDecayTime];
-[_UIScreenEdgePanRecognizerEdgeSettings setDefaultValues];
-[_UIScreenEdgePanRecognizerEdgeSettings setEdgeAngleWindow:];
-[_UIScreenEdgePanRecognizerEdgeSettings setMaximumSwipeDuration:];
-[_UIScreenEdgePanRecognizerEdgeSettings bottomEdgeRegionSize];
-[_UIScreenEdgePanRecognizerEdgeSettings setEdgeRegionSize:];
-[_UIScreenEdgePanRecognizerEdgeSettings setBottomEdgeRegionSize:];
-[_UIScreenEdgePanRecognizerEdgeSettings setEdgeAngleWindowDecayTime:];
-[_UIScreenEdgePanRecognizerEdgeSettings edgeAngleWindowDegreees];
-[_UIScreenEdgePanRecognizerEdgeSettings setEdgeAngleWindowDegreees:];
```
