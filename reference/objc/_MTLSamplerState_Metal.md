# `_MTLSamplerState`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLSamplerStateSPI`
- 5 instance variables, 12 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"NSString" _label;
Q _pixelFormat;
Q _resourceIndex;
Q _gpuAddress;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R) uniqueIdentifier;
@property (TQ,R,N,V_pixelFormat) pixelFormat;
@property (TQ,?,R,N,V_resourceIndex) resourceIndex;
@property (TQ,?,R,N,V_gpuAddress) gpuAddress;
@property (TQ,?,R) gpuHandle;
@property (T@"NSString",R,V_label) label;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLSamplerState resourceIndex];
-[_MTLSamplerState formattedDescription:];
-[_MTLSamplerState device];
-[_MTLSamplerState label];
-[_MTLSamplerState dealloc];
-[_MTLSamplerState gpuAddress];
-[_MTLSamplerState uniqueIdentifier];
-[_MTLSamplerState gpuHandle];
-[_MTLSamplerState description];
-[_MTLSamplerState pixelFormat];
-[_MTLSamplerState initWithDevice:samplerDescriptor:];
-[_MTLSamplerState gpuResourceID];
```
