# `MTKTextureIOBufferAllocator`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TXRBufferAllocator`
- 1 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTKTextureIOBufferAllocator initWithDevice:];
-[MTKTextureIOBufferAllocator newBufferWithLength:];
-[MTKTextureIOBufferAllocator newBufferWithBytesNoCopy:length:deallocNotification:error:];
```
