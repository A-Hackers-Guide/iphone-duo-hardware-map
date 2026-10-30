# `SBSystemNotesManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemNotesPresentationRequestServerDelegate`, `SBSystemNotesInteractionManagerDataSource`, `SBSystemNotesInteractionManagerDelegate`, `SBSystemNotesContentViewControllerDelegate`, `PTSettingsKeyPathObserver`, `SBSSystemNotesPresentationClientToServerInterface`, `MCProfileConnectionObserver`
- 28 instance variables, 4 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"FBSSceneSpecification" _sceneSpecification;
@"NSString" _launchBundleID;
@"SBPIPController" _pipController;
@"SBPIPSceneContentAdapter" _sceneContentAdapter;
@"SBApplicationController" _applicationController;
@"SBSceneManager" _sceneManager;
@"SBWindowScene" _windowScene;
@"FBSceneManager" _fbSceneManager;
@"SBSystemNotesPresentationRequestServer" _systemNotesRequestServer;
@"PTTestRecipe" _systemNotesTestRecipe;
@"SBMainWorkspace" _workspace;
@"SBSystemNotesSettings" _pipSettings;
@"SBKeyboardSuppressionManager" _keyboardSuppressionManager;
@"SBSystemNotesInteractionManager" _interactionManager;
@"SBKeyboardDismissalManager" _keyboardDismissalManager;
@"SBPIPContentViewLayoutSettings" _contentViewLayoutSettings;
@"__UIKeyboardArbiterManager" _keyboardArbiterManager;
@"UIApplicationSceneDeactivationManager" _sceneDeactivationManager;
@"BSServiceConnection" _presentedConnection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _lock_connections;
@"<BSInvalidatable>" _pegasusWindowLevelAssertion;
@"BSAbsoluteMachTimer" _interactionLoggingTimer;
Q _interactionRequests;
@"MCProfileConnection" _managedProfileConnection;
@"NSCountedSet" _displaysWithPendingScreenshots;
@"NSMutableDictionary" _displaysToScreenshotFlashWindows;
@"SBPIPSceneContentContainerAdapter" _presentedContainerAdapter;
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
-[SBSystemNotesManager profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[SBSystemNotesManager dealloc];
-[SBSystemNotesManager settings:changedValueForKeyPath:];
-[SBSystemNotesManager activateConfiguration:];
-[SBSystemNotesManager presentWithConfiguration:completion:];
-[SBSystemNotesManager server:connectionDidInvalidate:];
-[SBSystemNotesManager _addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:animated:];
-[SBSystemNotesManager _createContentViewControllerForPresentationContext:error:];
-[SBSystemNotesManager _currentPresentationMode];
-[SBSystemNotesManager _dismissNotesWithReason:];
-[SBSystemNotesManager _dismissNotesWithReason:animated:];
-[SBSystemNotesManager _handleCreateNoteRequestWithMode:presentationSource:];
-[SBSystemNotesManager _handleCreateNoteRequestWithPresentationContext:error:];
-[SBSystemNotesManager _presentedContainerViewController];
-[SBSystemNotesManager _presentedNotesContentViewController];
-[SBSystemNotesManager _reloadLaunchBundleID];
-[SBSystemNotesManager _sceneBundleIdentifierForNewConfiguration];
-[SBSystemNotesManager _sceneHandleForApplication:sceneSpecification:];
-[SBSystemNotesManager _setPresentedConnection:];
-[SBSystemNotesManager _tearDownContainerViewControllerForSceneHandle:];
-[SBSystemNotesManager contentViewController:didChangeToPresentationMode:];
-[SBSystemNotesManager contentViewController:didReceiveScreenshotRequestForDisplays:completion:];
-[SBSystemNotesManager contentViewControllerDidReceiveTapToExpand:];
-[SBSystemNotesManager contentViewControllerWantsDismissal:forReason:animated:];
-[SBSystemNotesManager currentContentViewLayoutSettingsForInteractionManager:];
-[SBSystemNotesManager currentPresentationModeForInteractionManager:];
-[SBSystemNotesManager initWithControllerCoordinator:workspace:sceneManager:windowScene:keyboardArbiterManager:fbSceneManager:sceneDeactivationManager:keyboardSuppressionManager:keyboardDismissalManager:applicationController:systemGestureManager:systemPointerInteractionManager:idleTimerCoordinator:managedProfileConnection:];
-[SBSystemNotesManager interactionManager:requestsNotesDismissalForSource:animated:];
-[SBSystemNotesManager interactionManager:requestsPresentationWithContext:];
-[SBSystemNotesManager interactionManager:requestsStartSuppressingKeyboardForReason:];
-[SBSystemNotesManager interactionManager:requestsStashAssertionForReason:];
-[SBSystemNotesManager interactionManager:requestsStopSuppressingKeyboardForReason:];
-[SBSystemNotesManager interactionManager:requestsUpdatePresentationMode:];
-[SBSystemNotesManager launchApplicationIdentityForInteractionManager:];
-[SBSystemNotesManager launchBundleIDForInteractionManager:];
-[SBSystemNotesManager presentedContainerViewControllerForInteractionManager:];
-[SBSystemNotesManager presentedPIPContentViewControllerForInteractionManager:];
-[SBSystemNotesManager server:targetForNewClientConnection:];
-[SBSystemNotesManager showOrHideForKeyCommand:];
```
