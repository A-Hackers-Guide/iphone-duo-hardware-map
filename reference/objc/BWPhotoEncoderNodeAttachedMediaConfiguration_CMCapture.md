# `BWPhotoEncoderNodeAttachedMediaConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
f _mainImageDownscalingFactor;
{?="width"i"height"i} _dimensions;
B _keepInputDimensions;
q _propagationMode;
```

## Properties

```
@property (Tf,R,N,V_mainImageDownscalingFactor) mainImageDownscalingFactor;
@property (T{?=ii},R,N,V_dimensions) dimensions;
@property (TB,R,N,V_keepInputDimensions) keepInputDimensions;
@property (Tq,N,V_propagationMode) propagationMode;
@property (TB,R,N) propagatesDownstream;
@property (TB,R,N) requiresEncoding;
```

## Instance methods

```
-[BWPhotoEncoderNodeAttachedMediaConfiguration dimensions];
-[BWPhotoEncoderNodeAttachedMediaConfiguration mainImageDownscalingFactor];
-[BWPhotoEncoderNodeAttachedMediaConfiguration description];
-[BWPhotoEncoderNodeAttachedMediaConfiguration propagationMode];
-[BWPhotoEncoderNodeAttachedMediaConfiguration initWithDimensions:propagationMode:];
-[BWPhotoEncoderNodeAttachedMediaConfiguration initWithKeepInputDimensions:propagationMode:];
-[BWPhotoEncoderNodeAttachedMediaConfiguration initWithMainImageDownscalingFactor:propagationMode:];
-[BWPhotoEncoderNodeAttachedMediaConfiguration keepInputDimensions];
-[BWPhotoEncoderNodeAttachedMediaConfiguration propagatesDownstream];
-[BWPhotoEncoderNodeAttachedMediaConfiguration requiresEncoding];
-[BWPhotoEncoderNodeAttachedMediaConfiguration setPropagationMode:];
```
