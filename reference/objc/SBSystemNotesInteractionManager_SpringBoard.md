# `SBSystemNotesInteractionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemGestureRecognizerDelegate`, `SBFZStackParticipantDelegate`, `SBPIPInteractionControllerDataSource`, `SBPIPSceneContentContainerAdapterDelegate`
- 22 instance variables, 4 properties, 69 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemNotesInteractionManagerDelegate>" _delegate;
@"<SBSystemNotesInteractionManagerDataSource>" _dataSource;
@"SBSystemNotesPositionHyperregionComposer" _positionRegionsComposer;
@"SBCornerPencilPanGestureRecognizer" _rightPencilSystemCornerGestureRecognizer;
@"SBCornerPencilPanGestureRecognizer" _leftPencilSystemCornerGestureRecognizer;
@"SBCornerFingerPanGestureRecognizer" _rightFingerSystemCornerGestureRecognizer;
@"SBCornerFingerPanGestureRecognizer" _leftFingerSystemCornerGestureRecognizer;
@"SBSystemNotesSettings" _pipSettings;
@"SBFZStackParticipant" _zStackParticipant;
@"SBSystemGestureManager" _systemGestureManager;
@"SBSystemPointerInteractionManager" _systemPointerInteractionManager;
Q _cornerDismissState;
I _cornerDismissGenCount;
B _isDismissingNonInteractively;
I _nonInteractiveDismissGenCount;
@"SBPIPControllerCoordinator" _pipCoordinator;
q _initialInteractorPanPresentationMode;
Q _edgeProtectState;
I _edgeProtectGenCount;
@"<BSInvalidatable>" _edgeProtectStashAssertion;
B _panGestureIsSystemGesture;
@"SBWindowScene" _windowScene;
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
-[SBSystemNotesInteractionManager gestureRecognizer:shouldReceiveTouch:];
-[SBSystemNotesInteractionManager zStackParticipant:updatePreferences:];
-[SBSystemNotesInteractionManager dismissAnimated:completion:];
-[SBSystemNotesInteractionManager zStackParticipantDidChange:];
-[SBSystemNotesInteractionManager zStackParticipant:updateZOrderPreferences:];
-[SBSystemNotesInteractionManager viewForSystemGestureRecognizer:];
-[SBSystemNotesInteractionManager gestureRecognizerShouldBegin:];
-[SBSystemNotesInteractionManager _gestureRecognizerIsActive:];
-[SBSystemNotesInteractionManager debugName];
-[SBSystemNotesInteractionManager _windowManagementStyleDidChange:];
-[SBSystemNotesInteractionManager layoutSettings];
-[SBSystemNotesInteractionManager expandAnimated:];
-[SBSystemNotesInteractionManager collapseAnimated:];
-[SBSystemNotesInteractionManager _touchTypeForGestureRecognizer:];
-[SBSystemNotesInteractionManager contentContainerAdapter:handleDestructionRequestForSceneHandle:];
-[SBSystemNotesInteractionManager _absoluteScaleForInteractiveSystemNotesGesture:];
-[SBSystemNotesInteractionManager _absoluteScaleThresholdBeforeFullSizeForGestureRecognizer:];
-[SBSystemNotesInteractionManager _cancelGestureIfNecessary:reason:];
-[SBSystemNotesInteractionManager _convertReferenceVelocity:toOrientation:];
-[SBSystemNotesInteractionManager _cornerDistanceBeforeScalingForDismissGestureRecognizer:];
-[SBSystemNotesInteractionManager _cornerForGestureRecognizer:];
-[SBSystemNotesInteractionManager _cornersForAllSwipes];
-[SBSystemNotesInteractionManager _cornersForTouchType:];
-[SBSystemNotesInteractionManager _flickVelocityThresholdForGestureRecognizer:];
-[SBSystemNotesInteractionManager _gestureIsActive];
-[SBSystemNotesInteractionManager _gestureSettingsForRecognizer:];
-[SBSystemNotesInteractionManager _handleInteractiveSwipeInGesture:];
-[SBSystemNotesInteractionManager _handleInteractiveSystemNotesGesture:];
-[SBSystemNotesInteractionManager _handleNonInteractiveSwipeInGesture:];
-[SBSystemNotesInteractionManager _interactionController:updateScaleInteractorForSwipeToDismiss:pipSize:forPanGesture:];
-[SBSystemNotesInteractionManager _interactionController:updateScaleInteractorForSwipeToPresent:pipSize:forPanGesture:];
-[SBSystemNotesInteractionManager _isSystemNotesForegroundActive];
-[SBSystemNotesInteractionManager _orientedLocationForReferenceLocation:];
-[SBSystemNotesInteractionManager _panDistanceBeforeScalingForGestureRecognizer:];
-[SBSystemNotesInteractionManager _panDistancePer1xScalingForGestureRecognizer:];
-[SBSystemNotesInteractionManager _panInitialThumbnailScaleForGestureRecognizer:];
-[SBSystemNotesInteractionManager _panRecognizerOverFlickThreshold:];
-[SBSystemNotesInteractionManager _pointForGestureCorner:];
-[SBSystemNotesInteractionManager _presentationModeForGestureBegin];
-[SBSystemNotesInteractionManager _scaleThresholdBeforeFullSizeForGestureRecognizer:];
-[SBSystemNotesInteractionManager _setupFingerGestureRecognizers];
-[SBSystemNotesInteractionManager _setupForInteractiveDismissal];
-[SBSystemNotesInteractionManager _setupPencilGestureRecognizers];
-[SBSystemNotesInteractionManager _shouldEdgeProtectGestureRecognizer:];
-[SBSystemNotesInteractionManager _springBoardBootCompleted:];
-[SBSystemNotesInteractionManager _updateFailureRequirements];
-[SBSystemNotesInteractionManager _updateFingerGestureEnablement];
-[SBSystemNotesInteractionManager _updateStashPadding];
-[SBSystemNotesInteractionManager canHandlePresentationRequests:];
-[SBSystemNotesInteractionManager contentContainerAdapter:willBeginInteractionWithGestureRecognizer:];
-[SBSystemNotesInteractionManager contentContainerAdapter:willUpdateStashState:];
-[SBSystemNotesInteractionManager contentContainerAdapterDidEndInteraction:targetWindowScene:];
-[SBSystemNotesInteractionManager contentContainerAdapterPanGestureDidEnd:];
-[SBSystemNotesInteractionManager contentContainerAdapterShouldUpdateUIForStashing:];
-[SBSystemNotesInteractionManager currentCornerRadiusForInteractionController:];
-[SBSystemNotesInteractionManager defaultPositionHyperregionComposers];
-[SBSystemNotesInteractionManager initWithWindowScene:systemGestureManager:systemPointerInteractionManager:pictureInPictureCoordinator:dataSource:delegate:];
-[SBSystemNotesInteractionManager initialStashStateForContentContainerAdapter:];
-[SBSystemNotesInteractionManager interactionController:edgeInsetsForWindowScene:];
-[SBSystemNotesInteractionManager interactionController:stashedPaddingForWindowScene:];
-[SBSystemNotesInteractionManager interactionController:updateScaleInteractor:pipSize:forPanGesture:];
-[SBSystemNotesInteractionManager interactionControllerConnectedWindowScenes:];
-[SBSystemNotesInteractionManager interactionControllerIsExternalPanGestureRecognizing:];
-[SBSystemNotesInteractionManager interactionControllerScalesDuringPanGesture:];
-[SBSystemNotesInteractionManager peepAnimated:];
-[SBSystemNotesInteractionManager shouldPointerInteractionBeginForInteractionController:atLocation:inView:];
-[SBSystemNotesInteractionManager startingPositionForExternalPresentationRequest];
-[SBSystemNotesInteractionManager systemGestureManagerForInteractionControllerResizing:];
-[SBSystemNotesInteractionManager systemPointerInteractionManagerForInteractionController:];
```
