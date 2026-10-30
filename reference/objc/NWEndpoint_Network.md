# `NWEndpoint`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`, `NSSecureCoding`, `NSCopying`
- 1 instance variables, 7 properties, 23 instance methods, 7 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" _internalEndpoint;
```

## Properties

```
@property (T@"NSObject<OS_nw_endpoint>",&,N,V_internalEndpoint) internalEndpoint;
@property (T@"NWInterface",&,N) interface;
@property (T@"NSString",R,N) parentEndpointDomain;
@property (T@"NSString",R,C,N) privateDescription;
@property (TS,N) alternatePort;
@property (Tq,N) remoteInterfaceType;
@property (T@"NSData",&,N) txtRecord;
```

## Class methods

```
+[NWEndpoint endpointType];
+[NWEndpoint supportsSecureCoding];
+[NWEndpoint copyClassForEndpointType:];
+[NWEndpoint endpointWithCEndpoint:];
+[NWEndpoint endpointWithProtocolBufferData:];
+[NWEndpoint endpointWithInternalEndpoint:];
+[NWEndpoint supportsResolverCallback];
```

## Instance methods

```
-[NWEndpoint setAlternatePort:];
-[NWEndpoint setRemoteInterfaceType:];
-[NWEndpoint createProtocolBufferObject];
-[NWEndpoint remoteInterfaceType];
-[NWEndpoint setInternalEndpoint:];
-[NWEndpoint alternatePort];
-[NWEndpoint parentEndpointDomain];
-[NWEndpoint txtRecord];
-[NWEndpoint internalEndpoint];
-[NWEndpoint setInterface:];
-[NWEndpoint encodedData];
-[NWEndpoint setTxtRecord:];
-[NWEndpoint initWithEndpoint:];
-[NWEndpoint privateDescription];
-[NWEndpoint descriptionWithIndent:showFullContent:];
-[NWEndpoint interface];
-[NWEndpoint copyCEndpoint];
-[NWEndpoint encodeWithCoder:];
-[NWEndpoint hash];
-[NWEndpoint description];
-[NWEndpoint initWithCoder:];
-[NWEndpoint copyWithZone:];
-[NWEndpoint isEqual:];
```
