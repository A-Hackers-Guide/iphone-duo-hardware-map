# `/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline`

iOS 27.2 dyld shared cache image. Version `685.1.3.0.1`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/Frameworks/MetalKit.framework/MetalKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 9 classes, 0 protocols, 72 methods, 22 properties

### Class pages

Every class and protocol, with its methods: [`MTLSAnimatablePathCollection`](../objc/MTLSAnimatablePathCollection_MTLSpline.md), [`MTLSArc`](../objc/MTLSArc_MTLSpline.md), [`MTLSCircle`](../objc/MTLSCircle_MTLSpline.md), [`MTLSCorner`](../objc/MTLSCorner_MTLSpline.md), [`MTLSPath`](../objc/MTLSPath_MTLSpline.md), [`MTLSPathBufferData`](../objc/MTLSPathBufferData_MTLSpline.md), [`MTLSPathUnion`](../objc/MTLSPathUnion_MTLSpline.md), [`MTLSSemiCircle`](../objc/MTLSSemiCircle_MTLSpline.md), [`MTLSplineRenderer`](../objc/MTLSplineRenderer_MTLSpline.md)

### Classes

`MTLSAnimatablePathCollection`, `MTLSArc`, `MTLSCircle`, `MTLSCorner`, `MTLSPath`, `MTLSPathBufferData`, `MTLSPathUnion`, `MTLSSemiCircle`, `MTLSplineRenderer`

### Properties

```
@property (T@"NSMutableDictionary",R,V_paths) paths;
@property (T@"MTLSPath",R,V_defaultPath) defaultPath;
@property (T^{ControlPoint=f},N,V_controlPointState) controlPointState;
@property (T^{ControlPoint=f},R) controlPoints;
@property (TQ,R) controlPointsCount;
@property (T^{PatchInfo=},R) patchInfo;
@property (TQ,R) patchInfoCount;
@property (T^S,R) indices;
@property (TQ,R) indicesCount;
@property (T^{InstanceInfo={?=[4]}},R) instances;
@property (TQ,R) instanceCount;
@property (T,V_viewRatio) viewRatio;
@property (T@"MTLSAnimatablePathCollection",&,V_collection) collection;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"<MTLBuffer>",R,V_tessellationFactors) tessellationFactors;
@property (T@"<MTLBuffer>",R,V_controlPoints) controlPoints;
@property (T@"<MTLBuffer>",R,V_indices) indices;
@property (T@"<MTLBuffer>",R,V_patchInfo) patchInfo;
@property (T@"<MTLBuffer>",R,V_instanceInfo) instanceInfo;
@property (T@"NSMutableArray",&,V_dataCollection) dataCollection;
@property (T{?=[4]},V_projectionMatrix) projectionMatrix;
@property (TQ,V_triangleFillMode) triangleFillMode;
```

## Strings (17)

```
default
ERROR: Failed to load metallib
tessellation_kernel_quad
Path Per-Patch Info
Path Per-Instance Info
2
metallib
tessellation_fragment
&
Path Tessellation Factors
Path Control Points
Render Command Encoder
vector
Spline Renderer's Command Queue
tessellation_vertex
Compute Command Encoder
Path Indices
```
