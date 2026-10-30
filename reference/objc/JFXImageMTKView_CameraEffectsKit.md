# `JFXImageMTKView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKView`
- Protocols: `JFXImageViewRendering`
- 23 instance variables, 9 properties, 24 instance methods, 2 class methods

## Instance variables

```
@"<MTLLibrary>" _library;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLRenderPipelineState>" _renderPipelineState;
@"MTKTextureLoader" _textureLoader;
@"<MTLTexture>" _mtlTexture_RGBA;
@"<MTLTexture>" _mtlTexture_YUV_Luma;
@"<MTLTexture>" _mtlTexture_YUV_Chroma;
@"<MTLSamplerState>" _sampler;
^{__CVMetalTextureCache=} _textureCache;
^{__CVBuffer=} _texture_RGBA;
^{__CVBuffer=} _texture_YUV_Luma;
^{__CVBuffer=} _texture_YUV_Chroma;
^v _pixelBufferColorAttachments;
{CGSize="width"d"height"d} _viewSize;
{CGSize="width"d"height"d} _textureSize;
B _needsUpdateVertices;
B _needsUpdateTexture;
{?="vertices"[4{?="position""texCoords"}]} _quad;
B _flipX;
B _flipY;
B _enableDebugDrawing;
@"JTImage" _jtImage;
q _renderingType;
```

## Properties

```
@property (T@"JTImage",&,N,V_jtImage) jtImage;
@property (Tq,R,N,V_renderingType) renderingType;
@property (TB,N,V_flipX) flipX;
@property (TB,N,V_flipY) flipY;
@property (TB,N,V_enableDebugDrawing) enableDebugDrawing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[JFXImageMTKView buildRenderPipelineWithLabel:vertexFunction:fragmentFunction:device:view:error:];
+[JFXImageMTKView buildSamplerStateWithDevice:addressMode:filter:];
```

## Instance methods

```
-[JFXImageMTKView setContentMode:];
-[JFXImageMTKView dealloc];
-[JFXImageMTKView drawRect:];
-[JFXImageMTKView layoutSubviews];
-[JFXImageMTKView initWithCoder:];
-[JFXImageMTKView initWithFrame:device:];
-[JFXImageMTKView flipX];
-[JFXImageMTKView updateTexture];
-[JFXImageMTKView renderingType];
-[JFXImageMTKView cleanupTextures];
-[JFXImageMTKView JFXImageMTKView_commonInit];
-[JFXImageMTKView jtImage];
-[JFXImageMTKView cleanupTextureCache];
-[JFXImageMTKView configureRenderPipelineForColorAttachments:];
-[JFXImageMTKView enableDebugDrawing];
-[JFXImageMTKView flipY];
-[JFXImageMTKView setEnableDebugDrawing:];
-[JFXImageMTKView setFlipX:];
-[JFXImageMTKView setFlipY:];
-[JFXImageMTKView setJtImage:];
-[JFXImageMTKView setRenderingType:];
-[JFXImageMTKView setupTextureCache];
-[JFXImageMTKView updateDebugDrawing];
-[JFXImageMTKView updateVertices];
```
