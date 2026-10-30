# `SBFRemoteBasebandLoggingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"CellularLogging" _cellularLogging;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"CellularLogging",&,N,V_cellularLogging) cellularLogging;
@property (T@"NSHashTable",&,N,V_observers) observers;
```

## Class methods

```
+[SBFRemoteBasebandLoggingManager sharedInstance];
```

## Instance methods

```
-[SBFRemoteBasebandLoggingManager _notifyObservers];
-[SBFRemoteBasebandLoggingManager removeObserver:];
-[SBFRemoteBasebandLoggingManager init];
-[SBFRemoteBasebandLoggingManager addObserver:];
-[SBFRemoteBasebandLoggingManager setObservers:];
-[SBFRemoteBasebandLoggingManager observers];
-[SBFRemoteBasebandLoggingManager cellularLogging];
-[SBFRemoteBasebandLoggingManager isLogCollectionEnabled];
-[SBFRemoteBasebandLoggingManager setCellularLogging:];
```
