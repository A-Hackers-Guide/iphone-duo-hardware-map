# `AVVCContextSettings`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _announceCallsEnabled;
q _activationMode;
@"NSString" _activationDeviceUID;
```

## Properties

```
@property (Tq,N,V_activationMode) activationMode;
@property (T@"NSString",&,N,V_activationDeviceUID) activationDeviceUID;
@property (TB,N,V_announceCallsEnabled) announceCallsEnabled;
```

## Instance methods

```
-[AVVCContextSettings toDictionary];
-[AVVCContextSettings activationMode];
-[AVVCContextSettings setActivationMode:];
-[AVVCContextSettings copyWithZone:];
-[AVVCContextSettings initWithMode:deviceUID:];
-[AVVCContextSettings announceCallsEnabled];
-[AVVCContextSettings setAnnounceCallsEnabled:];
-[AVVCContextSettings activationDeviceUID];
-[AVVCContextSettings setActivationDeviceUID:];
```
