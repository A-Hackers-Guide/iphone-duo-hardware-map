# `TUConversationActivityAdvertisement`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _sessionUUID;
@"NSString" _contactID;
@"TUHandle" _handle;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sessionUUID) sessionUUID;
@property (T@"NSString",R,C,N,V_contactID) contactID;
@property (T@"TUHandle",R,C,N,V_handle) handle;
```

## Class methods

```
+[TUConversationActivityAdvertisement supportsSecureCoding];
```

## Instance methods

```
-[TUConversationActivityAdvertisement sessionUUID];
-[TUConversationActivityAdvertisement handle];
-[TUConversationActivityAdvertisement encodeWithCoder:];
-[TUConversationActivityAdvertisement description];
-[TUConversationActivityAdvertisement initWithCoder:];
-[TUConversationActivityAdvertisement contactID];
-[TUConversationActivityAdvertisement initWithSessionID:contactID:handle:];
```
