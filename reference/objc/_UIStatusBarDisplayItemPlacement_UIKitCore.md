# `_UIStatusBarDisplayItemPlacement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarPrioritized`
- 9 instance variables, 9 properties, 21 instance methods, 2 class methods

## Instance variables

```
B _enabled;
q _priority;
@"_UIStatusBarIdentifier" _identifier;
@"NSHashTable" _excludedPlacements;
@"NSSet" _excludedRegionIdentifiers;
@"NSHashTable" _includedPlacements;
@"NSHashTable" _allRequiredPlacements;
@"NSHashTable" _anyRequiredPlacements;
@"NSDictionary" _itemInfo;
```

## Properties

```
@property (Tq,N,V_priority) priority;
@property (T@"_UIStatusBarIdentifier",R,C,N,V_identifier) identifier;
@property (T@"NSHashTable",R,C,N,V_excludedPlacements) excludedPlacements;
@property (T@"NSSet",R,C,N,V_excludedRegionIdentifiers) excludedRegionIdentifiers;
@property (T@"NSHashTable",R,C,N,V_includedPlacements) includedPlacements;
@property (T@"NSHashTable",R,C,N,V_allRequiredPlacements) allRequiredPlacements;
@property (T@"NSHashTable",R,C,N,V_anyRequiredPlacements) anyRequiredPlacements;
@property (T@"NSDictionary",R,C,N,V_itemInfo) itemInfo;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Class methods

```
+[_UIStatusBarDisplayItemPlacement placementWithIdentifier:priority:];
+[_UIStatusBarDisplayItemPlacement spacerPlacementWithSize:priority:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemPlacement priority];
-[_UIStatusBarDisplayItemPlacement allRequiredPlacements];
-[_UIStatusBarDisplayItemPlacement anyRequiredPlacements];
-[_UIStatusBarDisplayItemPlacement identifier];
-[_UIStatusBarDisplayItemPlacement excludingAllPlacementsInRegions:exceptPlacements:];
-[_UIStatusBarDisplayItemPlacement itemInfo];
-[_UIStatusBarDisplayItemPlacement setPriority:];
-[_UIStatusBarDisplayItemPlacement requiringAllPlacements:];
-[_UIStatusBarDisplayItemPlacement excludingPlacements:];
-[_UIStatusBarDisplayItemPlacement isEnabled];
-[_UIStatusBarDisplayItemPlacement excludingAllPlacementsInRegions:];
-[_UIStatusBarDisplayItemPlacement setEnabled:];
-[_UIStatusBarDisplayItemPlacement disabledPlacement];
-[_UIStatusBarDisplayItemPlacement hash];
-[_UIStatusBarDisplayItemPlacement description];
-[_UIStatusBarDisplayItemPlacement excludedRegionIdentifiers];
-[_UIStatusBarDisplayItemPlacement includedPlacements];
-[_UIStatusBarDisplayItemPlacement requiringAnyPlacements:];
-[_UIStatusBarDisplayItemPlacement isEqual:];
-[_UIStatusBarDisplayItemPlacement withItemInfo:];
-[_UIStatusBarDisplayItemPlacement excludedPlacements];
```
