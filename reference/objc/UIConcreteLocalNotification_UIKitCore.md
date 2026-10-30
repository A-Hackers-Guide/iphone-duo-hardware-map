# `UIConcreteLocalNotification`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILocalNotification`
- Protocols: `NSSecureCoding`
- 15 instance variables, 0 properties, 45 instance methods, 1 class methods

## Instance variables

```
@"NSDate" fireDate;
@"NSTimeZone" timeZone;
Q repeatInterval;
@"NSCalendar" repeatCalendar;
@"CLRegion" region;
B regionTriggersOnce;
@"NSString" alertBody;
B hasAction;
@"NSString" alertAction;
@"NSString" alertLaunchImage;
@"NSString" alertTitle;
@"NSString" soundName;
q applicationIconBadgeNumber;
@"NSData" userInfoData;
@"NSString" category;
```

## Class methods

```
+[UIConcreteLocalNotification supportsSecureCoding];
```

## Instance methods

```
-[UIConcreteLocalNotification setRegion:];
-[UIConcreteLocalNotification validate];
-[UIConcreteLocalNotification setTimeZone:];
-[UIConcreteLocalNotification region];
-[UIConcreteLocalNotification setCategory:];
-[UIConcreteLocalNotification repeatInterval];
-[UIConcreteLocalNotification setSoundName:];
-[UIConcreteLocalNotification init];
-[UIConcreteLocalNotification category];
-[UIConcreteLocalNotification setRepeatInterval:];
-[UIConcreteLocalNotification userInfo];
-[UIConcreteLocalNotification fireDate];
-[UIConcreteLocalNotification setUserInfo:];
-[UIConcreteLocalNotification alertBody];
-[UIConcreteLocalNotification setFireDate:];
-[UIConcreteLocalNotification timeZone];
-[UIConcreteLocalNotification alertLaunchImage];
-[UIConcreteLocalNotification soundName];
-[UIConcreteLocalNotification encodeWithCoder:];
-[UIConcreteLocalNotification isValid];
-[UIConcreteLocalNotification hash];
-[UIConcreteLocalNotification description];
-[UIConcreteLocalNotification initWithCoder:];
-[UIConcreteLocalNotification copyWithZone:];
-[UIConcreteLocalNotification setAlertLaunchImage:];
-[UIConcreteLocalNotification isEqual:];
-[UIConcreteLocalNotification setAlertBody:];
-[UIConcreteLocalNotification setAlertAction:];
-[UIConcreteLocalNotification _setUserInfoData:];
-[UIConcreteLocalNotification alertAction];
-[UIConcreteLocalNotification alertTitle];
-[UIConcreteLocalNotification applicationIconBadgeNumber];
-[UIConcreteLocalNotification compareFireDates:];
-[UIConcreteLocalNotification hasAction];
-[UIConcreteLocalNotification isTriggeredByDate];
-[UIConcreteLocalNotification isTriggeredByRegion];
-[UIConcreteLocalNotification nextFireDateAfterDate:localTimeZone:];
-[UIConcreteLocalNotification nextFireDateForLastFireDate:];
-[UIConcreteLocalNotification regionTriggersOnce];
-[UIConcreteLocalNotification repeatCalendar];
-[UIConcreteLocalNotification setAlertTitle:];
-[UIConcreteLocalNotification setApplicationIconBadgeNumber:];
-[UIConcreteLocalNotification setHasAction:];
-[UIConcreteLocalNotification setRegionTriggersOnce:];
-[UIConcreteLocalNotification setRepeatCalendar:];
```
