# `SBEntityRemovalDosidoDefaultAnimationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 15 instance variables, 15 properties, 31 instance methods, 2 class methods

## Instance variables

```
d _fromViewFinalScale;
d _fromViewFinalAlpha;
d _fromViewFinalBlurRadius;
d _fromViewAlphaAnimationDelay;
@"SBFFluidBehaviorSettings" _fromViewScaleAnimationSettings;
@"SBFFluidBehaviorSettings" _fromViewAlphaAnimationSettings;
d _toViewInitialPushInScale;
d _toViewScreenInitialAlpha;
d _toViewInitialDimmingAlpha;
d _toViewInitialBlurProgress;
d _toViewScaleAndAlphaResetAnimationDelay;
d _toViewDimmingViewFadeOutDelay;
@"SBFFluidBehaviorSettings" _toViewScaleAndAlphaResetAnimationSettings;
@"SBFFluidBehaviorSettings" _toViewWallpaperScaleAnimationSettings;
@"SBFFluidBehaviorSettings" _toViewDimmingViewAlphaAnimationSettings;
```

## Properties

```
@property (Td,N,V_fromViewFinalScale) fromViewFinalScale;
@property (Td,N,V_fromViewFinalAlpha) fromViewFinalAlpha;
@property (Td,N,V_fromViewFinalBlurRadius) fromViewFinalBlurRadius;
@property (Td,N,V_fromViewAlphaAnimationDelay) fromViewAlphaAnimationDelay;
@property (T@"SBFFluidBehaviorSettings",&,N,V_fromViewScaleAnimationSettings) fromViewScaleAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_fromViewAlphaAnimationSettings) fromViewAlphaAnimationSettings;
@property (Td,N,V_toViewInitialPushInScale) toViewInitialPushInScale;
@property (Td,N,V_toViewScreenInitialAlpha) toViewScreenInitialAlpha;
@property (Td,N,V_toViewInitialDimmingAlpha) toViewInitialDimmingAlpha;
@property (Td,N,V_toViewInitialBlurProgress) toViewInitialBlurProgress;
@property (Td,N,V_toViewScaleAndAlphaResetAnimationDelay) toViewScaleAndAlphaResetAnimationDelay;
@property (Td,N,V_toViewDimmingViewFadeOutDelay) toViewDimmingViewFadeOutDelay;
@property (T@"SBFFluidBehaviorSettings",&,N,V_toViewScaleAndAlphaResetAnimationSettings) toViewScaleAndAlphaResetAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_toViewWallpaperScaleAnimationSettings) toViewWallpaperScaleAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_toViewDimmingViewAlphaAnimationSettings) toViewDimmingViewAlphaAnimationSettings;
```

## Class methods

```
+[SBEntityRemovalDosidoDefaultAnimationSettings settingsControllerModule];
+[SBEntityRemovalDosidoDefaultAnimationSettings _settingsModule];
```

## Instance methods

```
-[SBEntityRemovalDosidoDefaultAnimationSettings setDefaultValues];
-[SBEntityRemovalDosidoDefaultAnimationSettings setFromViewAlphaAnimationDelay:];
-[SBEntityRemovalDosidoDefaultAnimationSettings fromViewAlphaAnimationDelay];
-[SBEntityRemovalDosidoDefaultAnimationSettings fromViewAlphaAnimationSettings];
-[SBEntityRemovalDosidoDefaultAnimationSettings fromViewFinalAlpha];
-[SBEntityRemovalDosidoDefaultAnimationSettings fromViewFinalBlurRadius];
-[SBEntityRemovalDosidoDefaultAnimationSettings fromViewFinalScale];
-[SBEntityRemovalDosidoDefaultAnimationSettings fromViewScaleAnimationSettings];
-[SBEntityRemovalDosidoDefaultAnimationSettings setFromViewAlphaAnimationSettings:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setFromViewFinalAlpha:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setFromViewFinalBlurRadius:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setFromViewFinalScale:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setFromViewScaleAnimationSettings:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewDimmingViewAlphaAnimationSettings:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewDimmingViewFadeOutDelay:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewInitialBlurProgress:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewInitialDimmingAlpha:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewInitialPushInScale:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewScaleAndAlphaResetAnimationDelay:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewScaleAndAlphaResetAnimationSettings:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewScreenInitialAlpha:];
-[SBEntityRemovalDosidoDefaultAnimationSettings setToViewWallpaperScaleAnimationSettings:];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewDimmingViewAlphaAnimationSettings];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewDimmingViewFadeOutDelay];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewInitialBlurProgress];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewInitialDimmingAlpha];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewInitialPushInScale];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewScaleAndAlphaResetAnimationDelay];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewScaleAndAlphaResetAnimationSettings];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewScreenInitialAlpha];
-[SBEntityRemovalDosidoDefaultAnimationSettings toViewWallpaperScaleAnimationSettings];
```
