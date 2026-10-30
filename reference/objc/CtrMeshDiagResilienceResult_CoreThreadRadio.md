# `CtrMeshDiagResilienceResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
C _healthScore;
@"CtrMeshDiagResilienceMetadata" _metadata;
```

## Properties

```
@property (TC,R,V_healthScore) healthScore;
@property (T@"CtrMeshDiagResilienceMetadata",R,V_metadata) metadata;
```

## Class methods

```
+[CtrMeshDiagResilienceResult supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagResilienceResult metadata];
-[CtrMeshDiagResilienceResult encodeWithCoder:];
-[CtrMeshDiagResilienceResult initWithCoder:];
-[CtrMeshDiagResilienceResult healthScore];
-[CtrMeshDiagResilienceResult initWithHealthScore:metadata:];
```
