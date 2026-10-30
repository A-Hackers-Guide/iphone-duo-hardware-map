# `CAFTestControlEvent`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 16 properties, 29 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTestDevEventNoParamsControl",R,N) testDevEventNoParamsControl;
@property (T@"CAFTestDevEventWithParamsControl",R,N) testDevEventWithParamsControl;
@property (T@"CAFTestAccEventNoParamsControl",R,N) testAccEventNoParamsControl;
@property (T@"CAFTestAccEventWithParamsControl",R,N) testAccEventWithParamsControl;
@property (TB,R,N) hasTestDevEventNoParams;
@property (TB,R,N) testDevEventNoParamsError;
@property (TB,R,N) testDevEventNoParamsDisabled;
@property (TB,R,N) testDevEventNoParamsRestricted;
@property (TB,R,N) testDevEventNoParamsHidden;
@property (TB,R,N) hasTestDevEventWithParams;
@property (TB,R,N) testDevEventWithParamsError;
@property (TB,R,N) testDevEventWithParamsDisabled;
@property (TB,R,N) testDevEventWithParamsRestricted;
@property (TB,R,N) testDevEventWithParamsHidden;
@property (TB,R,N) hasTestAccEventNoParams;
@property (TB,R,N) hasTestAccEventWithParams;
```

## Class methods

```
+[CAFTestControlEvent serviceIdentifier];
+[CAFTestControlEvent observerProtocol];
```

## Instance methods

```
-[CAFTestControlEvent removeObserver:];
-[CAFTestControlEvent addObserver:];
-[CAFTestControlEvent registerObserver:];
-[CAFTestControlEvent name];
-[CAFTestControlEvent unregisterObserver:];
-[CAFTestControlEvent _controlDidNotify:withValue:];
-[CAFTestControlEvent _controlDidUpdate:];
-[CAFTestControlEvent hasTestAccEventNoParams];
-[CAFTestControlEvent hasTestAccEventWithParams];
-[CAFTestControlEvent hasTestDevEventNoParams];
-[CAFTestControlEvent hasTestDevEventWithParams];
-[CAFTestControlEvent registeredForTestAccEventNoParams];
-[CAFTestControlEvent registeredForTestAccEventWithParams];
-[CAFTestControlEvent registeredForTestDevEventNoParams];
-[CAFTestControlEvent registeredForTestDevEventWithParams];
-[CAFTestControlEvent testAccEventNoParamsControl];
-[CAFTestControlEvent testAccEventWithParamsControl];
-[CAFTestControlEvent testDevEventNoParams];
-[CAFTestControlEvent testDevEventNoParamsControl];
-[CAFTestControlEvent testDevEventNoParamsDisabled];
-[CAFTestControlEvent testDevEventNoParamsError];
-[CAFTestControlEvent testDevEventNoParamsHidden];
-[CAFTestControlEvent testDevEventNoParamsRestricted];
-[CAFTestControlEvent testDevEventWithParamsControl];
-[CAFTestControlEvent testDevEventWithParamsDisabled];
-[CAFTestControlEvent testDevEventWithParamsError];
-[CAFTestControlEvent testDevEventWithParamsHidden];
-[CAFTestControlEvent testDevEventWithParamsRestricted];
-[CAFTestControlEvent testDevEventWithParamsWithTestInput9:testInput10:];
```
