# `EGStillImageStereoPhotoStagingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGQueueManagementNode`
- 9 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _gatingInput;
@"EGInput" _primarySbufInput;
@"EGInput" _secondarySbufInput;
@"EGStillImageOutput" _primarySbufOutput;
@"EGStillImageOutput" _secondarySbufOutput;
@"EGStillImageOutput" _primaryDCConfigurationDataOutput;
@"EGStillImageOutput" _secondaryDCConfigurationDataOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
```

## Properties

```
@property (T@"EGInput",R,N,V_gatingInput) gatingInput;
@property (T@"EGInput",R,N,V_primarySbufInput) primarySbufInput;
@property (T@"EGInput",R,N,V_secondarySbufInput) secondarySbufInput;
@property (T@"EGOutput",R,N,V_primarySbufOutput) primarySbufOutput;
@property (T@"EGOutput",R,N,V_secondarySbufOutput) secondarySbufOutput;
@property (T@"EGOutput",R,N,V_primaryDCConfigurationDataOutput) primaryDCConfigurationDataOutput;
@property (T@"EGOutput",R,N,V_secondaryDCConfigurationDataOutput) secondaryDCConfigurationDataOutput;
```

## Class methods

```
+[EGStillImageStereoPhotoStagingNode initialize];
```

## Instance methods

```
-[EGStillImageStereoPhotoStagingNode dealloc];
-[EGStillImageStereoPhotoStagingNode gatingInput];
-[EGStillImageStereoPhotoStagingNode initWithName:stillImageSettings:nodeConfiguration:];
-[EGStillImageStereoPhotoStagingNode primaryDCConfigurationDataOutput];
-[EGStillImageStereoPhotoStagingNode primarySbufInput];
-[EGStillImageStereoPhotoStagingNode primarySbufOutput];
-[EGStillImageStereoPhotoStagingNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageStereoPhotoStagingNode secondaryDCConfigurationDataOutput];
-[EGStillImageStereoPhotoStagingNode secondarySbufInput];
-[EGStillImageStereoPhotoStagingNode secondarySbufOutput];
```
