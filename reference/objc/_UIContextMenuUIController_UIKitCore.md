# `_UIContextMenuUIController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuViewDelegate`, `UIGestureRecognizerDelegate`, `_UIContextMenuPanControllerDelegate`, `_UICampoServiceSessionDelegate`
- 28 instance variables, 32 properties, 112 instance methods, 0 class methods

## Instance variables

```
B _previewSizeDidChange;
B _menuIsConcealed;
B _didAvoidKeyboard;
B __dragWasCanceled;
@"UIView" _platterContainerView;
@"UIView" _platterTransitionView;
@"UIVisualEffectView" _backgroundEffectView;
@"_UIMorphPlatterViewBase" _contentPlatterView;
@"_UIContextMenuView" _menuView;
@"_UIFlocker" _flocker;
@"_UIContextMenuLayoutArbiterOutput" _currentLayout;
@"UIViewFloatAnimatableProperty" _backgroundViewAnimationProgress;
@"<_UIContextMenuUIControllerDelegate>" _delegate;
@"_UIFulfilledContextMenuConfiguration" _menuConfiguration;
@"_UIContextMenuStyle" _menuStyle;
@"UITapGestureRecognizer" _platterActionTapGestureRecognizer;
@"UITapGestureRecognizer" _dismissalTapGestureRecognizer;
@"_UIContextMenuActionScrubbingHandoffGestureRecognizer" _actionScrubbingHandoffGestureRecognizer;
@"_UIContextMenuPanController" _platterPanController;
@"_UIContextMenuLayoutArbiter" _layoutArbiter;
Q _state;
@"_UIViewAlphaOverrideAssertion" _sourcePreviewAlphaOverrideAssertion;
@"_UIContextMenuSubterraneanContainerView" __subterraneanViewContainer;
@"_UIPlatterView" __destinationPlatterView;
@"UIView" __dragContainerView;
@"UIView" __dragContainerTransitionView;
@? __postMorphDragItemUpdate;
{CGSize="width"d"height"d} _previewSize;
```

## Properties

```
@property (T@"UITapGestureRecognizer",&,N,V_platterActionTapGestureRecognizer) platterActionTapGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_dismissalTapGestureRecognizer) dismissalTapGestureRecognizer;
@property (T@"_UIContextMenuActionScrubbingHandoffGestureRecognizer",&,N,V_actionScrubbingHandoffGestureRecognizer) actionScrubbingHandoffGestureRecognizer;
@property (T@"_UIFulfilledContextMenuConfiguration",&,N,V_menuConfiguration) menuConfiguration;
@property (T@"_UIContextMenuPanController",&,N,V_platterPanController) platterPanController;
@property (T@"_UIContextMenuLayoutArbiter",&,N,V_layoutArbiter) layoutArbiter;
@property (T@"_UIContextMenuStyle",C,N,V_menuStyle) menuStyle;
@property (T{CGSize=dd},N,V_previewSize) previewSize;
@property (TB,N,V_previewSizeDidChange) previewSizeDidChange;
@property (TB,N,V_menuIsConcealed) menuIsConcealed;
@property (TB,N,V_didAvoidKeyboard) didAvoidKeyboard;
@property (TQ,N,V_state) state;
@property (T@"_UIViewAlphaOverrideAssertion",&,N,V_sourcePreviewAlphaOverrideAssertion) sourcePreviewAlphaOverrideAssertion;
@property (T@"_UIContextMenuSubterraneanContainerView",&,N,V__subterraneanViewContainer) _subterraneanViewContainer;
@property (T@"_UIPlatterView",&,N,V__destinationPlatterView) _destinationPlatterView;
@property (T@"UIView",&,N,V__dragContainerView) _dragContainerView;
@property (T@"UIView",&,N,V__dragContainerTransitionView) _dragContainerTransitionView;
@property (T@?,C,N,V__postMorphDragItemUpdate) _postMorphDragItemUpdate;
@property (TB,N,V__dragWasCanceled) _dragWasCanceled;
@property (T@"<_UIContextMenuUIControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,N,V_platterTransitionView) platterTransitionView;
@property (T@"UIView",R,N,V_platterContainerView) platterContainerView;
@property (T@"UIVisualEffectView",R,N,V_backgroundEffectView) backgroundEffectView;
@property (T@"_UIMorphPlatterViewBase",R,N,V_contentPlatterView) contentPlatterView;
@property (T@"_UIContextMenuView",R,N,V_menuView) menuView;
@property (T@"_UIFlocker",R,N,V_flocker) flocker;
@property (T@"_UIContextMenuLayoutArbiterOutput",R,N,V_currentLayout) currentLayout;
@property (T@"UIViewFloatAnimatableProperty",R,N,V_backgroundViewAnimationProgress) backgroundViewAnimationProgress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuUIController _keyboardWillShow:];
-[_UIContextMenuUIController setState:];
-[_UIContextMenuUIController _keyboardWillHide:];
-[_UIContextMenuUIController _platformMetrics];
-[_UIContextMenuUIController retargetDismissingMenuToPreview:];
-[_UIContextMenuUIController _campoServiceSession:willShowPopoverPresentation:];
-[_UIContextMenuUIController viewTraitCollectionDidChange];
-[_UIContextMenuUIController dealloc];
-[_UIContextMenuUIController setMenuStyle:];
-[_UIContextMenuUIController currentLayout];
-[_UIContextMenuUIController previewForCancellingDragItem:];
-[_UIContextMenuUIController contentPlatterView];
-[_UIContextMenuUIController _campoServiceSessionDidEnd:];
-[_UIContextMenuUIController windowSceneActivationPreview];
-[_UIContextMenuUIController _sceneWillDeactivate:];
-[_UIContextMenuUIController setDelegate:];
-[_UIContextMenuUIController gestureRecognizerShouldBegin:];
-[_UIContextMenuUIController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIContextMenuUIController delegate];
-[_UIContextMenuUIController _campoServiceSession:didShowPopoverPresentation:];
-[_UIContextMenuUIController _isPresented];
-[_UIContextMenuUIController dragWillCancelWithAnimator:];
-[_UIContextMenuUIController livePreviewForDragItem:preferringFullSize:];
-[_UIContextMenuUIController backgroundEffectView];
-[_UIContextMenuUIController displayMenu:inPlaceOfMenu:];
-[_UIContextMenuUIController menuView];
-[_UIContextMenuUIController dismissalTransitionWillBegin];
-[_UIContextMenuUIController menuStyle];
-[_UIContextMenuUIController menuConfiguration];
-[_UIContextMenuUIController _campoServiceSessionDidBegin:];
-[_UIContextMenuUIController state];
-[_UIContextMenuUIController presentationTransitionWillBegin];
-[_UIContextMenuUIController _interfaceIdiom];
-[_UIContextMenuUIController _preferredSubmenuHierarchyStyle];
-[_UIContextMenuUIController backgroundViewAnimationProgress];
-[_UIContextMenuUIController flocker];
-[_UIContextMenuUIController platterPanControllerDidTearOff:];
-[_UIContextMenuUIController _handlePlatterActionTapGesture:];
-[_UIContextMenuUIController menuIsConcealed];
-[_UIContextMenuUIController setPreviewSize:];
-[_UIContextMenuUIController _adjustViewForKeyboardVisibility:keyboardInfo:];
-[_UIContextMenuUIController _campoServiceSession:willDismissPopoverPresentation:];
-[_UIContextMenuUIController _cleanUpDragViews];
-[_UIContextMenuUIController _concealMenu];
-[_UIContextMenuUIController _createMenuViewIfNecessaryForMenu:];
-[_UIContextMenuUIController _destinationPlatterView];
-[_UIContextMenuUIController _didBeginMorphToDragPreview];
-[_UIContextMenuUIController _didCompleteMorphToDragPreview];
-[_UIContextMenuUIController _displayMenu:updateType:];
-[_UIContextMenuUIController _dragContainerTransitionView];
-[_UIContextMenuUIController _dragContainerView];
-[_UIContextMenuUIController _dragWasCanceled];
-[_UIContextMenuUIController _enumeratePlatterViewsWithBlock:];
-[_UIContextMenuUIController _handleActionHandoffGesture:];
-[_UIContextMenuUIController _handleDismissalTapGesture:];
-[_UIContextMenuUIController _installViewsIntoDragContainerView:];
-[_UIContextMenuUIController _isAnimatingPresentation];
-[_UIContextMenuUIController _layoutWithUpdatedAttachment:concealedMenu:];
-[_UIContextMenuUIController _needsToAvoidKeyboardForResponder:];
-[_UIContextMenuUIController _postMorphDragItemUpdate];
-[_UIContextMenuUIController _primaryPlatterDragPreviewForDragItem:preferringFullSize:];
-[_UIContextMenuUIController _replaceVisibleMenu:withMenu:];
-[_UIContextMenuUIController _subterraneanViewContainer];
-[_UIContextMenuUIController _testing_dismissByTappingOutside];
-[_UIContextMenuUIController _testing_tapAnAction];
-[_UIContextMenuUIController _updateActionsViewReversesOrderForAttachment:];
-[_UIContextMenuUIController _updateLayoutAndAttachment:];
-[_UIContextMenuUIController _updatePlatterAndActionViewLayoutForce:updateAttachment:];
-[_UIContextMenuUIController _updatePlatterAndActionViewLayoutForce:updateAttachment:adjustDetent:];
-[_UIContextMenuUIController _updatePlatterContainerViewTraitCollection];
-[_UIContextMenuUIController actionScrubbingHandoffGestureRecognizer];
-[_UIContextMenuUIController contextMenuView:didSelectElement:];
-[_UIContextMenuUIController contextMenuView:willDisplayMenu:];
-[_UIContextMenuUIController didAvoidKeyboard];
-[_UIContextMenuUIController didSelectCancelActionInContextMenuView:];
-[_UIContextMenuUIController dismissalPreviewForSecondaryItem:style:];
-[_UIContextMenuUIController dismissalPreviewForStyle:clientReturnedPreview:];
-[_UIContextMenuUIController dismissalTapGestureRecognizer];
-[_UIContextMenuUIController dismissalTransitionDidEnd];
-[_UIContextMenuUIController endSourcePreviewHidingIfNeeded];
-[_UIContextMenuUIController hideSourcePreview:];
-[_UIContextMenuUIController initWithConfiguration:style:];
-[_UIContextMenuUIController layoutArbiter];
-[_UIContextMenuUIController platterActionTapGestureRecognizer];
-[_UIContextMenuUIController platterContainerView];
-[_UIContextMenuUIController platterPanController];
-[_UIContextMenuUIController platterPanControllerDidSwipeDown:];
-[_UIContextMenuUIController platterPanInteractionBegan:allowSwipeToDismiss:];
-[_UIContextMenuUIController platterPanInteractionEnded:];
-[_UIContextMenuUIController platterTransitionView];
-[_UIContextMenuUIController presentationTransitionDidEnd];
-[_UIContextMenuUIController previewSize];
-[_UIContextMenuUIController previewSizeDidChange];
-[_UIContextMenuUIController previewSizeDidChange:];
-[_UIContextMenuUIController setActionScrubbingHandoffGestureRecognizer:];
-[_UIContextMenuUIController setDidAvoidKeyboard:];
-[_UIContextMenuUIController setDismissalTapGestureRecognizer:];
-[_UIContextMenuUIController setLayoutArbiter:];
-[_UIContextMenuUIController setMenuConfiguration:];
-[_UIContextMenuUIController setMenuIsConcealed:];
-[_UIContextMenuUIController setPlatterActionTapGestureRecognizer:];
-[_UIContextMenuUIController setPlatterPanController:];
-[_UIContextMenuUIController setPreviewSizeDidChange:];
-[_UIContextMenuUIController setSourcePreviewAlphaOverrideAssertion:];
-[_UIContextMenuUIController set_destinationPlatterView:];
-[_UIContextMenuUIController set_dragContainerTransitionView:];
-[_UIContextMenuUIController set_dragContainerView:];
-[_UIContextMenuUIController set_dragWasCanceled:];
-[_UIContextMenuUIController set_postMorphDragItemUpdate:];
-[_UIContextMenuUIController set_subterraneanViewContainer:];
-[_UIContextMenuUIController shouldMaintainKeyboardAssertionForFirstResponder:];
-[_UIContextMenuUIController sourcePreviewAlphaOverrideAssertion];
```
