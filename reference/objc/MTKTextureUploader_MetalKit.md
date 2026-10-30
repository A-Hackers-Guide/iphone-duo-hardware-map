# `MTKTextureUploader`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTLCommandBuffer>" _commandBuffer;
@"<MTLBlitCommandEncoder>" _blit;
@"NSLock" _lock;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
```

## Instance methods

```
-[MTKTextureUploader dealloc];
-[MTKTextureUploader finishWithCompletionHandler:];
-[MTKTextureUploader generateMipmapsForTexture:];
-[MTKTextureUploader newTextureWithData:options:error:];
-[MTKTextureUploader copyBytes:toTexture:bitsPerPixel:pixelComponents:bytesPerRow:bytesPerImage:region:slice:level:flipVertically:];
-[MTKTextureUploader copyTexture:toTexture:];
-[MTKTextureUploader initWithDevice:commandQueue:notifyQueue:];
```
