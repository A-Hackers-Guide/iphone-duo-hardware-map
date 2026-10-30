# `CTVoicemailInfoType`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _available;
B _isNetworkOriginated;
B _isVoiceMailMWI;
@"NSString" _url;
@"NSNumber" _count;
```

## Properties

```
@property (T@"NSString",&,N,V_url) url;
@property (TB,N,V_available) available;
@property (T@"NSNumber",&,N,V_count) count;
@property (TB,N,V_isNetworkOriginated) isNetworkOriginated;
@property (TB,N,V_isVoiceMailMWI) isVoiceMailMWI;
```

## Class methods

```
+[CTVoicemailInfoType supportsSecureCoding];
```

## Instance methods

```
-[CTVoicemailInfoType setCount:];
-[CTVoicemailInfoType init];
-[CTVoicemailInfoType count];
-[CTVoicemailInfoType setAvailable:];
-[CTVoicemailInfoType available];
-[CTVoicemailInfoType encodeWithCoder:];
-[CTVoicemailInfoType description];
-[CTVoicemailInfoType initWithCoder:];
-[CTVoicemailInfoType setUrl:];
-[CTVoicemailInfoType copyWithZone:];
-[CTVoicemailInfoType isEqual:];
-[CTVoicemailInfoType url];
-[CTVoicemailInfoType initWithParam:available:count:isNetworkOriginated:isVoiceMailMWI:];
-[CTVoicemailInfoType isEqualToCTVoicemailInfoType:];
-[CTVoicemailInfoType isNetworkOriginated];
-[CTVoicemailInfoType isVoiceMailMWI];
-[CTVoicemailInfoType setIsNetworkOriginated:];
-[CTVoicemailInfoType setIsVoiceMailMWI:];
```
