# `CtrMeshDiagUnreliableNodesResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
C _unreliableNodeCount;
@"NSArray" _unreliableNodes;
```

## Properties

```
@property (TC,R,V_unreliableNodeCount) unreliableNodeCount;
@property (T@"NSArray",R,V_unreliableNodes) unreliableNodes;
```

## Class methods

```
+[CtrMeshDiagUnreliableNodesResult supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagUnreliableNodesResult encodeWithCoder:];
-[CtrMeshDiagUnreliableNodesResult initWithCoder:];
-[CtrMeshDiagUnreliableNodesResult unreliableNodes];
-[CtrMeshDiagUnreliableNodesResult initWithUnreliableNodeCount:unreliableNodes:];
-[CtrMeshDiagUnreliableNodesResult unreliableNodeCount];
```
