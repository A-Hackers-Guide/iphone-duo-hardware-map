# `EGStillImagePiecemealEncodingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWPhotoEncoderControllerDelegate`
- 7 instance variables, 7 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"EGInput" _sbufInput;
@"EGStillImageOutput" _encodingCompleteOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"NSString" _portType;
i _mode;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_encodingCompleteOutput) encodingCompleteOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImagePiecemealEncodingNode initialize];
```

## Instance methods

```
-[EGStillImagePiecemealEncodingNode dealloc];
-[EGStillImagePiecemealEncodingNode encodingCompleteOutput];
-[EGStillImagePiecemealEncodingNode initWithName:stillImageSettings:resourceCoordinator:portType:mode:delegate:];
-[EGStillImagePiecemealEncodingNode processorInput];
-[EGStillImagePiecemealEncodingNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImagePiecemealEncodingNode sbufInput];
```
