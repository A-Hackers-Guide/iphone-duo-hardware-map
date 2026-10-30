# `SBDashBoardEmergencyDialerViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHomeGestureDismissableCoverSheetViewController`
- Protocols: `SBLockScreenEmergencyDialerDelegate`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"TUCallCenter" _callCenter;
@"SBLockScreenEmergencyDialerController" _controller;
B _inEmergencyCall;
B _inEmergencyCallMode;
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
-[SBDashBoardEmergencyDialerViewController presentationType];
-[SBDashBoardEmergencyDialerViewController handleEvent:];
-[SBDashBoardEmergencyDialerViewController aggregateBehavior:];
-[SBDashBoardEmergencyDialerViewController dealloc];
-[SBDashBoardEmergencyDialerViewController presentationPriority];
-[SBDashBoardEmergencyDialerViewController viewDidLoad];
-[SBDashBoardEmergencyDialerViewController viewWillAppear:];
-[SBDashBoardEmergencyDialerViewController aggregateAppearance:];
-[SBDashBoardEmergencyDialerViewController viewDidDisappear:];
-[SBDashBoardEmergencyDialerViewController shouldAutomaticallyForwardAppearanceMethods];
-[SBDashBoardEmergencyDialerViewController _activateEmergencyDialerController];
-[SBDashBoardEmergencyDialerViewController _deactivateEmergencyDialerController];
-[SBDashBoardEmergencyDialerViewController _updateEmergencyCallMode:];
-[SBDashBoardEmergencyDialerViewController emergencyDialer:willDeactivateWithError:];
```
