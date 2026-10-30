# `EGStillImageInferenceMergingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGQueueManagementNode`
- 4 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _sbufInput;
@"EGStillImageOutput" _sbufOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
```

## Properties

```
@property (T@"EGInput",R,N,V_sbufInput) sbufInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
```

## Class methods

```
+[EGStillImageInferenceMergingNode initialize];
```

## Instance methods

```
-[EGStillImageInferenceMergingNode dealloc];
-[EGStillImageInferenceMergingNode initWithName:stillImageSettings:resourceCoordinator:];
-[EGStillImageInferenceMergingNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageInferenceMergingNode sbufInput];
-[EGStillImageInferenceMergingNode sbufOutput];
```
