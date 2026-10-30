# `WiFiAwarePublishServiceSpecificInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSData" _blob;
@"NSData" _txtRecordData;
@"NSString" _instanceName;
```

## Properties

```
@property (T@"NSData",C,N,V_blob) blob;
@property (T@"NSData",C,N,V_txtRecordData) txtRecordData;
@property (T@"NSString",C,N,V_instanceName) instanceName;
```

## Class methods

```
+[WiFiAwarePublishServiceSpecificInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePublishServiceSpecificInfo init];
-[WiFiAwarePublishServiceSpecificInfo encodeWithCoder:];
-[WiFiAwarePublishServiceSpecificInfo description];
-[WiFiAwarePublishServiceSpecificInfo initWithCoder:];
-[WiFiAwarePublishServiceSpecificInfo copyWithZone:];
-[WiFiAwarePublishServiceSpecificInfo isEqual:];
-[WiFiAwarePublishServiceSpecificInfo instanceName];
-[WiFiAwarePublishServiceSpecificInfo blob];
-[WiFiAwarePublishServiceSpecificInfo setBlob:];
-[WiFiAwarePublishServiceSpecificInfo setInstanceName:];
-[WiFiAwarePublishServiceSpecificInfo setTxtRecordData:];
-[WiFiAwarePublishServiceSpecificInfo txtRecordData];
-[WiFiAwarePublishServiceSpecificInfo blobEquals:];
-[WiFiAwarePublishServiceSpecificInfo instanceNameEquals:];
-[WiFiAwarePublishServiceSpecificInfo txtRecordEquals:];
```
