# `WiFiAwarePKBootstrappingRecordIngestionResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
B _ingested;
q _rejectionReason;
```

## Properties

```
@property (TB,N,V_ingested) ingested;
@property (Tq,N,V_rejectionReason) rejectionReason;
```

## Class methods

```
+[WiFiAwarePKBootstrappingRecordIngestionResult supportsSecureCoding];
+[WiFiAwarePKBootstrappingRecordIngestionResult stringForRejectionReason:];
```

## Instance methods

```
-[WiFiAwarePKBootstrappingRecordIngestionResult encodeWithCoder:];
-[WiFiAwarePKBootstrappingRecordIngestionResult description];
-[WiFiAwarePKBootstrappingRecordIngestionResult initWithCoder:];
-[WiFiAwarePKBootstrappingRecordIngestionResult rejectionReason];
-[WiFiAwarePKBootstrappingRecordIngestionResult setRejectionReason:];
-[WiFiAwarePKBootstrappingRecordIngestionResult ingested];
-[WiFiAwarePKBootstrappingRecordIngestionResult initWithIngested:rejectionReason:];
-[WiFiAwarePKBootstrappingRecordIngestionResult setIngested:];
```
