# `_UIContextMenuPreviewPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- 5 instance variables, 4 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _platterContentSizeDidChange;
@"UIView" _viewForRemoteTextEffectsWindowMatchAnimation;
@"<_UIContextMenuPreviewPresentationControllerDelegate>" _menuPresentationDelegate;
@"_UIContextMenuStyle" _menuStyle;
{CGSize="width"d"height"d} _platterContentSize;
```

## Properties

```
@property (T{CGSize=dd},N,V_platterContentSize) platterContentSize;
@property (TB,N,V_platterContentSizeDidChange) platterContentSizeDidChange;
@property (T@"<_UIContextMenuPreviewPresentationControllerDelegate>",W,N,V_menuPresentationDelegate) menuPresentationDelegate;
@property (T@"_UIContextMenuStyle",&,N,V_menuStyle) menuStyle;
```

## Instance methods

```
-[_UIContextMenuPreviewPresentationController _traitCollectionForChildEnvironment:];
-[_UIContextMenuPreviewPresentationController setPlatterContentSize:];
-[_UIContextMenuPreviewPresentationController menuDidPresentWithContentPlatterView:];
-[_UIContextMenuPreviewPresentationController _verticalBarAllowedForPresentation];
-[_UIContextMenuPreviewPresentationController preferredContentSizeDidChangeForChildContentContainer:];
-[_UIContextMenuPreviewPresentationController setMenuPresentationDelegate:];
-[_UIContextMenuPreviewPresentationController _baseContentInsetsWithLeftMargin:rightMargin:];
-[_UIContextMenuPreviewPresentationController presentationStyle];
-[_UIContextMenuPreviewPresentationController setMenuStyle:];
-[_UIContextMenuPreviewPresentationController _shouldKeepCurrentFirstResponder];
-[_UIContextMenuPreviewPresentationController _shouldPreserveFirstResponder];
-[_UIContextMenuPreviewPresentationController _shouldRestoreFirstResponder];
-[_UIContextMenuPreviewPresentationController _shouldOccludeDuringPresentation];
-[_UIContextMenuPreviewPresentationController _updatePlatterContentSizeWithPreferredContentSize:];
-[_UIContextMenuPreviewPresentationController _wantsAutomaticFirstResponderWhenPresentingRemoteViewController];
-[_UIContextMenuPreviewPresentationController frameOfPresentedViewInContainerView];
-[_UIContextMenuPreviewPresentationController platterContentSize];
-[_UIContextMenuPreviewPresentationController menuPresentationDelegate];
-[_UIContextMenuPreviewPresentationController preferredFocusEnvironments];
-[_UIContextMenuPreviewPresentationController systemLayoutFittingSizeDidChangeForChildContentContainer:];
-[_UIContextMenuPreviewPresentationController _shouldDisableInteractionDuringTransitions];
-[_UIContextMenuPreviewPresentationController platterContentSizeDidChange];
-[_UIContextMenuPreviewPresentationController setPlatterContentSizeDidChange:];
-[_UIContextMenuPreviewPresentationController _viewForRemoteTextEffectsWindowMatchAnimation];
-[_UIContextMenuPreviewPresentationController dismissalTransitionWillBegin];
-[_UIContextMenuPreviewPresentationController menuStyle];
-[_UIContextMenuPreviewPresentationController menuLayoutDidProducePreviewSize:];
-[_UIContextMenuPreviewPresentationController presentationTransitionWillBegin];
```
