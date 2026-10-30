# `SBFilteringSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- Protocols: `SBRoutingSwitcherModifierDelegate`
- 5 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBRoutingSwitcherModifier" _routingModifier;
@"_SBFilteringPassthroughTargetSwitcherModifier" _passthroughModifier;
@"NSSet" _displayItemsToFilter;
@"NSArray" _appLayoutsToFilter;
@"SBSwitcherModifier" _modifier;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_appLayoutsToFilter) appLayoutsToFilter;
@property (T@"SBSwitcherModifier",R,N,V_modifier) modifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFilteringSwitcherModifier didMoveToParentModifier:];
-[SBFilteringSwitcherModifier modifier];
-[SBFilteringSwitcherModifier setState:];
-[SBFilteringSwitcherModifier appLayoutsToFilter];
-[SBFilteringSwitcherModifier fallbackModifierForRoutingModifier:];
-[SBFilteringSwitcherModifier homeScreenModifierForRoutingModifier:];
-[SBFilteringSwitcherModifier initWithAppLayouts:modifier:];
-[SBFilteringSwitcherModifier routingModifier:animationAttributesModifierForLayoutElement:];
-[SBFilteringSwitcherModifier routingModifier:containerViewBoundsForModifier:];
-[SBFilteringSwitcherModifier routingModifier:event:forModifier:];
-[SBFilteringSwitcherModifier routingModifier:filteredAppLayouts:forModifier:];
-[SBFilteringSwitcherModifier routingModifier:filteredContinuousExposeIdentifiers:forModifier:];
-[SBFilteringSwitcherModifier routingModifier:modifierForAppLayout:];
-[SBFilteringSwitcherModifier routingModifier:switcherViewBoundsForModifier:];
-[SBFilteringSwitcherModifier scrollModifierForRoutingModifier:];
-[SBFilteringSwitcherModifier slideOverTongueModifierForRoutingModifier:];
-[SBFilteringSwitcherModifier transactionCompletionOptionsModifierForRoutingModifier:];
```
