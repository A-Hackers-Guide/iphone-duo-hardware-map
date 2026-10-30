# `_UITextMenuLinkInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextSimpleLinkInteraction`
- Protocols: `UIContextMenuInteractionDelegate`, `UIEditMenuInteractionDelegate`
- 3 instance variables, 4 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _configurationItems;
@"UIEditMenuInteraction" _editMenuInteraction;
B _isModifyingSelectionForLinkPresentation;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextMenuLinkInteraction contextMenuInteraction:willEndForConfiguration:animator:];
-[_UITextMenuLinkInteraction _willEndMenuDisplayForItem:animator:];
-[_UITextMenuLinkInteraction contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[_UITextMenuLinkInteraction contextMenuInteraction:configurationForMenuAtLocation:];
-[_UITextMenuLinkInteraction editMenuInteraction:willPresentMenuForConfiguration:animator:];
-[_UITextMenuLinkInteraction _willDisplayMenuForItem:animator:];
-[_UITextMenuLinkInteraction editMenuInteraction:targetRectForConfiguration:];
-[_UITextMenuLinkInteraction contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[_UITextMenuLinkInteraction contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[_UITextMenuLinkInteraction editMenuInteraction:willDismissMenuForConfiguration:animator:];
-[_UITextMenuLinkInteraction editMenuInteraction];
-[_UITextMenuLinkInteraction _contextMenuInteraction:configuration:interactionEffectForTargetedPreview:];
-[_UITextMenuLinkInteraction _targetedPreviewForItem:dismissing:];
-[_UITextMenuLinkInteraction willMoveToView:];
-[_UITextMenuLinkInteraction contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:];
-[_UITextMenuLinkInteraction initWithShouldProxyContextMenuDelegate:];
-[_UITextMenuLinkInteraction contextMenuDelegateProxy];
-[_UITextMenuLinkInteraction _contextMenuInteraction:shouldAttemptToPresentConfiguration:];
-[_UITextMenuLinkInteraction editMenuInteraction:menuForConfiguration:suggestedActions:];
-[_UITextMenuLinkInteraction _contextMenuInteraction:styleForMenuWithConfiguration:];
-[_UITextMenuLinkInteraction didMoveToView:];
-[_UITextMenuLinkInteraction _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[_UITextMenuLinkInteraction dismissEditMenuOnSelectionChangeIfNecessary];
```
