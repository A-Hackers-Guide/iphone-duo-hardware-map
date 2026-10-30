# `SBIconViewVisibilitySwitcherEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _visible;
@"SBAppLayout" _appLayout;
@"SBFFluidBehaviorSettings" _animationSettings;
@"NSSet" _excludedIconLocations;
d _scale;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (T@"SBFFluidBehaviorSettings",R,N,V_animationSettings) animationSettings;
@property (T@"NSSet",R,N,V_excludedIconLocations) excludedIconLocations;
@property (TB,R,N,GisVisible,V_visible) visible;
@property (Td,N,V_scale) scale;
```

## Instance methods

```
-[SBIconViewVisibilitySwitcherEventResponse animationSettings];
-[SBIconViewVisibilitySwitcherEventResponse excludedIconLocations];
-[SBIconViewVisibilitySwitcherEventResponse initWithAppLayout:visible:animationSettings:excludedIconLocations:];
-[SBIconViewVisibilitySwitcherEventResponse appLayout];
-[SBIconViewVisibilitySwitcherEventResponse isVisible];
-[SBIconViewVisibilitySwitcherEventResponse setScale:];
-[SBIconViewVisibilitySwitcherEventResponse scale];
-[SBIconViewVisibilitySwitcherEventResponse type];
-[SBIconViewVisibilitySwitcherEventResponse descriptionBuilderWithMultilinePrefix:];
```
