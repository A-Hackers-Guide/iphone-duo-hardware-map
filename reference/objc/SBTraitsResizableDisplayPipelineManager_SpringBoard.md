# `SBTraitsResizableDisplayPipelineManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsPipelineManager`
- Protocols: `TRAArbiterInputsDataSource`, `SBTraitsParticipantDelegate`
- 3 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"TRAArbitrationInputs" _inputs;
@"SBTraitsEmbeddedDisplayRolesAndDefaultPoliciesProvider" _rolesAndDefaultPoliciesProvider;
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
-[SBTraitsResizableDisplayPipelineManager inputs];
-[SBTraitsResizableDisplayPipelineManager didChangeSettingsForParticipant:context:];
-[SBTraitsResizableDisplayPipelineManager updatePreferencesForParticipant:updater:];
-[SBTraitsResizableDisplayPipelineManager initWithArbiter:sceneDelegate:userInterfaceStyleProvider:];
-[SBTraitsResizableDisplayPipelineManager setupDefaultPipelineForArbiter:];
-[SBTraitsResizableDisplayPipelineManager userInterfaceStyleStageRoles];
-[SBTraitsResizableDisplayPipelineManager zOrderStageRoles];
-[SBTraitsResizableDisplayPipelineManager _noteInputsNeedUpdateWithAnimationSettings:fence:reason:];
-[SBTraitsResizableDisplayPipelineManager orientationStageRoles];
-[SBTraitsResizableDisplayPipelineManager ambientPresentationStageRoles];
-[SBTraitsResizableDisplayPipelineManager supportsLiveDeviceRotation];
-[SBTraitsResizableDisplayPipelineManager userInterfaceStyleDidUpdateWithAnimationSettings:fence:];
-[SBTraitsResizableDisplayPipelineManager _updateInputsForCurrentUserInterfaceStyle];
```
