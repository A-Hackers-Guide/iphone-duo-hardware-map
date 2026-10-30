# `BWVideoStabilizationAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 13 instance variables, 12 properties, 23 instance methods, 0 class methods

## Instance variables

```
i _devicePosition;
i _height;
i _width;
f _startingUIZoom;
f _minUIZoom;
f _maxUIZoom;
I _averageLuxValue;
I _count;
[6@"NSString"] _portType;
[6i] _binningFactor;
[7f] _sigmaHistogram;
[6[7f]] _overscanHistogram;
@"NSString" _videoType;
```

## Properties

```
@property (Ti,N,V_devicePosition) devicePosition;
@property (Ti,N,V_height) height;
@property (Ti,N,V_width) width;
@property (Tf,N,V_startingUIZoom) startingUIZoom;
@property (Tf,N,V_minUIZoom) minUIZoom;
@property (Tf,N,V_maxUIZoom) maxUIZoom;
@property (T@"NSString",C,N,V_videoType) videoType;
@property (TI,N,V_averageLuxValue) averageLuxValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWVideoStabilizationAnalyticsPayload startingUIZoom];
-[BWVideoStabilizationAnalyticsPayload eventDictionary];
-[BWVideoStabilizationAnalyticsPayload init];
-[BWVideoStabilizationAnalyticsPayload dealloc];
-[BWVideoStabilizationAnalyticsPayload reset];
-[BWVideoStabilizationAnalyticsPayload setAverageLuxValue:];
-[BWVideoStabilizationAnalyticsPayload eventName];
-[BWVideoStabilizationAnalyticsPayload setHeight:];
-[BWVideoStabilizationAnalyticsPayload videoType];
-[BWVideoStabilizationAnalyticsPayload devicePosition];
-[BWVideoStabilizationAnalyticsPayload setVideoType:];
-[BWVideoStabilizationAnalyticsPayload setWidth:];
-[BWVideoStabilizationAnalyticsPayload width];
-[BWVideoStabilizationAnalyticsPayload height];
-[BWVideoStabilizationAnalyticsPayload setStartingUIZoom:];
-[BWVideoStabilizationAnalyticsPayload averageLuxValue];
-[BWVideoStabilizationAnalyticsPayload setDevicePosition:];
-[BWVideoStabilizationAnalyticsPayload maxUIZoom];
-[BWVideoStabilizationAnalyticsPayload minUIZoom];
-[BWVideoStabilizationAnalyticsPayload setMaxUIZoom:];
-[BWVideoStabilizationAnalyticsPayload setMinUIZoom:];
-[BWVideoStabilizationAnalyticsPayload setOverscanHistogram:BinningFactor:Histogram:];
-[BWVideoStabilizationAnalyticsPayload setSigmaHistogram:];
```
