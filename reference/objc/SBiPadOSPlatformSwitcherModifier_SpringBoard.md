# `SBiPadOSPlatformSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 7 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _previousDisplayItems;
@"NSSet" _displayItems;
@"SBDisplayItem" _lastGesturedDisplayItem;
@"SBDisplayItem" _lastPulsedDisplayItem;
@"NSSet" _activatingLiveAppLayouts;
@"SBTransitionSwitcherModifierEvent" _lastTransitionEvent;
q _currentUnlockedEnvironmentMode;
```

## Instance methods

```
-[SBiPadOSPlatformSwitcherModifier handleGestureEvent:];
-[SBiPadOSPlatformSwitcherModifier jetsamModeForAppLayout:];
-[SBiPadOSPlatformSwitcherModifier foregroundAppLayouts];
-[SBiPadOSPlatformSwitcherModifier didMoveToParentModifier:];
-[SBiPadOSPlatformSwitcherModifier activityModeForAppLayout:];
-[SBiPadOSPlatformSwitcherModifier handleTransitionEvent:];
-[SBiPadOSPlatformSwitcherModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:];
-[SBiPadOSPlatformSwitcherModifier handleUpdateWindowingModeEvent:];
-[SBiPadOSPlatformSwitcherModifier handlePrepareForSceneUpdateEvent:];
```
