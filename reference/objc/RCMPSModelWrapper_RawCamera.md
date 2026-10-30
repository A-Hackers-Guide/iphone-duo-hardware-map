# `RCMPSModelWrapper`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RCModelWrapper`
- 13 instance variables, 7 properties, 19 instance methods, 3 class methods

## Instance variables

```
@"NSString" _path;
@"NSString" _identifier;
B _autoResetEnabled;
@ _processorOutput;
@"<MTLDevice>" _device;
@"MPSGraphExecutable" _executable;
@"NSArray" _inputPortNames;
@"NSArray" _outputPortNames;
@"NSMutableArray" _inputPorts;
@"NSMutableArray" _outputPorts;
@"NSMutableDictionary" _inputSurfaces;
@"NSMutableDictionary" _outputSurfaces;
B _isBuilt;
```

## Properties

```
@property (T@"NSString",R,V_path) path;
@property (T@"NSString",R,V_identifier) identifier;
@property (TB,R,V_autoResetEnabled) autoResetEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[RCMPSModelWrapper clearCache];
+[RCMPSModelWrapper cache];
+[RCMPSModelWrapper cachedWrapperForPath:processorOutput:discriminator:autoReset:];
```

## Instance methods

```
-[RCMPSModelWrapper initWithPath:];
-[RCMPSModelWrapper identifier];
-[RCMPSModelWrapper dealloc];
-[RCMPSModelWrapper reset];
-[RCMPSModelWrapper path];
-[RCMPSModelWrapper autoResetEnabled];
-[RCMPSModelWrapper buildAndWait];
-[RCMPSModelWrapper buildAsync];
-[RCMPSModelWrapper executeAsyncWithCommandBuffer:preInferenceEncoder:postInferenceEncoder:callback:];
-[RCMPSModelWrapper inputPortDimensionsFor:];
-[RCMPSModelWrapper outputPortDimensionsFor:];
-[RCMPSModelWrapper _createPortsFromShapedTypes:isInput:];
-[RCMPSModelWrapper _executeAsyncWithCommandBuffer:preInferenceEncoder:postInferenceEncoder:callback:];
-[RCMPSModelWrapper _build];
-[RCMPSModelWrapper _byteSizeForShape:dataType:];
-[RCMPSModelWrapper _mtlSizeFromShape:];
-[RCMPSModelWrapper _pixelFormatForDataType:];
-[RCMPSModelWrapper _tensorDataForPorts:];
-[RCMPSModelWrapper initWithPath:processorOutput:autoReset:];
```
