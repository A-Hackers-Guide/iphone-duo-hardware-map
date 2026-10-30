# `VTLowLatencyFrameInterpolationImplementation`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorImplementationPrivate`
- 1 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"VCPVideoInterpolationSession" _vcpFrameInterpolationProcessor;
```

## Properties

```
@property (Tq,?,R,N) modelID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTLowLatencyFrameInterpolationImplementation finishProcessing];
-[VTLowLatencyFrameInterpolationImplementation init];
-[VTLowLatencyFrameInterpolationImplementation modelID];
-[VTLowLatencyFrameInterpolationImplementation dealloc];
-[VTLowLatencyFrameInterpolationImplementation processWithParameters:frameOutputHandler:];
-[VTLowLatencyFrameInterpolationImplementation processWithParams:error:];
-[VTLowLatencyFrameInterpolationImplementation startSessionWithConfiguration:error:];
```
