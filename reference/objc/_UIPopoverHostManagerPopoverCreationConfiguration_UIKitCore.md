# `_UIPopoverHostManagerPopoverCreationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _showsArrow;
@"UIViewController" _contentViewController;
@"UIView" _sourceView;
Q _permittedArrowDirections;
q _userInterfaceStyle;
@? _completionBlock;
@"UIPopoverPresentationController" _creatingPopoverPresentationController;
{CGSize="width"d"height"d} _contentSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRectInParentUIWindow;
```

## Properties

```
@property (T@"UIViewController",&,N,V_contentViewController) contentViewController;
@property (T@"UIView",&,N,V_sourceView) sourceView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRectInParentUIWindow) sourceRectInParentUIWindow;
@property (T{CGSize=dd},N,V_contentSize) contentSize;
@property (TQ,N,V_permittedArrowDirections) permittedArrowDirections;
@property (TB,N,V_showsArrow) showsArrow;
@property (Tq,N,V_userInterfaceStyle) userInterfaceStyle;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"UIPopoverPresentationController",W,N,V_creatingPopoverPresentationController) creatingPopoverPresentationController;
```

## Instance methods

```
-[_UIPopoverHostManagerPopoverCreationConfiguration setContentViewController:];
-[_UIPopoverHostManagerPopoverCreationConfiguration setCompletionBlock:];
-[_UIPopoverHostManagerPopoverCreationConfiguration completionBlock];
-[_UIPopoverHostManagerPopoverCreationConfiguration contentViewController];
-[_UIPopoverHostManagerPopoverCreationConfiguration contentSize];
-[_UIPopoverHostManagerPopoverCreationConfiguration userInterfaceStyle];
-[_UIPopoverHostManagerPopoverCreationConfiguration setUserInterfaceStyle:];
-[_UIPopoverHostManagerPopoverCreationConfiguration setSourceView:];
-[_UIPopoverHostManagerPopoverCreationConfiguration setContentSize:];
-[_UIPopoverHostManagerPopoverCreationConfiguration permittedArrowDirections];
-[_UIPopoverHostManagerPopoverCreationConfiguration sourceView];
-[_UIPopoverHostManagerPopoverCreationConfiguration creatingPopoverPresentationController];
-[_UIPopoverHostManagerPopoverCreationConfiguration setCreatingPopoverPresentationController:];
-[_UIPopoverHostManagerPopoverCreationConfiguration setPermittedArrowDirections:];
-[_UIPopoverHostManagerPopoverCreationConfiguration setShowsArrow:];
-[_UIPopoverHostManagerPopoverCreationConfiguration setSourceRectInParentUIWindow:];
-[_UIPopoverHostManagerPopoverCreationConfiguration showsArrow];
-[_UIPopoverHostManagerPopoverCreationConfiguration sourceRectInParentUIWindow];
```
