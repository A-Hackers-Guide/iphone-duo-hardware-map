# `SBBookmark`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHBookmark`
- Protocols: `UISApplicationStateServiceDataSource`
- 2 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
b3 _hasBadgeValue;
@"FBSApplicationDataStore" _dataStore;
```

## Properties

```
@property (T@"FBSApplicationDataStore",R,N,V_dataStore) dataStore;
@property (T@"<NSCopying>",C,N) badgeValue;
@property (TB,?,N) usesBackgroundNetwork;
@property (T@"NSDate",?,&,N) nextWakeDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBookmark badgeValue];
-[SBBookmark setBadgeValue:];
-[SBBookmark icon:launchFromLocation:context:];
-[SBBookmark dataStore];
-[SBBookmark isTimedOutForIcon:];
-[SBBookmark _noteIconDataSourceDidChange];
-[SBBookmark badgeNumberOrStringForIcon:];
-[SBBookmark initWithWebClip:];
```
