# `CAMViewfinderReticleView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 22 instance variables, 22 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _cornersVisible;
B _overCaptureGradientVisible;
B _viewportHairlinesVisible;
B __cornersAllowed;
d _viewportTopInset;
d _viewportBottomInset;
d _viewportLeftInset;
d _viewportRightInset;
q _material;
d _overCaptureGradientHeight;
@"UIView" __topMaskingView;
@"UIView" __bottomMaskingView;
@"UIView" __leftMaskingView;
@"UIView" __rightMaskingView;
@"UIImageView" __viewportBorderView;
@"UIImageView" __topLeftCornerView;
@"UIImageView" __topRightCornerView;
@"UIImageView" __bottomLeftCornerView;
@"UIImageView" __bottomRightCornerView;
@"CAMVerticalGradientView" __bottomOverCaptureGradientView;
@"UIView" __viewportTopHairlineView;
@"UIView" __viewportBottomHairlineView;
```

## Properties

```
@property (T@"UIView",R,N,V__topMaskingView) _topMaskingView;
@property (T@"UIView",R,N,V__bottomMaskingView) _bottomMaskingView;
@property (T@"UIView",R,N,V__leftMaskingView) _leftMaskingView;
@property (T@"UIView",R,N,V__rightMaskingView) _rightMaskingView;
@property (T@"UIImageView",R,N,V__viewportBorderView) _viewportBorderView;
@property (T@"UIImageView",R,N,V__topLeftCornerView) _topLeftCornerView;
@property (T@"UIImageView",R,N,V__topRightCornerView) _topRightCornerView;
@property (T@"UIImageView",R,N,V__bottomLeftCornerView) _bottomLeftCornerView;
@property (T@"UIImageView",R,N,V__bottomRightCornerView) _bottomRightCornerView;
@property (TB,R,N,V__cornersAllowed) _cornersAllowed;
@property (T@"CAMVerticalGradientView",&,N,V__bottomOverCaptureGradientView) _bottomOverCaptureGradientView;
@property (T@"UIView",&,N,V__viewportTopHairlineView) _viewportTopHairlineView;
@property (T@"UIView",&,N,V__viewportBottomHairlineView) _viewportBottomHairlineView;
@property (Td,R,N,V_viewportTopInset) viewportTopInset;
@property (Td,R,N,V_viewportBottomInset) viewportBottomInset;
@property (Td,R,N,V_viewportLeftInset) viewportLeftInset;
@property (Td,R,N,V_viewportRightInset) viewportRightInset;
@property (Tq,N,V_material) material;
@property (TB,N,V_cornersVisible) cornersVisible;
@property (TB,N,V_overCaptureGradientVisible) overCaptureGradientVisible;
@property (Td,N,V_overCaptureGradientHeight) overCaptureGradientHeight;
@property (TB,N,V_viewportHairlinesVisible) viewportHairlinesVisible;
```

## Instance methods

```
-[CAMViewfinderReticleView setOverCaptureGradientVisible:animated:];
-[CAMViewfinderReticleView setOverCaptureGradientHeight:];
-[CAMViewfinderReticleView setOverCaptureGradientVisible:];
-[CAMViewfinderReticleView setMaterial:withDuration:];
-[CAMViewfinderReticleView setViewportHairlinesVisible:animated:];
-[CAMViewfinderReticleView setCornersVisible:];
-[CAMViewfinderReticleView _topMaskingView];
-[CAMViewfinderReticleView set_viewportBottomHairlineView:];
-[CAMViewfinderReticleView _bottomRightCornerView];
-[CAMViewfinderReticleView _viewportBorderView];
-[CAMViewfinderReticleView _viewportBottomHairlineView];
-[CAMViewfinderReticleView _bottomOverCaptureGradientView];
-[CAMViewfinderReticleView viewportBottomInset];
-[CAMViewfinderReticleView layoutSubviews];
-[CAMViewfinderReticleView set_viewportTopHairlineView:];
-[CAMViewfinderReticleView viewportLeftInset];
-[CAMViewfinderReticleView overCaptureGradientVisible];
-[CAMViewfinderReticleView viewportHairlinesVisible];
-[CAMViewfinderReticleView _bottomLeftCornerView];
-[CAMViewfinderReticleView setCornersVisible:animated:];
-[CAMViewfinderReticleView _leftMaskingView];
-[CAMViewfinderReticleView _createBottomGradientViewIfNeeded];
-[CAMViewfinderReticleView setViewportHairlinesVisible:];
-[CAMViewfinderReticleView overCaptureGradientHeight];
-[CAMViewfinderReticleView _bottomMaskingView];
-[CAMViewfinderReticleView _newViewportCornerImage];
-[CAMViewfinderReticleView _updateMaterialOpacityWithDuration:];
-[CAMViewfinderReticleView _createHairlineViewsIfNeeded];
-[CAMViewfinderReticleView _topRightCornerView];
-[CAMViewfinderReticleView setViewportTopInset:bottomInset:leftInset:rightInset:animated:];
-[CAMViewfinderReticleView viewportRightInset];
-[CAMViewfinderReticleView cornersVisible];
-[CAMViewfinderReticleView _newViewportTemplateImage];
-[CAMViewfinderReticleView setMaterial:];
-[CAMViewfinderReticleView material];
-[CAMViewfinderReticleView _viewportTopHairlineView];
-[CAMViewfinderReticleView pointInside:withEvent:];
-[CAMViewfinderReticleView setOverCaptureGradientHeight:animated:];
-[CAMViewfinderReticleView _topLeftCornerView];
-[CAMViewfinderReticleView initWithFrame:];
-[CAMViewfinderReticleView _cornersAllowed];
-[CAMViewfinderReticleView _rightMaskingView];
-[CAMViewfinderReticleView set_bottomOverCaptureGradientView:];
-[CAMViewfinderReticleView viewportTopInset];
```
