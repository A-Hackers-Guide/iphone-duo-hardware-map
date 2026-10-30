# `UIContextMenuInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuPresentationDelegate`, `UIDeferredMenuElementDelegate`, `_UIVisualStyleStylable`, `_UIClickPresentationInteractionDelegateInternal`, `_UIWindowSceneActivator_Internal`, `UIInteraction`
- 15 instance variables, 29 properties, 101 instance methods, 2 class methods

## Instance variables

```
{?="highlightPreviewForItemWithIdentifier"B"dismissalPreviewForItemWithIdentifier"B"willPerformPreviewAction"B"willDisplay"B"willEndForConfiguration"B"styleForMenu"B"accessoriesForMenu"B"shouldByDelayedByGestureRecognizer"B"asyncConfigurationForMenuAtLocation"B"overrideSuggestedActions"B"shouldPresent"B"shouldAllowDragAfterDismiss"B"shouldAllowSwipeToDismiss"B"shouldDeferCommitAnimation"B"interactionEffectForTargetedPreview"B"shouldAttemptToPresentConfiguration"B"didPerformMenuLeaf"B"previewForHighlighting"B"previewForDismissing"B"_dci_secondaryHighlightPreview"B"_dci_secondaryDismissalPreview"B"willCommit"B} _delegateImplements;
B __requiresTouchAuthentication;
B __useSenderAsResponderSender;
B __ignorePreviewForDismissingDelegate;
@"UIView" _view;
@"_UIClickPresentationInteraction" _presentationInteraction;
@"<UIContextMenuInteractionDelegate>" _delegate;
@"UIContextMenuConfiguration" _pendingConfiguration;
@"NSMutableDictionary" _configurationsByIdentifier;
@"NSMutableDictionary" _presentationsByIdentifier;
@"_UIContextMenuPresentation" _outgoingPresentation;
@"_UIContextMenuAnimator" _pendingCommitAnimator;
@ __proxySender;
@"<UIMenuLeaf>" __selectedMenuLeaf;
{CGPoint="x"d"y"d} _pendingMenuSourceLocation;
```

## Properties

```
@property (T@"UIContextMenuConfiguration",&,N,V_pendingConfiguration) pendingConfiguration;
@property (T@"NSMutableDictionary",&,N,V_configurationsByIdentifier) configurationsByIdentifier;
@property (T@"NSMutableDictionary",&,N,V_presentationsByIdentifier) presentationsByIdentifier;
@property (T@"_UIContextMenuPresentation",&,N,V_outgoingPresentation) outgoingPresentation;
@property (T@"_UIClickPresentationInteraction",R,N,V_presentationInteraction) presentationInteraction;
@property (T@"_UIContextMenuAnimator",&,N,V_pendingCommitAnimator) pendingCommitAnimator;
@property (T{CGPoint=dd},N,V_pendingMenuSourceLocation) pendingMenuSourceLocation;
@property (TB,N,V__requiresTouchAuthentication) _requiresTouchAuthentication;
@property (TB,N) allowSimultaneousRecognition;
@property (T@"UIGestureRecognizer",R,N) gestureRecognizerForFailureRelationships;
@property (TB,R,N,G_reachedForceThreshold) reachedForceThreshold;
@property (TB,R,N) _hasVisibleMenu;
@property (TQ,R,N) _inputPrecision;
@property (T@"UIGestureRecognizer",R,N) _gestureRecognizerForBeginningDragRelationships;
@property (TQ,N,S_setFallbackDriverStyle:) _fallbackDriverStyle;
@property (T@,W,N,S_setProxySender:,V__proxySender) _proxySender;
@property (T@"NSSet",R,N) _internalIdentifiersForDismissingMenu;
@property (TB,N,V__useSenderAsResponderSender) _useSenderAsResponderSender;
@property (T@"<UIMenuLeaf>",W,N,V__selectedMenuLeaf) _selectedMenuLeaf;
@property (TB,N,V__ignorePreviewForDismissingDelegate) _ignorePreviewForDismissingDelegate;
@property (TB,R,N) _shouldAutomaticallyInstallIntelligentAssistantAction;
@property (T@"_UICampoActionConfiguration",R,N) _contextMenuPresenterConfiguration;
@property (T@"<UIContextMenuInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,R,N) menuAppearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[UIContextMenuInteraction visualStyleRegistryIdentity];
+[UIContextMenuInteraction _setDefaultDriverClasses:forIdiom:];
```

## Instance methods

```
-[UIContextMenuInteraction dismissMenu];
-[UIContextMenuInteraction _selectedMenuLeaf];
-[UIContextMenuInteraction clickPresentationInteraction:presentationForPresentingViewController:];
-[UIContextMenuInteraction initWithDelegate:];
-[UIContextMenuInteraction _hasVisibleMenu];
-[UIContextMenuInteraction setAllowSimultaneousRecognition:];
-[UIContextMenuInteraction _willBeginWithConfiguration:];
-[UIContextMenuInteraction _contextMenuPresenterConfiguration];
-[UIContextMenuInteraction _proxySender];
-[UIContextMenuInteraction dealloc];
-[UIContextMenuInteraction deferredMenuElementWasFulfilled:];
-[UIContextMenuInteraction _reachedForceThreshold];
-[UIContextMenuInteraction _inputPrecision];
-[UIContextMenuInteraction menuAppearance];
-[UIContextMenuInteraction allowSimultaneousRecognition];
-[UIContextMenuInteraction locationInView:];
-[UIContextMenuInteraction pendingConfiguration];
-[UIContextMenuInteraction view];
-[UIContextMenuInteraction _setProxySender:];
-[UIContextMenuInteraction activationStyleForClickPresentationInteraction:];
-[UIContextMenuInteraction set_selectedMenuLeaf:];
-[UIContextMenuInteraction setPendingConfiguration:];
-[UIContextMenuInteraction willMoveToView:];
-[UIContextMenuInteraction _useSenderAsResponderSender];
-[UIContextMenuInteraction delegate];
-[UIContextMenuInteraction gestureRecognizerForExclusionRelationships];
-[UIContextMenuInteraction clickPresentationInteraction:previewForHighlightingAtLocation:];
-[UIContextMenuInteraction _shouldAutomaticallyInstallIntelligentAssistantAction];
-[UIContextMenuInteraction setDrivers:];
-[UIContextMenuInteraction presentationInteraction];
-[UIContextMenuInteraction _viewTraitCollectionDidChange:];
-[UIContextMenuInteraction didMoveToView:];
-[UIContextMenuInteraction set_useSenderAsResponderSender:];
-[UIContextMenuInteraction contextMenuPresentationDidBeginIntelligentAssistantInteraction:];
-[UIContextMenuInteraction _actualLayoutForPreferredLayout:withConfiguration:];
-[UIContextMenuInteraction _clickPresentationInteraction:dragSessionDidEndForItems:];
-[UIContextMenuInteraction _clickPresentationInteraction:interactionEffectForTargetedPreview:];
-[UIContextMenuInteraction _clickPresentationInteraction:item:willAnimateDragCancelWithAnimator:];
-[UIContextMenuInteraction _clickPresentationInteraction:liveDragPreviewForPresentation:dragItem:];
-[UIContextMenuInteraction _clickPresentationInteraction:previewForCancellingDragItem:];
-[UIContextMenuInteraction _clickPresentationInteraction:shouldBeDelayedByGestureRecognizer:];
-[UIContextMenuInteraction _clickPresentationInteraction:shouldBeginWithTouch:completion:];
-[UIContextMenuInteraction _clickPresentationInteraction:shouldMaintainKeyboardAssertionForFirstResponder:presentation:];
-[UIContextMenuInteraction _clickPresentationInteraction:shouldPresentWithCompletion:];
-[UIContextMenuInteraction _clickPresentationInteractionEnded:forPresentation:reason:];
-[UIContextMenuInteraction _clickPresentationInteractionShouldAllowDragAfterDismiss:];
-[UIContextMenuInteraction _clickPresentationInteractionShouldAllowRapidRestart:];
-[UIContextMenuInteraction _clickPresentationInteractionShouldAssociateWithDrag:];
-[UIContextMenuInteraction _contextMenuPresentationPreviewWasTapped:];
-[UIContextMenuInteraction _defaultPreparationContextWithFirstResponderTarget:];
-[UIContextMenuInteraction _delegate_configurationForMenuAtLocation:];
-[UIContextMenuInteraction _delegate_contextMenuInteractionWillDisplayForConfiguration:];
-[UIContextMenuInteraction _delegate_contextMenuInteractionWillEndForConfiguration:presentation:];
-[UIContextMenuInteraction _delegate_getAccessoryViewsForConfiguration:];
-[UIContextMenuInteraction _delegate_performPreviewActionCommitAnimation:];
-[UIContextMenuInteraction _delegate_previewForDismissingForConfiguration:clientReturnedPreview:];
-[UIContextMenuInteraction _delegate_previewForHighlightingForConfiguration:];
-[UIContextMenuInteraction _delegate_tappedPreviewForConfiguration:withAnimator:];
-[UIContextMenuInteraction _fallbackDriverStyle];
-[UIContextMenuInteraction _fulfilledConfigurationForConfiguration:atLocation:];
-[UIContextMenuInteraction _gestureRecognizerForBeginningDragRelationships];
-[UIContextMenuInteraction _ignorePreviewForDismissingDelegate];
-[UIContextMenuInteraction _interactionShouldBeginAtPoint:completion:];
-[UIContextMenuInteraction _internalIdentifiersForDismissingMenu];
-[UIContextMenuInteraction _menuPreparedForDisplayWithMenu:firstResponder:];
-[UIContextMenuInteraction _performCleanupForConfigurationWithIdentifier:];
-[UIContextMenuInteraction _prepareSceneActivationConfiguration:];
-[UIContextMenuInteraction _presentMenuAtLocation3D:];
-[UIContextMenuInteraction _presentMenuAtLocation:];
-[UIContextMenuInteraction _requestSceneActivationWithConfiguration:animated:sender:errorHandler:];
-[UIContextMenuInteraction _requiresTouchAuthentication];
-[UIContextMenuInteraction _retargetDismissingMenuWithInternalIdentifier:toPreview:force:];
-[UIContextMenuInteraction _rootMenuPreparedForDisplayWithMenu:firstResponder:];
-[UIContextMenuInteraction _secondaryPreviewsForClickPresentationInteraction:];
-[UIContextMenuInteraction _setFallbackDriverStyle:];
-[UIContextMenuInteraction _shouldKeepInputViewVisibleForStyle:];
-[UIContextMenuInteraction _suggestedMenuForConfiguration:atLocation:inCoordinateSpace:];
-[UIContextMenuInteraction _testing_metdataForMenuElements:];
-[UIContextMenuInteraction configurationsByIdentifier];
-[UIContextMenuInteraction contextMenuPresentation:didBeginDragWithTouch:];
-[UIContextMenuInteraction contextMenuPresentation:didRequestDismissalWithReason:alongsideActions:completion:];
-[UIContextMenuInteraction contextMenuPresentation:didSelectMenuLeaf:];
-[UIContextMenuInteraction contextMenuPresentation:dismissalPreviewForItem:clientReturnedPreview:];
-[UIContextMenuInteraction contextMenuPresentation:willDisplayMenu:];
-[UIContextMenuInteraction contextMenuPresentationDidEndPanInteraction:];
-[UIContextMenuInteraction contextMenuPresentationShouldAdoptDragSession:];
-[UIContextMenuInteraction contextMenuPresentationShouldAllowSwipeToDismissForBeginningPanInteraction:];
-[UIContextMenuInteraction gestureRecognizerForFailureRelationships];
-[UIContextMenuInteraction outgoingPresentation];
-[UIContextMenuInteraction pendingCommitAnimator];
-[UIContextMenuInteraction pendingMenuSourceLocation];
-[UIContextMenuInteraction presentationsByIdentifier];
-[UIContextMenuInteraction presenterConfigurationForIntelligentAssistantInContextMenuPresentation:];
-[UIContextMenuInteraction setConfigurationsByIdentifier:];
-[UIContextMenuInteraction setOutgoingPresentation:];
-[UIContextMenuInteraction setPendingCommitAnimator:];
-[UIContextMenuInteraction setPendingMenuSourceLocation:];
-[UIContextMenuInteraction setPresentationsByIdentifier:];
-[UIContextMenuInteraction set_ignorePreviewForDismissingDelegate:];
-[UIContextMenuInteraction set_requiresTouchAuthentication:];
-[UIContextMenuInteraction updateVisibleMenuWithBlock:];
```
