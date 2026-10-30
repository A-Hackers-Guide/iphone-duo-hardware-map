# `BLSRenderedFlipbookFrame` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 13 properties, 15 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) presentationTime;
@property (TQ,R,N) frameId;
@property (Tf,R,N) apl;
@property (Tf,R,N) aplDimming;
@property (TQ,R,N) memoryUsage;
@property (T@"<BLSPresentationDateSpecifying>",R,N) bls_specifier;
@property (T^{__IOSurface=},R,N) surface;
@property (T^{__IOSurface=},R,N) rawSurface;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) rawSurfaceFrame;
@property (TB,R,N,GisInverted) inverted;
@property (T@"NSUUID",R,N) bls_uuid;
@property (TB,R,N) lowPowerRendering;
@property (TQ,R,N) lowPowerRenderingPresentationTime;
```

## Instance methods

```
-[BLSRenderedFlipbookFrame isInverted];
-[BLSRenderedFlipbookFrame bls_loggingString];
-[BLSRenderedFlipbookFrame bls_shortLoggingString];
-[BLSRenderedFlipbookFrame surface];
-[BLSRenderedFlipbookFrame frameId];
-[BLSRenderedFlipbookFrame lowPowerRenderingPresentationTime];
-[BLSRenderedFlipbookFrame rawSurfaceFrame];
-[BLSRenderedFlipbookFrame apl];
-[BLSRenderedFlipbookFrame aplDimming];
-[BLSRenderedFlipbookFrame lowPowerRendering];
-[BLSRenderedFlipbookFrame memoryUsage];
-[BLSRenderedFlipbookFrame presentationTime];
-[BLSRenderedFlipbookFrame rawSurface];
-[BLSRenderedFlipbookFrame bls_specifier];
-[BLSRenderedFlipbookFrame bls_uuid];
```
