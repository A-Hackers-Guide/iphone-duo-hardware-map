# `SBElasticHUDSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 43 instance variables, 43 properties, 87 instance methods, 1 class methods

## Instance variables

```
B _showDebugUI;
B _autoDismiss;
B _displayBrightnessKeyCommandsEnabled;
B _keyboardBrightnessKeyCommandsEnabled;
f _volumeStepDelta;
@"SBFFluidBehaviorSettings" _defaultTransitionSettings;
@"SBFFluidBehaviorSettings" _defaultPositionSettings;
@"SBFFluidBehaviorSettings" _baseToInitialTransitionSettings;
@"SBFFluidBehaviorSettings" _baseToInitialPositionSettings;
@"SBFFluidBehaviorSettings" _deflationTransitionSettings;
@"SBFFluidBehaviorSettings" _deflatingToBaseTransitionSettings;
@"SBFFluidBehaviorSettings" _deflatingToBasePositionSettings;
@"SBFFluidBehaviorSettings" _generalToBaseTransitionSettings;
@"SBFFluidBehaviorSettings" _compactToBaseTransitionSettings;
d _baseScaleFactor;
d _deflatedScaleFactor;
d _compactStretchAmount;
d _interactingStretchAmount;
d _labelPadding;
d _dismissalInterval;
d _deflationDismissalInterval;
d _postTransitionDismissalInterval;
d _dimmingAlpha;
d _legibilityStrength;
d _onscreenTopMargin;
d _offscreenTopMargin;
d _landscapeCornerRadiusFraction;
d _volumeButtonsCenterY;
d _onscreenLeadingMargin;
d _offscreenLeadingMargin;
d _portraitCornerRadiusFraction;
d _landscapeState1Width;
d _landscapeState2Width;
d _landscapeState3Width;
d _landscapeState1Height;
d _landscapeState2Height;
d _landscapeState3Height;
d _portraitState1Width;
d _portraitState2Width;
d _portraitState3Width;
d _portraitState1Height;
d _portraitState2Height;
d _portraitState3Height;
```

## Properties

```
@property (T@"SBFFluidBehaviorSettings",&,N,V_defaultTransitionSettings) defaultTransitionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_defaultPositionSettings) defaultPositionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_baseToInitialTransitionSettings) baseToInitialTransitionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_baseToInitialPositionSettings) baseToInitialPositionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_deflationTransitionSettings) deflationTransitionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_deflatingToBaseTransitionSettings) deflatingToBaseTransitionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_deflatingToBasePositionSettings) deflatingToBasePositionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_generalToBaseTransitionSettings) generalToBaseTransitionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_compactToBaseTransitionSettings) compactToBaseTransitionSettings;
@property (Td,N,V_baseScaleFactor) baseScaleFactor;
@property (Td,N,V_deflatedScaleFactor) deflatedScaleFactor;
@property (Td,N,V_compactStretchAmount) compactStretchAmount;
@property (Td,N,V_interactingStretchAmount) interactingStretchAmount;
@property (Td,N,V_labelPadding) labelPadding;
@property (Td,N,V_dismissalInterval) dismissalInterval;
@property (Td,N,V_deflationDismissalInterval) deflationDismissalInterval;
@property (Td,N,V_postTransitionDismissalInterval) postTransitionDismissalInterval;
@property (Td,N,V_dimmingAlpha) dimmingAlpha;
@property (Td,N,V_legibilityStrength) legibilityStrength;
@property (Td,N,V_onscreenTopMargin) onscreenTopMargin;
@property (Td,N,V_offscreenTopMargin) offscreenTopMargin;
@property (Td,N,V_landscapeCornerRadiusFraction) landscapeCornerRadiusFraction;
@property (Td,N,V_volumeButtonsCenterY) volumeButtonsCenterY;
@property (Td,N,V_onscreenLeadingMargin) onscreenLeadingMargin;
@property (Td,N,V_offscreenLeadingMargin) offscreenLeadingMargin;
@property (Td,N,V_portraitCornerRadiusFraction) portraitCornerRadiusFraction;
@property (Td,N,V_landscapeState1Width) landscapeState1Width;
@property (Td,N,V_landscapeState2Width) landscapeState2Width;
@property (Td,N,V_landscapeState3Width) landscapeState3Width;
@property (Td,N,V_landscapeState1Height) landscapeState1Height;
@property (Td,N,V_landscapeState2Height) landscapeState2Height;
@property (Td,N,V_landscapeState3Height) landscapeState3Height;
@property (Td,N,V_portraitState1Width) portraitState1Width;
@property (Td,N,V_portraitState2Width) portraitState2Width;
@property (Td,N,V_portraitState3Width) portraitState3Width;
@property (Td,N,V_portraitState1Height) portraitState1Height;
@property (Td,N,V_portraitState2Height) portraitState2Height;
@property (Td,N,V_portraitState3Height) portraitState3Height;
@property (TB,N,V_showDebugUI) showDebugUI;
@property (TB,N,V_autoDismiss) autoDismiss;
@property (Tf,N,V_volumeStepDelta) volumeStepDelta;
@property (TB,N,V_displayBrightnessKeyCommandsEnabled) displayBrightnessKeyCommandsEnabled;
@property (TB,N,V_keyboardBrightnessKeyCommandsEnabled) keyboardBrightnessKeyCommandsEnabled;
```

## Class methods

```
+[SBElasticHUDSettings settingsControllerModule];
```

## Instance methods

```
-[SBElasticHUDSettings volumeStepDelta];
-[SBElasticHUDSettings compactStretchAmount];
-[SBElasticHUDSettings setCompactToBaseTransitionSettings:];
-[SBElasticHUDSettings baseToInitialTransitionSettings];
-[SBElasticHUDSettings postTransitionDismissalInterval];
-[SBElasticHUDSettings setVolumeButtonsCenterY:];
-[SBElasticHUDSettings setLandscapeState1Height:];
-[SBElasticHUDSettings defaultTransitionSettings];
-[SBElasticHUDSettings setShowDebugUI:];
-[SBElasticHUDSettings setDeflatingToBasePositionSettings:];
-[SBElasticHUDSettings setPostTransitionDismissalInterval:];
-[SBElasticHUDSettings setGeneralToBaseTransitionSettings:];
-[SBElasticHUDSettings landscapeState2Height];
-[SBElasticHUDSettings landscapeState1Height];
-[SBElasticHUDSettings volumeButtonsCenterY];
-[SBElasticHUDSettings landscapeState1Width];
-[SBElasticHUDSettings generalToBaseTransitionSettings];
-[SBElasticHUDSettings baseToInitialPositionSettings];
-[SBElasticHUDSettings setOnscreenTopMargin:];
-[SBElasticHUDSettings setDefaultTransitionSettings:];
-[SBElasticHUDSettings offscreenLeadingMargin];
-[SBElasticHUDSettings setLegibilityStrength:];
-[SBElasticHUDSettings landscapeState2Width];
-[SBElasticHUDSettings setAutoDismiss:];
-[SBElasticHUDSettings portraitState2Width];
-[SBElasticHUDSettings keyboardBrightnessKeyCommandsEnabled];
-[SBElasticHUDSettings legibilityStrength];
-[SBElasticHUDSettings landscapeState3Width];
-[SBElasticHUDSettings offscreenTopMargin];
-[SBElasticHUDSettings setVolumeStepDelta:];
-[SBElasticHUDSettings deflatingToBasePositionSettings];
-[SBElasticHUDSettings dismissalInterval];
-[SBElasticHUDSettings setLandscapeCornerRadiusFraction:];
-[SBElasticHUDSettings landscapeCornerRadiusFraction];
-[SBElasticHUDSettings defaultPositionSettings];
-[SBElasticHUDSettings labelPadding];
-[SBElasticHUDSettings baseScaleFactor];
-[SBElasticHUDSettings deflatingToBaseTransitionSettings];
-[SBElasticHUDSettings setBaseToInitialPositionSettings:];
-[SBElasticHUDSettings setDeflationDismissalInterval:];
-[SBElasticHUDSettings setLandscapeState2Height:];
-[SBElasticHUDSettings interactingStretchAmount];
-[SBElasticHUDSettings portraitState2Height];
-[SBElasticHUDSettings landscapeState3Height];
-[SBElasticHUDSettings deflatedScaleFactor];
-[SBElasticHUDSettings setDefaultValues];
-[SBElasticHUDSettings setPortraitState3Height:];
-[SBElasticHUDSettings setDismissalInterval:];
-[SBElasticHUDSettings setLandscapeState3Width:];
-[SBElasticHUDSettings setBaseScaleFactor:];
-[SBElasticHUDSettings setDeflationTransitionSettings:];
-[SBElasticHUDSettings onscreenTopMargin];
-[SBElasticHUDSettings portraitCornerRadiusFraction];
-[SBElasticHUDSettings portraitState3Height];
-[SBElasticHUDSettings portraitState1Height];
-[SBElasticHUDSettings setDefaultPositionSettings:];
-[SBElasticHUDSettings setOffscreenLeadingMargin:];
-[SBElasticHUDSettings setDisplayBrightnessKeyCommandsEnabled:];
-[SBElasticHUDSettings onscreenLeadingMargin];
-[SBElasticHUDSettings setKeyboardBrightnessKeyCommandsEnabled:];
-[SBElasticHUDSettings showDebugUI];
-[SBElasticHUDSettings setPortraitState2Height:];
-[SBElasticHUDSettings deflationDismissalInterval];
-[SBElasticHUDSettings setDeflatedScaleFactor:];
-[SBElasticHUDSettings portraitState3Width];
-[SBElasticHUDSettings setLabelPadding:];
-[SBElasticHUDSettings dimmingAlpha];
-[SBElasticHUDSettings setOnscreenLeadingMargin:];
-[SBElasticHUDSettings setBaseToInitialTransitionSettings:];
-[SBElasticHUDSettings setLandscapeState1Width:];
-[SBElasticHUDSettings setPortraitState3Width:];
-[SBElasticHUDSettings setPortraitState1Width:];
-[SBElasticHUDSettings autoDismiss];
-[SBElasticHUDSettings displayBrightnessKeyCommandsEnabled];
-[SBElasticHUDSettings compactToBaseTransitionSettings];
-[SBElasticHUDSettings deflationTransitionSettings];
-[SBElasticHUDSettings setPortraitState2Width:];
-[SBElasticHUDSettings setCompactStretchAmount:];
-[SBElasticHUDSettings setPortraitCornerRadiusFraction:];
-[SBElasticHUDSettings setInteractingStretchAmount:];
-[SBElasticHUDSettings portraitState1Width];
-[SBElasticHUDSettings setOffscreenTopMargin:];
-[SBElasticHUDSettings setLandscapeState2Width:];
-[SBElasticHUDSettings setDeflatingToBaseTransitionSettings:];
-[SBElasticHUDSettings setLandscapeState3Height:];
-[SBElasticHUDSettings setDimmingAlpha:];
-[SBElasticHUDSettings setPortraitState1Height:];
```
