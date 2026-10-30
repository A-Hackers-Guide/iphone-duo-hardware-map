# `MTLSPath`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__Frameworks__MTLSpline.framework__MTLSpline.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 30 instance methods, 0 class methods

## Instance variables

```
f _strokeWeight;
{vector<ControlPoint, std::allocator<ControlPoint>>="__begin_"^{ControlPoint}"__end_"^{ControlPoint}""{?="__cap_"^{ControlPoint}}} _controlPointsVector;
{vector<PatchInfo, std::allocator<PatchInfo>>="__begin_"^{PatchInfo}"__end_"^{PatchInfo}""{?="__cap_"^{PatchInfo}}} _patchInfoVector;
{vector<unsigned short, std::allocator<unsigned short>>="__begin_"^S"__end_"^S""{?="__cap_"^S}} _indicesVector;
{vector<InstanceInfo, std::allocator<InstanceInfo>>="__begin_"^{InstanceInfo}"__end_"^{InstanceInfo}""{?="__cap_"^{InstanceInfo}}} _instancesVector;
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _collapsedTransforms;
```

## Properties

```
@property (T^{ControlPoint=f},R) controlPoints;
@property (TQ,R) controlPointsCount;
@property (T^{PatchInfo=},R) patchInfo;
@property (TQ,R) patchInfoCount;
@property (T^S,R) indices;
@property (TQ,R) indicesCount;
@property (T^{InstanceInfo={?=[4]}},R) instances;
@property (TQ,R) instanceCount;
```

## Instance methods

```
-[MTLSPath init];
-[MTLSPath instanceCount];
-[MTLSPath indices];
-[MTLSPath controlPoints];
-[MTLSPath instances];
-[MTLSPath indicesCount];
-[MTLSPath appendInstances:count:];
-[MTLSPath clearInstances];
-[MTLSPath controlPointsCount];
-[MTLSPath initWithPoints:colors:count:strokeWeight:pattern:rotation:scale:translation:];
-[MTLSPath interpolateTangentWithPoints:t:];
-[MTLSPath appendControlPoints:count:];
-[MTLSPath appendIndices:count:];
-[MTLSPath appendPatchInfo:count:];
-[MTLSPath collapseTransform:];
-[MTLSPath controlPointsVectorCount];
-[MTLSPath controlPointsVectorData];
-[MTLSPath genIndicesWithPattern:];
-[MTLSPath genLeftCapWithWidth:];
-[MTLSPath genRightCapWithWidth:];
-[MTLSPath indicesVectorCount];
-[MTLSPath indicesVectorData];
-[MTLSPath initWithPoints:count:strokeWeight:pattern:rotation:scale:translation:];
-[MTLSPath instanceInfoVectorCount];
-[MTLSPath instanceInfoVectorData];
-[MTLSPath interpolateWithPoints:t:];
-[MTLSPath patchInfo];
-[MTLSPath patchInfoCount];
-[MTLSPath patchInfoVectorCount];
-[MTLSPath patchInfoVectorData];
```
