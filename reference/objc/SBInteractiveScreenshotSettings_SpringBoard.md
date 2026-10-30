# `SBInteractiveScreenshotSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 23 instance variables, 23 properties, 47 instance methods, 1 class methods

## Instance variables

```
B _enabled;
B _shouldAsynchronouslyRender;
B _shouldPreheat;
B _shouldInjectVelocity;
@"SBCornerPencilPanGestureSettings" _pencilGestureSettings;
@"SBCornerFingerPanGestureSettings" _fingerGestureSettings;
d _applicationTouchDelayHysteresis;
d _cornerRadiusVisibleProgressThreshold;
d _cropCornersVisibleProgressThreshold;
d _cropLinesVisibleProgressThreshold;
d _baseCornerTranslationDegrees;
d _projectionDecelerationRate;
d _rubberbandingRange;
d _normalizedDistanceForCommitThreshold;
d _horizontalTranslationFactor;
d _verticalTranslationFactor;
d _maximumInjectedVelocity;
d _disabledGestureCancellationDistance;
d _disabledGestureVelocityScale;
@"SBFFluidBehaviorSettings" _contentAnimationSettings;
@"SBFFluidBehaviorSettings" _disabledGestureContentAnimationSettings;
@"SBFFluidBehaviorSettings" _cropsAnimationSettings;
@"SBFFluidBehaviorSettings" _cropLinesAlphaAnimationSettings;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"SBCornerPencilPanGestureSettings",&,N,V_pencilGestureSettings) pencilGestureSettings;
@property (T@"SBCornerFingerPanGestureSettings",&,N,V_fingerGestureSettings) fingerGestureSettings;
@property (TB,N,V_shouldAsynchronouslyRender) shouldAsynchronouslyRender;
@property (TB,N,V_shouldPreheat) shouldPreheat;
@property (Td,N,V_applicationTouchDelayHysteresis) applicationTouchDelayHysteresis;
@property (Td,N,V_cornerRadiusVisibleProgressThreshold) cornerRadiusVisibleProgressThreshold;
@property (Td,N,V_cropCornersVisibleProgressThreshold) cropCornersVisibleProgressThreshold;
@property (Td,N,V_cropLinesVisibleProgressThreshold) cropLinesVisibleProgressThreshold;
@property (Td,N,V_baseCornerTranslationDegrees) baseCornerTranslationDegrees;
@property (Td,N,V_projectionDecelerationRate) projectionDecelerationRate;
@property (Td,N,V_rubberbandingRange) rubberbandingRange;
@property (Td,N,V_normalizedDistanceForCommitThreshold) normalizedDistanceForCommitThreshold;
@property (Td,N,V_horizontalTranslationFactor) horizontalTranslationFactor;
@property (Td,N,V_verticalTranslationFactor) verticalTranslationFactor;
@property (TB,N,V_shouldInjectVelocity) shouldInjectVelocity;
@property (Td,N,V_maximumInjectedVelocity) maximumInjectedVelocity;
@property (Td,N,V_disabledGestureCancellationDistance) disabledGestureCancellationDistance;
@property (Td,N,V_disabledGestureVelocityScale) disabledGestureVelocityScale;
@property (T@"SBFFluidBehaviorSettings",&,N,V_contentAnimationSettings) contentAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_disabledGestureContentAnimationSettings) disabledGestureContentAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_cropsAnimationSettings) cropsAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_cropLinesAlphaAnimationSettings) cropLinesAlphaAnimationSettings;
```

## Class methods

```
+[SBInteractiveScreenshotSettings settingsControllerModule];
```

## Instance methods

```
-[SBInteractiveScreenshotSettings isEnabled];
-[SBInteractiveScreenshotSettings setDefaultValues];
-[SBInteractiveScreenshotSettings setEnabled:];
-[SBInteractiveScreenshotSettings applicationTouchDelayHysteresis];
-[SBInteractiveScreenshotSettings cropLinesAlphaAnimationSettings];
-[SBInteractiveScreenshotSettings setHorizontalTranslationFactor:];
-[SBInteractiveScreenshotSettings baseCornerTranslationDegrees];
-[SBInteractiveScreenshotSettings contentAnimationSettings];
-[SBInteractiveScreenshotSettings cornerRadiusVisibleProgressThreshold];
-[SBInteractiveScreenshotSettings cropCornersVisibleProgressThreshold];
-[SBInteractiveScreenshotSettings cropLinesVisibleProgressThreshold];
-[SBInteractiveScreenshotSettings cropsAnimationSettings];
-[SBInteractiveScreenshotSettings disabledGestureCancellationDistance];
-[SBInteractiveScreenshotSettings disabledGestureContentAnimationSettings];
-[SBInteractiveScreenshotSettings disabledGestureVelocityScale];
-[SBInteractiveScreenshotSettings fingerGestureSettings];
-[SBInteractiveScreenshotSettings horizontalTranslationFactor];
-[SBInteractiveScreenshotSettings maximumInjectedVelocity];
-[SBInteractiveScreenshotSettings normalizedDistanceForCommitThreshold];
-[SBInteractiveScreenshotSettings pencilGestureSettings];
-[SBInteractiveScreenshotSettings projectionDecelerationRate];
-[SBInteractiveScreenshotSettings rubberbandingRange];
-[SBInteractiveScreenshotSettings setApplicationTouchDelayHysteresis:];
-[SBInteractiveScreenshotSettings setBaseCornerTranslationDegrees:];
-[SBInteractiveScreenshotSettings setContentAnimationSettings:];
-[SBInteractiveScreenshotSettings setCornerRadiusVisibleProgressThreshold:];
-[SBInteractiveScreenshotSettings setCropCornersVisibleProgressThreshold:];
-[SBInteractiveScreenshotSettings setCropLinesAlphaAnimationSettings:];
-[SBInteractiveScreenshotSettings setCropLinesVisibleProgressThreshold:];
-[SBInteractiveScreenshotSettings setCropsAnimationSettings:];
-[SBInteractiveScreenshotSettings setDisabledGestureCancellationDistance:];
-[SBInteractiveScreenshotSettings setDisabledGestureContentAnimationSettings:];
-[SBInteractiveScreenshotSettings setDisabledGestureVelocityScale:];
-[SBInteractiveScreenshotSettings setFingerGestureSettings:];
-[SBInteractiveScreenshotSettings setMaximumInjectedVelocity:];
-[SBInteractiveScreenshotSettings setNormalizedDistanceForCommitThreshold:];
-[SBInteractiveScreenshotSettings setPencilGestureSettings:];
-[SBInteractiveScreenshotSettings setProjectionDecelerationRate:];
-[SBInteractiveScreenshotSettings setRubberbandingRange:];
-[SBInteractiveScreenshotSettings setShouldAsynchronouslyRender:];
-[SBInteractiveScreenshotSettings setShouldInjectVelocity:];
-[SBInteractiveScreenshotSettings setShouldPreheat:];
-[SBInteractiveScreenshotSettings setVerticalTranslationFactor:];
-[SBInteractiveScreenshotSettings shouldAsynchronouslyRender];
-[SBInteractiveScreenshotSettings shouldInjectVelocity];
-[SBInteractiveScreenshotSettings shouldPreheat];
-[SBInteractiveScreenshotSettings verticalTranslationFactor];
```
