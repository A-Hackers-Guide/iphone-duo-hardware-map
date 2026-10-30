# `TUConversationLinkOriginator`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"TUHandle" _handle;
@"NSString" _identifier;
q _revision;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"TUHandle",&,N,V_handle) handle;
@property (Tq,N,V_revision) revision;
```

## Class methods

```
+[TUConversationLinkOriginator supportsSecureCoding];
```

## Instance methods

```
-[TUConversationLinkOriginator revision];
-[TUConversationLinkOriginator identifier];
-[TUConversationLinkOriginator setIdentifier:];
-[TUConversationLinkOriginator handle];
-[TUConversationLinkOriginator encodeWithCoder:];
-[TUConversationLinkOriginator hash];
-[TUConversationLinkOriginator description];
-[TUConversationLinkOriginator initWithCoder:];
-[TUConversationLinkOriginator setHandle:];
-[TUConversationLinkOriginator copyWithZone:];
-[TUConversationLinkOriginator isEqual:];
-[TUConversationLinkOriginator setRevision:];
-[TUConversationLinkOriginator initWithIdentifier:revision:handle:];
-[TUConversationLinkOriginator isEqualToConversationLinkOriginator:];
```
