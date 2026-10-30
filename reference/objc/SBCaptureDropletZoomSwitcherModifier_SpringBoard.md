# `SBCaptureDropletZoomSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 9 instance variables, 0 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"SBCaptureButtonSettings" _settings;
@"SBAppLayout" _appLayout;
@"SBSwitcherModifier" _zoomModifier;
@"<SBHardwareButtonLaunchPreludeAnimationToken>" _preludeAnimationToken;
@"<SBHardwareButtonLaunchZoomUpAnimationToken>" _zoomupAnimationToken;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialDropletFrame;
B _dropletEffectRequired;
B _allowHomeScreenBlur;
B _shouldDimBackground;
```

## Instance methods

```
-[SBCaptureDropletZoomSwitcherModifier scaleForIndex:];
-[SBCaptureDropletZoomSwitcherModifier homeScreenBackdropBlurProgress];
-[SBCaptureDropletZoomSwitcherModifier didMoveToParentModifier:];
-[SBCaptureDropletZoomSwitcherModifier animationAttributesForLayoutElement:];
-[SBCaptureDropletZoomSwitcherModifier animatablePropertyIdentifiers];
-[SBCaptureDropletZoomSwitcherModifier topMostLayoutElements];
-[SBCaptureDropletZoomSwitcherModifier visibleAppLayouts];
-[SBCaptureDropletZoomSwitcherModifier updateModeForAnimatableProperty:];
-[SBCaptureDropletZoomSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBCaptureDropletZoomSwitcherModifier transitionDidEnd];
-[SBCaptureDropletZoomSwitcherModifier handleTimerEvent:];
-[SBCaptureDropletZoomSwitcherModifier frameForIndex:];
-[SBCaptureDropletZoomSwitcherModifier transitionWillBegin];
-[SBCaptureDropletZoomSwitcherModifier isDropletEffectRequiredBehindAppLayout:];
-[SBCaptureDropletZoomSwitcherModifier completesWhenChildrenComplete];
-[SBCaptureDropletZoomSwitcherModifier wantsBezelEffectsLayoutElement];
-[SBCaptureDropletZoomSwitcherModifier switcherDimmingAlpha];
-[SBCaptureDropletZoomSwitcherModifier wantsSwitcherDimmingView];
-[SBCaptureDropletZoomSwitcherModifier settingsForAnimatableProperty:];
-[SBCaptureDropletZoomSwitcherModifier modelValueForAnimatableProperty:currentValue:creating:];
-[SBCaptureDropletZoomSwitcherModifier handleAnimatablePropertyChangedEvent:];
-[SBCaptureDropletZoomSwitcherModifier handleHardwareButtonDropletAnimationEvent:];
-[SBCaptureDropletZoomSwitcherModifier initWithTransitionID:zoomModifier:appLayout:launchPreludeAnimationToken:];
```
