# `SBCaptureButtonAppConfigurationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSCaptureButtonAppConfigurationServerDelegate`, `SBCaptureApplicationCenterObserver`, `SBCaptureButtonAppConfigurationProviding`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"SBCaptureButtonDefaults" _captureButtonDefaults;
@"SBSCaptureButtonAppConfigurationServer" _server;
@"<BSInvalidatable>" _captureApplicationLaunchActionsAssertion;
@"NSString" _associatedAppBundleIdentifier;
@"NSSet" _eligibleApps;
```

## Properties

```
@property (T@"NSString",C,N,S_setAssociatedAppBundleIdentifier:,V_associatedAppBundleIdentifier) associatedAppBundleIdentifier;
@property (T@"NSSet",C,N,S_setEligibleApps:,V_eligibleApps) eligibleApps;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureButtonAppConfigurationCoordinator associatedAppBundleIdentifier];
-[SBCaptureButtonAppConfigurationCoordinator removeObserver:];
-[SBCaptureButtonAppConfigurationCoordinator init];
-[SBCaptureButtonAppConfigurationCoordinator addObserver:];
-[SBCaptureButtonAppConfigurationCoordinator captureButtonAppConfigurationServer:setCurrentAssociatedAppUsingBundleIdentifier:];
-[SBCaptureButtonAppConfigurationCoordinator eligibleApps];
-[SBCaptureButtonAppConfigurationCoordinator _reevaluateCurrentAssociatedApp];
-[SBCaptureButtonAppConfigurationCoordinator _notifyObserversOfConfigurationUpdates];
-[SBCaptureButtonAppConfigurationCoordinator _setAssociatedAppBundleIdentifier:];
-[SBCaptureButtonAppConfigurationCoordinator _setAssociatedAppBundleIdentifier:shouldPersistToDefaults:];
-[SBCaptureButtonAppConfigurationCoordinator _setAssociatedAppBundleIdentifierFromDefaults];
-[SBCaptureButtonAppConfigurationCoordinator _setEligibleApps:];
-[SBCaptureButtonAppConfigurationCoordinator _updateLaunchActionsAssertionForAssociatedAppBundleIdentifier:];
-[SBCaptureButtonAppConfigurationCoordinator captureApplicationCenter:didUpdateKnownApplications:];
```
