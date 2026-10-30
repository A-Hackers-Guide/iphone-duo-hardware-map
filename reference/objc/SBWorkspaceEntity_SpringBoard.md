# `SBWorkspaceEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `SBActivationSettings`, `SBDeactivationSettings`, `BSDescriptionProviding`, `SBLayoutElementDescriptor`
- 4 instance variables, 17 properties, 51 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
q _layoutRole;
@"SBActivationSettings" _activationSettings;
@"SBDeactivationSettings" _deactivationSettings;
```

## Properties

```
@property (TB,R,N) isPreviousWorkspaceEntity;
@property (TB,R,N) isEmptyWorkspaceEntity;
@property (TB,R,N) isHomeScreenEntity;
@property (Tq,N,V_layoutRole) layoutRole;
@property (T@"SBActivationSettings",R,N,V_activationSettings) activationSettings;
@property (T@"SBDeactivationSettings",R,N,V_deactivationSettings) deactivationSettings;
@property (TB,R,N) supportsPresentationAtAnySize;
@property (TB,R,N) supportsSplitView;
@property (TB,R,N) wantsExclusiveForeground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) uniqueIdentifier;
@property (T@"SBLayoutRoleSet",R,N) supportedLayoutRoles;
@property (TQ,R,N) layoutAttributes;
@property (T@?,R,C,N) entityGenerator;
```

## Class methods

```
+[SBWorkspaceEntity entity];
```

## Instance methods

```
-[SBWorkspaceEntity clearActivationSettings];
-[SBWorkspaceEntity wantsExclusiveForeground];
-[SBWorkspaceEntity applyActivationSettings:];
-[SBWorkspaceEntity layoutRole];
-[SBWorkspaceEntity _generator];
-[SBWorkspaceEntity succinctDescriptionBuilder];
-[SBWorkspaceEntity init];
-[SBWorkspaceEntity applicationSceneEntity];
-[SBWorkspaceEntity setLayoutRole:];
-[SBWorkspaceEntity layoutAttributes];
-[SBWorkspaceEntity isDeviceApplicationSceneEntity];
-[SBWorkspaceEntity descriptionWithMultilinePrefix:];
-[SBWorkspaceEntity uniqueIdentifier];
-[SBWorkspaceEntity isHomeScreenEntity];
-[SBWorkspaceEntity flagForActivationSetting:];
-[SBWorkspaceEntity succinctDescription];
-[SBWorkspaceEntity supportsPresentationAtAnySize];
-[SBWorkspaceEntity displayItemRepresentation];
-[SBWorkspaceEntity boolForActivationSetting:];
-[SBWorkspaceEntity supportedLayoutRoles];
-[SBWorkspaceEntity dashBoardHostableEntity];
-[SBWorkspaceEntity supportsSplitView];
-[SBWorkspaceEntity copyActivationSettings];
-[SBWorkspaceEntity deviceApplicationSceneEntity];
-[SBWorkspaceEntity entityGenerator];
-[SBWorkspaceEntity setObject:forActivationSetting:];
-[SBWorkspaceEntity description];
-[SBWorkspaceEntity objectForActivationSetting:];
-[SBWorkspaceEntity hasLayoutAttributes:];
-[SBWorkspaceEntity setFlag:forActivationSetting:];
-[SBWorkspaceEntity isDashBoardHostableEntity];
-[SBWorkspaceEntity copyWithZone:];
-[SBWorkspaceEntity representsSameLayoutElementAsDescriptor:];
-[SBWorkspaceEntity descriptionBuilderWithMultilinePrefix:];
-[SBWorkspaceEntity setFlag:forDeactivationSetting:];
-[SBWorkspaceEntity activationSettings];
-[SBWorkspaceEntity appClipPlaceholderEntity];
-[SBWorkspaceEntity applyDeactivationSettings:];
-[SBWorkspaceEntity boolForDeactivationSetting:];
-[SBWorkspaceEntity clearDeactivationSettings];
-[SBWorkspaceEntity copyDeactivationSettings];
-[SBWorkspaceEntity deactivationSettings];
-[SBWorkspaceEntity flagForDeactivationSetting:];
-[SBWorkspaceEntity initWithIdentifier:displayChangeSettings:];
-[SBWorkspaceEntity isAnalogousToEntity:];
-[SBWorkspaceEntity isAppClipPlaceholderEntity];
-[SBWorkspaceEntity isApplicationSceneEntity];
-[SBWorkspaceEntity isEmptyWorkspaceEntity];
-[SBWorkspaceEntity isPreviousWorkspaceEntity];
-[SBWorkspaceEntity objectForDeactivationSetting:];
-[SBWorkspaceEntity setObject:forDeactivationSetting:];
```
