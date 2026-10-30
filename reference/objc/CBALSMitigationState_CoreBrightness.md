# `CBALSMitigationState`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
I _ceModelID;
f _ceConfidenceThreshold;
@"CBALSNode" _alsNode;
@"CBCEModule" _ceModule;
@"CBColorPolicyFilter" _policyFilter;
@"ConfidenceEstimatorStats" _stats;
```

## Properties

```
@property (T@"CBALSNode",&,N,V_alsNode) alsNode;
@property (T@"CBCEModule",&,N,V_ceModule) ceModule;
@property (T@"CBColorPolicyFilter",&,N,V_policyFilter) policyFilter;
@property (T@"ConfidenceEstimatorStats",&,N,V_stats) stats;
@property (TI,N,V_ceModelID) ceModelID;
@property (Tf,N,V_ceConfidenceThreshold) ceConfidenceThreshold;
```

## Instance methods

```
-[CBALSMitigationState dealloc];
-[CBALSMitigationState stats];
-[CBALSMitigationState setStats:];
-[CBALSMitigationState alsNode];
-[CBALSMitigationState ceConfidenceThreshold];
-[CBALSMitigationState ceModelID];
-[CBALSMitigationState ceModule];
-[CBALSMitigationState policyFilter];
-[CBALSMitigationState setAlsNode:];
-[CBALSMitigationState setCeConfidenceThreshold:];
-[CBALSMitigationState setCeModelID:];
-[CBALSMitigationState setCeModule:];
-[CBALSMitigationState setPolicyFilter:];
```
