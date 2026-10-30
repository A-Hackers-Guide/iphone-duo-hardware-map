# `MTLCaptureScope` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R,N) device;
@property (T@"<MTLCommandQueue>",R,N) commandQueue;
@property (T@"<MTL4CommandQueue>",R,N) mtl4CommandQueue;
```

## Instance methods

```
-[MTLCaptureScope device];
-[MTLCaptureScope label];
-[MTLCaptureScope mtl4CommandQueue];
-[MTLCaptureScope setLabel:];
-[MTLCaptureScope beginScope];
-[MTLCaptureScope commandQueue];
-[MTLCaptureScope endScope];
```
