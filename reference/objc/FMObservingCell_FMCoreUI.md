# `FMObservingCell`

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@ _representedObject;
@"NSMutableDictionary" _kvoObservationTokens;
@"NSMutableSet" _notificationTokens;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_kvoObservationTokens) kvoObservationTokens;
@property (T@"NSMutableSet",&,N,V_notificationTokens) notificationTokens;
@property (T@,W,N,V_representedObject) representedObject;
```

## Instance methods

```
-[FMObservingCell prepareForReuse];
-[FMObservingCell representedObject];
-[FMObservingCell setRepresentedObject:];
-[FMObservingCell notificationTokens];
-[FMObservingCell setNotificationTokens:];
-[FMObservingCell addKVOObservationToken:forObject:];
-[FMObservingCell addNotificationToken:];
-[FMObservingCell addObserversForRepresentedObject:];
-[FMObservingCell kvoObservationTokens];
-[FMObservingCell removeKVOObservationTokens];
-[FMObservingCell removeNotificationTokens];
-[FMObservingCell setKvoObservationTokens:];
```
