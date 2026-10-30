# `KCSharingGroupFetchRequest`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 5 instance methods, 7 class methods

## Instance variables

```
@"NSPredicate" _predicate;
```

## Properties

```
@property (T@"NSPredicate",R,N,V_predicate) predicate;
```

## Class methods

```
+[KCSharingGroupFetchRequest supportsSecureCoding];
+[KCSharingGroupFetchRequest pending];
+[KCSharingGroupFetchRequest all];
+[KCSharingGroupFetchRequest groupName:];
+[KCSharingGroupFetchRequest predicateMatchingAllGroups];
+[KCSharingGroupFetchRequest predicateMatchingGroupsWithInviteStatus:];
+[KCSharingGroupFetchRequest predicateMatchingGroupsWithName:];
```

## Instance methods

```
-[KCSharingGroupFetchRequest init];
-[KCSharingGroupFetchRequest encodeWithCoder:];
-[KCSharingGroupFetchRequest initWithCoder:];
-[KCSharingGroupFetchRequest initWithPredicate:];
-[KCSharingGroupFetchRequest predicate];
```
