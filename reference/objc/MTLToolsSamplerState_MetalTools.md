# `MTLToolsSamplerState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLSamplerState`, `MTLSamplerStateSPI`
- 0 instance variables, 12 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) pixelFormat;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,?,R) uniqueIdentifier;
@property (TQ,?,R) gpuHandle;
```

## Instance methods

```
-[MTLToolsSamplerState resourceIndex];
-[MTLToolsSamplerState device];
-[MTLToolsSamplerState label];
-[MTLToolsSamplerState dealloc];
-[MTLToolsSamplerState gpuAddress];
-[MTLToolsSamplerState uniqueIdentifier];
-[MTLToolsSamplerState gpuHandle];
-[MTLToolsSamplerState pixelFormat];
-[MTLToolsSamplerState gpuResourceID];
-[MTLToolsSamplerState initWithSamplerState:descriptor:device:];
```
