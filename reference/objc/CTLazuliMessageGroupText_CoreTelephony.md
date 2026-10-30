# `CTLazuliMessageGroupText`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"CTLazuliGroupChatInformation" _chatInformation;
@"NSString" _content;
@"CTLazuliCustomMetaData" _metaData;
```

## Properties

```
@property (T@"CTLazuliGroupChatInformation",&,N,V_chatInformation) chatInformation;
@property (T@"NSString",&,N,V_content) content;
@property (T@"CTLazuliCustomMetaData",&,N,V_metaData) metaData;
```

## Class methods

```
+[CTLazuliMessageGroupText supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageGroupText setMetaData:];
-[CTLazuliMessageGroupText setContent:];
-[CTLazuliMessageGroupText metaData];
-[CTLazuliMessageGroupText content];
-[CTLazuliMessageGroupText encodeWithCoder:];
-[CTLazuliMessageGroupText description];
-[CTLazuliMessageGroupText initWithCoder:];
-[CTLazuliMessageGroupText copyWithZone:];
-[CTLazuliMessageGroupText isEqual:];
-[CTLazuliMessageGroupText chatInformation];
-[CTLazuliMessageGroupText initWithReflection:];
-[CTLazuliMessageGroupText isEqualToCTLazuliMessageGroupText:];
-[CTLazuliMessageGroupText setChatInformation:];
```
