# `SBDefaultUserInterfaceStyleProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUserInterfaceStyleProvider`
- 1 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (Tq,R,N) currentStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDefaultUserInterfaceStyleProvider currentStyle];
-[SBDefaultUserInterfaceStyleProvider removeObserver:];
-[SBDefaultUserInterfaceStyleProvider init];
-[SBDefaultUserInterfaceStyleProvider addObserver:];
-[SBDefaultUserInterfaceStyleProvider _notifyObserversCurrentStyleChanged];
```
