# `_UITextSimpleLinkInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextLinkInteraction`
- 5 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UITapGestureRecognizer" _linkTap;
@"UILongPressGestureRecognizer" _highlighter;
@"_UITextInteractableItem" _highlightedItem;
{?="presentingFromSimpleTap"b1"didCheckViewProtocolConformance"b1"viewConformsToTextItemInteracting"b1"viewConformsToWillDisplayMenuWithAnimator"b1"viewConformsToWillDismissMenuWithAnimator"b1} _flags;
B _shouldProxyContextMenuDelegate;
```

## Properties

```
@property (TB,R,N,V_shouldProxyContextMenuDelegate) shouldProxyContextMenuDelegate;
```

## Instance methods

```
-[_UITextSimpleLinkInteraction _gestureRecognizerFailed:];
-[_UITextSimpleLinkInteraction gesturesForFailureRequirements];
-[_UITextSimpleLinkInteraction itemInteractableView];
-[_UITextSimpleLinkInteraction highlight:];
-[_UITextSimpleLinkInteraction _beginInteractionSessionForLinkAtPoint:asTap:precision:];
-[_UITextSimpleLinkInteraction _allowItemInteractions];
-[_UITextSimpleLinkInteraction editMenuInteraction];
-[_UITextSimpleLinkInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UITextSimpleLinkInteraction interaction_gestureRecognizer:shouldReceiveTouch:];
-[_UITextSimpleLinkInteraction linkTapped:];
-[_UITextSimpleLinkInteraction _canBeginInteractionSessionForLinkAtPoint:asTap:precision:];
-[_UITextSimpleLinkInteraction initWithShouldProxyContextMenuDelegate:];
-[_UITextSimpleLinkInteraction contextMenuDelegateProxy];
-[_UITextSimpleLinkInteraction shouldProxyContextMenuDelegate];
-[_UITextSimpleLinkInteraction didMoveToView:];
-[_UITextSimpleLinkInteraction _removeInteractableItemFromCache:];
-[_UITextSimpleLinkInteraction interaction_gestureRecognizerShouldBegin:];
```
