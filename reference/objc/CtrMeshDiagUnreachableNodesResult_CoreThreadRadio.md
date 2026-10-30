# `CtrMeshDiagUnreachableNodesResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
C _unreachableNodeCount;
@"NSArray" _unreachableNodes;
```

## Properties

```
@property (TC,R,V_unreachableNodeCount) unreachableNodeCount;
@property (T@"NSArray",R,V_unreachableNodes) unreachableNodes;
```

## Class methods

```
+[CtrMeshDiagUnreachableNodesResult supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagUnreachableNodesResult encodeWithCoder:];
-[CtrMeshDiagUnreachableNodesResult initWithCoder:];
-[CtrMeshDiagUnreachableNodesResult initWithUnreachableNodeCount:unreachableNodes:];
-[CtrMeshDiagUnreachableNodesResult unreachableNodeCount];
-[CtrMeshDiagUnreachableNodesResult unreachableNodes];
```
