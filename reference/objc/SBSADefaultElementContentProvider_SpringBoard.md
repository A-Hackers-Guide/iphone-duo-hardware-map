# `SBSADefaultElementContentProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 4 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"SBSAIndicatorElementDescription" _indicatorElementDescription;
@"NSMutableDictionary" _identifiersToBlankingRegionElementDescriptions;
@"NSMutableDictionary" _identifiersToElementDescriptions;
B _wasAnimating;
```

## Class methods

```
+[SBSADefaultElementContentProvider initialize];
```

## Instance methods

```
-[SBSADefaultElementContentProvider defaultTransitionSettings];
-[SBSADefaultElementContentProvider membersForCoder];
-[SBSADefaultElementContentProvider _pruneElementDescriptionWithIdentifier:];
-[SBSADefaultElementContentProvider _updateElementDescriptionsWithDescription:];
-[SBSADefaultElementContentProvider _updatedBlankingRegionElementDescriptionForContext:transitionDescriptions:context:updateReasons:];
-[SBSADefaultElementContentProvider _updatedElementDescriptionAssociatedWithElementContext:transitionDescriptions:context:updateReasons:];
-[SBSADefaultElementContentProvider _updatedElementDescriptionFromDescription:associatedElementContext:associatedSnapshotContext:transitionDescriptions:context:updateReasons:];
-[SBSADefaultElementContentProvider _updatedIndicatorElementDescriptionFromDescription:associatedElementIdentity:transitionDescriptions:context:updateReasons:];
-[SBSADefaultElementContentProvider preferencesFromContext:];
```
