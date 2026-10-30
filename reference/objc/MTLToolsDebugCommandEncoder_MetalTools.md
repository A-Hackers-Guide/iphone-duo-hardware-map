# `MTLToolsDebugCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandEncoder`
- Protocols: `MTLDebugCommandEncoder`
- 0 instance variables, 6 properties, 17 instance methods, 0 class methods

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
-[MTLToolsDebugCommandEncoder stopCapture];
-[MTLToolsDebugCommandEncoder kprintfBytes:length:];
-[MTLToolsDebugCommandEncoder startCapture];
-[MTLToolsDebugCommandEncoder IOLog:];
-[MTLToolsDebugCommandEncoder postFinishEvent];
-[MTLToolsDebugCommandEncoder IOLogBytes:length:];
-[MTLToolsDebugCommandEncoder dumpBuffer:];
-[MTLToolsDebugCommandEncoder dumpBuffer:name:];
-[MTLToolsDebugCommandEncoder dumpTexture:];
-[MTLToolsDebugCommandEncoder dumpTexture:name:];
-[MTLToolsDebugCommandEncoder dumpTexture:name:glMode:];
-[MTLToolsDebugCommandEncoder getLastStartStopCaptureResult];
-[MTLToolsDebugCommandEncoder kprintf:];
-[MTLToolsDebugCommandEncoder postFinishEvent:];
-[MTLToolsDebugCommandEncoder startCaptureWithSettings:];
-[MTLToolsDebugCommandEncoder startCaptureWithSettings:from:];
-[MTLToolsDebugCommandEncoder stopCapture:];
```
