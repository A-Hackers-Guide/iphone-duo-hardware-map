# `SBFlexibleWindowingWindowDragSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- Protocols: `SBContinuousExposeWindowDragDestinationSwitcherModifierDelegate`
- 40 instance variables, 11 properties, 58 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _location;
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _averageVelocity;
{CGPoint="x"d"y"d} _anchorPoint;
{CGPoint="x"d"y"d} _initialAnchorPoint;
{CGPoint="x"d"y"d} _initialNormalizedCenter;
B _gestureWasCanceled;
B _prefersInitialLayout;
d _detachmentThreshold;
{CGPoint="x"d"y"d} _initialLocation;
{CGPoint="x"d"y"d} _rubberBandedTranslation;
{CGSize="width"d"height"d} _sizeOfSelectedDisplayItem;
B _dragBeganInOurSwitcher;
B _dragBeganInOtherSwitcher;
B _dragBeganInAnyStrip;
B _dragBeganOnAnyStage;
@"UIViewFloatAnimatableProperty" _anchorPointRampingProperty;
@"SBContinuousExposeWindowDragDestinationSwitcherModifier" _destinationModifier;
@"SBFlexibleWindowingAutoLayoutSpace" _initialAutoLayoutSpace;
@"SBFlexibleWindowingAutoLayoutSpace" _previousAutoLayoutSpace;
@"SBFlexibleWindowingAutoLayoutController" _autoLayoutController;
{SBWindowControlsLayout="style"q"underlapsStatusBar"B"margin"{CGPoint="x"d"y"d}} _currentWindowControlsLayout;
B _draggedDisplayItemIntersectsHomeAffordanceArea;
@"SBDisplayItemLayoutGrid" _layoutGrid;
B _selectedAppLayoutWasInitiallyFullScreen;
@"SBDisplayItemLayoutAttributes" _initialLayoutAttributes;
B _slideOverIsCenterExiting;
B _layOutSlideOverItemFullyOffscreen;
B _startedStashed;
B _hasUnstashed;
d _lastCenterYBeforeStashingOrUnstashingBegan;
q _slideOverCenterExitingUpdateGeneration;
@"NSString" _slideOverCenterExitingUpdateReason;
{SBDisplayItemSlideOverConfiguration="corner"q"yOffsetFromCorner"d"size"{CGSize="width"d"height"d}"isActive"B"isStashed"B"dodgesDock"B} _initialSlideOverConfiguration;
{CGPoint="x"d"y"d} _centerExitingEntryPoint;
B _wantsSlideOverTongue;
Q _slideOverTongueState;
Q _slideOverTongueDirection;
@"SBAppLayout" _initialAppLayout;
@"SBDisplayItem" _selectedDisplayItem;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_initialAppLayout) initialAppLayout;
@property (T@"SBDisplayItem",R,N,V_selectedDisplayItem) selectedDisplayItem;
@property (T@"SBAppLayout",R,N) proposedAppLayout;
@property (T@"SBAppLayout",R,N) hoveringOverAppLayout;
@property (TB,R,N,V_wantsSlideOverTongue) wantsSlideOverTongue;
@property (TQ,R,N,V_slideOverTongueState) slideOverTongueState;
@property (TQ,R,N,V_slideOverTongueDirection) slideOverTongueDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFlexibleWindowingWindowDragSwitcherModifier handleGestureEvent:];
-[SBFlexibleWindowingWindowDragSwitcherModifier scaleForIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier anchorPointForIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFlexibleWindowingWindowDragSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBFlexibleWindowingWindowDragSwitcherModifier handleEvent:];
-[SBFlexibleWindowingWindowDragSwitcherModifier didMoveToParentModifier:];
-[SBFlexibleWindowingWindowDragSwitcherModifier cornerRadiiForIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier animationAttributesForLayoutElement:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutOnStage];
-[SBFlexibleWindowingWindowDragSwitcherModifier topMostLayoutElements];
-[SBFlexibleWindowingWindowDragSwitcherModifier isSwitcherWindowVisible];
-[SBFlexibleWindowingWindowDragSwitcherModifier titleAndIconOpacityForIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFlexibleWindowingWindowDragSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier handleTransitionEvent:];
-[SBFlexibleWindowingWindowDragSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBFlexibleWindowingWindowDragSwitcherModifier visibleAppLayouts];
-[SBFlexibleWindowingWindowDragSwitcherModifier perspectiveAngleForIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayout];
-[SBFlexibleWindowingWindowDragSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier handleTimerEvent:];
-[SBFlexibleWindowingWindowDragSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBFlexibleWindowingWindowDragSwitcherModifier frameForIndex:];
-[SBFlexibleWindowingWindowDragSwitcherModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier wantsSlideOverTongue];
-[SBFlexibleWindowingWindowDragSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:];
-[SBFlexibleWindowingWindowDragSwitcherModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier slideOverTongueDirection];
-[SBFlexibleWindowingWindowDragSwitcherModifier isHitTestBlockingViewVisible];
-[SBFlexibleWindowingWindowDragSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier shadowStyleForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier _appLayoutContainingDisplayItem:];
-[SBFlexibleWindowingWindowDragSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutToAttachSlideOverTongue];
-[SBFlexibleWindowingWindowDragSwitcherModifier slideOverTongueState];
-[SBFlexibleWindowingWindowDragSwitcherModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier descriptionBuilderWithMultilinePrefix:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBFlexibleWindowingWindowDragSwitcherModifier _isStripStashed];
-[SBFlexibleWindowingWindowDragSwitcherModifier _anyProposedAppLayoutContainsSelectedDisplayItem];
-[SBFlexibleWindowingWindowDragSwitcherModifier _baseLayoutSettings];
-[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingAnchorPointRampingPropertyWithMode:settings:];
-[SBFlexibleWindowingWindowDragSwitcherModifier _draggingItemScreenCenterForSize:scale:];
-[SBFlexibleWindowingWindowDragSwitcherModifier _performSlideOverConfigurationUpdateWithConfiguration:appLayout:layoutAttributes:];
-[SBFlexibleWindowingWindowDragSwitcherModifier _shouldLockYPosition];
-[SBFlexibleWindowingWindowDragSwitcherModifier _slideOverCenterExitRemainingTimeWithSettledDuration:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutByAddingAppLayout:toAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutContainingAppLayout:];
-[SBFlexibleWindowingWindowDragSwitcherModifier continuousExposeStripProgress];
-[SBFlexibleWindowingWindowDragSwitcherModifier hoveringOverAppLayout];
-[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:];
-[SBFlexibleWindowingWindowDragSwitcherModifier initialAppLayout];
-[SBFlexibleWindowingWindowDragSwitcherModifier preferredCenterForSelectedItemInDestinationModifier:clippingToInitialStageArea:];
-[SBFlexibleWindowingWindowDragSwitcherModifier proposedAppLayout];
-[SBFlexibleWindowingWindowDragSwitcherModifier selectedDisplayItem];
-[SBFlexibleWindowingWindowDragSwitcherModifier slideOverIsCenterExiting];
-[SBFlexibleWindowingWindowDragSwitcherModifier updateProposedAppLayoutWithAppLayout:andInitialAppLayout:];
```
