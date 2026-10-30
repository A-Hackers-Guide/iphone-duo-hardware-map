# `CTLazuliDestination`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _isBot;
@"NSString" _uri;
@"NSString" _extractedUri;
@"CTLazuliAlternateIdentities" _identities;
@"NSString" _conversationID;
```

## Properties

```
@property (T@"NSString",C,N,V_extractedUri) extractedUri;
@property (TB,N,V_isBot) isBot;
@property (T@"CTLazuliAlternateIdentities",&,N,V_identities) identities;
@property (T@"NSString",C,N,V_uri) uri;
@property (T@"NSString",C,N,V_conversationID) conversationID;
```

## Class methods

```
+[CTLazuliDestination supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliDestination identities];
-[CTLazuliDestination uri];
-[CTLazuliDestination setConversationID:];
-[CTLazuliDestination conversationID];
-[CTLazuliDestination setUri:];
-[CTLazuliDestination setIdentities:];
-[CTLazuliDestination encodeWithCoder:];
-[CTLazuliDestination description];
-[CTLazuliDestination initWithCoder:];
-[CTLazuliDestination copyWithZone:];
-[CTLazuliDestination isEqual:];
-[CTLazuliDestination extractedUri];
-[CTLazuliDestination initWithReflection:];
-[CTLazuliDestination isBot];
-[CTLazuliDestination isEqualToCTLazuliDestination:];
-[CTLazuliDestination setExtractedUri:];
-[CTLazuliDestination setIsBot:];
```
