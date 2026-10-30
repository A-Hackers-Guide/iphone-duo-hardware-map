# `BWFrameStatisticsByPortType`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`, `NSSecureCoding`
- 6 instance variables, 3 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _portTypes;
@"NSDictionary" _portTypeToFrameStatistics;
^{?={?=qiIq}f{CGRect={CGPoint=dd}{CGSize=dd}}IIIIffdIIIfffdfIIIIBBBiBfiBiiiiiiiiiififii@q@IfiBBSSSSSSSSSII} _frameStatisticsStoragesForPortTypes;
Q _frameCount;
f _adrcExposureRealizedGain;
B _autoFocusRecommendedPrimaryPortTypeEnabled;
```

## Properties

```
@property (T@"NSArray",R,N) portTypes;
@property (TQ,R,N) frameCount;
@property (Tf,R,N) adrcExposureRealizedGain;
```

## Class methods

```
+[BWFrameStatisticsByPortType supportsSecureCoding];
+[BWFrameStatisticsByPortType initialize];
```

## Instance methods

```
-[BWFrameStatisticsByPortType portTypes];
-[BWFrameStatisticsByPortType frameCount];
-[BWFrameStatisticsByPortType init];
-[BWFrameStatisticsByPortType dealloc];
-[BWFrameStatisticsByPortType reset];
-[BWFrameStatisticsByPortType updateWithFrameMetadata:updateFocusDistance:];
-[BWFrameStatisticsByPortType objectForKeyedSubscript:];
-[BWFrameStatisticsByPortType countByEnumeratingWithState:objects:count:];
-[BWFrameStatisticsByPortType encodeWithCoder:];
-[BWFrameStatisticsByPortType copyForPortType:];
-[BWFrameStatisticsByPortType hash];
-[BWFrameStatisticsByPortType copyTo:];
-[BWFrameStatisticsByPortType initWithPortTypes:];
-[BWFrameStatisticsByPortType description];
-[BWFrameStatisticsByPortType initWithCoder:];
-[BWFrameStatisticsByPortType _setFrameCount:];
-[BWFrameStatisticsByPortType initWithPortTypes:defaultFNumberByPortType:autoFocusRecommendedPrimaryPortTypeEnabled:];
-[BWFrameStatisticsByPortType adrcExposureRealizedGain];
-[BWFrameStatisticsByPortType isEqual:];
```
