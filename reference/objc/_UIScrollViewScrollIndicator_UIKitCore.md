# `_UIScrollViewScrollIndicator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`, `_UIScrollViewScrollIndicator`
- 8 instance variables, 13 properties, 27 instance methods, 4 class methods

## Instance variables

```
@"<_UIScrollViewScrollIndicatorVisualStyle>" _visualStyle;
B _hasPointer;
B _expandedForDirectManipulation;
q _style;
Q _type;
@"UIColor" _foregroundColor;
@"UIView" _roundedFillView;
@"UIColor" _effectiveForegroundColor;
```

## Properties

```
@property (T@"UIView",&,N,V_roundedFillView) roundedFillView;
@property (T@"UIColor",&,N,V_effectiveForegroundColor) effectiveForegroundColor;
@property (T@"<_UIScrollViewScrollIndicatorVisualStyle>",R,N,G_visualStyle) _visualStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_type) type;
@property (Tq,N,V_style) style;
@property (T@"UIColor",&,N,V_foregroundColor) foregroundColor;
@property (TB,N,V_expandedForDirectManipulation) expandedForDirectManipulation;
@property (T{CGSize=dd},R,N) layoutOffset;
@property (TB,N,V_hasPointer) hasPointer;
```

## Class methods

```
+[_UIScrollViewScrollIndicator _ensureDefaultStyles];
+[_UIScrollViewScrollIndicator visualStyleForTraitCollection:];
+[_UIScrollViewScrollIndicator registerVisualStyle:forIdiom:];
+[_UIScrollViewScrollIndicator visualStyleForIdiom:];
```

## Instance methods

```
-[_UIScrollViewScrollIndicator setForegroundColor:];
-[_UIScrollViewScrollIndicator didMoveToWindow];
-[_UIScrollViewScrollIndicator pointerInteraction:styleForRegion:];
-[_UIScrollViewScrollIndicator effectiveForegroundColor];
-[_UIScrollViewScrollIndicator pointerInteraction:willEnterRegion:animator:];
-[_UIScrollViewScrollIndicator _layoutFillViewAnimated:];
-[_UIScrollViewScrollIndicator pointerInteraction:willExitRegion:animator:];
-[_UIScrollViewScrollIndicator layoutSubviews];
-[_UIScrollViewScrollIndicator hitTest:withEvent:];
-[_UIScrollViewScrollIndicator style];
-[_UIScrollViewScrollIndicator _visualStyle];
-[_UIScrollViewScrollIndicator setHasPointer:];
-[_UIScrollViewScrollIndicator setStyle:];
-[_UIScrollViewScrollIndicator setRoundedFillView:];
-[_UIScrollViewScrollIndicator setType:];
-[_UIScrollViewScrollIndicator setExpandedForDirectManipulation:];
-[_UIScrollViewScrollIndicator type];
-[_UIScrollViewScrollIndicator roundedFillView];
-[_UIScrollViewScrollIndicator hasPointer];
-[_UIScrollViewScrollIndicator pointerInteraction:regionForRequest:defaultRegion:];
-[_UIScrollViewScrollIndicator _offsetFillViewRectForExpandedState:];
-[_UIScrollViewScrollIndicator setEffectiveForegroundColor:];
-[_UIScrollViewScrollIndicator foregroundColor];
-[_UIScrollViewScrollIndicator initWithFrame:];
-[_UIScrollViewScrollIndicator expandedForDirectManipulation];
-[_UIScrollViewScrollIndicator layoutOffset];
-[_UIScrollViewScrollIndicator _updateEffectiveColor];
```
