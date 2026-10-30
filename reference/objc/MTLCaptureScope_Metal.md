# `MTLCaptureScope`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLCaptureScope`
- 3 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _commandQueue;
@"<MTL4CommandQueue>" _mtl4CommandQueue;
```

## Properties

```
@property (T@"NSString",C,D) label;
@property (T@"<MTLDevice>",R,N,V_device) device;
@property (T@"<MTLCommandQueue>",R,N,V_commandQueue) commandQueue;
@property (T@"<MTL4CommandQueue>",R,N,V_mtl4CommandQueue) mtl4CommandQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLCaptureScope initWithDevice:mtl4CommandQueue:];
-[MTLCaptureScope device];
-[MTLCaptureScope mtl4CommandQueue];
-[MTLCaptureScope dealloc];
-[MTLCaptureScope initWithDevice:commandQueue:];
-[MTLCaptureScope beginScope];
-[MTLCaptureScope commandQueue];
-[MTLCaptureScope endScope];
```
