# `UIEditMenuInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDeferredMenuElementDelegate`, `_UIEditMenuPresentationDelegate`, `UIInteraction_Internal`, `_UIVisualStyleStylable`, `UIInteraction`
- 20 instance variables, 24 properties, 74 instance methods, 2 class methods

## Instance variables

```
{?="menuForSuggestedActions"b1"targetRectForConfiguration"b1"willPresentAnimator"b1"willDismissAnimator"b1"asyncMenuForSuggestedActions"b1"didTransition"b1"titleView"b1"firstResponderTarget"b1"didPerformMenuLeaf"b1"preferredLayoutRects"b1} _delegateImplements;
d _lastDismissalTime;
B _dismissedByMenuAction;
B __includeMenuControllerItems;
B __isTextEditMenuInteraction;
B _displayingMenu;
B __useSenderAsResponderSender;
B __enforcesMenuControllerLifecycle;
B _presentsContextMenuAsSecondaryAction;
@"UIView" _view;
@"UIContextMenuInteraction" _contextMenuInteraction;
@ __proxySender;
@"_UIEditMenuHandoffContext" _activeHandoffContext;
@"<UIEditMenuInteractionDelegate>" _delegate;
@"UIEditMenuConfiguration" _pendingConfiguration;
@"UIEditMenuConfiguration" _activeConfiguration;
@"_UIEditMenuPresentation" _activeEditMenuPresentation;
@"_UIEditMenuPresentation" __outgoingPresentation;
@"_UIEditMenuPresentation" _activeHandoffPresentation;
@"<UIMenuLeaf>" __selectedMenuLeaf;
```

## Properties

```
@property (T@"UIEditMenuConfiguration",&,N,V_pendingConfiguration) pendingConfiguration;
@property (T@"UIEditMenuConfiguration",&,N,V_activeConfiguration) activeConfiguration;
@property (T@"_UIEditMenuPresentation",R,N,V_activeEditMenuPresentation) activeEditMenuPresentation;
@property (T@"_UIEditMenuPresentation",R,N,V__outgoingPresentation) _outgoingPresentation;
@property (T@"_UIEditMenuHandoffContext",R,N,V_activeHandoffContext) _activeHandoffContext;
@property (T@"_UIEditMenuPresentation",R,N,V_activeHandoffPresentation) activeHandoffPresentation;
@property (TB,N,V__includeMenuControllerItems) _includeMenuControllerItems;
@property (TB,R,N) _dismissedRecently;
@property (TB,R,N) _dismissedByActionSelection;
@property (TB,N,GisDisplayingMenu,V_displayingMenu) displayingMenu;
@property (TB,R,N) _isDisplayingHandoffMenu;
@property (T@"<UIMenuLeaf>",W,N,V__selectedMenuLeaf) _selectedMenuLeaf;
@property (T@"UIContextMenuInteraction",R,N,V_contextMenuInteraction) contextMenuInteraction;
@property (T@,W,N,S_setProxySender:,V__proxySender) _proxySender;
@property (TB,N,S_setUseSenderAsResponderSender:,V__useSenderAsResponderSender) _useSenderAsResponderSender;
@property (TB,N,S_setEnforcesMenuControllerLifecycle:,V__enforcesMenuControllerLifecycle) _enforcesMenuControllerLifecycle;
@property (TB,N,V_presentsContextMenuAsSecondaryAction) presentsContextMenuAsSecondaryAction;
@property (T@"<UIEditMenuInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[UIEditMenuInteraction visualStyleRegistryIdentity];
+[UIEditMenuInteraction _isOutOfProcessEditMenusEnabled];
```

## Instance methods

```
-[UIEditMenuInteraction dismissMenu];
-[UIEditMenuInteraction contextMenuInteraction:willEndForConfiguration:animator:];
-[UIEditMenuInteraction _selectedMenuLeaf];
-[UIEditMenuInteraction activeConfiguration];
-[UIEditMenuInteraction _editMenuPresentation:willPresentMenuForConfiguration:animator:];
-[UIEditMenuInteraction contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[UIEditMenuInteraction initWithDelegate:];
-[UIEditMenuInteraction activeHandoffPresentation];
-[UIEditMenuInteraction _editMenuPresentation:didFailPresentMenuForConfiguration:];
-[UIEditMenuInteraction activeEditMenuPresentation];
-[UIEditMenuInteraction _intelligentAssistantTextSelectionContext];
-[UIEditMenuInteraction _prepareMenuAtLocation:configuration:completionHandler:];
-[UIEditMenuInteraction presentEditMenuWithConfiguration:];
-[UIEditMenuInteraction contextMenuInteraction:configurationForMenuAtLocation:];
-[UIEditMenuInteraction set_includeMenuControllerItems:];
-[UIEditMenuInteraction updateVisibleMenuPositionAnimated:];
-[UIEditMenuInteraction _menuPreparationContextForConfiguration:];
-[UIEditMenuInteraction _enforcesMenuControllerLifecycle];
-[UIEditMenuInteraction _defaultSuggestedActionsMenuAtLocation:configuration:];
-[UIEditMenuInteraction _proxySender];
-[UIEditMenuInteraction _editMenuPresentation:didTransitionMenuForConfiguration:];
-[UIEditMenuInteraction deferredMenuElementWasFulfilled:];
-[UIEditMenuInteraction contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[UIEditMenuInteraction menuFrameInCoordinateSpace:];
-[UIEditMenuInteraction _willPresentMenuForConfiguration:animator:];
-[UIEditMenuInteraction presentsContextMenuAsSecondaryAction];
-[UIEditMenuInteraction _editMenuPresentation:handoffDisplayedMenuWithContext:];
-[UIEditMenuInteraction contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[UIEditMenuInteraction _didMoveFromWindow:toWindow:];
-[UIEditMenuInteraction presenterConfigurationForIntelligentAssistantInEditMenuPresentation:];
-[UIEditMenuInteraction _isDisplayingHandoffMenu];
-[UIEditMenuInteraction _anchorForPreferredArrowDirection:];
-[UIEditMenuInteraction _setUseSenderAsResponderSender:];
-[UIEditMenuInteraction locationInView:];
-[UIEditMenuInteraction pendingConfiguration];
-[UIEditMenuInteraction _editMenuPresentation:preparedMenuForDisplay:completion:];
-[UIEditMenuInteraction _dismissedRecently];
-[UIEditMenuInteraction view];
-[UIEditMenuInteraction _setProxySender:];
-[UIEditMenuInteraction setActiveConfiguration:];
-[UIEditMenuInteraction reloadVisibleMenu];
-[UIEditMenuInteraction _outgoingPresentation];
-[UIEditMenuInteraction set_selectedMenuLeaf:];
-[UIEditMenuInteraction _editMenuPresentation:preferredLayoutRectsForConfiguration:];
-[UIEditMenuInteraction _targetRectForConfiguration:];
-[UIEditMenuInteraction contextMenuInteraction];
-[UIEditMenuInteraction setPendingConfiguration:];
-[UIEditMenuInteraction _includeMenuControllerItems];
-[UIEditMenuInteraction _editMenuPresentation:titleViewForMenu:configuration:];
-[UIEditMenuInteraction willMoveToView:];
-[UIEditMenuInteraction _editMenuPresentation:willDismissMenuForConfiguration:animator:];
-[UIEditMenuInteraction _useSenderAsResponderSender];
-[UIEditMenuInteraction delegate];
-[UIEditMenuInteraction setDisplayingMenu:];
-[UIEditMenuInteraction _activeHandoffContext];
-[UIEditMenuInteraction _setEnforcesMenuControllerLifecycle:];
-[UIEditMenuInteraction _updateContextMenuInteractionDrivers];
-[UIEditMenuInteraction _dismissedByActionSelection];
-[UIEditMenuInteraction isDisplayingMenu];
-[UIEditMenuInteraction firstResponderTargetForConfiguration:];
-[UIEditMenuInteraction _editMenuPresentation:targetRectForConfiguration:];
-[UIEditMenuInteraction _contextMenuInteraction:configurationForMenuAtLocation:completion:];
-[UIEditMenuInteraction _dismissMenuWithPresentationType:];
-[UIEditMenuInteraction _contextMenuInteraction:didPerformMenuLeaf:target:];
-[UIEditMenuInteraction _viewTraitCollectionDidChange:];
-[UIEditMenuInteraction _menuForSuggestedActions:configuration:];
-[UIEditMenuInteraction presenterConfigurationForIntelligentAssistantInEditMenuPresentation:completionHandler:];
-[UIEditMenuInteraction _contextMenuInteraction:styleForMenuWithConfiguration:];
-[UIEditMenuInteraction didMoveToView:];
-[UIEditMenuInteraction _willDismissMenuForConfiguration:animator:];
-[UIEditMenuInteraction _editMenuPresentation:didSelectMenuLeaf:completion:];
-[UIEditMenuInteraction _updateVisibleMenuWithReason:updateBlock:];
-[UIEditMenuInteraction _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[UIEditMenuInteraction setPresentsContextMenuAsSecondaryAction:];
```
