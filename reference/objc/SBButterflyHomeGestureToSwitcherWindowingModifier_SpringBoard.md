# `SBButterflyHomeGestureToSwitcherWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 8 instance variables, 1 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _selectedAppLayout;
@"SBWindowingModifier" _multitaskingModifier;
@"SBUnlockedEnvironmentState" _startingEnvironmentState;
{CGPoint="x"d"y"d} _liftOffVelocity;
{CGPoint="x"d"y"d} _liftOffTranslation;
@"NSUUID" _transitionID;
@"SBDeckRegionModel" _toDeckModel;
Q _hidEventSenderID;
```

## Properties

```
@property (TQ,N,V_hidEventSenderID) hidEventSenderID;
```

## Instance methods

```
-[SBButterflyHomeGestureToSwitcherWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBButterflyHomeGestureToSwitcherWindowingModifier containerStatusBarAnimationDuration];
-[SBButterflyHomeGestureToSwitcherWindowingModifier isHomeScreenContentRequired];
-[SBButterflyHomeGestureToSwitcherWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier transactionCompletionOptions];
-[SBButterflyHomeGestureToSwitcherWindowingModifier homeScreenBackdropBlurType];
-[SBButterflyHomeGestureToSwitcherWindowingModifier _layoutSettings];
-[SBButterflyHomeGestureToSwitcherWindowingModifier isSwitcherWindowVisible];
-[SBButterflyHomeGestureToSwitcherWindowingModifier appLayoutsToCacheSnapshots];
-[SBButterflyHomeGestureToSwitcherWindowingModifier isWallpaperRequiredForSwitcher];
-[SBButterflyHomeGestureToSwitcherWindowingModifier contentOffsetForIndex:alignment:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier wallpaperStyle];
-[SBButterflyHomeGestureToSwitcherWindowingModifier transitionWillBegin:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier visibleItems];
-[SBButterflyHomeGestureToSwitcherWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyHomeGestureToSwitcherWindowingModifier animationAttributesForItem:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier prefersHomeAffordanceInItemContainerForLayoutElement:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier timerFired:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier deckRegionModel];
-[SBButterflyHomeGestureToSwitcherWindowingModifier _appLayoutAlignmentToScrollToDuringTransition];
-[SBButterflyHomeGestureToSwitcherWindowingModifier _appLayoutToScrollToDuringTransition];
-[SBButterflyHomeGestureToSwitcherWindowingModifier _appLayoutsForSwitcher];
-[SBButterflyHomeGestureToSwitcherWindowingModifier _containerViewBounds];
-[SBButterflyHomeGestureToSwitcherWindowingModifier _dismissForEmptySwitcherResponseName];
-[SBButterflyHomeGestureToSwitcherWindowingModifier hidEventSenderID];
-[SBButterflyHomeGestureToSwitcherWindowingModifier initWithMultitaskingModifier:selectedAppLayout:startingEnvironmentState:liftOffVelocity:liftOffTranslation:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier setHidEventSenderID:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier shouldInterruptForActivity:];
-[SBButterflyHomeGestureToSwitcherWindowingModifier transitionDidComplete:];
```
