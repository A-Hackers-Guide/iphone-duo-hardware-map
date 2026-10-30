# `CTLazuliMessageText`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _content;
@"CTLazuliChatBotSuggestedChipList" _chipList;
@"CTLazuliCustomMetaData" _metaData;
```

## Properties

```
@property (T@"CTLazuliChatBotSuggestedChipList",&,N,V_chipList) chipList;
@property (T@"NSString",C,N,V_content) content;
@property (T@"CTLazuliCustomMetaData",&,N,V_metaData) metaData;
```

## Class methods

```
+[CTLazuliMessageText supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageText setMetaData:];
-[CTLazuliMessageText setContent:];
-[CTLazuliMessageText metaData];
-[CTLazuliMessageText content];
-[CTLazuliMessageText encodeWithCoder:];
-[CTLazuliMessageText description];
-[CTLazuliMessageText initWithCoder:];
-[CTLazuliMessageText copyWithZone:];
-[CTLazuliMessageText isEqual:];
-[CTLazuliMessageText chipList];
-[CTLazuliMessageText initWithReflection:];
-[CTLazuliMessageText isEqualToCTLazuliMessageText:];
-[CTLazuliMessageText setChipList:];
```
