# `SBAppDragAndDropGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- 19 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _initialFullScreenAppLayout;
@"SBAppLayout" _fullScreenAppLayout;
@"SBAppLayout" _dropTransitionFromAppLayout;
@"SBDragAndDropToAppTransitionSwitcherModifier" _transitionModifier;
q _dropAction;
@"NSString" _draggedSceneIdentifier;
B _isWindowDrag;
B _hasPlatterized;
B _hasPreviewLifted;
q _draggedSceneOriginalLayoutRole;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _platterFrame;
{CGPoint="x"d"y"d} _location;
B _shouldPushInFullScreenContent;
B _isResizing;
B _hasResizedEnoughToUnblur;
B _isBlurring;
B _isBlurred;
B _needsBlurBecauseFramesWillMismatch;
B _gestureEnded;
```

## Instance methods

```
-[SBAppDragAndDropGestureSwitcherModifier handleGestureEvent:];
-[SBAppDragAndDropGestureSwitcherModifier scaleForIndex:];
-[SBAppDragAndDropGestureSwitcherModifier homeScreenDimmingAlpha];
-[SBAppDragAndDropGestureSwitcherModifier cornerRadiiForIndex:];
-[SBAppDragAndDropGestureSwitcherModifier animationAttributesForLayoutElement:];
-[SBAppDragAndDropGestureSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBAppDragAndDropGestureSwitcherModifier handleTransitionEvent:];
-[SBAppDragAndDropGestureSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBAppDragAndDropGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBAppDragAndDropGestureSwitcherModifier switcherHitTestsAsOpaque];
-[SBAppDragAndDropGestureSwitcherModifier frameForIndex:];
-[SBAppDragAndDropGestureSwitcherModifier backgroundOpacityForIndex:];
-[SBAppDragAndDropGestureSwitcherModifier completesWhenChildrenComplete];
-[SBAppDragAndDropGestureSwitcherModifier handleResizeProgressEvent:];
-[SBAppDragAndDropGestureSwitcherModifier resizeProgressNotificationsForLayoutRole:inAppLayout:];
-[SBAppDragAndDropGestureSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBAppDragAndDropGestureSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBAppDragAndDropGestureSwitcherModifier _isDraggingLiveWindow];
-[SBAppDragAndDropGestureSwitcherModifier _recomputeBlurStateWithCompletion:];
-[SBAppDragAndDropGestureSwitcherModifier _shouldPushInFullScreenContentForEvent:];
-[SBAppDragAndDropGestureSwitcherModifier _showResizeUI];
-[SBAppDragAndDropGestureSwitcherModifier handleBlurProgressEvent:];
-[SBAppDragAndDropGestureSwitcherModifier handleSceneReadyEvent:];
-[SBAppDragAndDropGestureSwitcherModifier initWithGestureID:fullScreenAppLayout:];
```
