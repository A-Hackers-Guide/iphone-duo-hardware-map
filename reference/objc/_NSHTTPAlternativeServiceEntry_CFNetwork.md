# `_NSHTTPAlternativeServiceEntry`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _host;
@"NSString" _alternateHost;
q _port;
q _alternatePort;
@"NSString" _partition;
@"NSDate" _expirationDate;
q _serviceType;
```

## Properties

```
@property (T@"NSString",&,N,V_host) host;
@property (T@"NSString",&,N,V_alternateHost) alternateHost;
@property (Tq,N,V_port) port;
@property (Tq,N,V_alternatePort) alternatePort;
@property (T@"NSString",&,N,V_partition) partition;
@property (T@"NSDate",&,N,V_expirationDate) expirationDate;
@property (Tq,N,V_serviceType) serviceType;
```

## Instance methods

```
-[_NSHTTPAlternativeServiceEntry setHost:];
-[_NSHTTPAlternativeServiceEntry setPort:];
-[_NSHTTPAlternativeServiceEntry setAlternatePort:];
-[_NSHTTPAlternativeServiceEntry expirationDate];
-[_NSHTTPAlternativeServiceEntry init];
-[_NSHTTPAlternativeServiceEntry alternatePort];
-[_NSHTTPAlternativeServiceEntry partition];
-[_NSHTTPAlternativeServiceEntry setAlternateHost:];
-[_NSHTTPAlternativeServiceEntry port];
-[_NSHTTPAlternativeServiceEntry hash];
-[_NSHTTPAlternativeServiceEntry description];
-[_NSHTTPAlternativeServiceEntry setExpirationDate:];
-[_NSHTTPAlternativeServiceEntry copyWithZone:];
-[_NSHTTPAlternativeServiceEntry setServiceType:];
-[_NSHTTPAlternativeServiceEntry setPartition:];
-[_NSHTTPAlternativeServiceEntry isEqual:];
-[_NSHTTPAlternativeServiceEntry host];
-[_NSHTTPAlternativeServiceEntry serviceType];
-[_NSHTTPAlternativeServiceEntry alternateHost];
```
