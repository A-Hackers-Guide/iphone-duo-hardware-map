# `SBApplicationLaunchImageParameters`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSString" _defaultPNGName;
@"NSString" _extension;
@"NSString" _minOSVersionString;
{CGSize="width"d"height"d} _size;
q _interfaceOrientation;
```

## Properties

```
@property (T@"NSString",R,C,N,V_defaultPNGName) defaultPNGName;
@property (T@"NSString",R,C,N,V_extension) extension;
@property (T@"NSString",R,C,N,V_minOSVersionString) minOSVersionString;
@property (T{CGSize=dd},R,N,V_size) size;
@property (Tq,R,N,V_interfaceOrientation) interfaceOrientation;
```

## Class methods

```
+[SBApplicationLaunchImageParameters launchImageParametersFromLaunchImagesInfo:withBundleIdentifier:isMonarchLinked:];
+[SBApplicationLaunchImageParameters validInfoPlistOrientationKeys];
```

## Instance methods

```
-[SBApplicationLaunchImageParameters interfaceOrientation];
-[SBApplicationLaunchImageParameters init];
-[SBApplicationLaunchImageParameters size];
-[SBApplicationLaunchImageParameters hash];
-[SBApplicationLaunchImageParameters description];
-[SBApplicationLaunchImageParameters extension];
-[SBApplicationLaunchImageParameters isEqual:];
-[SBApplicationLaunchImageParameters defaultPNGName];
-[SBApplicationLaunchImageParameters minOSVersionString];
```
