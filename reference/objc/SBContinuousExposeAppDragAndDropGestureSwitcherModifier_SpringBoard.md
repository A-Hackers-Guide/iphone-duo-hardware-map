# `SBContinuousExposeAppDragAndDropGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- 31 instance variables, 0 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _initialAppLayout;
@"SBAppLayout" _appLayout;
@"SBDisplayItem" _displayItemThatWouldBeEvictedIfAnyBasedOnZOrder;
@"SBDisplayItem" _currentDisplayItemToReplace;
@"SBAppLayout" _dropTransitionFromAppLayout;
@"SBAppLayout" _minimizingAppLayout;
@"SBContinuousExposeDragAndDropToAppTransitionSwitcherModifier" _transitionModifier;
@"NSDictionary" _initialLayoutAttributesMap;
@"SBFlexibleWindowingAutoLayoutSpace" _initialAutoLayoutSpace;
@"SBDisplayItem" _initialSlideOverItem;
@"SBDisplayItem" _initialSlideOverItemOnStage;
B _isActivatingSlideOver;
B _initialAppLayoutContainsDraggingItem;
@"NSSet" _initialVisibleSplitViewNubs;
@"NSSet" _initialVisibleSplitViewDimmings;
@"NSDictionary" _framesForSplitViewHandleNubViews;
@"NSDictionary" _framesForSplitViewHandleDimmingViews;
B _isBlurred;
B _isResizing;
B _hasResizedEnoughToUnblur;
B _needsBlurBecauseFramesWillMismatch;
q _dropAction;
@"NSString" _draggedSceneIdentifier;
B _hasPlatterized;
B _hasPreviewLifted;
q _draggedSceneOriginalLayoutRole;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _platterFrame;
{CGPoint="x"d"y"d} _location;
B _performedDrop;
B _gestureEnded;
@"SBDisplayItem" _fullStageDisplayItem;
```

## Instance methods

```
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier handleGestureEvent:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier homeScreenDimmingAlpha];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier frameForSlideOverTongueAppLayout];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier didMoveToParentModifier:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier animationAttributesForLayoutElement:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier visibleSplitViewHandleNubViews];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier visibleSplitViewHandleDimmingViews];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier topMostLayoutElements];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier handleTransitionEvent:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier switcherHitTestsAsOpaque];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier completesWhenChildrenComplete];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier handleResizeProgressEvent:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier wantsSlideOverTongue];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier frameForSplitViewHandleNubView:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier slideOverTongueDirection];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier isHitTestBlockingViewVisible];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier occlusionStateForLayoutRole:inAppLayout:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier resizeProgressNotificationsForLayoutRole:inAppLayout:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier frameForSplitViewHandleDimmingView:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier slideOverTongueState];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier _recomputeBlurStateWithCompletion:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier handleBlurProgressEvent:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier handleSceneReadyEvent:];
-[SBContinuousExposeAppDragAndDropGestureSwitcherModifier initWithGestureID:appLayout:displayItemThatWouldBeEvicted:];
```
