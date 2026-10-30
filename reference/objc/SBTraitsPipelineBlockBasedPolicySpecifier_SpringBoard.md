# `SBTraitsPipelineBlockBasedPolicySpecifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `TRAPreferencesStageResolutionPolicySpecifying`
- 5 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isValid;
@"NSNumber" _componentOrder;
@? _specifierBlock;
@"TRAArbiter" _arbiter;
@"NSString" _specifierDescription;
```

## Properties

```
@property (T@?,R,C,N,V_specifierBlock) specifierBlock;
@property (T@"TRAArbiter",R,W,N,V_arbiter) arbiter;
@property (T@"NSNumber",R,N) componentOrder;
@property (T@"NSString",C,N,V_specifierDescription) specifierDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsPipelineBlockBasedPolicySpecifier dealloc];
-[SBTraitsPipelineBlockBasedPolicySpecifier arbiter];
-[SBTraitsPipelineBlockBasedPolicySpecifier invalidate];
-[SBTraitsPipelineBlockBasedPolicySpecifier description];
-[SBTraitsPipelineBlockBasedPolicySpecifier preferencesType];
-[SBTraitsPipelineBlockBasedPolicySpecifier componentOrder];
-[SBTraitsPipelineBlockBasedPolicySpecifier initWithPolicySpecifierBlock:specifierDescription:componentOrder:arbiter:];
-[SBTraitsPipelineBlockBasedPolicySpecifier setSpecifierDescription:];
-[SBTraitsPipelineBlockBasedPolicySpecifier specifierBlock];
-[SBTraitsPipelineBlockBasedPolicySpecifier specifierDescription];
-[SBTraitsPipelineBlockBasedPolicySpecifier updateStageParticipantsResolutionPolicies:context:];
```
