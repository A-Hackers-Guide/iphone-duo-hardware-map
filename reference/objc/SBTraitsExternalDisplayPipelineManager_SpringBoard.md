# `SBTraitsExternalDisplayPipelineManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsPipelineManager`
- Protocols: `TRAArbiterInputsDataSource`, `SBTraitsParticipantDelegate`
- 3 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"TRAArbitrationInputs" _inputs;
@"SBTraitsExternalDisplayRolesAndDefaultPoliciesProvider" _rolesAndDefaultPoliciesProvider;
@"TRAParticipant" _activeOrientationParticipant;
```

## Properties

```
@property (T@"TRAArbitrationInputs",R,N) inputs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsExternalDisplayPipelineManager inputs];
-[SBTraitsExternalDisplayPipelineManager didChangeSettingsForParticipant:context:];
-[SBTraitsExternalDisplayPipelineManager updatePreferencesForParticipant:updater:];
-[SBTraitsExternalDisplayPipelineManager initWithArbiter:sceneDelegate:userInterfaceStyleProvider:];
-[SBTraitsExternalDisplayPipelineManager setupDefaultPipelineForArbiter:];
-[SBTraitsExternalDisplayPipelineManager userInterfaceStyleStageRoles];
-[SBTraitsExternalDisplayPipelineManager zOrderStageRoles];
-[SBTraitsExternalDisplayPipelineManager _noteInputsNeedUpdateWithAnimationSettings:fence:reason:];
-[SBTraitsExternalDisplayPipelineManager orientationStageRoles];
-[SBTraitsExternalDisplayPipelineManager ambientPresentationStageRoles];
-[SBTraitsExternalDisplayPipelineManager supportsLiveDeviceRotation];
-[SBTraitsExternalDisplayPipelineManager userInterfaceStyleDidUpdateWithAnimationSettings:fence:];
-[SBTraitsExternalDisplayPipelineManager _updateInputsForCurrentUserInterfaceStyle];
```
