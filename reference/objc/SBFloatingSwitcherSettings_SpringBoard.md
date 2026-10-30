# `SBFloatingSwitcherSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 25 instance variables, 25 properties, 52 instance methods, 1 class methods

## Instance variables

```
B _showFloats;
d _switcherCardScale;
d _cardSpacing;
d _dimmingAlpha;
d _leadingEdgeRubberbandingRange;
d _perCardAdditionalScaleCoefficient;
d _scaleCurveExponent;
d _opacityMinimumDistanceThreshold;
d _opacityFadeDistance;
d _darkeningMinimumDistanceThreshold;
d _darkeningFadeDistance;
d _maximumDarkening;
d _titleAndIconOpacityMinimumDistanceThreshold;
d _titleAndIconOpacityFadeDistance;
d _titleOpacityMinimumDistanceThreshold;
d _titleOpacityFadeDistance;
d _overshootPullbackDelayOffscreen;
d _overshootPullbackDelayOnscreen;
d _rightEdgePeekDelay;
d _rightEdgePeekTimeout;
@"SBFFluidBehaviorSettings" _tongueContainerPositionAnimationSettings;
@"SBFFluidBehaviorSettings" _tongueContainerTransformAnimationSettings;
@"SBFFluidBehaviorSettings" _tongueCollapsedToExpandedAnimationSettings;
@"SBFFluidBehaviorSettings" _tongueExpandedToCollapsedAnimationSettings;
@"MTLumaDodgePillSettings" _homeAffordanceSettings;
```

## Properties

```
@property (TB,V_showFloats) showFloats;
@property (Td,V_switcherCardScale) switcherCardScale;
@property (Td,V_cardSpacing) cardSpacing;
@property (Td,V_dimmingAlpha) dimmingAlpha;
@property (Td,V_leadingEdgeRubberbandingRange) leadingEdgeRubberbandingRange;
@property (Td,V_perCardAdditionalScaleCoefficient) perCardAdditionalScaleCoefficient;
@property (Td,V_scaleCurveExponent) scaleCurveExponent;
@property (Td,V_opacityMinimumDistanceThreshold) opacityMinimumDistanceThreshold;
@property (Td,V_opacityFadeDistance) opacityFadeDistance;
@property (Td,V_darkeningMinimumDistanceThreshold) darkeningMinimumDistanceThreshold;
@property (Td,V_darkeningFadeDistance) darkeningFadeDistance;
@property (Td,V_maximumDarkening) maximumDarkening;
@property (Td,V_titleAndIconOpacityMinimumDistanceThreshold) titleAndIconOpacityMinimumDistanceThreshold;
@property (Td,V_titleAndIconOpacityFadeDistance) titleAndIconOpacityFadeDistance;
@property (Td,V_titleOpacityMinimumDistanceThreshold) titleOpacityMinimumDistanceThreshold;
@property (Td,V_titleOpacityFadeDistance) titleOpacityFadeDistance;
@property (Td,V_overshootPullbackDelayOffscreen) overshootPullbackDelayOffscreen;
@property (Td,V_overshootPullbackDelayOnscreen) overshootPullbackDelayOnscreen;
@property (Td,V_rightEdgePeekDelay) rightEdgePeekDelay;
@property (Td,V_rightEdgePeekTimeout) rightEdgePeekTimeout;
@property (T@"SBFFluidBehaviorSettings",&,V_tongueContainerPositionAnimationSettings) tongueContainerPositionAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,V_tongueContainerTransformAnimationSettings) tongueContainerTransformAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,V_tongueCollapsedToExpandedAnimationSettings) tongueCollapsedToExpandedAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,V_tongueExpandedToCollapsedAnimationSettings) tongueExpandedToCollapsedAnimationSettings;
@property (T@"MTLumaDodgePillSettings",&,V_homeAffordanceSettings) homeAffordanceSettings;
```

## Class methods

```
+[SBFloatingSwitcherSettings settingsControllerModule];
```

## Instance methods

```
-[SBFloatingSwitcherSettings setSwitcherCardScale:];
-[SBFloatingSwitcherSettings switcherCardScale];
-[SBFloatingSwitcherSettings archiveValueForKey:];
-[SBFloatingSwitcherSettings setDefaultValues];
-[SBFloatingSwitcherSettings setShowFloats:];
-[SBFloatingSwitcherSettings dimmingAlpha];
-[SBFloatingSwitcherSettings showFloats];
-[SBFloatingSwitcherSettings setDimmingAlpha:];
-[SBFloatingSwitcherSettings opacityMinimumDistanceThreshold];
-[SBFloatingSwitcherSettings overshootPullbackDelayOffscreen];
-[SBFloatingSwitcherSettings setCardSpacing:];
-[SBFloatingSwitcherSettings titleAndIconOpacityFadeDistance];
-[SBFloatingSwitcherSettings cardSpacing];
-[SBFloatingSwitcherSettings darkeningFadeDistance];
-[SBFloatingSwitcherSettings darkeningMinimumDistanceThreshold];
-[SBFloatingSwitcherSettings homeAffordanceSettings];
-[SBFloatingSwitcherSettings leadingEdgeRubberbandingRange];
-[SBFloatingSwitcherSettings maximumDarkening];
-[SBFloatingSwitcherSettings opacityFadeDistance];
-[SBFloatingSwitcherSettings overshootPullbackDelayOnscreen];
-[SBFloatingSwitcherSettings perCardAdditionalScaleCoefficient];
-[SBFloatingSwitcherSettings rightEdgePeekDelay];
-[SBFloatingSwitcherSettings rightEdgePeekTimeout];
-[SBFloatingSwitcherSettings scaleCurveExponent];
-[SBFloatingSwitcherSettings setDarkeningFadeDistance:];
-[SBFloatingSwitcherSettings setDarkeningMinimumDistanceThreshold:];
-[SBFloatingSwitcherSettings setHomeAffordanceSettings:];
-[SBFloatingSwitcherSettings setLeadingEdgeRubberbandingRange:];
-[SBFloatingSwitcherSettings setMaximumDarkening:];
-[SBFloatingSwitcherSettings setOpacityFadeDistance:];
-[SBFloatingSwitcherSettings setOpacityMinimumDistanceThreshold:];
-[SBFloatingSwitcherSettings setOvershootPullbackDelayOffscreen:];
-[SBFloatingSwitcherSettings setOvershootPullbackDelayOnscreen:];
-[SBFloatingSwitcherSettings setPerCardAdditionalScaleCoefficient:];
-[SBFloatingSwitcherSettings setRightEdgePeekDelay:];
-[SBFloatingSwitcherSettings setRightEdgePeekTimeout:];
-[SBFloatingSwitcherSettings setScaleCurveExponent:];
-[SBFloatingSwitcherSettings setTitleAndIconOpacityFadeDistance:];
-[SBFloatingSwitcherSettings setTitleAndIconOpacityMinimumDistanceThreshold:];
-[SBFloatingSwitcherSettings setTitleOpacityFadeDistance:];
-[SBFloatingSwitcherSettings setTitleOpacityMinimumDistanceThreshold:];
-[SBFloatingSwitcherSettings setTongueCollapsedToExpandedAnimationSettings:];
-[SBFloatingSwitcherSettings setTongueContainerPositionAnimationSettings:];
-[SBFloatingSwitcherSettings setTongueContainerTransformAnimationSettings:];
-[SBFloatingSwitcherSettings setTongueExpandedToCollapsedAnimationSettings:];
-[SBFloatingSwitcherSettings titleAndIconOpacityMinimumDistanceThreshold];
-[SBFloatingSwitcherSettings titleOpacityFadeDistance];
-[SBFloatingSwitcherSettings titleOpacityMinimumDistanceThreshold];
-[SBFloatingSwitcherSettings tongueCollapsedToExpandedAnimationSettings];
-[SBFloatingSwitcherSettings tongueContainerPositionAnimationSettings];
-[SBFloatingSwitcherSettings tongueContainerTransformAnimationSettings];
-[SBFloatingSwitcherSettings tongueExpandedToCollapsedAnimationSettings];
```
