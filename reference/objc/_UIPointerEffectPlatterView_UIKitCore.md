# `_UIPointerEffectPlatterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 18 instance variables, 18 properties, 51 instance methods, 0 class methods

## Instance variables

```
B _tintDisabled;
B _useSoftShadow;
B _geometryFrozen;
B _pressed;
@"UITargetedPreview" _targetedPreview;
d _shadowAlpha;
q _tintMode;
d _tintViewScale;
@"UIPointerShape" _tintViewShape;
@"UIView" _specularHighlight;
Q _specularOptions;
@? _tintColorMatrixProvider;
@"UIView" _contentView;
@"UIView" _shadowView;
@"_UIPointerEffectTintView" _tintView;
@"_UILumaTrackingBackdropView" _lumaTrackingView;
@"UIView" _specularOverlayView;
@"NSMutableArray" _accessoryPortals;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"UIView",&,N,V_shadowView) shadowView;
@property (T@"_UIPointerEffectTintView",&,N,V_tintView) tintView;
@property (T@"_UILumaTrackingBackdropView",&,N,V_lumaTrackingView) lumaTrackingView;
@property (T@"UIView",&,N,V_specularOverlayView) specularOverlayView;
@property (T@"NSMutableArray",&,N,V_accessoryPortals) accessoryPortals;
@property (T@"UITargetedPreview",C,N,V_targetedPreview) targetedPreview;
@property (Td,N,V_shadowAlpha) shadowAlpha;
@property (TB,N,GisTintDisabled,V_tintDisabled) tintDisabled;
@property (Tq,N,V_tintMode) tintMode;
@property (Td,N,V_tintViewScale) tintViewScale;
@property (T@"UIPointerShape",&,N,V_tintViewShape) tintViewShape;
@property (T@"UIView",&,N,V_specularHighlight) specularHighlight;
@property (TQ,N,V_specularOptions) specularOptions;
@property (TB,N,V_useSoftShadow) useSoftShadow;
@property (TB,N,V_geometryFrozen) geometryFrozen;
@property (TB,N,GisPressed,V_pressed) pressed;
@property (T@?,C,N,V_tintColorMatrixProvider) tintColorMatrixProvider;
```

## Instance methods

```
-[_UIPointerEffectPlatterView setShadowAlpha:];
-[_UIPointerEffectPlatterView shadowAlpha];
-[_UIPointerEffectPlatterView setContentView:];
-[_UIPointerEffectPlatterView setHidden:];
-[_UIPointerEffectPlatterView setCenter:];
-[_UIPointerEffectPlatterView layoutSubviews];
-[_UIPointerEffectPlatterView setBounds:];
-[_UIPointerEffectPlatterView shadowView];
-[_UIPointerEffectPlatterView isPressed];
-[_UIPointerEffectPlatterView initWithTargetedPreview:];
-[_UIPointerEffectPlatterView contentView];
-[_UIPointerEffectPlatterView setGeometryFrozen:];
-[_UIPointerEffectPlatterView setFrame:];
-[_UIPointerEffectPlatterView _isEligibleForFocusOcclusion];
-[_UIPointerEffectPlatterView setShadowView:];
-[_UIPointerEffectPlatterView geometryFrozen];
-[_UIPointerEffectPlatterView tintView];
-[_UIPointerEffectPlatterView _ignoreRemoveAllAnimations];
-[_UIPointerEffectPlatterView setPressed:];
-[_UIPointerEffectPlatterView setTintView:];
-[_UIPointerEffectPlatterView specularOptions];
-[_UIPointerEffectPlatterView _layoutTintView];
-[_UIPointerEffectPlatterView targetedPreview];
-[_UIPointerEffectPlatterView _installAccessoryView:];
-[_UIPointerEffectPlatterView _newLumaTrackingViewForTintView:];
-[_UIPointerEffectPlatterView _newShadowView];
-[_UIPointerEffectPlatterView _newTintView];
-[_UIPointerEffectPlatterView _specularOverlayView:withOptions:];
-[_UIPointerEffectPlatterView _updateContentMask];
-[_UIPointerEffectPlatterView accessoryPortals];
-[_UIPointerEffectPlatterView isTintDisabled];
-[_UIPointerEffectPlatterView lumaTrackingView];
-[_UIPointerEffectPlatterView setAccessoryPortals:];
-[_UIPointerEffectPlatterView setLumaTrackingView:];
-[_UIPointerEffectPlatterView setSpecularHighlight:];
-[_UIPointerEffectPlatterView setSpecularOptions:];
-[_UIPointerEffectPlatterView setSpecularOverlayView:];
-[_UIPointerEffectPlatterView setTargetedPreview:];
-[_UIPointerEffectPlatterView setTintColorMatrixProvider:];
-[_UIPointerEffectPlatterView setTintDisabled:];
-[_UIPointerEffectPlatterView setTintMode:];
-[_UIPointerEffectPlatterView setTintViewScale:];
-[_UIPointerEffectPlatterView setTintViewShape:];
-[_UIPointerEffectPlatterView setUseSoftShadow:];
-[_UIPointerEffectPlatterView specularHighlight];
-[_UIPointerEffectPlatterView specularOverlayView];
-[_UIPointerEffectPlatterView tintColorMatrixProvider];
-[_UIPointerEffectPlatterView tintMode];
-[_UIPointerEffectPlatterView tintViewScale];
-[_UIPointerEffectPlatterView tintViewShape];
-[_UIPointerEffectPlatterView useSoftShadow];
```
