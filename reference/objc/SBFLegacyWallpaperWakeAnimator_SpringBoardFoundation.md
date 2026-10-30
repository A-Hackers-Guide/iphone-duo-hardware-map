# `SBFLegacyWallpaperWakeAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFScreenWakeAnimationTarget`
- 2 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _wakeState;
@"UIVisualEffectView" _wakeEffectView;
```

## Properties

```
@property (Tq,N,V_wakeState) wakeState;
@property (T@"UIVisualEffectView",W,N,V_wakeEffectView) wakeEffectView;
@property (TB,R,N,GisDisplayingSleepWakeEffects) displayingSleepWakeEffects;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFLegacyWallpaperWakeAnimator setWakeEffectView:];
-[SBFLegacyWallpaperWakeAnimator wakeEffectView];
-[SBFLegacyWallpaperWakeAnimator _shouldHideWakeEffectViewAfterUpdate];
-[SBFLegacyWallpaperWakeAnimator _targetWakeStateForFadeIn:];
-[SBFLegacyWallpaperWakeAnimator _wakeEffectsForAnimatingWakeState:];
-[SBFLegacyWallpaperWakeAnimator _wakeEffectsForPersistentWakeState:];
-[SBFLegacyWallpaperWakeAnimator isDisplayingSleepWakeEffects];
-[SBFLegacyWallpaperWakeAnimator removeAllWakeEffects];
-[SBFLegacyWallpaperWakeAnimator setWakeState:];
-[SBFLegacyWallpaperWakeAnimator updateWakeEffectsForWake:];
-[SBFLegacyWallpaperWakeAnimator updateWakeEffectsForWake:animated:completion:];
-[SBFLegacyWallpaperWakeAnimator wakeState];
```
