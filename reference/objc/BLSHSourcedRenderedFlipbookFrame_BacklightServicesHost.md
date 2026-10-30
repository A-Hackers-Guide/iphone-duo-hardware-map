# `BLSHSourcedRenderedFlipbookFrame`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHRenderedFlipbookFrame`
- 2 instance variables, 17 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<BLSHRenderedFlipbookFrame>" _wrappedFrame;
q _sourceFrameType;
```

## Properties

```
@property (T@"BLSHPresentationDateSpecifier",R,N) bls_specifier;
@property (TQ,R,N) presentationTime;
@property (TQ,R,N) frameId;
@property (Tf,R,N) apl;
@property (Tf,R,N) aplDimming;
@property (TQ,R,N) memoryUsage;
@property (T^{__IOSurface=},R,N) surface;
@property (T^{__IOSurface=},R,N) rawSurface;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) rawSurfaceFrame;
@property (TB,R,N,GisInverted) inverted;
@property (T@"NSUUID",R,N) bls_uuid;
@property (TB,R,N) lowPowerRendering;
@property (TQ,R,N) lowPowerRenderingPresentationTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHSourcedRenderedFlipbookFrame isInverted];
-[BLSHSourcedRenderedFlipbookFrame bls_loggingString];
-[BLSHSourcedRenderedFlipbookFrame bls_shortLoggingString];
-[BLSHSourcedRenderedFlipbookFrame surface];
-[BLSHSourcedRenderedFlipbookFrame frameId];
-[BLSHSourcedRenderedFlipbookFrame description];
-[BLSHSourcedRenderedFlipbookFrame lowPowerRenderingPresentationTime];
-[BLSHSourcedRenderedFlipbookFrame rawSurfaceFrame];
-[BLSHSourcedRenderedFlipbookFrame apl];
-[BLSHSourcedRenderedFlipbookFrame aplDimming];
-[BLSHSourcedRenderedFlipbookFrame lowPowerRendering];
-[BLSHSourcedRenderedFlipbookFrame memoryUsage];
-[BLSHSourcedRenderedFlipbookFrame presentationTime];
-[BLSHSourcedRenderedFlipbookFrame rawSurface];
-[BLSHSourcedRenderedFlipbookFrame bls_specifier];
-[BLSHSourcedRenderedFlipbookFrame bls_uuid];
-[BLSHSourcedRenderedFlipbookFrame initWithFrame:sourceFrameType:];
```
