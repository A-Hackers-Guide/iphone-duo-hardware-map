# `SBTraitsRoleFollowsDeviceOrientationPolicySpecifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsOrientationStageComponent`
- Protocols: `TRAPreferencesStageResolutionPolicySpecifying`
- 2 instance variables, 7 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _targetRole;
@"NSArray" _deviceOrientationStateTypes;
```

## Properties

```
@property (T@"NSString",R,N) targetRole;
@property (T@"NSArray",C,N,V_deviceOrientationStateTypes) deviceOrientationStateTypes;
@property (T@"NSNumber",R,N) componentOrder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsRoleFollowsDeviceOrientationPolicySpecifier setDeviceOrientationStateTypes:];
-[SBTraitsRoleFollowsDeviceOrientationPolicySpecifier deviceOrientationStateTypes];
-[SBTraitsRoleFollowsDeviceOrientationPolicySpecifier initWithComponentOrder:];
-[SBTraitsRoleFollowsDeviceOrientationPolicySpecifier targetRole];
-[SBTraitsRoleFollowsDeviceOrientationPolicySpecifier updateStageParticipantsResolutionPolicies:context:];
```
