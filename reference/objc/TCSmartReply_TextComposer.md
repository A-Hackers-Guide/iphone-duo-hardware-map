# `TCSmartReply`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isRichSmartReply;
B _isPersonalized;
@"NSString" _responseText;
@"NSString" _responseTextMetadata;
@"NSUUID" _replyIdentifier;
@"NSString" _intent;
```

## Properties

```
@property (T@"NSString",R,C,N,V_responseText) responseText;
@property (TB,R,N,V_isRichSmartReply) isRichSmartReply;
@property (TB,R,N,V_isPersonalized) isPersonalized;
@property (T@"NSString",R,C,N,V_responseTextMetadata) responseTextMetadata;
@property (T@"NSUUID",R,C,N,V_replyIdentifier) replyIdentifier;
@property (T@"NSString",R,C,N,V_intent) intent;
```

## Class methods

```
+[TCSmartReply supportsSecureCoding];
```

## Instance methods

```
-[TCSmartReply intent];
-[TCSmartReply replyIdentifier];
-[TCSmartReply encodeWithCoder:];
-[TCSmartReply hash];
-[TCSmartReply initWithCoder:];
-[TCSmartReply copyWithZone:];
-[TCSmartReply isEqual:];
-[TCSmartReply isPersonalized];
-[TCSmartReply responseText];
-[TCSmartReply initWithResponseText:isRichSmartReply:];
-[TCSmartReply isRichSmartReply];
-[TCSmartReply initWithResponseText:isRichSmartReply:isPersonalized:];
-[TCSmartReply initWithResponseText:isRichSmartReply:isPersonalized:responseTextMetadata:];
-[TCSmartReply initWithResponseText:isRichSmartReply:isPersonalized:responseTextMetadata:identifier:intent:];
-[TCSmartReply responseTextMetadata];
```
