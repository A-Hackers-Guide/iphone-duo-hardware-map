# `SBTraitsContinuityDisplayPipelineManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsPipelineManager`
- Protocols: `TRAArbiterInputsDataSource`, `SBTraitsParticipantDelegate`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"TRAArbitrationInputs" _inputs;
@"SBTraitsEmbeddedDisplayRolesAndDefaultPoliciesProvider" _rolesAndDefaultPoliciesProvider;
@"SBTraitsOrientationSupportTreeNodesSpecifier" _orientationTreeNodesSpecifier;
@"TRAParticipant" _activeOrientationParticipant;
Q _currentSupportedInterfaceOrientations;
q _currentDeviceOrientation;
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
-[SBTraitsContinuityDisplayPipelineManager setDeviceOrientation:];
-[SBTraitsContinuityDisplayPipelineManager inputs];
-[SBTraitsContinuityDisplayPipelineManager didChangeSettingsForParticipant:context:];
-[SBTraitsContinuityDisplayPipelineManager updatePreferencesForParticipant:updater:];
-[SBTraitsContinuityDisplayPipelineManager initWithArbiter:sceneDelegate:userInterfaceStyleProvider:];
-[SBTraitsContinuityDisplayPipelineManager setupDefaultPipelineForArbiter:];
-[SBTraitsContinuityDisplayPipelineManager userInterfaceStyleStageRoles];
-[SBTraitsContinuityDisplayPipelineManager zOrderStageRoles];
-[SBTraitsContinuityDisplayPipelineManager _noteInputsNeedUpdateWithAnimationSettings:fence:reason:];
-[SBTraitsContinuityDisplayPipelineManager orientationStageRoles];
-[SBTraitsContinuityDisplayPipelineManager ambientPresentationStageRoles];
-[SBTraitsContinuityDisplayPipelineManager supportsLiveDeviceRotation];
-[SBTraitsContinuityDisplayPipelineManager userInterfaceStyleDidUpdateWithAnimationSettings:fence:];
-[SBTraitsContinuityDisplayPipelineManager _updateInputsForCurrentUserInterfaceStyle];
-[SBTraitsContinuityDisplayPipelineManager _updateInputsForDeviceOrientation:];
```
