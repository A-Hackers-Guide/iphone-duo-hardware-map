# `CAFStartupNotificationGate`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _carFirstObservedAt;
@"NSDate" _carReadyAt;
```

## Properties

```
@property (T@"NSDate",&,N,V_carFirstObservedAt) carFirstObservedAt;
@property (T@"NSDate",&,N,V_carReadyAt) carReadyAt;
@property (TB,R,N) shouldSuppress;
```

## Class methods

```
+[CAFStartupNotificationGate fallbackInterval];
+[CAFStartupNotificationGate readyInterval];
```

## Instance methods

```
-[CAFStartupNotificationGate shouldSuppress];
-[CAFStartupNotificationGate markCarObserved];
-[CAFStartupNotificationGate carFirstObservedAt];
-[CAFStartupNotificationGate carReadyAt];
-[CAFStartupNotificationGate clearCar];
-[CAFStartupNotificationGate markCarReady];
-[CAFStartupNotificationGate setCarFirstObservedAt:];
-[CAFStartupNotificationGate setCarReadyAt:];
```
