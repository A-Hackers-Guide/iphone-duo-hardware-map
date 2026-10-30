# `ICDocCamImageSequenceFrame`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _pb;
@"NSDictionary" _frameOptions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropRegionOfInterest;
```

## Properties

```
@property (T^{__CVBuffer=},N,V_pb) pb;
@property (T@"NSDictionary",C,N,V_frameOptions) frameOptions;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_cropRegionOfInterest) cropRegionOfInterest;
```

## Instance methods

```
-[ICDocCamImageSequenceFrame init];
-[ICDocCamImageSequenceFrame cropRegionOfInterest];
-[ICDocCamImageSequenceFrame frameOptions];
-[ICDocCamImageSequenceFrame pb];
-[ICDocCamImageSequenceFrame setCropRegionOfInterest:];
-[ICDocCamImageSequenceFrame setFrameOptions:];
-[ICDocCamImageSequenceFrame setPb:];
```
