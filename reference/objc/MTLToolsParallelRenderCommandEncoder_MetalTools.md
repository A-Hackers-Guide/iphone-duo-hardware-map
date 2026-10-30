# `MTLToolsParallelRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandEncoder`
- Protocols: `MTLParallelRenderCommandEncoderSPI`
- 0 instance variables, 6 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsParallelRenderCommandEncoder setColorStoreAction:atIndex:];
-[MTLToolsParallelRenderCommandEncoder endEncoding];
-[MTLToolsParallelRenderCommandEncoder setStencilStoreActionOptions:];
-[MTLToolsParallelRenderCommandEncoder setStencilStoreAction:];
-[MTLToolsParallelRenderCommandEncoder setDepthStoreAction:];
-[MTLToolsParallelRenderCommandEncoder setDepthStoreActionOptions:];
-[MTLToolsParallelRenderCommandEncoder setColorStoreActionOptions:atIndex:];
-[MTLToolsParallelRenderCommandEncoder isMemorylessRender];
-[MTLToolsParallelRenderCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLToolsParallelRenderCommandEncoder initWithBaseObject:parent:];
-[MTLToolsParallelRenderCommandEncoder renderCommandEncoder];
-[MTLToolsParallelRenderCommandEncoder sampledRenderCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLToolsParallelRenderCommandEncoder initWithParallelRenderCommandEncoder:parent:descriptor:];
```
