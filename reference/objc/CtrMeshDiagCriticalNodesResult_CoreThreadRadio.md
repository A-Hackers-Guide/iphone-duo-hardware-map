# `CtrMeshDiagCriticalNodesResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
C _criticalNodeCount;
@"NSArray" _criticalNodes;
```

## Properties

```
@property (TC,R,V_criticalNodeCount) criticalNodeCount;
@property (T@"NSArray",R,V_criticalNodes) criticalNodes;
```

## Class methods

```
+[CtrMeshDiagCriticalNodesResult supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagCriticalNodesResult encodeWithCoder:];
-[CtrMeshDiagCriticalNodesResult initWithCoder:];
-[CtrMeshDiagCriticalNodesResult criticalNodeCount];
-[CtrMeshDiagCriticalNodesResult criticalNodes];
-[CtrMeshDiagCriticalNodesResult initWithCriticalNodeCount:criticalNodes:];
```
