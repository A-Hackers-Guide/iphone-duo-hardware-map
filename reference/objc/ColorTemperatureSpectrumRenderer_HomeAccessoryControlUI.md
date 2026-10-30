# `ColorTemperatureSpectrumRenderer`

- Image: [`/System/Library/PrivateFrameworks/HomeAccessoryControlUI.framework/HomeAccessoryControlUI`](../userland/System__Library__PrivateFrameworks__HomeAccessoryControlUI.framework__HomeAccessoryControlUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTKViewDelegate`
- 8 instance variables, 12 properties, 23 instance methods, 2 class methods

## Instance variables

```
S _startColor;
S _endColor;
@"MTKView" _metalView;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLDevice>" _device;
@"<MTLRenderPipelineState>" _pipelineState;
@"<MTLBuffer>" _vertexBuffer;
@"<MTLBuffer>" _fragmentShaderArgumentBuffer;
```

## Properties

```
@property (T@"MTKView",&,N,V_metalView) metalView;
@property (T@"<MTLCommandQueue>",&,N,V_commandQueue) commandQueue;
@property (T@"<MTLDevice>",&,N,V_device) device;
@property (T@"<MTLRenderPipelineState>",&,N,V_pipelineState) pipelineState;
@property (T@"<MTLBuffer>",&,N,V_vertexBuffer) vertexBuffer;
@property (T@"<MTLBuffer>",&,N,V_fragmentShaderArgumentBuffer) fragmentShaderArgumentBuffer;
@property (TS,N,V_startColor) startColor;
@property (TS,N,V_endColor) endColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ColorTemperatureSpectrumRenderer colorAtLocation:];
+[ColorTemperatureSpectrumRenderer positionForColor:];
```

## Instance methods

```
-[ColorTemperatureSpectrumRenderer setCommandQueue:];
-[ColorTemperatureSpectrumRenderer metalView];
-[ColorTemperatureSpectrumRenderer startColor];
-[ColorTemperatureSpectrumRenderer setDevice:];
-[ColorTemperatureSpectrumRenderer device];
-[ColorTemperatureSpectrumRenderer setMetalView:];
-[ColorTemperatureSpectrumRenderer pipelineState];
-[ColorTemperatureSpectrumRenderer mtkView:drawableSizeWillChange:];
-[ColorTemperatureSpectrumRenderer commandQueue];
-[ColorTemperatureSpectrumRenderer setEndColor:];
-[ColorTemperatureSpectrumRenderer drawInMTKView:];
-[ColorTemperatureSpectrumRenderer endColor];
-[ColorTemperatureSpectrumRenderer setStartColor:];
-[ColorTemperatureSpectrumRenderer setPipelineState:];
-[ColorTemperatureSpectrumRenderer setVertexBuffer:];
-[ColorTemperatureSpectrumRenderer vertexBuffer];
-[ColorTemperatureSpectrumRenderer colorAtLocation:];
-[ColorTemperatureSpectrumRenderer fragmentShaderArgumentBuffer];
-[ColorTemperatureSpectrumRenderer initWithMetal:startColor:endColor:];
-[ColorTemperatureSpectrumRenderer initializeVertexBuffer];
-[ColorTemperatureSpectrumRenderer positionForColor:];
-[ColorTemperatureSpectrumRenderer setFragmentShaderArgumentBuffer:];
-[ColorTemperatureSpectrumRenderer setupRenderPipeline];
```
