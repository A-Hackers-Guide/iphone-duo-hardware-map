# `SBTraitsPipelineBlockBasedZOrderStageResolver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `TRAPreferencesStageResolving`
- 5 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isValid;
@"NSNumber" _componentOrder;
@? _stageResolverBlock;
@"TRAArbiter" _arbiter;
@"NSString" _specifierDescription;
```

## Properties

```
@property (T@?,R,C,N,V_stageResolverBlock) stageResolverBlock;
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
-[SBTraitsPipelineBlockBasedZOrderStageResolver dealloc];
-[SBTraitsPipelineBlockBasedZOrderStageResolver arbiter];
-[SBTraitsPipelineBlockBasedZOrderStageResolver invalidate];
-[SBTraitsPipelineBlockBasedZOrderStageResolver description];
-[SBTraitsPipelineBlockBasedZOrderStageResolver preferencesType];
-[SBTraitsPipelineBlockBasedZOrderStageResolver componentOrder];
-[SBTraitsPipelineBlockBasedZOrderStageResolver initWithStageResolverBlock:specifierDescription:componentOrder:arbiter:];
-[SBTraitsPipelineBlockBasedZOrderStageResolver resolveStagePreferencesWithContext:preferencesTree:];
-[SBTraitsPipelineBlockBasedZOrderStageResolver setSpecifierDescription:];
-[SBTraitsPipelineBlockBasedZOrderStageResolver specifierDescription];
-[SBTraitsPipelineBlockBasedZOrderStageResolver stageResolverBlock];
```
