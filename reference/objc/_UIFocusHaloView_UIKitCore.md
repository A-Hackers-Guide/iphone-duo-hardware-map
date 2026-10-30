# `_UIFocusHaloView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 12 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _geometryFrozen;
@"_UIShape" _shape;
q _position;
d _thickness;
d _gapWidth;
@"_UIShapeView" _haloView;
@"_UIShapeView" _gapView;
@"_UIShapeView" _maskViewWhenInside;
@"UIColor" _gapColor;
@"UITraitCollection" _gapSourceTraitCollection;
```

## Properties

```
@property (T@"_UIShapeView",&,N,V_haloView) haloView;
@property (T@"_UIShapeView",&,N,V_gapView) gapView;
@property (T@"_UIShapeView",&,N,V_maskViewWhenInside) maskViewWhenInside;
@property (T@"UIColor",&,N,V_gapColor) gapColor;
@property (T@"UITraitCollection",&,N,V_gapSourceTraitCollection) gapSourceTraitCollection;
@property (T@"UIColor",R,N) haloColor;
@property (T@"_UIShape",C,N,V_shape) shape;
@property (Tq,N,V_position) position;
@property (Td,N,V_thickness) thickness;
@property (Td,N,V_gapWidth) gapWidth;
@property (TB,N,V_geometryFrozen) geometryFrozen;
@property (Td,R,N) totalConsumedSpace;
```

## Class methods

```
+[_UIFocusHaloView _supportsInvalidatingFocusCache];
```

## Instance methods

```
-[_UIFocusHaloView _isEligibleForFocusInteraction];
-[_UIFocusHaloView setShape:];
-[_UIFocusHaloView position];
-[_UIFocusHaloView gapSourceTraitCollection];
-[_UIFocusHaloView shape];
-[_UIFocusHaloView setHidden:];
-[_UIFocusHaloView focusItemsInRect:];
-[_UIFocusHaloView setCenter:];
-[_UIFocusHaloView totalConsumedSpace];
-[_UIFocusHaloView setBounds:];
-[_UIFocusHaloView setHaloView:];
-[_UIFocusHaloView maskViewWhenInside];
-[_UIFocusHaloView tintColorDidChange];
-[_UIFocusHaloView setGapWidth:];
-[_UIFocusHaloView _updateHalo];
-[_UIFocusHaloView haloView];
-[_UIFocusHaloView setGapView:];
-[_UIFocusHaloView _updateGapColor];
-[_UIFocusHaloView haloColor];
-[_UIFocusHaloView setGeometryFrozen:];
-[_UIFocusHaloView setFrame:];
-[_UIFocusHaloView gapColor];
-[_UIFocusHaloView description];
-[_UIFocusHaloView gapWidth];
-[_UIFocusHaloView thickness];
-[_UIFocusHaloView geometryFrozen];
-[_UIFocusHaloView setThickness:];
-[_UIFocusHaloView setPosition:];
-[_UIFocusHaloView _updateHaloForCurrentUserInterfaceStyle];
-[_UIFocusHaloView setMaskViewWhenInside:];
-[_UIFocusHaloView _ignoreRemoveAllAnimations];
-[_UIFocusHaloView setGapColor:];
-[_UIFocusHaloView didMoveToSuperview];
-[_UIFocusHaloView gapView];
-[_UIFocusHaloView initWithFrame:];
-[_UIFocusHaloView resolvedGapColor];
-[_UIFocusHaloView setGapSourceTraitCollection:];
```
