# `SBContinuousFadeEffectViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBContinuousFoldEffectViewControlling`
- 11 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
q _effectViewRole;
@"SBDeviceContinuousFoldInteractionSettings" _settings;
B _effectVisible;
@"UIView" _fadeToBlackView;
d _angleProgress;
d _progressToSwap;
d _progressFromSwap;
@? _settleCompletion;
d _settleTarget;
@"UIViewFloatAnimatableProperty" _angleProgressProperty;
B _crossfadesLiveContent;
```

## Properties

```
@property (TB,N,V_crossfadesLiveContent) crossfadesLiveContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuousFadeEffectViewController supportedInterfaceOrientations];
-[SBContinuousFadeEffectViewController dealloc];
-[SBContinuousFadeEffectViewController viewDidLoad];
-[SBContinuousFadeEffectViewController viewDidLayoutSubviews];
-[SBContinuousFadeEffectViewController _canShowWhileLocked];
-[SBContinuousFadeEffectViewController initWithRole:];
-[SBContinuousFadeEffectViewController _applyAngleProgress:];
-[SBContinuousFadeEffectViewController _completeSettleIfConverged];
-[SBContinuousFadeEffectViewController _directSetAngleProgress:];
-[SBContinuousFadeEffectViewController _finishSettle:];
-[SBContinuousFadeEffectViewController _updateDimForCurrentAngleProgress];
-[SBContinuousFadeEffectViewController crossfadesLiveContent];
-[SBContinuousFadeEffectViewController prepareForTransitionWithMode:foldEffectProgress:];
-[SBContinuousFadeEffectViewController setCrossfadesLiveContent:];
-[SBContinuousFadeEffectViewController settleOpen:completion:];
-[SBContinuousFadeEffectViewController updateWithFoldEffectProgress:swapProgressTo:from:];
```
