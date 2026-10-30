# `SBCoverSheetSceneManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _performingSceneUpdate;
B _displayLayoutElementDesired;
@"UIWindow" _coverSheetWindow;
@"<BSInvalidatable>" _displayLayoutAssertion;
@"UIApplicationSceneDeactivationAssertion" _notificationCenterAssertion;
@"UIApplicationSceneDeactivationAssertion" _systemAnimationAssertion;
@"NSMutableArray" _pendingSceneUpdateBlocks;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
```

## Properties

```
@property (T@"<BSInvalidatable>",&,N,V_displayLayoutAssertion) displayLayoutAssertion;
@property (T@"UIApplicationSceneDeactivationAssertion",&,N,V_notificationCenterAssertion) notificationCenterAssertion;
@property (T@"UIApplicationSceneDeactivationAssertion",&,N,V_systemAnimationAssertion) systemAnimationAssertion;
@property (T@"NSMutableArray",&,N,V_pendingSceneUpdateBlocks) pendingSceneUpdateBlocks;
@property (TB,N,GisPerformingSceneUpdate,V_performingSceneUpdate) performingSceneUpdate;
@property (T@"<BSInvalidatable>",&,N,V_stateCaptureInvalidatable) stateCaptureInvalidatable;
@property (TB,N,G_isDisplayLayoutElementDesired,V_displayLayoutElementDesired) displayLayoutElementDesired;
@property (T@"UIWindow",W,N,V_coverSheetWindow) coverSheetWindow;
```

## Instance methods

```
-[SBCoverSheetSceneManager displayLayoutAssertion];
-[SBCoverSheetSceneManager _setDisplayLayoutElementActive:];
-[SBCoverSheetSceneManager dealloc];
-[SBCoverSheetSceneManager coverSheetWindow];
-[SBCoverSheetSceneManager setCoverSheetWindow:];
-[SBCoverSheetSceneManager setDisplayLayoutAssertion:];
-[SBCoverSheetSceneManager setDisplayLayoutElementDesired:];
-[SBCoverSheetSceneManager setNotificationCenterAssertion:];
-[SBCoverSheetSceneManager _isDisplayLayoutElementDesired];
-[SBCoverSheetSceneManager _performNextSceneUpdateBlock];
-[SBCoverSheetSceneManager _performSceneUpdateBlock:];
-[SBCoverSheetSceneManager _setSceneBackgrounded:suspendUnderLockEnvironment:];
-[SBCoverSheetSceneManager _updateDisplayLayoutElement];
-[SBCoverSheetSceneManager _updateForegroundScenesForNotificationCenter:];
-[SBCoverSheetSceneManager initWithCoverSheetWindow:];
-[SBCoverSheetSceneManager isPerformingSceneUpdate];
-[SBCoverSheetSceneManager noteActiveWindowSceneMayHaveChanged];
-[SBCoverSheetSceneManager noteWindowHiddenMayHaveChanged];
-[SBCoverSheetSceneManager notificationCenterAssertion];
-[SBCoverSheetSceneManager pendingSceneUpdateBlocks];
-[SBCoverSheetSceneManager setPendingSceneUpdateBlocks:];
-[SBCoverSheetSceneManager setPerformingSceneUpdate:];
-[SBCoverSheetSceneManager setStateCaptureInvalidatable:];
-[SBCoverSheetSceneManager setSystemAnimationAssertion:];
-[SBCoverSheetSceneManager stateCaptureInvalidatable];
-[SBCoverSheetSceneManager systemAnimationAssertion];
-[SBCoverSheetSceneManager updateForegroundScenesForCoverSheetAnimationActive:];
-[SBCoverSheetSceneManager updateSceneManagerForPresented:suspendUnderLockEnvironment:];
```
