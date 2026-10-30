# `MTL4GPUDebugCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandQueue`
- Protocols: `MTL4GPUDebugCommandQueueGTSwizzable`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{GPUDebugDeviceOptions=b1b1b1b1b1b1} _deviceOptions;
@"NSLock" _commitMutex;
@"NSString" _tracePath;
```

## Properties

```
@property (T@"NSString",R,N,V_tracePath) tracePath;
```

## Instance methods

```
-[MTL4GPUDebugCommandQueue dealloc];
-[MTL4GPUDebugCommandQueue tracePath];
-[MTL4GPUDebugCommandQueue commit:count:];
-[MTL4GPUDebugCommandQueue commit:count:options:];
-[MTL4GPUDebugCommandQueue _checkReportBuffers:outputArray:encoderLabels:];
-[MTL4GPUDebugCommandQueue _commit:count:options:];
-[MTL4GPUDebugCommandQueue _decodeReportLogState:outputArray:encoderLabels:];
-[MTL4GPUDebugCommandQueue initWithCommandQueue:device:];
-[MTL4GPUDebugCommandQueue setUpLogState:];
```
