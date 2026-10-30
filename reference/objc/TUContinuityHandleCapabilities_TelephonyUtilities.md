# `TUContinuityHandleCapabilities`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
B _supportsTelephonyCalls;
B _supportsFaceTimeAudio;
B _supportsFaceTimeVideo;
```

## Properties

```
@property (TB,R,N,V_supportsTelephonyCalls) supportsTelephonyCalls;
@property (TB,R,N,V_supportsFaceTimeAudio) supportsFaceTimeAudio;
@property (TB,R,N,V_supportsFaceTimeVideo) supportsFaceTimeVideo;
```

## Class methods

```
+[TUContinuityHandleCapabilities supportsSecureCoding];
```

## Instance methods

```
-[TUContinuityHandleCapabilities supportsTelephonyCalls];
-[TUContinuityHandleCapabilities encodeWithCoder:];
-[TUContinuityHandleCapabilities initWithCoder:];
-[TUContinuityHandleCapabilities initWithSupportsTelephonyCalls:supportsFaceTimeAudio:supportsFaceTimeVideo:];
-[TUContinuityHandleCapabilities supportsFaceTimeAudio];
-[TUContinuityHandleCapabilities supportsFaceTimeVideo];
```
