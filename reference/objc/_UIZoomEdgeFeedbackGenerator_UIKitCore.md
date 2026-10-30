# `_UIZoomEdgeFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIEdgeFeedbackGenerator`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
d _minimumZoomScale;
d _maximumZoomScale;
d _minimumTemporaryZoomScale;
d _maximumTemporaryZoomScale;
```

## Properties

```
@property (Td,N,V_minimumZoomScale) minimumZoomScale;
@property (Td,N,V_maximumZoomScale) maximumZoomScale;
@property (Td,N,V_minimumTemporaryZoomScale) minimumTemporaryZoomScale;
@property (Td,N,V_maximumTemporaryZoomScale) maximumTemporaryZoomScale;
```

## Instance methods

```
-[_UIZoomEdgeFeedbackGenerator maximumZoomScale];
-[_UIZoomEdgeFeedbackGenerator setMaximumZoomScale:];
-[_UIZoomEdgeFeedbackGenerator init];
-[_UIZoomEdgeFeedbackGenerator initWithView:];
-[_UIZoomEdgeFeedbackGenerator maximumTemporaryZoomScale];
-[_UIZoomEdgeFeedbackGenerator zoomScaleUpdated:atLocation:];
-[_UIZoomEdgeFeedbackGenerator setMaximumTemporaryZoomScale:];
-[_UIZoomEdgeFeedbackGenerator _updateMaximumValue];
-[_UIZoomEdgeFeedbackGenerator minimumZoomScale];
-[_UIZoomEdgeFeedbackGenerator setMinimumTemporaryZoomScale:];
-[_UIZoomEdgeFeedbackGenerator setMinimumZoomScale:];
-[_UIZoomEdgeFeedbackGenerator _zoomScaleUpdated:withVelocity:atLocation:];
-[_UIZoomEdgeFeedbackGenerator zoomScaleUpdated:];
-[_UIZoomEdgeFeedbackGenerator minimumTemporaryZoomScale];
```
