# `_UISEGestureFeatureSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISEGestureFeatureSettings`
- 16 instance variables, 16 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _ignoreHIDEdgeFlags;
B _disableEdgeRegionEnforcement;
d _backProjectTime;
d _bottomEdgeAngleWindow;
d _bottomEdgeRegionSize;
d _cornerAngleWindow;
d _edgeAngleWindow;
d _edgeAngleWindowDecayTime;
d _edgeRegionSize;
d _hysteresis;
Q _interfaceBottomEdge;
Q _minimumNumberOfSubfeatures;
d _maximumBackProjectTimeFactor;
d _maximumSwipeDuration;
Q _targetEdges;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (Td,N,V_backProjectTime) backProjectTime;
@property (Td,N,V_bottomEdgeAngleWindow) bottomEdgeAngleWindow;
@property (Td,N,V_bottomEdgeRegionSize) bottomEdgeRegionSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
@property (Td,N,V_cornerAngleWindow) cornerAngleWindow;
@property (Td,N,V_edgeAngleWindow) edgeAngleWindow;
@property (Td,N,V_edgeAngleWindowDecayTime) edgeAngleWindowDecayTime;
@property (Td,N,V_edgeRegionSize) edgeRegionSize;
@property (Td,N,V_hysteresis) hysteresis;
@property (TQ,N,V_interfaceBottomEdge) interfaceBottomEdge;
@property (TQ,N,V_minimumNumberOfSubfeatures) minimumNumberOfSubfeatures;
@property (Td,N,V_maximumBackProjectTimeFactor) maximumBackProjectTimeFactor;
@property (Td,N,V_maximumSwipeDuration) maximumSwipeDuration;
@property (TQ,N,V_targetEdges) targetEdges;
@property (TB,N,V_ignoreHIDEdgeFlags) ignoreHIDEdgeFlags;
@property (TB,N,V_disableEdgeRegionEnforcement) disableEdgeRegionEnforcement;
```

## Instance methods

```
-[_UISEGestureFeatureSettings setHysteresis:];
-[_UISEGestureFeatureSettings maximumSwipeDuration];
-[_UISEGestureFeatureSettings setIgnoreHIDEdgeFlags:];
-[_UISEGestureFeatureSettings hysteresis];
-[_UISEGestureFeatureSettings setMaximumBackProjectTimeFactor:];
-[_UISEGestureFeatureSettings edgeAngleWindow];
-[_UISEGestureFeatureSettings bottomEdgeAngleWindow];
-[_UISEGestureFeatureSettings ignoreHIDEdgeFlags];
-[_UISEGestureFeatureSettings setBottomEdgeAngleWindow:];
-[_UISEGestureFeatureSettings init];
-[_UISEGestureFeatureSettings disableEdgeRegionEnforcement];
-[_UISEGestureFeatureSettings edgeRegionSize];
-[_UISEGestureFeatureSettings setCornerAngleWindow:];
-[_UISEGestureFeatureSettings setTargetEdges:];
-[_UISEGestureFeatureSettings cornerAngleWindow];
-[_UISEGestureFeatureSettings edgeAngleWindowDecayTime];
-[_UISEGestureFeatureSettings setBounds:];
-[_UISEGestureFeatureSettings maximumBackProjectTimeFactor];
-[_UISEGestureFeatureSettings minimumNumberOfSubfeatures];
-[_UISEGestureFeatureSettings backProjectTime];
-[_UISEGestureFeatureSettings setEdgeAngleWindow:];
-[_UISEGestureFeatureSettings setMaximumSwipeDuration:];
-[_UISEGestureFeatureSettings bottomEdgeRegionSize];
-[_UISEGestureFeatureSettings setEdgeRegionSize:];
-[_UISEGestureFeatureSettings bounds];
-[_UISEGestureFeatureSettings setInterfaceBottomEdge:];
-[_UISEGestureFeatureSettings setBackProjectTime:];
-[_UISEGestureFeatureSettings setMinimumNumberOfSubfeatures:];
-[_UISEGestureFeatureSettings targetEdges];
-[_UISEGestureFeatureSettings setBottomEdgeRegionSize:];
-[_UISEGestureFeatureSettings interfaceBottomEdge];
-[_UISEGestureFeatureSettings setDisableEdgeRegionEnforcement:];
-[_UISEGestureFeatureSettings setEdgeAngleWindowDecayTime:];
```
