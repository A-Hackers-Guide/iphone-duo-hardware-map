# `CAFTestControlAsync`

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
+[CAFTestControlAsync serviceIdentifier];
+[CAFTestControlAsync observerProtocol];
```

## Instance methods

```
-[CAFTestControlAsync removeObserver:];
-[CAFTestControlAsync addObserver:];
-[CAFTestControlAsync registerObserver:];
-[CAFTestControlAsync name];
-[CAFTestControlAsync unregisterObserver:];
-[CAFTestControlAsync _controlDidUpdate:];
-[CAFTestControlAsync hasTestAccRequestNoParams];
-[CAFTestControlAsync hasTestAccRequestWithReqAndResParams];
-[CAFTestControlAsync hasTestAccRequestWithReqParams];
-[CAFTestControlAsync hasTestAccRequestWithResParams];
-[CAFTestControlAsync hasTestDevRequestNoParams];
-[CAFTestControlAsync hasTestDevRequestWithReqAndResParams];
-[CAFTestControlAsync hasTestDevRequestWithReqParams];
-[CAFTestControlAsync hasTestDevRequestWithResParams];
-[CAFTestControlAsync registeredForTestAccRequestNoParams];
-[CAFTestControlAsync registeredForTestAccRequestWithReqAndResParams];
-[CAFTestControlAsync registeredForTestAccRequestWithReqParams];
-[CAFTestControlAsync registeredForTestAccRequestWithResParams];
-[CAFTestControlAsync registeredForTestDevRequestNoParams];
-[CAFTestControlAsync registeredForTestDevRequestWithReqAndResParams];
-[CAFTestControlAsync registeredForTestDevRequestWithReqParams];
-[CAFTestControlAsync registeredForTestDevRequestWithResParams];
-[CAFTestControlAsync setTestAccRequestNoParamsHandler:];
-[CAFTestControlAsync setTestAccRequestWithReqAndResParamsHandler:];
-[CAFTestControlAsync setTestAccRequestWithReqParamsHandler:];
-[CAFTestControlAsync setTestAccRequestWithResParamsHandler:];
-[CAFTestControlAsync testAccRequestNoParamsControl];
-[CAFTestControlAsync testAccRequestNoParamsHandler];
-[CAFTestControlAsync testAccRequestWithReqAndResParamsControl];
-[CAFTestControlAsync testAccRequestWithReqAndResParamsHandler];
-[CAFTestControlAsync testAccRequestWithReqParamsControl];
-[CAFTestControlAsync testAccRequestWithReqParamsHandler];
-[CAFTestControlAsync testAccRequestWithResParamsControl];
-[CAFTestControlAsync testAccRequestWithResParamsHandler];
-[CAFTestControlAsync testDevRequestNoParamsControl];
-[CAFTestControlAsync testDevRequestNoParamsDisabled];
-[CAFTestControlAsync testDevRequestNoParamsError];
-[CAFTestControlAsync testDevRequestNoParamsHidden];
-[CAFTestControlAsync testDevRequestNoParamsRestricted];
-[CAFTestControlAsync testDevRequestNoParamsWithCompletion:];
-[CAFTestControlAsync testDevRequestWithReqAndResParamsControl];
-[CAFTestControlAsync testDevRequestWithReqAndResParamsDisabled];
-[CAFTestControlAsync testDevRequestWithReqAndResParamsError];
-[CAFTestControlAsync testDevRequestWithReqAndResParamsHidden];
-[CAFTestControlAsync testDevRequestWithReqAndResParamsRestricted];
-[CAFTestControlAsync testDevRequestWithReqAndResParamsWithTestInput5:testInput6:completion:];
-[CAFTestControlAsync testDevRequestWithReqParamsControl];
-[CAFTestControlAsync testDevRequestWithReqParamsDisabled];
-[CAFTestControlAsync testDevRequestWithReqParamsError];
-[CAFTestControlAsync testDevRequestWithReqParamsHidden];
-[CAFTestControlAsync testDevRequestWithReqParamsRestricted];
-[CAFTestControlAsync testDevRequestWithReqParamsWithTestInput1:testInput2:completion:];
-[CAFTestControlAsync testDevRequestWithResParamsControl];
-[CAFTestControlAsync testDevRequestWithResParamsDisabled];
-[CAFTestControlAsync testDevRequestWithResParamsError];
-[CAFTestControlAsync testDevRequestWithResParamsHidden];
-[CAFTestControlAsync testDevRequestWithResParamsRestricted];
-[CAFTestControlAsync testDevRequestWithResParamsWithCompletion:];
```
