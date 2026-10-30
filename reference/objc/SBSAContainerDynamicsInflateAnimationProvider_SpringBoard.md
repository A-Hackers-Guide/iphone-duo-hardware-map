# `SBSAContainerDynamicsInflateAnimationProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 4 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _elementIdentitiesWithInflateApplied;
@"NSMapTable" _pendingMilestonePropertyIdentitiesToElementIdentities;
@"NSMutableSet" _elementIdentitiesWaitingToExpandBeforeInflation;
@"NSMutableSet" _elementIdentitiesThatFinishedWaitingToExpandBeforeInflation;
```

## Class methods

```
+[SBSAContainerDynamicsInflateAnimationProvider initialize];
```

## Instance methods

```
-[SBSAContainerDynamicsInflateAnimationProvider encodeWithCoder:];
-[SBSAContainerDynamicsInflateAnimationProvider membersForCoder];
-[SBSAContainerDynamicsInflateAnimationProvider _addMilestonesIfNecessaryForUntrackedBoundsExpansionsForElementIdentities:preferencesMutator:context:];
-[SBSAContainerDynamicsInflateAnimationProvider _identitiesWithMilestoneReached:];
-[SBSAContainerDynamicsInflateAnimationProvider preferencesFromContext:];
```
