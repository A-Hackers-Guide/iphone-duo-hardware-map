# `CMIndoorOutdoorManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"CMIndoorOutdoorManagerInternal" _internal;
@"<CMIndoorOutdoorDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMIndoorOutdoorDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[CMIndoorOutdoorManager isIndoorOutdoorStateAvailable];
```

## Instance methods

```
-[CMIndoorOutdoorManager init];
-[CMIndoorOutdoorManager dealloc];
-[CMIndoorOutdoorManager setDelegate:];
-[CMIndoorOutdoorManager delegate];
-[CMIndoorOutdoorManager lastKnownIndoorOutdoorStateWithHandler:];
-[CMIndoorOutdoorManager startIndoorOutdoorUpdates];
-[CMIndoorOutdoorManager stopIndoorOutdoorUpdates];
```
