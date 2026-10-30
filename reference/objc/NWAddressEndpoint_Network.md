# `NWAddressEndpoint`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWHostEndpoint`
- 0 instance variables, 5 properties, 7 instance methods, 3 class methods

## Properties

```
@property (T@"NSString",R,N) addressString;
@property (T@"NSString",R,N) addressStringNoPort;
@property (T@"NSData",R,N) addressData;
@property (Tr^{sockaddr=CC[14c]},R,N) address;
@property (TQ,R,N) addressFamily;
```

## Class methods

```
+[NWAddressEndpoint endpointType];
+[NWAddressEndpoint endpointWithHostname:port:];
+[NWAddressEndpoint endpointWithAddress:];
```

## Instance methods

```
-[NWAddressEndpoint addressData];
-[NWAddressEndpoint addressString];
-[NWAddressEndpoint address];
-[NWAddressEndpoint addressFamily];
-[NWAddressEndpoint descriptionWithIndent:showFullContent:];
-[NWAddressEndpoint addressStringNoPort];
-[NWAddressEndpoint ethernetAddress];
```
