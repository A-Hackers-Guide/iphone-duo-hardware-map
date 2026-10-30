# `TUUIContext`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _inCallUIState;
```

## Properties

```
@property (TQ,N,V_inCallUIState) inCallUIState;
@property (TB,R,N,GisMicIndicatorVisible) isMicIndicatorVisible;
@property (TB,R,N,GisFullScreen) fullScreen;
```

## Class methods

```
+[TUUIContext supportsSecureCoding];
```

## Instance methods

```
-[TUUIContext isFullScreen];
-[TUUIContext initWithState:];
-[TUUIContext encodeWithCoder:];
-[TUUIContext initWithCoder:];
-[TUUIContext inCallUIState];
-[TUUIContext isMicIndicatorVisible];
-[TUUIContext setInCallUIState:];
```
