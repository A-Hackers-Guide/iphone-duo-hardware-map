# `SBSADefaultContainerLayoutProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 4 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"SBSAContainerViewDescription" _indicatorContainerDescription;
@"NSMutableDictionary" _blankingRegionContainerDescriptionsByRegionIdentifier;
@"NSMutableArray" _orderedContainerDescriptions;
@"SBSAViewDescription" _fixedSensorMatchMoveSourceViewDescription;
```

## Class methods

```
+[SBSADefaultContainerLayoutProvider initialize];
```

## Instance methods

```
-[SBSADefaultContainerLayoutProvider defaultTransitionSettings];
-[SBSADefaultContainerLayoutProvider membersForCoder];
-[SBSADefaultContainerLayoutProvider _indexOfContainerViewDescriptionWithIdentifier:];
-[SBSADefaultContainerLayoutProvider _pruneContainerDescriptionWithIdentifier:];
-[SBSADefaultContainerLayoutProvider _shouldHideContainerAtRestInContext:];
-[SBSADefaultContainerLayoutProvider _updateContainerDescriptionAtIndex:transitionDescriptions:context:updateReason:];
-[SBSADefaultContainerLayoutProvider _updateContainerViewDescriptionInCollection:];
-[SBSADefaultContainerLayoutProvider _updatedContainerViewDescription:transitionDescriptions:context:];
-[SBSADefaultContainerLayoutProvider _updatedFixedIndicatorViewDescription:transitionDescriptions:context:];
-[SBSADefaultContainerLayoutProvider behaviorSettingsForProperty:];
-[SBSADefaultContainerLayoutProvider preferencesFromContext:];
```
