# `SBAssistantIslandSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 36 instance variables, 36 properties, 73 instance methods, 2 class methods

## Instance variables

```
B _systemApertureCompactEnabled;
B _systemApertureUnifiedAnimationEnabled;
B _homeScreenTranslationEnabled;
B _homeScreenScaleEnabled;
B _showSliders;
d _defaultActivityGlassShadowOpacity;
d _defaultActivitySearchTopInset;
d _defaultActivitySearchContentInset;
d _defaultActivitySearchWidth;
d _defaultActivitySearchHeight;
d _defaultActivitySearchCornerRadius;
d _defaultActivityVoiceTopInset;
d _defaultActivityVoiceSystemApertureTopOutset;
d _defaultActivityVoiceWidth;
d _defaultActivityVoiceHeight;
d _defaultActivityVoiceCornerRadius;
d _defaultActivityThinkingTopInset;
d _defaultActivityThinkingWidth;
d _defaultActivityThinkingHeight;
d _defaultActivityThinkingCornerRadius;
d _systemAperturePresentationOutsetLeft;
d _systemAperturePresentationOutsetRight;
d _floatingPresentationStatusBarOutset;
d _topEdgeZoneAssistantIslandLeadingBoundaryFraction;
d _topEdgeZoneAssistantIslandTrailingBoundaryFraction;
d _maxTranslationForHomeScreenScale;
d _homeScreenScaleRubberbandingMin;
d _homeScreenScaleRubberbandingMax;
d _homeScreenScaleRubberbandingRange;
@"SBFFluidBehaviorSettings" _homeScreenScaleAnimationSettings;
d _listeningThinkingWaveLensingHeight;
d _listeningThinkingWaveLensingAmount;
d _listeningThinkingWaveInitialGaussianRadius;
d _listeningThinkingWaveActiveGaussianRadius;
d _listeningThinkingWaveVariableBlurRadius;
d _listeningThinkingWaveVariableBlurLocation;
```

## Properties

```
@property (TB,V_showSliders) showSliders;
@property (Td,N,V_defaultActivityGlassShadowOpacity) defaultActivityGlassShadowOpacity;
@property (Td,N,V_defaultActivitySearchTopInset) defaultActivitySearchTopInset;
@property (Td,N,V_defaultActivitySearchContentInset) defaultActivitySearchContentInset;
@property (Td,N,V_defaultActivitySearchWidth) defaultActivitySearchWidth;
@property (Td,N,V_defaultActivitySearchHeight) defaultActivitySearchHeight;
@property (Td,N,V_defaultActivitySearchCornerRadius) defaultActivitySearchCornerRadius;
@property (Td,N,V_defaultActivityVoiceTopInset) defaultActivityVoiceTopInset;
@property (Td,N,V_defaultActivityVoiceSystemApertureTopOutset) defaultActivityVoiceSystemApertureTopOutset;
@property (Td,N,V_defaultActivityVoiceWidth) defaultActivityVoiceWidth;
@property (Td,N,V_defaultActivityVoiceHeight) defaultActivityVoiceHeight;
@property (Td,N,V_defaultActivityVoiceCornerRadius) defaultActivityVoiceCornerRadius;
@property (Td,N,V_defaultActivityThinkingTopInset) defaultActivityThinkingTopInset;
@property (Td,N,V_defaultActivityThinkingWidth) defaultActivityThinkingWidth;
@property (Td,N,V_defaultActivityThinkingHeight) defaultActivityThinkingHeight;
@property (Td,N,V_defaultActivityThinkingCornerRadius) defaultActivityThinkingCornerRadius;
@property (Td,N,V_systemAperturePresentationOutsetLeft) systemAperturePresentationOutsetLeft;
@property (Td,N,V_systemAperturePresentationOutsetRight) systemAperturePresentationOutsetRight;
@property (Td,N,V_floatingPresentationStatusBarOutset) floatingPresentationStatusBarOutset;
@property (Td,N,V_topEdgeZoneAssistantIslandLeadingBoundaryFraction) topEdgeZoneAssistantIslandLeadingBoundaryFraction;
@property (Td,N,V_topEdgeZoneAssistantIslandTrailingBoundaryFraction) topEdgeZoneAssistantIslandTrailingBoundaryFraction;
@property (TB,N,V_systemApertureCompactEnabled) systemApertureCompactEnabled;
@property (TB,N,V_systemApertureUnifiedAnimationEnabled) systemApertureUnifiedAnimationEnabled;
@property (TB,N,GisHomeScreenTranslationEnabled,V_homeScreenTranslationEnabled) homeScreenTranslationEnabled;
@property (TB,N,GisHomeScreenScaleEnabled,V_homeScreenScaleEnabled) homeScreenScaleEnabled;
@property (Td,N,V_maxTranslationForHomeScreenScale) maxTranslationForHomeScreenScale;
@property (Td,N,V_homeScreenScaleRubberbandingMin) homeScreenScaleRubberbandingMin;
@property (Td,N,V_homeScreenScaleRubberbandingMax) homeScreenScaleRubberbandingMax;
@property (Td,N,V_homeScreenScaleRubberbandingRange) homeScreenScaleRubberbandingRange;
@property (T@"SBFFluidBehaviorSettings",&,N,V_homeScreenScaleAnimationSettings) homeScreenScaleAnimationSettings;
@property (Td,N,V_listeningThinkingWaveLensingHeight) listeningThinkingWaveLensingHeight;
@property (Td,N,V_listeningThinkingWaveLensingAmount) listeningThinkingWaveLensingAmount;
@property (Td,N,V_listeningThinkingWaveInitialGaussianRadius) listeningThinkingWaveInitialGaussianRadius;
@property (Td,N,V_listeningThinkingWaveActiveGaussianRadius) listeningThinkingWaveActiveGaussianRadius;
@property (Td,N,V_listeningThinkingWaveVariableBlurRadius) listeningThinkingWaveVariableBlurRadius;
@property (Td,N,V_listeningThinkingWaveVariableBlurLocation) listeningThinkingWaveVariableBlurLocation;
```

## Class methods

```
+[SBAssistantIslandSettings settingsControllerModule];
+[SBAssistantIslandSettings _isV68Like];
```

## Instance methods

```
-[SBAssistantIslandSettings setDefaultValues];
-[SBAssistantIslandSettings defaultActivityThinkingTopInset];
-[SBAssistantIslandSettings setShowSliders:];
-[SBAssistantIslandSettings defaultActivityGlassShadowOpacity];
-[SBAssistantIslandSettings defaultActivitySearchContentInset];
-[SBAssistantIslandSettings defaultActivitySearchCornerRadius];
-[SBAssistantIslandSettings defaultActivitySearchTopInset];
-[SBAssistantIslandSettings defaultActivityThinkingCornerRadius];
-[SBAssistantIslandSettings defaultActivityVoiceCornerRadius];
-[SBAssistantIslandSettings defaultActivityVoiceTopInset];
-[SBAssistantIslandSettings listeningThinkingWaveActiveGaussianRadius];
-[SBAssistantIslandSettings listeningThinkingWaveInitialGaussianRadius];
-[SBAssistantIslandSettings listeningThinkingWaveLensingAmount];
-[SBAssistantIslandSettings listeningThinkingWaveLensingHeight];
-[SBAssistantIslandSettings listeningThinkingWaveVariableBlurLocation];
-[SBAssistantIslandSettings listeningThinkingWaveVariableBlurRadius];
-[SBAssistantIslandSettings setDefaultActivityGlassShadowOpacity:];
-[SBAssistantIslandSettings setDefaultActivitySearchContentInset:];
-[SBAssistantIslandSettings setDefaultActivitySearchCornerRadius:];
-[SBAssistantIslandSettings setDefaultActivitySearchTopInset:];
-[SBAssistantIslandSettings setDefaultActivityThinkingCornerRadius:];
-[SBAssistantIslandSettings setDefaultActivityThinkingTopInset:];
-[SBAssistantIslandSettings setDefaultActivityVoiceCornerRadius:];
-[SBAssistantIslandSettings setDefaultActivityVoiceTopInset:];
-[SBAssistantIslandSettings setListeningThinkingWaveActiveGaussianRadius:];
-[SBAssistantIslandSettings setListeningThinkingWaveInitialGaussianRadius:];
-[SBAssistantIslandSettings setListeningThinkingWaveLensingAmount:];
-[SBAssistantIslandSettings setListeningThinkingWaveLensingHeight:];
-[SBAssistantIslandSettings setListeningThinkingWaveVariableBlurLocation:];
-[SBAssistantIslandSettings setListeningThinkingWaveVariableBlurRadius:];
-[SBAssistantIslandSettings showSliders];
-[SBAssistantIslandSettings homeScreenScaleRubberbandingMin];
-[SBAssistantIslandSettings setDefaultActivitySearchHeight:];
-[SBAssistantIslandSettings homeScreenScaleRubberbandingMax];
-[SBAssistantIslandSettings defaultActivitySearchHeight];
-[SBAssistantIslandSettings defaultActivitySearchWidth];
-[SBAssistantIslandSettings defaultActivityThinkingHeight];
-[SBAssistantIslandSettings defaultActivityThinkingWidth];
-[SBAssistantIslandSettings defaultActivityVoiceHeight];
-[SBAssistantIslandSettings defaultActivityVoiceSystemApertureTopOutset];
-[SBAssistantIslandSettings defaultActivityVoiceWidth];
-[SBAssistantIslandSettings floatingPresentationStatusBarOutset];
-[SBAssistantIslandSettings homeScreenScaleAnimationSettings];
-[SBAssistantIslandSettings homeScreenScaleRubberbandingRange];
-[SBAssistantIslandSettings isHomeScreenScaleEnabled];
-[SBAssistantIslandSettings isHomeScreenTranslationEnabled];
-[SBAssistantIslandSettings maxTranslationForHomeScreenScale];
-[SBAssistantIslandSettings setDefaultActivitySearchWidth:];
-[SBAssistantIslandSettings setDefaultActivityThinkingHeight:];
-[SBAssistantIslandSettings setDefaultActivityThinkingWidth:];
-[SBAssistantIslandSettings setDefaultActivityVoiceHeight:];
-[SBAssistantIslandSettings setDefaultActivityVoiceSystemApertureTopOutset:];
-[SBAssistantIslandSettings setDefaultActivityVoiceWidth:];
-[SBAssistantIslandSettings setFloatingPresentationStatusBarOutset:];
-[SBAssistantIslandSettings setHomeScreenScaleAnimationSettings:];
-[SBAssistantIslandSettings setHomeScreenScaleEnabled:];
-[SBAssistantIslandSettings setHomeScreenScaleRubberbandingMax:];
-[SBAssistantIslandSettings setHomeScreenScaleRubberbandingMin:];
-[SBAssistantIslandSettings setHomeScreenScaleRubberbandingRange:];
-[SBAssistantIslandSettings setHomeScreenTranslationEnabled:];
-[SBAssistantIslandSettings setMaxTranslationForHomeScreenScale:];
-[SBAssistantIslandSettings setSystemApertureCompactEnabled:];
-[SBAssistantIslandSettings setSystemAperturePresentationOutsetLeft:];
-[SBAssistantIslandSettings setSystemAperturePresentationOutsetRight:];
-[SBAssistantIslandSettings setSystemApertureUnifiedAnimationEnabled:];
-[SBAssistantIslandSettings setTopEdgeZoneAssistantIslandLeadingBoundaryFraction:];
-[SBAssistantIslandSettings setTopEdgeZoneAssistantIslandTrailingBoundaryFraction:];
-[SBAssistantIslandSettings systemApertureCompactEnabled];
-[SBAssistantIslandSettings systemAperturePresentationOutsetLeft];
-[SBAssistantIslandSettings systemAperturePresentationOutsetRight];
-[SBAssistantIslandSettings systemApertureUnifiedAnimationEnabled];
-[SBAssistantIslandSettings topEdgeZoneAssistantIslandLeadingBoundaryFraction];
-[SBAssistantIslandSettings topEdgeZoneAssistantIslandTrailingBoundaryFraction];
```
