# `_UICursorAccessoryHostView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITouchPassthroughView`
- 9 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _resolvedPlacement;
@"UITapGestureRecognizer" _dismissGestureRecognizer;
@"_UITouchFallbackView" _touchFallbackView;
B _collapsed;
B _touchFallbackEnabled;
Q _preferredPlacementEdge;
@"_UICursorAccessoryView" _cursorAccessoryView;
@"_UIContainerWindowPortalInteraction" _portalInteraction;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _selectionRect;
```

## Properties

```
@property (T@"_UIContainerWindowPortalInteraction",&,N,V_portalInteraction) portalInteraction;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_selectionRect) selectionRect;
@property (TQ,N,V_preferredPlacementEdge) preferredPlacementEdge;
@property (TB,N,GisCollapsed,V_collapsed) collapsed;
@property (T@"_UICursorAccessoryView",&,N,V_cursorAccessoryView) cursorAccessoryView;
@property (TB,N,V_touchFallbackEnabled) touchFallbackEnabled;
```

## Instance methods

```
-[_UICursorAccessoryHostView selectionRect];
-[_UICursorAccessoryHostView setCollapsed:];
-[_UICursorAccessoryHostView setHidden:];
-[_UICursorAccessoryHostView portalInteraction];
-[_UICursorAccessoryHostView _didRecognizeDismissGestureRecognizer:];
-[_UICursorAccessoryHostView dealloc];
-[_UICursorAccessoryHostView layoutSubviews];
-[_UICursorAccessoryHostView setTouchFallbackEnabled:];
-[_UICursorAccessoryHostView removeFromSuperview];
-[_UICursorAccessoryHostView isCollapsed];
-[_UICursorAccessoryHostView cursorAccessoryView];
-[_UICursorAccessoryHostView setSelectionRect:];
-[_UICursorAccessoryHostView setPreferredPlacementEdge:];
-[_UICursorAccessoryHostView preferredPlacementEdge];
-[_UICursorAccessoryHostView setCursorAccessoryView:];
-[_UICursorAccessoryHostView initWithCursorItemDataSource:];
-[_UICursorAccessoryHostView touchFallbackEnabled];
-[_UICursorAccessoryHostView setPortalInteraction:];
```
