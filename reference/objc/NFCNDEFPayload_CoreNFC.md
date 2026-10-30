# `NFCNDEFPayload`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 4 properties, 20 instance methods, 5 class methods

## Instance variables

```
Q _chunkSize;
C _typeNameFormat;
@"NSData" _type;
@"NSData" _identifier;
@"NSData" _payload;
```

## Properties

```
@property (TC,N,V_typeNameFormat) typeNameFormat;
@property (T@"NSData",C,N,V_type) type;
@property (T@"NSData",C,N,V_identifier) identifier;
@property (T@"NSData",C,N,V_payload) payload;
```

## Class methods

```
+[NFCNDEFPayload supportsSecureCoding];
+[NFCNDEFPayload wellKnownTypeURIPayloadWithURL:];
+[NFCNDEFPayload wellKnowTypeTextPayloadWithString:locale:];
+[NFCNDEFPayload wellKnownTypeTextPayloadWithString:locale:];
+[NFCNDEFPayload wellKnownTypeURIPayloadWithString:];
```

## Instance methods

```
-[NFCNDEFPayload identifier];
-[NFCNDEFPayload payload];
-[NFCNDEFPayload setPayload:];
-[NFCNDEFPayload setIdentifier:];
-[NFCNDEFPayload setType:];
-[NFCNDEFPayload type];
-[NFCNDEFPayload encodeWithCoder:];
-[NFCNDEFPayload description];
-[NFCNDEFPayload initWithCoder:];
-[NFCNDEFPayload asData];
-[NFCNDEFPayload chunkSize];
-[NFCNDEFPayload setChunkSize:];
-[NFCNDEFPayload setTypeNameFormat:];
-[NFCNDEFPayload typeNameFormat];
-[NFCNDEFPayload initWithFormat:type:identifier:payload:];
-[NFCNDEFPayload initWithFormat:type:identifier:payload:chunkSize:];
-[NFCNDEFPayload initWithFormatType:type:identifier:payload:chunkSize:];
-[NFCNDEFPayload resolveURIString:];
-[NFCNDEFPayload wellKnownTypeTextPayloadWithLocale:];
-[NFCNDEFPayload wellKnownTypeURIPayload];
```
