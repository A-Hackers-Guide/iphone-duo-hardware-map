# `SBDashBoardIdleTimerController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalEventHandling`, `SBLockScreenIdleTimerCoordinatorObserving`, `CSIdleTimerControlling`, `SBLockScreenIdleTimerControlling`
- 1 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"CSCoverSheetViewController" _coverSheetViewController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBDashBoardIdleTimerController handleEvent:];
-[SBDashBoardIdleTimerController wouldHandleButtonEvent:];
-[SBDashBoardIdleTimerController _idleTimerCoordinator];
-[SBDashBoardIdleTimerController idleTimerDidRefresh:];
-[SBDashBoardIdleTimerController dealloc];
-[SBDashBoardIdleTimerController idleTimerDidExpire:];
-[SBDashBoardIdleTimerController conformsToCSEventHandling];
-[SBDashBoardIdleTimerController coverSheetIdentifier];
-[SBDashBoardIdleTimerController idleTimerDidWarn:];
-[SBDashBoardIdleTimerController participantState];
-[SBDashBoardIdleTimerController addIdleTimerDisabledAssertionReason:];
-[SBDashBoardIdleTimerController removeIdleTimerDisabledAssertionReason:];
-[SBDashBoardIdleTimerController resetIdleTimerIfTopMost];
-[SBDashBoardIdleTimerController idleTimerBehaviorProvider];
-[SBDashBoardIdleTimerController idleTimerDidChange:];
-[SBDashBoardIdleTimerController idleTimerWillRefresh:];
-[SBDashBoardIdleTimerController initWithCoverSheetViewController:];
-[SBDashBoardIdleTimerController updateIdleTimerBehaviorWithReason:];
```
