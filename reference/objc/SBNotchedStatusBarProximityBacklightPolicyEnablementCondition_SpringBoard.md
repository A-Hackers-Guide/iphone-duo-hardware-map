# `SBNotchedStatusBarProximityBacklightPolicyEnablementCondition`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneStatusBarAssertionManagerObserver`, `SBSceneManagerObserver`, `SBDeviceApplicationSceneHandleObserver`, `UIStatusBarServerClient`, `SBUIActiveOrientationObserver`, `BSInvalidatable`
- 11 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"SpringBoard" _orientationProvider;
@"UIStatusBarServer" _statusBarConnection;
@"SBWindowSceneStatusBarManager" _windowSceneStatusBarManager;
@"SBWindowSceneStatusBarAssertionManager" _statusBarAssertionManager;
@"SBSceneManager" _sceneManager;
@"UIApplicationSceneSettingsDiffInspector" _applicationSceneSettingsDiffInspector;
@"NSSet" _currentBackgroundActivityIdentifiers;
@"<SBNotchedStatusBarProximityBacklightPolicyEnablementConditionDelegate>" _delegate;
d _statusBarHeight;
B _isEnabled;
B _invalidated;
```

## Properties

```
@property (T@"<SBNotchedStatusBarProximityBacklightPolicyEnablementConditionDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisEnabled,V_isEnabled) enabled;
@property (Td,R,N,V_statusBarHeight) enabledStatusBarHeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition sceneManager:didAddExternalForegroundApplicationSceneHandle:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition sceneManager:didRemoveExternalForegroundApplicationSceneHandle:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition init];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition dealloc];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition statusBarServer:didReceiveGlowAnimationState:forStyle:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition activeInterfaceOrientationWillChangeToOrientation:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition isEnabled];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition invalidate];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition setDelegate:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition statusBarAssertionManager:statusBarSettingsDidChange:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition delegate];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition statusBarServer:didReceiveDoubleHeightStatusString:forStyle:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition statusBarServer:didReceiveStatusBarData:withActions:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition _evaluateEnablement];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition statusBarServer:didReceiveStyleOverrides:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition _setEnabled:statusBarHeight:];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition enabledStatusBarHeight];
-[SBNotchedStatusBarProximityBacklightPolicyEnablementCondition initWithSceneManager:windowSceneStatusBarManager:statusBarServer:orientationProvider:];
```
