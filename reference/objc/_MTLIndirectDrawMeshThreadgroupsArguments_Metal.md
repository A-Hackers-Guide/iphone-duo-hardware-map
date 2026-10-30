# `_MTLIndirectDrawMeshThreadgroupsArguments`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
{?="width"Q"height"Q"depth"Q} threadgroupsPerGrid;
{?="width"Q"height"Q"depth"Q} threadsPerObjectThreadgroup;
{?="width"Q"height"Q"depth"Q} threadsPerMeshThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadgroupsPerGrid;
{?="width"Q"height"Q"depth"Q} _threadsPerObjectThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerMeshThreadgroup;
```

## Properties

```
@property (T{?=QQQ},N,V_threadgroupsPerGrid) threadgroupsPerGrid;
@property (T{?=QQQ},N,V_threadsPerObjectThreadgroup) threadsPerObjectThreadgroup;
@property (T{?=QQQ},N,V_threadsPerMeshThreadgroup) threadsPerMeshThreadgroup;
```

## Instance methods

```
-[_MTLIndirectDrawMeshThreadgroupsArguments setThreadsPerObjectThreadgroup:];
-[_MTLIndirectDrawMeshThreadgroupsArguments setThreadgroupsPerGrid:];
-[_MTLIndirectDrawMeshThreadgroupsArguments setThreadsPerMeshThreadgroup:];
-[_MTLIndirectDrawMeshThreadgroupsArguments threadgroupsPerGrid];
-[_MTLIndirectDrawMeshThreadgroupsArguments threadsPerMeshThreadgroup];
-[_MTLIndirectDrawMeshThreadgroupsArguments threadsPerObjectThreadgroup];
```
