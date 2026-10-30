# `CEKWheelScrubberViewCell`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 7 instance variables, 7 properties, 16 instance methods, 5 class methods

## Instance variables

```
d _contentInsetWidth;
@"UIView" _itemView;
d _selectionDotCenterTopSpacing;
q _dotPlacement;
@"UIView" _overlayView;
@"UIView" __selectionDotView;
@"UIView" __clippingView;
```

## Properties

```
@property (T@"UIView",R,N,V__selectionDotView) _selectionDotView;
@property (T@"UIView",R,N,V__clippingView) _clippingView;
@property (Td,N,V_contentInsetWidth) contentInsetWidth;
@property (T@"UIView",R,N,V_itemView) itemView;
@property (Td,N,V_selectionDotCenterTopSpacing) selectionDotCenterTopSpacing;
@property (Tq,N,V_dotPlacement) dotPlacement;
@property (T@"UIView",&,N,V_overlayView) overlayView;
```

## Class methods

```
+[CEKWheelScrubberViewCell defaultSize];
+[CEKWheelScrubberViewCell defaultContentSize];
+[CEKWheelScrubberViewCell defaultScreenScaleContentSize];
+[CEKWheelScrubberViewCell borderInsetWidth];
+[CEKWheelScrubberViewCell defaultContentInsetWidth];
```

## Instance methods

```
-[CEKWheelScrubberViewCell setSelected:];
-[CEKWheelScrubberViewCell layoutSubviews];
-[CEKWheelScrubberViewCell overlayView];
-[CEKWheelScrubberViewCell prepareForReuse];
-[CEKWheelScrubberViewCell setOverlayView:];
-[CEKWheelScrubberViewCell initWithFrame:];
-[CEKWheelScrubberViewCell itemView];
-[CEKWheelScrubberViewCell setDotPlacement:];
-[CEKWheelScrubberViewCell setSelectionDotCenterTopSpacing:];
-[CEKWheelScrubberViewCell _clippingView];
-[CEKWheelScrubberViewCell _selectionDotView];
-[CEKWheelScrubberViewCell _updateSelectionDot];
-[CEKWheelScrubberViewCell contentInsetWidth];
-[CEKWheelScrubberViewCell dotPlacement];
-[CEKWheelScrubberViewCell selectionDotCenterTopSpacing];
-[CEKWheelScrubberViewCell setContentInsetWidth:];
```
