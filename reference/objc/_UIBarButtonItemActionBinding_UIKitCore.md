# `_UIBarButtonItemActionBinding`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
{?="isMonitoring"b1} _flags;
@"NSArray" _barButtonItems;
@? _registerObservers;
@? _unregisterObservers;
```

## Properties

```
@property (T@"NSArray",&,N,V_barButtonItems) barButtonItems;
@property (T@?,C,N,V_registerObservers) registerObservers;
@property (T@?,C,N,V_unregisterObservers) unregisterObservers;
```

## Instance methods

```
-[_UIBarButtonItemActionBinding startMonitoring];
-[_UIBarButtonItemActionBinding barButtonItems];
-[_UIBarButtonItemActionBinding stopMonitoring];
-[_UIBarButtonItemActionBinding setBarButtonItems:];
-[_UIBarButtonItemActionBinding _update:];
-[_UIBarButtonItemActionBinding initWithBarButtonItems:registerObservers:unregisterObservers:];
-[_UIBarButtonItemActionBinding registerObservers];
-[_UIBarButtonItemActionBinding setRegisterObservers:];
-[_UIBarButtonItemActionBinding setUnregisterObservers:];
-[_UIBarButtonItemActionBinding unregisterObservers];
```
