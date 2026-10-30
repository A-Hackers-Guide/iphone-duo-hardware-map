# `BWIOSurfaceCompressionStatisticsAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 10 instance variables, 14 properties, 23 instance methods, 0 class methods

## Instance variables

```
f _averageRatio;
f _minRatio;
f _maxRatio;
f _standardDeviation;
i _compressionType;
I _bufferHeight;
I _numberOfSamples;
Q _totalCompressedSize;
Q _totalUncompressedSize;
i _nodeType;
```

## Properties

```
@property (Tf,N,V_averageRatio) averageRatio;
@property (Tf,N,V_minRatio) minRatio;
@property (Tf,N,V_maxRatio) maxRatio;
@property (Tf,N,V_standardDeviation) standardDeviation;
@property (Ti,N,V_compressionType) compressionType;
@property (TI,N,V_bufferHeight) bufferHeight;
@property (TI,N,V_numberOfSamples) numberOfSamples;
@property (TQ,N,V_totalCompressedSize) totalCompressedSize;
@property (TQ,N,V_totalUncompressedSize) totalUncompressedSize;
@property (Ti,N,V_nodeType) nodeType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload compressionType];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setCompressionType:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload eventDictionary];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload reset];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload numberOfSamples];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload eventName];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload standardDeviation];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload nodeType];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setNodeType:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setStandardDeviation:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload averageRatio];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload bufferHeight];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload maxRatio];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload minRatio];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setAverageRatio:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setBufferHeight:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setMaxRatio:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setMinRatio:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setNumberOfSamples:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setTotalCompressedSize:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload setTotalUncompressedSize:];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload totalCompressedSize];
-[BWIOSurfaceCompressionStatisticsAnalyticsPayload totalUncompressedSize];
```
