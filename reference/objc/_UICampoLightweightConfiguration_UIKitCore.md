# `_UICampoLightweightConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _leadingAligned;
q _presenterSource;
@"UIView" _sourceView;
q _initialState;
Q _permittedArrowDirections;
d _hoverPresentationDelay;
@"NSArray" _additionalPassthroughViews;
@"NSArray" _selectionRects;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _popoverAnchorRect;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _sourceRectOutset;
```

## Properties

```
@property (Tq,R,N,V_presenterSource) presenterSource;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_popoverAnchorRect) popoverAnchorRect;
@property (T@"UIView",R,N,V_sourceView) sourceView;
@property (Tq,R,N,V_initialState) initialState;
@property (TQ,N,V_permittedArrowDirections) permittedArrowDirections;
@property (TB,N,V_leadingAligned) leadingAligned;
@property (Td,N,V_hoverPresentationDelay) hoverPresentationDelay;
@property (T{UIEdgeInsets=dddd},N,V_sourceRectOutset) sourceRectOutset;
@property (T@"NSArray",C,N,V_additionalPassthroughViews) additionalPassthroughViews;
@property (T@"NSArray",C,N,V_selectionRects) selectionRects;
```

## Instance methods

```
-[_UICampoLightweightConfiguration setSourceRect:];
-[_UICampoLightweightConfiguration sourceRect];
-[_UICampoLightweightConfiguration leadingAligned];
-[_UICampoLightweightConfiguration setLeadingAligned:];
-[_UICampoLightweightConfiguration setSelectionRects:];
-[_UICampoLightweightConfiguration selectionRects];
-[_UICampoLightweightConfiguration description];
-[_UICampoLightweightConfiguration initialState];
-[_UICampoLightweightConfiguration permittedArrowDirections];
-[_UICampoLightweightConfiguration sourceView];
-[_UICampoLightweightConfiguration presenterSource];
-[_UICampoLightweightConfiguration additionalPassthroughViews];
-[_UICampoLightweightConfiguration hoverPresentationDelay];
-[_UICampoLightweightConfiguration initWithPresenterSource:sourceRect:sourceView:expanded:];
-[_UICampoLightweightConfiguration initWithPresenterSource:sourceRect:sourceView:initialState:];
-[_UICampoLightweightConfiguration initWithSourceRect:sourceView:];
-[_UICampoLightweightConfiguration initWithSourceRect:sourceView:expanded:];
-[_UICampoLightweightConfiguration initWithSourceRect:sourceView:initialState:];
-[_UICampoLightweightConfiguration popoverAnchorRect];
-[_UICampoLightweightConfiguration setAdditionalPassthroughViews:];
-[_UICampoLightweightConfiguration setHoverPresentationDelay:];
-[_UICampoLightweightConfiguration setPermittedArrowDirections:];
-[_UICampoLightweightConfiguration setPopoverAnchorRect:];
-[_UICampoLightweightConfiguration setSourceRectOutset:];
-[_UICampoLightweightConfiguration sourceRectOutset];
```
