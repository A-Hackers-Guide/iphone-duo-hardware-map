# `FBSProcessExecutionStrategy`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 7 instance variables, 11 properties, 21 instance methods, 7 class methods

## Instance variables

```
B _customPolicy;
I _bksReason;
I _bksFlags;
@"NSString" _strategyName;
q _schedulingPolicy;
q _graphicsPolicy;
q _jetsamPolicy;
```

## Properties

```
@property (T@"NSString",C,N,V_strategyName) strategyName;
@property (Tq,N,V_schedulingPolicy) schedulingPolicy;
@property (Tq,N,V_graphicsPolicy) graphicsPolicy;
@property (Tq,N,V_jetsamPolicy) jetsamPolicy;
@property (TB,N,GisCustomPolicy,V_customPolicy) customPolicy;
@property (TI,N,V_bksReason) reason;
@property (TI,N,V_bksFlags) flags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSProcessExecutionStrategy userInteractive];
+[FBSProcessExecutionStrategy initialize];
+[FBSProcessExecutionStrategy background];
+[FBSProcessExecutionStrategy backgroundWithUI];
+[FBSProcessExecutionStrategy policyWithReason:flags:];
+[FBSProcessExecutionStrategy strategyForSchedulingPolicy:graphicsPolicy:jetsamPolicy:];
+[FBSProcessExecutionStrategy userInteractiveWithoutUI];
```

## Instance methods

```
-[FBSProcessExecutionStrategy debugDescription];
-[FBSProcessExecutionStrategy setFlags:];
-[FBSProcessExecutionStrategy flags];
-[FBSProcessExecutionStrategy succinctDescriptionBuilder];
-[FBSProcessExecutionStrategy setReason:];
-[FBSProcessExecutionStrategy descriptionWithMultilinePrefix:];
-[FBSProcessExecutionStrategy succinctDescription];
-[FBSProcessExecutionStrategy description];
-[FBSProcessExecutionStrategy reason];
-[FBSProcessExecutionStrategy copyWithZone:];
-[FBSProcessExecutionStrategy descriptionBuilderWithMultilinePrefix:];
-[FBSProcessExecutionStrategy graphicsPolicy];
-[FBSProcessExecutionStrategy isCustomPolicy];
-[FBSProcessExecutionStrategy jetsamPolicy];
-[FBSProcessExecutionStrategy schedulingPolicy];
-[FBSProcessExecutionStrategy setCustomPolicy:];
-[FBSProcessExecutionStrategy setGraphicsPolicy:];
-[FBSProcessExecutionStrategy setJetsamPolicy:];
-[FBSProcessExecutionStrategy setSchedulingPolicy:];
-[FBSProcessExecutionStrategy setStrategyName:];
-[FBSProcessExecutionStrategy strategyName];
```
