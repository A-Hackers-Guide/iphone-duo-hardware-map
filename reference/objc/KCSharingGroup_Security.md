# `KCSharingGroup`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 10 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSString" _groupID;
@"NSString" _displayName;
@"NSArray" _participants;
@"NSURL" _shareURL;
```

## Properties

```
@property (T@"NSArray",C,N,V_participants) participants;
@property (T@"NSString",R,C,N) longDescription;
@property (T@"NSDictionary",R,C,N) JSONObject;
@property (T@"NSString",R,C,N,V_groupID) groupID;
@property (T@"NSString",C,N,V_displayName) displayName;
@property (Tq,R,N) joinState;
@property (T@"KCSharingParticipant",R,N) currentUserParticipant;
@property (T@"KCSharingParticipant",R,N) ownerParticipant;
@property (T@"NSURL",R,N,V_shareURL) shareURL;
@property (TB,R,N) isOwned;
```

## Class methods

```
+[KCSharingGroup supportsSecureCoding];
```

## Instance methods

```
-[KCSharingGroup shareURL];
-[KCSharingGroup addParticipant:];
-[KCSharingGroup JSONObject];
-[KCSharingGroup groupID];
-[KCSharingGroup displayName];
-[KCSharingGroup setDisplayName:];
-[KCSharingGroup setParticipants:];
-[KCSharingGroup removeParticipant:];
-[KCSharingGroup encodeWithCoder:];
-[KCSharingGroup hash];
-[KCSharingGroup description];
-[KCSharingGroup initWithCoder:];
-[KCSharingGroup copyWithZone:];
-[KCSharingGroup participants];
-[KCSharingGroup isEqual:];
-[KCSharingGroup longDescription];
-[KCSharingGroup isOwned];
-[KCSharingGroup currentUserParticipant];
-[KCSharingGroup initWithGroupID:participants:displayName:shareURL:];
-[KCSharingGroup initWithParticipants:displayName:];
-[KCSharingGroup joinState];
-[KCSharingGroup ownerParticipant];
```
