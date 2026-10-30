# `UILocalNotification`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSCoding`
- 0 instance variables, 15 properties, 11 instance methods, 2 class methods

## Properties

```
@property (T@"NSDate",C,D,N) fireDate;
@property (T@"NSTimeZone",C,D,N) timeZone;
@property (TQ,D,N) repeatInterval;
@property (T@"NSCalendar",C,D,N) repeatCalendar;
@property (T@"CLRegion",C,D,N) region;
@property (TB,D,N) regionTriggersOnce;
@property (T@"NSString",C,D,N) alertBody;
@property (TB,D,N) hasAction;
@property (T@"NSString",C,D,N) alertAction;
@property (T@"NSString",C,D,N) alertLaunchImage;
@property (T@"NSString",C,D,N) alertTitle;
@property (T@"NSString",C,D,N) soundName;
@property (Tq,D,N) applicationIconBadgeNumber;
@property (T@"NSDictionary",C,D,N) userInfo;
@property (T@"NSString",C,D,N) category;
```

## Class methods

```
+[UILocalNotification allocWithZone:];
+[UILocalNotification alloc];
```

## Instance methods

```
-[UILocalNotification validate];
-[UILocalNotification init];
-[UILocalNotification encodeWithCoder:];
-[UILocalNotification isValid];
-[UILocalNotification initWithCoder:];
-[UILocalNotification copyWithZone:];
-[UILocalNotification compareFireDates:];
-[UILocalNotification isTriggeredByDate];
-[UILocalNotification isTriggeredByRegion];
-[UILocalNotification nextFireDateAfterDate:localTimeZone:];
-[UILocalNotification nextFireDateForLastFireDate:];
```
