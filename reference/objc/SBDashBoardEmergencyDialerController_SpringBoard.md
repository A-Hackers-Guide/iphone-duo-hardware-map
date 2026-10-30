# `SBDashBoardEmergencyDialerController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`, `CSEmergencyCalling`, `SBLockScreenCallHandling`
- 2 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBDashBoardEmergencyDialerViewController" _emergencyDialerViewController;
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
-[SBDashBoardEmergencyDialerController dealloc];
-[SBDashBoardEmergencyDialerController settings:changedValueForKey:];
-[SBDashBoardEmergencyDialerController initWithWindowScene:];
-[SBDashBoardEmergencyDialerController isMakingEmergencyCall];
-[SBDashBoardEmergencyDialerController launchEmergencyDialer];
-[SBDashBoardEmergencyDialerController emergencyDialerExitedWithError:];
-[SBDashBoardEmergencyDialerController exitEmergencyDialerAnimated:];
-[SBDashBoardEmergencyDialerController launchEmergencyDialerAnimated:];
```
