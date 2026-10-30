# `MSCMSContentInfo`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MessageSecurityMessage`
- 3 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSData" _content;
@"<MSCMSMessage>" _embeddedContent;
@"MSOID" _contentType;
```

## Properties

```
@property (T@"NSData",&,V_content) content;
@property (T@"<MSCMSMessage>",&,V_embeddedContent) embeddedContent;
@property (T@"MSOID",&,V_contentType) contentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MSCMSContentInfo decodeMessageSecurityObject:options:error:];
```

## Instance methods

```
-[MSCMSContentInfo setContentType:];
-[MSCMSContentInfo encodeMessageSecurityObject:];
-[MSCMSContentInfo setContent:];
-[MSCMSContentInfo content];
-[MSCMSContentInfo contentType];
-[MSCMSContentInfo embeddedContent];
-[MSCMSContentInfo setEmbeddedContent:];
-[MSCMSContentInfo initWithDataContent:];
-[MSCMSContentInfo initWithEmbeddedContent:];
```
