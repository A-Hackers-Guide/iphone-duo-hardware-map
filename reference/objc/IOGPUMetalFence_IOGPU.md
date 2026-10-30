# `IOGPUMetalFence`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLFence`
- Protocols: `MTLFenceSPI`
- 3 instance variables, 6 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice<MTLDevice>" _device;
@"IOGPUMTLFence" _fence;
I _fenceIndex;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C,D) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[IOGPUMetalFence initWithDevice:];
-[IOGPUMetalFence device];
-[IOGPUMetalFence dealloc];
```
