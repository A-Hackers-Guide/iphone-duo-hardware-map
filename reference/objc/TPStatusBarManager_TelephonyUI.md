# `TPStatusBarManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _currentAbbreviatedStatusBarString;
@"NSTimer" _callDurationTimer;
```

## Properties

```
@property (T@"NSTimer",&,N,V_callDurationTimer) callDurationTimer;
@property (T@"NSString",C,N,V_currentAbbreviatedStatusBarString) currentAbbreviatedStatusBarString;
```

## Class methods

```
+[TPStatusBarManager sharedInstance];
```

## Instance methods

```
-[TPStatusBarManager init];
-[TPStatusBarManager dealloc];
-[TPStatusBarManager callDurationTimer];
-[TPStatusBarManager currentAbbreviatedStatusBarString];
-[TPStatusBarManager setCallDurationTimer:];
-[TPStatusBarManager setCurrentAbbreviatedStatusBarString:];
-[TPStatusBarManager updateCurrentAbbreviatedStatusBarString];
-[TPStatusBarManager updateCurrentAbbreviatedStatusBarStringAndSendNotification];
```
