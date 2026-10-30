# `MPSGraphDevice`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 4 instance variables, 5 properties, 7 instance methods, 5 class methods

## Instance variables

```
I _type;
@"<MTLDevice>" _metalDevice;
@"NSString" _metalDeviceName;
@"MPSGraphDeviceDescriptor" _deviceDescriptor;
```

## Properties

```
@property (T@"NSString",R,N,V_metalDeviceName) metalDeviceName;
@property (Tq,R,N) gpuCoreCount;
@property (T@"MPSGraphDeviceDescriptor",R,N,V_deviceDescriptor) deviceDescriptor;
@property (TI,R,N,V_type) type;
@property (T@"<MTLDevice>",R,N,V_metalDevice) metalDevice;
```

## Class methods

```
+[MPSGraphDevice initialize];
+[MPSGraphDevice deviceWithMTLDevice:];
+[MPSGraphDevice CPUDevice];
+[MPSGraphDevice ANEDevice];
+[MPSGraphDevice getSoCName];
```

## Instance methods

```
-[MPSGraphDevice metalDevice];
-[MPSGraphDevice type];
-[MPSGraphDevice gpuCoreCount];
-[MPSGraphDevice deviceDescriptor];
-[MPSGraphDevice initWithDeviceDescriptor:];
-[MPSGraphDevice initWithDeviceType:metalDevice:];
-[MPSGraphDevice metalDeviceName];
```
