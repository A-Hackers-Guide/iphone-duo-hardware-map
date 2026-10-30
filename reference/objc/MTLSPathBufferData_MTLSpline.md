# `MTLSPathBufferData`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__Frameworks__MTLSpline.framework__MTLSpline.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
_viewRatio;
@"MTLSAnimatablePathCollection" _collection;
@"<MTLDevice>" _device;
@"<MTLBuffer>" _tessellationFactors;
@"<MTLBuffer>" _controlPoints;
@"<MTLBuffer>" _indices;
@"<MTLBuffer>" _patchInfo;
@"<MTLBuffer>" _instanceInfo;
```

## Properties

```
@property (T,V_viewRatio) viewRatio;
@property (T@"MTLSAnimatablePathCollection",&,V_collection) collection;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"<MTLBuffer>",R,V_tessellationFactors) tessellationFactors;
@property (T@"<MTLBuffer>",R,V_controlPoints) controlPoints;
@property (T@"<MTLBuffer>",R,V_indices) indices;
@property (T@"<MTLBuffer>",R,V_patchInfo) patchInfo;
@property (T@"<MTLBuffer>",R,V_instanceInfo) instanceInfo;
```

## Instance methods

```
-[MTLSPathBufferData commit];
-[MTLSPathBufferData device];
-[MTLSPathBufferData collection];
-[MTLSPathBufferData indices];
-[MTLSPathBufferData setCollection:];
-[MTLSPathBufferData controlPoints];
-[MTLSPathBufferData instanceInfo];
-[MTLSPathBufferData initWithCollection:device:viewRatio:];
-[MTLSPathBufferData updateControlPointBufferWithData:count:];
-[MTLSPathBufferData updateInstanceBufferWithData:count:];
-[MTLSPathBufferData initWithDefaultPath:device:viewRatio:];
-[MTLSPathBufferData initWithDevice:viewRatio:];
-[MTLSPathBufferData patchInfo];
-[MTLSPathBufferData setViewRatio:];
-[MTLSPathBufferData tessellationFactors];
-[MTLSPathBufferData viewRatio];
```
