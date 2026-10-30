# `TPAlert`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@? _completion;
^{__CFUserNotification=} _userNotification;
```

## Properties

```
@property (T^{__CFUserNotification=},N,V_userNotification) userNotification;
@property (T@?,C,N,V_completion) completion;
@property (T@"NSString",R,N) title;
@property (T@"NSString",R,N) message;
@property (T@"NSString",R,N) defaultButtonTitle;
@property (T@"NSString",R,N) alternateButtonTitle;
@property (T@"NSString",R,N) otherButtonTitle;
```

## Instance methods

```
-[TPAlert setCompletion:];
-[TPAlert completion];
-[TPAlert message];
-[TPAlert dealloc];
-[TPAlert defaultButtonTitle];
-[TPAlert alternateButtonTitle];
-[TPAlert invalidate];
-[TPAlert title];
-[TPAlert show];
-[TPAlert setUserNotification:];
-[TPAlert otherButtonTitle];
-[TPAlert userNotification];
-[TPAlert defaultResponse];
-[TPAlert alternateResponse];
-[TPAlert otherResponse];
-[TPAlert showOnViewController:];
```
