# `CTLazuliChatCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _autoAcceptChat;
@"NSNumber" _max1ToManyRecipients;
@"NSNumber" _revokeTimer;
@"NSNumber" _maxSize;
@"NSString" _spamReportingUri;
```

## Properties

```
@property (TB,N,V_autoAcceptChat) autoAcceptChat;
@property (T@"NSNumber",&,N,V_max1ToManyRecipients) max1ToManyRecipients;
@property (T@"NSNumber",&,N,V_revokeTimer) revokeTimer;
@property (T@"NSNumber",&,N,V_maxSize) maxSize;
@property (T@"NSString",&,N,V_spamReportingUri) spamReportingUri;
```

## Class methods

```
+[CTLazuliChatCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliChatCapabilities maxSize];
-[CTLazuliChatCapabilities encodeWithCoder:];
-[CTLazuliChatCapabilities setMaxSize:];
-[CTLazuliChatCapabilities description];
-[CTLazuliChatCapabilities initWithCoder:];
-[CTLazuliChatCapabilities copyWithZone:];
-[CTLazuliChatCapabilities isEqual:];
-[CTLazuliChatCapabilities setRevokeTimer:];
-[CTLazuliChatCapabilities autoAcceptChat];
-[CTLazuliChatCapabilities initWithReflection:];
-[CTLazuliChatCapabilities isEqualToCTLazuliChatCapabilities:];
-[CTLazuliChatCapabilities max1ToManyRecipients];
-[CTLazuliChatCapabilities revokeTimer];
-[CTLazuliChatCapabilities setAutoAcceptChat:];
-[CTLazuliChatCapabilities setMax1ToManyRecipients:];
-[CTLazuliChatCapabilities setSpamReportingUri:];
-[CTLazuliChatCapabilities spamReportingUri];
```
