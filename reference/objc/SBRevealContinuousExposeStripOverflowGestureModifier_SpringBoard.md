# `SBRevealContinuousExposeStripOverflowGestureModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- 9 instance variables, 1 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _isRevealingSwitcher;
@"NSString" _appExposeBundleIdentifier;
@"SBAppLayout" _initialAppLayout;
@"SBSwitcherModifier" _continuousExposeAppSwitcherModifier;
B _showingAppSwitcherLayout;
B _beginAnimatingAppSwitcherLayoutProperty;
d _translation;
d _stripWidth;
@"SBAppSwitcherDefaults" _appSwitcherDefaults;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_initialAppLayout) initialAppLayout;
```

## Instance methods

```
-[SBRevealContinuousExposeStripOverflowGestureModifier handleGestureEvent:];
-[SBRevealContinuousExposeStripOverflowGestureModifier scaleForIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier anchorPointForIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier titleOpacityForIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBRevealContinuousExposeStripOverflowGestureModifier cornerRadiiForIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier animationAttributesForLayoutElement:];
-[SBRevealContinuousExposeStripOverflowGestureModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier animatablePropertyIdentifiers];
-[SBRevealContinuousExposeStripOverflowGestureModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier handleTransitionEvent:];
-[SBRevealContinuousExposeStripOverflowGestureModifier shouldPinLayoutRolesToSpace:];
-[SBRevealContinuousExposeStripOverflowGestureModifier visibleAppLayouts];
-[SBRevealContinuousExposeStripOverflowGestureModifier updateModeForAnimatableProperty:];
-[SBRevealContinuousExposeStripOverflowGestureModifier perspectiveAngleForIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier shadowOpacityForLayoutRole:atIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier scaleForLayoutRole:inAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBRevealContinuousExposeStripOverflowGestureModifier frameForIndex:];
-[SBRevealContinuousExposeStripOverflowGestureModifier shouldUpdateAnimatableProperty:];
-[SBRevealContinuousExposeStripOverflowGestureModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier modelValueForAnimatableProperty:currentValue:creating:];
-[SBRevealContinuousExposeStripOverflowGestureModifier contentPageViewScaleForAppLayout:withScale:];
-[SBRevealContinuousExposeStripOverflowGestureModifier _appSwitcherDefaults];
-[SBRevealContinuousExposeStripOverflowGestureModifier _finalScaleForFullScreenAppLayout];
-[SBRevealContinuousExposeStripOverflowGestureModifier _hideDock];
-[SBRevealContinuousExposeStripOverflowGestureModifier _layoutSettingsForAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier initWithGestureID:initialAppLayout:];
-[SBRevealContinuousExposeStripOverflowGestureModifier initialAppLayout];
```
