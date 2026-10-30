# `SBTraitsPipelineManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TRAArbiterDrawingDataSource`
- 5 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"SBMedusa1oSettings" _medusaSettings;
@"TRAArbiter" _arbiter;
@"<SBWindowSceneDelegate>" _sceneDelegate;
@"<SBUserInterfaceStyleProvider>" _userInterfaceStyleProvider;
@"SBResolvedKeyboardFocusContext" _resolvedKeyboardFocusContext;
```

## Properties

```
@property (T@"TRAArbiter",W,N,V_arbiter) arbiter;
@property (T@"<SBWindowSceneDelegate>",W,N,V_sceneDelegate) sceneDelegate;
@property (T@"<SBUserInterfaceStyleProvider>",R,N,V_userInterfaceStyleProvider) userInterfaceStyleProvider;
@property (T@"SBResolvedKeyboardFocusContext",C,N,V_resolvedKeyboardFocusContext) resolvedKeyboardFocusContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsPipelineManager inputs];
-[SBTraitsPipelineManager arbiter];
-[SBTraitsPipelineManager continuousFoldPinnedInterfaceOrientation];
-[SBTraitsPipelineManager initWithArbiter:sceneDelegate:userInterfaceStyleProvider:];
-[SBTraitsPipelineManager setupDefaultPipelineForArbiter:];
-[SBTraitsPipelineManager systemArbitratedDeviceOrientation];
-[SBTraitsPipelineManager resolvedKeyboardFocusContext];
-[SBTraitsPipelineManager userInterfaceStyleStageRoles];
-[SBTraitsPipelineManager zOrderStageRoles];
-[SBTraitsPipelineManager setSceneDelegate:];
-[SBTraitsPipelineManager setArbiter:];
-[SBTraitsPipelineManager sceneDelegate];
-[SBTraitsPipelineManager acquireContinuousFoldDeviceOrientationLock:];
-[SBTraitsPipelineManager acquireContinuousFoldDeviceOrientationLockExtension];
-[SBTraitsPipelineManager lastNonFlatDeviceOrientation];
-[SBTraitsPipelineManager orientationStageRoles];
-[SBTraitsPipelineManager defaultOrientationAnimationSettingsAnimatable:];
-[SBTraitsPipelineManager ambientPresentationStageRoles];
-[SBTraitsPipelineManager supportsLiveDeviceRotation];
-[SBTraitsPipelineManager systemArbitratedInterfaceOrientation];
-[SBTraitsPipelineManager setResolvedKeyboardFocusContext:];
-[SBTraitsPipelineManager userInterfaceStyleDidUpdateWithAnimationSettings:fence:];
-[SBTraitsPipelineManager initWithUserInterfaceStyleProvider:];
-[SBTraitsPipelineManager newBlockBasedOrientationPolicySpecifier:forParticipant:];
-[SBTraitsPipelineManager newBlockBasedOrientationPolicySpecifier:forRole:];
-[SBTraitsPipelineManager newBlockBasedZOrderStageResolver:forRole:];
-[SBTraitsPipelineManager userInterfaceStyleProvider];
```
