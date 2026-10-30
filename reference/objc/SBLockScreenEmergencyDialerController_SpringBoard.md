# `SBLockScreenEmergencyDialerController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLockScreenEmergencyCallViewControllerDelegate`
- 3 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenEmergencyCallViewController" _viewController;
B _active;
@"<SBLockScreenEmergencyDialerDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N,GisActive,V_active) active;
@property (T@"UIViewController",R,N,V_viewController) viewController;
@property (T@"<SBLockScreenEmergencyDialerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenEmergencyDialerController activateWithCompletion:];
-[SBLockScreenEmergencyDialerController deactivate];
-[SBLockScreenEmergencyDialerController viewController];
-[SBLockScreenEmergencyDialerController setDelegate:];
-[SBLockScreenEmergencyDialerController delegate];
-[SBLockScreenEmergencyDialerController isActive];
-[SBLockScreenEmergencyDialerController dismissEmergencyCallViewController:];
-[SBLockScreenEmergencyDialerController emergencyCallViewController:didExitWithError:];
```
