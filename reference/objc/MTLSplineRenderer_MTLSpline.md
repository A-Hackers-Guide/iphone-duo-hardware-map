# `MTLSplineRenderer`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/Frameworks/MTLSpline.framework/MTLSpline`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__Frameworks__MTLSpline.framework__MTLSpline.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
f _edgeFactor;
f _insideFactor;
@"MTKView" _view;
@"<MTLDevice>" _device;
@"<MTLLibrary>" _library;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLComputePipelineState>" _computeTessellationFactorsPipeline;
@"<MTLRenderPipelineState>" _renderPostTessellationPipelineState;
@"NSMutableArray" _dataCollection;
Q _triangleFillMode;
{?="columns"[4]} _projectionMatrix;
```

## Properties

```
@property (T@"NSMutableArray",&,V_dataCollection) dataCollection;
@property (T{?=[4]},V_projectionMatrix) projectionMatrix;
@property (TQ,V_triangleFillMode) triangleFillMode;
```

## Instance methods

```
-[MTLSplineRenderer init];
-[MTLSplineRenderer setTriangleFillMode:];
-[MTLSplineRenderer projectionMatrix];
-[MTLSplineRenderer setProjectionMatrix:];
-[MTLSplineRenderer initWithMTKView:dataCollection:];
-[MTLSplineRenderer createPipelineStates];
-[MTLSplineRenderer renderWithCommandBuffer:];
-[MTLSplineRenderer computeTessellationFactors:data:];
-[MTLSplineRenderer dataCollection];
-[MTLSplineRenderer renderPostTessellation:data:];
-[MTLSplineRenderer renderToTextureWithCommandBuffer:texture:];
-[MTLSplineRenderer setDataCollection:];
-[MTLSplineRenderer triangleFillMode];
```
