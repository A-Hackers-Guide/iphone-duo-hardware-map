# `SBProximityReaderUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `SBBarSwipeAffordanceControllingDelegate`, `SBBarSwipeAffordanceDelegate`, `SBBarSwipeAffordanceObserver`, `SBHomeGrabberPointerClickDelegate`, `SBFProximityReaderBlockProvider`
- 13 instance variables, 4 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"<BSInvalidatable>" _suppressSystemGesturesAssertion;
@"<BSInvalidatable>" _bannerSuppressionAssertion;
@"<BSInvalidatable>" _suppressSystemApertureAssertion;
@"UIApplicationSceneDeactivationAssertion" _sceneDeactivationAssertion;
@"<BSInvalidatable>" _captureButtonSuppressionAssertion;
B _presenting;
@"NSHashTable" _observers;
@"SBFDeviceLockOutController" _lockOutController;
@"SBSUIStatusBarSceneHostComponent" _statusBarComponent;
@"SBSUIFeaturePolicyHostComponent" _featurePolicyComponent;
@"SBSUIIdleTimerSceneHostComponent" _idleTimerComponent;
@"NSMutableSet" _handlingBackgroundActivities;
@"SBBarSwipeAffordanceViewController" _homeAffordanceViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBProximityReaderUISceneController _setupInfo];
```

## Instance methods

```
-[SBProximityReaderUISceneController initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBProximityReaderUISceneController willEnableSecureRendering:];
-[SBProximityReaderUISceneController homeGrabberViewDidReceiveClick:];
-[SBProximityReaderUISceneController zStackParticipant:updatePreferences:];
-[SBProximityReaderUISceneController barSwipeAffordanceView:systemGestureTypeForType:];
-[SBProximityReaderUISceneController dealloc];
-[SBProximityReaderUISceneController scenePresenter:willDismissScene:];
-[SBProximityReaderUISceneController handleLockButtonPress];
-[SBProximityReaderUISceneController zStackParticipantDidChange:];
-[SBProximityReaderUISceneController homeGesturePerformedForBarSwipeAffordanceView:];
-[SBProximityReaderUISceneController scenePresenter:didPresentScene:];
-[SBProximityReaderUISceneController _isDefaultPresenterDelegate];
-[SBProximityReaderUISceneController _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
-[SBProximityReaderUISceneController handleHomeButtonPress];
-[SBProximityReaderUISceneController addProximityReaderObserver:];
-[SBProximityReaderUISceneController isProximityReaderBlocked];
-[SBProximityReaderUISceneController removeProximityReaderObserver:];
-[SBProximityReaderUISceneController _addHandlingBackgroundActivity:];
-[SBProximityReaderUISceneController _handleActionForHomeAffordanceView:];
-[SBProximityReaderUISceneController _isHandlingBackgroundActivity:];
-[SBProximityReaderUISceneController _removeHandlingBackgroundActivity:];
-[SBProximityReaderUISceneController _updateHomeAffordance:window:];
-[SBProximityReaderUISceneController handleBackgroundActivity:handler:];
-[SBProximityReaderUISceneController scenePresenter:updateHomeAffordance:forScene:];
-[SBProximityReaderUISceneController setDefaultPresenter:];
```
