# `SBButterflyRemovalWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 17 instance variables, 0 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _removedAppLayout;
q _reason;
@"NSString" _appExposeBundleID;
Q _phase;
Q _indexToScrollToAfterRemoval;
@"NSSet" _visibleItemsPriorToRemoval;
@"NSSet" _visibleSpaceAppLayoutsPriorToRemoval;
@"NSArray" _topMostItemsPriorToRemoval;
@"SBAppLayout" _remainingAppLayoutIfAny;
Q _remainingAppLayoutInitialHingeEdge;
@"SBAppLayout" _resizingAppLayoutIfAny;
Q _resizeGeneration;
@"SBAppLayout" _blurredAppLayoutIfAny;
@"SBAppLayout" _interlopingAppLayoutIfAny;
{SBWindowingItemFrame="bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"position"{CGPoint="x"d"y"d}"anchorPoint"{CGPoint="x"d"y"d}"scale"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}} _frameForInterlopingAppLayoutPriorToRemoval;
@"NSUUID" _transitionIDToAwaitIfAny;
B _hasBegunAwaitingTransition;
```

## Instance methods

```
-[SBButterflyRemovalWindowingModifier shouldScaleContentToFillBoundsAtIndex:];
-[SBButterflyRemovalWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBButterflyRemovalWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBButterflyRemovalWindowingModifier requiresAnimatableSnapshotUpdatesForLeafAppLayout:];
-[SBButterflyRemovalWindowingModifier shouldAccessoryDrawShadowForAppLayout:];
-[SBButterflyRemovalWindowingModifier transitionWillBegin:];
-[SBButterflyRemovalWindowingModifier visibleItems];
-[SBButterflyRemovalWindowingModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:];
-[SBButterflyRemovalWindowingModifier animationAttributesForItem:];
-[SBButterflyRemovalWindowingModifier opacityForItem:];
-[SBButterflyRemovalWindowingModifier resizeProgressNotificationsForLayoutRole:inAppLayout:];
-[SBButterflyRemovalWindowingModifier asyncRenderingAttributesForAppLayout:];
-[SBButterflyRemovalWindowingModifier topMostItems];
-[SBButterflyRemovalWindowingModifier visibleAppSpaces];
-[SBButterflyRemovalWindowingModifier frameForItem:];
-[SBButterflyRemovalWindowingModifier preferredSnapshotUpdateAnimationDurationForLeafAppLayout:];
-[SBButterflyRemovalWindowingModifier didComplete];
-[SBButterflyRemovalWindowingModifier _isAppLayoutInDeckAfterRemoval:];
-[SBButterflyRemovalWindowingModifier _blurParameters];
-[SBButterflyRemovalWindowingModifier _appLayoutPairedWithAppLayout:];
-[SBButterflyRemovalWindowingModifier _appendBlurResponseIfNeeded];
-[SBButterflyRemovalWindowingModifier _appendSwapToLiveContentResponseIfNeeded];
-[SBButterflyRemovalWindowingModifier _appendSwapToLiveSnapshotResponseIfNeeded];
-[SBButterflyRemovalWindowingModifier _appendUnblurResponseIfNeeded];
-[SBButterflyRemovalWindowingModifier _appendUpdateStyleResponseIfNeeded];
-[SBButterflyRemovalWindowingModifier _completeIfEnded];
-[SBButterflyRemovalWindowingModifier _isAppLayoutInvolvedInRemoval:];
-[SBButterflyRemovalWindowingModifier _performBlockWhileSimulatingPostRemovalAppLayoutState:];
-[SBButterflyRemovalWindowingModifier _stopAwaitingTransition];
-[SBButterflyRemovalWindowingModifier _wantsRemovedAppLayoutVisible];
-[SBButterflyRemovalWindowingModifier gestureWillBegin:];
-[SBButterflyRemovalWindowingModifier initWithAppLayout:reason:appExposeBundleID:];
-[SBButterflyRemovalWindowingModifier itemInserted:];
-[SBButterflyRemovalWindowingModifier itemRemoved:];
-[SBButterflyRemovalWindowingModifier resizeProgressChanged:];
-[SBButterflyRemovalWindowingModifier transitionDidComplete:];
```
