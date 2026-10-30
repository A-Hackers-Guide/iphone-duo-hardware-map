# `SBFullScreenAppLayoutSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 5 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"SBCoplanarSwitcherModifier" _coplanarModifier;
@"_SBFullScreenAppFloorSwitcherModifier" _floorModifier;
B _handlesAssistantPresentationEvents;
@"NSUUID" _homeAffordanceReuseIdentifier;
```

## Properties

```
@property (T@"NSUUID",&,N,V_homeAffordanceReuseIdentifier) homeAffordanceReuseIdentifier;
@property (TB,N,V_handlesAssistantPresentationEvents) handlesAssistantPresentationEvents;
```

## Instance methods

```
-[SBFullScreenAppLayoutSwitcherModifier initWithActiveAppLayout:homeAffordanceReuseIdentifier:];
-[SBFullScreenAppLayoutSwitcherModifier homeAffordanceReuseIdentifier];
-[SBFullScreenAppLayoutSwitcherModifier didMoveToParentModifier:];
-[SBFullScreenAppLayoutSwitcherModifier handleTransitionEvent:];
-[SBFullScreenAppLayoutSwitcherModifier initWithActiveAppLayout:];
-[SBFullScreenAppLayoutSwitcherModifier setHandlesAssistantPresentationEvents:];
-[SBFullScreenAppLayoutSwitcherModifier handlesAssistantPresentationEvents];
-[SBFullScreenAppLayoutSwitcherModifier setHomeAffordanceReuseIdentifier:];
-[SBFullScreenAppLayoutSwitcherModifier _addAssistantModifierIfNeededForInterfaceOrientation:];
-[SBFullScreenAppLayoutSwitcherModifier fullScreenFrameForAppLayout:];
-[SBFullScreenAppLayoutSwitcherModifier handleAssistantPresentationChangedEvent:];
```
