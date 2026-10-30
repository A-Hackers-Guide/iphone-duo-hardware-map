# `CtrMeshDiagAnalysisResults`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 11 instance methods, 1 class methods

## Instance variables

```
S _version;
@"CtrMeshDiagCriticalNodesResult" _criticalNodesResult;
@"CtrMeshDiagUnreliableNodesResult" _unreliableNodesResult;
@"CtrMeshDiagUnreachableNodesResult" _unreachableNodesResult;
@"CtrMeshDiagAsymmetricLinksResult" _asymmetricLinksResult;
@"CtrMeshDiagBottleneckNodesResult" _bottleneckNodesResult;
@"CtrMeshDiagUnsupportedEnhancedDiagnosticsResult" _unsupportedEnhancedDiagnosticsResult;
@"CtrMeshDiagResilienceResult" _resilienceResult;
```

## Properties

```
@property (T@"CtrMeshDiagCriticalNodesResult",R,V_criticalNodesResult) criticalNodesResult;
@property (T@"CtrMeshDiagUnreliableNodesResult",R,V_unreliableNodesResult) unreliableNodesResult;
@property (T@"CtrMeshDiagUnreachableNodesResult",R,V_unreachableNodesResult) unreachableNodesResult;
@property (T@"CtrMeshDiagAsymmetricLinksResult",R,V_asymmetricLinksResult) asymmetricLinksResult;
@property (T@"CtrMeshDiagBottleneckNodesResult",R,V_bottleneckNodesResult) bottleneckNodesResult;
@property (T@"CtrMeshDiagUnsupportedEnhancedDiagnosticsResult",R,V_unsupportedEnhancedDiagnosticsResult) unsupportedEnhancedDiagnosticsResult;
@property (T@"CtrMeshDiagResilienceResult",R,V_resilienceResult) resilienceResult;
@property (TS,R,V_version) version;
```

## Class methods

```
+[CtrMeshDiagAnalysisResults supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagAnalysisResults version];
-[CtrMeshDiagAnalysisResults encodeWithCoder:];
-[CtrMeshDiagAnalysisResults initWithCoder:];
-[CtrMeshDiagAnalysisResults asymmetricLinksResult];
-[CtrMeshDiagAnalysisResults bottleneckNodesResult];
-[CtrMeshDiagAnalysisResults criticalNodesResult];
-[CtrMeshDiagAnalysisResults initWithCriticalNodesResult:unreliableNodesResult:unreachableNodesResult:asymmetricLinksResult:bottleneckNodesResult:unsupportedEnhancedDiagnosticsResult:resilienceResult:version:];
-[CtrMeshDiagAnalysisResults resilienceResult];
-[CtrMeshDiagAnalysisResults unreachableNodesResult];
-[CtrMeshDiagAnalysisResults unreliableNodesResult];
-[CtrMeshDiagAnalysisResults unsupportedEnhancedDiagnosticsResult];
```
