# `THPreferredNetworkEntry`

- Image: [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](../userland/System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _networkName;
@"NSData" _extendedPANID;
@"NSData" _ipv4Signature;
@"NSData" _ipv6Signature;
@"NSString" _wifiSSID;
@"THCredentials" _credentialsRecord;
@"NSDate" _creationDate;
@"NSDate" _lastModificationDate;
```

## Properties

```
@property (T@"NSString",R,N,V_networkName) networkName;
@property (T@"NSData",R,N,V_extendedPANID) extendedPANID;
@property (T@"NSData",R,N,V_ipv4Signature) ipv4Signature;
@property (T@"NSData",R,N,V_ipv6Signature) ipv6Signature;
@property (T@"NSString",R,N,V_wifiSSID) wifiSSID;
@property (T@"THCredentials",R,N,V_credentialsRecord) credentialsRecord;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSDate",R,N,V_lastModificationDate) lastModificationDate;
```

## Class methods

```
+[THPreferredNetworkEntry supportsSecureCoding];
```

## Instance methods

```
-[THPreferredNetworkEntry networkName];
-[THPreferredNetworkEntry creationDate];
-[THPreferredNetworkEntry encodeWithCoder:];
-[THPreferredNetworkEntry initWithCoder:];
-[THPreferredNetworkEntry extendedPANID];
-[THPreferredNetworkEntry lastModificationDate];
-[THPreferredNetworkEntry wifiSSID];
-[THPreferredNetworkEntry ipv4Signature];
-[THPreferredNetworkEntry ipv6Signature];
-[THPreferredNetworkEntry credentialsRecord];
-[THPreferredNetworkEntry initPrefEntry:extendedPANID:ipv4Signature:ipv6Signature:wifiSSID:creationDate:lastModificationDate:credentialsRecord:];
```
