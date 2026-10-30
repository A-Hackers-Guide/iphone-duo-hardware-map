# `_UIStatusBarDisplayItemState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarPrioritized`
- 20 instance variables, 26 properties, 66 instance methods, 2 class methods

## Instance variables

```
B _wasEnabled;
B _wasVisible;
B _dataEnabled;
B _floating;
@"_UIStatusBarDisplayItem" _displayItem;
@"_UIStatusBarIdentifier" _identifier;
@"_UIStatusBar" _statusBar;
@"_UIStatusBarItem" _item;
@"NSMutableArray" _placementStates;
q _preferredPlacementStateIndex;
q _currentPlacementStateIndex;
@"_UIStatusBarStyleAttributes" _overriddenStyleAttributes;
q _previousPlacementStateIndex;
q _dataUpdateStatus;
q _placementUpdateStatus;
q _enabilityStatus;
q _visibilityStatus;
@"_UIStatusBarAnimation" _addingAnimation;
@"_UIStatusBarAnimation" _removingAnimation;
@"NSMutableSet" _animations;
```

## Properties

```
@property (T@"_UIStatusBarIdentifier",C,N,V_identifier) identifier;
@property (T@"_UIStatusBar",W,N,V_statusBar) statusBar;
@property (T@"_UIStatusBarItem",W,N,V_item) item;
@property (T@"_UIStatusBarDisplayItem",W,N,V_displayItem) displayItem;
@property (T@"NSMutableArray",&,N,V_placementStates) placementStates;
@property (T@"_UIStatusBarDisplayItemPlacementState",R,N) currentPlacementState;
@property (Tq,N,V_preferredPlacementStateIndex) preferredPlacementStateIndex;
@property (Tq,N,V_currentPlacementStateIndex) currentPlacementStateIndex;
@property (T@"_UIStatusBarStyleAttributes",&,N,V_overriddenStyleAttributes) overriddenStyleAttributes;
@property (TB,N,V_wasEnabled) wasEnabled;
@property (TB,N,V_wasVisible) wasVisible;
@property (Tq,N,V_previousPlacementStateIndex) previousPlacementStateIndex;
@property (Tq,R,N,G_animationType) animationType;
@property (Tq,N,V_dataUpdateStatus) dataUpdateStatus;
@property (Tq,N,V_placementUpdateStatus) placementUpdateStatus;
@property (TB,R,N,GisEnabledIgnoringAnimations) enabledIgnoringAnimations;
@property (TB,N,V_dataEnabled) dataEnabled;
@property (TB,N,V_floating) floating;
@property (Tq,N,V_enabilityStatus) enabilityStatus;
@property (Tq,N,V_visibilityStatus) visibilityStatus;
@property (T@"_UIStatusBarAnimation",&,N,V_addingAnimation) addingAnimation;
@property (T@"_UIStatusBarAnimation",&,N,V_removingAnimation) removingAnimation;
@property (T@"NSMutableSet",R,N,V_animations) animations;
@property (TB,R,N,GisEnabled) enabled;
@property (T@"NSArray",R,C,N) potentialPlacementRegionIdentifiers;
@property (Tq,R,N) priority;
```

## Class methods

```
+[_UIStatusBarDisplayItemState setupRelationsBetweenDisplayItemStates:visualProvider:];
+[_UIStatusBarDisplayItemState stateForDisplayItemWithIdentifier:statusBar:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemState statusBar];
-[_UIStatusBarDisplayItemState addingAnimation];
-[_UIStatusBarDisplayItemState priority];
-[_UIStatusBarDisplayItemState animations];
-[_UIStatusBarDisplayItemState prepareAnimation:];
-[_UIStatusBarDisplayItemState prepareForDataUpdate];
-[_UIStatusBarDisplayItemState previousPlacementStateIndex];
-[_UIStatusBarDisplayItemState setFloating:];
-[_UIStatusBarDisplayItemState setPlacementStates:];
-[_UIStatusBarDisplayItemState wasVisible];
-[_UIStatusBarDisplayItemState _animationType];
-[_UIStatusBarDisplayItemState enabilityStatus];
-[_UIStatusBarDisplayItemState setStatusBar:];
-[_UIStatusBarDisplayItemState setEnabilityStatus:];
-[_UIStatusBarDisplayItemState _cancelObsoleteAnimations];
-[_UIStatusBarDisplayItemState identifier];
-[_UIStatusBarDisplayItemState setOverriddenStyleAttributes:];
-[_UIStatusBarDisplayItemState placementStates];
-[_UIStatusBarDisplayItemState prepareForOverflowDataUpdate];
-[_UIStatusBarDisplayItemState updateWithData:styleAttributes:];
-[_UIStatusBarDisplayItemState setPlacementUpdateStatus:];
-[_UIStatusBarDisplayItemState setItem:];
-[_UIStatusBarDisplayItemState visibilityStatus];
-[_UIStatusBarDisplayItemState floating];
-[_UIStatusBarDisplayItemState dataUpdateStatus];
-[_UIStatusBarDisplayItemState setCurrentPlacementStateIndex:];
-[_UIStatusBarDisplayItemState setDataEnabled:];
-[_UIStatusBarDisplayItemState wasEnabled];
-[_UIStatusBarDisplayItemState _updateForUpdatedData:updatedStyleAttributes:updatedEnability:];
-[_UIStatusBarDisplayItemState _animationWithUpdateAnimation:];
-[_UIStatusBarDisplayItemState item];
-[_UIStatusBarDisplayItemState _updateStatuses];
-[_UIStatusBarDisplayItemState isEnabled];
-[_UIStatusBarDisplayItemState displayItem];
-[_UIStatusBarDisplayItemState setWasEnabled:];
-[_UIStatusBarDisplayItemState _resolveDependentItemStatesWithBlock:];
-[_UIStatusBarDisplayItemState hasRunningAnimations];
-[_UIStatusBarDisplayItemState setIdentifier:];
-[_UIStatusBarDisplayItemState placementStateForPlacement:];
-[_UIStatusBarDisplayItemState setRemovingAnimation:];
-[_UIStatusBarDisplayItemState _updateForItem:data:styleAttributes:];
-[_UIStatusBarDisplayItemState isCurrentPlacement:];
-[_UIStatusBarDisplayItemState removingAnimation];
-[_UIStatusBarDisplayItemState setDisplayItem:];
-[_UIStatusBarDisplayItemState currentPlacementStateIndex];
-[_UIStatusBarDisplayItemState potentialPlacementRegionIdentifiers];
-[_UIStatusBarDisplayItemState setVisibilityStatus:];
-[_UIStatusBarDisplayItemState updatePlacement];
-[_UIStatusBarDisplayItemState addPlacement:inRegion:];
-[_UIStatusBarDisplayItemState currentPlacementState];
-[_UIStatusBarDisplayItemState description];
-[_UIStatusBarDisplayItemState _updateToNextPlacementStateIfNeeded];
-[_UIStatusBarDisplayItemState setPreviousPlacementStateIndex:];
-[_UIStatusBarDisplayItemState updateToNextEnabledPlacement];
-[_UIStatusBarDisplayItemState _updatePlacementWithRecursionBlock:];
-[_UIStatusBarDisplayItemState resetToPreferredPlacement];
-[_UIStatusBarDisplayItemState setDataUpdateStatus:];
-[_UIStatusBarDisplayItemState setPreferredPlacementStateIndex:];
-[_UIStatusBarDisplayItemState overriddenStyleAttributes];
-[_UIStatusBarDisplayItemState preferredPlacementStateIndex];
-[_UIStatusBarDisplayItemState setWasVisible:];
-[_UIStatusBarDisplayItemState _effectiveStyleAttributesFromStyleAttributes:data:styleAttributesChanged:];
-[_UIStatusBarDisplayItemState isEnabledIgnoringAnimations];
-[_UIStatusBarDisplayItemState setAddingAnimation:];
-[_UIStatusBarDisplayItemState placementUpdateStatus];
-[_UIStatusBarDisplayItemState dataEnabled];
```
