# `BWBracketSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 7 properties, 18 instance methods, 2 class methods

## Instance variables

```
i _bracketingMode;
B _providePreBracketedEV0;
B _lensStabilizationEnabledForClientBracket;
@"NSArray" _exposureValues;
@"NSArray" _manualExposureBracketedCaptureParams;
@"NSDictionary" _oisBracketedCaptureParams;
```

## Properties

```
@property (Ti,R,N,V_bracketingMode) bracketingMode;
@property (Ti,R,N) bracketFrameCount;
@property (TB,N,V_providePreBracketedEV0) providePreBracketedEV0;
@property (TB,N,V_lensStabilizationEnabledForClientBracket) lensStabilizationEnabledForClientBracket;
@property (T@"NSArray",C,N,V_exposureValues) exposureValues;
@property (T@"NSArray",C,N,V_manualExposureBracketedCaptureParams) manualExposureBracketedCaptureParams;
@property (T@"NSDictionary",C,N,V_oisBracketedCaptureParams) oisBracketedCaptureParams;
```

## Class methods

```
+[BWBracketSettings supportsSecureCoding];
+[BWBracketSettings bracketSettingsForBracketingMode:];
```

## Instance methods

```
-[BWBracketSettings dealloc];
-[BWBracketSettings setLensStabilizationEnabledForClientBracket:];
-[BWBracketSettings lensStabilizationEnabledForClientBracket];
-[BWBracketSettings encodeWithCoder:];
-[BWBracketSettings hash];
-[BWBracketSettings description];
-[BWBracketSettings initWithCoder:];
-[BWBracketSettings isEqual:];
-[BWBracketSettings bracketFrameCount];
-[BWBracketSettings bracketingMode];
-[BWBracketSettings exposureValues];
-[BWBracketSettings manualExposureBracketedCaptureParams];
-[BWBracketSettings oisBracketedCaptureParams];
-[BWBracketSettings providePreBracketedEV0];
-[BWBracketSettings setExposureValues:];
-[BWBracketSettings setManualExposureBracketedCaptureParams:];
-[BWBracketSettings setOisBracketedCaptureParams:];
-[BWBracketSettings setProvidePreBracketedEV0:];
```
