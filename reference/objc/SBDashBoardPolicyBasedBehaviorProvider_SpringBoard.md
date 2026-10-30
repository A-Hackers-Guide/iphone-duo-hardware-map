# `SBDashBoardPolicyBasedBehaviorProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalBehaviorProviding`
- 3 instance variables, 10 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBPolicyAggregator" _policyAggregator;
@ _notificationToken;
```

## Properties

```
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBDashBoardPolicyBasedBehaviorProvider conformsToCSBehaviorProviding];
-[SBDashBoardPolicyBasedBehaviorProvider dealloc];
-[SBDashBoardPolicyBasedBehaviorProvider proximityDetectionMode];
-[SBDashBoardPolicyBasedBehaviorProvider scrollingStrategy];
-[SBDashBoardPolicyBasedBehaviorProvider notificationBehavior];
-[SBDashBoardPolicyBasedBehaviorProvider conformsToCSExternalBehaviorProviding];
-[SBDashBoardPolicyBasedBehaviorProvider coverSheetIdentifier];
-[SBDashBoardPolicyBasedBehaviorProvider participantState];
-[SBDashBoardPolicyBasedBehaviorProvider restrictedCapabilities];
-[SBDashBoardPolicyBasedBehaviorProvider _restrictedCapability:forAggregatorCapability:];
-[SBDashBoardPolicyBasedBehaviorProvider initWithCoverSheetViewController:policyAggregator:];
```
