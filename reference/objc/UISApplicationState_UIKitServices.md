# `UISApplicationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"UISApplicationStateClient" _client;
```

## Properties

```
@property (TB,N,S_setUsesBackgroundNetwork:) _usesBackgroundNetwork;
@property (T@"NSDate",N,S_setNextWakeDate:) _nextWakeDate;
@property (T@,C,N) badgeValue;
```

## Instance methods

```
-[UISApplicationState badgeValue];
-[UISApplicationState setBadgeValue:];
-[UISApplicationState init];
-[UISApplicationState _usesBackgroundNetwork];
-[UISApplicationState dealloc];
-[UISApplicationState initForCurrentApplication];
-[UISApplicationState _nextWakeDate];
-[UISApplicationState _setMinimumBackgroundFetchInterval:];
-[UISApplicationState _setNextWakeDate:];
-[UISApplicationState initWithBundleIdentifier:];
-[UISApplicationState _setUsesBackgroundNetwork:];
```
