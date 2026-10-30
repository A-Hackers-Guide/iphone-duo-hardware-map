# `UIStoryboardPopoverSegue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStoryboardSegue`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIPopoverController" _popoverController;
@"NSArray" _passthroughViews;
Q _permittedArrowDirections;
@"UIView" _anchorView;
@"UIBarButtonItem" _anchorBarButtonItem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _anchorRect;
```

## Properties

```
@property (T@"NSArray",C,N,S_setPassthroughViews:,V_passthroughViews) _passthroughViews;
@property (TQ,N,S_setPermittedArrowDirections:,V_permittedArrowDirections) _permittedArrowDirections;
@property (T@"UIBarButtonItem",&,N,S_setAnchorBarButtonItem:,V_anchorBarButtonItem) _anchorBarButtonItem;
@property (T@"UIView",&,N,S_setAnchorView:,V_anchorView) _anchorView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setAnchorRect:,V_anchorRect) _anchorRect;
@property (T@"UIPopoverController",R,N,V_popoverController) popoverController;
```

## Instance methods

```
-[UIStoryboardPopoverSegue _setPassthroughViews:];
-[UIStoryboardPopoverSegue _passthroughViews];
-[UIStoryboardPopoverSegue perform];
-[UIStoryboardPopoverSegue _setAnchorRect:];
-[UIStoryboardPopoverSegue _setAnchorView:];
-[UIStoryboardPopoverSegue _anchorBarButtonItem];
-[UIStoryboardPopoverSegue _anchorRect];
-[UIStoryboardPopoverSegue _anchorView];
-[UIStoryboardPopoverSegue _permittedArrowDirections];
-[UIStoryboardPopoverSegue _setAnchorBarButtonItem:];
-[UIStoryboardPopoverSegue _setPermittedArrowDirections:];
-[UIStoryboardPopoverSegue popoverController];
```
