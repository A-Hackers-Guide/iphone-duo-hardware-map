# `_UIGlyphPathBoundsIntersectionViewData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIView" _clippingView;
@"NSArray" _overlappingSiblingViews;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _availableBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _glyphPathBounds;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_availableBounds) availableBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_glyphPathBounds) glyphPathBounds;
@property (T@"UIView",W,N,V_clippingView) clippingView;
@property (T@"NSArray",C,N,V_overlappingSiblingViews) overlappingSiblingViews;
```

## Instance methods

```
-[_UIGlyphPathBoundsIntersectionViewData debugDescription];
-[_UIGlyphPathBoundsIntersectionViewData init];
-[_UIGlyphPathBoundsIntersectionViewData clippingView];
-[_UIGlyphPathBoundsIntersectionViewData setClippingView:];
-[_UIGlyphPathBoundsIntersectionViewData availableBounds];
-[_UIGlyphPathBoundsIntersectionViewData glyphPathBounds];
-[_UIGlyphPathBoundsIntersectionViewData _frameDebugDescription:];
-[_UIGlyphPathBoundsIntersectionViewData overlappingSiblingViews];
-[_UIGlyphPathBoundsIntersectionViewData setAvailableBounds:];
-[_UIGlyphPathBoundsIntersectionViewData setGlyphPathBounds:];
-[_UIGlyphPathBoundsIntersectionViewData setOverlappingSiblingViews:];
```
