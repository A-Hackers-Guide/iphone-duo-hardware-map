# `ISPKitResourceFinder`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSBundle" _bundle;
@"NSObject<OS_os_log>" _logger;
B _hasOverride;
```

## Properties

```
@property (TB,R,N,V_hasOverride) hasOverride;
```

## Class methods

```
+[ISPKitResourceFinder sharedInstance];
```

## Instance methods

```
-[ISPKitResourceFinder init];
-[ISPKitResourceFinder hasOverride];
-[ISPKitResourceFinder modelSpecificName];
-[ISPKitResourceFinder pathForABDNetResources];
-[ISPKitResourceFinder pathForCurrentDeviceResource:ofType:];
-[ISPKitResourceFinder pathForDevice:resource:ofType:];
```
