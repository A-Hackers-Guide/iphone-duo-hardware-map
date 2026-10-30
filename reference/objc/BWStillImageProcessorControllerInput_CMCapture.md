# `BWStillImageProcessorControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"BWStillImageSettings" _settings;
@"BWStillImageCaptureStreamSettings" _captureStreamSettings;
@"NSMutableDictionary" _outputSampleBufferRoutersByBufferType;
@"<BWStillImageProcessorControllerInputUpdatesDelegate>" _delegate;
```

## Properties

```
@property (T@"<BWStillImageProcessorControllerInputUpdatesDelegate>",&,N,V_delegate) delegate;
@property (T@"BWStillImageSettings",R,N) stillImageSettings;
@property (T@"FigCaptureStillImageSettings",R,N) settings;
@property (T@"BWStillImageCaptureSettings",R,N) captureSettings;
@property (T@"BWStillImageCaptureStreamSettings",R,N) captureStreamSettings;
@property (T@"BWStillImageProcessingSettings",R,N) processingSettings;
@property (TB,R,N) isMaster;
@property (T@"NSString",R,N) portType;
```

## Instance methods

```
-[BWStillImageProcessorControllerInput stillImageSettings];
-[BWStillImageProcessorControllerInput portType];
-[BWStillImageProcessorControllerInput settings];
-[BWStillImageProcessorControllerInput dealloc];
-[BWStillImageProcessorControllerInput setDelegate:];
-[BWStillImageProcessorControllerInput delegate];
-[BWStillImageProcessorControllerInput captureStreamSettings];
-[BWStillImageProcessorControllerInput description];
-[BWStillImageProcessorControllerInput initWithSettings:portType:];
-[BWStillImageProcessorControllerInput captureSettings];
-[BWStillImageProcessorControllerInput isMaster];
-[BWStillImageProcessorControllerInput addBypassedProcessorType:forBufferTypes:];
-[BWStillImageProcessorControllerInput addOutputSampleBufferRouter:forBufferTypes:];
-[BWStillImageProcessorControllerInput addOutputSampleBufferRouter:forBufferTypes:name:];
-[BWStillImageProcessorControllerInput outputSampleBufferRouterForBufferType:];
-[BWStillImageProcessorControllerInput processingSettings];
```
