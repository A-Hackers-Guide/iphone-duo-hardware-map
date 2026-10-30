# `MTKView`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `NSCoding`, `CALayerDelegate`
- 52 instance variables, 31 properties, 92 instance methods, 1 class methods

## Instance variables

```
@"CAMetalLayer" _metalLayer;
B _sizeDirty;
{CGSize="width"d"height"d} _drawableScaleFactor;
B _pausedOnBackgrounding;
@"CADisplayLink" _displayLink;
@"<CAMetalDrawable>" _currentDrawable;
^? _drawRectSubIMP;
B _subClassOverridesDrawRect;
B _deviceReset;
B _doesNotifyOnRecommendedSizeUpdate;
@"<MTLTexture>" _depthStencilTexture;
@"<MTLTexture>" _multisampleColorTexture;
B _framebufferOnly;
Q _depthStencilTextureUsage;
Q _multisampleColorTextureUsage;
Q _depthStencilStorageMode;
Q _drawableAttachmentIndex;
q _nominalFramesPerSecond;
q _maxValidAttachmentIndex;
[8Q] _colorPixelFormats;
[8@"<MTLTexture>"] _multisampleColorTextures;
[8@"<MTLTexture>"] _colorTextures;
[3@"MTKOffscreenDrawable"] _offscreenSwapChain;
Q _drawableIdx;
i _renderAttachmentDirtyState;
Q _terminateAfterFrame;
Q _terminateAfterSeconds;
Q _measureAfterFrame;
Q _measureAfterSeconds;
Q _dumpFrameAtFrame;
Q _dumpFrameAtSeconds;
@"NSString" _dumpPath;
B _dumpFirstFrame;
B _drawOffscreen;
q _forceOrientation;
d _startTime;
I _frameNum;
@"<MTLResidencySet>" _residencySet;
[3@"NSMutableArray"] _allocationsToEvict;
B _enableSetNeedsDisplay;
B _autoResizeDrawable;
B _paused;
I _clearStencil;
@"<MTKViewDelegate>" _delegate;
@"<MTLDevice>" _device;
Q _depthStencilPixelFormat;
Q _sampleCount;
d _clearDepth;
q _preferredFramesPerSecond;
{CGSize="width"d"height"d} _drawableSize;
{CGSize="width"d"height"d} _preferredDrawableSize;
{?="red"d"green"d"blue"d"alpha"d} _clearColor;
```

## Properties

```
@property (T@"<MTKViewDelegate>",W,N,V_delegate) delegate;
@property (T@"<MTLDevice>",&,N,V_device) device;
@property (T@"<CAMetalDrawable>",R,N,V_currentDrawable) currentDrawable;
@property (TB,N) framebufferOnly;
@property (TQ,N) depthStencilAttachmentTextureUsage;
@property (TQ,N) multisampleColorAttachmentTextureUsage;
@property (TB,N) presentsWithTransaction;
@property (TQ,N) colorPixelFormat;
@property (TQ,N,V_depthStencilPixelFormat) depthStencilPixelFormat;
@property (TQ,N) depthStencilStorageMode;
@property (TQ,N,V_sampleCount) sampleCount;
@property (T{?=dddd},N,V_clearColor) clearColor;
@property (Td,N,V_clearDepth) clearDepth;
@property (TI,N,V_clearStencil) clearStencil;
@property (T@"<MTLTexture>",R,N) depthStencilTexture;
@property (T@"<MTLTexture>",R,N) multisampleColorTexture;
@property (T@"MTLRenderPassDescriptor",R,N) currentRenderPassDescriptor;
@property (T@"MTL4RenderPassDescriptor",R,N) currentMTL4RenderPassDescriptor;
@property (Tq,N,V_preferredFramesPerSecond) preferredFramesPerSecond;
@property (TB,N,V_enableSetNeedsDisplay) enableSetNeedsDisplay;
@property (TB,N,V_autoResizeDrawable) autoResizeDrawable;
@property (T{CGSize=dd},N,V_drawableSize) drawableSize;
@property (T{CGSize=dd},R,N,V_preferredDrawableSize) preferredDrawableSize;
@property (T@"<MTLDevice>",R) preferredDevice;
@property (TB,N,GisPaused,V_paused) paused;
@property (T^{CGColorSpace=},N) colorspace;
@property (T@"<MTLResidencySet>",R,N) residencySet;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MTKView layerClass];
```

## Instance methods

```
-[MTKView clearColor];
-[MTKView _applicationWillEnterForeground:];
-[MTKView _applicationDidEnterBackground:];
-[MTKView colorPixelFormat];
-[MTKView setContentScaleFactor:];
-[MTKView setClearColor:];
-[MTKView isPaused];
-[MTKView _canDrawContent];
-[MTKView didMoveToWindow];
-[MTKView setClearStencil:];
-[MTKView displayLayer:];
-[MTKView setDevice:];
-[MTKView nominalFramesPerSecond];
-[MTKView clearDepth];
-[MTKView setSampleCount:];
-[MTKView setColorspace:];
-[MTKView clearStencil];
-[MTKView device];
-[MTKView startTime];
-[MTKView dealloc];
-[MTKView drawLayer:inContext:];
-[MTKView layoutSubviews];
-[MTKView setPreferredFramesPerSecond:];
-[MTKView depthStencilPixelFormat];
-[MTKView colorspace];
-[MTKView setClearDepth:];
-[MTKView setPaused:];
-[MTKView setDelegate:];
-[MTKView depthStencilTexture];
-[MTKView sampleCount];
-[MTKView setNilValueForKey:];
-[MTKView currentRenderPassDescriptor];
-[MTKView encodeWithCoder:];
-[MTKView preferredFramesPerSecond];
-[MTKView delegate];
-[MTKView setFrame:];
-[MTKView initWithCoder:];
-[MTKView setColorPixelFormat:];
-[MTKView framebufferOnly];
-[MTKView currentDrawable];
-[MTKView initWithFrame:];
-[MTKView setFramebufferOnly:];
-[MTKView preferredDevice];
-[MTKView drawableSize];
-[MTKView presentsWithTransaction];
-[MTKView residencySet];
-[MTKView setDrawableSize:];
-[MTKView setPresentsWithTransaction:];
-[MTKView _controlsOwnScaleFactor];
-[MTKView setEnableSetNeedsDisplay:];
-[MTKView initWithFrame:device:];
-[MTKView releaseDrawables];
-[MTKView setAutoResizeDrawable:];
-[MTKView setDepthStencilPixelFormat:];
-[MTKView draw];
-[MTKView _createDisplayLinkForScreen:];
-[MTKView enableSetNeedsDisplay];
-[MTKView _resizeDrawable];
-[MTKView currentMTL4RenderPassDescriptor];
-[MTKView _evictResources];
-[MTKView __initCommon];
-[MTKView _calculateRefeshesPerSecond];
-[MTKView _dumpFrameImageWithFilename:];
-[MTKView _dumpFramerate:withFilename:];
-[MTKView _initializeResidencyManagement];
-[MTKView _pixelSizeFromPointSize:];
-[MTKView _replaceResidencySetEntryForOriginalTexture:newTexture:];
-[MTKView _resizeMetalLayerDrawable];
-[MTKView _updateToNativeScale];
-[MTKView autoResizeDrawable];
-[MTKView colorTextures];
-[MTKView colorTexturesForceUpdate:];
-[MTKView configureColorAttachments:];
-[MTKView configureDepthAttachment:stencilAttachment:];
-[MTKView createDepthStencilTexture];
-[MTKView depthStencilAttachmentTextureUsage];
-[MTKView depthStencilStorageMode];
-[MTKView drawNumber];
-[MTKView drawableAttachmentIndex];
-[MTKView exportToTargaAtLocation:width:height:size:bytes:];
-[MTKView getEnvironmentSettings];
-[MTKView multisampleColorAttachmentTextureUsage];
-[MTKView multisampleColorTexture];
-[MTKView multisampleColorTextures];
-[MTKView multisampleColorTexturesForceUpdate:];
-[MTKView preferredDrawableSize];
-[MTKView setColorPixelFormat:atIndex:];
-[MTKView setDepthStencilAttachmentTextureUsage:];
-[MTKView setDepthStencilStorageMode:];
-[MTKView setDrawableAttachmentIndex:];
-[MTKView setMultisampleColorAttachmentTextureUsage:];
-[MTKView setNominalFramesPerSecond:];
```
