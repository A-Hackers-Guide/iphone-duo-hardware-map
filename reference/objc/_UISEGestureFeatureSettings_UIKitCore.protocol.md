# `_UISEGestureFeatureSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 16 properties, 16 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) backProjectTime;
@property (Td,R,N) bottomEdgeAngleWindow;
@property (Td,R,N) bottomEdgeRegionSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (Td,R,N) cornerAngleWindow;
@property (Td,R,N) edgeAngleWindow;
@property (Td,R,N) edgeAngleWindowDecayTime;
@property (Td,R,N) edgeRegionSize;
@property (Td,R,N) hysteresis;
@property (TQ,R,N) interfaceBottomEdge;
@property (TQ,R,N) minimumNumberOfSubfeatures;
@property (Td,R,N) maximumBackProjectTimeFactor;
@property (Td,R,N) maximumSwipeDuration;
@property (TQ,R,N) targetEdges;
@property (TB,R,N) ignoreHIDEdgeFlags;
@property (TB,R,N) disableEdgeRegionEnforcement;
```

## Instance methods

```
-[_UISEGestureFeatureSettings maximumSwipeDuration];
-[_UISEGestureFeatureSettings hysteresis];
-[_UISEGestureFeatureSettings edgeAngleWindow];
-[_UISEGestureFeatureSettings bottomEdgeAngleWindow];
-[_UISEGestureFeatureSettings ignoreHIDEdgeFlags];
-[_UISEGestureFeatureSettings disableEdgeRegionEnforcement];
-[_UISEGestureFeatureSettings edgeRegionSize];
-[_UISEGestureFeatureSettings cornerAngleWindow];
-[_UISEGestureFeatureSettings edgeAngleWindowDecayTime];
-[_UISEGestureFeatureSettings maximumBackProjectTimeFactor];
-[_UISEGestureFeatureSettings minimumNumberOfSubfeatures];
-[_UISEGestureFeatureSettings backProjectTime];
-[_UISEGestureFeatureSettings bottomEdgeRegionSize];
-[_UISEGestureFeatureSettings bounds];
-[_UISEGestureFeatureSettings targetEdges];
-[_UISEGestureFeatureSettings interfaceBottomEdge];
```
