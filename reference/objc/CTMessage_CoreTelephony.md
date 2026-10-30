# `CTMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 19 properties, 52 instance methods, 0 class methods

## Instance variables

```
@"NSObject<CTMessageAddress><NSCopying>" _sender;
@"NSMutableArray" _recipients;
@"NSMutableArray" _items;
@"NSDictionary" _rawHeaders;
@"NSDate" _date;
I _messageId;
i _messageType;
@"CTPhoneNumber" _serviceCenter;
@"NSString" _subject;
@"NSString" _contentType;
@"NSMutableDictionary" _contentTypeParams;
I _replaceMessage;
@"NSString" _countryCode;
@"NSString" _lazuliGUID;
@"NSUUID" _uuid;
B _bypassSupportedMessageModesCheck;
B _appCheckBypassForCriticalMessaging;
@"CTXPCServiceSubscriptionContext" _context;
B _replyEnabled;
i _smsType;
C _messageReference;
```

## Properties

```
@property (T@"NSArray",R,V_recipients) recipients;
@property (T@"NSDate",R,V_date) date;
@property (T@"NSArray",R,V_items) items;
@property (T@"NSDictionary",R,V_rawHeaders) rawHeaders;
@property (TI,R,V_replaceMessage) replaceMessage;
@property (TI,N,V_messageId) messageId;
@property (Ti,N,V_messageType) messageType;
@property (T@"CTPhoneNumber",C,N,V_serviceCenter) serviceCenter;
@property (T@"NSString",C,N,V_subject) subject;
@property (T@"NSObject<CTMessageAddress><NSCopying>",C,N,V_sender) sender;
@property (T@"NSString",C,N,V_contentType) contentType;
@property (T@"NSString",R,C,N,V_countryCode) countryCode;
@property (T@"NSUUID",&,N,V_uuid) uniqueIdentifier;
@property (TB,N,V_bypassSupportedMessageModesCheck) bypassSupportedMessageModesCheck;
@property (TB,N,V_appCheckBypassForCriticalMessaging) appCheckBypassForCriticalMessaging;
@property (T@"CTXPCServiceSubscriptionContext",C,N,V_context) context;
@property (TB,R,N,V_replyEnabled) replyEnabled;
@property (Ti,N,V_smsType) smsType;
@property (TC,N,V_messageReference) messageReference;
```

## Instance methods

```
-[CTMessage setSubject:];
-[CTMessage setContentType:];
-[CTMessage addText:];
-[CTMessage initWithDate:];
-[CTMessage subject];
-[CTMessage setRecipient:];
-[CTMessage init];
-[CTMessage messageType];
-[CTMessage addRecipient:];
-[CTMessage contentType];
-[CTMessage setUniqueIdentifier:];
-[CTMessage items];
-[CTMessage setMessageId:];
-[CTMessage uniqueIdentifier];
-[CTMessage date];
-[CTMessage sender];
-[CTMessage countryCode];
-[CTMessage setContext:];
-[CTMessage messageId];
-[CTMessage description];
-[CTMessage setRecipients:];
-[CTMessage setSender:];
-[CTMessage removeRecipient:];
-[CTMessage context];
-[CTMessage recipients];
-[CTMessage setCountryCode:];
-[CTMessage setMessageType:];
-[CTMessage smsType];
-[CTMessage addContentTypeParameterWithName:value:];
-[CTMessage addData:withContentType:];
-[CTMessage addEmailRecipient:];
-[CTMessage addPart:];
-[CTMessage addPhoneRecipient:];
-[CTMessage allContentTypeParameterNames];
-[CTMessage appCheckBypassForCriticalMessaging];
-[CTMessage bypassSupportedMessageModesCheck];
-[CTMessage contentTypeParameterWithName:];
-[CTMessage messageReference];
-[CTMessage rawHeaders];
-[CTMessage removePartAtIndex:];
-[CTMessage removeRecipientsInArray:];
-[CTMessage replaceMessage];
-[CTMessage replyEnabled];
-[CTMessage serviceCenter];
-[CTMessage setAppCheckBypassForCriticalMessaging:];
-[CTMessage setBypassSupportedMessageModesCheck:];
-[CTMessage setMessageReference:];
-[CTMessage setRawHeaders:];
-[CTMessage setReplaceMessage:];
-[CTMessage setReplyEnabled:];
-[CTMessage setServiceCenter:];
-[CTMessage setSmsType:];
```
