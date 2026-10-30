# `CtrMeshDiagBottleneckNodesResult`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
C _bottleneckNodeCount;
@"NSArray" _bottleneckNodes;
```

## Properties

```
@property (TC,R,V_bottleneckNodeCount) bottleneckNodeCount;
@property (T@"NSArray",R,V_bottleneckNodes) bottleneckNodes;
```

## Class methods

```
+[CtrMeshDiagBottleneckNodesResult supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagBottleneckNodesResult encodeWithCoder:];
-[CtrMeshDiagBottleneckNodesResult initWithCoder:];
-[CtrMeshDiagBottleneckNodesResult bottleneckNodes];
-[CtrMeshDiagBottleneckNodesResult bottleneckNodeCount];
-[CtrMeshDiagBottleneckNodesResult initWithBottleneckNodeCount:bottleneckNodes:];
```
