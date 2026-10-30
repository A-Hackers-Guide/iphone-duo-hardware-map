# `CAFLocalNotificationUserActions`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 2 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _localNotificationUserActions;
@"NSError" _parseError;
```

## Properties

```
@property (T@"NSArray",R,N,V_localNotificationUserActions) localNotificationUserActions;
@property (T@"NSError",R,N,V_parseError) parseError;
@property (T@"NSString",R,N) formattedValue;
@property (T@"NSArray",R,N) arrayRepresentation;
```

## Class methods

```
+[CAFLocalNotificationUserActions localNotificationUserActionsWithArray:];
+[CAFLocalNotificationUserActions localNotificationUserActionsWithLocalNotificationUserActions:];
```

## Instance methods

```
-[CAFLocalNotificationUserActions formattedValue];
-[CAFLocalNotificationUserActions objectAtIndexedSubscript:];
-[CAFLocalNotificationUserActions initWithArray:];
-[CAFLocalNotificationUserActions countByEnumeratingWithState:objects:count:];
-[CAFLocalNotificationUserActions arrayRepresentation];
-[CAFLocalNotificationUserActions objectAtIndex:];
-[CAFLocalNotificationUserActions parseError];
-[CAFLocalNotificationUserActions localNotificationUserActions];
-[CAFLocalNotificationUserActions initWithLocalNotificationUserActions:];
```
