# `SBExampleUserNotificationCenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"UNUserNotificationCenter" _userNotificationCenter;
```

## Properties

```
@property (T@"NSString",R,N) latestNotificationRequestIdentifier;
@property (T@"NSString",R,N) sectionIdentifier;
```

## Class methods

```
+[SBExampleUserNotificationCenter sharedInstance];
```

## Instance methods

```
-[SBExampleUserNotificationCenter publish];
-[SBExampleUserNotificationCenter update];
-[SBExampleUserNotificationCenter sectionIdentifier];
-[SBExampleUserNotificationCenter removeAllNotifications];
-[SBExampleUserNotificationCenter _existingNotificationRequestForIdentifier:];
-[SBExampleUserNotificationCenter _newNotificationRequest:threadIdentifier:];
-[SBExampleUserNotificationCenter _postNotificationWithID:threadIdentifier:];
-[SBExampleUserNotificationCenter _userNotificationCenter];
-[SBExampleUserNotificationCenter latestNotificationRequestIdentifier];
-[SBExampleUserNotificationCenter publish:completion:];
-[SBExampleUserNotificationCenter publish:numberOfUniqueThreads:completion:];
-[SBExampleUserNotificationCenter publishWithNumberOfUniqueThreads:];
```
