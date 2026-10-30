# `MTL4CommandQueue` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
```

## Instance methods

```
-[MTL4CommandQueue removeResidencySet:];
-[MTL4CommandQueue addResidencySets:count:];
-[MTL4CommandQueue removeResidencySets:count:];
-[MTL4CommandQueue device];
-[MTL4CommandQueue label];
-[MTL4CommandQueue addResidencySet:];
-[MTL4CommandQueue signalEvent:value:];
-[MTL4CommandQueue waitForEvent:value:];
-[MTL4CommandQueue signalDrawable:];
-[MTL4CommandQueue commit:count:];
-[MTL4CommandQueue commit:count:options:];
-[MTL4CommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:];
-[MTL4CommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:];
-[MTL4CommandQueue updateBufferMappings:heap:operations:count:];
-[MTL4CommandQueue updateTextureMappings:heap:operations:count:];
-[MTL4CommandQueue waitForDrawable:];
```
