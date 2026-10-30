# `CAMLensSmudgeDisplayState`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 11 instance methods, 2 class methods

## Instance variables

```
d displayDuration;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 delegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 devicePosition;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 preferences;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 modeIsChanging;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 analyticsHelper;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 timer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _status;
```

## Properties

```
@property (Tq,N) status;
@property (Td,N,VdisplayDuration) displayDuration;
@property (TB,N,R) shouldDisplayLensIsSmudged;
```

## Class methods

```
+[CAMLensSmudgeDisplayState logDidEnterBackground];
+[CAMLensSmudgeDisplayState logModeChangedWithMode:];
```

## Instance methods

```
-[CAMLensSmudgeDisplayState didEnterBackground];
-[CAMLensSmudgeDisplayState init];
-[CAMLensSmudgeDisplayState status];
-[CAMLensSmudgeDisplayState setStatus:];
-[CAMLensSmudgeDisplayState displayDuration];
-[CAMLensSmudgeDisplayState setDisplayDuration:];
-[CAMLensSmudgeDisplayState acknowledgeSmudgeDetection];
-[CAMLensSmudgeDisplayState initWithDelegate:devicePosition:displayDuration:preferences:];
-[CAMLensSmudgeDisplayState modeDidChange];
-[CAMLensSmudgeDisplayState modeWillChange];
-[CAMLensSmudgeDisplayState shouldDisplayLensIsSmudged];
```
