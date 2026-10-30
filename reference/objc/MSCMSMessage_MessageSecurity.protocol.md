# `MSCMSMessage` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MessageSecurityMessage`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"MSOID",R) type;
@property (T@"NSData",&,N) dataContent;
@property (T@"<MSCMSMessage>",&) embeddedContent;
@property (T@"MSOID",&) contentType;
```

## Instance methods

```
-[MSCMSMessage setContentType:];
-[MSCMSMessage contentType];
-[MSCMSMessage embeddedContent];
-[MSCMSMessage type];
-[MSCMSMessage setEmbeddedContent:];
-[MSCMSMessage dataContent];
-[MSCMSMessage setDataContent:];
```
