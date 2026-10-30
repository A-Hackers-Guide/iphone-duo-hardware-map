# `SBSwitcherTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSMutableCopying`
- 27 instance variables, 33 properties, 65 instance methods, 8 class methods

## Instance variables

```
B _settlesMultiAppFullScreenSpacesImmediately;
B _prefersZoomDownAnimation;
B _preventSwitcherRecencyModelUpdates;
B _nilAppLayoutIsEmptySpace;
B _sceneUpdatesOnly;
B _fenceSceneUpdate;
B _swappingAppSides;
B _preservesSceneViewDisplayMode;
B _appLaunchDuringWindowDragGesture;
B _retainsSiri;
@"SBAppLayout" _appLayout;
@"SBDisplayItem" _activatingDisplayItem;
q _appLayoutEnvironment;
@"SBUnlockedEnvironmentState" _unlockedEnvironmentState;
q _preferredInterfaceOrientation;
q _floatingConfiguration;
@"NSDictionary" _displayItemLayoutAttributesMap;
q _floatingSwitcherVisible;
q _animationDisabled;
q _autoPIPDisabled;
q _source;
q _peekConfiguration;
@"SBAppExposeBundleIdentifierState" _appExposeBundleIdentifierState;
q _entityInsertionPolicy;
@"SBDisplayItem" _minimizingDisplayItem;
@"SBFFluidBehaviorSettings" _animationSettings;
@"FBSDisplayConfiguration" _displayConfiguration;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_appLayout) appLayout;
@property (T@"SBDisplayItem",&,N,V_activatingDisplayItem) activatingDisplayItem;
@property (Tq,N,V_appLayoutEnvironment) appLayoutEnvironment;
@property (T@"SBUnlockedEnvironmentState",&,N,V_unlockedEnvironmentState) unlockedEnvironmentState;
@property (Tq,N,V_preferredInterfaceOrientation) preferredInterfaceOrientation;
@property (Tq,N,V_floatingConfiguration) floatingConfiguration;
@property (T@"NSDictionary",&,N,V_displayItemLayoutAttributesMap) displayItemLayoutAttributesMap;
@property (Tq,N,V_floatingSwitcherVisible) floatingSwitcherVisible;
@property (Tq,N,V_animationDisabled) animationDisabled;
@property (Tq,N,V_autoPIPDisabled) autoPIPDisabled;
@property (Tq,N,V_source) source;
@property (Tq,N,V_peekConfiguration) peekConfiguration;
@property (T@"SBAppExposeBundleIdentifierState",&,N,V_appExposeBundleIdentifierState) appExposeBundleIdentifierState;
@property (Tq,N,V_entityInsertionPolicy) entityInsertionPolicy;
@property (TB,N,V_settlesMultiAppFullScreenSpacesImmediately) settlesMultiAppFullScreenSpacesImmediately;
@property (TB,N,V_sceneUpdatesOnly) sceneUpdatesOnly;
@property (TB,N,V_fenceSceneUpdate) fenceSceneUpdate;
@property (TB,N,GisSwappingAppSides,V_swappingAppSides) swappingAppSides;
@property (TB,N,V_preservesSceneViewDisplayMode) preservesSceneViewDisplayMode;
@property (TB,N,V_preventSwitcherRecencyModelUpdates) preventSwitcherRecencyModelUpdates;
@property (TB,N,V_nilAppLayoutIsEmptySpace) nilAppLayoutIsEmptySpace;
@property (TB,N,V_prefersZoomDownAnimation) prefersZoomDownAnimation;
@property (T@"SBFFluidBehaviorSettings",&,N,V_animationSettings) animationSettings;
@property (TB,N,GisAppLaunchDuringWindowDragGesture,SsetAppLaunchDuringWindowDragGesture:,V_appLaunchDuringWindowDragGesture) appLaunchDuringWindowDragGesture;
@property (TB,N,V_retainsSiri) retainsSiri;
@property (T@"FBSDisplayConfiguration",C,N,V_displayConfiguration) displayConfiguration;
@property (T@"SBDisplayItem",&,N,V_minimizingDisplayItem) minimizingDisplayItem;
@property (Tq,R,N) unlockedEnvironmentMode;
@property (T@"NSString",R,C,N) bundleIdentifierForAppExpose;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherTransitionRequest requestForStashingFloatingApplicationWithFloatingConfiguration:];
+[SBSwitcherTransitionRequest requestForActivatingAppSwitcher];
+[SBSwitcherTransitionRequest requestForActivatingAppLayout:];
+[SBSwitcherTransitionRequest requestForActivatingFloatingSwitcher];
+[SBSwitcherTransitionRequest requestForActivatingHomeScreen];
+[SBSwitcherTransitionRequest requestForDeactivatingFloatingSwitcher];
+[SBSwitcherTransitionRequest requestForTapAppLayoutEvent:];
+[SBSwitcherTransitionRequest requestForTapAppLayoutHeaderEvent:];
```

## Instance methods

```
-[SBSwitcherTransitionRequest setAnimationSettings:];
-[SBSwitcherTransitionRequest floatingConfiguration];
-[SBSwitcherTransitionRequest animationSettings];
-[SBSwitcherTransitionRequest displayConfiguration];
-[SBSwitcherTransitionRequest mutableCopyWithZone:];
-[SBSwitcherTransitionRequest preferredInterfaceOrientation];
-[SBSwitcherTransitionRequest succinctDescriptionBuilder];
-[SBSwitcherTransitionRequest init];
-[SBSwitcherTransitionRequest setAppLayout:];
-[SBSwitcherTransitionRequest appLayout];
-[SBSwitcherTransitionRequest setPreservesSceneViewDisplayMode:];
-[SBSwitcherTransitionRequest minimizingDisplayItem];
-[SBSwitcherTransitionRequest preventSwitcherRecencyModelUpdates];
-[SBSwitcherTransitionRequest setMinimizingDisplayItem:];
-[SBSwitcherTransitionRequest unlockedEnvironmentState];
-[SBSwitcherTransitionRequest setRetainsSiri:];
-[SBSwitcherTransitionRequest descriptionWithMultilinePrefix:];
-[SBSwitcherTransitionRequest displayItemLayoutAttributesMap];
-[SBSwitcherTransitionRequest setDisplayConfiguration:];
-[SBSwitcherTransitionRequest setSource:];
-[SBSwitcherTransitionRequest preservesSceneViewDisplayMode];
-[SBSwitcherTransitionRequest succinctDescription];
-[SBSwitcherTransitionRequest settlesMultiAppFullScreenSpacesImmediately];
-[SBSwitcherTransitionRequest retainsSiri];
-[SBSwitcherTransitionRequest setPreferredInterfaceOrientation:];
-[SBSwitcherTransitionRequest setSettlesMultiAppFullScreenSpacesImmediately:];
-[SBSwitcherTransitionRequest unlockedEnvironmentMode];
-[SBSwitcherTransitionRequest description];
-[SBSwitcherTransitionRequest peekConfiguration];
-[SBSwitcherTransitionRequest appExposeBundleIdentifierState];
-[SBSwitcherTransitionRequest setPreventSwitcherRecencyModelUpdates:];
-[SBSwitcherTransitionRequest prefersZoomDownAnimation];
-[SBSwitcherTransitionRequest source];
-[SBSwitcherTransitionRequest setPrefersZoomDownAnimation:];
-[SBSwitcherTransitionRequest descriptionBuilderWithMultilinePrefix:];
-[SBSwitcherTransitionRequest setAnimationDisabled:];
-[SBSwitcherTransitionRequest autoPIPDisabled];
-[SBSwitcherTransitionRequest activatingDisplayItem];
-[SBSwitcherTransitionRequest animationDisabled];
-[SBSwitcherTransitionRequest appLayoutEnvironment];
-[SBSwitcherTransitionRequest bundleIdentifierForAppExpose];
-[SBSwitcherTransitionRequest entityInsertionPolicy];
-[SBSwitcherTransitionRequest fenceSceneUpdate];
-[SBSwitcherTransitionRequest floatingSwitcherVisible];
-[SBSwitcherTransitionRequest isAppLaunchDuringWindowDragGesture];
-[SBSwitcherTransitionRequest isSwappingAppSides];
-[SBSwitcherTransitionRequest nilAppLayoutIsEmptySpace];
-[SBSwitcherTransitionRequest sceneUpdatesOnly];
-[SBSwitcherTransitionRequest setActivatingDisplayItem:];
-[SBSwitcherTransitionRequest setAppExposeBundleIdentifierState:];
-[SBSwitcherTransitionRequest setAppLaunchDuringWindowDragGesture:];
-[SBSwitcherTransitionRequest setAppLayoutEnvironment:];
-[SBSwitcherTransitionRequest setAutoPIPDisabled:];
-[SBSwitcherTransitionRequest setBundleIdentifierForAppExpose:];
-[SBSwitcherTransitionRequest setDisplayItemLayoutAttributesMap:];
-[SBSwitcherTransitionRequest setEntityInsertionPolicy:];
-[SBSwitcherTransitionRequest setFenceSceneUpdate:];
-[SBSwitcherTransitionRequest setFloatingConfiguration:];
-[SBSwitcherTransitionRequest setFloatingSwitcherVisible:];
-[SBSwitcherTransitionRequest setNilAppLayoutIsEmptySpace:];
-[SBSwitcherTransitionRequest setPeekConfiguration:];
-[SBSwitcherTransitionRequest setSceneUpdatesOnly:];
-[SBSwitcherTransitionRequest setSwappingAppSides:];
-[SBSwitcherTransitionRequest setUnlockedEnvironmentMode:];
-[SBSwitcherTransitionRequest setUnlockedEnvironmentState:];
```
