# `CAMPanoramaOutput`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureVideoDataOutput`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _photoEncodingBehavior;
@"CAMCaptureEngine" __engine;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceBounds;
```

## Properties

```
@property (T@"CAMCaptureEngine",R,W,N,V__engine) _engine;
@property (Tq,R,N,V_photoEncodingBehavior) photoEncodingBehavior;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceBounds) referenceBounds;
```

## Instance methods

```
-[CAMPanoramaOutput referenceBounds];
-[CAMPanoramaOutput initWithEngine:];
-[CAMPanoramaOutput photoEncodingBehavior];
-[CAMPanoramaOutput changeToEncodingBehavior:];
-[CAMPanoramaOutput changeToReferenceBounds:];
-[CAMPanoramaOutput changeToDirection:];
-[CAMPanoramaOutput _engine];
```
