# `EGStillImageStereoPhotoPreDeepZoomMergingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGQueueManagementNode`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _primarySbufInput;
@"EGInput" _secondarySbufInput;
@"EGStillImageOutput" _secondarySbufOutput;
```

## Properties

```
@property (T@"EGInput",R,N,V_primarySbufInput) primarySbufInput;
@property (T@"EGInput",R,N,V_secondarySbufInput) secondarySbufInput;
@property (T@"EGOutput",R,N,V_secondarySbufOutput) secondarySbufOutput;
```

## Class methods

```
+[EGStillImageStereoPhotoPreDeepZoomMergingNode initialize];
```

## Instance methods

```
-[EGStillImageStereoPhotoPreDeepZoomMergingNode dealloc];
-[EGStillImageStereoPhotoPreDeepZoomMergingNode initWithName:];
-[EGStillImageStereoPhotoPreDeepZoomMergingNode primarySbufInput];
-[EGStillImageStereoPhotoPreDeepZoomMergingNode queueManagedReceiveData:fromInputGroup:];
-[EGStillImageStereoPhotoPreDeepZoomMergingNode secondarySbufInput];
-[EGStillImageStereoPhotoPreDeepZoomMergingNode secondarySbufOutput];
```
