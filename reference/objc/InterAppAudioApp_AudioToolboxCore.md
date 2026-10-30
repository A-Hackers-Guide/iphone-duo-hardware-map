# `InterAppAudioApp`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"BKSApplicationStateMonitor" appMonitor;
B _isHost;
B _isCurrentApp;
B _isForeground;
q _key;
@"NSString" _name;
@"UIImage" _icon;
@"NSURL" _url;
```

## Properties

```
@property (Tq,R,N,V_key) key;
@property (T@"NSString",R,N,V_name) name;
@property (T@"UIImage",R,N,V_icon) icon;
@property (T@"NSURL",R,N,V_url) url;
@property (TB,R,N,V_isHost) isHost;
@property (TB,R,N,V_isCurrentApp) isCurrentApp;
@property (TB,R,N,V_isForeground) isForeground;
```

## Instance methods

```
-[InterAppAudioApp dealloc];
-[InterAppAudioApp isForeground];
-[InterAppAudioApp description];
-[InterAppAudioApp name];
-[InterAppAudioApp url];
-[InterAppAudioApp key];
-[InterAppAudioApp icon];
-[InterAppAudioApp init:iconSize:];
-[InterAppAudioApp isCurrentApp];
-[InterAppAudioApp isHost];
-[InterAppAudioApp processRunningOnForeground:];
```
