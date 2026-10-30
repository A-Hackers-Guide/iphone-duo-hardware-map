# `UIPreviewParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 14 instance variables, 17 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _textLineRects;
B _hiddenDuringDrag;
B _appliesShadow;
B _hidesSourceViewDuringDropAnimation;
B _isUsingCustomBackgroundColor;
d _textPathCornerRadius;
@"UIColor" _overrideBackgroundColor;
@"_UIPreviewParametersCornerRadii" _overrideCornerRadii;
@"UIBezierPath" _visiblePath;
@"UIBezierPath" _shadowPath;
@"UIColor" _backgroundColor;
q _previewMode;
{?="width"d"height"d"depth"d} _placeholderContentSize3D;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _textPathInsets;
```

## Properties

```
@property (Tq,N,G_previewMode,S_setPreviewMode:,V_previewMode) previewMode;
@property (TB,N,V_appliesShadow) appliesShadow;
@property (TB,N,V_hidesSourceViewDuringDropAnimation) hidesSourceViewDuringDropAnimation;
@property (T@"UIBezierPath",R,N) effectiveShadowPath;
@property (TB,R,N,G_isSingleLineText) singleLineText;
@property (TB,R,N,V_isUsingCustomBackgroundColor) isUsingCustomBackgroundColor;
@property (T@"UIColor",C,N,S_setOverrideBackgroundColor:,V_overrideBackgroundColor) _overrideBackgroundColor;
@property (T@"UIColor",R,N) _effectiveBackgroundColor;
@property (T@"_UIPreviewParametersCornerRadii",&,N,V_overrideCornerRadii) _overrideCornerRadii;
@property (TB,N,G_isHiddenDuringDrag,S_setHiddenDuringDrag:,V_hiddenDuringDrag) _hiddenDuringDrag;
@property (T{?=ddd},N,S_setPlaceholderContentSize3D:,V_placeholderContentSize3D) _placeholderContentSize3D;
@property (T@"NSArray",&,N,G_textLineRects,S_setTextLineRects:,V_textLineRects) _textLineRects;
@property (T{UIEdgeInsets=dddd},N,G_textPathInsets,S_setTextPathInsets:,V_textPathInsets) _textPathInsets;
@property (Td,N,G_textPathCornerRadius,S_setTextPathCornerRadius:,V_textPathCornerRadius) _textPathCornerRadius;
@property (T@"UIBezierPath",C,N,V_visiblePath) visiblePath;
@property (T@"UIBezierPath",C,N,V_shadowPath) shadowPath;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
```

## Instance methods

```
-[UIPreviewParameters setShadowPath:];
-[UIPreviewParameters init];
-[UIPreviewParameters _setPreviewMode:];
-[UIPreviewParameters shadowPath];
-[UIPreviewParameters setBackgroundColor:];
-[UIPreviewParameters hash];
-[UIPreviewParameters backgroundColor];
-[UIPreviewParameters description];
-[UIPreviewParameters visiblePath];
-[UIPreviewParameters _previewMode];
-[UIPreviewParameters copyWithZone:];
-[UIPreviewParameters isEqual:];
-[UIPreviewParameters _textPathInsets];
-[UIPreviewParameters setVisiblePath:];
-[UIPreviewParameters _effectiveBackgroundColor];
-[UIPreviewParameters _initWithMode:visiblePath:backgroundColor:];
-[UIPreviewParameters _isHiddenDuringDrag];
-[UIPreviewParameters _isSingleLineText];
-[UIPreviewParameters _overrideBackgroundColor];
-[UIPreviewParameters _overrideCornerRadii];
-[UIPreviewParameters _placeholderContentSize3D];
-[UIPreviewParameters _setHiddenDuringDrag:];
-[UIPreviewParameters _setOverrideBackgroundColor:];
-[UIPreviewParameters _setPlaceholderContentSize3D:];
-[UIPreviewParameters _setTextLineRects:];
-[UIPreviewParameters _setTextPathCornerRadius:];
-[UIPreviewParameters _setTextPathInsets:];
-[UIPreviewParameters _textLineRects];
-[UIPreviewParameters _textPathCornerRadius];
-[UIPreviewParameters appliesShadow];
-[UIPreviewParameters effectiveShadowPath];
-[UIPreviewParameters hidesSourceViewDuringDropAnimation];
-[UIPreviewParameters initWithTextLineRects:];
-[UIPreviewParameters isUsingCustomBackgroundColor];
-[UIPreviewParameters setAppliesShadow:];
-[UIPreviewParameters setHidesSourceViewDuringDropAnimation:];
-[UIPreviewParameters set_overrideCornerRadii:];
```
