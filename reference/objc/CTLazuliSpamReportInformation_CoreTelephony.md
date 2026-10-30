# `CTLazuliSpamReportInformation`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _isChatbot;
@"NSString" _destinationUri;
@"NSString" _spamReportingUri;
@"CTLazuliMessageIDList" _messageIDList;
@"NSString" _content;
q _spamType;
@"NSString" _freeBodyText;
```

## Properties

```
@property (T@"NSString",&,N,V_spamReportingUri) spamReportingUri;
@property (TB,N,V_isChatbot) isChatbot;
@property (T@"NSString",&,N,V_destinationUri) destinationUri;
@property (T@"CTLazuliMessageIDList",&,N,V_messageIDList) messageIDList;
@property (T@"NSString",&,N,V_content) content;
@property (Tq,N,V_spamType) spamType;
@property (T@"NSString",&,N,V_freeBodyText) freeBodyText;
```

## Class methods

```
+[CTLazuliSpamReportInformation supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliSpamReportInformation setContent:];
-[CTLazuliSpamReportInformation content];
-[CTLazuliSpamReportInformation encodeWithCoder:];
-[CTLazuliSpamReportInformation description];
-[CTLazuliSpamReportInformation initWithCoder:];
-[CTLazuliSpamReportInformation copyWithZone:];
-[CTLazuliSpamReportInformation isEqual:];
-[CTLazuliSpamReportInformation destinationUri];
-[CTLazuliSpamReportInformation freeBodyText];
-[CTLazuliSpamReportInformation initWithReflection:];
-[CTLazuliSpamReportInformation isChatbot];
-[CTLazuliSpamReportInformation isEqualToCTLazuliSpamReportInformation:];
-[CTLazuliSpamReportInformation messageIDList];
-[CTLazuliSpamReportInformation setDestinationUri:];
-[CTLazuliSpamReportInformation setFreeBodyText:];
-[CTLazuliSpamReportInformation setIsChatbot:];
-[CTLazuliSpamReportInformation setMessageIDList:];
-[CTLazuliSpamReportInformation setSpamReportingUri:];
-[CTLazuliSpamReportInformation setSpamType:];
-[CTLazuliSpamReportInformation spamReportingUri];
-[CTLazuliSpamReportInformation spamType];
```
