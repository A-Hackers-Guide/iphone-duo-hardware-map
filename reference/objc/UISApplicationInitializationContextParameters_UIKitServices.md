# `UISApplicationInitializationContextParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`
- 8 instance variables, 12 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _supportedInterfaceOrientations;
@"NSArray" _deviceFamilies;
B _requiresFullScreen;
B _supportsMultiwindow;
I _initialCGDirectDisplayID;
{CGSize="width"d"height"d} _usableDisplaySizeHint;
B _preferSmallerDisplaySize;
B _useTrueDisplaySize;
```

## Properties

```
@property (TQ,N,V_supportedInterfaceOrientations) supportedInterfaceOrientations;
@property (T@"NSArray",C,N,V_deviceFamilies) deviceFamilies;
@property (TB,N,V_requiresFullScreen) requiresFullScreen;
@property (TB,N,V_supportsMultiwindow) supportsMultiwindow;
@property (TI,N,V_initialCGDirectDisplayID) initialCGDirectDisplayID;
@property (T{CGSize=dd},N,V_usableDisplaySizeHint) usableDisplaySizeHint;
@property (TB,N,V_preferSmallerDisplaySize) preferSmallerDisplaySize;
@property (TB,N,V_useTrueDisplaySize) useTrueDisplaySize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISApplicationInitializationContextParameters init];
-[UISApplicationInitializationContextParameters supportedInterfaceOrientations];
-[UISApplicationInitializationContextParameters initWithXPCDictionary:];
-[UISApplicationInitializationContextParameters encodeWithXPCDictionary:];
-[UISApplicationInitializationContextParameters requiresFullScreen];
-[UISApplicationInitializationContextParameters setSupportsMultiwindow:];
-[UISApplicationInitializationContextParameters deviceFamilies];
-[UISApplicationInitializationContextParameters supportsMultiwindow];
-[UISApplicationInitializationContextParameters setSupportedInterfaceOrientations:];
-[UISApplicationInitializationContextParameters initialCGDirectDisplayID];
-[UISApplicationInitializationContextParameters preferSmallerDisplaySize];
-[UISApplicationInitializationContextParameters setDeviceFamilies:];
-[UISApplicationInitializationContextParameters setInitialCGDirectDisplayID:];
-[UISApplicationInitializationContextParameters setPreferSmallerDisplaySize:];
-[UISApplicationInitializationContextParameters setRequiresFullScreen:];
-[UISApplicationInitializationContextParameters setUsableDisplaySizeHint:];
-[UISApplicationInitializationContextParameters setUseTrueDisplaySize:];
-[UISApplicationInitializationContextParameters usableDisplaySizeHint];
-[UISApplicationInitializationContextParameters useTrueDisplaySize];
```
