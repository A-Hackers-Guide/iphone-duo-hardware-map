# `SBLibraryViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHLibraryViewController`
- Protocols: `SBHLibraryViewControllerObserver`, `SBBarSwipeAffordanceObserver`, `SBBarSwipeAffordanceDelegate`, `SBBarSwipeAffordanceControllingDelegate`, `SBLayoutStateTransitionObserver`, `BSInvalidatable`
- 8 instance variables, 13 properties, 56 instance methods, 0 class methods

## Instance variables

```
B _rotating;
B _invalidated;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarSettingsAssertion;
@"SBAsynchronousRenderingAssertion" _asynchronousRenderingAssertion;
@"<BSInvalidatable>" _expandedPodDisplayLayoutElementAssertion;
@"<BSInvalidatable>" _useSnapshotAsBackgroundViewAssertion;
@"SBWindowScene" _windowScene;
@"ATXAppDirectoryClient" _loggingClient;
```

## Properties

```
@property (T@"SBBarSwipeAffordanceViewController",&,D,N) barSwipeViewController;
@property (T@"SBWindowSceneStatusBarSettingsAssertion",&,N,V_statusBarSettingsAssertion) statusBarSettingsAssertion;
@property (T@"SBAsynchronousRenderingAssertion",&,N,V_asynchronousRenderingAssertion) asynchronousRenderingAssertion;
@property (T@"<BSInvalidatable>",&,N,V_expandedPodDisplayLayoutElementAssertion) expandedPodDisplayLayoutElementAssertion;
@property (T@"<BSInvalidatable>",&,N,V_useSnapshotAsBackgroundViewAssertion) useSnapshotAsBackgroundViewAssertion;
@property (TB,N,GisRotating,V_rotating) rotating;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (T@"ATXAppDirectoryClient",R,N,V_loggingClient) loggingClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLibraryViewController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBLibraryViewController _setStatusBarSettingsAssertionActive:];
-[SBLibraryViewController setAsynchronousRenderingAssertion:];
-[SBLibraryViewController loggingClient];
-[SBLibraryViewController libraryViewController:didPresentSearchController:];
-[SBLibraryViewController libraryViewController:didDismissSearchController:];
-[SBLibraryViewController zStackParticipant:updatePreferences:];
-[SBLibraryViewController _setExpandedPodDisplayLayoutElementActive:];
-[SBLibraryViewController setPresenter:];
-[SBLibraryViewController libraryViewController:willPresentFolderController:];
-[SBLibraryViewController pressesCancelled:withEvent:];
-[SBLibraryViewController barSwipeAffordanceView:systemGestureTypeForType:];
-[SBLibraryViewController pressesEnded:withEvent:];
-[SBLibraryViewController libraryViewControllerDidPresent:];
-[SBLibraryViewController _canHandleKeyEvents];
-[SBLibraryViewController dealloc];
-[SBLibraryViewController initWithCategoryMapProvider:windowScene:];
-[SBLibraryViewController setUseSnapshotAsBackgroundViewAssertion:];
-[SBLibraryViewController libraryViewController:willDismissSearchController:];
-[SBLibraryViewController _evaluateFirstResponderStatus];
-[SBLibraryViewController _acquireUseSnapshotAsBackgroundViewAssertionIfNecessary];
-[SBLibraryViewController zStackParticipantDidChange:];
-[SBLibraryViewController _evaluateAsyncRenderingAssertion];
-[SBLibraryViewController libraryViewControllerWillPresent:];
-[SBLibraryViewController libraryViewControllerDidDismiss:];
-[SBLibraryViewController homeGesturePerformedForBarSwipeAffordanceView:];
-[SBLibraryViewController statusBarSettingsAssertion];
-[SBLibraryViewController isInvalidated];
-[SBLibraryViewController asynchronousRenderingAssertion];
-[SBLibraryViewController setInvalidated:];
-[SBLibraryViewController overlayController:didChangePresentationProgress:newPresentationProgress:fromLeading:];
-[SBLibraryViewController pressesBegan:withEvent:];
-[SBLibraryViewController pressesChanged:withEvent:];
-[SBLibraryViewController invalidate];
-[SBLibraryViewController libraryViewController:willDismissFolderController:];
-[SBLibraryViewController _canHandleKeyUIEvent:];
-[SBLibraryViewController _didActivateTypeAheadSearchWithPhysicalKeyboardEvent:];
-[SBLibraryViewController _sbWindowScene];
-[SBLibraryViewController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBLibraryViewController userInterfaceStyleDidChange];
-[SBLibraryViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBLibraryViewController _currentLayoutState];
-[SBLibraryViewController _handlePressesBegan:];
-[SBLibraryViewController _isPresentationForegroundModal];
-[SBLibraryViewController isRotating];
-[SBLibraryViewController setRotating:];
-[SBLibraryViewController _setStatusBarSettingsAssertionActive:quickly:];
-[SBLibraryViewController _evaluateAffordanceActivation];
-[SBLibraryViewController keyboardHomeAffordanceAssertionForBarSwipeAffordanceControlling:];
-[SBLibraryViewController setStatusBarSettingsAssertion:];
-[SBLibraryViewController libraryViewControllerWillDismiss:];
-[SBLibraryViewController useSnapshotAsBackgroundViewAssertion];
-[SBLibraryViewController windowScene];
-[SBLibraryViewController canBecomeFirstResponder];
-[SBLibraryViewController setExpandedPodDisplayLayoutElementAssertion:];
-[SBLibraryViewController expandedPodDisplayLayoutElementAssertion];
```
