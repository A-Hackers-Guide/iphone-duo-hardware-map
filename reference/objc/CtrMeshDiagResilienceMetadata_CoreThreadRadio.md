# `CtrMeshDiagResilienceMetadata`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 11 properties, 14 instance methods, 1 class methods

## Instance variables

```
f _penaltyCriticalNodes;
f _penaltyBottlenecks;
f _penaltyAsymmetricLinks;
f _penaltyUnreliableNodes;
f _penaltyUnreachableNodes;
f _weightCriticalNodes;
f _weightBottlenecks;
f _weightAsymmetricLinks;
f _weightUnreliableNodes;
f _weightUnreachableNodes;
@"NSString" _scoreSummary;
```

## Properties

```
@property (Tf,R,V_penaltyCriticalNodes) penaltyCriticalNodes;
@property (Tf,R,V_penaltyBottlenecks) penaltyBottlenecks;
@property (Tf,R,V_penaltyAsymmetricLinks) penaltyAsymmetricLinks;
@property (Tf,R,V_penaltyUnreliableNodes) penaltyUnreliableNodes;
@property (Tf,R,V_penaltyUnreachableNodes) penaltyUnreachableNodes;
@property (Tf,R,V_weightCriticalNodes) weightCriticalNodes;
@property (Tf,R,V_weightBottlenecks) weightBottlenecks;
@property (Tf,R,V_weightAsymmetricLinks) weightAsymmetricLinks;
@property (Tf,R,V_weightUnreliableNodes) weightUnreliableNodes;
@property (Tf,R,V_weightUnreachableNodes) weightUnreachableNodes;
@property (T@"NSString",R,V_scoreSummary) scoreSummary;
```

## Class methods

```
+[CtrMeshDiagResilienceMetadata supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagResilienceMetadata encodeWithCoder:];
-[CtrMeshDiagResilienceMetadata initWithCoder:];
-[CtrMeshDiagResilienceMetadata scoreSummary];
-[CtrMeshDiagResilienceMetadata initWithPenaltyCriticalNodes:penaltyBottlenecks:penaltyAsymmetricLinks:penaltyUnreliableNodes:penaltyUnreachableNodes:weightCriticalNodes:weightBottlenecks:weightAsymmetricLinks:weightUnreliableNodes:weightUnreachableNodes:scoreSummary:];
-[CtrMeshDiagResilienceMetadata penaltyAsymmetricLinks];
-[CtrMeshDiagResilienceMetadata penaltyBottlenecks];
-[CtrMeshDiagResilienceMetadata penaltyCriticalNodes];
-[CtrMeshDiagResilienceMetadata penaltyUnreachableNodes];
-[CtrMeshDiagResilienceMetadata penaltyUnreliableNodes];
-[CtrMeshDiagResilienceMetadata weightAsymmetricLinks];
-[CtrMeshDiagResilienceMetadata weightBottlenecks];
-[CtrMeshDiagResilienceMetadata weightCriticalNodes];
-[CtrMeshDiagResilienceMetadata weightUnreachableNodes];
-[CtrMeshDiagResilienceMetadata weightUnreliableNodes];
```
