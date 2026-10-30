# `NFCNDEFMessage`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 2 properties, 12 instance methods, 4 class methods

## Instance variables

```
@"NSArray" _records;
```

## Properties

```
@property (T@"NSArray",C,N,V_records) records;
@property (TQ,R,N) length;
```

## Class methods

```
+[NFCNDEFMessage supportsSecureCoding];
+[NFCNDEFMessage _getPayloadsFromNDEFRecords:];
+[NFCNDEFMessage _validateRecords:fromOriginal:];
+[NFCNDEFMessage ndefMessageWithData:];
```

## Instance methods

```
-[NFCNDEFMessage records];
-[NFCNDEFMessage length];
-[NFCNDEFMessage encodeWithCoder:];
-[NFCNDEFMessage setRecords:];
-[NFCNDEFMessage _initWithRecords:];
-[NFCNDEFMessage description];
-[NFCNDEFMessage initWithCoder:];
-[NFCNDEFMessage asData];
-[NFCNDEFMessage _getURLsFromNDEFMessage:];
-[NFCNDEFMessage initWithEmptyNdefMessage];
-[NFCNDEFMessage initWithNDEFRecords:];
-[NFCNDEFMessage initWithNFNdefMessage:];
```
