# `_UITextSelectionHighlightShimmerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextSelectionHighlightView`
- 4 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"_UITextSelectionRangeView" _rangeView;
@"UIVisualEffectView" _shimmerView;
@"NSArray" _selectionRects;
d _selectionCornerRadius;
```

## Properties

```
@property (Td,N,S_setSelectionCornerRadius:,V_selectionCornerRadius) _selectionCornerRadius;
@property (T@"NSArray",&,N,V_selectionRects) selectionRects;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextSelectionHighlightShimmerView layoutSubviews];
-[_UITextSelectionHighlightShimmerView _selectionCornerRadius];
-[_UITextSelectionHighlightShimmerView setSelectionRects:];
-[_UITextSelectionHighlightShimmerView selectionRects];
-[_UITextSelectionHighlightShimmerView _setSelectionCornerRadius:];
-[_UITextSelectionHighlightShimmerView initWithFrame:];
-[_UITextSelectionHighlightShimmerView initWithFrame:effect:];
```
