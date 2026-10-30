# `_UIContextMenuPresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIClickPresentation`
- Protocols: `_UIContextMenuUIControllerDelegate`, `_UIContextMenuPreviewPresentationControllerDelegate`
- 3 instance variables, 9 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _suppressInputViewDuringPresentation;
@"<_UIContextMenuPresentationDelegate>" _delegate;
@"_UIContextMenuUIController" _uiController;
```

## Properties

```
@property (T@"<_UIContextMenuPresentationDelegate>",W,N,V_delegate) delegate;
@property (T@"_UIContextMenuUIController",R,N,V_uiController) uiController;
@property (TB,N,V_suppressInputViewDuringPresentation) suppressInputViewDuringPresentation;
@property (T@"_UIFulfilledContextMenuConfiguration",R,N) menuConfiguration;
@property (T@"NSArray",R,N) visibleMenus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuPresentation present];
-[_UIContextMenuPresentation addDismissalCompletion:];
-[_UIContextMenuPresentation contextMenuPreviewPresentationController:didChangePreviewContentSize:];
-[_UIContextMenuPresentation uiController];
-[_UIContextMenuPresentation _platformMetrics];
-[_UIContextMenuPresentation dismiss];
-[_UIContextMenuPresentation retargetDismissingMenuToPreview:];
-[_UIContextMenuPresentation contextMenuUIController:didRequestDismissalWithReason:alongsideActions:completion:];
-[_UIContextMenuPresentation viewTraitCollectionDidChange];
-[_UIContextMenuPresentation initWithPresentingViewController:configuration:style:outgoingPresentation:];
-[_UIContextMenuPresentation contextMenuUIControllerShouldAllowSwipeToDismissForBeginningPanInteraction:];
-[_UIContextMenuPresentation prepareToDismiss];
-[_UIContextMenuPresentation requestMenuDismissal];
-[_UIContextMenuPresentation previewForCancellingDragItem:];
-[_UIContextMenuPresentation presenterConfigurationForIntelligentAssistantInContextMenuUIController:];
-[_UIContextMenuPresentation setAlongsideAnimatorForPresentation:];
-[_UIContextMenuPresentation windowSceneActivationPreview];
-[_UIContextMenuPresentation preferredFocusEnvironmentsForContextMenuPreviewPresentationController:];
-[_UIContextMenuPresentation contextMenuUIController:willDisplayMenu:];
-[_UIContextMenuPresentation prepareToPresent];
-[_UIContextMenuPresentation setDelegate:];
-[_UIContextMenuPresentation contextMenuUIController:dismissalPreviewForItem:clientReturnedPreview:];
-[_UIContextMenuPresentation contextMenuUIController:didBeginDragWithTouch:];
-[_UIContextMenuPresentation delegate];
-[_UIContextMenuPresentation visibleMenus];
-[_UIContextMenuPresentation dragWillCancelWithAnimator:];
-[_UIContextMenuPresentation presentingViewControllerForIntelligentAssistantInContextMenuUIController:];
-[_UIContextMenuPresentation livePreviewForDragItem:preferringFullSize:];
-[_UIContextMenuPresentation suppressInputViewDuringPresentation];
-[_UIContextMenuPresentation setSuppressInputViewDuringPresentation:];
-[_UIContextMenuPresentation contextMenuUIController:didSelectMenuLeaf:];
-[_UIContextMenuPresentation contextMenuUIControllerWillPerformLayout:withPreviewSize:];
-[_UIContextMenuPresentation displayMenu:inPlaceOfMenu:];
-[_UIContextMenuPresentation contextMenuUIControllerDidEndPanInteraction:];
-[_UIContextMenuPresentation contextMenuUIControllerDidBeginIntelligentAssistantInteraction:];
-[_UIContextMenuPresentation setAlongsideAnimatorForDismissal:];
-[_UIContextMenuPresentation menuConfiguration];
```
