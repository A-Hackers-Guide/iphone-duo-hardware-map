# `PKMetalShader`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"<MTLFunction>" _vertexFunction;
@"<MTLFunction>" _fragmentFunction;
@"<MTLRenderPipelineState>" _pipelineState;
@"<MTLRenderPipelineState>" _pipelineStateWithColorMaskNone;
@"<MTLRenderPipelineState>" _msaaPipelineState;
@"<MTLRenderPipelineState>" _msaaPipelineStateWithColorMaskNone;
Q _stencilPixelFormat;
q _blendMode;
Q _colorAttachmentIndex;
@"MTLRenderPipelineDescriptor" _sharedPipelineDescriptor;
Q _numColorAttachments;
@"PKMetalShader" _noBlendModeShader;
@"PKMetalShader" _addBlendModeShader;
@"PKMetalShader" _addNoAlphaBlendModeShader;
@"PKMetalShader" _linearDodgeBlendModeShader;
@"PKMetalShader" _multiplyBlendModeShader;
@"PKMetalShader" _sourceOverBlendModeShader;
@"PKMetalShader" _subtractBlendModeShader;
@"PKMetalShader" _maxBlendModeShader;
@"PKMetalShader" _invertBlendModeShader;
Q _msaaPipelineStateSampleCount;
Q _msaaPipelineStateWithColorMaskNoneSampleCount;
```

## Instance methods

```
-[PKMetalShader init];
```
