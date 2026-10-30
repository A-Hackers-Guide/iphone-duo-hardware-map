# `MTKOffscreenDrawable`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMetalDrawable`
- 8 instance variables, 11 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<MTLTexture>" _texture;
Q _pixelFormat;
{CGSize="width"d"height"d} _size;
B _textureDirty;
@"CAMetalLayer" _layer;
d _presentedTime;
Q _drawableID;
@"<MTLDevice>" _device;
```

## Properties

```
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
```

## Instance methods

```
-[MTKOffscreenDrawable present];
-[MTKOffscreenDrawable addPresentedHandler:];
-[MTKOffscreenDrawable setDevice:];
-[MTKOffscreenDrawable layer];
-[MTKOffscreenDrawable device];
-[MTKOffscreenDrawable texture];
-[MTKOffscreenDrawable size];
-[MTKOffscreenDrawable presentAfterMinimumDuration:];
-[MTKOffscreenDrawable drawableID];
-[MTKOffscreenDrawable presentAtTime:];
-[MTKOffscreenDrawable pixelFormat];
-[MTKOffscreenDrawable setPixelFormat:];
-[MTKOffscreenDrawable presentedTime];
-[MTKOffscreenDrawable setSize:];
-[MTKOffscreenDrawable initWithDevice:pixelFormat:size:drawableID:];
```
