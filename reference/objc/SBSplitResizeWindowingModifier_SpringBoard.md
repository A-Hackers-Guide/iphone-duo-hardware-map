# `SBSplitResizeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 22 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _gestureID;
@"SBDisplayItem" _leftDisplayItem;
@"SBDisplayItem" _rightDisplayItem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftAppRubberbandedFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rightAppRubberbandedFrame;
{CGPoint="x"d"y"d} _locationEdgeAdjustment;
d _initialGrabberMargin;
{CGPoint="x"d"y"d} _initialLocation;
{CGSize="width"d"height"d} _currentLeftAppSceneSize;
{CGSize="width"d"height"d} _currentRightAppSceneSize;
B _needsSceneSizeUpdate;
@"SBDisplayItemLayoutGrid" _layoutGrid;
B _gestureIsEnding;
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
q _delayedSceneSizeUpdateGeneration;
@"NSString" _delayedSceneSizeUpdateReason;
@"SBFlexibleWindowingAutoLayoutSpace" _initialAutoLayoutSpace;
@"SBDisplayItem" _itemToMinimizeUponRelease;
B _allowsMinimizing;
d _progressToMaxDisplacement;
d _requiredGestureTranslationBeforeSeparation;
@"SBAppLayout" _splitPairAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_splitPairAppLayout) splitPairAppLayout;
```

## Instance methods

```
-[SBSplitResizeWindowingModifier visibleSplitViewHandleDimmingViews];
-[SBSplitResizeWindowingModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBSplitResizeWindowingModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBSplitResizeWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBSplitResizeWindowingModifier transitionWillBegin:];
-[SBSplitResizeWindowingModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBSplitResizeWindowingModifier splitPairAppLayout];
-[SBSplitResizeWindowingModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBSplitResizeWindowingModifier frameForSplitViewHandleNubView:];
-[SBSplitResizeWindowingModifier animationAttributesForItem:];
-[SBSplitResizeWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBSplitResizeWindowingModifier timerFired:];
-[SBSplitResizeWindowingModifier frameForSplitViewHandleDimmingView:];
-[SBSplitResizeWindowingModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:];
-[SBSplitResizeWindowingModifier willBegin];
-[SBSplitResizeWindowingModifier _animationSettingsForLayout];
-[SBSplitResizeWindowingModifier _displacementForItemToMinimizeUponRelease];
-[SBSplitResizeWindowingModifier _responseForItem:sceneSizeUpdateToSize:center:];
-[SBSplitResizeWindowingModifier _updateWithGesture:];
-[SBSplitResizeWindowingModifier gestureDidComplete:];
-[SBSplitResizeWindowingModifier gestureDidUpdate:];
-[SBSplitResizeWindowingModifier gestureWillBegin:];
-[SBSplitResizeWindowingModifier initWithSplitPairAppLayout:];
-[SBSplitResizeWindowingModifier layoutRestrictionInfoForItem:];
-[SBSplitResizeWindowingModifier transitionDidComplete:];
```
