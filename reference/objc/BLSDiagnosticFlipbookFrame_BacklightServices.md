# `BLSDiagnosticFlipbookFrame`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSRenderedFlipbookFrame`, `NSSecureCoding`, `BSXPCCoding`
- 12 instance variables, 19 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"BLSDiagnosticPresentationDateSpecifier" _specifier;
B _inverted;
B _lowPowerRendering;
f _apl;
f _aplDimming;
Q _presentationTime;
Q _frameId;
Q _memoryUsage;
Q _lowPowerRenderingPresentationTime;
@"NSUUID" _uuid;
@"<BLSDiagnosticFlipbookFrameSurfaceProvider>" _surfaceProvider;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rawSurfaceFrame;
```

## Properties

```
@property (T@"<BLSDiagnosticFlipbookFrameSurfaceProvider>",W,V_surfaceProvider) surfaceProvider;
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (TQ,R,N,V_presentationTime) presentationTime;
@property (TQ,R,N,V_frameId) frameId;
@property (Tf,R,N,V_apl) apl;
@property (Tf,R,N,V_aplDimming) aplDimming;
@property (TQ,R,N,V_memoryUsage) memoryUsage;
@property (T@"<BLSPresentationDateSpecifying>",R,N) bls_specifier;
@property (T^{__IOSurface=},R,N) surface;
@property (T^{__IOSurface=},R,N) rawSurface;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rawSurfaceFrame) rawSurfaceFrame;
@property (TB,R,N,GisInverted,V_inverted) inverted;
@property (T@"NSUUID",R,N) bls_uuid;
@property (TB,R,N,V_lowPowerRendering) lowPowerRendering;
@property (TQ,R,N,V_lowPowerRenderingPresentationTime) lowPowerRenderingPresentationTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSDiagnosticFlipbookFrame supportsSecureCoding];
+[BLSDiagnosticFlipbookFrame createWithFrame:];
```

## Instance methods

```
-[BLSDiagnosticFlipbookFrame isInverted];
-[BLSDiagnosticFlipbookFrame bls_loggingString];
-[BLSDiagnosticFlipbookFrame bls_shortLoggingString];
-[BLSDiagnosticFlipbookFrame surface];
-[BLSDiagnosticFlipbookFrame uuid];
-[BLSDiagnosticFlipbookFrame initWithXPCDictionary:];
-[BLSDiagnosticFlipbookFrame frameId];
-[BLSDiagnosticFlipbookFrame encodeWithXPCDictionary:];
-[BLSDiagnosticFlipbookFrame encodeWithCoder:];
-[BLSDiagnosticFlipbookFrame hash];
-[BLSDiagnosticFlipbookFrame description];
-[BLSDiagnosticFlipbookFrame initWithCoder:];
-[BLSDiagnosticFlipbookFrame isEqual:];
-[BLSDiagnosticFlipbookFrame initWithFrame:];
-[BLSDiagnosticFlipbookFrame lowPowerRenderingPresentationTime];
-[BLSDiagnosticFlipbookFrame rawSurfaceFrame];
-[BLSDiagnosticFlipbookFrame apl];
-[BLSDiagnosticFlipbookFrame aplDimming];
-[BLSDiagnosticFlipbookFrame lowPowerRendering];
-[BLSDiagnosticFlipbookFrame memoryUsage];
-[BLSDiagnosticFlipbookFrame presentationTime];
-[BLSDiagnosticFlipbookFrame rawSurface];
-[BLSDiagnosticFlipbookFrame surfaceProvider];
-[BLSDiagnosticFlipbookFrame setSurfaceProvider:];
-[BLSDiagnosticFlipbookFrame bls_specifier];
-[BLSDiagnosticFlipbookFrame bls_uuid];
-[BLSDiagnosticFlipbookFrame initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:lowPowerRendering:lowPowerRenderingPresentationTime:];
```
