# `FigCaptureIrisPreparedSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigXPCCoding`, `NSCopying`, `NSSecureCoding`
- 10 instance variables, 14 properties, 30 instance methods, 1 class methods

## Instance variables

```
q _settingsID;
I _processedOutputFormat;
I _rawOutputFormat;
I _outputWidth;
I _outputHeight;
I _bracketedImageCount;
i _qualityPrioritization;
i _HDRMode;
i _digitalFlashMode;
@"NSArray" _bravoConstituentImageDeliveryDeviceTypes;
```

## Properties

```
@property (Tq,N,V_settingsID) settingsID;
@property (TI,N,V_processedOutputFormat) processedOutputFormat;
@property (TI,N,V_rawOutputFormat) rawOutputFormat;
@property (TI,N,V_outputWidth) outputWidth;
@property (TI,N,V_outputHeight) outputHeight;
@property (TI,N,V_bracketedImageCount) bracketedImageCount;
@property (Ti,N,V_qualityPrioritization) qualityPrioritization;
@property (Ti,N,V_HDRMode) HDRMode;
@property (Ti,N,V_digitalFlashMode) digitalFlashMode;
@property (T@"NSArray",C,N,V_bravoConstituentImageDeliveryDeviceTypes) bravoConstituentImageDeliveryDeviceTypes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureIrisPreparedSettings supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureIrisPreparedSettings outputHeight];
-[FigCaptureIrisPreparedSettings setHDRMode:];
-[FigCaptureIrisPreparedSettings setBravoConstituentImageDeliveryDeviceTypes:];
-[FigCaptureIrisPreparedSettings digitalFlashMode];
-[FigCaptureIrisPreparedSettings init];
-[FigCaptureIrisPreparedSettings setRawOutputFormat:];
-[FigCaptureIrisPreparedSettings dealloc];
-[FigCaptureIrisPreparedSettings bravoConstituentImageDeliveryDeviceTypes];
-[FigCaptureIrisPreparedSettings settingsID];
-[FigCaptureIrisPreparedSettings qualityPrioritization];
-[FigCaptureIrisPreparedSettings setDigitalFlashMode:];
-[FigCaptureIrisPreparedSettings setQualityPrioritization:];
-[FigCaptureIrisPreparedSettings setOutputWidth:];
-[FigCaptureIrisPreparedSettings setOutputHeight:];
-[FigCaptureIrisPreparedSettings encodeWithCoder:];
-[FigCaptureIrisPreparedSettings setSettingsID:];
-[FigCaptureIrisPreparedSettings copyXPCEncoding];
-[FigCaptureIrisPreparedSettings description];
-[FigCaptureIrisPreparedSettings initWithXPCEncoding:];
-[FigCaptureIrisPreparedSettings initWithCoder:];
-[FigCaptureIrisPreparedSettings outputWidth];
-[FigCaptureIrisPreparedSettings rawOutputFormat];
-[FigCaptureIrisPreparedSettings copyWithZone:];
-[FigCaptureIrisPreparedSettings isEqual:];
-[FigCaptureIrisPreparedSettings HDRMode];
-[FigCaptureIrisPreparedSettings bracketedImageCount];
-[FigCaptureIrisPreparedSettings processedOutputFormat];
-[FigCaptureIrisPreparedSettings setBracketedImageCount:];
-[FigCaptureIrisPreparedSettings setProcessedOutputFormat:];
-[FigCaptureIrisPreparedSettings figCaptureStillImageSettingsRepresentation];
```
