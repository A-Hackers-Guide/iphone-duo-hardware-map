# `CTBinarySMS`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _portAddressingScheme;
i _srcPort;
i _dstPort;
i _smsType;
@"NSData" _payload;
@"NSString" _destinationAddress;
@"NSString" _smscAddress;
@"CTXPCServiceSubscriptionContext" _context;
```

## Properties

```
@property (Ti,N,V_portAddressingScheme) portAddressingScheme;
@property (Ti,N,V_srcPort) srcPort;
@property (Ti,N,V_dstPort) dstPort;
@property (T@"NSData",C,N,V_payload) payload;
@property (T@"NSString",C,N,V_destinationAddress) destinationAddress;
@property (T@"NSString",C,N,V_smscAddress) smscAddress;
@property (T@"CTXPCServiceSubscriptionContext",C,N,V_context) context;
@property (Ti,N,V_smsType) smsType;
```

## Instance methods

```
-[CTBinarySMS init];
-[CTBinarySMS payload];
-[CTBinarySMS setPayload:];
-[CTBinarySMS setContext:];
-[CTBinarySMS isValid];
-[CTBinarySMS context];
-[CTBinarySMS dstPort];
-[CTBinarySMS setSmscAddress:];
-[CTBinarySMS smsType];
-[CTBinarySMS srcPort];
-[CTBinarySMS destinationAddress];
-[CTBinarySMS portAddressingScheme];
-[CTBinarySMS setDestinationAddress:];
-[CTBinarySMS setDstPort:];
-[CTBinarySMS setPortAddressingScheme:];
-[CTBinarySMS setSmsType:];
-[CTBinarySMS setSrcPort:];
-[CTBinarySMS smscAddress];
```
