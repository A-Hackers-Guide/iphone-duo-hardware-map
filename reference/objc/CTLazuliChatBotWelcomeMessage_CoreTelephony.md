# `CTLazuliChatBotWelcomeMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
q _contentType;
@ _content;
@"NSURL" _fallbackURL;
```

## Properties

```
@property (T@"NSString",R,N) prefilledText;
@property (T@"NSData",R,N) messagePayloadData;
@property (Tq,N,V_contentType) contentType;
@property (T@,&,N,V_content) content;
@property (T@"NSURL",&,N,V_fallbackURL) fallbackURL;
```

## Class methods

```
+[CTLazuliChatBotWelcomeMessage supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliChatBotWelcomeMessage setContentType:];
-[CTLazuliChatBotWelcomeMessage setContent:];
-[CTLazuliChatBotWelcomeMessage content];
-[CTLazuliChatBotWelcomeMessage contentType];
-[CTLazuliChatBotWelcomeMessage fallbackURL];
-[CTLazuliChatBotWelcomeMessage encodeWithCoder:];
-[CTLazuliChatBotWelcomeMessage description];
-[CTLazuliChatBotWelcomeMessage initWithCoder:];
-[CTLazuliChatBotWelcomeMessage copyWithZone:];
-[CTLazuliChatBotWelcomeMessage isEqual:];
-[CTLazuliChatBotWelcomeMessage setFallbackURL:];
-[CTLazuliChatBotWelcomeMessage initWithReflection:];
-[CTLazuliChatBotWelcomeMessage isEqualToCTLazuliChatBotWelcomeMessage:];
-[CTLazuliChatBotWelcomeMessage messagePayloadData];
-[CTLazuliChatBotWelcomeMessage prefilledText];
```
