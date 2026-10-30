# `UIMailConversationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIConversationContext`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _responseHasCustomSignature;
@"NSString" _responseSubject;
@"NSSet" _responseSecondaryRecipientIdentifiers;
```

## Properties

```
@property (T@"NSString",C,N,V_responseSubject) responseSubject;
@property (TB,N,V_responseHasCustomSignature) responseHasCustomSignature;
@property (T@"NSSet",C,N,V_responseSecondaryRecipientIdentifiers) responseSecondaryRecipientIdentifiers;
```

## Instance methods

```
-[UIMailConversationContext infoDictionary];
-[UIMailConversationContext init];
-[UIMailConversationContext responseSubject];
-[UIMailConversationContext inputContextHistoryRepresentation];
-[UIMailConversationContext responseHasCustomSignature];
-[UIMailConversationContext responseSecondaryRecipientIdentifiers];
-[UIMailConversationContext setResponseHasCustomSignature:];
-[UIMailConversationContext setResponseSecondaryRecipientIdentifiers:];
-[UIMailConversationContext setResponseSubject:];
-[UIMailConversationContext stringForMailSubtype:];
```
