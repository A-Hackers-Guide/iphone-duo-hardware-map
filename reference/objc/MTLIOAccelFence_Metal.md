# `MTLIOAccelFence`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLFence`
- Protocols: `MTLFenceSPI`
- 2 instance variables, 6 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelDevice<MTLDevice>" _device;
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
-[MTLIOAccelFence device];
-[MTLIOAccelFence dealloc];
-[MTLIOAccelFence initWithDevice:fenceIndex:];
```
