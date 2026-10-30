# `MTLDebugCommandEncoder` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoderSPI`
- 0 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance methods

```
-[MTLDebugCommandEncoder kprintfBytes:length:];
-[MTLDebugCommandEncoder IOLog:];
-[MTLDebugCommandEncoder IOLogBytes:length:];
-[MTLDebugCommandEncoder kprintf:];
-[MTLDebugCommandEncoder stopCapture];
-[MTLDebugCommandEncoder startCapture];
-[MTLDebugCommandEncoder postFinishEvent];
-[MTLDebugCommandEncoder dumpBuffer:];
-[MTLDebugCommandEncoder dumpBuffer:name:];
-[MTLDebugCommandEncoder dumpTexture:];
-[MTLDebugCommandEncoder dumpTexture:name:];
-[MTLDebugCommandEncoder dumpTexture:name:glMode:];
-[MTLDebugCommandEncoder getLastStartStopCaptureResult];
-[MTLDebugCommandEncoder postFinishEvent:];
-[MTLDebugCommandEncoder startCaptureWithSettings:];
-[MTLDebugCommandEncoder startCaptureWithSettings:from:];
-[MTLDebugCommandEncoder stopCapture:];
```
