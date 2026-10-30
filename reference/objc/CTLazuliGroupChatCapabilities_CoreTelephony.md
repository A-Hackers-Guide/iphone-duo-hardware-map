# `CTLazuliGroupChatCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _autoAcceptGroupChat;
B _supportsComposingIndicator;
@"NSNumber" _maxGroupSize;
```

## Properties

```
@property (TB,N,V_autoAcceptGroupChat) autoAcceptGroupChat;
@property (T@"NSNumber",&,N,V_maxGroupSize) maxGroupSize;
@property (TB,N,V_supportsComposingIndicator) supportsComposingIndicator;
```

## Class methods

```
+[CTLazuliGroupChatCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliGroupChatCapabilities encodeWithCoder:];
-[CTLazuliGroupChatCapabilities description];
-[CTLazuliGroupChatCapabilities initWithCoder:];
-[CTLazuliGroupChatCapabilities copyWithZone:];
-[CTLazuliGroupChatCapabilities isEqual:];
-[CTLazuliGroupChatCapabilities autoAcceptGroupChat];
-[CTLazuliGroupChatCapabilities initWithReflection:];
-[CTLazuliGroupChatCapabilities isEqualToCTLazuliGroupChatCapabilities:];
-[CTLazuliGroupChatCapabilities maxGroupSize];
-[CTLazuliGroupChatCapabilities setAutoAcceptGroupChat:];
-[CTLazuliGroupChatCapabilities setMaxGroupSize:];
-[CTLazuliGroupChatCapabilities setSupportsComposingIndicator:];
-[CTLazuliGroupChatCapabilities supportsComposingIndicator];
```
