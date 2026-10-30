# `AGXG19FamilyDebugContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalDebugCommandEncoder`
- Protocols: `MTLDebugCommandEncoder`
- 1 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

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
-[AGXG19FamilyDebugContext stopCapture];
-[AGXG19FamilyDebugContext endEncoding];
-[AGXG19FamilyDebugContext dealloc];
-[AGXG19FamilyDebugContext startCapture];
-[AGXG19FamilyDebugContext postFinishEvent];
-[AGXG19FamilyDebugContext dumpBuffer:];
-[AGXG19FamilyDebugContext dumpBuffer:name:];
-[AGXG19FamilyDebugContext dumpTexture:];
-[AGXG19FamilyDebugContext dumpTexture:name:];
-[AGXG19FamilyDebugContext dumpTexture:name:glMode:];
-[AGXG19FamilyDebugContext getLastStartStopCaptureResult];
-[AGXG19FamilyDebugContext initWithCommandBuffer:];
-[AGXG19FamilyDebugContext postFinishEvent:];
-[AGXG19FamilyDebugContext startCaptureWithSettings:];
-[AGXG19FamilyDebugContext startCaptureWithSettings:from:];
-[AGXG19FamilyDebugContext stopCapture:];
```
