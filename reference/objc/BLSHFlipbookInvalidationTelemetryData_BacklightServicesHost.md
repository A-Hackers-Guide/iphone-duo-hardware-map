# `BLSHFlipbookInvalidationTelemetryData`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _didClearDateSpecifiers;
B _wasReset;
d _timestamp;
@"NSString" _reason;
@"NSString" _source;
@"BLSHFlipbookFramesHistogram" _invalidatedFramesHistogram;
@"NSArray" _environmentIdentifiers;
```

## Properties

```
@property (T@"NSString",R,N) blsh_analyticsEventName;
@property (T@"NSDictionary",R,N) blsh_analyticsPayload;
@property (Td,R,N,V_timestamp) timestamp;
@property (T@"NSString",R,N,V_reason) reason;
@property (T@"NSString",R,N,V_source) source;
@property (TB,R,N,V_didClearDateSpecifiers) didClearDateSpecifiers;
@property (TB,R,N,V_wasReset) wasReset;
@property (T@"BLSHFlipbookFramesHistogram",R,N,V_invalidatedFramesHistogram) invalidatedFramesHistogram;
@property (T@"NSArray",R,N,V_environmentIdentifiers) environmentIdentifiers;
```

## Instance methods

```
-[BLSHFlipbookInvalidationTelemetryData timestamp];
-[BLSHFlipbookInvalidationTelemetryData description];
-[BLSHFlipbookInvalidationTelemetryData reason];
-[BLSHFlipbookInvalidationTelemetryData source];
-[BLSHFlipbookInvalidationTelemetryData wasReset];
-[BLSHFlipbookInvalidationTelemetryData didClearDateSpecifiers];
-[BLSHFlipbookInvalidationTelemetryData environmentIdentifiers];
-[BLSHFlipbookInvalidationTelemetryData invalidatedFramesHistogram];
-[BLSHFlipbookInvalidationTelemetryData blsh_analyticsEventName];
-[BLSHFlipbookInvalidationTelemetryData blsh_analyticsPayload];
-[BLSHFlipbookInvalidationTelemetryData initWithTimestamp:reason:source:didClearDateSpecifiers:wasReset:invalidatedFramesHistogram:environmentIdentifiers:];
```
