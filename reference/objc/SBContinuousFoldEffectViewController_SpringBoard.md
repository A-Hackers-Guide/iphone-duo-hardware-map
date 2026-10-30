# `SBContinuousFoldEffectViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PTSettingsKeyPathObserver`, `SBContinuousFoldEffectViewControlling`
- 27 instance variables, 4 properties, 38 instance methods, 0 class methods

## Instance variables

```
q _effectViewRole;
q _mode;
d _foldWidth;
d _angleProgress;
d _meshDisplacement;
@"SBDeviceContinuousFoldInteractionSettings" _settings;
@"UIViewFloatAnimatableProperty" _angleProgressProperty;
q _phase;
@? _settleCompletion;
d _settleTarget;
B _effectVisible;
d _pendingAngleProgress;
B _hasPendingAngleProgress;
B _hasLaidOut;
@"SBContinuousFoldBackdropView" _behindContentCaptureView;
@"UIView" _blackBackgroundView;
@"SBContinuousFoldBackdropView" _capturedContentRenderView;
@"SBContinuousFoldBackdropView" _variableBlurBackdropView;
@"SBGradientView" _variableBlurMaskView;
@"SBGradientView" _dimGradientView;
@"SBGradientView" _seamDimView;
@"UIView" _fadeToBlackView;
@"UIView" _touchBlockingView;
@"SBGradientView" _coneTopView;
@"SBGradientView" _coneBottomView;
@"UIImageView" _cylinderEdgeView;
@"UIView" _cornerMaskView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuousFoldEffectViewController viewIsAppearing:];
-[SBContinuousFoldEffectViewController supportedInterfaceOrientations];
-[SBContinuousFoldEffectViewController dealloc];
-[SBContinuousFoldEffectViewController viewDidLoad];
-[SBContinuousFoldEffectViewController viewDidLayoutSubviews];
-[SBContinuousFoldEffectViewController _canShowWhileLocked];
-[SBContinuousFoldEffectViewController settings:changedValueForKeyPath:];
-[SBContinuousFoldEffectViewController initWithRole:];
-[SBContinuousFoldEffectViewController _innerMeshTransformForProgress:];
-[SBContinuousFoldEffectViewController _outerMeshTransformForProgress:];
-[SBContinuousFoldEffectViewController _updateToAngleProgress:catchUp:];
-[SBContinuousFoldEffectViewController _animateToAngleProgress:];
-[SBContinuousFoldEffectViewController _applyAngleProgress:];
-[SBContinuousFoldEffectViewController _applyEffectSettings];
-[SBContinuousFoldEffectViewController _backdropScaleForRadius:];
-[SBContinuousFoldEffectViewController _blurRadiusForCurrentAngleProgress];
-[SBContinuousFoldEffectViewController _completeSettleIfConverged];
-[SBContinuousFoldEffectViewController _configureCornerMaskRadii];
-[SBContinuousFoldEffectViewController _directSetAngleProgress:];
-[SBContinuousFoldEffectViewController _distortionProgress];
-[SBContinuousFoldEffectViewController _fadeToBlackAlpha];
-[SBContinuousFoldEffectViewController _finishSettle:];
-[SBContinuousFoldEffectViewController _fullModeFadeToBlackAlpha];
-[SBContinuousFoldEffectViewController _prolongedDimCrossoverProgress];
-[SBContinuousFoldEffectViewController _scaledAnimationSettingsForTargetAngleProgress:];
-[SBContinuousFoldEffectViewController _seamDimOpacityForProgress:];
-[SBContinuousFoldEffectViewController _updateAllEffects];
-[SBContinuousFoldEffectViewController _updateBlurForCurrentAngleProgress];
-[SBContinuousFoldEffectViewController _updateConeAndCylinderForCurrentAngleProgress];
-[SBContinuousFoldEffectViewController _updateDimForCurrentAngleProgress];
-[SBContinuousFoldEffectViewController _updateFadeToBlackForCurrentAngleProgress];
-[SBContinuousFoldEffectViewController _updateMeshTransform];
-[SBContinuousFoldEffectViewController _updatePerspectiveCaptureForCurrentMesh];
-[SBContinuousFoldEffectViewController _updateRenderLayerRasterizationScale];
-[SBContinuousFoldEffectViewController _updateSeamDim];
-[SBContinuousFoldEffectViewController prepareForTransitionWithMode:foldEffectProgress:];
-[SBContinuousFoldEffectViewController settleOpen:completion:];
-[SBContinuousFoldEffectViewController updateWithFoldEffectProgress:swapProgressTo:from:];
```
