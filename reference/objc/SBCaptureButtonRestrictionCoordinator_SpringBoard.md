# `SBCaptureButtonRestrictionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCaptureButtonRestrictionServerDelegate`
- 6 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBCaptureButtonRestrictionServer" _xpcServer;
@"BSCompoundAssertion" _observers;
@"BSCompoundAssertion" _inhibitedAssertion;
@"SBCaptureButtonSOSRestriction" _restrictionForSOS;
@"SBCaptureButtonMCProfileRestriction" _restrictionForMCProfile;
@"SBCaptureButtonDisabledUserDefaultRestriction" _restrictionForUserDefault;
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
-[SBCaptureButtonRestrictionCoordinator inhibitCaptureButtonActionAssertionWithReason:];
-[SBCaptureButtonRestrictionCoordinator init];
-[SBCaptureButtonRestrictionCoordinator addObserver:];
-[SBCaptureButtonRestrictionCoordinator isCaptureButtonActionInhibited:];
-[SBCaptureButtonRestrictionCoordinator captureButtonSuppressionOptions];
-[SBCaptureButtonRestrictionCoordinator _notifyObserversCaptureButtonInhibitionDidChange];
-[SBCaptureButtonRestrictionCoordinator inhibitCaptureButtonActionAssertionWithReason:options:];
```
