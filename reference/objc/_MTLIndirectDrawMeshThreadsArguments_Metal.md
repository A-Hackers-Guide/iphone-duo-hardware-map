# `_MTLIndirectDrawMeshThreadsArguments`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
{?="width"Q"height"Q"depth"Q} threadsPerGrid;
{?="width"Q"height"Q"depth"Q} threadsPerObjectThreadgroup;
{?="width"Q"height"Q"depth"Q} threadsPerMeshThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerGrid;
{?="width"Q"height"Q"depth"Q} _threadsPerObjectThreadgroup;
{?="width"Q"height"Q"depth"Q} _threadsPerMeshThreadgroup;
```

## Properties

```
@property (T{?=QQQ},N,V_threadsPerGrid) threadsPerGrid;
@property (T{?=QQQ},N,V_threadsPerObjectThreadgroup) threadsPerObjectThreadgroup;
@property (T{?=QQQ},N,V_threadsPerMeshThreadgroup) threadsPerMeshThreadgroup;
```

## Instance methods

```
-[_MTLIndirectDrawMeshThreadsArguments setThreadsPerObjectThreadgroup:];
-[_MTLIndirectDrawMeshThreadsArguments setThreadsPerGrid:];
-[_MTLIndirectDrawMeshThreadsArguments setThreadsPerMeshThreadgroup:];
-[_MTLIndirectDrawMeshThreadsArguments threadsPerGrid];
-[_MTLIndirectDrawMeshThreadsArguments threadsPerMeshThreadgroup];
-[_MTLIndirectDrawMeshThreadsArguments threadsPerObjectThreadgroup];
```
