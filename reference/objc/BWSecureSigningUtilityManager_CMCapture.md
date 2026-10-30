# `BWSecureSigningUtilityManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _timestampQueue;
@"NSData" _lowerBoundTimestampData;
@"NSData" _clientProvidedHash;
@"NSData" _sealingManifestData;
@"NSData" _secureBootTicketData;
@"NSData" _sealingManifestUniqueIDData;
@"NSData" _sensorCertificateUniqueIDData;
@"NSData" _sensorCertificateData;
@"NSData" _trustObjectData;
@"NSData" _trustObjectDigestData;
@"NSMutableArray" _clientProvidedHashHistory;
@"NSObject<OS_dispatch_source>" _refreshTimer;
@"<BWSecureSigningUtilityManagerDelegate>" _delegate;
B _fdrUnavailable;
@"NSError" _sealingManifestError;
@"NSError" _sensorCertificateError;
@"NSError" _trustObjectError;
@"NSError" _secureBootTicketError;
```

## Properties

```
@property (T@"<BWSecureSigningUtilityManagerDelegate>",W,N) delegate;
@property (T@"NSData",R,N) clientProvidedHash;
@property (T@"NSData",R,N) lowerBoundTimestampData;
@property (T@"NSData",R,N) sealingManifestUniqueIDData;
@property (T@"NSData",R,N) sealingManifestData;
@property (T@"NSData",R,N) sensorCertificateUniqueIDData;
@property (T@"NSData",R,N) sensorCertificateData;
@property (T@"NSData",R,N) trustObjectData;
@property (T@"NSData",R,N) trustObjectDigestData;
@property (T@"NSData",R,N) secureBootTicketData;
```

## Class methods

```
+[BWSecureSigningUtilityManager sharedManager];
```

## Instance methods

```
-[BWSecureSigningUtilityManager init];
-[BWSecureSigningUtilityManager dealloc];
-[BWSecureSigningUtilityManager setDelegate:];
-[BWSecureSigningUtilityManager delegate];
-[BWSecureSigningUtilityManager trustObjectData];
-[BWSecureSigningUtilityManager clientProvidedHash];
-[BWSecureSigningUtilityManager clientProvidedSensorPayloadInfoForClientProvidedHash:];
-[BWSecureSigningUtilityManager firstSecureSigningStaticDataFailure:];
-[BWSecureSigningUtilityManager isSecureSigningCertificateAvailableWithTimeout:];
-[BWSecureSigningUtilityManager issueSecureSigningClientCertificateOnQueue:completion:];
-[BWSecureSigningUtilityManager lowerBoundTimestampData];
-[BWSecureSigningUtilityManager lowerBoundTimestampDataForClientProvidedHash:];
-[BWSecureSigningUtilityManager sealingManifestData];
-[BWSecureSigningUtilityManager sealingManifestUniqueIDData];
-[BWSecureSigningUtilityManager secureBootTicketData];
-[BWSecureSigningUtilityManager sensorCertificateData];
-[BWSecureSigningUtilityManager sensorCertificateUniqueIDData];
-[BWSecureSigningUtilityManager trustObjectDigestData];
```
