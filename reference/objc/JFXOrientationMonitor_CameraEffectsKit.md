# `JFXOrientationMonitor`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 23 instance methods, 10 class methods

## Instance variables

```
i _darwinNotificationToken;
@"UIWindow" _keyWindow;
@"NSObject<OS_dispatch_queue>" _darwinNotificationQ;
q _deviceOrientation_lock;
q _deviceInterfaceOrientation;
q _deviceInterfaceOrientation_lock;
q _interfaceOrientation_lock;
```

## Properties

```
@property (T@"UIWindow",R,N,V_keyWindow) keyWindow;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_darwinNotificationQ) darwinNotificationQ;
@property (Ti,N,V_darwinNotificationToken) darwinNotificationToken;
@property (Tq,N) deviceOrientation;
@property (Tq,N,V_deviceOrientation_lock) deviceOrientation_lock;
@property (Tq,N,V_deviceInterfaceOrientation) deviceInterfaceOrientation;
@property (Tq,N,V_deviceInterfaceOrientation_lock) deviceInterfaceOrientation_lock;
@property (Tq,N) interfaceOrientation;
@property (Tq,N,V_interfaceOrientation_lock) interfaceOrientation_lock;
```

## Class methods

```
+[JFXOrientationMonitor deviceOrientation];
+[JFXOrientationMonitor interfaceOrientation];
+[JFXOrientationMonitor initialized];
+[JFXOrientationMonitor deviceInterfaceOrientation];
+[JFXOrientationMonitor keyWindow];
+[JFXOrientationMonitor uninitialize];
+[JFXOrientationMonitor JFX_initLock];
+[JFXOrientationMonitor initializeWithKeyWindow:];
+[JFXOrientationMonitor initializeWithViewController:];
+[JFXOrientationMonitor isDeviceInterfaceLandscape];
```

## Instance methods

```
-[JFXOrientationMonitor setDeviceOrientation:];
-[JFXOrientationMonitor deviceOrientation];
-[JFXOrientationMonitor interfaceOrientation];
-[JFXOrientationMonitor setInterfaceOrientation:];
-[JFXOrientationMonitor setDeviceInterfaceOrientation:];
-[JFXOrientationMonitor dealloc];
-[JFXOrientationMonitor deviceInterfaceOrientation];
-[JFXOrientationMonitor keyWindow];
-[JFXOrientationMonitor JFX_UIApplicationDidEnterBackgroundNotification:];
-[JFXOrientationMonitor JFX_initDarwinNotification];
-[JFXOrientationMonitor JFX_UIApplicationDidChangeStatusBarOrientationNotification:];
-[JFXOrientationMonitor JFX_UIApplicationWillEnterForegroundNotification:];
-[JFXOrientationMonitor JFX_deviceOrientation_darwinNotificationQ];
-[JFXOrientationMonitor deviceInterfaceOrientation_lock];
-[JFXOrientationMonitor darwinNotificationQ];
-[JFXOrientationMonitor darwinNotificationToken];
-[JFXOrientationMonitor deviceOrientation_lock];
-[JFXOrientationMonitor initWithKeyWindow:];
-[JFXOrientationMonitor interfaceOrientation_lock];
-[JFXOrientationMonitor setDarwinNotificationToken:];
-[JFXOrientationMonitor setDeviceInterfaceOrientation_lock:];
-[JFXOrientationMonitor setDeviceOrientation_lock:];
-[JFXOrientationMonitor setInterfaceOrientation_lock:];
```
