# `SBSASettlingBehaviorProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 10 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"SBSAElementLayoutTransition" _lastChangingElementLayoutTransition;
q _activePhase;
@"NSDictionary" _containerIDsToOvershootOutsets;
@"NSSet" _pendingPhaseTransitionPropertyIdentities;
@"NSSet" _pendingCollisionPropertyIdentities;
@"NSSet" _pendingSteadyPropertyIdentities;
@"NSDictionary" _stackContainerInterfaceElementIdentifiersToBounds;
B _collisionImminent;
B _collisionIsNotOvershooting;
@"NSMutableDictionary" _heldCollisionContainerDescriptions;
```

## Class methods

```
+[SBSASettlingBehaviorProvider initialize];
```

## Instance methods

```
-[SBSASettlingBehaviorProvider encodeWithCoder:];
-[SBSASettlingBehaviorProvider membersForCoder];
-[SBSASettlingBehaviorProvider _currentContainersAreAtInertFrameInContext:];
-[SBSASettlingBehaviorProvider _fluidBehaviorSettingsForTransitionPhase:forElementContext:];
-[SBSASettlingBehaviorProvider _overshootFractionForDampingRatio:];
-[SBSASettlingBehaviorProvider _overshootOutsetsForTransitionPhase:baseOutsets:elementContext:context:];
-[SBSASettlingBehaviorProvider _overshootOutsetsTargetingContainerDescription:initialContainerDescription:settings:context:];
-[SBSASettlingBehaviorProvider _progressMilestoneForTransitionPhase:];
-[SBSASettlingBehaviorProvider _resetSettlingState];
-[SBSASettlingBehaviorProvider _setActivePhase:context:logReason:];
-[SBSASettlingBehaviorProvider preferencesFromContext:];
```
