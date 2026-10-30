# `TBFetchRequestDescriptor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"PBCodable",R,N) remoteRequest;
@property (T#,R,N) remoteRequestClass;
@property (TQ,R,N) type;
@property (T@"TBLocalFetchRequestDescriptor",R,N) localFetchDescriptor;
@property (T@"TBLocalFetchRequestDescriptor",?,R,N) preferLocalFetchDescriptor;
@property (T@"NSSet",?,R,N) tileItems;
```

## Instance methods

```
-[TBFetchRequestDescriptor type];
-[TBFetchRequestDescriptor remoteRequest];
-[TBFetchRequestDescriptor localFetchDescriptor];
-[TBFetchRequestDescriptor remoteRequestClass];
-[TBFetchRequestDescriptor preferLocalFetchDescriptor];
-[TBFetchRequestDescriptor tileItems];
```
