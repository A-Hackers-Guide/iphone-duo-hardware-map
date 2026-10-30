# `UITextContextMenuInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteraction`
- Protocols: `UIContextMenuInteractionDelegate_Private`, `UIContextMenuInteractionDelegate_ForWebKitOnly`, `_UIContextMenuInteractionDelegateInternal`, `_UIEditMenuInteractionDelegateInternal`
- 9 instance variables, 12 properties, 56 instance methods, 0 class methods

## Instance variables

```
{?="previewForHighlighting_DEPR"B"previewForDismissing_DEPR"B"highlightPreviewForItem"B"dismissalPreviewForItem"B"willPerformPreviewAction"B"willDisplay"B"willEndForConfiguration"B"styleForMenu"B"accessoriesForMenu"B"shouldBeDelayedByGestureRecognizer"B"asyncConfigurationForMenuAtLocation"B"overrideSuggestedActions"B"shouldAttemptToPresent"B"interactionEffectForTargetedPreview"B} _externalDelegateImplements;
@"UIEditMenuConfiguration" _currentInputUIConfiguration;
@"UIEditMenuConfiguration" _currentSelectionCommandsConfiguration;
B _isPresentingOrDismissingContextMenu;
B _keepsMenuPresentedActionInProgress;
@"<UIContextMenuInteractionDelegate>" _externalContextMenuDelegate;
@"UIContextMenuInteraction" _contextMenuInteraction;
@"UIEditMenuInteraction" _editMenuInteraction;
@"UIContextMenuConfiguration" _externallyManagedConfiguration;
```

## Properties

```
@property (T@"UIEditMenuInteraction",R,N,V_editMenuInteraction) editMenuInteraction;
@property (T@"UIContextMenuConfiguration",R,N,V_externallyManagedConfiguration) externallyManagedConfiguration;
@property (T@"<UIContextMenuInteractionDelegate>",W,N,V_externalContextMenuDelegate) externalContextMenuDelegate;
@property (T@"UIContextMenuInteraction",R,N,V_contextMenuInteraction) contextMenuInteraction;
@property (TB,R,N) dismissedRecently;
@property (TB,R,N) isDisplayingMenu;
@property (TB,R,N) isDisplayingHandoffMenu;
@property (TB,R,N) dismissedByActionSelection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextContextMenuInteraction contextMenuInteraction:configuration:dismissalPreviewForItemWithIdentifier:];
-[UITextContextMenuInteraction contextMenuInteraction:willEndForConfiguration:animator:];
-[UITextContextMenuInteraction _contextMenuInteraction:accessoriesForMenuWithConfiguration:];
-[UITextContextMenuInteraction dismissMenuForInputUI];
-[UITextContextMenuInteraction _isExternalConfiguration:];
-[UITextContextMenuInteraction _editMenuForSuggestedActions:rvItem:isEditMenu:];
-[UITextContextMenuInteraction _shouldBridgeMenuControllerItems];
-[UITextContextMenuInteraction contextMenuInteraction:configurationForMenuAtLocation:];
-[UITextContextMenuInteraction updateVisibleMenuPositionAnimated:];
-[UITextContextMenuInteraction updateVisibleMenuPosition];
-[UITextContextMenuInteraction editMenuInteraction:willPresentMenuForConfiguration:animator:];
-[UITextContextMenuInteraction init];
-[UITextContextMenuInteraction isDisplayingHandoffMenu];
-[UITextContextMenuInteraction editMenuInteraction:targetRectForConfiguration:];
-[UITextContextMenuInteraction _presentEditMenuForInputUI];
-[UITextContextMenuInteraction prepareForContextMenuAtLocationInView:completion:];
-[UITextContextMenuInteraction presentSelectionCommandsWithConfiguration:];
-[UITextContextMenuInteraction contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:];
-[UITextContextMenuInteraction _editMenuForCurrentSelectionWithSuggestedActions:isEditMenu:];
-[UITextContextMenuInteraction contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[UITextContextMenuInteraction _currentInputUIMenuElements];
-[UITextContextMenuInteraction _suggestedActionsForContextMenuInteraction:location:];
-[UITextContextMenuInteraction _logDeprecatedMenuControllerUsageIfNeeded];
-[UITextContextMenuInteraction dismissedRecently];
-[UITextContextMenuInteraction _editMenuInteraction:menuForConfiguration:suggestedActions:completionHandler:];
-[UITextContextMenuInteraction editMenuInteraction:willDismissMenuForConfiguration:animator:];
-[UITextContextMenuInteraction _editMenuInteraction:didPerformMenuLeaf:target:];
-[UITextContextMenuInteraction presentMenuForInputUI:preferredArrowDirection:];
-[UITextContextMenuInteraction editMenuInteraction];
-[UITextContextMenuInteraction isDisplayingMenuForInputUI];
-[UITextContextMenuInteraction contextMenuInteraction];
-[UITextContextMenuInteraction _contextMenuInteraction:configuration:interactionEffectForTargetedPreview:];
-[UITextContextMenuInteraction willMoveToView:];
-[UITextContextMenuInteraction externallyManagedConfiguration];
-[UITextContextMenuInteraction _contextMenuInteraction:shouldBeDelayedByGestureRecognizer:];
-[UITextContextMenuInteraction setExternalContextMenuDelegate:];
-[UITextContextMenuInteraction _targetedPreviewForCurrentSelection];
-[UITextContextMenuInteraction externalContextMenuDelegate];
-[UITextContextMenuInteraction contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:];
-[UITextContextMenuInteraction dismissSelectionCommandsWithReason:];
-[UITextContextMenuInteraction isDisplayingMenu];
-[UITextContextMenuInteraction _editMenuInteraction:preferredLayoutRectsForConfiguration:];
-[UITextContextMenuInteraction _didPerformMenuLeaf:target:];
-[UITextContextMenuInteraction _contextMenuInteraction:configurationForMenuAtLocation:completion:];
-[UITextContextMenuInteraction _contextMenuInteraction:shouldAttemptToPresentConfiguration:];
-[UITextContextMenuInteraction _editMenuInteraction:titleViewForMenu:configuration:];
-[UITextContextMenuInteraction _contextMenuInteraction:didPerformMenuLeaf:target:];
-[UITextContextMenuInteraction isDisplayingMenuForSelectionCommands];
-[UITextContextMenuInteraction editMenuInteraction:menuForConfiguration:suggestedActions:];
-[UITextContextMenuInteraction dismissedByActionSelection];
-[UITextContextMenuInteraction _contextMenuInteraction:styleForMenuWithConfiguration:];
-[UITextContextMenuInteraction didMoveToView:];
-[UITextContextMenuInteraction _textInputIsSecure];
-[UITextContextMenuInteraction _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[UITextContextMenuInteraction _querySelectionCommandsForConfiguration:suggestedActions:completionHandler:];
-[UITextContextMenuInteraction locationInTextInputViewForLocationInView:];
```
