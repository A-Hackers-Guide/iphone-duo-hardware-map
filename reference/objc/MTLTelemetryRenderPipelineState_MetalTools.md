# `MTLTelemetryRenderPipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderPipelineState`
- 5 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
I uniqueID;
@"MTLTelemetryDevice" device;
B hasAnisoConstantSampler;
@"NSSet" activeFragmentSamplers;
@"NSSet" activeFragmentTextures;
```

## Class methods

```
+[MTLTelemetryRenderPipelineState generateUniqueID];
```

## Instance methods

```
-[MTLTelemetryRenderPipelineState dealloc];
-[MTLTelemetryRenderPipelineState accumulateUsage];
-[MTLTelemetryRenderPipelineState initWithPipelineState:reflection:parent:descriptor:];
```
