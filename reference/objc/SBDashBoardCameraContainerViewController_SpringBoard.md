# `SBDashBoardCameraContainerViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `CSHostableEntityPresenterDelegate`, `SBZStackForegroundScenePolicyAssistantDelegate`, `SBSystemApertureZStackPolicyAssistantDelegate`, `CSDismissableModalViewControllerDelegate`, `SBApplicationHosting`, `SBFZStackParticipantDelegate`, `BSInvalidatable`, `CSEntityHosting`, `CSHostableEntityContentContaining`
- 11 instance variables, 8 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"SBDashBoardTraitsOrientedContentViewController" _orientedContentViewController;
@"TRAParticipant" _traitsParticipant;
@"SBTraitsSceneParticipantDelegate" _traitsParticipantDelegate;
@"SBAudioCategoryZStackPolicyAssistant" _audioCategoryZStackPolicyAssistant;
@"SBPhysicalButtonZStackPolicyAssistant" _physicalButtonZStackPolicyAssistant;
@"SBSystemApertureZStackPolicyAssistant" _systemApertureZStackPolicyAssistant;
@"SBUIBiometricResource" _biometricResource;
@"<SBFAuthenticationAssertionProviding>" _authenticationAssertionProvider;
@"SBFAuthenticationAssertion" _sustainAuthenticationAssertion;
q _desiredContentModeBeforeWindowTransition;
@"CSHostedEntityViewController" _hostedEntityViewController;
```

## Properties

```
@property (T@"<CSHostableEntity>",&,N) hostedEntity;
@property (T@"CSHostedEntityViewController",R,N,V_hostedEntityViewController) hostedEntityViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BSInvalidatable>",?,&,N) entityPreservationToken;
@property (T@"NSSet",?,&,N) actionsToDeliver;
```

## Instance methods

```
-[SBDashBoardCameraContainerViewController addGrabberView:];
-[SBDashBoardCameraContainerViewController hostableEntityPresenter:didBeginHosting:];
-[SBDashBoardCameraContainerViewController hostableEntityPresenter:didEndHosting:];
-[SBDashBoardCameraContainerViewController hostedEntity];
-[SBDashBoardCameraContainerViewController conformsToCSApplicationHosting];
-[SBDashBoardCameraContainerViewController handleEvent:];
-[SBDashBoardCameraContainerViewController dismissForHomeButton];
-[SBDashBoardCameraContainerViewController wouldHandleButtonEvent:];
-[SBDashBoardCameraContainerViewController foregroundSceneZStackPolicyAssistantDidChange:forReason:];
-[SBDashBoardCameraContainerViewController zStackParticipant:updatePreferences:];
-[SBDashBoardCameraContainerViewController aggregateBehavior:];
-[SBDashBoardCameraContainerViewController dealloc];
-[SBDashBoardCameraContainerViewController viewDidLoad];
-[SBDashBoardCameraContainerViewController handlesRotationIndependentOfCoverSheet];
-[SBDashBoardCameraContainerViewController zStackParticipantDidChange:];
-[SBDashBoardCameraContainerViewController zStackParticipant:updateZOrderPreferences:];
-[SBDashBoardCameraContainerViewController initWithNibName:bundle:];
-[SBDashBoardCameraContainerViewController _traitsArbiter];
-[SBDashBoardCameraContainerViewController viewWillAppear:];
-[SBDashBoardCameraContainerViewController conformsToSBApplicationHosting];
-[SBDashBoardCameraContainerViewController invalidate];
-[SBDashBoardCameraContainerViewController handleBarSwipeHomeGesturePerformed];
-[SBDashBoardCameraContainerViewController aggregateAppearance:];
-[SBDashBoardCameraContainerViewController setHostedEntity:];
-[SBDashBoardCameraContainerViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBDashBoardCameraContainerViewController viewDidAppear:];
-[SBDashBoardCameraContainerViewController hostedAppSceneHandle];
-[SBDashBoardCameraContainerViewController canHostAnApp];
-[SBDashBoardCameraContainerViewController hostedAppSceneHandles];
-[SBDashBoardCameraContainerViewController aggregatePresentation:];
-[SBDashBoardCameraContainerViewController viewDidDisappear:];
-[SBDashBoardCameraContainerViewController _acquireTraitsParticipant];
-[SBDashBoardCameraContainerViewController conformsToCSEventHandling];
-[SBDashBoardCameraContainerViewController wantsDefaultModalDismissalBehavior];
-[SBDashBoardCameraContainerViewController _updateZStackPolicyAssistants];
-[SBDashBoardCameraContainerViewController isHostingAnApp];
-[SBDashBoardCameraContainerViewController hostedEntityViewController];
-[SBDashBoardCameraContainerViewController windowSceneForSystemApertureZStackPolicyAssistant:];
-[SBDashBoardCameraContainerViewController _handleWindowDetachmentIfNeeded];
-[SBDashBoardCameraContainerViewController _handleWindowAttachmentForWindow:];
-[SBDashBoardCameraContainerViewController _invalidateTraitsParticipant];
-[SBDashBoardCameraContainerViewController _referenceBoundsForBounds:];
-[SBDashBoardCameraContainerViewController _setPresenterNeedsZStackPreferencesUpdateWithReason:];
-[SBDashBoardCameraContainerViewController systemApertureZStackPolicyAssistantDidChange:];
```
