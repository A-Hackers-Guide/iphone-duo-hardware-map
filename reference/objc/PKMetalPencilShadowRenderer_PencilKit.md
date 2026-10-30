# `PKMetalPencilShadowRenderer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 1 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"MTLVertexDescriptor" _vertexDescriptor;
@"<MTLDevice>" _device;
@"<MTLLibrary>" _library;
[5@"<MTLTexture>"] _textures;
@"<MTLTexture>" _pyramidTexture;
@"<MTLBuffer>" _vertexBuffer;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _vertexBufferBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _imageMaxBlurredExtent;
Q _currentPixelFormat;
@"<MTLRenderPipelineState>" _currentPipelineState;
@"<MTLCommandQueue>" _commandQueue;
d _currentRoll;
d _currentAltitude;
@"<MTLBuffer>" _blurVertexBuffer;
@"<MTLRenderPipelineState>" _blurPipelineState;
@"<MTLBuffer>" _grayscaleVertexBuffer;
@"<MTLRenderPipelineState>" _grayscalePipelineState;
@"CIImage" _genericShadowImage;
@"NSMutableDictionary" _objectsCache;
@"NSString" _currentModel;
d _currentRenderedRoll;
d _currentRenderedAltitude;
B _currentModelNeedsRoll;
```

## Properties

```
@property (T@"<MTLCommandQueue>",R,N) commandQueue;
```

## Class methods

```
+[PKMetalPencilShadowRenderer pixelSize];
+[PKMetalPencilShadowRenderer maxBlurSize];
```

## Instance methods

```
-[PKMetalPencilShadowRenderer initWithDevice:];
-[PKMetalPencilShadowRenderer commandQueue];
-[PKMetalPencilShadowRenderer initWithDevice:library:];
-[PKMetalPencilShadowRenderer renderInto:commandBuffer:position:azimuth:altitude:height:alpha:scale:clearFramebuffer:grayscale:];
-[PKMetalPencilShadowRenderer updateInk:];
-[PKMetalPencilShadowRenderer updateInk:oldInk:rollAngle:altitudeAngle:progress:];
-[PKMetalPencilShadowRenderer updateRoll:altitudeAngle:];
```
