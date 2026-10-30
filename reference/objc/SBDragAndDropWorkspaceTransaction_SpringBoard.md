# `SBDragAndDropWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMainWorkspaceTransaction`
- Protocols: `SBWorkspaceApplicationSceneTransitionContextDelegate`, `SBSceneLayoutWorkspaceTransactionObserver`, `UIDragInteractionDelegate_Private`, `UIDropInteractionDelegate_Private`
- 47 instance variables, 5 properties, 75 instance methods, 18 class methods

## Instance variables

```
@"SBSwitcherController" _switcherController;
@"SBFluidSwitcherViewController" _switcherContentController;
@"SBApplicationController" _applicationController;
@"<SBDragAndDropWorkspaceTransactionDelegate>" _delegate;
@"SBMainDisplayLayoutState" _initialLayoutState;
@"SBMainDisplayLayoutState" _currentLayoutState;
@"SBMainDisplayLayoutState" _finalLayoutState;
@"SBApplicationDropSession" _dropSession;
Q _sessionState;
@"SBDeviceApplicationSceneHandle" _draggingApplicationSceneHandle;
@"SBDisplayItem" _draggingDisplayItem;
B _beganTrackingDropSession;
@"SBMainWorkspaceTransitionRequest" _dropTransitionRequest;
@"SBToAppsWorkspaceTransaction" _currentWorkspaceTransaction;
q _currentDropAction;
@"SBMainDisplayLayoutState" _currentDropActionProposedLayoutState;
B _performedDrop;
B _dropAnimationCompleted;
B _layoutStateTransitionCompleted;
B _dragExitedDropZone;
{CGSize="width"d"height"d} _cachedDefaultReferenceSizeForSceneView;
@"SBLayoutElement" _layoutElementForWindowDrag;
B _windowDragEnteredPlatterZone;
B _windowLiftAnimationCompleted;
@"SBApplicationSceneUpdateTransaction" _sceneUpdateTransactionForWindowDrag;
@"CADisplayLink" _displayLinkForWindowDrag;
q _windowDragPauseCounter;
@"NSMutableSet" _pendingSceneUpdatesTransactions;
@"SBAppPlatterDragPreview" _activePlatterPreview;
@"<SBAppPlatterDragSourceViewProviding>" _activeSourceViewProvider;
Q _numberOfAttemptsRequestingVisibleItems;
@"UIView" _contentDragPreview;
q _animatingPlatterPreview;
@"<BSInvalidatable>" _deferOrientationUpdatesForDragAndDropAssertion;
@"SBTouchHistory" _touchHistory;
@"SBMedusaSettings" _medusaSettings;
@"SBSwitcherWindowingSettings" _windowingSettings;
@"NSUUID" _gestureID;
@"SBFluidSwitcherGesture" _dragAndDropGesture;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
B _draggingExistingItemFromActiveLayoutState;
B _draggingItemWasInitiallyFullscreen;
@"SBFlexibleWindowingAutoLayoutSpace" _initialAutoLayoutSpace;
@"SBDisplayItemLayoutAttributes" _initialDisplayItemLayoutAttributes;
@"SBDisplayItem" _initialSlideOverDisplayItem;
B _currentlyOverExistingSlideOverItem;
B _inDesignatedSlideOverDropZone;
```

## Properties

```
@property (TB,R,N,GisDragging) dragging;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDragAndDropWorkspaceTransaction _screenInsetsForUIDragDropSession:];
+[SBDragAndDropWorkspaceTransaction _shouldTrackLocationOfDropSession:forSwitcherController:applicationController:isCurrentlyTracking:];
+[SBDragAndDropWorkspaceTransaction isDragOverFullscreenRegionAtLocation:inBounds:];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsContentDraggingCommandeerInsetForUniversalControl];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsContentDraggingCommandeerWidth];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsContentDraggingFloatingActivationWidth];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsContentDraggingSideActivationWidth];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsFullscreenActivationRegionSize];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsLeftOrRightTilingActivationRegionWidthPercentage];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsPaddingAboveDockToDisallowDropBoundsHeightPercentage];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsSideActivationGutterSize];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsSlideOverActivationRegionHeightPercentage];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsSlideOverActivationRegionWidthPercentage];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsWindowTearOffDraggingFloatingActivationWidth];
+[SBDragAndDropWorkspaceTransaction prototypeSettingsWindowTearOffDraggingSideActivationWidth];
+[SBDragAndDropWorkspaceTransaction screenEdgeForDragOverSideGutterRegionsAtLocation:inBounds:totalContentDragGutterWidth:screenInsets:];
+[SBDragAndDropWorkspaceTransaction shouldTrackLocationOfDropSession:forSwitcherController:applicationController:];
+[SBDragAndDropWorkspaceTransaction sourceSceneInterfaceOrientedBoundsForDropSession:switcherController:applicationController:];
```

## Instance methods

```
-[SBDragAndDropWorkspaceTransaction dragInteraction:previewForLiftingItem:session:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:itemsForBeginningSession:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:previewForCancellingItem:withDefault:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:item:willAnimateCancelWithAnimator:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:sessionDidEnter:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:sessionDidMove:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:sessionDidUpdate:];
-[SBDragAndDropWorkspaceTransaction _childTransactionDidComplete:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:session:didEndWithOperation:];
-[SBDragAndDropWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:sessionWillBegin:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:concludeDrop:];
-[SBDragAndDropWorkspaceTransaction _canBeInterrupted];
-[SBDragAndDropWorkspaceTransaction _didComplete];
-[SBDragAndDropWorkspaceTransaction _begin];
-[SBDragAndDropWorkspaceTransaction dragInteraction:session:willEndWithOperation:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:performDrop:];
-[SBDragAndDropWorkspaceTransaction transaction:didCommitSceneUpdate:];
-[SBDragAndDropWorkspaceTransaction dealloc];
-[SBDragAndDropWorkspaceTransaction applicationTransitionContext:frameForApplicationSceneEntity:];
-[SBDragAndDropWorkspaceTransaction layoutStateForApplicationTransitionContext:];
-[SBDragAndDropWorkspaceTransaction isDragging];
-[SBDragAndDropWorkspaceTransaction dropInteraction:item:willAnimateDropWithAnimator:];
-[SBDragAndDropWorkspaceTransaction previousLayoutStateForApplicationTransitionContext:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:sessionDidExit:];
-[SBDragAndDropWorkspaceTransaction _willInterruptWithReason:];
-[SBDragAndDropWorkspaceTransaction dragInteraction:willAnimateLiftWithAnimator:session:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:sessionDidEnd:];
-[SBDragAndDropWorkspaceTransaction dropInteraction:previewForDroppingItem:withDefault:];
-[SBDragAndDropWorkspaceTransaction _didInterruptWithReason:];
-[SBDragAndDropWorkspaceTransaction _dragInteraction:customSpringAnimationBehaviorForCancellingItem:];
-[SBDragAndDropWorkspaceTransaction _dragInteractionDidCancelLiftWithoutDragging:];
-[SBDragAndDropWorkspaceTransaction _dropInteraction:customSpringAnimationBehaviorForDroppingItem:];
-[SBDragAndDropWorkspaceTransaction _getPlatterDiffuseShadowParameters:rimShadowParameters:diffuseFilters:rimFilters:forDropAction:setDown:mode:userInterfaceStyle:];
-[SBDragAndDropWorkspaceTransaction _createPlatterPreviewForApplication:withSourceView:dropSession:];
-[SBDragAndDropWorkspaceTransaction _currentGestureEventForGesture:];
-[SBDragAndDropWorkspaceTransaction _runFinalLayoutStateTransaction];
-[SBDragAndDropWorkspaceTransaction _updateForWindowDragForSession:];
-[SBDragAndDropWorkspaceTransaction _addChildWorkspaceTransaction:];
-[SBDragAndDropWorkspaceTransaction _cleanUpAndCompleteTransactionIfNecessary];
-[SBDragAndDropWorkspaceTransaction _configurePlatterPreview:forSceneHandle:completion:];
-[SBDragAndDropWorkspaceTransaction _cornerRadiusConfigurationForDropAction:proposedDropLayoutState:setDown:mode:];
-[SBDragAndDropWorkspaceTransaction _defaultReferenceSizeForSceneView];
-[SBDragAndDropWorkspaceTransaction _displayLinkDidUpdate:];
-[SBDragAndDropWorkspaceTransaction _dragPreviewForDroppingItem:withDefault:];
-[SBDragAndDropWorkspaceTransaction _endDragAndDropFluidGesture];
-[SBDragAndDropWorkspaceTransaction _handleSessionDidEnd:];
-[SBDragAndDropWorkspaceTransaction _handleSessionDidPerformDrop:];
-[SBDragAndDropWorkspaceTransaction _handleSessionDidUpdate:];
-[SBDragAndDropWorkspaceTransaction _handleWillAnimateDropWithAnimator:];
-[SBDragAndDropWorkspaceTransaction _iconManager];
-[SBDragAndDropWorkspaceTransaction _interruptForDragExitedDropZoneIfNecessary];
-[SBDragAndDropWorkspaceTransaction _layoutAttributesForArrangingItemsGivenDropAction:];
-[SBDragAndDropWorkspaceTransaction _platterFrameInSwitcherView];
-[SBDragAndDropWorkspaceTransaction _platterScale];
-[SBDragAndDropWorkspaceTransaction _platterSizeForDropAction:proposedDropLayoutState:setDown:];
-[SBDragAndDropWorkspaceTransaction _platterSourceViewScaleForSetDropAction:setDown:];
-[SBDragAndDropWorkspaceTransaction _setupPlatterPreviewForContentDrag];
-[SBDragAndDropWorkspaceTransaction _showResizeUI];
-[SBDragAndDropWorkspaceTransaction _transitionRequestForDropAction:];
-[SBDragAndDropWorkspaceTransaction _uncommandeerContentDrag];
-[SBDragAndDropWorkspaceTransaction _updateActiveSourceViewProviderWithDragState:];
-[SBDragAndDropWorkspaceTransaction _updateAnchorPointForPlatterPreview:dragPreview:withSourceViewBounds:location:];
-[SBDragAndDropWorkspaceTransaction _updateCurrentDropActionForSession:];
-[SBDragAndDropWorkspaceTransaction _updateCurrentDropActionProposedLayoutState];
-[SBDragAndDropWorkspaceTransaction _updatePlatterPreviewForSetDown:animated:];
-[SBDragAndDropWorkspaceTransaction _updatePlatterPreviewWithUpdatedSourceView];
-[SBDragAndDropWorkspaceTransaction _updatePlatterViewBlurForDropCompletion];
-[SBDragAndDropWorkspaceTransaction _updateSlideOverTongueIfNeeded];
-[SBDragAndDropWorkspaceTransaction _willInterruptForTransitionRequest:];
-[SBDragAndDropWorkspaceTransaction blurReadinessDidChange];
-[SBDragAndDropWorkspaceTransaction initWithTransitionRequest:switcherController:applicationController:dropSession:delegate:];
-[SBDragAndDropWorkspaceTransaction matchesApplicationDropSession:];
-[SBDragAndDropWorkspaceTransaction matchesUIDragDropSession:];
-[SBDragAndDropWorkspaceTransaction resizeUIAnimationFactory];
```
