# `SBHomeGestureToMixedGridSwitcherSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 7 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"SBSwitcherModifier<SBMixedGridSwitcherProviding>" _mixedGridModifier;
@"SBHomeGestureToSwitcherSwitcherModifier" _homeGestureModifier;
q _startingEnvironmentMode;
{CGPoint="x"d"y"d} _liftOffVelocity;
{CGPoint="x"d"y"d} _liftOffTranslation;
Q _hidEventSenderID;
```

## Properties

```
@property (TQ,N,V_hidEventSenderID) hidEventSenderID;
```

## Instance methods

```
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier scaleForIndex:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier visibleAppLayouts];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier contentOffsetForIndex:alignment:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier frameForIndex:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier _appLayoutToScrollTo];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier _dismissForEmptySwitcherResponseName];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier _firstFloatingAppLayout:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier _newMixedGridModifier];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier _performBlockWhileSimulatingPostPresentationScrollViewContentOffset:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier hidEventSenderID];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier initWithTransitionID:mixedGridModifier:selectedAppLayout:startingEnvironmentMode:liftOfVelocity:liftOffTranslation:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier responseForProposedChildResponse:childModifier:event:];
-[SBHomeGestureToMixedGridSwitcherSwitcherModifier setHidEventSenderID:];
```
