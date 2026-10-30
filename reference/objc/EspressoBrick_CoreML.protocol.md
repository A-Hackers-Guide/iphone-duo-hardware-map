# `EspressoBrick` (protocol)

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance methods

```
-[EspressoBrick initWithParameters:];
-[EspressoBrick hasGPUSupport];
-[EspressoBrick setupForInputShapes:withParameters:];
-[EspressoBrick computeDynamicOutputShape:];
-[EspressoBrick computeOnCPUWithInputTensors:outputTensors:];
-[EspressoBrick encodeToMetalCommandBuffer:inputTensors:outputTensors:];
-[EspressoBrick hasDynamicOutputShape:];
-[EspressoBrick setMappedWeights:sizeInBytes:];
```
