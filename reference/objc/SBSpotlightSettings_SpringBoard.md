# `SBSpotlightSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 21 instance variables, 21 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"SBFFluidBehaviorSettings" _opacityAnimationSettings;
@"SBFFluidBehaviorSettings" _snappyOpacityAnimationSettings;
@"SBFFluidBehaviorSettings" _scaleAnimationSettings;
@"SBFFluidBehaviorSettings" _snappyScaleAnimationSettings;
d _anchorPointY;
d _hiddenScale;
d _hiddenBlurRadius;
d _minTranslationToShowSpotlight;
d _maxTranslationForSpotlightScale;
d _spotlightScaleRubberbandingMin;
d _spotlightScaleRubberbandingMax;
d _spotlightScaleRubberbandingRange;
d _maxTranslationForHomeScreenScale;
d _homeScreenScaleRubberbandingMin;
d _homeScreenScaleRubberbandingMax;
d _homeScreenScaleRubberbandingRange;
d _maxTranslationForDimmingView;
d _dimmingViewRubberbandingMin;
d _dimmingViewRubberbandingMax;
d _dimmingViewRubberbandingRange;
d _spotlightTranslationRubberbandingRange;
```

## Properties

```
@property (T@"SBFFluidBehaviorSettings",&,N,V_opacityAnimationSettings) opacityAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_snappyOpacityAnimationSettings) snappyOpacityAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_scaleAnimationSettings) scaleAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_snappyScaleAnimationSettings) snappyScaleAnimationSettings;
@property (Td,N,V_anchorPointY) anchorPointY;
@property (Td,N,V_hiddenScale) hiddenScale;
@property (Td,N,V_hiddenBlurRadius) hiddenBlurRadius;
@property (Td,N,V_minTranslationToShowSpotlight) minTranslationToShowSpotlight;
@property (Td,N,V_maxTranslationForSpotlightScale) maxTranslationForSpotlightScale;
@property (Td,N,V_spotlightScaleRubberbandingMin) spotlightScaleRubberbandingMin;
@property (Td,N,V_spotlightScaleRubberbandingMax) spotlightScaleRubberbandingMax;
@property (Td,N,V_spotlightScaleRubberbandingRange) spotlightScaleRubberbandingRange;
@property (Td,N,V_maxTranslationForHomeScreenScale) maxTranslationForHomeScreenScale;
@property (Td,N,V_homeScreenScaleRubberbandingMin) homeScreenScaleRubberbandingMin;
@property (Td,N,V_homeScreenScaleRubberbandingMax) homeScreenScaleRubberbandingMax;
@property (Td,N,V_homeScreenScaleRubberbandingRange) homeScreenScaleRubberbandingRange;
@property (Td,N,V_maxTranslationForDimmingView) maxTranslationForDimmingView;
@property (Td,N,V_dimmingViewRubberbandingMin) dimmingViewRubberbandingMin;
@property (Td,N,V_dimmingViewRubberbandingMax) dimmingViewRubberbandingMax;
@property (Td,N,V_dimmingViewRubberbandingRange) dimmingViewRubberbandingRange;
@property (Td,N,V_spotlightTranslationRubberbandingRange) spotlightTranslationRubberbandingRange;
```

## Class methods

```
+[SBSpotlightSettings settingsControllerModule];
```

## Instance methods

```
-[SBSpotlightSettings setDefaultValues];
-[SBSpotlightSettings homeScreenScaleRubberbandingMin];
-[SBSpotlightSettings maxTranslationForSpotlightScale];
-[SBSpotlightSettings setDimmingViewRubberbandingMax:];
-[SBSpotlightSettings homeScreenScaleRubberbandingMax];
-[SBSpotlightSettings setDimmingViewRubberbandingMin:];
-[SBSpotlightSettings setHiddenScale:];
-[SBSpotlightSettings anchorPointY];
-[SBSpotlightSettings dimmingViewRubberbandingMax];
-[SBSpotlightSettings dimmingViewRubberbandingMin];
-[SBSpotlightSettings dimmingViewRubberbandingRange];
-[SBSpotlightSettings hiddenBlurRadius];
-[SBSpotlightSettings hiddenScale];
-[SBSpotlightSettings homeScreenScaleRubberbandingRange];
-[SBSpotlightSettings maxTranslationForDimmingView];
-[SBSpotlightSettings maxTranslationForHomeScreenScale];
-[SBSpotlightSettings minTranslationToShowSpotlight];
-[SBSpotlightSettings opacityAnimationSettings];
-[SBSpotlightSettings scaleAnimationSettings];
-[SBSpotlightSettings setAnchorPointY:];
-[SBSpotlightSettings setDimmingViewRubberbandingRange:];
-[SBSpotlightSettings setHiddenBlurRadius:];
-[SBSpotlightSettings setHomeScreenScaleRubberbandingMax:];
-[SBSpotlightSettings setHomeScreenScaleRubberbandingMin:];
-[SBSpotlightSettings setHomeScreenScaleRubberbandingRange:];
-[SBSpotlightSettings setMaxTranslationForDimmingView:];
-[SBSpotlightSettings setMaxTranslationForHomeScreenScale:];
-[SBSpotlightSettings setMaxTranslationForSpotlightScale:];
-[SBSpotlightSettings setMinTranslationToShowSpotlight:];
-[SBSpotlightSettings setOpacityAnimationSettings:];
-[SBSpotlightSettings setScaleAnimationSettings:];
-[SBSpotlightSettings setSnappyOpacityAnimationSettings:];
-[SBSpotlightSettings setSnappyScaleAnimationSettings:];
-[SBSpotlightSettings setSpotlightScaleRubberbandingMax:];
-[SBSpotlightSettings setSpotlightScaleRubberbandingMin:];
-[SBSpotlightSettings setSpotlightScaleRubberbandingRange:];
-[SBSpotlightSettings setSpotlightTranslationRubberbandingRange:];
-[SBSpotlightSettings snappyOpacityAnimationSettings];
-[SBSpotlightSettings snappyScaleAnimationSettings];
-[SBSpotlightSettings spotlightScaleRubberbandingMax];
-[SBSpotlightSettings spotlightScaleRubberbandingMin];
-[SBSpotlightSettings spotlightScaleRubberbandingRange];
-[SBSpotlightSettings spotlightTranslationRubberbandingRange];
```
