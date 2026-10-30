# `_UITextSelectionHighlightView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextSelectionHighlightView`
- 6 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"_UITextSelectionRangeView" _rangeView;
B _hasClientHostedRects;
@"NSHashTable" _clientHostedLayers;
@"NSArray" _selectionRects;
d _selectionCornerRadius;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _selectionEdgeInsets;
```

## Properties

```
@property (T@"UIColor",&,D,N,S_setSelectionBorderColor:) _selectionBorderColor;
@property (Td,D,N,S_setSelectionBorderWidth:) _selectionBorderWidth;
@property (Td,N,S_setSelectionCornerRadius:,V_selectionCornerRadius) _selectionCornerRadius;
@property (T{UIEdgeInsets=dddd},N,S_setSelectionEdgeInsets:,V_selectionEdgeInsets) _selectionEdgeInsets;
@property (T@"NSArray",&,N,V_selectionRects) selectionRects;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextSelectionHighlightView setHidden:];
-[_UITextSelectionHighlightView layoutSubviews];
-[_UITextSelectionHighlightView _selectionCornerRadius];
-[_UITextSelectionHighlightView _selectionEdgeInsets];
-[_UITextSelectionHighlightView _setSelectionEdgeInsets:];
-[_UITextSelectionHighlightView _updateClientHostedLayerVisibility];
-[_UITextSelectionHighlightView tintColorDidChange];
-[_UITextSelectionHighlightView setAlpha:];
-[_UITextSelectionHighlightView setSelectionRects:];
-[_UITextSelectionHighlightView _layoutPathsPerClientLayer];
-[_UITextSelectionHighlightView selectionRects];
-[_UITextSelectionHighlightView _setSelectionBorderWidth:];
-[_UITextSelectionHighlightView _selectionBorderWidth];
-[_UITextSelectionHighlightView _setSelectionCornerRadius:];
-[_UITextSelectionHighlightView initWithFrame:];
-[_UITextSelectionHighlightView _setSelectionBorderColor:];
-[_UITextSelectionHighlightView _selectionBorderColor];
```
