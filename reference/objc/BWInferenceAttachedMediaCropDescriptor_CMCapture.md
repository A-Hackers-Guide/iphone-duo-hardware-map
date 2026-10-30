# `BWInferenceAttachedMediaCropDescriptor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceCropDescriptor`
- 5 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _attachedMediaKey;
@"NSString" _cropRectKey;
{?="width"i"height"i} _targetDimensions;
B _extendCropRect;
```

## Properties

```
@property (Tc,R,N) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceAttachedMediaCropDescriptor initialize];
+[BWInferenceAttachedMediaCropDescriptor attachedMediaCropDescriptorWithName:attachedMediaKey:cropRectKey:targetDimensions:extendCropRect:];
```

## Instance methods

```
-[BWInferenceAttachedMediaCropDescriptor identifier];
-[BWInferenceAttachedMediaCropDescriptor dealloc];
-[BWInferenceAttachedMediaCropDescriptor description];
-[BWInferenceAttachedMediaCropDescriptor copyWithZone:];
-[BWInferenceAttachedMediaCropDescriptor applicableToSampleBuffer:forMediaKey:];
-[BWInferenceAttachedMediaCropDescriptor maxCropForDimensions:];
-[BWInferenceAttachedMediaCropDescriptor rectForSampleBuffer:];
```
