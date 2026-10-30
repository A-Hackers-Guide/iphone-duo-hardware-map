# `CAFTestControlSync`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 36 properties, 58 instance methods, 2 class methods

## Properties

```
@property (T@"CAFTestDevRequestNoParamsControl",R,N) testDevRequestNoParamsControl;
@property (T@"CAFTestDevRequestWithReqParamsControl",R,N) testDevRequestWithReqParamsControl;
@property (T@"CAFTestDevRequestWithResParamsControl",R,N) testDevRequestWithResParamsControl;
@property (T@"CAFTestDevRequestWithReqAndResParamsControl",R,N) testDevRequestWithReqAndResParamsControl;
@property (T@"CAFTestAccRequestNoParamsControl",R,N) testAccRequestNoParamsControl;
@property (T@"CAFTestAccRequestWithReqParamsControl",R,N) testAccRequestWithReqParamsControl;
@property (T@"CAFTestAccRequestWithResParamsControl",R,N) testAccRequestWithResParamsControl;
@property (T@"CAFTestAccRequestWithReqAndResParamsControl",R,N) testAccRequestWithReqAndResParamsControl;
@property (TB,R,N) hasTestDevRequestNoParams;
@property (TB,R,N) testDevRequestNoParamsError;
@property (TB,R,N) testDevRequestNoParamsDisabled;
@property (TB,R,N) testDevRequestNoParamsRestricted;
@property (TB,R,N) testDevRequestNoParamsHidden;
@property (TB,R,N) hasTestDevRequestWithReqParams;
@property (TB,R,N) testDevRequestWithReqParamsError;
@property (TB,R,N) testDevRequestWithReqParamsDisabled;
@property (TB,R,N) testDevRequestWithReqParamsRestricted;
@property (TB,R,N) testDevRequestWithReqParamsHidden;
@property (TB,R,N) hasTestDevRequestWithResParams;
@property (TB,R,N) testDevRequestWithResParamsError;
@property (TB,R,N) testDevRequestWithResParamsDisabled;
@property (TB,R,N) testDevRequestWithResParamsRestricted;
@property (TB,R,N) testDevRequestWithResParamsHidden;
@property (TB,R,N) hasTestDevRequestWithReqAndResParams;
@property (TB,R,N) testDevRequestWithReqAndResParamsError;
@property (TB,R,N) testDevRequestWithReqAndResParamsDisabled;
@property (TB,R,N) testDevRequestWithReqAndResParamsRestricted;
@property (TB,R,N) testDevRequestWithReqAndResParamsHidden;
@property (T@?,C,N) testAccRequestNoParamsHandler;
@property (TB,R,N) hasTestAccRequestNoParams;
@property (T@?,C,N) testAccRequestWithReqParamsHandler;
@property (TB,R,N) hasTestAccRequestWithReqParams;
@property (T@?,C,N) testAccRequestWithResParamsHandler;
@property (TB,R,N) hasTestAccRequestWithResParams;
@property (T@?,C,N) testAccRequestWithReqAndResParamsHandler;
@property (TB,R,N) hasTestAccRequestWithReqAndResParams;
```

## Class methods

```
+[CAFTestControlSync serviceIdentifier];
+[CAFTestControlSync observerProtocol];
```

## Instance methods

```
-[CAFTestControlSync removeObserver:];
-[CAFTestControlSync addObserver:];
-[CAFTestControlSync registerObserver:];
-[CAFTestControlSync name];
-[CAFTestControlSync unregisterObserver:];
-[CAFTestControlSync _controlDidUpdate:];
-[CAFTestControlSync hasTestAccRequestNoParams];
-[CAFTestControlSync hasTestAccRequestWithReqAndResParams];
-[CAFTestControlSync hasTestAccRequestWithReqParams];
-[CAFTestControlSync hasTestAccRequestWithResParams];
-[CAFTestControlSync hasTestDevRequestNoParams];
-[CAFTestControlSync hasTestDevRequestWithReqAndResParams];
-[CAFTestControlSync hasTestDevRequestWithReqParams];
-[CAFTestControlSync hasTestDevRequestWithResParams];
-[CAFTestControlSync registeredForTestAccRequestNoParams];
-[CAFTestControlSync registeredForTestAccRequestWithReqAndResParams];
-[CAFTestControlSync registeredForTestAccRequestWithReqParams];
-[CAFTestControlSync registeredForTestAccRequestWithResParams];
-[CAFTestControlSync registeredForTestDevRequestNoParams];
-[CAFTestControlSync registeredForTestDevRequestWithReqAndResParams];
-[CAFTestControlSync registeredForTestDevRequestWithReqParams];
-[CAFTestControlSync registeredForTestDevRequestWithResParams];
-[CAFTestControlSync setTestAccRequestNoParamsHandler:];
-[CAFTestControlSync setTestAccRequestWithReqAndResParamsHandler:];
-[CAFTestControlSync setTestAccRequestWithReqParamsHandler:];
-[CAFTestControlSync setTestAccRequestWithResParamsHandler:];
-[CAFTestControlSync testAccRequestNoParamsControl];
-[CAFTestControlSync testAccRequestNoParamsHandler];
-[CAFTestControlSync testAccRequestWithReqAndResParamsControl];
-[CAFTestControlSync testAccRequestWithReqAndResParamsHandler];
-[CAFTestControlSync testAccRequestWithReqParamsControl];
-[CAFTestControlSync testAccRequestWithReqParamsHandler];
-[CAFTestControlSync testAccRequestWithResParamsControl];
-[CAFTestControlSync testAccRequestWithResParamsHandler];
-[CAFTestControlSync testDevRequestNoParamsControl];
-[CAFTestControlSync testDevRequestNoParamsDisabled];
-[CAFTestControlSync testDevRequestNoParamsError];
-[CAFTestControlSync testDevRequestNoParamsHidden];
-[CAFTestControlSync testDevRequestNoParamsRestricted];
-[CAFTestControlSync testDevRequestNoParamsWithCompletion:];
-[CAFTestControlSync testDevRequestWithReqAndResParamsControl];
-[CAFTestControlSync testDevRequestWithReqAndResParamsDisabled];
-[CAFTestControlSync testDevRequestWithReqAndResParamsError];
-[CAFTestControlSync testDevRequestWithReqAndResParamsHidden];
-[CAFTestControlSync testDevRequestWithReqAndResParamsRestricted];
-[CAFTestControlSync testDevRequestWithReqAndResParamsWithTestInput5:testInput6:completion:];
-[CAFTestControlSync testDevRequestWithReqParamsControl];
-[CAFTestControlSync testDevRequestWithReqParamsDisabled];
-[CAFTestControlSync testDevRequestWithReqParamsError];
-[CAFTestControlSync testDevRequestWithReqParamsHidden];
-[CAFTestControlSync testDevRequestWithReqParamsRestricted];
-[CAFTestControlSync testDevRequestWithReqParamsWithTestInput1:testInput2:completion:];
-[CAFTestControlSync testDevRequestWithResParamsControl];
-[CAFTestControlSync testDevRequestWithResParamsDisabled];
-[CAFTestControlSync testDevRequestWithResParamsError];
-[CAFTestControlSync testDevRequestWithResParamsHidden];
-[CAFTestControlSync testDevRequestWithResParamsRestricted];
-[CAFTestControlSync testDevRequestWithResParamsWithCompletion:];
```
