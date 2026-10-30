# `SBSAEjectStretchBehaviorProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 3 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
q _phase;
@"NSUUID" _identifierOfActiveTimer;
@"SBSAInterfaceElementPropertyIdentity" _pendingCollapsePropertyIdentity;
```

## Class methods

```
+[SBSAEjectStretchBehaviorProvider initialize];
```

## Instance methods

```
-[SBSAEjectStretchBehaviorProvider membersForCoder];
-[SBSAEjectStretchBehaviorProvider _startTimerIfNecessary:context:];
-[SBSAEjectStretchBehaviorProvider _checkContextForExpiredContractionMilestone:];
-[SBSAEjectStretchBehaviorProvider _isTimerExpired:];
-[SBSAEjectStretchBehaviorProvider preferencesFromContext:];
```
