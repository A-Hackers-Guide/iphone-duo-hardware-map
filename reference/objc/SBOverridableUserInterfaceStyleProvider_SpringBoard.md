# `SBOverridableUserInterfaceStyleProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUserInterfaceStyleObserver`, `SBUserInterfaceStyleProvider`
- 3 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
q _overrideStyle;
@"SBDefaultUserInterfaceStyleProvider" _defaultUserInterfaceStyleProvider;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) currentStyle;
```

## Instance methods

```
-[SBOverridableUserInterfaceStyleProvider currentStyle];
-[SBOverridableUserInterfaceStyleProvider removeObserver:];
-[SBOverridableUserInterfaceStyleProvider init];
-[SBOverridableUserInterfaceStyleProvider addObserver:];
-[SBOverridableUserInterfaceStyleProvider _notifyObserversCurrentStyleChangedWithCompletion:];
-[SBOverridableUserInterfaceStyleProvider setOverrideStyle:completion:];
-[SBOverridableUserInterfaceStyleProvider userInterfaceStyleProvider:didUpdateStyle:preferredAnimationSettings:completion:];
```
