# `/System/Library/Frameworks/MetalKit.framework/MetalKit`

iOS 27.2 dyld shared cache image. Version `174.4.0.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/PrivateFrameworks/TextureIO.framework/TextureIO`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/Frameworks/ImageIO.framework/ImageIO`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 21 classes, 13 protocols, 321 methods, 118 properties

### Class pages

Every class and protocol, with its methods: [`CALayerDelegate`](../objc/CALayerDelegate_MetalKit.protocol.md), [`CAMetalDrawable`](../objc/CAMetalDrawable_MetalKit.protocol.md), [`MDLMeshBuffer`](../objc/MDLMeshBuffer_MetalKit.protocol.md), [`MDLMeshBufferAllocator`](../objc/MDLMeshBufferAllocator_MetalKit.protocol.md), [`MDLMeshBufferZone`](../objc/MDLMeshBufferZone_MetalKit.protocol.md), [`MDLNamed`](../objc/MDLNamed_MetalKit.protocol.md), [`MTKMesh`](../objc/MTKMesh_MetalKit.md), [`MTKMeshBuffer`](../objc/MTKMeshBuffer_MetalKit.md), [`MTKMeshBufferAllocator`](../objc/MTKMeshBufferAllocator_MetalKit.md), [`MTKMeshBufferHolder`](../objc/MTKMeshBufferHolder_MetalKit.md), [`MTKMeshBufferZone`](../objc/MTKMeshBufferZone_MetalKit.md), [`MTKOffscreenDrawable`](../objc/MTKOffscreenDrawable_MetalKit.md), [`MTKSubmesh`](../objc/MTKSubmesh_MetalKit.md), [`MTKTextureIOBuffer`](../objc/MTKTextureIOBuffer_MetalKit.md), [`MTKTextureIOBufferAllocator`](../objc/MTKTextureIOBufferAllocator_MetalKit.md), [`MTKTextureIOBufferMap`](../objc/MTKTextureIOBufferMap_MetalKit.md), [`MTKTextureLoader`](../objc/MTKTextureLoader_MetalKit.md), [`MTKTextureLoaderASTCHelper`](../objc/MTKTextureLoaderASTCHelper_MetalKit.md), [`MTKTextureLoaderData`](../objc/MTKTextureLoaderData_MetalKit.md), [`MTKTextureLoaderImageIO`](../objc/MTKTextureLoaderImageIO_MetalKit.md), [`MTKTextureLoaderKTX`](../objc/MTKTextureLoaderKTX_MetalKit.md), [`MTKTextureLoaderMDL`](../objc/MTKTextureLoaderMDL_MetalKit.md), [`MTKTextureLoaderPVR`](../objc/MTKTextureLoaderPVR_MetalKit.md), [`MTKTextureLoaderPVR3`](../objc/MTKTextureLoaderPVR3_MetalKit.md), [`MTKTextureUploader`](../objc/MTKTextureUploader_MetalKit.md), [`MTKView`](../objc/MTKView_MetalKit.md), [`MTKViewDisplayLinkTarget`](../objc/MTKViewDisplayLinkTarget_MetalKit.md), [`MTLDrawable`](../objc/MTLDrawable_MetalKit.protocol.md), [`NSCoding`](../objc/NSCoding_MetalKit.protocol.md), [`NSCopying`](../objc/NSCopying_MetalKit.protocol.md), [`NSObject`](../objc/NSObject_MetalKit.protocol.md), [`TXRBuffer`](../objc/TXRBuffer_MetalKit.protocol.md), [`TXRBufferAllocator`](../objc/TXRBufferAllocator_MetalKit.protocol.md), [`TXRBufferMap`](../objc/TXRBufferMap_MetalKit.protocol.md)

### Classes

`MTKMesh`, `MTKMeshBuffer`, `MTKMeshBufferAllocator`, `MTKMeshBufferHolder`, `MTKMeshBufferZone`, `MTKOffscreenDrawable`, `MTKSubmesh`, `MTKTextureIOBuffer`, `MTKTextureIOBufferAllocator`, `MTKTextureIOBufferMap`, `MTKTextureLoader`, `MTKTextureLoaderASTCHelper`, `MTKTextureLoaderData`, `MTKTextureLoaderImageIO`, `MTKTextureLoaderKTX`, `MTKTextureLoaderMDL`, `MTKTextureLoaderPVR`, `MTKTextureLoaderPVR3`, `MTKTextureUploader`, `MTKView`, `MTKViewDisplayLinkTarget`

### Protocols

`CALayerDelegate`, `CAMetalDrawable`, `MDLMeshBuffer`, `MDLMeshBufferAllocator`, `MDLMeshBufferZone`, `MDLNamed`, `MTLDrawable`, `NSCoding`, `NSCopying`, `NSObject`, `TXRBuffer`, `TXRBufferAllocator`, `TXRBufferMap`

### Properties

```
@property (T@"<MTLTexture>",R) texture;
@property (T@"CAMetalLayer",R) layer;
@property (TQ,R,N) length;
@property (T@"<MDLMeshBufferAllocator>",R,&,N) allocator;
@property (T@"<MDLMeshBufferZone>",R,&,N) zone;
@property (TQ,R,N) type;
@property (TQ,R,N) capacity;
@property (T@"<MDLMeshBufferAllocator>",R,N) allocator;
@property (T@"NSString",C,N) name;
@property (Td,R,N) presentedTime;
@property (TQ,R,N) drawableID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^v,R,N) bytes;
@property (T@"NSArray",R,N,V_vertexBuffers) vertexBuffers;
@property (T@"MDLVertexDescriptor",R,N,V_vertexDescriptor) vertexDescriptor;
@property (T@"NSArray",R,N,V_submeshes) submeshes;
@property (TQ,R,N,V_vertexCount) vertexCount;
@property (T@"NSString",C,N,V_name) name;
@property (TQ,R,N,V_length) length;
@property (T@"MTKMeshBufferAllocator",R,N,V_allocator) allocator;
@property (T@"<MDLMeshBufferZone>",R,N,V_zone) zone;
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R,N,V_offset) offset;
@property (TQ,R,N,V_type) type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",C,N) name;
@property (T@"<MTLDevice>",R,N,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"MTKMeshBuffer",V_buffer) buffer;
@property (TQ,R,N,V_capacity) capacity;
@property (T@"<MDLMeshBufferAllocator>",R,N,V_allocator) allocator;
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CAMetalLayer",R,V_layer) layer;
@property (T@"<MTLTexture>",R) texture;
@property (Td,R,N,V_presentedTime) presentedTime;
@property (TQ,R,N,V_drawableID) drawableID;
@property (T@"<MTLDevice>",&,N,V_device) device;
@property (T{CGSize=dd},N) size;
@property (TQ,N) pixelFormat;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N,V_primitiveType) primitiveType;
@property (TQ,R,N,V_indexType) indexType;
@property (T@"MTKMeshBuffer",R,N,V_indexBuffer) indexBuffer;
@property (TQ,R,N,V_indexCount) indexCount;
@property (T@"MTKMesh",R,W,N,V_mesh) mesh;
@property (T@"NSString",C,N,V_name) name;
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^v,R,N) bytes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<MTLDevice>",R,N) device;
@property (T@"NSString",N,V_imageOrigin) imageOrigin;
@property (TQ,N,V_numArrayElements) numArrayElements;
@property (TQ,N,V_numFaces) numFaces;
@property (TQ,N,V_numMipmapLevels) numMipmapLevels;
@property (TQ,N,V_width) width;
@property (TQ,N,V_height) height;
@property (TQ,N,V_depth) depth;
@property (TQ,N,V_textureType) textureType;
@property (TQ,N,V_pixelFormat) pixelFormat;
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
@property (T@"MTKView",W,N,V_target) target;
```

## Strings (199)

```
txrTexture.pixelFormat < 0x80000000
MDLSubmesh
MTKView Stencil
MTKViewClearColorCoderKey
32Bit idnices:
MTKTextureLoaderCubeLayoutVertical
MTKTextureLoaderOptionGenerateMipmaps is only supported for color renderable and filterable pixel formats
com.apple.MTKTextureLoader
ktxorientation
MTKModelErrorKey
/
MTKViewFirstFrameDump
MTKViewFrameDumpAfterSeconds_%lu
PVR header metadata size too large
v8@?0
getFillValueForComponentType
MTKTextureLoaderKTX.m
Vertical flip is not supported for block texture formats
MTKModel.m
MDLMeshBufferMap
MTKViewFramerateAfterSeconds_%lu
Vertical flip is not supported for compressed PVR textures
MTKTextureLoaderOptionGenerateMipmaps
MTKTextureLoaderOptionTextureStorageMode
[MTKTextureLoaderPVR isPVRFile:data] && \"This function should not be reachable.\"
false && \"Unsupported MTKOSVersion\"
Could not determine format from MDLTexture
MTKTextureLoaderOptionAllocateMipmaps
MTKTextureLoaderOriginTopLeft
Image decoding failed
/tmp
MTKView Depth
bytesReturned == bytesExpected
MTKViewPausedCoderKey
MTKTextureLoaderPVR3.m
Too many vertex attributes in MTLVertexDescriptor to create a MDLVertexDescriptor
-[MTKMeshBufferZone destroyBuffer:]
.txt
source != nil
Vertical flip is only supported for 2D, 2D array, and cube map textures
bytes && texture
MTKTextureLoaderOptionTextureUsage
MTKTextureLoaderPVR.m
!\"Model I/O vertex descriptor attribute count should be at least MTL_MAX_VERTEX_ATTRIBUTES\"
!\"Model I/O vertex descriptor layouts count should be at least MTL_MAX_VERTEX_BUFFERS\"
Portrait
LandscapeLeft
MTKViewClearDepthCoderKey
MTKViewFrameDumpAfterFrame_%d
clearColor
Could not parse KTX metadata
com.apple.mtktextureloaderload
No compatible MTLVertexFormat format for MDLVertexAttribute format
MTKViewColorPixelFormatArrayCoderKey
MTKViewPresentsWithTransactionCoderKey
MTKTextureUploader.m
Could not find resource %@ at specified location.
[image.buffer isKindOfClass:[MTKTextureIOBuffer class]]
MTKTextureLoaderImageIO.m
Could not determine format from KTX header
destination != nil
/System/Library/Frameworks/ModelIO.framework/ModelIO
MTK_DUMP_FRAME_AFTER_SECONDS
!\"No texture loader supports MSAA or TexBuffers\"
!error && \"Should not get here if we already encountered an error\"
Texture height %lu exceeds device support of 1..%lu for texture type %@
Textures must have 1, 2, or 4 channels
MTKTextureLoaderErrorDomain
MTKTextureLoaderOptionPackedRowStride
MTKTextureLoaderOriginBottomLeft
MTKTextureLoaderOriginFlippedVertically
Failed to allocate texture memory.
Texture malformed.
Creating cube maps from 2D textures is not supported for MDL textures
getASTCHDRFormatForPixelFormat
S=r,T=u
-[MTKTextureLoaderPVR initWithData:options:error:]
MTK_DRAW_OFFSCREEN
Couldn't export image to TGA %@
-[MTKView _dumpFrameImageWithFilename:]
MTKView.m
MTKViewClearStencilCoderKey
MTKViewAutoResizeDrawableCoderKey
_residencySet != nil
!!
clearStencil
MTKTextureLoaderOptionCubeLayout
-[MTKTextureLoader _newSyncTexturesFromTXRTextures:labels:options:error:]
MTKModelErrorDomain
A
file:///
%d 
16Bit idnices:
Metal does not support texture cube arrays
com.apple.mtktextureloadernotify
txrTexture.dimensions.x == txrTexture.dimensions.y
orientation
LandscapeRight
MTKView Depth Stencil
sampleCount
[MTKTextureLoaderKTX isKTXFile:data] && \"Function should not be reachable.\"
expandRGBToRGBA
MTK_MEASURE_FRAMERATE_AFTER_SECONDS
MTK_DUMP_PATH
MTKViewNumberColorPixelFormatsCoderKey
MTKViewSampleCountCoderKey
MTKViewPreferredFramesPerSecondCoderKey
-[MTKView setDepthStencilPixelFormat:]
Invalid NSData, %@
-[MTKTextureLoaderKTX initWithData:options:error:]
MTKTextureLoader_Internal.m
MTK_DUMP_FIRST_FRAME
%f
MTKViewEnableSetNeedsDisplayCoderKey
MTKViewFramerateAfterFrame_%d
-[MTKView setContentScaleFactor:]
Creating cube maps from 2D textures is not supported for PVR files
-[MTKTextureUploader copyTexture:toTexture:]
Creating cube maps from 2D textures is not supported for KTX files
required conversion from orginal submesh indexType and geometryType failed
-[MTKTextureLoaderPVR3 initWithData:options:error:]
Could not determine format from PVR header
MTKTextureLoader.m
Could not find texture or image named \"%@\" in supplied bundle
!\"Unhandled PixelFormat\"
MTKViewFramebufferOnlyCoderKey
MTKTextureLoaderOptionSRGB
Texture width %lu exceeds device support of 1..%lu for texture type %@
0 && \"Unhandled texture type\"
Must supply asset
MTK_DUMP_FRAME_AFTER_FRAME
PortraitUpsideDown
Image Dump Error - %s: %s 
MTKViewColorPixelFormatCoderKey
Pixel format(%s) is not valid on this device
MTKTextureLoaderOptionTextureCPUCacheMode
MTKTextureLoaderOptionOrigin
Texture array element count %lu exceeds device support of 1..%lu for texture type %@
Attempt to load a cubemap array on platform that does not support cubemap arrays
arrayTextureTypeFromTextureType
MDLVertexDescriptor
KTX metadata size exceeds metadata region size
-[MTKTextureUploader copyBytes:toTexture:bitsPerPixel:pixelComponents:bytesPerRow:bytesPerImage:region:slice:level:flipVertically:]
Unsupported image orientation
!\"Incorrect values being passed to fillForComponent\"
Could not load ASTC texture, data is malformed
[MTKTextureLoaderPVR3 isPVR3File:data] && \"This function should not be reachable\"
kCGImageBlockSingletonRequest
vertex buffer in MDLMesh was not created using a MTKMeshBufferAllocator
MDLMesh
-[MTKView initWithCoder:]
MTKViewDrawableAttachmentIndexCoderKey
clearDepth
MetalKit_Internal.m
URL is nil
invalid geometry type in submesh
MTK_MEASURE_FRAMERATE_AFTER_FRAME
MTK_FORCE_ORIENTATION
srcTexture && dstTexture
-[MTKTextureLoader _loadData:options:uploader:label:completionHandler:]
Texture depth %lu exceeds device support of 1..%lu for texture type %@
MTK_TERMINATE_AFTER_FRAME
MTK_TERMINATE_AFTER_SECONDS
com.apple.MTKView.residencySet
MTKTextureLoaderErrorKey
MTKTextureLoaderOptionCubeFromVerticalTexture
com.apple.mtktextureloaderupload
Texture mipmap level count %lu invalid for texture with dimensions %lux%lux%lu
Could not get asset catalog from supplied bundle
invalid index type submesh
depthStencilPixelFormat != MTLPixelFormatX32_Stencil8 && \"depthStencilPixelFormat cannot be a stencil texture view pixel format\"
-[MTKView _initializeResidencyManagement]
Too many vertex layouts in MTLVertexDescriptor to create a MDLVertexDescriptor
png
self.contentScaleFactor != 0
MTKTextureLoaderOptionLoadAsArray
v24@?0@\"NSArray\"8@\"NSError\"16
1 == txrTexture.dimensions.z
kCGImageBlockFormatBGRx8
S=r,T=d
index buffer in MDLSubmesh was not created using a MTKMeshBufferAllocator
MTKModelIOVertexDescriptorFromMetalWithError
MTKViewDepthStencilPixelFormatCoderKey
v24@?0@\"<MTLTexture>\"8@\"NSError\"16
Texture face count %lu does not match expected value %lu for texture type %@
v32@?0@\"TXRTexture\"8Q16^B24
kCGImageBlockIOSurfaceOptimizedRequest
kCGImageBlockFormatRequest
false && \"Expected format tagged by isPixelFormatASTCLDR\"
_mtkLinkedOnOrAfter
Textures must use 8 or 16 bits per channel
v16@?0@\"<MTLCommandBuffer>\"8
Image height must be six times the image width for a vertical cubemap texture
Must supply device
No compatible MDLVertexFormat format for MTLVertexAttribute format
MTKMeshBufferZone.m
destroyedBuffer.zone == self
public.png
v40@?0r^v8{_NSRange=QQ}16^B32
```
