# `MTLIOAccelCommandQueue`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLCommandQueue`
- 4 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
^{__IOAccelCommandQueue=} _commandQueue;
@"MTLIOAccelDevice<MTLDevice>" _device;
Q _priority;
Q _backgroundPriority;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
```

## Instance methods

```
-[MTLIOAccelCommandQueue setGPUPriority:];
-[MTLIOAccelCommandQueue initWithDevice:descriptor:];
-[MTLIOAccelCommandQueue device];
-[MTLIOAccelCommandQueue setLabel:];
-[MTLIOAccelCommandQueue setBackgroundGPUPriority:offset:];
-[MTLIOAccelCommandQueue dealloc];
-[MTLIOAccelCommandQueue submitCommandBuffers:count:];
-[MTLIOAccelCommandQueue _setGPUPriority:backgroundPriority:];
-[MTLIOAccelCommandQueue getBackgroundGPUPriority];
-[MTLIOAccelCommandQueue setGPUPriority:offset:];
-[MTLIOAccelCommandQueue getGPUPriority];
-[MTLIOAccelCommandQueue setCompletionQueue:];
-[MTLIOAccelCommandQueue setBackgroundGPUPriority:];
```
