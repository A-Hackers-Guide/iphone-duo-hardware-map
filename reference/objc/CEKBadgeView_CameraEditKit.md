# `CEKBadgeView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _tappable;
@"<CEKBadgeViewDelegate>" _delegate;
@"<CEKBadgeViewTapDelegate>" _tapDelegate;
d __fillCornerRadius;
@"UIColor" __fillColor;
@"UIColor" __contentColor;
@"UITapGestureRecognizer" __tapGestureRecognizer;
```

## Properties

```
@property (Td,N,S_setFillCornerRadius:,V__fillCornerRadius) _fillCornerRadius;
@property (T@"UIColor",&,N,S_setFillColor:,V__fillColor) _fillColor;
@property (T@"UIColor",&,N,S_setContentColor:,V__contentColor) _contentColor;
@property (T@"UITapGestureRecognizer",&,N,V__tapGestureRecognizer) _tapGestureRecognizer;
@property (T@"<CEKBadgeViewDelegate>",W,N,V_delegate) delegate;
@property (T@"<CEKBadgeViewTapDelegate>",W,N,V_tapDelegate) tapDelegate;
@property (TB,N,GisTappable,V_tappable) tappable;
```

## Instance methods

```
-[CEKBadgeView _contentColor];
-[CEKBadgeView _handleTap:];
-[CEKBadgeView drawRect:];
-[CEKBadgeView sizeThatFits:];
-[CEKBadgeView setDelegate:];
-[CEKBadgeView _tapGestureRecognizer];
-[CEKBadgeView delegate];
-[CEKBadgeView isTappable];
-[CEKBadgeView initWithFrame:];
-[CEKBadgeView _fillColor];
-[CEKBadgeView _maskImage];
-[CEKBadgeView _setContentColor:];
-[CEKBadgeView _setFillColor:];
-[CEKBadgeView setTappable:];
-[CEKBadgeView setTapDelegate:];
-[CEKBadgeView _fillCornerRadius];
-[CEKBadgeView _invertMaskImage:];
-[CEKBadgeView _setFillCornerRadius:];
-[CEKBadgeView set_tapGestureRecognizer:];
-[CEKBadgeView tapDelegate];
```
