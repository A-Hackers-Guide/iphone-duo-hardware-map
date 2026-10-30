# `SBApplicationServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacility`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"<SBApplicationServerMiscDelegate>" _miscDelegate;
@"<SBApplicationServerHarmonyDelegate>" _harmonyDelegate;
@"<SBApplicationServerShortcutDelegate>" _shortcutDelegate;
@"<SBApplicationServerMultiwindowDelegate>" _multiwindowDelegate;
```

## Properties

```
@property (T@"<SBApplicationServerMiscDelegate>",W,N,V_miscDelegate) miscDelegate;
@property (T@"<SBApplicationServerHarmonyDelegate>",W,N,V_harmonyDelegate) harmonyDelegate;
@property (T@"<SBApplicationServerShortcutDelegate>",W,N,V_shortcutDelegate) shortcutDelegate;
@property (T@"<SBApplicationServerMultiwindowDelegate>",W,N,V_multiwindowDelegate) multiwindowDelegate;
```

## Class methods

```
+[SBApplicationServer sharedInstance];
```

## Instance methods

```
-[SBApplicationServer dealloc];
-[SBApplicationServer noteDidReceiveMessage:withType:fromClient:];
-[SBApplicationServer harmonyDelegate];
-[SBApplicationServer miscDelegate];
-[SBApplicationServer multiwindowDelegate];
-[SBApplicationServer setHarmonyDelegate:];
-[SBApplicationServer setMiscDelegate:];
-[SBApplicationServer setMultiwindowDelegate:];
-[SBApplicationServer setShortcutDelegate:];
-[SBApplicationServer shortcutDelegate];
```
