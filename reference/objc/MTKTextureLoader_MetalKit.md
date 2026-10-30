# `MTKTextureLoader`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _loadQueue;
@"NSObject<OS_dispatch_queue>" _uploadQueue;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
@"NSObject<OS_dispatch_semaphore>" _loadSemaphore;
@"<MTLCommandQueue>" _blitQueue;
@"<TXRBufferAllocator>" _bufferAllocator;
@"<MTLDeviceSPI>" _device;
```

## Properties

```
@property (T@"<MTLDevice>",R,N) device;
```

## Instance methods

```
-[MTKTextureLoader initWithDevice:];
-[MTKTextureLoader device];
-[MTKTextureLoader dealloc];
-[MTKTextureLoader newTextureWithData:options:error:];
-[MTKTextureLoader newTextureWithCGImage:options:error:];
-[MTKTextureLoader newTextureWithContentsOfURL:options:error:];
-[MTKTextureLoader newTextureWithName:scaleFactor:bundle:options:error:];
-[MTKTextureLoader newTextureWithCGImage:options:completionHandler:];
-[MTKTextureLoader newTextureWithContentsOfURL:options:completionHandler:];
-[MTKTextureLoader newTextureWithName:scaleFactor:bundle:options:completionHandler:];
-[MTKTextureLoader _determineFileType:];
-[MTKTextureLoader _loadCGImage:options:completionHandler:];
-[MTKTextureLoader _loadData:options:completionHandler:];
-[MTKTextureLoader _loadData:options:uploader:label:completionHandler:];
-[MTKTextureLoader _loadMDLTexture:options:completionHandler:];
-[MTKTextureLoader _newAsyncTextureWithNames:scaleFactor:displayGamut:bundle:options:completionHandler:];
-[MTKTextureLoader _newSyncTexturesFromTXRTextures:labels:options:error:];
-[MTKTextureLoader newTextureFromTXRTexture:options:error:];
-[MTKTextureLoader newTextureWithData:options:completionHandler:];
-[MTKTextureLoader newTextureWithMDLTexture:options:completionHandler:];
-[MTKTextureLoader newTextureWithMDLTexture:options:error:];
-[MTKTextureLoader newTextureWithName:scaleFactor:displayGamut:bundle:options:completionHandler:];
-[MTKTextureLoader newTextureWithName:scaleFactor:displayGamut:bundle:options:error:];
-[MTKTextureLoader newTexturesFromTXRTextures:options:error:];
-[MTKTextureLoader newTexturesWithContentsOfURLs:options:completionHandler:];
-[MTKTextureLoader newTexturesWithContentsOfURLs:options:error:];
-[MTKTextureLoader newTexturesWithNames:scaleFactor:bundle:options:completionHandler:];
-[MTKTextureLoader newTexturesWithNames:scaleFactor:displayGamut:bundle:options:completionHandler:];
-[MTKTextureLoader newUploaderForOptions:];
-[MTKTextureLoader validateGenerateMipmapsForPixelFormat:options:error:];
```
