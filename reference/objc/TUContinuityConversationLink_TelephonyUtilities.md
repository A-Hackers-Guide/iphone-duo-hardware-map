# `TUContinuityConversationLink`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"TUConversationLink" _tuConversationLink;
@"NSString" _displayName;
@"NSDate" _date;
@"NSString" _uniqueId;
@"NSUUID" _groupUUID;
```

## Properties

```
@property (T@"TUConversationLink",R,N,V_tuConversationLink) tuConversationLink;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (T@"NSDate",R,N,V_date) date;
@property (T@"NSString",R,N,V_uniqueId) uniqueId;
@property (T@"NSUUID",R,N,V_groupUUID) groupUUID;
```

## Class methods

```
+[TUContinuityConversationLink supportsSecureCoding];
```

## Instance methods

```
-[TUContinuityConversationLink groupUUID];
-[TUContinuityConversationLink displayName];
-[TUContinuityConversationLink date];
-[TUContinuityConversationLink uniqueId];
-[TUContinuityConversationLink encodeWithCoder:];
-[TUContinuityConversationLink description];
-[TUContinuityConversationLink initWithCoder:];
-[TUContinuityConversationLink initWithTUConversationLink:displayName:date:uniqueId:groupUUID:];
-[TUContinuityConversationLink tuConversationLink];
```
