# `TUCollaborationNotice`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationNoticeProtocol`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
q _sessionEventType;
@"SWCollaborationHighlight" _collaboration;
```

## Properties

```
@property (T@"SWCollaborationHighlight",&,N,V_collaboration) collaboration;
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (Tq,N,V_sessionEventType) sessionEventType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCollaborationNotice supportsSecureCoding];
```

## Instance methods

```
-[TUCollaborationNotice initWithUUID:];
-[TUCollaborationNotice UUID];
-[TUCollaborationNotice encodeWithCoder:];
-[TUCollaborationNotice hash];
-[TUCollaborationNotice description];
-[TUCollaborationNotice initWithCoder:];
-[TUCollaborationNotice isEqual:];
-[TUCollaborationNotice collaboration];
-[TUCollaborationNotice isEqualToCollaborationNotice:];
-[TUCollaborationNotice sessionEventType];
-[TUCollaborationNotice setCollaboration:];
-[TUCollaborationNotice setSessionEventType:];
```
