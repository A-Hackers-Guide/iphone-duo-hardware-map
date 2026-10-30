# `_UIBlendingHighlightView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIInterfaceActionVisualBackgroundDisplaying`, `UIInterfaceActionVisualGroupBackgroundDisplaying`
- 2 instance variables, 6 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _blendingViews;
d _cornerRadius;
```

## Properties

```
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T@"UIColor",?,&,N) fillColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBlendingHighlightView _blendingPressedView];
+[_UIBlendingHighlightView _blendingSeparatorView];
+[_UIBlendingHighlightView isBorderView];
```

## Instance methods

```
-[_UIBlendingHighlightView layoutSubviews];
-[_UIBlendingHighlightView setCornerRadius:];
-[_UIBlendingHighlightView setHighlighted:];
-[_UIBlendingHighlightView _setContinuousCornerRadius:];
-[_UIBlendingHighlightView cornerRadius];
-[_UIBlendingHighlightView setRoundedCornerPosition:];
-[_UIBlendingHighlightView setPressed:];
-[_UIBlendingHighlightView _effectiveNonDirectionalContentInsets];
-[_UIBlendingHighlightView _enumerateAllBlendingViewsWithBlock:];
-[_UIBlendingHighlightView _enumerateBlendingBorderViewsWithBlock:];
-[_UIBlendingHighlightView initWithCompositingBurnColor:plusDColor:];
-[_UIBlendingHighlightView initWithTopLevelFilters:compositingColors:compositingFilterModes:];
```
