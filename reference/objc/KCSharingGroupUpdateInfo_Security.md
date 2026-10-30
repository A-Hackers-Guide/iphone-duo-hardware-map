# `KCSharingGroupUpdateInfo`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _updateType;
@"KCSharingGroup" _updatedGroup;
@"NSArray" _addedParticipants;
@"NSString" _departedGroupID;
```

## Properties

```
@property (Tq,R,N,V_updateType) updateType;
@property (T@"KCSharingGroup",R,N,V_updatedGroup) updatedGroup;
@property (T@"NSArray",R,N,V_addedParticipants) addedParticipants;
@property (T@"NSString",R,N,V_departedGroupID) departedGroupID;
```

## Class methods

```
+[KCSharingGroupUpdateInfo supportsSecureCoding];
```

## Instance methods

```
-[KCSharingGroupUpdateInfo updateType];
-[KCSharingGroupUpdateInfo encodeWithCoder:];
-[KCSharingGroupUpdateInfo description];
-[KCSharingGroupUpdateInfo initWithCoder:];
-[KCSharingGroupUpdateInfo departedGroupID];
-[KCSharingGroupUpdateInfo addedParticipants];
-[KCSharingGroupUpdateInfo initWithDepartedGroupID:];
-[KCSharingGroupUpdateInfo initWithGroup:addedParticipants:];
-[KCSharingGroupUpdateInfo updatedGroup];
```
