# `SBDuoDisplaySystemUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- 6 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _presentedSceneIdentifiers;
@"NSMutableArray" _suppressSystemGesturesAssertions;
@"NSMutableArray" _suppressSystemApertureAssertions;
@"NSMutableArray" _systemUISceneContentAssertions;
@"<BSInvalidatable>" _disableIdleTimerAssertion;
d _hingeAngleDegreesBeforePin;
```

## Class methods

```
+[SBDuoDisplaySystemUISceneController _setupInfo];
```

## Instance methods

```
-[SBDuoDisplaySystemUISceneController initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBDuoDisplaySystemUISceneController scenePresenter:willDismissScene:];
-[SBDuoDisplaySystemUISceneController scenePresenter:didPresentScene:];
-[SBDuoDisplaySystemUISceneController _isDefaultPresenterDelegate];
-[SBDuoDisplaySystemUISceneController _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
-[SBDuoDisplaySystemUISceneController _acquireDeviceAssertions];
-[SBDuoDisplaySystemUISceneController _releaseDeviceAssertions];
-[SBDuoDisplaySystemUISceneController _setDevicePosePinned:];
```
