# `BLSHPseudoFlipbookFrame`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHRenderedFlipbookFrame`
- 6 instance variables, 17 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _lowPowerRendering;
Q _presentationTime;
Q _frameId;
@"BLSHPresentationDateSpecifier" _bls_specifier;
Q _lowPowerRenderingPresentationTime;
Q _memoryUsage;
```

## Properties

```
@property (TQ,R,N,V_memoryUsage) memoryUsage;
@property (TB,N,V_lowPowerRendering) lowPowerRendering;
@property (TQ,N,V_lowPowerRenderingPresentationTime) lowPowerRenderingPresentationTime;
@property (T@"BLSHPresentationDateSpecifier",R,N,V_bls_specifier) bls_specifier;
@property (TQ,R,N,V_presentationTime) presentationTime;
@property (TQ,R,N,V_frameId) frameId;
@property (Tf,R,N) apl;
@property (Tf,R,N) aplDimming;
@property (T^{__IOSurface=},R,N) surface;
@property (T^{__IOSurface=},R,N) rawSurface;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) rawSurfaceFrame;
@property (TB,R,N,GisInverted) inverted;
@property (T@"NSUUID",R,N) bls_uuid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHPseudoFlipbookFrame isInverted];
-[BLSHPseudoFlipbookFrame bls_loggingString];
-[BLSHPseudoFlipbookFrame bls_shortLoggingString];
-[BLSHPseudoFlipbookFrame surface];
-[BLSHPseudoFlipbookFrame setLowPowerRenderingPresentationTime:];
-[BLSHPseudoFlipbookFrame frameId];
-[BLSHPseudoFlipbookFrame description];
-[BLSHPseudoFlipbookFrame lowPowerRenderingPresentationTime];
-[BLSHPseudoFlipbookFrame rawSurfaceFrame];
-[BLSHPseudoFlipbookFrame apl];
-[BLSHPseudoFlipbookFrame aplDimming];
-[BLSHPseudoFlipbookFrame lowPowerRendering];
-[BLSHPseudoFlipbookFrame memoryUsage];
-[BLSHPseudoFlipbookFrame presentationTime];
-[BLSHPseudoFlipbookFrame rawSurface];
-[BLSHPseudoFlipbookFrame setLowPowerRendering:];
-[BLSHPseudoFlipbookFrame bls_specifier];
-[BLSHPseudoFlipbookFrame bls_uuid];
-[BLSHPseudoFlipbookFrame initWithPresentationTime:frameId:specifier:memoryUsage:];
```
