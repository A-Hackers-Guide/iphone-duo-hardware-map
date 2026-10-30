# `SRFaceMetrics`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `SRSampling`, `NSCopying`, `NSSecureCoding`
- 6 instance variables, 12 properties, 27 instance methods, 3 class methods

## Instance variables

```
@"NSString" _version;
@"NSString" _sessionIdentifier;
Q _context;
@"ARFaceAnchor" _faceAnchor;
@"NSMutableArray" _mutableWholeFaceExpressions;
@"NSMutableArray" _mutablePartialFaceExpressions;
```

## Properties

```
@property (T@"NSString",C,N,V_version) version;
@property (T@"NSString",C,N,V_sessionIdentifier) sessionIdentifier;
@property (TQ,N,V_context) context;
@property (T@"ARFaceAnchor",C,N,V_faceAnchor) faceAnchor;
@property (T@"NSMutableArray",&,N,V_mutableWholeFaceExpressions) mutableWholeFaceExpressions;
@property (T@"NSMutableArray",&,N,V_mutablePartialFaceExpressions) mutablePartialFaceExpressions;
@property (T@"NSArray",R,C,N) wholeFaceExpressions;
@property (T@"NSArray",R,C,N) partialFaceExpressions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRFaceMetrics supportsSecureCoding];
+[SRFaceMetrics initialize];
+[SRFaceMetrics new];
```

## Instance methods

```
-[SRFaceMetrics sessionIdentifier];
-[SRFaceMetrics init];
-[SRFaceMetrics dealloc];
-[SRFaceMetrics setSessionIdentifier:];
-[SRFaceMetrics version];
-[SRFaceMetrics setContext:];
-[SRFaceMetrics encodeWithCoder:];
-[SRFaceMetrics hash];
-[SRFaceMetrics description];
-[SRFaceMetrics initWithCoder:];
-[SRFaceMetrics setVersion:];
-[SRFaceMetrics copyWithZone:];
-[SRFaceMetrics context];
-[SRFaceMetrics isEqual:];
-[SRFaceMetrics binarySampleRepresentation];
-[SRFaceMetrics initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRFaceMetrics setMutableWholeFaceExpressions:];
-[SRFaceMetrics faceAnchor];
-[SRFaceMetrics initWithHAFacialMetricsPacket:];
-[SRFaceMetrics initWithVersion:sessionIdentifier:context:faceAnchor:wholeFaceExpressions:partialFaceExpressions:];
-[SRFaceMetrics initWithVersion:sessionIdentifier:context:faceIdentifier:trackingData:wholeFaceExpressions:partialFaceExpressions:];
-[SRFaceMetrics mutablePartialFaceExpressions];
-[SRFaceMetrics mutableWholeFaceExpressions];
-[SRFaceMetrics partialFaceExpressions];
-[SRFaceMetrics setFaceAnchor:];
-[SRFaceMetrics setMutablePartialFaceExpressions:];
-[SRFaceMetrics wholeFaceExpressions];
```
