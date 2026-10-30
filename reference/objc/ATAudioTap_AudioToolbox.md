# `ATAudioTap`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _screenSharingHost;
@"ATAudioTapDescription" _tapDescription;
```

## Properties

```
@property (T@"ATAudioTapDescription",R,N,V_tapDescription) tapDescription;
@property (TB,N,GisScreenSharingHost,V_screenSharingHost) screenSharingHost;
```

## Class methods

```
+[ATAudioTap supportsSecureCoding];
```

## Instance methods

```
-[ATAudioTap encodeWithCoder:];
-[ATAudioTap initWithTapDescription:];
-[ATAudioTap description];
-[ATAudioTap initWithCoder:];
-[ATAudioTap tapDescription];
-[ATAudioTap setScreenSharingHost:];
-[ATAudioTap isEqual:];
-[ATAudioTap isScreenSharingHost];
```
