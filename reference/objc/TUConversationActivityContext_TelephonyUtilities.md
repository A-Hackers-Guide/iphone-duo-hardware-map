# `TUConversationActivityContext`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 7 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSString" _typedIdentifier;
@"NSString" _actionDescription;
@"NSString" _ongoingDescription;
@"NSString" _completedDescription;
```

## Properties

```
@property (T@"NSString",C,N,V_typedIdentifier) typedIdentifier;
@property (T@"NSString",C,N,V_actionDescription) actionDescription;
@property (T@"NSString",C,N,V_ongoingDescription) ongoingDescription;
@property (T@"NSString",C,N,V_completedDescription) completedDescription;
@property (T@"NSString",R,C,N) identifier;
@property (T@"NSString",R,C,N) analyticsIdentifier;
@property (TB,R,N,GisMedia) media;
```

## Class methods

```
+[TUConversationActivityContext supportsSecureCoding];
+[TUConversationActivityContext mediaContextIdentifiers];
```

## Instance methods

```
-[TUConversationActivityContext identifier];
-[TUConversationActivityContext encodeWithCoder:];
-[TUConversationActivityContext hash];
-[TUConversationActivityContext description];
-[TUConversationActivityContext initWithCoder:];
-[TUConversationActivityContext copyWithZone:];
-[TUConversationActivityContext isEqual:];
-[TUConversationActivityContext actionDescription];
-[TUConversationActivityContext isMedia];
-[TUConversationActivityContext typedIdentifier];
-[TUConversationActivityContext analyticsIdentifier];
-[TUConversationActivityContext completedDescription];
-[TUConversationActivityContext initWithContextIdentifier:actionDescription:ongoingDescription:completedDescription:];
-[TUConversationActivityContext isEqualToActivityContext:];
-[TUConversationActivityContext ongoingDescription];
-[TUConversationActivityContext setActionDescription:];
-[TUConversationActivityContext setCompletedDescription:];
-[TUConversationActivityContext setOngoingDescription:];
-[TUConversationActivityContext setTypedIdentifier:];
```
