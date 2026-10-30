# `UIDropShadowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIDropShadowViewContentViewInstrinsicContentSizeChange`
- 19 instance variables, 26 properties, 47 instance methods, 0 class methods

## Instance variables

```
B __hasGrabber;
B __insetsContentViewForGrabber;
B __grabberLumaTrackingEnabled;
B __grabberBlurEnabled;
B _masksTopCornersOnly;
B _supportsShadow;
@"UIView" _contentView;
@"UIView" _overlayView;
d __grabberAlpha;
d __grabberSpacing;
q __grabberEdge;
@"<UIDropShadowViewDelegate>" __delegate;
@"UIView" _clippingView;
@"_UIGrabber" __topGrabber;
@"_UIGrabber" __bottomGrabber;
@"_UIRoundedRectShadowView" _magicShadowView;
{CGSize="width"d"height"d} __grabberSize;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _environmentMatchingCornerRadii;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentTouchInsets;
```

## Properties

```
@property (TB,R,N,V_supportsShadow) supportsShadow;
@property (T@"UIView",R,W,N,V_clippingView) clippingView;
@property (T@"_UIGrabber",R,N,V__topGrabber) _topGrabber;
@property (T@"_UIGrabber",R,N,V__bottomGrabber) _bottomGrabber;
@property (TB,R,N) _effectiveInsetsContentViewForGrabber;
@property (TB,R,N) _hasCreatedGrabbers;
@property (T@"_UIRoundedRectShadowView",R,N,V_magicShadowView) magicShadowView;
@property (T{UIRectCornerRadii=dddd},N,V_environmentMatchingCornerRadii) environmentMatchingCornerRadii;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"UIView",&,N,V_overlayView) overlayView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _contentViewFrame;
@property (TB,N,S_setHasGrabber:,V__hasGrabber) _hasGrabber;
@property (Td,N,S_setGrabberAlpha:,V__grabberAlpha) _grabberAlpha;
@property (Td,N,S_setGrabberSpacing:,V__grabberSpacing) _grabberSpacing;
@property (Tq,N,S_setGrabberEdge:,V__grabberEdge) _grabberEdge;
@property (TB,N,S_setInsetsContentViewForGrabber:,V__insetsContentViewForGrabber) _insetsContentViewForGrabber;
@property (TB,N,G_isGrabberLumaTrackingEnabled,S_setGrabberLumaTrackingEnabled:,V__grabberLumaTrackingEnabled) _grabberLumaTrackingEnabled;
@property (TB,N,G_isGrabberBlurEnabled,S_setGrabberBlurEnabled:,V__grabberBlurEnabled) _grabberBlurEnabled;
@property (T{CGSize=dd},N,S_setGrabberSize:,V__grabberSize) _grabberSize;
@property (T{UIEdgeInsets=dddd},N,V_contentTouchInsets) contentTouchInsets;
@property (T@"<UIDropShadowViewDelegate>",W,N,V__delegate) _delegate;
@property (TB,N,V_masksTopCornersOnly) masksTopCornersOnly;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDropShadowView _contentViewFrame];
-[UIDropShadowView _hasGrabber];
-[UIDropShadowView magicShadowView];
-[UIDropShadowView setContentView:];
-[UIDropShadowView setMasksTopCornersOnly:];
-[UIDropShadowView _setGrabberSpacing:];
-[UIDropShadowView intrinsicContentSizeChangedForChildView:];
-[UIDropShadowView _setHasGrabber:];
-[UIDropShadowView contentTouchInsets];
-[UIDropShadowView masksTopCornersOnly];
-[UIDropShadowView _effectiveInsetsContentViewForGrabber];
-[UIDropShadowView _setGrabberEdge:];
-[UIDropShadowView layoutSubviews];
-[UIDropShadowView _setGrabberBlurEnabled:];
-[UIDropShadowView hitTest:withEvent:];
-[UIDropShadowView _isGrabberBlurEnabled];
-[UIDropShadowView _setGrabberAlpha:];
-[UIDropShadowView initWithFrame:supportsShadow:stylesSheetsAsCards:];
-[UIDropShadowView _isGrabber:];
-[UIDropShadowView overlayView];
-[UIDropShadowView _layoutGrabbers];
-[UIDropShadowView _grabberPrimaryAction];
-[UIDropShadowView _delegate];
-[UIDropShadowView didFinishRotation];
-[UIDropShadowView updateClippingView];
-[UIDropShadowView _grabberEdge];
-[UIDropShadowView willBeginRotationWithOriginalBounds:newBounds:];
-[UIDropShadowView environmentMatchingCornerRadii];
-[UIDropShadowView _topGrabber];
-[UIDropShadowView _hasCreatedGrabbers];
-[UIDropShadowView clippingView];
-[UIDropShadowView _setGrabberLumaTrackingEnabled:];
-[UIDropShadowView setMagicShadowAlpha:];
-[UIDropShadowView _grabberSpacing];
-[UIDropShadowView contentView];
-[UIDropShadowView set_delegate:];
-[UIDropShadowView _insetsContentViewForGrabber];
-[UIDropShadowView _grabberAlpha];
-[UIDropShadowView _setGrabberSize:];
-[UIDropShadowView _bottomGrabber];
-[UIDropShadowView setOverlayView:];
-[UIDropShadowView _grabberSize];
-[UIDropShadowView setContentTouchInsets:];
-[UIDropShadowView _setInsetsContentViewForGrabber:];
-[UIDropShadowView setEnvironmentMatchingCornerRadii:];
-[UIDropShadowView supportsShadow];
-[UIDropShadowView _isGrabberLumaTrackingEnabled];
```
