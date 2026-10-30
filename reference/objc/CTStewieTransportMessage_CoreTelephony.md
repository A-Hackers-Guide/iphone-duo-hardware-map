# `CTStewieTransportMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSString" _msgId;
@"NSData" _data;
@"NSDictionary" _metadata;
```

## Properties

```
@property (T@"NSString",&,N,V_msgId) msgId;
@property (T@"NSData",&,N,V_data) data;
@property (T@"NSDictionary",&,N,V_metadata) metadata;
```

## Class methods

```
+[CTStewieTransportMessage supportsSecureCoding];
+[CTStewieTransportMessage allowedSetOfClasses];
```

## Instance methods

```
-[CTStewieTransportMessage init];
-[CTStewieTransportMessage data];
-[CTStewieTransportMessage metadata];
-[CTStewieTransportMessage setData:];
-[CTStewieTransportMessage encodeWithCoder:];
-[CTStewieTransportMessage setMetadata:];
-[CTStewieTransportMessage description];
-[CTStewieTransportMessage initWithCoder:];
-[CTStewieTransportMessage copyWithZone:];
-[CTStewieTransportMessage isEqual:];
-[CTStewieTransportMessage initWithMsgId:];
-[CTStewieTransportMessage isEqualToTransportMessage:];
-[CTStewieTransportMessage msgId];
-[CTStewieTransportMessage setMsgId:];
```
