# `SBMutableSwitcherTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherTransitionRequest`
- 1 instance variables, 30 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifierOfAppToKillGracefully;
```

## Properties

```
@property (T@"SBAppLayout",&,D,N) appLayout;
@property (T@"SBDisplayItem",&,D,N) activatingDisplayItem;
@property (Tq,D,N) appLayoutEnvironment;
@property (Tq,D,N) unlockedEnvironmentMode;
@property (T@"SBUnlockedEnvironmentState",&,D,N) unlockedEnvironmentState;
@property (Tq,D,N) preferredInterfaceOrientation;
@property (Tq,D,N) floatingConfiguration;
@property (T@"NSDictionary",&,D,N) displayItemLayoutAttributesMap;
@property (Tq,D,N) floatingSwitcherVisible;
@property (Tq,D,N) animationDisabled;
@property (Tq,D,N) autoPIPDisabled;
@property (Tq,D,N) source;
@property (Tq,D,N) peekConfiguration;
@property (T@"NSString",C,D,N) bundleIdentifierForAppExpose;
@property (T@"SBAppExposeBundleIdentifierState",&,D,N) appExposeBundleIdentifierState;
@property (Tq,D,N) entityInsertionPolicy;
@property (TB,D,N) settlesMultiAppFullScreenSpacesImmediately;
@property (TB,D,N) preventSwitcherRecencyModelUpdates;
@property (TB,D,N) nilAppLayoutIsEmptySpace;
@property (TB,D,N) sceneUpdatesOnly;
@property (TB,D,N) fenceSceneUpdate;
@property (TB,D,N,GisSwappingAppSides) swappingAppSides;
@property (TB,D,N) preservesSceneViewDisplayMode;
@property (TB,D,N) prefersZoomDownAnimation;
@property (T@"SBFFluidBehaviorSettings",&,D,N) animationSettings;
@property (T@"SBDisplayItem",&,D,N) minimizingDisplayItem;
@property (T@"NSString",C,N,V_bundleIdentifierOfAppToKillGracefully) bundleIdentifierOfAppToKillGracefully;
@property (TB,D,N,GisAppLaunchDuringWindowDragGesture,SsetAppLaunchDuringWindowDragGesture:) appLaunchDuringWindowDragGesture;
@property (TB,D,N) retainsSiri;
@property (T@"FBSDisplayConfiguration",C,D,N) displayConfiguration;
```

## Instance methods

```
-[SBMutableSwitcherTransitionRequest bundleIdentifierOfAppToKillGracefully];
-[SBMutableSwitcherTransitionRequest setBundleIdentifierOfAppToKillGracefully:];
```
