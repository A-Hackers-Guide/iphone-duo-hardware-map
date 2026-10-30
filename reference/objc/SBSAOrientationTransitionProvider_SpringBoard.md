# `SBSAOrientationTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 5 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _renderedOrientation;
q _pendingOrientation;
q _previouslyObservedOrientation;
q _phase;
B _containersHiddenForCollapse;
```

## Class methods

```
+[SBSAOrientationTransitionProvider initialize];
```

## Instance methods

```
-[SBSAOrientationTransitionProvider membersForCoder];
-[SBSAOrientationTransitionProvider _adoptPendingOrientationInContext:];
-[SBSAOrientationTransitionProvider _collapseDidFinishInContext:];
-[SBSAOrientationTransitionProvider _endPhase];
-[SBSAOrientationTransitionProvider _preferencesByForcingUnanimatedTeleportInPreferences:];
-[SBSAOrientationTransitionProvider _preferencesByHoldingContainersHiddenInPreferences:];
-[SBSAOrientationTransitionProvider _preferencesByRequestingFollowingQueryForReason:inPreferences:];
-[SBSAOrientationTransitionProvider _updatePhaseForContext:];
-[SBSAOrientationTransitionProvider preferencesFromContext:];
```
