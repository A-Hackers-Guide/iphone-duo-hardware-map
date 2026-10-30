# `MSCMSCompressedData`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSMessage`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"MSOID" type;
? dataContent;
@"<MSCMSMessage>" embeddedContent;
@"MSOID" contentType;
```

## Properties

```
@property (T@"MSOID",N,&,Vtype) type;
@property (T@"NSData",N,C) dataContent;
@property (T@"<MSCMSMessage>",N,&,VembeddedContent) embeddedContent;
@property (T@"MSOID",N,&,VcontentType) contentType;
```

## Class methods

```
+[MSCMSCompressedData decodeMessageSecurityObject:options:error:];
```

## Instance methods

```
-[MSCMSCompressedData setContentType:];
-[MSCMSCompressedData encodeMessageSecurityObject:];
-[MSCMSCompressedData init];
-[MSCMSCompressedData contentType];
-[MSCMSCompressedData embeddedContent];
-[MSCMSCompressedData setType:];
-[MSCMSCompressedData type];
-[MSCMSCompressedData setEmbeddedContent:];
-[MSCMSCompressedData dataContent];
-[MSCMSCompressedData setDataContent:];
-[MSCMSCompressedData initWithDataContent:error:];
-[MSCMSCompressedData initWithEmbeddedContent:error:];
```
