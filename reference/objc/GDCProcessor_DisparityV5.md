# `GDCProcessor`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _mtlDevice;
@"<MTLCommandQueue>" _mtlCommandQueue;
[3@"<MTLSamplerState>"] _samplers;
[2@"<MTLRenderPipelineState>"] _pipelineStates;
@"FigMetalContext" _metalContext;
@"<MTLBuffer>" _distortUniforms;
@"<MTLBuffer>" _unDistortUniforms;
```

## Instance methods

```
-[GDCProcessor dealloc];
-[GDCProcessor initWithMetalContext:];
-[GDCProcessor initMetal];
-[GDCProcessor setSamplers:];
-[GDCProcessor GDCDistort:to:parameters:commandBuffer:];
-[GDCProcessor GDCFrom:to:parameters:];
-[GDCProcessor GDCFromPixelBuffer:toPixelBuffer:parameters:];
-[GDCProcessor GDCDistort:to:parameters:];
-[GDCProcessor GDCDistortPixelBuffer:toPixelBuffer:parameters:];
-[GDCProcessor GDCFrom:to:parameters:commandBuffer:];
-[GDCProcessor compileShadersWithLib:];
```
