# `SBSceneResizeGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- 12 instance variables, 0 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
q _startingSpaceConfiguration;
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _location;
{CGPoint="x"d"y"d} _velocity;
@"UIViewFloatAnimatableProperty" _rampingProperty;
@"SBFFluidBehaviorSettings" _rampedLayoutSettings;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialSpaceFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startingFrameForPrimaryItem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startingFrameForSideItem;
Q _timerGenCount;
{CGPoint="x"d"y"d} _lastTranslationThatUpdatedScene;
```

## Instance methods

```
-[SBSceneResizeGestureSwitcherModifier handleGestureEvent:];
-[SBSceneResizeGestureSwitcherModifier scaleForIndex:];
-[SBSceneResizeGestureSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBSceneResizeGestureSwitcherModifier didMoveToParentModifier:];
-[SBSceneResizeGestureSwitcherModifier cornerRadiiForIndex:];
-[SBSceneResizeGestureSwitcherModifier shouldScaleOverlayToFillBoundsAtIndex:];
-[SBSceneResizeGestureSwitcherModifier animationAttributesForLayoutElement:];
-[SBSceneResizeGestureSwitcherModifier handleTransitionEvent:];
-[SBSceneResizeGestureSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBSceneResizeGestureSwitcherModifier handleTimerEvent:];
-[SBSceneResizeGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBSceneResizeGestureSwitcherModifier backgroundOpacityForIndex:];
-[SBSceneResizeGestureSwitcherModifier keyboardSuppressionMode];
-[SBSceneResizeGestureSwitcherModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBSceneResizeGestureSwitcherModifier blurDelayForLayoutRole:inAppLayout:];
-[SBSceneResizeGestureSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBSceneResizeGestureSwitcherModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:];
-[SBSceneResizeGestureSwitcherModifier isLayoutRoleBlurred:inAppLayout:];
-[SBSceneResizeGestureSwitcherModifier _currentPresentationAction];
-[SBSceneResizeGestureSwitcherModifier _maxCardWidthForDismissalAction];
-[SBSceneResizeGestureSwitcherModifier _normalizedDismissRightProgress];
-[SBSceneResizeGestureSwitcherModifier _actionForNormalizedProgress:inOrientation:];
-[SBSceneResizeGestureSwitcherModifier _appLayoutForAction:];
-[SBSceneResizeGestureSwitcherModifier _beginAnimatingRampingProperty];
-[SBSceneResizeGestureSwitcherModifier _currentActionWithProjection:];
-[SBSceneResizeGestureSwitcherModifier _handleGestureEventBeganWithEvent:];
-[SBSceneResizeGestureSwitcherModifier _handleGestureEventChangedWithEvent:];
-[SBSceneResizeGestureSwitcherModifier _handleGestureEventEndedWithEvent:];
-[SBSceneResizeGestureSwitcherModifier _minimumCardWidthForDismissalAction];
-[SBSceneResizeGestureSwitcherModifier _normalizedDismissLeftProgress];
-[SBSceneResizeGestureSwitcherModifier _normalizedHalfHalfProgress];
-[SBSceneResizeGestureSwitcherModifier _normalizedHorizontalLocationWithProjection:];
-[SBSceneResizeGestureSwitcherModifier _normalizedNarrowWideProgress];
-[SBSceneResizeGestureSwitcherModifier _normalizedPeekDismissLeftProgress];
-[SBSceneResizeGestureSwitcherModifier _normalizedPeekDismissRightProgress];
-[SBSceneResizeGestureSwitcherModifier _normalizedProgressBetweenHalfHalfAndWideNarrow];
-[SBSceneResizeGestureSwitcherModifier _normalizedProgressBetweenNarrowWideAndHalfHalf];
-[SBSceneResizeGestureSwitcherModifier _normalizedWideNarrowProgress];
-[SBSceneResizeGestureSwitcherModifier _presentationActionForNormalizedProgress:];
-[SBSceneResizeGestureSwitcherModifier _responseForGestureUpdateWithPause:gestureIsEnding:];
-[SBSceneResizeGestureSwitcherModifier _rubberbandingRange];
-[SBSceneResizeGestureSwitcherModifier _switcherWidth];
-[SBSceneResizeGestureSwitcherModifier initWithGestureID:appLayout:spaceConfiguration:];
```
