# `OTSerializedPlistEscrowRecord`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _label;
@"NSData" _blob;
@"NSData" _metadata;
```

## Properties

```
@property (T@"NSString",C,N,V_label) label;
@property (T@"NSData",C,N,V_blob) blob;
@property (T@"NSData",C,N,V_metadata) metadata;
```

## Class methods

```
+[OTSerializedPlistEscrowRecord supportsSecureCoding];
```

## Instance methods

```
-[OTSerializedPlistEscrowRecord label];
-[OTSerializedPlistEscrowRecord setLabel:];
-[OTSerializedPlistEscrowRecord metadata];
-[OTSerializedPlistEscrowRecord encodeWithCoder:];
-[OTSerializedPlistEscrowRecord setMetadata:];
-[OTSerializedPlistEscrowRecord description];
-[OTSerializedPlistEscrowRecord initWithCoder:];
-[OTSerializedPlistEscrowRecord blob];
-[OTSerializedPlistEscrowRecord init:blob:metadata:];
-[OTSerializedPlistEscrowRecord setBlob:];
```
