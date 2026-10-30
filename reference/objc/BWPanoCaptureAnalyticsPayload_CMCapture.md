# `BWPanoCaptureAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 14 instance variables, 18 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSString" _portType;
f _scalingFactor;
f _minAbsTranslationX;
f _maxAbsTranslationX;
f _aveAbsTranslationX;
f _minAbsTranslationY;
f _maxAbsTranslationY;
f _aveAbsTranslationY;
f _exposureTime;
f _minLuxValue;
f _maxLuxValue;
f _averageLuxValue;
f _focusDistance;
I _numFrames;
```

## Properties

```
@property (T@"NSString",&,N,V_portType) portType;
@property (Tf,N,V_scalingFactor) scalingFactor;
@property (Tf,N,V_minAbsTranslationX) minAbsTranslationX;
@property (Tf,N,V_maxAbsTranslationX) maxAbsTranslationX;
@property (Tf,N,V_aveAbsTranslationX) aveAbsTranslationX;
@property (Tf,N,V_minAbsTranslationY) minAbsTranslationY;
@property (Tf,N,V_maxAbsTranslationY) maxAbsTranslationY;
@property (Tf,N,V_aveAbsTranslationY) aveAbsTranslationY;
@property (Tf,N,V_exposureTime) exposureTime;
@property (Tf,N,V_minLuxValue) minLuxValue;
@property (Tf,N,V_maxLuxValue) maxLuxValue;
@property (Tf,N,V_averageLuxValue) averageLuxValue;
@property (Tf,N,V_focusDistance) focusDistance;
@property (TI,N,V_numFrames) numFrames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWPanoCaptureAnalyticsPayload focusDistance];
-[BWPanoCaptureAnalyticsPayload portType];
-[BWPanoCaptureAnalyticsPayload eventDictionary];
-[BWPanoCaptureAnalyticsPayload minLuxValue];
-[BWPanoCaptureAnalyticsPayload scalingFactor];
-[BWPanoCaptureAnalyticsPayload init];
-[BWPanoCaptureAnalyticsPayload dealloc];
-[BWPanoCaptureAnalyticsPayload reset];
-[BWPanoCaptureAnalyticsPayload setAverageLuxValue:];
-[BWPanoCaptureAnalyticsPayload exposureTime];
-[BWPanoCaptureAnalyticsPayload setPortType:];
-[BWPanoCaptureAnalyticsPayload setMinLuxValue:];
-[BWPanoCaptureAnalyticsPayload eventName];
-[BWPanoCaptureAnalyticsPayload setFocusDistance:];
-[BWPanoCaptureAnalyticsPayload setScalingFactor:];
-[BWPanoCaptureAnalyticsPayload setExposureTime:];
-[BWPanoCaptureAnalyticsPayload setMaxLuxValue:];
-[BWPanoCaptureAnalyticsPayload averageLuxValue];
-[BWPanoCaptureAnalyticsPayload maxLuxValue];
-[BWPanoCaptureAnalyticsPayload aveAbsTranslationX];
-[BWPanoCaptureAnalyticsPayload aveAbsTranslationY];
-[BWPanoCaptureAnalyticsPayload maxAbsTranslationX];
-[BWPanoCaptureAnalyticsPayload maxAbsTranslationY];
-[BWPanoCaptureAnalyticsPayload minAbsTranslationX];
-[BWPanoCaptureAnalyticsPayload minAbsTranslationY];
-[BWPanoCaptureAnalyticsPayload numFrames];
-[BWPanoCaptureAnalyticsPayload setAveAbsTranslationX:];
-[BWPanoCaptureAnalyticsPayload setAveAbsTranslationY:];
-[BWPanoCaptureAnalyticsPayload setMaxAbsTranslationX:];
-[BWPanoCaptureAnalyticsPayload setMaxAbsTranslationY:];
-[BWPanoCaptureAnalyticsPayload setMinAbsTranslationX:];
-[BWPanoCaptureAnalyticsPayload setMinAbsTranslationY:];
-[BWPanoCaptureAnalyticsPayload setNumFrames:];
```
