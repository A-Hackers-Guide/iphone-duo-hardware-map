# `CTLazuliChatBotSpamReportInformation`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _chatbotUri;
@"CTLazuliMessageIDList" _messageIDList;
q _spamType;
@"NSString" _freeBodyText;
```

## Properties

```
@property (T@"NSString",&,N,V_chatbotUri) chatbotUri;
@property (T@"CTLazuliMessageIDList",&,N,V_messageIDList) messageIDList;
@property (Tq,N,V_spamType) spamType;
@property (T@"NSString",&,N,V_freeBodyText) freeBodyText;
```

## Class methods

```
+[CTLazuliChatBotSpamReportInformation supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliChatBotSpamReportInformation encodeWithCoder:];
-[CTLazuliChatBotSpamReportInformation description];
-[CTLazuliChatBotSpamReportInformation initWithCoder:];
-[CTLazuliChatBotSpamReportInformation copyWithZone:];
-[CTLazuliChatBotSpamReportInformation isEqual:];
-[CTLazuliChatBotSpamReportInformation chatbotUri];
-[CTLazuliChatBotSpamReportInformation freeBodyText];
-[CTLazuliChatBotSpamReportInformation initWithReflection:];
-[CTLazuliChatBotSpamReportInformation isEqualToCTLazuliChatBotSpamReportInformation:];
-[CTLazuliChatBotSpamReportInformation messageIDList];
-[CTLazuliChatBotSpamReportInformation setChatbotUri:];
-[CTLazuliChatBotSpamReportInformation setFreeBodyText:];
-[CTLazuliChatBotSpamReportInformation setMessageIDList:];
-[CTLazuliChatBotSpamReportInformation setSpamType:];
-[CTLazuliChatBotSpamReportInformation spamType];
```
